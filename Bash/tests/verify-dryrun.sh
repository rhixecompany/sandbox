#!/usr/bin/env bash
set -euo pipefail
IFS=$'\n\t'

ROOT="$(cd "$(dirname "${BASH_SOURCE[0]}")/.." && pwd)"
SCRIPTS_DIR="${ROOT}"

FAIL=0
MISSING_MARKERS=()
SELF="$(cd "$(dirname "${BASH_SOURCE[0]}")" && pwd)/$(basename "${BASH_SOURCE[0]}")"

# Limit candidates to likely executable scripts only to avoid scanning docs/docs/tests/lock files.
mapfile -t candidates < <(find "${SCRIPTS_DIR}" -type f \( -name '*.sh' -o -name '*.ps1' -o -name '*.bat' -o -name '*.ts' -o -name '*.js' \) \
  ! -path "${SCRIPTS_DIR}/tests/*" \
  ! -path "${SCRIPTS_DIR}/docs/*" \
  ! -path "${SCRIPTS_DIR}/logs/*" \
  ! -path "${SCRIPTS_DIR}/node_modules/*" \
  ! -path "${SCRIPTS_DIR}/.git/*" \
  ! -path "${SCRIPTS_DIR}/archive/*" \
  2>/dev/null | grep -v "^${SELF}\$" || true)

# For each candidate, check for DRY_RUN_SUPPORT marker and attempt dry-run invocation if supported
for f in "${candidates[@]}"; do
  echo "Checking $f"
  if grep -q "DRY_RUN_SUPPORT=true" "$f"; then
    echo "  has DRY_RUN_SUPPORT marker"
    # Determine invocation
    case "$f" in
      *.sh)
        if command -v bash >/dev/null 2>&1; then
          bash "$f" --dry-run || { echo "  dry-run failed for $f"; FAIL=1; }
        else
          echo "  bash not available; skipping runtime invocation"
        fi
        ;;
      *.ps1)
        if command -v pwsh >/dev/null 2>&1; then
          pwsh -NoProfile -Command "& {& '${f}' --dry-run }" || { echo "  pwsh dry-run failed for $f"; FAIL=1; }
        else
          echo "  pwsh not available; skipping runtime invocation"
        fi
        ;;
      *.js|*.ts)
        if command -v node >/dev/null 2>&1; then
          node "$f" --dry-run || { echo "  node dry-run failed for $f"; FAIL=1; }
        else
          echo "  node not available; skipping runtime invocation"
        fi
        ;;
      *)
        echo "  unknown type; ensure it supports --dry-run"
        ;;
    esac
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
