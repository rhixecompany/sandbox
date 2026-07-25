# AI-Readiness Scoring for Markdown Documentation

Scoring methodology to evaluate how well a `.md` file can be consumed by both human readers and AI agents (LLMs, RAG systems, code assistants).

## Scoring Rubric

| Criterion | Points | Detection Method | Why It Matters |
|-----------|--------|-----------------|----------------|
| YAML frontmatter present | +20 | `grep -c '^---$' first 5 lines` | AI agents parse frontmatter for context, routing, and metadata |
| Summary paragraph in first 3 lines | +15 | Non-empty paragraph within 3 lines after H1 | AI snippets truncate after ~3 lines; summary ensures the signal survives |
| Language-tagged code blocks | +10 each (max +30) | Count ` ```<lang>\n` patterns | Untagged blocks get no syntax highlighting and confuse AI language detection |
| Relative cross-refs that resolve | +10 each (max +20) | Check each `](./path)` with `test -f` | Broken links produce 404s for humans and hallucinations for AI |
| H2/H3 break every <200 lines | +15 | Count lines between `^##` and `^###` markers | Walls of text exceed AI context windows and lose human readers |
| **Penalty**: >500 lines with no H2/H3 | −20 | No heading after first 500 lines | Pure wall-of-text — both humans and AI will skip it |

**Maximum score: 100**

## Thresholds

| Score | Rating | Action |
|-------|--------|--------|
| ≥70 | **AI-ready** | Document passes automated check. Minor improvements optional. |
| 40–69 | **Needs work** | Document is readable but will lose points in AI retrieval. Add missing frontmatter, summary, or code tags. |
| <40 | **Rewrite required** | Document is a wall of text with no structure. Restructure with H2/H3 sections, add frontmatter and summary. |

## Scoring Script Template

```bash
#!/usr/bin/env bash
# score-docs.sh — Score all .md files for AI-readiness
# Usage: bash score-docs.sh [directory]

SCORE_DIR="${1:-docs}"
SUMMARY_FILE="${SCORE_DIR}/ai-readiness-report.md"

echo "# AI-Readiness Report" > "$SUMMARY_FILE"
echo "" >> "$SUMMARY_FILE"
echo "| File | Score | Rating | Key Gaps |" >> "$SUMMARY_FILE"
echo "|------|-------|--------|----------|" >> "$SUMMARY_FILE"

TOTAL=0
PASS=0
FAIL=0

find "$SCORE_DIR" -name '*.md' -not -path '*/node_modules/*' | while read -r file; do
  score=0
  gaps=""

  # 1. YAML frontmatter (+20)
  if head -5 "$file" | grep -c '^---$' > /dev/null 2>&1; then
    score=$((score + 20))
  else
    gaps="${gaps}no-frontmatter "
  fi

  # 2. Summary in first 3 lines after H1 (+15)
  summary=$(sed -n '/^# /,/^$/p' "$file" | head -6 | tail -4 | grep -v '^#' | grep -v '^$' | head -1)
  if [ -n "$summary" ] && [ ${#summary} -gt 20 ]; then
    score=$((score + 15))
  else
    gaps="${gaps}no-summary "
  fi

  # 3. Language-tagged code blocks (+10 each, max +30)
  lang_blocks=$(grep -c '^```[a-zA-Z]' "$file" 2>/dev/null || echo 0)
  block_points=$((lang_blocks * 10))
  [ "$block_points" -gt 30 ] && block_points=30
  score=$((score + block_points))
  [ "$lang_blocks" -eq 0 ] && gaps="${gaps}no-lang-tags "

  # 4. Relative cross-refs that resolve (+10 each, max +20)
  dir=$(dirname "$file")
  refs=0
  while IFS= read -r ref; do
    target="${dir}/${ref}"
    if [ -f "$target" ]; then
      refs=$((refs + 1))
    fi
  done < <(grep -oP '\]\(\./[^)]+\)' "$file" 2>/dev/null | sed 's/\]\(\.\//\//' | sed 's/)$//' | sed 's/^//')
  ref_points=$((refs * 10))
  [ "$ref_points" -gt 20 ] && ref_points=20
  score=$((score + ref_points))

  # 5. H2/H3 breaks (+15)
  total_lines=$(wc -l < "$file")
  section_count=$(grep -c '^##\|^###' "$file" 2>/dev/null || echo 0)
  if [ "$section_count" -gt 0 ]; then
    avg_lines_per_section=$((total_lines / section_count))
    [ "$avg_lines_per_section" -lt 200 ] && score=$((score + 15))
  fi

  # Penalty: >500 lines with no headings
  if [ "$total_lines" -gt 500 ] && [ "$section_count" -eq 0 ]; then
    score=$((score - 20))
    gaps="${gaps}wall-of-text "
  fi

  # Rating
  if [ "$score" -ge 70 ]; then
    rating="✅ AI-ready"
    pass=$((pass + 1))
  elif [ "$score" -ge 40 ]; then
    rating="⚠️ Needs work"
    fail=$((fail + 1))
  else
    rating="❌ Rewrite"
    fail=$((fail + 1))
  fi

  total=$((total + 1))
  echo "| $file | $score | $rating | $gaps |" >> "$SUMMARY_FILE"
done

echo "" >> "$SUMMARY_FILE"
echo "**Summary: $total files — $pass AI-ready, $fail need work**" >> "$SUMMARY_FILE"
echo "Report: $SUMMARY_FILE"
```

## Usage in enhance-markdown

After Phase 4 (Verification) completes, optionally run AI-readiness scoring to produce a quantitative metric:

```
/enhance-markdown --score-docs [directory]
```

The scoring report (`docs/ai-readiness-report.md`) becomes an input to the next enhancement cycle, forming a continuous improvement loop: score → fix → re-score.
