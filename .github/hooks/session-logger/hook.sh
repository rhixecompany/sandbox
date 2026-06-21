#!/usr/bin/env bash
set -euo pipefail

# Session Logger Hook - Unified entry point for session lifecycle events
# Events: on_session_start, on_session_end, pre_llm_call
# Logs structured JSONL to ~/AppData/Local/hermes/logs/sessions/

# Source shared library
source "$(dirname "$0")/../lib.sh"

LOG_DIR="${HOME}/AppData/Local/hermes/logs/sessions"
REPORT_PATH="${HOME}/Desktop/SandBox/SESSION_REPORT.md"
ensure_log_dir "$LOG_DIR"

# Parse stdin input for session metadata
INPUT="$(cat)"
SESSION_ID="${HERMES_SESSION_ID:-$(echo "$INPUT" | jq -r '.session_id // "unknown"' 2>/dev/null || echo "unknown")}"
PROFILE="${HERMES_PROFILE:-$(echo "$INPUT" | jq -r '.profile // "default"' 2>/dev/null || echo "default")}"
MODEL="${HERMES_MODEL:-$(echo "$INPUT" | jq -r '.model // "unknown"' 2>/dev/null || echo "unknown")}"
TIMESTAMP="$(iso_timestamp)"

# Determine event type from hook invocation
EVENT_TYPE="${1:-unknown}"

# Extract summary from input
SUMMARY="$(echo "$INPUT" | jq -r '.summary // .message // .prompt // "no summary"' 2>/dev/null || echo "parse error")"
SUMMARY_ESCAPED="$(escape_for_json "$SUMMARY")"
INPUT_ESCAPED="$(escape_for_json "$INPUT")"

log_event() {
    local event_type="$1"
    local session_id="$2"
    local profile="$3"
    local model="$4"
    local timestamp="$5"
    local summary="$6"
    local input_json="$7"

    log_jsonl "${LOG_DIR}/${session_id}.jsonl" \
        --arg et "$event_type" \
        --arg id "$session_id" \
        --arg profile "$profile" \
        --arg model "$model" \
        --arg ts "$timestamp" \
        --arg summary "$summary" \
        --arg input "$input_json" \
        '{event:$et,session_id:$id,profile:$profile,model:$model,timestamp:$ts,summary:$summary,input:$input}'

    # Append to compact sessions log (for SESSION_REPORT generation)
    local compact_line="${timestamp} | ${event_type} | ${session_id} | ${profile} | ${model} | ${summary}"
    echo "$compact_line" >> "${LOG_DIR}/sessions.log"

    # Also write session_meta.json for audit/verification (overwrite, not append)
    local meta_json
    meta_json=$(jq -n \
        --arg et "$event_type" \
        --arg id "$session_id" \
        --arg profile "$profile" \
        --arg model "$model" \
        --arg ts "$timestamp" \
        --arg summary "$summary" \
        '{event:$et,session_id:$id,profile:$profile,model:$model,timestamp:$ts,summary:$summary}')
    echo "$meta_json" > "${LOG_DIR}/session_meta.json"
}

case "$EVENT_TYPE" in
    on_session_start)
        log_event "session_start" "$SESSION_ID" "$PROFILE" "$MODEL" "$TIMESTAMP" "$SUMMARY_ESCAPED" "$INPUT_ESCAPED"
        ;;
    on_session_end)
        log_event "session_end" "$SESSION_ID" "$PROFILE" "$MODEL" "$TIMESTAMP" "$SUMMARY_ESCAPED" "$INPUT_ESCAPED"
        # Trigger auto-commit hook for SESSION_REPORT update
        if [ -x "${HOME}/AppData/Local/hermes/hooks/session-auto-commit/hook.sh" ]; then
            "${HOME}/AppData/Local/hermes/hooks/session-auto-commit/hook.sh" "$REPORT_PATH"
        fi
        ;;
    pre_llm_call)
        log_event "prompt" "$SESSION_ID" "$PROFILE" "$MODEL" "$TIMESTAMP" "$SUMMARY_ESCAPED" "$INPUT_ESCAPED"
        ;;
    *)
        log_event "unknown" "$SESSION_ID" "$PROFILE" "$MODEL" "$TIMESTAMP" "$SUMMARY_ESCAPED" "$INPUT_ESCAPED"
        ;;
esac

# Output empty JSON for hook protocol compliance
printf '{}'
exit 0