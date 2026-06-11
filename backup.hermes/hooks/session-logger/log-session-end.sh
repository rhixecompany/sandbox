#!/bin/bash

# Log session end event (Hermes hook)

set -euo pipefail

# Skip if logging disabled
if [[ "${SKIP_LOGGING:-}" == "true" ]]; then
  exit 0
fi

# Read input from Hermes
INPUT=$(cat)

# Create logs directory if it doesn't exist
mkdir -p "$HOME/AppData/Local/hermes/logs/hermes"

# Extract timestamp
TIMESTAMP=$(date -u +"%Y-%m-%dT%H:%M:%SZ")

# Log session end (use jq -c for compact single-line JSON)
LOG_FILE="$HOME/AppData/Local/hermes/logs/hermes/session.log"
jq -Rnc --arg timestamp "$TIMESTAMP" '{"timestamp":$timestamp,"event":"sessionEnd"}' >> "$LOG_FILE"

echo "📝 Session end logged"
exit 0
