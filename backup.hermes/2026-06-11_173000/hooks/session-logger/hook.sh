#!/usr/bin/env bash
set -euo pipefail

# Skip flag
[[ "${SKIP_LOGGING:-}" == "true" ]] && echo '{"status": "skipped"}' && exit 0

input=$(cat)
event=$(printf '%s' "$input" | jq -r '.event // empty' 2>/dev/null || true)
session_id=$(printf '%s' "$input" | jq -r '.session_id // .sessionId // empty' 2>/dev/null || true)
turn_id=$(printf '%s' "$input" | jq -r '.turn_id // .turnId // empty' 2>/dev/null || true)

case "$event" in
  sessionStart)
    event="on_session_start"
    ;;
  sessionEnd)
    event="on_session_end"
    ;;
  userPromptSubmitted)
    event="pre_llm_call"
    ;;
esac

log_dir=/c/Users/Alexa/AppData/Local/hermes/logs/hermes
mkdir -p "$log_dir"
log_file="$log_dir/session-${session_id:-unknown}.log"

case "$event" in
  on_session_start)
    echo "$(date -Iseconds) SESSION_START ${session_id:-unknown} cwd=$(pwd)" >> "$log_file"
    ;;
  on_session_end)
    duration=$(printf '%s' "$input" | jq -r '.duration_seconds // .duration_ms // empty' 2>/dev/null || true)
    msg_count=$(printf '%s' "$input" | jq -r '.message_count // empty' 2>/dev/null || true)
    tool_calls=$(printf '%s' "$input" | jq -r '.tool_calls // empty' 2>/dev/null || true)
    completed=$(printf '%s' "$input" | jq -r '.completed // empty' 2>/dev/null || true)
    interrupted=$(printf '%s' "$input" | jq -r '.interrupted // empty' 2>/dev/null || true)
    reason=$(printf '%s' "$input" | jq -r '.reason // empty' 2>/dev/null || true)

    details=()
    [[ -n "$duration" ]] && details+=("duration=${duration}")
    [[ -n "$msg_count" ]] && details+=("msgs=${msg_count}")
    [[ -n "$tool_calls" ]] && details+=("tools=${tool_calls}")
    [[ -n "$completed" ]] && details+=("completed=${completed}")
    [[ -n "$interrupted" ]] && details+=("interrupted=${interrupted}")
    [[ -n "$reason" ]] && details+=("reason=${reason}")

    line="$(date -Iseconds) SESSION_END ${session_id:-unknown}"
    if [[ ${#details[@]} -gt 0 ]]; then
      line+=" ${details[*]}"
    fi
    echo "$line" >> "$log_file"
    ;;
  pre_llm_call)
    prompt=$(printf '%s' "$input" | jq -r '.user_message // .userMessage // .prompt // empty' 2>/dev/null || true)
    [[ -z "$prompt" ]] && prompt=$(printf '%s' "$input" | head -c 100)
    prompt=$(printf '%s' "$prompt" | head -c 100)
    echo "$(date -Iseconds) PRE_LLM_CALL ${session_id:-unknown} turn=${turn_id:-unknown}: $prompt..." >> "$log_file"
    ;;
esac

echo '{"status": "ok"}'
