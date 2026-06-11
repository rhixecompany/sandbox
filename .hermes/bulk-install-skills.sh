#!/usr/bin/env bash
# Bulk install workspace skills to Hermes profile

WS_ROOT=".github/skills"
PROFILE_SKILLS="$HOME/AppData/Local/hermes/skills"

INSTALLED=0
SKIPPED=0
FAILED=0

for cat_dir in "$WS_ROOT"/*/; do
    category=$(basename "$cat_dir")
    for skill_dir in "$cat_dir"*/; do
        [[ -d "$skill_dir" ]] || continue
        [[ -f "$skill_dir/SKILL.md" ]] || continue
        
        # Extract name from SKILL.md
        name=$(grep -E '^name:' "$skill_dir/SKILL.md" | head -1 | sed 's/name: *//' | sed 's/ *$//')
        [[ -z "$name" ]] && { echo "  No name in $skill_dir/SKILL.md"; ((FAILED++)); continue; }
        
        target="$PROFILE_SKILLS/$name"
        
        if [[ -d "$target" ]]; then
            echo "  SKIP: $name (already exists)"
            ((SKIPPED++))
            continue
        fi
        
        echo "  INSTALL: $name (from $category)"
        mkdir -p "$target"
        cp -r "$skill_dir"/* "$target/"
        ((INSTALLED++))
    done
done

echo ""
echo "=== Summary ==="
echo "Installed: $INSTALLED"
echo "Skipped:   $SKIPPED"
echo "Failed:    $FAILED"