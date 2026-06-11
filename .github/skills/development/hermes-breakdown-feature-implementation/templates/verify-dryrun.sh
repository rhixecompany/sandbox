#!/usr/bin/env bash
# verify-dryrun.sh template for the hermes-breakdown-feature-implementation skill
# Place this in templates/ so agents or users can copy into their repo

set -euo pipefail
IFS=$'\n\t'

ROOT="$(pwd)"
SCRIPTS_DIR="${ROOT}/Bash"
FAIL=0
MISSING_MARKERS=()

mapfile -t candidates < <(grep -RIl --exclude-dir=logs -e "rm -f\|rm -rf\|git push\|npm publish\|bun publish\|docker\|scp\|mv \|cp \|chown \|chmod " "${SCRIPTS_DIR}" || true)

for f in "${candidates[@]}"; do
  echo "Checking $f"
  if grep -q "DRY_RUN_SUPPORT=true" "$f"; then
    echo "  has DRY_RUN_SUPPORT marker"
  else
    echo "  MISSING DRY_RUN_SUPPORT marker"
    MISSING_MARKERS+=("$f")
    FAIL=1
  fi
done

if [ ${#MISSING_MARKERS[@]} -ne 0 ]; then
  echo "ERROR: ${#MISSING_MARKERS[@]} scripts lack DRY_RUN_SUPPORT marker:" 
  for x in "${MISSING_MARKERS[@]}"; do
    echo " - $x"
  done
fi

if [ "$FAIL" -ne 0 ]; then
  echo "verify-dryrun: FAILED"
  exit 2
fi

echo "verify-dryrun: OK"
exit 0
