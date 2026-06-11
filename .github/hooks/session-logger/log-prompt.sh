#!/bin/bash

# Log pre-LLM turn preview (Hermes hook)

set -euo pipefail

# Skip if logging disabled
if [[ "${SKIP_LOGGING:-}" == "true" ]]; then
  exit 0
fi

# Read input from Hermes (contains turn context)
INPUT=$(cat)

# Create logs directory if it doesn't exist
mkdir -p "$HOME/AppData/Local/hermes/logs/hermes"

# Extract timestamp and prompt preview
TIMESTAMP=$(date -u +"%Y-%m-%dT%H:%M:%SZ")
PROMPT=$(printf '%s' "$INPUT" | jq -r '.user_message // .prompt // empty' 2>/dev/null || true)
if [[ -z "$PROMPT" ]]; then
  PROMPT=$(printf '%s' "$INPUT" | head -c 100)
fi

# Log prompt (use jq -c for compact single-line JSON)
LOG_FILE="$HOME/AppData/Local/hermes/logs/hermes/prompts.log"
jq -Rnc \
  --arg timestamp "$TIMESTAMP" \
  --arg level "${LOG_LEVEL:-INFO}" \
  --arg prompt "$(printf '%s' "$PROMPT" | head -c 100)" \
  '{"timestamp":$timestamp,"event":"pre_llm_call","level":$level,"prompt_preview":$prompt}' >> "$LOG_FILE"

exit 0
