#!/usr/bin/env bash
# Hermes Hooks Shared Library
# Source this in hooks: source "${HOOKS_LIB:-$(dirname "$0")/lib.sh}"

set -euo pipefail

# Add common tool paths not in default bash -c PATH
export PATH="$PATH:/c/ProgramData/chocolatey/bin:/usr/bin:/c/Program Files/Git/usr/bin"

# JSON escaping - single-pass parameter substitution (from superpowers best practice)
# Orders of magnitude faster than character-by-character loops
escape_for_json() {
    local s="$1"
    s="${s//\\/\\\\}"
    s="${s//\"/\\\"}"
    s="${s//$'\n'/\\n}"
    s="${s//$'\r'/\\r}"
    s="${s//$'\t'/\\t}"
    printf '%s' "$s"
}

# Get current ISO timestamp
iso_timestamp() {
    date -Iseconds
}

# Get hook directory (resolves symlinks)
hook_dir() {
    cd "$(dirname "$0")" && pwd
}

# Ensure log directory exists
ensure_log_dir() {
    local dir="${1:-${HOME}/AppData/Local/hermes/logs}"
    mkdir -p "$dir"
}

# Write JSONL entry to log file
log_jsonl() {
    local file="$1"
    shift
    local json
    json=$(jq -n "$@")
    echo "$json" >> "$file"
}

# Check if running in Hermes context (env vars set)
is_hermes_context() {
    [ -n "${HERMES_SESSION_ID:-}" ] || [ -n "${HERMES_PROFILE:-}" ] || [ -n "${HERMES_MODEL:-}" ]
}

# Extract session metadata from stdin/input
extract_session_meta() {
    local input="$1"
    local session_id profile model
    session_id=$(echo "$input" | jq -r '.session_id // "unknown"' 2>/dev/null || echo "unknown")
    profile=$(echo "$input" | jq -r '.profile // "default"' 2>/dev/null || echo "default")
    model=$(echo "$input" | jq -r '.model // "unknown"' 2>/dev/null || echo "unknown")
    printf '%s|%s|%s' "$session_id" "$profile" "$model"
}

# Portable line reversal (replaces tac)
reverse_lines() {
    awk '{lines[NR]=$0} END {for(i=NR;i>=1;i--) print lines[i]}'
}

# Safe git commit if file changed
git_commit_if_changed() {
    local repo_root="$1"
    local file="$2"
    local message="$3"
    if [ -d "$repo_root/.git" ]; then
        cd "$repo_root" || return 0
        if git status --porcelain | grep -q "$file"; then
            git add "$file"
            git commit -m "$message" >/dev/null 2>&1 || true
        fi
    fi
}