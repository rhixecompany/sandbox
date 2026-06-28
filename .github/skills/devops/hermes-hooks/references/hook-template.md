# Complete Hook Template

```bash
#!/usr/bin/env bash
set -euo pipefail

# Read JSON from stdin
input=$(cat)

# Check skip flag
skip_var="SKIP_MY_HOOK"
if [[ "${!skip_var:-}" == "true" ]]; then
  echo '{"status": "skipped"}'
  exit 0
fi

# Parse event
event=$(echo "$input" | jq -r '.event')
session_id=$(echo "$input" | jq -r '.session_id')
timestamp=$(echo "$input" | jq -r '.timestamp')

# Logging setup
log_file=~/.hermes/logs/hermes/my-hook.log
mkdir -p "$(dirname "$log_file")"

case "$event" in
  sessionStart)
    # Your logic here
    echo "$(date -Iseconds) SESSION_START $session_id" >> "$log_file"
    echo '{"status": "ok"}'
    ;;
  sessionEnd)
    duration=$(echo "$input" | jq -r '.duration_seconds')
    msg_count=$(echo "$input" | jq -r '.message_count')
    tool_calls=$(echo "$input" | jq -r '.tool_calls')
    echo "$(date -Iseconds) SESSION_END $session_id duration=${duration}s msgs=$msg_count tools=$tool_calls" >> "$log_file"
    echo '{"status": "ok"}'
    ;;
  userPromptSubmitted)
    prompt=$(echo "$input" | jq -r '.prompt' | head -c 100)
    # Your logic here (e.g., security scan, cost tracking)
    echo "$(date -Iseconds) PROMPT $session_id: $prompt..." >> "$log_file"
    echo '{"status": "ok"}'
    ;;
  *)
    echo '{"status": "ignored"}'
    ;;
esac
```

## Error Handling
```bash
# Return error status (agent will log but continue)
echo '{"status": "error", "message": "hook failed: ..."}' >&2
exit 1
```

## Key Requirements
- ✅ `jq -c` for JSON output
- ✅ `awk` for float comparison
- ✅ SKIP flag support
- ✅ Absolute paths
- ✅ Log to `~/.hermes/logs/hermes/`
- ✅ Executable: `chmod +x hook.sh`