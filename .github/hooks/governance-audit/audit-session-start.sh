#!/bin/bash
set -euo xfail
INPUT=$(cat)
if [ "${SKIP_GOVERNANCE_AUDIT:-false}" = "true" ]; then exit 0; fi
printf '%sn' "$INPUT" | jq -c '{event:"audit_session_start",ts:(now|tostring)}' >/dev/null 2>&1 || true
