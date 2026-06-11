#!/usr/bin/env bash
# verify-dryrun canonical template for skill usage
set -euo pipefail
IFS=$'\n\t'

ROOT=$(cd "$(dirname "$0")/.." && pwd)
SCAN_DIR="$ROOT/Bash"

grep -E "\b(rm|git push|npm publish|docker |scp |mv |cp |chown |chmod |apt |yum |brew )\b" -R --line-number "$SCAN_DIR" || true

# For each shell/ps1 file that references destructive commands, check for marker
missing_marker=()
while IFS= read -r f; do
  case "$f" in
    *.sh)
      if ! grep -q "DRY_RUN_SUPPORT=true" "$f"; then
        missing_marker+=("$f")
      fi
      ;;
    *.ps1)
      if ! grep -q "DRY_RUN_SUPPORT=true" "$f"; then
        missing_marker+=("$f")
      fi
      ;;
    *.ts|*.js)
      # check for top-level marker comment
      if ! grep -q "DRY_RUN_SUPPORT=true" "$f"; then
        missing_marker+=("$f")
      fi
      ;;
  esac
done < <(grep -R --line-number -E "\b(rm|git push|npm publish|docker |scp |mv |cp |chown |chmod |apt |yum |brew )\b" "$SCAN_DIR" | cut -d: -f1 | sort -u)

if [ ${#missing_marker[@]} -gt 0 ]; then
  printf "Missing DRY_RUN_SUPPORT markers found in:\n"
  printf "%s\n" "${missing_marker[@]}"
  exit 2
fi

# Attempt to invoke each candidate in dry-run mode
failures=()
while IFS= read -r f; do
  case "$f" in
    *.sh)
      bash "$f" --dry-run || failures+=("$f")
      ;;
    *.ps1)
      pwsh -NoProfile -File "$f" --dry-run || failures+=("$f")
      ;;
    *.ts)
      # Try bunx tsx if available, else node
      if command -v bunx >/dev/null 2>&1; then
        bunx tsx "$f" --dry-run || failures+=("$f")
      else
        node "$f" --dry-run || failures+=("$f")
      fi
      ;;
    *.js)
      node "$f" --dry-run || failures+=("$f")
      ;;
  esac
done < <(grep -R --line-number -E "\b(rm|git push|npm publish|docker |scp |mv |cp |chown |chmod |apt |yum |brew )\b" "$SCAN_DIR" | cut -d: -f1 | sort -u)

if [ ${#failures[@]} -gt 0 ]; then
  printf "Dry-run invocation failed for:\n"
  printf "%s\n" "${failures[@]}"
  exit 3
fi

printf "All candidates declare DRY_RUN_SUPPORT and dry-run invocation succeeded\n"
exit 0
