#!/bin/bash

# Governance Audit: Log session start with governance context (Hermes hook)

set -euo pipefail

if [[ "${SKIP_GOVERNANCE_AUDIT:-}" == "true" ]]; then
  exit 0
fi

INPUT=$(cat)

LOG_DIR="$HOME/AppData/Local/hermes/logs/hermes/governance"
mkdir -p "$LOG_DIR"

TIMESTAMP=$(date -u +"%Y-%m-%dT%H:%M:%SZ")
CWD=$(pwd)
LEVEL="${GOVERNANCE_LEVEL:-standard}"

# Use jq -c for compact single-line JSON
jq -Rnc \
  --arg timestamp "$TIMESTAMP" \
  --arg cwd "$CWD" \
  --arg level "$LEVEL" \
  '{"timestamp":$timestamp,"event":"session_start","governance_level":$level,"cwd":$cwd}' \
  >> "$LOG_DIR/audit.log"

echo "🛡️ Governance audit active (level: $LEVEL)"
exit 0
