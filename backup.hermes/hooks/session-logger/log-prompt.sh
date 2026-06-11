#!/bin/bash

# Log user prompt submission (Hermes hook)

set -euo pipefail

# Skip if logging disabled
if [[ "${SKIP_LOGGING:-}" == "true" ]]; then
  exit 0
fi

# Read input from Hermes (contains prompt info)
INPUT=$(cat)

# Create logs directory if it doesn't exist
mkdir -p "$HOME/AppData/Local/hermes/logs/hermes"

# Extract timestamp
TIMESTAMP=$(date -u +"%Y-%m-%dT%H:%M:%SZ")

# Log prompt (use jq -c for compact single-line JSON)
LOG_FILE="$HOME/AppData/Local/hermes/logs/hermes/prompts.log"
jq -Rnc --arg timestamp "$TIMESTAMP" --arg level "${LOG_LEVEL:-INFO}" '{"timestamp":$timestamp,"event":"userPromptSubmitted","level":$level}' >> "$LOG_FILE"

exit 0
