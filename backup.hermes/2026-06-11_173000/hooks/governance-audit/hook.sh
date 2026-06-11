#!/usr/bin/env bash
set -euo pipefail

[[ "${SKIP_GOVERNANCE_AUDIT:-}" == "true" ]] && echo '{"status": "skipped"}' && exit 0

input=$(cat)
prompt=$(printf '%s' "$input" | jq -r '.user_message // .userMessage // .prompt // empty' 2>/dev/null || true)
session_id=$(printf '%s' "$input" | jq -r '.session_id // .sessionId // empty' 2>/dev/null || true)
turn_id=$(printf '%s' "$input" | jq -r '.turn_id // .turnId // empty' 2>/dev/null || true)

if [[ -z "$prompt" ]]; then
  prompt="$input"
fi

# Simple threat detection patterns
threats=("ignore previous" "system prompt" "reveal your" "bypass" "jailbreak")
for threat in "${threats[@]}"; do
  if echo "$prompt" | grep -qi "$threat"; then
    echo "{\"status\": \"threat-detected\", \"pattern\": \"$threat\"}" >&2
    logger -t hermes-governance "THREAT: $threat session=${session_id:-unknown} turn=${turn_id:-unknown}"
    break
  fi
done

echo '{"status": "ok"}'
