#!/usr/bin/env bash
# session-logger: log-prompt.sh
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
tools_count=$(echo "$payload" | jq -r '.tools_count // 0')
prompt_summary=$(echo "$payload" | jq -r '.prompt // .prompt_summary // ""' | head -c 120 | sed 's/"/\\"/g')
event_type=$(echo "$payload" | jq -r '.event // "pre_llm_call"')
session_end=$(echo "$payload" | jq -r '.session_end // ""')

log_dir="C:/Users/Alexa/AppData/Local/hermes/logs/sessions"
mkdir -p "${log_dir}"
log_file="${log_dir}/${session_id}.jsonl"

cat <<EOF >> "${log_file}"
{"event": "${event_type}", "session_id": "${session_id}", "timestamp": "${timestamp}", "model": "${model}", "provider": "${provider}", "prompt_length": ${prompt_length}, "system_prompt_length": ${system_prompt_length}, "tools_count": ${tools_count}, "prompt_summary": "${prompt_summary}", "session_end": "${session_end}"}
EOF

log_info "LLM call logged: ${session_id} -> ${model} (${prompt_length} chars)"
