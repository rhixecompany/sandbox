#!/bin/bash

# Governance Audit: Log session end with summary statistics (Hermes hook)

set -euo pipefail

if [[ "${SKIP_GOVERNANCE_AUDIT:-}" == "true" ]]; then
  exit 0
fi

INPUT=$(cat)

LOG_DIR="$HOME/AppData/Local/hermes/logs/hermes/governance"
mkdir -p "$LOG_DIR"

TIMESTAMP=$(date -u +"%Y-%m-%dT%H:%M:%SZ")
LOG_FILE="$LOG_DIR/audit.log"

# Count events from this session
TOTAL=0
THREATS=0
SESSION_START=""

if [[ -f "$LOG_FILE" ]]; then
  # Find the last session_start event to scope stats to current session
  SESSION_START=$(grep '"session_start"' "$LOG_FILE" 2>/dev/null | tail -1 | jq -r '.timestamp' 2>/dev/null || echo "")
  if [[ -n "$SESSION_START" ]]; then
    # Count events and threats after session start using jq
    TOTAL=$(jq -r --arg start "$SESSION_START" 'select(.timestamp >= $start) | .timestamp' "$LOG_FILE" 2>/dev/null | wc -l || echo 0)
    THREATS=$(jq -r --arg start "$SESSION_START" 'select(.timestamp >= $start and .event == "threat_detected") | .timestamp' "$LOG_FILE" 2>/dev/null | wc -l || echo 0)
  else
    TOTAL=$(wc -l < "$LOG_FILE" 2>/dev/null || echo 0)
    THREATS=$(grep -c '"threat_detected"' "$LOG_FILE" 2>/dev/null || echo 0)
  fi
fi

# Use jq -c for compact single-line JSON
jq -Rnc \
  --arg timestamp "$TIMESTAMP" \
  --argjson total "$TOTAL" \
  --argjson threats "$THREATS" \
  '{"timestamp":$timestamp,"event":"session_end","total_events":$total,"threats_detected":$threats}' \
  >> "$LOG_FILE"

if [[ "$THREATS" -gt 0 ]]; then
  echo "⚠️ Session ended: $THREATS threat(s) detected in $TOTAL events"
else
  echo "✅ Session ended: $TOTAL events, no threats"
fi

exit 0
