#!/bin/bash
set -euo pipefail
INPUT=$(cat)
printf '%s\n' "$INPUT" | jq -c '{event:"session_end",ts:(now|tostring)}' >/dev/null 2>&1 || echo '{"event":"session_end"}' >/dev/null 2>&1 || true
