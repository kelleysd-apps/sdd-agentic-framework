#!/usr/bin/env bash
# Protect Governance Files — PreToolUse hook (Write/Edit + Bash), Principle VI/governance.
#
# The model has Write/Edit/Bash access to the very files that govern it — the
# hook scripts, settings.json, the constitution, governance.conf. Left open, a
# model (or a subagent) can soften or delete its own guardrails (observed in the
# wild — Claude Code RFC #45427). This hook makes the governance surface
# self-protecting:
#   - a SUBAGENT (agent_id present) editing a protected path  -> DENY (hard)
#   - the MAIN agent editing a protected path                 -> ASK (human approval,
#                                                                like git mutations)
#   - anything else                                           -> ALLOW
#
# It is NOT airtight (a string gate can't see interpreter/eval indirection — see
# subagent-git-guard's note); it is one layer of defense-in-depth, not a sandbox.
#
# Input:  PreToolUse JSON via stdin (Write/Edit/MultiEdit/NotebookEdit or Bash).
# Output: hookSpecificOutput decision (deny / ask / allow).
set -euo pipefail

SCRIPT_DIR="$(cd "$(dirname "${BASH_SOURCE[0]}")" && pwd)"
# plugins/loom-governance/hooks/scripts -> repo root is 4 up
REPO_ROOT="$(cd "$SCRIPT_DIR/../../../.." && pwd)"

# Shared verdict lib (the L2 "verdict function" seam — see
# .docs/architecture/governance-threat-model.md). Fail OPEN if absent
# (infra-gap posture, matching guard-dangerous-commands).
VERDICT_LIB="$REPO_ROOT/.logic-loom/lib/governance-verdicts.sh"
# shellcheck disable=SC1090
{ [ -f "$VERDICT_LIB" ] && source "$VERDICT_LIB"; } 2>/dev/null || true

INPUT=$(cat)

# jq -> python3 -> grep. The third rung was missing here, exactly as it was in
# subagent-git-guard.sh: on a machine with NEITHER jq nor python3 every json_get
# returned empty, the empty .agent_id read as "main agent", and a SUBAGENT write
# to .claude/settings.json came back ALLOW where it is denied on any normal
# machine. Verified: deny -> allow. That is the hook whose whole job is stopping
# the model from rewriting its own rules, so it failing open is the worst of the
# set. `git-safety-gate.sh` already had this rung and survived the same test.
have_structured_parser() {
  command -v jq >/dev/null 2>&1 || command -v python3 >/dev/null 2>&1
}

json_get() { # jq-path
  if command -v jq >/dev/null 2>&1; then
    printf '%s' "$INPUT" | jq -r "$1 // empty" 2>/dev/null && return
  fi
  if command -v python3 >/dev/null 2>&1; then
    printf '%s' "$INPUT" | python3 -c \
      "import sys,json
d=json.load(sys.stdin)
keys='${1//[.\"]/ }'.split()
v=d
for k in keys:
    v=v.get(k) if isinstance(v,dict) else None
print(v if v is not None else '')" 2>/dev/null && return
  fi
  # Last rung: the raw payload as text. A string gate on JSON, so it cannot see
  # through escaping or nesting — hence the degraded-parse branch below.
  leaf=${1##*.}
  printf '%s' "$INPUT" \
    | grep -oE "\"$leaf\"[[:space:]]*:[[:space:]]*\"[^\"]*\"" \
    | head -1 | sed "s/.*\"$leaf\"[^\"]*\"//; s/\"$//"
}

allow() { printf '{"hookSpecificOutput":{"hookEventName":"PreToolUse","permissionDecision":"allow"}}\n'; exit 0; }
decide() { # deny|ask  reason
  local d="$1" reason="$2" esc
  esc=$(printf '%s' "$reason" | sed 's/\\/\\\\/g; s/"/\\"/g')
  printf '{"hookSpecificOutput":{"hookEventName":"PreToolUse","permissionDecision":"%s","permissionDecisionReason":"%s"}}\n' "$d" "$esc"
  exit 0
}

AGENT_ID="$(json_get '.agent_id' || true)"

# FAIL CLOSED ON A DEGRADED PARSE. With no structured parser we are reading JSON
# with grep, so an empty agent_id is not evidence of the main agent — it is
# evidence we cannot tell. Being wrong this way costs the main agent an approval
# prompt on a governance file, which it already gets. Being wrong the other way
# lets a subagent silently rewrite the rules that constrain it.
if [ -z "$AGENT_ID" ] && ! have_structured_parser; then
  # Keyed on `agent_id` ONLY. `agent_type` was in this list and came out on
  # external review: it can be present for a TOP-LEVEL session, so matching it
  # would classify a main agent as a subagent and deny its legitimate git —
  # trading a silent hole for a silent blockage. `agent_id` is the documented
  # discriminator this hook uses everywhere else, so it is the only honest
  # degraded-mode signal.
  case "$INPUT" in
    *'"agent_id"'*) AGENT_ID="unknown-degraded-parse" ;;
  esac
