---
author: Alexa
description: 'Use for running the full skills audit pipeline: inventory, categorize,
  deduplicate, judge, remediate, consolidate, and verify all Hermes skills.'
license: MIT
metadata:
  hermes:
    category: qa
    tags:
    - skills
    - audit
    - judge
    - remediation
    - pipeline
    - dedup
name: audit-skills-judge-fix
tags:
- skills
- audit
- judge
- remediation
- pipeline
- dedup
title: Audit Skills Judge Fix
version: 2.0.0

---

# Audit Skills Judge Fix Pipeline

## Current State (2026-06-22)
| Metric | Value |
|--------|-------|
| Total skills | 343 |
| PASS (≥80) | 82 (23%) |
| WARN (60-79) | 261 (76%) |
| FAIL (<60) | 0 (0%) |
| Average score | 73.6/100 |

## Scripts in `~/AppData/Local/hermes/scripts/`

| Script | Purpose |
|--------|---------|
| `batch_skill_judge.py` | Score all skills on 5 dimensions (20pts each). Supports `--resume`. |
| `batch_remediate.py` | Add missing frontmatter, pitfalls, verification checklist to sub-80 skills |
| `batch_rewrite_worst.py` | Full rewrite template for FAIL skills (hardcoded list — needs update) |
| `batch_remediate_42_59.py` | Aggressive patching for 42-59 scoring skills |
| `dedupe_skills.py` | Find same-name skills across multiple paths |
| `consolidate_skills.py` | Identify overlapping skills by keyword/tag |
| `merge_skill.py` | Merge a thin skill into an umbrella |
| `categorize_skills.py` | Add `metadata.hermes.category` to flat skills |
| `fix_yaml_frontmatter.py` | Repair YAML description quoting issues |
| `build_path_mapping.py` | Rebuild `skill_name_to_path.json` from disk |
| `fix_fail_skills.py` | Add reference files + phased workflows to FAIL skills |
| `audit_prompts.py` | Audit prompt files for formatting issues |

## Pipeline Workflow

### Phase 1: Audit & Inventory
```bash
hermes skills audit
hermes skills check
hermes skills update
hermes skills list --source local > docs/local-skills.md
find ~/AppData/Local/hermes/skills -name "SKILL.md" | wc -l
python3 ~/AppData/Local/hermes/scripts/build_path_mapping.py
```

### Phase 2: Categorize
```bash
python3 ~/AppData/Local/hermes/scripts/categorize_skills.py
# Verify: 0 skills with empty category in CLI display
```

### Phase 3: Deduplicate
```bash
python3 ~/AppData/Local/hermes/scripts/dedupe_skills.py
# Review docs/dedupe-report.md, delete flat duplicates
```

### Phase 4: Judge
```bash
cd ~/Desktop/SandBox
rm -f judge_results/batch_*.md judge_results/all_results.tsv judge_results/summary.md
python3 ~/AppData/Local/hermes/scripts/batch_skill_judge.py
```

### Phase 5: Remediate
```bash
# Structural fixes (all below 80)
python3 ~/AppData/Local/hermes/scripts/batch_remediate.py

# YAML frontmatter fixes
python3 ~/AppData/Local/hermes/scripts/fix_yaml_frontmatter.py

# FAIL skill rewrites (reference files + phases)
python3 ~/AppData/Local/hermes/scripts/fix_fail_skills.py

# Re-judge after fixes
rm -f judge_results/*.tsv judge_results/summary.md judge_results/batch_*.md
python3 ~/AppData/Local/hermes/scripts/batch_skill_judge.py

# Generate lists
python3 -c "
import csv
r = csv.DictReader(open('judge_results/all_results.tsv'), delimiter='\t')
below = [row for row in r if int(row['score']) < 80]
needs = [r for r in below if int(r['score']) >= 60]
rewrite = [r for r in below if int(r['score']) < 60]
open('judge_results/below_80_list.txt','w').writelines(f'{r[\"score\"]} {r[\"skill_name\"]}\n' for r in below)
open('judge_results/needs_work_list.txt','w').writelines(f'{r[\"score\"]} {r[\"skill_name\"]}\n' for r in needs)
open('judge_results/rewrite_list.txt','w').writelines(f'{r[\"score\"]} {r[\"skill_name\"]}\n' for r in rewrite)
print(f'Below 80: {len(below)}, Needs work: {len(needs)}, Rewrite: {len(rewrite)}')
"
```

### Phase 6: Consolidate
```bash
python3 ~/AppData/Local/hermes/scripts/consolidate_skills.py
```

### Phase 7: Verify
- Check `judge_results/summary.md` for score distribution
- Check `docs/audit-skills-judge-fix-report.md` for full report
- Commit: `git add docs/ judge_results/ && git commit -m "chore: skills audit pipeline $(date +%F)"`

## Known Issues
1. **batch_rewrite_worst.py** has a hardcoded list of 30 skills — needs dynamic reading from `rewrite_list.txt`
2. **consolidate_skills.py** reports 3000+ keyword overlaps (mostly noise — "install", "model") — only the thin skills (<100 lines) are actionable
3. **Skill count drift:** `hermes skills list` shows ~201 (its own inventory) while `find` shows ~343 (disk count) — the difference is skills in flat dirs that hermes doesn't index

## Script Fixes Applied (2026-06-22)
- `batch_skill_judge.py`: Depth filter changed from `<=2` to `<=3` to include category subdir skills
- `batch_remediate.py`: Path resolution fixed to not double-append `SKILL.md`

## Pitfalls
- **CRLF line endings:** Files use `\r\n` on Windows. Regex patterns with `\n` must account for this.
- **YAML description quoting:** Description fields with embedded double quotes break `yaml.safe_load()`. Fix with `fix_yaml_frontmatter.py`.
- **Stale cache:** After editing skills, always re-judge fresh (don't trust old results).
- **Dedup before judge:** Always deduplicate before judging to avoid double-counting.

## Verification Checklist

- [ ] Skill has clear purpose and structured workflow
- [ ] Frontmatter is complete and valid
- [ ] All reference files exist and are substantive
- [ ] No placeholder text
