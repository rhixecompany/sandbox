#!/bin/bash
set -euo pipefail
INPUT=$(cat)
printf '%s\n' "$INPUT" | jq -c '{event:"prompt",ts:(now|tostring)}' >/dev/null 2>&1 || echo '{"event":"prompt"}' >/dev/null 2>&1 || true