fi
TOOL="$(json_get '.tool_name' || true)"

# Protected governance surface (repo-root-relative path prefixes). Delegates to
# the shared verdict lib (single, conformance-tested source of the protected
# set); the inline case below is the fail-open fallback when the lib is absent.
#
# The lib's set is the built-in FLOOR plus any ADDITIVE `protected_paths` entries
# in governance.conf (see the invariant block in governance-verdicts.sh: config
# can only add, the floor can never be removed). The inline fallback below
# reproduces only the floor — it is a last resort for a missing lib, and by
# construction it can be a SUBSET of the real set, never a superset. That is
# consistent with this hook's documented fail-open-on-infra-gap posture: a fork
# whose extra paths matter should notice the lib is gone, not rely on a duplicate
# config parser here.
is_protected() { # rel_path -> 0 if protected
  if declare -f loom_path_is_protected >/dev/null 2>&1; then
    loom_path_is_protected "$1"; return
  fi
  case "$1" in
    .claude/hooks/*|.claude/hooks \
    |.claude/settings.json|.claude/settings.local.json \
    |.logic-loom/config/governance.conf \
    |.logic-loom/memory/constitution.md \
    |.logic-loom/lib/governance-verdicts.sh|.logic-loom/lib/policy.sh \
    |plugins/loom-governance/hooks/*|plugins/loom-governance/hooks \
    |plugins/loom-governance/.claude-plugin/plugin.json) return 0 ;;
  esac
  return 1
}

# The same set as TOKENS for the Bash branch, which substring-matches command
# text rather than asking a yes/no about one path. Same sourcing rule: the lib
# when present (floor + config additions), the floor-only fallback otherwise.
protected_tokens() { # -> one protected path/prefix per line
  if declare -f loom_protected_path_tokens >/dev/null 2>&1; then
    loom_protected_path_tokens; return
  fi
  printf '%s\n' \
    '.claude/hooks' '.claude/settings.json' '.claude/settings.local.json' \
    '.logic-loom/config/governance.conf' '.logic-loom/memory/constitution.md' \
    '.logic-loom/lib/governance-verdicts.sh' '.logic-loom/lib/policy.sh' \
    'plugins/loom-governance/hooks' \
    'plugins/loom-governance/.claude-plugin/plugin.json'
}

# Canonicalize a path and make it repo-root-relative for matching.
rel_of() { # raw_path -> relative path (or raw if outside repo)
  local p="$1" canon
  if command -v python3 >/dev/null 2>&1; then
    canon=$(python3 -c 'import os,sys; print(os.path.realpath(sys.argv[1]))' "$p" 2>/dev/null)
  fi
  [ -n "${canon:-}" ] || canon=$(printf '%s' "$p" | sed 's://*:/:g')
  case "$canon" in
    "$REPO_ROOT"/*) printf '%s' "${canon:${#REPO_ROOT}+1}" ;;
    /*)             printf '%s' "$canon" ;;   # absolute, outside repo
    *)              printf '%s' "$canon" ;;   # already relative
  esac
}

gate() { # rel_path  verb-desc
  is_protected "$1" || return 0
  if [ -n "$AGENT_ID" ]; then
    decide deny "Governance file '$1' may NOT be modified by a subagent ('$(json_get '.agent_type')'). The hooks/constitution/settings that enforce governance are main-agent + explicit-user-approval only. Return the proposed change to the main agent."
  else
    decide ask "About to modify a GOVERNANCE file: '$1'. This changes the rules that enforce the constitution (hooks/settings/constitution/governance.conf). Approve only if you intend to change governance itself."
  fi
}

# LOOM-0044. The degraded-parse branch above is restrictive about WHO is calling
# but this dispatch was permissive about WHAT they are doing: an empty extraction
# fell through to an explicit `allow`. With no structured parser we are reading
# JSON with grep, so an empty value is NOT evidence the field is absent — it is
# evidence we cannot read it, and "I cannot tell what this writes" must not
# authorize a write to the governance surface.
#
# SCOPE, stated honestly because an external reviewer pushed on exactly this:
# it closes the EMPTY case only. A grep rung keys on the last dot-segment, so a
# WRONGLY-EXTRACTED NON-EMPTY value (`.tool_input.command` aliasing a nested
# `.foo.command`) is still taken at face value. That residual is real, is NOT
# fixed here, and is recorded in the threat model and the backlog rather than
# papered over — closing it means not making security decisions from grep at all.
undetermined_target() { # verb-desc
  if [ -n "$AGENT_ID" ]; then
    decide deny "Cannot determine the target of this $1: neither jq nor python3 is on PATH, so the governance hook is reading its payload with grep and got no value. A subagent is denied rather than allowed on an unreadable payload. Install jq or python3 (the adopt README lists it as a session-time requirement) and retry."
  else
    decide ask "Cannot determine the target of this $1: neither jq nor python3 is on PATH, so the governance hook cannot read its own payload and cannot tell whether this touches the governance surface. This is a hook-health problem, not a policy decision — install jq or python3 to restore normal gating."
  fi
}

case "$TOOL" in
  Write|Edit|MultiEdit|NotebookEdit)
    FP="$(json_get '.tool_input.file_path' || true)"
    [ -z "$FP" ] && FP="$(json_get '.tool_input.notebook_path' || true)"
    if [ -z "$FP" ]; then
      if have_structured_parser; then allow; else undetermined_target "write"; fi
    fi
    gate "$(rel_of "$FP")" "write"
    ;;
  Bash)
    CMD="$(json_get '.tool_input.command' || true)"
    if [ -z "$CMD" ]; then
      if have_structured_parser; then allow; else undetermined_target "command"; fi
    fi
    # Only MUTATING bash that TARGETS a protected path is gated. A read-only
    # command that merely MENTIONS a governance path (ls / find / cat / head /
    # grep / wc / stat / file …) must pass — an adversarial reviewer had a plain
    # `find plugins/loom-governance/hooks` denied because the old matcher looked
    # for a mutation shape ANYWHERE in the line (a bare ">" matched the
    # `2>/dev/null` of a read; "chmod"/"truncate" matched unanchored).
    #
    # Two anchored signals now, evaluated per shell segment (segments start at a
    # command position, so the command WORD is identifiable):
    #   1. the segment's command word is a mutator (tee/dd of=/sed -i/rm/mv/
    #      truncate/chmod/chown/install) AND the segment mentions a protected path
    #   2. a REDIRECTION TARGET (> / >>) in the segment is a protected path
    # The gated set is unchanged; only the false positives are gone.
    gate_bash() { # protected-token
      if [ -n "$AGENT_ID" ]; then
        decide deny "Subagent ('$(json_get '.agent_type')') may not modify governance file '$1' via Bash. Governance changes are main-agent + user-approval only."
      else
        decide ask "Bash command appears to MODIFY a governance path ('$1'). Approve only if you intend to change governance itself. Command: $CMD"
      fi
    }

    # Command word of a segment, path-stripped; skips VAR=value assignments and
    # sudo/env-style prefix words.
    seg_cmd_word() { # segment -> command word (may be empty)
      local s="$1" tok
      while :; do
        s="${s#"${s%%[![:space:]]*}"}"
        [ -n "$s" ] || { printf ''; return 0; }
        tok="${s%%[[:space:]]*}"
        case "${tok##*/}" in
          *=*|sudo|env|command|nohup|nice|time|exec|xargs|stdbuf|ionice) ;;
          -*) ;;
          *) printf '%s' "${tok##*/}"; return 0 ;;
        esac
        s="${s#"$tok"}"
      done
    }

    seg_is_mutator() { # segment -> 0 if its command word writes files
      case "$(seg_cmd_word "$1")" in
        tee|truncate|chmod|chown|install|rm|mv) return 0 ;;
        # LOOM-0059. These four were absent and a subagent could overwrite any
        # governance file with them. `ln` is the worst of the four: it does not
        # just overwrite once, it repoints the path OUTSIDE the repo, and
        # rel_of() canonicalizes with realpath, so every SUBSEQUENT Write/Edit
        # to that path then resolves outside $REPO_ROOT and is allowed.
        cp|ln|patch|rsync) return 0 ;;
        # Archive/fetch tools that write a named target. Flagged by the
        # Antigravity review as still-open after cp/ln/patch/rsync.
        tar|unzip) return 0 ;;
        # `find <dir> -delete` and `find ... -exec rm {} +` mutate without any
        # mutator command word of their own.
        find) printf '%s' "$1" | grep -qE '(^|[[:space:]])-(delete|exec|execdir)([[:space:]]|$)' && return 0 ;;
        # Short (-o) and long (--output=) forms both name a write target. The
        # earlier pattern only matched the short form because `[a-zA-Z]*` cannot
        # cross the second dash of a long option.
        curl) printf '%s' "$1" | grep -qE '(^|[[:space:]])(-[a-zA-Z]*[oO]|--output|--remote-name)([[:space:]]|=|$)' && return 0 ;;
        wget) printf '%s' "$1" | grep -qE '(^|[[:space:]])(-[a-zA-Z]*O|--output-document)([[:space:]]|=|$)' && return 0 ;;
        dd)  printf '%s' "$1" | grep -qE '(^|[[:space:]])of=' && return 0 ;;
        sed) printf '%s' "$1" | grep -qE '(^|[[:space:]])-i' && return 0 ;;
      esac
      return 1
    }

    seg_redirect_targets() { # segment -> one redirection target per line
      printf '%s' "$1" \
        | grep -oE '>>?[[:space:]]*[^[:space:]<>|;&]+' \
        | sed -e 's/^>>*//' -e 's/^[[:space:]]*//'
    }

    # LOOM-0069. The Write/Edit branch canonicalizes with rel_of(); this branch
    # used to substring-match the RAW segment text, so three trivial spellings
    # walked straight past it: `.claude/./settings.json`, `a/../settings.json`,
    # and `cd .claude && rm settings.json` (the `cd` splits the path off the
    # mutating segment entirely). Normalize lexically — normpath does NOT touch
    # the filesystem, so this stays a pure text decision and cannot be fooled by
    # a symlink that does not exist yet.
    norm_path() { # raw token -> lexically normalized
      local out=""
      if command -v python3 >/dev/null 2>&1; then
        out=$(python3 -c 'import os,sys; print(os.path.normpath(sys.argv[1]))' "$1" 2>/dev/null)
      fi
      if [ -z "$out" ]; then
        # No python3. Collapse //, /./ and one-level seg/../ LEXICALLY, looping
        # until stable. Without this the degraded path left `a/../b` unresolved,
        # which is weaker than the pre-fix behaviour for that spelling.
        out=$(printf '%s' "$1" | sed -e 's://*:/:g' -e 's:/\./:/:g' -e 's:^\./::')
        _np_prev=""
        while [ "$out" != "$_np_prev" ]; do
          _np_prev="$out"
          out=$(printf '%s' "$out" | sed -e 's:[^/][^/]*/\.\./::g' -e 's:^\./::')
        done
      fi
      printf '%s' "$out"
    }

    # Does this segment name $prot, in ANY spelling, given the cwd a preceding
    # `cd` established? Compares normalized candidates, not raw substrings.
    seg_names_prot() { # segment prot cd_prefix -> 0 if it does
      local seg="$1" prot="$2" cdp="$3" tok cand
      for tok in $seg; do
        [ -n "$tok" ] || continue
        # Strip a key= prefix BEFORE discarding options. `dd of=<path>` and
        # `curl --output=<path>` both carry the target after an `=`; doing the
        # `-*` skip first threw the long-option form away with the flag.
        case "$tok" in
          *=*) tok="${tok#*=}"; [ -n "$tok" ] || continue ;;
          -*)  continue ;;
        esac
        cand="$tok"
        case "$cand" in
          /*) ;;
          *) [ -n "$cdp" ] && cand="$cdp/$cand" ;;
        esac
        cand="$(norm_path "$cand")"
        case "$cand" in
          "$prot"|"$prot"/*) return 0 ;;
        esac
        # keep the old raw-substring behaviour as a floor: normalization must
        # only ever ADD coverage, never remove a case that used to be caught.
        case "$tok" in *"$prot"*) return 0 ;; esac
      done
      return 1
    }

    # Token list comes from the verdict lib so the Bash branch and the Write/Edit
    # branch protect the SAME set — including any additive governance.conf
    # entries. Computed once, outside the segment loop.
    PROT_TOKENS="$(protected_tokens || true)"

    # LOOM-0069. Unwrap interpreter indirection BEFORE splitting. `bash -c "rm
    # .claude/settings.json"` put the command word `bash` in front, which is not
    # a mutator, so the whole segment was skipped without ever inspecting the
    # inner command. Stripping the wrapper hands the inner command to the same
    # scan — which also means `bash -c "cat .claude/settings.json"` stays an
    # allowed READ, rather than being blanket-gated for being an interpreter.
    SCAN_CMD="$CMD"
    UNWRAP_N=0
    while [ "$UNWRAP_N" -lt 3 ]; do
      case "$SCAN_CMD" in
        *[Bb]ash\ -c\ *|*sh\ -c\ *|*zsh\ -c\ *)
          SCAN_CMD="$(printf '%s' "$SCAN_CMD" \
            | sed -e 's/[a-z]*sh[[:space:]]*-c[[:space:]]*//g' -e "s/[\"']//g")"
          UNWRAP_N=$((UNWRAP_N + 1))
          ;;
        *) break ;;
      esac
    done

    CD_PREFIX=""
    while IFS= read -r SEG; do
      [ -n "$SEG" ] || continue
      # Track `cd <dir>` so a later relative path resolves against it.
      case "$(seg_cmd_word "$SEG")" in cd|pushd) SEG_IS_CD=1 ;; *) SEG_IS_CD=0 ;; esac
      if [ "$SEG_IS_CD" = 1 ]; then
        # -E: BSD sed (stock macOS) has no \| alternation in basic regex, and
        # silently produced a wrong CD_ARG rather than erroring.
        CD_ARG="$(printf '%s' "$SEG" | sed -E -e 's/^[[:space:]]*(cd|pushd)[[:space:]]*//' -e 's/[[:space:]].*$//')"
        case "$CD_ARG" in
          ''|-*) ;;
          /*) CD_PREFIX="$CD_ARG" ;;
          *)  [ -n "$CD_PREFIX" ] && CD_PREFIX="$CD_PREFIX/$CD_ARG" || CD_PREFIX="$CD_ARG" ;;
        esac
        CD_PREFIX="$(norm_path "$CD_PREFIX")"
        continue
      fi
      SEG_MUTATES=0
      seg_is_mutator "$SEG" && SEG_MUTATES=1
      RTARGETS="$(seg_redirect_targets "$SEG" || true)"
      [ "$SEG_MUTATES" = 0 ] && [ -z "$RTARGETS" ] && continue
      while IFS= read -r prot; do
        [ -n "$prot" ] || continue
        if [ "$SEG_MUTATES" = 1 ] && seg_names_prot "$SEG" "$prot" "$CD_PREFIX"; then
          gate_bash "$prot"
        fi
        if [ -n "$RTARGETS" ] && seg_names_prot "$RTARGETS" "$prot" "$CD_PREFIX"; then
          gate_bash "$prot"
        fi
      done <<< "$PROT_TOKENS"
    done <<< "$(printf '%s' "$SCAN_CMD" | tr ';|&(){}`' '\n\n\n\n\n\n\n\n')"
    ;;
esac

allow
