#!/bin/bash
# VSCode Extension Manager
# Installs recommended, removes unwanted, idempotent

set -e

EXT_FILE=".vscode/extensions.json"

echo "=== VSCode Extension Manager ==="

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
    echo -e "\nAlready configured correctly!"
    echo "Recommended: All installed ($REC_COUNT)"
    echo "Unwanted: All removed ($UNWANT_COUNT)"
    exit 0
fi

if [ "${1:-}" != "--force" ]; then
    echo -e "\nDifferences detected. Run with --force to apply changes."
    echo "Missing: $MISSING | Still unwanted: $STILL_UNWANTED"
    echo -e "\nMissing extensions:"
    while IFS= read -r ext; do
        [ -z "$ext" ] && continue
        if ! echo "$INSTALLED" | grep -q "^$ext$"; then
            echo "  - $ext"
        fi
    done <<< "$RECOMMENDED"
    echo -e "\nStill unwanted:"
    while IFS= read -r ext; do
        [ -z "$ext" ] && continue
        if echo "$INSTALLED" | grep -q "^$ext$"; then
            echo "  - $ext"
        fi
    done <<< "$UNWANTED"
    exit 1
fi

# Step 1: Remove unwanted
if [ "$STILL_UNWANTED" -gt 0 ]; then
    echo -e "\n[1/4] Removing unwanted extensions ($STILL_UNWANTED)..."
    while IFS= read -r ext; do
        [ -z "$ext" ] && continue
        code --uninstall-extension "$ext" 2>/dev/null || true
        echo -e "  [-] \033[0;31m$ext\033[0m"
    done <<< "$UNWANTED"
fi

# Step 2: Uninstall all (clean slate)
echo -e "\n[2/4] Uninstalling all extensions..."
echo "$INSTALLED" | xargs -P 8 -I {} code --uninstall-extension {} 2>/dev/null || true

# Step 3: Install recommended in parallel
echo -e "\n[3/4] Installing recommended extensions ($REC_COUNT)..."

# Export function for parallel
install_ext() {
    ext=$1
    if code --install-extension "$ext" --force 2>/dev/null; then
        echo "OK:$ext"
    else
        echo "FAIL:$ext"
    fi
}
export -f install_ext

while IFS= read -r ext; do
    [ -z "$ext" ] && continue
    install_ext "$ext" &
done <<< "$RECOMMENDED"

# Wait for all background jobs
wait

# Step 4: Verify
echo -e "\n[4/4] Verifying..."
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

# Report
echo -e "\n=== Results ==="
echo "Installed: $((REC_COUNT - VERIFY_MISSING))/$REC_COUNT"
echo "Removed: $((UNWANT_COUNT - VERIFY_STILL_UNWANTED))/$UNWANT_COUNT"

if [ "$VERIFY_MISSING" -gt 0 ]; then
    echo -e "\nStill missing ($VERIFY_MISSING):"
    while IFS= read -r ext; do
        [ -z "$ext" ] && continue
        if ! echo "$FINAL" | grep -q "^$ext$"; then
            echo "  - $ext"
        fi
    done <<< "$RECOMMENDED"
fi

if [ "$VERIFY_STILL_UNWANTED" -gt 0 ]; then
    echo -e "\nStill installed ($VERIFY_STILL_UNWANTED):"
    while IFS= read -r ext; do
        [ -z "$ext" ] && continue
        if echo "$FINAL" | grep -q "^$ext$"; then
            echo "  - $ext"
        fi
    done <<< "$UNWANTED"
fi

if [ "$VERIFY_MISSING" -eq 0 ] && [ "$VERIFY_STILL_UNWANTED" -eq 0 ]; then
    echo -e "\n\033[0;32mSUCCESS!\033[0m"
    exit 0
else
    echo -e "\n\033[0;31mISSUES DETECTED\033[0m"
    exit 1
fi
