#!/usr/bin/env bash
# validate-yaml.sh — Run yamllint across all YAML files
# Exits 0 if clean, 1 with detailed report if issues found
# Excludes cookiecutter Jinja template directories

set -euo pipefail

CONFIG="${1:-.yamllint.yaml}"
TMPDIR=$(mktemp -d)
trap 'rm -rf "$TMPDIR"' EXIT

WORKSPACE=$(git rev-parse --show-toplevel 2>/dev/null || echo ".")
cd "$WORKSPACE"

echo "=== YAML Validation Report ==="
echo "Config: $CONFIG"
echo "Workspace: $WORKSPACE"
echo ""

# Collect all YAML files excluding cookiecutter Jinja templates
ALL_FILES=$(find . -name "*.yml" -o -name "*.yaml" | grep -v '/{{cookiecutter' | grep -v '/node_modules/' | grep -v '/\.git/' | sort)

ERROR_COUNT=0
FILE_COUNT=0

for f in $ALL_FILES; do
  FILE_COUNT=$((FILE_COUNT + 1))
  RESULT=$(yamllint -c "$CONFIG" "$f" 2>&1) || true
  if [ -n "$RESULT" ]; then
    ERROR_COUNT=$((ERROR_COUNT + 1))
    echo "[FAIL] $f"
    echo "$RESULT" | head -10
    echo ""
  else
    echo "[PASS] $f"
  fi
done

echo ""
echo "=== Summary ==="
echo "Total files: $FILE_COUNT"
echo "Files with issues: $ERROR_COUNT"
echo "Result: $([ "$ERROR_COUNT" -eq 0 ] && echo 'ALL CLEAN ✅' || echo 'ISSUES FOUND ❌')"

exit $([ "$ERROR_COUNT" -eq 0 ] && echo 0 || echo 1)