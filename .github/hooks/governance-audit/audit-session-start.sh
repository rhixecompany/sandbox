#!/usr/bin/env bash
# governance-audit: audit-session-start.sh
# Legacy script mapped to canonical on_session_start event.
set -euo pipefail

HOOK_DIR="$( cd "$( dirname "${BASH_SOURCE[0]}" )" &>/dev/null && pwd -W )"
HOOK_DIR="${HOOK_DIR//\\//}"
readonly LIB_DIR="${HOOK_DIR}/../lib.sh"
source "${LIB_DIR}"

payload=$(cat)
session_id=$(echo "$payload" | jq -r '.session_id // "unknown"')
timestamp=$(echo "$payload" | jq -r '.timestamp // ""')
if [[ -z "${timestamp}" ]]; then timestamp=$(date -u +"%Y-%m-%d %H:%M:%S"); fi
profile=$(echo "$payload" | jq -r '.profile // "default"')
user=$(echo "$payload" | jq -r '.user // "unknown"')
model=$(echo "$payload" | jq -r '.model // "unknown"')

log_dir="C:/Users/Alexa/AppData/Local/hermes/logs/hermes/governance"
mkdir -p "${log_dir}"
log_file="${log_dir}/${session_id}.jsonl"

cat <<EOF >> "${log_file}"
{"event": "session_start", "session_id": "${session_id}", "timestamp": "${timestamp}", "profile": "${profile}", "user": "${user}", "model": "${model}", "checks": ["prompt_injection", "secret_leak", "policy_compliance"]}
EOF

log_info "Governance audit session start logged: ${session_id}"
