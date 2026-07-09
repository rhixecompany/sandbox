# DRY_RUN_SUPPORT=true
#!/usr/bin/env bash
# shellcheck shell=bash

# Phase 2: Light Inventory for MEDIUM+LOW repos
# Quick snapshot of 13 medium and low priority repos

set -euo pipefail

REPO_INVENTORY="./scripts/config/repo-inventory.json"
AUDIT_DIR="./docs/audits"
TIMESTAMP=$(date +%Y-%m-%d_%H-%M-%S)

echo "=========================================="
echo "Phase 2: Light Inventory (MEDIUM+LOW repos)"
echo "=========================================="

# Get all MEDIUM and LOW repos
MEDIUM_LOW_REPOS=$(node -e "
  const inventory = require('$REPO_INVENTORY');
  inventory.repos
    .filter(r => r.priority === 'MEDIUM' || r.priority === 'LOW')
    .forEach(r => console.log(r.id));
")

for repo_id in $MEDIUM_LOW_REPOS; do
  echo ""
  echo "Inventory: $repo_id"
  echo "---"

  # Get repo info from inventory
  repo_info=$(node -e "
    const inventory = require('$REPO_INVENTORY');
    const repo = inventory.repos.find(r => r.id === '$repo_id');
    if (repo) console.log(JSON.stringify(repo, null, 2));
  ")

  if [ -z "$repo_info" ]; then
    echo "ERROR: Repo $repo_id not found"
    continue
  fi

  # Extract path
  repo_path=$(echo "$repo_info" | grep -o '"path": "[^"]*"' | cut -d'"' -f4)

  if [ ! -d "$repo_path" ]; then
    echo "WARNING: Path does not exist: $repo_path"
    continue
  fi

  # Quick inventory
  echo "$repo_info" > "$AUDIT_DIR/${repo_id}_inventory_${TIMESTAMP}.json"
  echo "Files: $(find "$repo_path" -type f | wc -l)"
  echo "Directories: $(find "$repo_path" -type d | wc -l)"

  # Check for key files
  [ -f "$repo_path/package.json" ] && echo "  ✓ package.json" || echo "  ✗ package.json"
  [ -f "$repo_path/tsconfig.json" ] && echo "  ✓ tsconfig.json" || echo "  ✗ tsconfig.json"
  [ -f "$repo_path/pyproject.toml" ] && echo "  ✓ pyproject.toml" || echo "  ✗ pyproject.toml"
  [ -f "$repo_path/setup.py" ] && echo "  ✓ setup.py" || echo "  ✗ setup.py"
  [ -f "$repo_path/README.md" ] && echo "  ✓ README.md" || echo "  ✗ README.md"
  [ -f "$repo_path/.git/config" ] && echo "  ✓ git repository" || echo "  ✗ git repository"

done

echo ""
echo "=========================================="
echo "Phase 2 Complete"
echo "Output: $AUDIT_DIR/"
echo "=========================================="
