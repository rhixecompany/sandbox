#!/usr/bin/env bash
# shellcheck shell=bash

set -euo pipefail

# install-vscode-extensions.sh - Install VSCode Extensions
# Installs recommended, removes unwanted, idempotent
#
# Usage:
#   ./install-vscode-extensions.sh              # Check and report differences
#   ./install-vscode-extensions.sh --force      # Apply changes (install/remove)
#   ./install-vscode-extensions.sh --help       # Show help
#
# Exit codes:
#   0  Success (all configured correctly)
#   1  Differences detected or operation failed

set -e

# Show help
if [[ "$*" == *"--help"* ]] || [[ "$*" == *"-h"* ]]; then
  echo "ComicWise VSCode Extensions Manager"
  echo ""
  echo "Usage:"
  echo "  ./install-vscode-extensions.sh              # Check and report differences"
  echo "  ./install-vscode-extensions.sh --force      # Apply changes (install/remove)"
  echo "  ./install-vscode-extensions.sh --help       # Show this help message"
  echo ""
  echo "Configuration: .vscode/extensions.json"
  echo "  • recommendations: Extensions to install"
  echo "  • unwantedRecommendations: Extensions to remove"
  echo ""
  exit 0
fi

EXT_FILE=".vscode/extensions.json"

echo "=== VSCode Extension Manager ==="
echo ""

# Check prerequisites
if ! command -v code &> /dev/null; then
  echo "ERROR: 'code' command not found. Install VSCode CLI."
  exit 1
fi

if ! command -v jq &> /dev/null; then
  echo "ERROR: 'jq' not found. Install jq."
  exit 1
fi

if [ ! -f "$EXT_FILE" ]; then
  echo "ERROR: $EXT_FILE not found"
  exit 1
fi

# Read extensions
RECOMMENDED=$(jq -r '.recommendations[]' "$EXT_FILE")
UNWANTED=$(jq -r '.unwantedRecommendations[]' "$EXT_FILE")
REC_COUNT=$(echo "$RECOMMENDED" | grep -c . || echo 0)
UNWANT_COUNT=$(echo "$UNWANTED" | grep -c . || echo 0)

echo "Recommended: $REC_COUNT | Unwanted: $UNWANT_COUNT"
echo ""

# Get current state
INSTALLED=$(code --list-extensions)

# Idempotent check
MISSING=0
while IFS= read -r ext; do
  [ -z "$ext" ] && continue
  if ! echo "$INSTALLED" | grep -q "^$ext$"; then
    ((MISSING++))
  fi
done <<< "$RECOMMENDED"

STILL_UNWANTED=0
while IFS= read -r ext; do
  [ -z "$ext" ] && continue
  if echo "$INSTALLED" | grep -q "^$ext$"; then
    ((STILL_UNWANTED++))
  fi
done <<< "$UNWANTED"

if [ "$MISSING" -eq 0 ] && [ "$STILL_UNWANTED" -eq 0 ]; then
  echo "✓ Already configured correctly!"
  echo "  Recommended: All installed ($REC_COUNT)"
  echo "  Unwanted: All removed ($UNWANT_COUNT)"
  exit 0
fi

if [ "${1:-}" != "--force" ]; then
  echo "⚠ Differences detected. Run with --force to apply changes."
  echo "  Missing: $MISSING | Still unwanted: $STILL_UNWANTED"
  echo ""
  if [ "$MISSING" -gt 0 ]; then
    echo "Missing extensions:"
    while IFS= read -r ext; do
      [ -z "$ext" ] && continue
      if ! echo "$INSTALLED" | grep -q "^$ext$"; then
        echo "  - $ext"
      fi
    done <<< "$RECOMMENDED"
  fi
  if [ "$STILL_UNWANTED" -gt 0 ]; then
    echo "Still unwanted:"
    while IFS= read -r ext; do
      [ -z "$ext" ] && continue
      if echo "$INSTALLED" | grep -q "^$ext$"; then
        echo "  - $ext"
      fi
    done <<< "$UNWANTED"
  fi
  exit 1
fi

# Apply changes
echo "Configuring extensions..."
echo ""

# Step 1: Remove unwanted
if [ "$STILL_UNWANTED" -gt 0 ]; then
  echo "[1/3] Removing unwanted extensions ($STILL_UNWANTED)..."
  while IFS= read -r ext; do
    [ -z "$ext" ] && continue
    code --uninstall-extension "$ext" 2>/dev/null || true
    echo "  [-] $ext"
  done <<< "$UNWANTED"
  echo ""
fi

# Step 2: Install recommended in parallel
echo "[2/3] Installing recommended extensions ($REC_COUNT)..."

install_ext() {
  ext=$1
  if code --install-extension "$ext" --force 2>/dev/null; then
    echo "OK:$ext"
  else
    echo "FAIL:$ext"
  fi
}
export -f install_ext

INSTALL_FAILED=0
while IFS= read -r ext; do
  [ -z "$ext" ] && continue
  install_ext "$ext" &
done <<< "$RECOMMENDED"

wait
echo ""

# Step 3: Verify
echo "[3/3] Verifying..."
FINAL=$(code --list-extensions)

VERIFY_MISSING=0
while IFS= read -r ext; do
  [ -z "$ext" ] && continue
  if ! echo "$FINAL" | grep -q "^$ext$"; then
    ((VERIFY_MISSING++))
  fi
done <<< "$RECOMMENDED"

VERIFY_STILL_UNWANTED=0
while IFS= read -r ext; do
  [ -z "$ext" ] && continue
  if echo "$FINAL" | grep -q "^$ext$"; then
    ((VERIFY_STILL_UNWANTED++))
  fi
done <<< "$UNWANTED"

echo ""
echo "=== Results ==="
echo "Installed: $((REC_COUNT - VERIFY_MISSING))/$REC_COUNT"
echo "Removed: $((UNWANT_COUNT - VERIFY_STILL_UNWANTED))/$UNWANT_COUNT"
echo ""

if [ "$VERIFY_MISSING" -eq 0 ] && [ "$VERIFY_STILL_UNWANTED" -eq 0 ]; then
  echo "✓ SUCCESS!"
  exit 0
else
  echo "✗ Issues detected:"
  if [ "$VERIFY_MISSING" -gt 0 ]; then
    echo "  Still missing ($VERIFY_MISSING):"
    while IFS= read -r ext; do
      [ -z "$ext" ] && continue
      if ! echo "$FINAL" | grep -q "^$ext$"; then
        echo "    - $ext"
      fi
    done <<< "$RECOMMENDED"
  fi
  if [ "$VERIFY_STILL_UNWANTED" -gt 0 ]; then
    echo "  Still installed ($VERIFY_STILL_UNWANTED):"
    while IFS= read -r ext; do
      [ -z "$ext" ] && continue
      if echo "$FINAL" | grep -q "^$ext$"; then
        echo "    - $ext"
      fi
    done <<< "$UNWANTED"
  fi
  exit 1
fi
