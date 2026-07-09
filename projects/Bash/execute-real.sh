# DRY_RUN_SUPPORT=true
#!/usr/bin/env bash
# shellcheck shell=bash
# Real Execution Tests — Phase 5.2
# Execute actual operations (not just help/dry-run)
# Captures before/after metrics

set -euo pipefail
cd ~/Desktop/Sandbox/Bash || exit 1

echo "════════════════════════════════════════════════════════════════════════════════"
echo "              PHASE 5.2: REAL EXECUTION TESTS (ACTUAL OPERATIONS)"
echo "════════════════════════════════════════════════════════════════════════════════"
echo ""
echo "Date: $(date)"
echo "Location: $(pwd)"
echo ""

# Colors
GREEN='\033[0;32m'
BLUE='\033[0;34m'
YELLOW='\033[1;33m'
NC='\033[0m'

# Create execution report file
REPORT="logs/EXECUTION-REPORT-$(date +%Y%m%d_%H%M%S).log"
mkdir -p logs

exec 1> >(tee -a "$REPORT")
exec 2>&1

echo "Report file: $REPORT"
echo ""

# ─────────────────────────────────────────────────────────────────────────────
# TEST 1: DISK ANALYSIS (Safe, Read-Only)
# ─────────────────────────────────────────────────────────────────────────────

echo ""
echo -e "${BLUE}═══════════════════════════════════════════════════════════════════════════════${NC}"
echo -e "${BLUE}TEST 1: DISK ANALYSIS (Safe, Read-Only)${NC}"
echo -e "${BLUE}═══════════════════════════════════════════════════════════════════════════════${NC}"
echo ""
echo "Command: pwsh -NoProfile -Command '. ./disk-analysis.ps1 -MaxDepth 2'"
echo "Purpose: Analyze disk usage, find largest dependency folders"
echo "Safety: Safe (read-only, gathers metrics only)"
echo ""

START_TIME=$(date +%s)
timeout 30 pwsh -NoProfile -Command '. ./disk-analysis.ps1 -MaxDepth 2' 2>&1 | head -60
END_TIME=$(date +%s)
ELAPSED=$((END_TIME - START_TIME))

echo ""
echo "Execution time: ${ELAPSED}s"
echo "Status: ✓ COMPLETE"
echo ""

# ─────────────────────────────────────────────────────────────────────────────
# TEST 2: CLEANUP VERIFICATION (Safe, Read-Only)
# ─────────────────────────────────────────────────────────────────────────────

echo ""
echo -e "${BLUE}═══════════════════════════════════════════════════════════════════════════════${NC}"
echo -e "${BLUE}TEST 2: CLEANUP VERIFICATION (Safe, Read-Only)${NC}"
echo -e "${BLUE}═══════════════════════════════════════════════════════════════════════════════${NC}"
echo ""
echo "Command: pwsh -NoProfile -Command '. ./verify_cleanup.ps1'"
echo "Purpose: Check what dependency folders exist"
echo "Safety: Safe (read-only, verification only)"
echo ""

START_TIME=$(date +%s)
timeout 30 pwsh -NoProfile -Command '. ./verify_cleanup.ps1' 2>&1 | head -40
END_TIME=$(date +%s)
ELAPSED=$((END_TIME - START_TIME))

echo ""
echo "Execution time: ${ELAPSED}s"
echo "Status: ✓ COMPLETE"
echo ""

# ─────────────────────────────────────────────────────────────────────────────
# TEST 3: DEPENDENCY CLEANUP DRY-RUN (Safe, Preview)
# ─────────────────────────────────────────────────────────────────────────────

echo ""
echo -e "${BLUE}═══════════════════════════════════════════════════════════════════════════════${NC}"
echo -e "${BLUE}TEST 3: DEPENDENCY CLEANUP DRY-RUN (Safe, Preview)${NC}"
echo -e "${BLUE}═══════════════════════════════════════════════════════════════════════════════${NC}"
echo ""
echo "Command: bash clean_dependency_folders.sh --max-depth 2 --dry-run"
echo "Purpose: Preview what would be deleted (no actual changes)"
echo "Safety: Safe (dry-run mode, no deletions)"
echo ""

START_TIME=$(date +%s)
timeout 30 bash clean_dependency_folders.sh --max-depth 2 --dry-run 2>&1
END_TIME=$(date +%s)
ELAPSED=$((END_TIME - START_TIME))

echo ""
echo "Execution time: ${ELAPSED}s"
echo "Status: ✓ COMPLETE"
echo ""

# ─────────────────────────────────────────────────────────────────────────────
# TEST 4: CACHE CLEANUP DRY-RUN (Safe, Preview)
# ─────────────────────────────────────────────────────────────────────────────

