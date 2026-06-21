#!/usr/bin/env bash
set -euo pipefail

# Governance Audit Hook - Unified entry point for all governance events
# Events: on_session_start, on_session_end, pre_llm_call
# Threat detection: prompt injection, data exfiltration, tool misuse, instruction override

# Source shared library
source "$(dirname "$0")/../lib.sh"

LOG_DIR="${HOME}/AppData/Local/hermes/logs/governance"
ensure_log_dir "$LOG_DIR"

EVENT="${1:-unknown}"
INPUT="$(cat)"
TIMESTAMP="$(iso_timestamp)"

log_audit() {
    local event_type="$1"
    local finding="$2"
    local severity="$3"
    local detail="$4"
    log_jsonl "${LOG_DIR}/audit.log" \
        --arg ts "$TIMESTAMP" \
        --arg event "$event_type" \
        --arg finding "$finding" \
        --arg severity "$severity" \
        --argjson detail "$detail" \
        '{ts:$ts,event:$event,finding:$finding,severity:$severity,detail:$detail}'
}

detect_prompt_injection() {
    local input="$1"
    local patterns=(
        'ignore (previous|all|above) instructions?'
        'disregard (previous|all|above) instructions?'
        'forget (previous|all|above) (instructions?|context|prompts?)'
        'you are now'
        'act as (if you are|a|an)'
        'pretend to be'
        'roleplay as'
        'system prompt'
        'developer prompt'
        'system message'
        'ignore (this|that|the) (prompt|message|instruction)'
        'bypass (safety|security|guard|filter|protection)'
        'jailbreak'
        'DAN mode'
        'developer mode'
        'ignore all rules'
        'no rules'
        'unrestricted'
        'do anything now'
        'simulate (a|an)'
        'continue the pattern'
        'output only'
        'repeat the (prompt|message|instruction)'
        'show (me|us) (the|your) (prompt|instructions|system prompt)'
        'what (is|are) your (instructions|system prompt|guidelines|rules)'
        'override (safety|instructions|rules|guidelines)'
        'disable (safety|filter|guard)'
    )
    local lower_input
    lower_input="$(echo "$input" | tr '[:upper:]' '[:lower:]')"
    for pattern in "${patterns[@]}"; do
        if echo "$lower_input" | grep -qiE -- "$pattern"; then
            return 0
        fi
    done
    return 1
}

detect_data_exfiltration() {
    local input="$1"
    local patterns=(
        'api[_-]?key'
        'secret[_-]?key'
        'access[_-]?token'
        'bearer [a-zA-Z0-9._-]+'
        'password[=:]\s*\S+'
        'private[_-]?key'
        'ssh[_-]?key'
        'aws[_-]?secret'
        'database[_-]?url'
        'connection[_-]?string'
        '-----BEGIN (RSA |EC )?PRIVATE KEY-----'
        'sk-[a-zA-Z0-9]{20,}'
        'ghp_[a-zA-Z0-9]{36}'
        'gho_[a-zA-Z0-9]{36}'
        'ghu_[a-zA-Z0-9]{36}'
        'github_pat_[a-zA-Z0-9_]{22,}'
        'gcp[_-]?key'
        'firebase[_-]?key'
    )
    local lower_input
    lower_input="$(echo "$input" | tr '[:upper:]' '[:lower:]')"
    for pattern in "${patterns[@]}"; do
        if echo "$lower_input" | grep -qiE -- "$pattern"; then
            return 0
        fi
    done
    return 1
}

detect_tool_misuse() {
    local input="$1"
    local patterns=(
        'rm -rf /'
        'rm -rf \*'
        'chmod 777'
        'chmod -R 777'
        'curl.*\| *bash'
        'wget.*\| *bash'
        'curl.*\| *sh'
        'wget.*\| *sh'
        'eval \$\(curl'
        'eval \$\(wget'
        'nc -l'
        'netcat -l'
        'reverse shell'
        'bind shell'
        'mkfifo.*/dev/tcp'
        '/dev/tcp/'
        '> /dev/tcp/'
        'base64 -d.*\|'
        'powershell -enc'
        'powershell -e '
        'cmd\.exe /c'
        'rundll32'
        'regsvr32'
        'mshta'
        'certutil -decode'
        'bitsadmin'
        'schtasks /create'
        'at \d\d:\d\d'
    )
    local lower_input
    lower_input="$(echo "$input" | tr '[:upper:]' '[:lower:]')"
    for pattern in "${patterns[@]}"; do
        if echo "$lower_input" | grep -qiE -- "$pattern"; then
            return 0
        fi
    done
    return 1
}

detect_instruction_override() {
    local input="$1"
    local patterns=(
        'you must (not|never|always)'
        'you are required to'
        'you have to'
        'you will (not|never)'
        'do not (tell|say|reveal|disclose|mention)'
        'keep (this|it) (secret|confidential|private)'
        'between (us|you and me)'
        'off the record'
        'confidential'
        'do not (log|record|store|save)'
        'delete (this|the) (conversation|message|log)'
        'forget (this|that)'
        'ignore (the|my) (question|request|instruction)'
        'actually, (ignore|forget|disregard)'
        'wait, (ignore|forget|disregard)'
        'never mind,'
        'scratch that'
    )
    local lower_input
    lower_input="$(echo "$input" | tr '[:upper:]' '[:lower:]')"
    for pattern in "${patterns[@]}"; do
        if echo "$lower_input" | grep -qiE -- "$pattern"; then
            return 0
        fi
    done
    return 1
}

case "$EVENT" in
    on_session_start)
        log_audit "session_start" "session_initiated" "info" '{}'
        ;;
    on_session_end)
        log_audit "session_end" "session_terminated" "info" '{}'
        ;;
    pre_llm_call)
        if detect_prompt_injection "$INPUT"; then
            log_audit "pre_llm_call" "prompt_injection_detected" "high" "$(jq -cn --arg v "$INPUT" '$v')"
        elif detect_data_exfiltration "$INPUT"; then
            log_audit "pre_llm_call" "data_exfiltration_attempt" "high" "$(jq -cn --arg v "$INPUT" '$v')"
        elif detect_tool_misuse "$INPUT"; then
            log_audit "pre_llm_call" "tool_misuse_detected" "high" "$(jq -cn --arg v "$INPUT" '$v')"
        elif detect_instruction_override "$INPUT"; then
            log_audit "pre_llm_call" "instruction_override_attempt" "medium" "$(jq -cn --arg v "$INPUT" '$v')"
        else
            log_audit "pre_llm_call" "prompt_clean" "info" '{}'
        fi
        ;;
    *)
        log_audit "unknown_event" "unrecognized_event" "low" "$(jq -cn --arg v "$EVENT" '$v')"
        ;;
esac

# Always output empty JSON for hook protocol compliance
printf '{}'
exit 0