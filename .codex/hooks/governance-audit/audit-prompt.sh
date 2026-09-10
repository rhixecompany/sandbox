#!/usr/bin/env bash
# governance-audit: audit-prompt.sh
# Legacy script mapped to canonical pre_llm_call event.
set -euo pipefail

HOOK_DIR="$( cd "$( dirname "${BASH_SOURCE[0]}" )" &>/dev/null && pwd -W )"
HOOK_DIR="${HOOK_DIR//\\//}"
readonly LIB_DIR="${HOOK_DIR}/../lib.sh"
source "${LIB_DIR}"

payload=$(cat)
session_id=$(echo "$payload" | jq -r '.session_id // "unknown"')
timestamp=$(echo "$payload" | jq -r '.timestamp // ""')
if [[ -z "${timestamp}" ]]; then timestamp=$(date -u +"%Y-%m-%d %H:%M:%S"); fi
model=$(echo "$payload" | jq -r '.model // "unknown"')
provider=$(echo "$payload" | jq -r '.provider // "unknown"')
prompt_length=$(echo "$payload" | jq -r '.prompt_length // 0')
system_prompt_length=$(echo "$payload" | jq -r '.system_prompt_length // 0')
user_message=$(echo "$payload" | jq -r '.user_message // ""' | head -c 180 | sed 's/"/\\"/g')

log_dir="C:/Users/Alexa/AppData/Local/hermes/logs/hermes/governance"
mkdir -p "${log_dir}"
log_file="${log_dir}/${session_id}.jsonl"

cat <<EOF >> "${log_file}"
{"event": "pre_llm_call", "session_id": "${session_id}", "timestamp": "${timestamp}", "model": "${model}", "provider": "${provider}", "prompt_length": ${prompt_length}, "system_prompt_length": ${system_prompt_length}, "user_message": "${user_message}", "checks": ["prompt_injection", "secret_leak", "policy_compliance"]}
EOF

log_info "Governance audit prompt logged: ${session_id} -> ${model} (${prompt_length} chars)"
