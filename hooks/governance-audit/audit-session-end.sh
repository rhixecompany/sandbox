#!/usr/bin/env bash
# governance-audit: audit-session-end.sh
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

log_dir="C:/Users/Alexa/AppData/Local/hermes/logs/hermes/governance"
mkdir -p "${log_dir}"
log_file="${log_dir}/${session_id}.jsonl"

cat <<EOF >> "${log_file}"
{"event": "session_end", "session_id": "${session_id}", "timestamp": "${timestamp}", "duration_ms": ${duration_ms}, "turns": ${turns}, "tokens_in": ${tokens_in}, "tokens_out": ${tokens_out}, "status": "${status}", "checks": ["prompt_injection", "secret_leak", "policy_compliance"]}
EOF

log_info "Governance audit session end logged: ${session_id} (${duration_ms}ms, ${turns} turns)"
