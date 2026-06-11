#!/usr/bin/env bash
# shellcheck shell=bash

# DRY_RUN_SUPPORT=true
# Minimal dry-run handling: set DRY_RUN=true via env or --dry-run flag
DRY_RUN=${DRY_RUN:-false}
for arg in "$@"; do
  if [ "$arg" = "--dry-run" ] || [ "$arg" = "-n" ]; then DRY_RUN=true; fi
done
if [ "$DRY_RUN" = "true" ]; then
  echo "DRY-RUN: $(basename "$0") would run diagnostics for critical repos (no side effects)."
  exit 0
fi

set -euo pipefail

REPO_INVENTORY="./scripts/config/repo-inventory.json"
DIAGNOSTICS_CONFIG="./scripts/config/diagnostics-config.json"
AUDIT_DIR="./docs/audits"
TIMESTAMP=$(date +%Y-%m-%d_%H-%M-%S)

echo "=========================================="
echo "Phase 1: Deep Triage (CRITICAL+HIGH repos)"
echo "=========================================="

# Critical repos: comicwise, banking, rhixe_scans, university-libary-jsm
CRITICAL_REPOS=("comicwise" "banking" "rhixe_scans" "university-libary-jsm")

for repo_id in "${CRITICAL_REPOS[@]}"; do
  echo ""
  echo "Processing: $repo_id"
  echo "---"

  # Get repo path from inventory
  repo_path=$(node -e "
    const inventory = require('$REPO_INVENTORY');
    const repo = inventory.repos.find(r => r.id === '$repo_id');
    if (repo) console.log(repo.path);
  ")

  if [ -z "$repo_path" ]; then
    echo "ERROR: Repo $repo_id not found in inventory"
    continue
  fi

  # Check if path exists
  if [ ! -d "$repo_path" ]; then
    echo "ERROR: Path does not exist: $repo_path"
    continue
  fi

  # Run scanner
  echo "Running diagnostics..."
  node -e "
    const RepoScanner = require('./scripts/lib/repo-scanner.js');
    const diagnosticsConfig = require('$DIAGNOSTICS_CONFIG');
    const scanner = new RepoScanner('$repo_path', diagnosticsConfig);
    const result = scanner.scan();
    console.log(JSON.stringify(result, null, 2));
  " > "$AUDIT_DIR/${repo_id}_diagnostic_${TIMESTAMP}.json" 2>&1 || {
    echo "WARNING: Diagnostic collection failed for $repo_id, continuing..."
  }

  # Parse findings
  echo "Parsing findings..."
  node -e "
    const FindingParser = require('./scripts/lib/finding-parser.js');
    const scanResult = require('$AUDIT_DIR/${repo_id}_diagnostic_${TIMESTAMP}.json');
    const parser = new FindingParser();
    const findings = parser.parseAllDiagnostics(scanResult, '$repo_id');
    findings.forEach(f => {
      console.log(\`Finding: \${f.id} [\${f.severity}] \${f.type}: \${f.rootCause}\`);
    });
  " > "$AUDIT_DIR/${repo_id}_findings_${TIMESTAMP}.txt" 2>&1 || {
    echo "WARNING: Finding parsing failed for $repo_id, continuing..."
  }

done

echo ""
echo "=========================================="
echo "Phase 1 Complete"
echo "Output: $AUDIT_DIR/"
echo "=========================================="
