#!/usr/bin/env bash
# session-logger: log-session-end.sh
# Legacy script mapped to canonical on_session_end event.
set -euo pipefail

HOOK_DIR="$( cd "$( dirname "${BASH_SOURCE[0]}" )" &>/dev/null && pwd -W )"
HOOK_DIR="${HOOK_DIR//\\//}"
readonly LIB_DIR="${HOOK_DIR}/../lib.sh"
source "${LIB_DIR}"

payload=$(cat)
session_id=$(echo "$payload" | jq -r '.session_id // "unknown"')
timestamp=$(echo "$payload" | jq -r '.timestamp // ""')
if [[ -z "${timestamp}" ]]; then timestamp=$(date -u +"%Y-%m-%d %H:%M:%S"); fi
duration_ms=$(echo "$payload" | jq -r '.duration_ms // 0')
turns=$(echo "$payload" | jq -r '.turns // 0')
tokens_in=$(echo "$payload" | jq -r '.tokens_in // 0')
tokens_out=$(echo "$payload" | jq -r '.tokens_out // 0')
status=$(echo "$payload" | jq -r '.status // "unknown"')
working_dir=$(echo "$payload" | jq -r '.working_dir // ""')
exit_code=$(echo "$payload" | jq -r '.exit_code // ""')
duration_seconds=$(echo "$payload" | jq -r '.duration_seconds // ""')

log_dir="C:/Users/Alexa/AppData/Local/hermes/logs/sessions"
mkdir -p "${log_dir}"
log_file="${log_dir}/${session_id}.jsonl"

cat <<EOF >> "${log_file}"
{"event": "session_end", "session_id": "${session_id}", "timestamp": "${timestamp}", "duration_ms": ${duration_ms}, "duration_seconds": ${duration_seconds}, "turns": ${turns}, "tokens_in": ${tokens_in}, "tokens_out": ${tokens_out}, "status": "${status}", "working_dir": "${working_dir}", "exit_code": ${exit_code}}
EOF

log_info "Session end logged: ${session_id} (${duration_ms}ms, ${turns} turns)"
