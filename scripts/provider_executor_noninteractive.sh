#!/usr/bin/env bash
set -euo pipefail

# Non-interactive provider executor for authorized providers only.
# Usage: ./scripts/provider_executor_noninteractive.sh <provider> <prompt_or_request>
# Outputs: JSON to stdout with provider, agent, context, max_output, capabilities, status, result

PROVIDER="${1:-}"
REQUEST="${2:-}"
PROFILE="${PROFILE:-default}"
MAX_OUTPUT="${MAX_OUTPUT:-4096}"
HERMES_HOME="${HERMES_HOME:-C:/Users/Alexa/AppData/Local/hermes}"

if [[ -z "$PROVIDER" || -z "$REQUEST" ]]; then
  echo '{"status":"error","result":"missing provider or request"}' >&2
  exit 1
fi

# Map provider to capability hints based on public provider metadata.
case "$PROVIDER" in
  copilot|deepseek|gemini|huggingface|minimax-oauth|nous|ollama-cloud|openai-api|openai-codex|opencode-zen|openrouter|xai|xai-oauth)
    ;;
  *)
    echo "{\"status\":\"error\",\"result\":\"unauthorized provider: $PROVIDER\"}" >&2
    exit 1
    ;;
esac

# Hermes oneshot invocation without interactivity.
HERMES_CMD=(hermes chat -p "$PROFILE" --oneshot "$REQUEST")
if [[ "$PROVIDER" != "$PROFILE" ]]; then
  # Attempt provider-specific routing if config supports it.
  HERMES_CMD+=(--provider "$PROVIDER")
fi

# Run with bounded output.
RAW_OUTPUT="$( "${HERMES_CMD[@]}" 2>&1 || true )"
TRUNCATED="false"
if [[ "$(printf "%s" "$RAW_OUTPUT" | wc -c)" -gt "$MAX_OUTPUT" ]]; then
  RAW_OUTPUT="$(printf "%s" "$RAW_OUTPUT" | head -c "$MAX_OUTPUT")"
  TRUNCATED="true"
fi

# Emit structured JSON.
printf '{"provider":"%s","agent":"%s","context":"cli","max_output":%s,"capabilities":["chat","oneshot"],"status":"ok","truncated":%s,"result":%s}\n' \
  "$PROVIDER" "$PROVIDER" "$MAX_OUTPUT" "$TRUNCATED" "$(printf '%s' "$RAW_OUTPUT" | python -c 'import json,sys; print(json.dumps(sys.stdin.read()))')"
