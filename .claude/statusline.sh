#!/bin/bash

# Fixed Status Line Script that reads live data from Claude Code session files
# Works around the issue of Claude Code not sending JSON via stdin

set -euo pipefail

# Color and styling constants
readonly RESET='\033[0m'
readonly DIM='\033[2m'
readonly BOLD='\033[1m'
readonly ITALIC='\033[3m'

# Foreground colors
readonly RED='\033[31m'
readonly GREEN='\033[32m'
readonly YELLOW='\033[33m'
readonly BLUE='\033[34m'
readonly MAGENTA='\033[35m'
readonly CYAN='\033[36m'
readonly WHITE='\033[37m'
readonly GRAY='\033[90m'

# Background colors for widgets
readonly BG_BLUE='\033[44m'
readonly BG_MAGENTA='\033[45m'
readonly BG_CYAN='\033[46m'
readonly BG_DARK_BLUE='\033[48;5;25m'  # Brighter blue
readonly BG_PURPLE='\033[48;5;54m'
readonly BG_DARK_CYAN='\033[48;5;31m'  # Better contrast cyan
readonly BG_DARK_MAGENTA='\033[48;5;89m'
readonly BG_DARK_RED='\033[48;5;52m'

# Box drawing removed - no framing needed

# Get latest session file
# Dynamically find session file based on current project directory
project_name=$(basename "$(git rev-parse --show-toplevel 2>/dev/null || pwd)")
session_file=$(ls -t /home/codespace/.claude/projects/-workspaces-${project_name}/*.jsonl 2>/dev/null | head -1)

# Extract live data from session file if it exists
context_used="0"
context_total="200000"
last_action="Ready"
model_name="Claude"

if [ -n "$session_file" ] && [ -f "$session_file" ]; then
    # Get the last entry for context and other info
    last_entry=$(tail -10 "$session_file" | grep '"usage":' | tail -1)

    if [ -n "$last_entry" ]; then
        # Context is the cache_read_input_tokens from the last entry
        cache_read=$(echo "$last_entry" | jq -r '.message.usage.cache_read_input_tokens // 0' 2>/dev/null || echo "0")
        if [ "$cache_read" -gt 0 ]; then
            context_used=$(awk "BEGIN { printf \"%.1f\", $cache_read / 1000 }" 2>/dev/null || echo "0")
        fi

        # Extract model name
        model_raw=$(echo "$last_entry" | jq -r '.message.model // "claude"' 2>/dev/null)
        if [ -n "$model_raw" ] && [ "$model_raw" != "null" ]; then
            # Simplify model name (e.g., claude-opus-4-1-20250805 -> Opus 4.1)
            case "$model_raw" in
                *opus*) model_name="Opus 4.1" ;;
                *sonnet*) model_name="Sonnet" ;;
                *haiku*) model_name="Haiku" ;;
                *) model_name="Claude" ;;
            esac
        fi

        # Check message type and tool use for better action description
        msg_type=$(echo "$last_entry" | jq -r '.type // ""' 2>/dev/null)
        tool_name=$(echo "$last_entry" | jq -r '.message.content[0].name // ""' 2>/dev/null)

        # Determine action based on type and tool
        if [ "$msg_type" = "assistant" ]; then
            if [ -n "$tool_name" ] && [ "$tool_name" != "null" ]; then
                # Show tool name (truncated if needed)
                case "$tool_name" in
                    "Bash") last_action="Running bash" ;;
                    "Read") last_action="Reading file" ;;
                    "Edit") last_action="Editing file" ;;
                    "Write") last_action="Writing file" ;;
                    "MultiEdit") last_action="Multi-editing" ;;
                    "Grep") last_action="Searching" ;;
                    "TodoWrite") last_action="Managing todos" ;;
                    *)
                        if [ ${#tool_name} -gt 12 ]; then
                            last_action="${tool_name:0:12}..."
                        else
                            last_action="$tool_name"
                        fi
                        ;;
                esac
            else
                last_action="Responding"
            fi
        elif [ "$msg_type" = "user" ]; then
            last_action="Processing"
        else
            last_action="Active"
        fi
    fi
fi

# Get system info
user=$(whoami 2>/dev/null || echo "user")
hostname=$(hostname -s 2>/dev/null || echo "host")
current_dir=$(pwd)

# Calculate relative path
rel_path="/"
repo_root=$(git rev-parse --show-toplevel 2>/dev/null || pwd)
if [[ "$current_dir" == "$repo_root"* ]]; then
    rel_path="${current_dir#$repo_root}"
    if [ -z "$rel_path" ]; then
        rel_path="/"
    fi
fi

# Truncate long paths
if [ ${#rel_path} -gt 25 ]; then
    rel_path="...${rel_path: -22}"
fi

# Get git information
git_branch=""
if git rev-parse --git-dir >/dev/null 2>&1; then
    git_branch=$(git branch --show-current 2>/dev/null || echo "main")
fi

# Get environment versions
node_version=""
python_version=""
if command -v node >/dev/null 2>&1; then
    node_version=$(node --version 2>/dev/null | sed 's/v//')
fi
if command -v python3 >/dev/null 2>&1; then
    python_version=$(python3 --version 2>/dev/null | cut -d' ' -f2 | cut -d'.' -f1-2)
fi

# Calculate context percentage (context_total is in k, context_used is in k)
context_percentage="0"
if [ -n "$context_used" ] && [ "$context_used" != "0" ]; then
    # Both values are already in k units
    context_total_k=200  # 200k is the default
    context_percentage=$(awk "BEGIN { printf \"%.1f\", ($context_used * 100) / $context_total_k }" 2>/dev/null || echo "0")
fi

# No framing needed - removed helper functions

# Build the status line (no borders)

# Line 1: User, path, git, model
line1=""
line1="${line1}${BG_DARK_BLUE}${BOLD}${WHITE} 💻 ${user}@${hostname} ${RESET}"
line1="${line1} ${DIM}|${RESET} ${BG_DARK_CYAN}${BOLD}${WHITE} 🔧 ${rel_path} ${RESET}"

if [ -n "$git_branch" ]; then
    git_display="$git_branch"
    if [ ${#git_display} -gt 8 ]; then
        git_display="${git_display:0:8}"
    fi
    line1="${line1} ${DIM}|${RESET} ${BG_PURPLE}${BOLD}${WHITE} 🌿 ${git_display} ${RESET}"
fi

line1="${line1} ${DIM}|${RESET} ${BG_DARK_MAGENTA}${BOLD}${WHITE} 🧠 ${model_name} ${RESET}"

printf "%b\n" "$line1"

# Line 2: Environment, context, tokens, status
line2=""
first_item=true

if [ -n "$node_version" ]; then
    line2="${line2}${BG_DARK_MAGENTA}${BOLD}${WHITE} 📗 ${node_version} ${RESET}"
    first_item=false
fi

if [ -n "$python_version" ]; then
    if [ "$first_item" = false ]; then
        line2="${line2} ${DIM}|${RESET} "
    fi
    line2="${line2}${BG_DARK_BLUE}${BOLD}${WHITE} 🐍 ${python_version} ${RESET}"
    first_item=false
fi

# Context widget (show 200k as the total)
if [ "$first_item" = false ]; then
    line2="${line2} ${DIM}|${RESET} "
fi
line2="${line2}${BG_PURPLE}${BOLD}${WHITE} 📊 ${context_used}k/200k (${context_percentage}%) ${RESET}"

# Status widget
line2="${line2} ${DIM}|${RESET} ${BG_DARK_RED}${BOLD}${WHITE} 💬 ${last_action} ${RESET}"

printf "%b" "$line2"