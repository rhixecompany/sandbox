# DRY_RUN_SUPPORT=true
#!/usr/bin/env bash
# shellcheck shell=bash
# score-docs.sh: Score all .md files on AI-readiness (0-100)
# Usage: bash score-docs.sh [target_directory]
# Output: docs/ai-readiness-report.md

set -euo pipefail

TARGET_DIR="${1:-.}"
OUTPUT_FILE="docs/ai-readiness-report.md"
SCORE_TABLE=$(mktemp)
SCORE_JSON=$(mktemp)

total_files=0
total_score=0
max_score=0

echo "# AI-Readiness Report" > "$OUTPUT_FILE"
echo "" >> "$OUTPUT_FILE"
echo "**Generated**: $(date)" >> "$OUTPUT_FILE"
echo "**Scope**: \`$TARGET_DIR\`" >> "$OUTPUT_FILE"
echo "" >> "$OUTPUT_FILE"
echo "| File | FM+20 | Summary+15 | LangTags+30 | XRefs+20 | Structure+15 | Penalty | Score | Verdict |" >> "$OUTPUT_FILE"
echo "|------|-------|------------|-------------|----------|--------------|---------|-------|---------|" >> "$OUTPUT_FILE"

echo "[" > "$SCORE_JSON"
first=true

# Find all .md files excluding node_modules and .git
find "$TARGET_DIR" -name '*.md' -not -path '*/node_modules/*' -not -path '*/.git/*' -not -path '*/\.*' 2>/dev/null | while read -r file; do
    total_files=$((total_files + 1))
    score=0
    fm_score=0
    summary_score=0
    lang_score=0
    xref_score=0
    struct_score=0
    penalty=0

    # Read first 5 lines
    head_content=$(head -5 "$file" 2>/dev/null)

    # Criterion 1: YAML frontmatter (+20)
    if echo "$head_content" | grep -q '^---'; then
        fm_score=20
        score=$((score + 20))
    fi

    # Get total lines and full content for other checks
    total_lines=$(wc -l < "$file" 2>/dev/null || echo 0)
    full_content=$(cat "$file" 2>/dev/null || echo "")

    # Criterion 2: Summary paragraph in first 3 lines after H1 (+15)
    h1_line=$(echo "$full_content" | grep -n '^# ' | head -1 | cut -d: -f1 || echo 0)
    if [ "$h1_line" -gt 0 ] 2>/dev/null; then
        after_h1=$(echo "$full_content" | tail -n +$((h1_line + 1)) | head -3)
        if echo "$after_h1" | grep -qE '^[A-Za-z].{20,}'; then
            summary_score=15
            score=$((score + 15))
        fi
    fi

    # Criterion 3: Language-tagged code blocks (+10 each, max +30)
    lang_count=$(echo "$full_content" | grep -cE '^```[a-zA-Z]' 2>/dev/null || echo "0")
    lang_count="${lang_count%%[$'\n\r ']*}"  # strip any trailing whitespace/newlines
    lang_count="${lang_count##*[$'\n\r ']}"
    [ -z "$lang_count" ] && lang_count=0
    lang_score=$((lang_count * 10))
    [ "$lang_score" -gt 30 ] && lang_score=30
    score=$((score + lang_score))

    # Criterion 4: Relative cross-refs that resolve (+10 each, max +20)
    file_dir=$(dirname "$file")
    xref_count=0
    while IFS= read -r link; do
        link=$(echo "$link" | sed 's/.*\](\([^)]*\)).*/\1/' 2>/dev/null)
        # Only check relative links (no http://, no #fragment-only)
        if echo "$link" | grep -qE '^\.\.?/' && [ -f "$file_dir/$link" ] 2>/dev/null; then
            xref_count=$((xref_count + 1))
        fi
    done < <(echo "$full_content" | grep -oE '\[.*\]\(\.\.?/[^)]+\)' 2>/dev/null || echo "")
    xref_score=$((xref_count * 10))
    [ "$xref_score" -gt 20 ] && xref_score=20
    score=$((score + xref_score))

    # Criterion 5: H2/H3 break every <200 lines (+15)
    header_count=$(echo "$full_content" | grep -cE '^## |^### ' 2>/dev/null || echo "0")
    header_count="${header_count%% *}"  # strip trailing spaces
    header_count="${header_count##* }"
    [ -z "$header_count" ] && header_count=0
    
    if [ "${total_lines:-0}" -gt 0 ] && [ "${header_count:-0}" -gt 0 ] 2>/dev/null; then
        lines_per_header=$((total_lines / header_count))
        if [ "$lines_per_header" -lt 200 ] 2>/dev/null; then
            struct_score=15
            score=$((score + 15))
        fi
    fi

    # Penalty: >500 lines with no H2/H3 (-20)
    if [ "${total_lines:-0}" -gt 500 ] && [ "${header_count:-0}" -eq 0 ] 2>/dev/null; then
        penalty=20
        score=$((score - 20))
    fi

    [ "$score" -lt 0 ] && score=0

    # Verdict
    if [ "$score" -ge 70 ]; then
        verdict="AI-READY ✅"
    elif [ "$score" -ge 40 ]; then
        verdict="NEEDS WORK ⚠️"
    else
        verdict="REWRITE ❌"
    fi

    # Relative path for display
    rel_path="${file#$TARGET_DIR/}"
    [ "$rel_path" = "$file" ] && rel_path="$file"

    echo "| $rel_path | $fm_score | $summary_score | $lang_score | $xref_score | $struct_score | -$penalty | **$score** | $verdict |" >> "$OUTPUT_FILE"

    if [ "$first" = true ]; then
        first=false
    else
        echo "," >> "$SCORE_JSON"
    fi
    echo "  {\"file\": \"$rel_path\", \"score\": $score, \"verdict\": \"$verdict\"}" >> "$SCORE_JSON"
done

echo "]" >> "$SCORE_JSON"

# Summary
echo "" >> "$OUTPUT_FILE"
echo "## Summary" >> "$OUTPUT_FILE"
echo "" >> "$OUTPUT_FILE"

ready=$(grep -c 'AI-READY' "$OUTPUT_FILE" 2>/dev/null || echo 0)
needs_work=$(grep -c 'NEEDS WORK' "$OUTPUT_FILE" 2>/dev/null || echo 0)
rewrite=$(grep -c 'REWRITE' "$OUTPUT_FILE" 2>/dev/null || echo 0)
total=$(grep -c '| \*\*' "$OUTPUT_FILE" 2>/dev/null || echo 0)

echo "| Metric | Count |" >> "$OUTPUT_FILE"
echo "|--------|-------|" >> "$OUTPUT_FILE"
echo "| Total files scored | $total_files |" >> "$OUTPUT_FILE"
echo "| AI-ready (>=70) | $ready |" >> "$OUTPUT_FILE"
echo "| Needs work (40-69) | $needs_work |" >> "$OUTPUT_FILE"
echo "| Rewrite required (<40) | $rewrite |" >> "$OUTPUT_FILE"

rm -f "$SCORE_TABLE" "$SCORE_JSON"

echo "Report saved to $OUTPUT_FILE"
echo "Files scored: $total_files"
echo "AI-ready: $ready"
echo "Needs work: $needs_work"
echo "Rewrite: $rewrite"
