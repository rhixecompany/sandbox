#!/bin/bash
set -euo pipefail
INPUT=$(cat)
mkdir -p "${HOME}/AppData/Local/hermes/logs/hermes" >/dev/null 2>&1 || true
printf '%s
' "$INPUT" | jq -c '.' >/dev/null 2>&1 || true
echo "{}"
