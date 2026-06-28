#!/usr/bin/env bash
# docs-cleanup-verify.sh
# Verifies docs/ consolidation state after the 2026-06-22 cleanup.
#
# Checks:
#   1. docs/skills-reports/ has 0 .md files (auto-generated artifacts not recreated)
#   2. docs/skills-audit/ has only index.md
#
# Usage: docs-cleanup-verify.sh [workspace-path]
#   If no path given, uses the current working directory.

set -euo pipefail

WORKSPACE="${1:-$(pwd)}"
DOCS_DIR="$WORKSPACE/docs"
issues=0

echo "=========================================="
echo " Docs Cleanup Verification Hook"
echo "=========================================="
echo "Workspace : $WORKSPACE"
echo "Timestamp : $(date '+%Y-%m-%d %H:%M:%S')"
echo ""

# ------------------------------------------------------------------
# 1. Check docs/skills-reports/ — must have 0 .md files
# ------------------------------------------------------------------
check_skills_reports() {
    local dir="$DOCS_DIR/skills-reports"
    echo "--- Checking: $dir ---"

    if [ ! -d "$dir" ]; then
        echo "  OK: Directory does not exist (clean)."
        return 0
    fi

    local count
    count=$(find "$dir" -maxdepth 1 -name '*.md' -type f 2>/dev/null | wc -l)

    if [ "$count" -eq 0 ]; then
        echo "  OK: 0 .md files found."
    else
        echo "  ALERT: $count .md file(s) found — regrowth detected!"
        find "$dir" -maxdepth 1 -name '*.md' -type f 2>/dev/null | sed 's/^/    - /'
        issues=$((issues + 1))
    fi
}

# ------------------------------------------------------------------
# 2. Check docs/skills-audit/ — only index.md allowed
# ------------------------------------------------------------------
check_skills_audit() {
    local dir="$DOCS_DIR/skills-audit"
    echo "--- Checking: $dir ---"

    if [ ! -d "$dir" ]; then
        echo "  OK: Directory does not exist."
        return 0
    fi

    # Verify index.md is present
    if [ -f "$dir/index.md" ]; then
        echo "  OK: index.md present."
    else
        echo "  ALERT: index.md is missing!"
        issues=$((issues + 1))
    fi

    # Find .md files other than index.md
    local extra_files
    extra_files=$(find "$dir" -maxdepth 1 -name '*.md' -type f ! -name 'index.md' 2>/dev/null || true)

    if [ -z "$extra_files" ]; then
        echo "  OK: No unexpected .md files."
    else
        local extra_count
        extra_count=$(echo "$extra_files" | wc -l)
        echo "  ALERT: $extra_count unexpected .md file(s) found — regrowth detected!"
        echo "$extra_files" | sed 's/^/    - /'
        issues=$((issues + 1))
    fi
}

# ------------------------------------------------------------------
# Run checks
# ------------------------------------------------------------------
check_skills_reports
echo ""
check_skills_audit
echo ""

# ------------------------------------------------------------------
# Summary
# ------------------------------------------------------------------
echo "=========================================="
if [ "$issues" -gt 0 ]; then
    echo " RESULT: FAILED — $issues issue(s) detected."
    echo " Action: Clean up regrown files in docs/ subdirectories."
    echo "=========================================="
    exit 1
else
    echo " RESULT: PASSED — docs/ consolidation state is clean."
    echo "=========================================="
    exit 0
fi
