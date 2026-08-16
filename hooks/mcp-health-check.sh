#!/bin/bash
# MCP Health Check Hook — periodic check that all MCP servers are responsive
# Run via cron or as a pre-execution hook in Hermès config

set -e

HERMES_HOME="${HERMES_HOME:-C:/Users/Alexa/AppData/Local/hermes}"
LOG_FILE="${HERMES_HOME}/logs/mcp-health.log"
MIN_SUCCESS=20  # Alert if fewer than this many servers are OK

log() {
    echo "[$(date '+%Y-%m-%d %H:%M:%S')] $*" | tee -a "$LOG_FILE"
}

alert() {
    log "ALERT: $*"
}

# Ensure log directory exists
mkdir -p "$(dirname "$LOG_FILE")"

log "Starting MCP health check..."

# Get server list from Hermès config — only from mcp_servers: section (indent 2)
CONFIG="$HERMES_HOME/config.yaml"

if [ ! -f "$CONFIG" ]; then
    alert "Config file not found: $CONFIG"
    exit 1
fi

# Parse server entries from mcp_servers: section
# Server entries have indent 2 and end with ':' (not sub-keys)
SERVERS=$(awk '/^mcp_servers:/{found=1; next} found && /^[[:space:]]{2}[a-z][a-z0-9_-]*:/{gsub(/:/,""); print}' "$CONFIG" | sort -u)

SUCCESS=0
FAIL=0
TOTAL=0

for SERVER in $SERVERS; do
    TOTAL=$((TOTAL + 1))
    
    STATUS=$(hermes mcp list 2>/dev/null | grep -A1 "  $SERVER " | tail -1 | grep -o "✓ enabled\|✗ disabled" || echo "UNKNOWN")
    
    if [ "$STATUS" = "✓ enabled" ]; then
        SUCCESS=$((SUCCESS + 1))
        log "  ✓ $SERVER: enabled"
    else
        FAIL=$((FAIL + 1))
        log "  ✗ $SERVER: $STATUS"
    fi
done

log "MCP Health Check Complete: $SUCCESS/$TOTAL OK, $FAIL failed"

if [ $SUCCESS -lt $MIN_SUCCESS ]; then
    alert "Only $SUCCESS/$TOTAL MCP servers healthy (threshold: $MIN_SUCCESS)"
fi

if [ $FAIL -gt 0 ]; then
    alert "$FAIL MCP server(s) not healthy — check configuration"
fi

log "MCP health check complete."
