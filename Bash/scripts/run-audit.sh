#!/usr/bin/env bash
# shellcheck shell=bash

# DRY_RUN_SUPPORT=true
# Minimal dry-run handling: set DRY_RUN=true via env or --dry-run flag
DRY_RUN=${DRY_RUN:-false}
for arg in "$@"; do
  if [ "$arg" = "--dry-run" ] || [ "$arg" = "-n" ]; then DRY_RUN=true; fi
done
if [ "$DRY_RUN" = "true" ]; then
  echo "DRY-RUN: $(basename "$0") would perform orchestration (no side effects)."
  exit 0
fi

# Master Orchestration Script
# Runs all 5 phases of the rhixe audit process

set -euo pipefail

TIMESTAMP=$(date +%Y-%m-%d_%H-%M-%S)

echo "=========================================="
echo "Rhixe Audit - Master Orchestration"
echo "Timestamp: $TIMESTAMP"
echo "=========================================="

# Verify directories exist
mkdir -p ./docs/audits
mkdir -p ./BATCH_LOGS

echo ""
echo "Starting audit phases..."
echo ""

# Phase 1: Deep Triage (CRITICAL+HIGH repos)
echo ">>> Phase 1: Deep Triage (CRITICAL+HIGH)"
if [ -f "./scripts/phase-1-deep-triage.sh" ]; then
  bash ./scripts/phase-1-deep-triage.sh || {
    echo "WARNING: Phase 1 had issues, but continuing..."
  }
else
  echo "WARNING: phase-1-deep-triage.sh not found — skipping"
fi

# Phase 2: Light Inventory (MEDIUM+LOW repos)
echo ""
echo ">>> Phase 2: Light Inventory (MEDIUM+LOW)"
if [ -f "./scripts/phase-2-light-inventory.ps1" ]; then
  pwsh ./scripts/phase-2-light-inventory.ps1 || {
    echo "WARNING: Phase 2 had issues, but continuing..."
  }
else
  echo "WARNING: phase-2-light-inventory.ps1 not found — skipping"
fi

# Phase 3: Consolidation (merge findings, batch)
echo ""
echo ">>> Phase 3: Consolidation"
if [ -f "./scripts/phase-3-consolidation.js" ]; then
  node ./scripts/phase-3-consolidation.js || {
    echo "WARNING: Phase 3 had issues, but continuing..."
  }
elif [ -f "./scripts/phase-3-consolidation.ts" ]; then
  bunx tsx ./scripts/phase-3-consolidation.ts || {
    echo "WARNING: Phase 3 had issues, but continuing..."
  }
else
  echo "WARNING: phase-3-consolidation not found — skipping"
fi

# Phase 4: Batch Executor (apply fixes)
echo ""
echo ">>> Phase 4: Batch Execution"
if [ -f "./scripts/phase-4-batch-executor.js" ]; then
  node ./scripts/phase-4-batch-executor.js || {
    echo "WARNING: Phase 4 had issues, but continuing..."
  }
elif [ -f "./scripts/phase-4-batch-executor.ts" ]; then
  bunx tsx ./scripts/phase-4-batch-executor.ts || {
    echo "WARNING: Phase 4 had issues, but continuing..."
  }
else
  echo "WARNING: phase-4-batch-executor not found — skipping"
fi

# Phase 5: Final Summary (report generation)
echo ""
echo ">>> Phase 5: Final Summary"
if [ -f "./scripts/phase-5-final-summary.js" ]; then
  node ./scripts/phase-5-final-summary.js || {
    echo "WARNING: Phase 5 had issues, check logs..."
  }
elif [ -f "./scripts/phase-5-final-summary.ts" ]; then
  bunx tsx ./scripts/phase-5-final-summary.ts || {
    echo "WARNING: Phase 5 had issues, check logs..."
  }
else
  echo "WARNING: phase-5-final-summary not found — skipping"
fi

echo ""
echo "=========================================="
echo "Audit Complete!"
echo "=========================================="
echo ""
echo "Artifacts:"
echo "  - Audit findings: ./docs/audits/"
echo "  - Consolidated report: ./CONSOLIDATED_PROPOSED_FIXES.md"
echo "  - Batch execution logs: ./BATCH_LOGS/"
echo "  - Final summary: ./FINAL_AUDIT_SUMMARY.md"
echo ""
