#!/bin/bash

# Log session start event (Hermes hook)

set -euo pipefail

# Skip if logging disabled
if [[ "${SKIP_LOGGING:-}" == "true" ]]; then
  exit 0
fi

# Read input from Hermes
INPUT=$(cat)

# Create logs directory if it doesn't exist
mkdir -p "$HOME/AppData/Local/hermes/logs/hermes"

# Extract timestamp and session info
TIMESTAMP=$(date -u +"%Y-%m-%dT%H:%M:%SZ")
CWD=$(pwd)

# Log session start (use jq -c for compact single-line JSON)
LOG_FILE="$HOME/AppData/Local/hermes/logs/hermes/session.log"
jq -Rnc --arg timestamp "$TIMESTAMP" --arg cwd "$CWD" '{"timestamp":$timestamp,"event":"sessionStart","cwd":$cwd}' >> "$LOG_FILE"

echo "📝 Session logged"
exit 0
