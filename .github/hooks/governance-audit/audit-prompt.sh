#!/bin/bash
set -euo pipefail
INPUT=$(cat)
if [ "${SKIP_GOVERNANCE_AUDIT:-false}" = "true" ]; then exit 0; fi
printf '%s\n' "$INPUT" | jq -c '{event:"audit_prompt",ts:(now|tostring)}' >/dev/null 2>&1 || true
exit 0
