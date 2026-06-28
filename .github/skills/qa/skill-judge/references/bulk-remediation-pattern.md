# Bulk Skill Remediation Pattern

**Source:** Session 2026-06-22 — bulk remediation of 73 skills scoring below 80.

## Pattern: batch_remediate.py

When many skills share the same deficiency pattern (missing frontmatter, no Skills Required table, no Pitfalls, no Verification Checklist), use a Python script to apply fixes in bulk rather than patching one-by-one.

### Script Location
`~/AppData/Local/hermes/scripts/batch_remediate.py`

### What It Does
1. Reads `judge_results/all_results.tsv` to identify skills scoring < 80
2. For each skill, applies common fixes:
   - Adds missing frontmatter fields (`title`, `version`, `author`, `license`)
   - Adds `Skills Required` table (inserted before first `## ` section after Description)
   - Adds `Pitfalls` section (inserted before Verification Checklist or appended)
   - Adds `Verification Checklist` (appended to end)
3. Writes modified content back to disk

### Results
- **Before:** 1 PASS, 54 WARN, 19 FAIL (avg 62.9)
- **After bulk patch:** 4 PASS, 68 WARN, 2 FAIL (avg 70.7)
- 72 of 73 skills patched successfully
- Remaining 6 FAIL needed targeted patching (same script, second pass)

### Key Insight
Bulk auto-fix moves most skills from FAIL to WARN. Getting from WARN to PASS (80+) requires content-level work (concrete examples, phased workflows, reference files) that can't be auto-generated.

### Usage
```bash
# Run judge first
python3 ~/AppData/Local/hermes/scripts/batch_skill_judge.py

# Remediate
python3 ~/AppData/Local/hermes/scripts/batch_remediate.py

# Re-judge to verify
rm -f judge_results/batch_*.md judge_results/all_results.tsv judge_results/summary.md
python3 ~/AppData/Local/hermes/scripts/batch_skill_judge.py
```

### Pitfall: Verify Before Deleting Duplicates
When the orchestrator says "delete duplicate skills", ALWAYS verify the skill exists in >=2 paths before deleting any copy. If only one path exists, that's the only copy -- move it to the correct category directory instead of deleting it.
