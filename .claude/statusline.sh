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

# Unicode box drawing and symbols
readonly BOX_H='─'
readonly BOX_V='│'
readonly BOX_TL='┌'
readonly BOX_TR='┐'
readonly BOX_BL='└'
readonly BOX_BR='┘'
readonly BOX_L='├'
readonly BOX_R='┤'
readonly WIDGET_L='┤'
readonly WIDGET_R='├'

# Get latest session file
session_file=$(ls -t /home/codespace/.claude/projects/-workspaces-ioun-ai/*.jsonl 2>/dev/null | head -1)

# Extract live data from session file if it exists
tokens_used="0"
context_used="0"
context_total="200000"
last_action="Ready"
model_name="Claude"

if [ -n "$session_file" ] && [ -f "$session_file" ]; then
    # Get the last entry with usage data
    last_entry=$(tail -10 "$session_file" | grep '"usage":' | tail -1)

    if [ -n "$last_entry" ]; then
        # Extract token counts using jq for proper JSON parsing
        output_tokens=$(echo "$last_entry" | jq -r '.message.usage.output_tokens // 0' 2>/dev/null || echo "0")
        input_tokens=$(echo "$last_entry" | jq -r '.message.usage.input_tokens // 0' 2>/dev/null || echo "0")
        cache_read=$(echo "$last_entry" | jq -r '.message.usage.cache_read_input_tokens // 0' 2>/dev/null || echo "0")

        # Calculate total tokens (output + input + cache)
        total_tokens=$((output_tokens + input_tokens + cache_read))
        if [ "$total_tokens" -gt 0 ]; then
            tokens_used=$(awk "BEGIN { printf \"%.1fk\", $total_tokens / 1000 }" 2>/dev/null || echo "0k")
        fi

        # Context is essentially the cache_read_input_tokens
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
if [[ "$current_dir" == "/workspaces/ioun-ai"* ]]; then
    rel_path="${current_dir#/workspaces/ioun-ai}"
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

# Frame width calculation - fixed at 90 for consistent display
frame_width=90

# Generate horizontal border
border_length=$((frame_width - 2))
horizontal_border=""
i=0
while [ $i -lt $border_length ]; do
    horizontal_border="${horizontal_border}${BOX_H}"
    i=$((i + 1))
done

# Helper function to frame a widget
frame_widget() {
    local widget_content="$1"
    printf "${DIM}${WIDGET_L}${RESET}%s${DIM}${WIDGET_R}${RESET}" "$widget_content"
}

# Helper function to print a line with padding
print_frame_line() {
    local content="$1"
    local target_width=$((frame_width - 2))

    printf "${BOLD}${BOX_V}${RESET}"
    printf "%b" "$content"

    # Calculate visible length more accurately
    # Remove ANSI escape sequences
    local clean_content=$(echo "$content" | sed 's/\x1b\[[0-9;]*m//g')

    # Count regular characters
    local char_length=$(echo -n "$clean_content" | wc -c)

    # Count emojis (each takes 2 spaces in terminal)
    local emoji_count=$(echo "$clean_content" | grep -o '[🔧💻🌿🧠⚡📊🔢💬🐳☁️📗🐍]' | wc -l 2>/dev/null || echo 0)

    # Count widget frames (each ┤ and ├ takes 1 space)
    local frame_count=$(echo "$clean_content" | grep -o '[┤├]' | wc -l 2>/dev/null || echo 0)

    # Calculate actual visible length
    # Regular chars + (emojis * 2) + frames - spaces around widgets
    local visible_length=$((char_length + emoji_count - 2))

    # Calculate padding
    local padding_needed=$((target_width - visible_length))
    if [ $padding_needed -lt 0 ]; then
        padding_needed=1
    fi

    printf "%*s" "$padding_needed" ""
    printf "${BOLD}${BOX_V}${RESET}"
}

# Build the status line

# Top border
printf "${BOLD}${BOX_TL}${horizontal_border}${BOX_TR}${RESET}\n"

# Line 1: User, path, git, model
line1=" "
line1="${line1}$(frame_widget "💻 ${CYAN}${user}${RESET}${DIM}@${hostname}${RESET}") "
line1="${line1}$(frame_widget "🔧 ${BLUE}${rel_path}${RESET}") "

if [ -n "$git_branch" ]; then
    git_display="$git_branch"
    if [ ${#git_display} -gt 8 ]; then
        git_display="${git_display:0:8}"
    fi
    line1="${line1}$(frame_widget "🌿 ${GREEN}${git_display}${RESET}") "
fi

line1="${line1}$(frame_widget "🧠 ${MAGENTA}${model_name}${RESET}")  "

print_frame_line "$line1"
printf "\n"

# Middle separator
printf "${BOLD}${BOX_L}${horizontal_border}${BOX_R}${RESET}\n"

# Line 2: Environment, context, tokens, status
line2=" "

if [ -n "$node_version" ]; then
    line2="${line2}$(frame_widget "📗 ${GREEN}${node_version}${RESET}") "
fi

if [ -n "$python_version" ]; then
    line2="${line2}$(frame_widget "🐍 ${YELLOW}${python_version}${RESET}") "
fi

# Context widget (show 200k as the total)
context_widget="📊 ${context_used}k/200k ${WHITE}(${context_percentage}%)${RESET}"
line2="${line2}$(frame_widget "${context_widget}") "

# Token widget
line2="${line2}$(frame_widget "🔢 ${GRAY}${tokens_used} tokens${RESET}") "

# Status widget
line2="${line2}$(frame_widget "💬 ${last_action}")  "

print_frame_line "$line2"
printf "\n"

# Bottom border
printf "${BOLD}${BOX_BL}${horizontal_border}${BOX_BR}${RESET}"