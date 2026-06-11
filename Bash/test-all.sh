#!/usr/bin/env bash
# shellcheck shell=bash
# Test all scripts in Sandbox/Bash
# Phase 5: Execute & Test

set -euo pipefail
cd ~/Desktop/Sandbox/Bash || exit 1

echo "════════════════════════════════════════════════════════════"
echo "  PHASE 5: EXECUTE & TEST ALL SCRIPTS"
echo "════════════════════════════════════════════════════════════"
echo ""

# Counters
pass=0
fail=0
skip=0

# Color codes
RED='\033[0;31m'
GREEN='\033[0;32m'
YELLOW='\033[1;33m'
NC='\033[0m'

test_script() {
    local name="$1"
    local cmd="$2"
    local desc="$3"
    
    echo -n "Testing $name ... "
    
    if timeout 10 $cmd >/dev/null 2>&1; then
        echo -e "${GREEN}✓ PASS${NC} ($desc)"
        ((pass++))
    else
        echo -e "${RED}✗ FAIL${NC} ($desc)"
        ((fail++))
    fi
}

# ─────────────────────────────────────────────────────────────
# SHELL SCRIPTS
# ─────────────────────────────────────────────────────────────

echo "SHELL SCRIPTS (.sh):"
test_script "upgrade.sh" "bash upgrade.sh --help" "show help"
test_script "cache-clean.sh" "bash cache-clean.sh --help" "show help"
test_script "clean_dependency_folders.sh" "bash clean_dependency_folders.sh --help" "show help"
test_script "git-commit-batches.sh" "bash git-commit-batches.sh --help" "show help"

# ─────────────────────────────────────────────────────────────
# POWERSHELL SCRIPTS
# ─────────────────────────────────────────────────────────────

echo ""
echo "POWERSHELL SCRIPTS (.ps1):"

test_script "upgrade-native.ps1" "pwsh -NoProfile -Command '. ./upgrade-native.ps1 -Help'" "show help"
test_script "cache-clean.ps1" "pwsh -NoProfile -Command '. ./cache-clean.ps1 -Help'" "show help"
test_script "clean-dependency-folders.ps1" "pwsh -NoProfile -Command '. ./clean-dependency-folders.ps1 -Help'" "show help"
test_script "disk-analysis.ps1" "pwsh -NoProfile -Command '. ./disk-analysis.ps1 -Help'" "show help"
test_script "verify_cleanup.ps1" "pwsh -NoProfile -Command '. ./verify_cleanup.ps1 -Help'" "show help"

# ─────────────────────────────────────────────────────────────
# BATCH FILES (limited testing in bash)
# ─────────────────────────────────────────────────────────────

echo ""
echo "BATCH FILES (.bat) - Syntax Check:"

for f in *.bat; do
    echo -n "Checking $f ... "
    if grep -q "^@echo off" "$f" && grep -q "^bunx tsx src/" "$f"; then
        echo -e "${GREEN}✓ VALID${NC}"
        ((pass++))
    else
        echo -e "${YELLOW}⚠ WARNING${NC} (syntax unclear)"
        ((skip++))
    fi
done

# ─────────────────────────────────────────────────────────────
# DRY-RUN TESTS
# ─────────────────────────────────────────────────────────────

echo ""
echo "DRY-RUN TESTS (--dry-run flag):"

test_script "cache-clean dry" "bash cache-clean.sh --all --dry-run" "preview mode"
test_script "clean-dep dry" "bash clean_dependency_folders.sh --dry-run" "preview mode"
test_script "git-batch dry" "bash git-commit-batches.sh --dry-run" "preview mode"

# ─────────────────────────────────────────────────────────────
# SUMMARY
# ─────────────────────────────────────────────────────────────

echo ""
echo "════════════════════════════════════════════════════════════"
echo "TEST SUMMARY"
echo "════════════════════════════════════════════════════════════"
echo -e "${GREEN}Pass:${NC}  $pass"
echo -e "${RED}Fail:${NC}  $fail"
echo -e "${YELLOW}Skip:${NC}  $skip"
echo ""

if [ "$fail" -eq 0 ]; then
    echo -e "${GREEN}✓ ALL TESTS PASSED${NC}"
    exit 0
else
    echo -e "${RED}✗ $fail TESTS FAILED${NC}"
    exit 1
fi