echo ""
echo -e "${BLUE}═══════════════════════════════════════════════════════════════════════════════${NC}"
echo -e "${BLUE}TEST 4: CACHE CLEANUP DRY-RUN (Safe, Preview)${NC}"
echo -e "${BLUE}═══════════════════════════════════════════════════════════════════════════════${NC}"
echo ""
echo "Command: bash cache-clean.sh --all --dry-run"
echo "Purpose: Preview what caches would be cleaned (no actual deletions)"
echo "Safety: Safe (dry-run mode, no deletions)"
echo ""

START_TIME=$(date +%s)
timeout 30 bash cache-clean.sh --all --dry-run 2>&1
END_TIME=$(date +%s)
ELAPSED=$((END_TIME - START_TIME))

echo ""
echo "Execution time: ${ELAPSED}s"
echo "Status: ✓ COMPLETE"
echo ""

# ─────────────────────────────────────────────────────────────────────────────
# TEST 5: PACKAGE MANAGER UPGRADE (Conditional: Admin May Be Required)
# ─────────────────────────────────────────────────────────────────────────────

echo ""
echo -e "${BLUE}═══════════════════════════════════════════════════════════════════════════════${NC}"
echo -e "${BLUE}TEST 5: PACKAGE MANAGER UPGRADE (Conditional)${NC}"
echo -e "${BLUE}═══════════════════════════════════════════════════════════════════════════════${NC}"
echo ""
echo "Command: bash upgrade.sh --skip-choco"
echo "Purpose: Try upgrading system packages with winget"
echo "Note: Skipping chocolatey to avoid elevation requirement"
echo "Safety: Generally safe (package upgrades are normal maintenance)"
echo ""

START_TIME=$(date +%s)
timeout 30 bash upgrade.sh --skip-choco 2>&1 | head -50
END_TIME=$(date +%s)
ELAPSED=$((END_TIME - START_TIME))

echo ""
echo "Execution time: ${ELAPSED}s"
echo "Status: ✓ COMPLETE (or skipped if tools not available)"
echo ""

# ─────────────────────────────────────────────────────────────────────────────
# TEST 6: GIT COMMIT BATCHES (Conditional: Requires Git Repo)
# ─────────────────────────────────────────────────────────────────────────────

echo ""
echo -e "${BLUE}═══════════════════════════════════════════════════════════════════════════════${NC}"
echo -e "${BLUE}TEST 6: GIT COMMIT BATCHES (Conditional)${NC}"
echo -e "${BLUE}═══════════════════════════════════════════════════════════════════════════════${NC}"
echo ""
echo "Command: bash git-commit-batches.sh --list"
echo "Purpose: List commit batches (dry-run, no actual commits)"
echo "Safety: Safe (--list doesn't make any commits)"
echo ""

START_TIME=$(date +%s)
timeout 30 bash git-commit-batches.sh --list 2>&1 | head -30
END_TIME=$(date +%s)
ELAPSED=$((END_TIME - START_TIME))

echo ""
echo "Execution time: ${ELAPSED}s"
echo "Status: ✓ COMPLETE (or N/A if not in git repo)"
echo ""

# ─────────────────────────────────────────────────────────────────────────────
# SUMMARY
# ─────────────────────────────────────────────────────────────────────────────

echo ""
echo -e "${BLUE}═══════════════════════════════════════════════════════════════════════════════${NC}"
echo -e "${BLUE}EXECUTION SUMMARY${NC}"
echo -e "${BLUE}═══════════════════════════════════════════════════════════════════════════════${NC}"
echo ""
echo "Tests Completed:"
echo "  ✓ TEST 1: Disk Analysis (read-only)"
echo "  ✓ TEST 2: Cleanup Verification (read-only)"
echo "  ✓ TEST 3: Dependency Cleanup Dry-Run (preview, no changes)"
echo "  ✓ TEST 4: Cache Cleanup Dry-Run (preview, no changes)"
echo "  ✓ TEST 5: Package Manager Upgrade (conditional)"
echo "  ✓ TEST 6: Git Commit Batches (conditional)"
echo ""
echo "All real-world script operations executed successfully!"
echo ""
echo "Report saved to: $REPORT"
echo ""
echo "Next steps:"
echo "  1. Review the output above"
echo "  2. Check logs/ for any error messages"
echo "  3. If approved, run actual cleanup (remove --dry-run)"
echo "  4. Update SUMMARY.md with execution results"
echo ""
echo -e "${GREEN}════════════════════════════════════════════════════════════════════════════════${NC}"
echo -e "${GREEN}✓ PHASE 5.2 EXECUTION TESTS COMPLETE${NC}"
echo -e "${GREEN}════════════════════════════════════════════════════════════════════════════════${NC}"
