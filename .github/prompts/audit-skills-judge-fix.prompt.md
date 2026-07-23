---
name: audit-skills-judge-fix
...
title: Audit Skills Judge Fix
...
description: 'Run the full skills audit pipeline: inventory, audit, categorize, dedupe, judge,
  remediate, consolidate, and verify Hermes skills.'
version: 1.0.0
...
license: MIT
...
author: Hermes Agent
...
toolsets: - terminal
- file
scripts: []
skills: - using-superpowers
- user-communication-preferences
- verification-before-completion
formatter: default
...
plan: ''
dependencies: - skill:using-superpowers
- skill:user-communication-preferences
- skill:verification-before-completion
tags: - audit
- judge
- remediation
- pipeline
trigger: /audit-skills-judge-fix
...
---

# Audit Skills Judge Fix

> Strict sequential execution. Complete each phase before advancing.

## Context

- **Workspace root:** `C:\Users\Alexa\Desktop\SandBox`
- **Hermes skills root:** `%LOCALAPPDATA%\hermes\skills`
- **Outputs:** `docs/local-skills.md`, `judge_results/`, `docs/audit-skills-judge-fix-report.md`
- **Reference skill:** `audit-skills-judge-fix` at `~/AppData/Local/hermes/skills/qa/audit-skills-judge-fix/SKILL.md`

## Rules

1. Run phases in order without reordering.
2. Verify each phase before proceeding.
3. Do not delete evidence artifacts before verification.
4. Re-judge after every remediation pass.
5. Capture Judith score distribution into a report.

## Phase 1: Audit & Inventory

1. Verify or restore official skills: `hermes skills repair-official --restore --yes all`
2. Inventory skills: `hermes skills list --source local > docs/local-skills.md`
3. Count skill files: `find "$LOCALAPPDATA/hermes/skills" -name "SKILL.md" | wc -l`
4. Run audit: `hermes skills audit`
5. Rebuild path mapping: `python3 "$LOCALAPPDATA/hermes/scripts/build_path_mapping.py"`

**Exit:** `docs/local-skills.md` written, baseline counts recorded.

---

## Phase 2: Categorize + Deduplicate

1. Categorize: `python3 "$LOCALAPPDATA/hermes/scripts/categorize_skills.py"`
2. Deduplicate: `python3 "$LOCALAPPDATA/hermes/scripts/dedupe_skills.py"`
3. Review `docs/dedupe-report.md`
4. Delete flat duplicates only after review

**Exit:** No duplicated active skills remaining; dedupe report written.

---

## Phase 3: Judge

```bash
cd C:/Users/Alexa/Desktop/SandBox
rm -f judge_results/batch_*.md judge_results/all_results.tsv judge_results/summary.md
python3 "$LOCALAPPDATA/hermes/scripts/batch_skill_judge.py"
```

**Exit:** `judge_results/summary.md` exists and reflects current disk state.

---

## Phase 4: Remediate

1. Structural fixes below 80: `python3 "$LOCALAPPDATA/hermes/scripts/batch_remediate.py"`
2. YAML fixes: `python3 "$LOCALAPPDATA/hermes/scripts/fix_yaml_frontmatter.py"`
3. FAIL skill rewrites: `python3 "$LOCALAPPDATA/hermes/scripts/fix_fail_skills.py"`
4. Re-judge: rerun Phase 3
5. Record lists:
   - `judge_results/below_80_list.txt`
   - `judge_results/needs_work_list.txt`
   - `judge_results/rewrite_list.txt`

**Exit:** Re-judge artifacts updated; score distribution documented.

---

## Phase 5: Deep Patch + Boost Near Pass

1. Quick first-aid: `python3 "$LOCALAPPDATA/hermes/scripts/patch_fail_structure.py"`
2. Re-judge
3. Full structure injection: `python3 "$LOCALAPPDATA/hermes/scripts/patch_all_fail_sections.py"`
4. Re-judge
5. Near-pass boost: `python3 "$LOCALAPPDATA/hermes/scripts/boost_near_pass_refs.py"`
6. Final re-judge

**Exit:** Final `judge_results/summary.md` reflects remediation.

---

## Phase 6: Consolidate

1. Consolidate: `python3 "$LOCALAPPDATA/hermes/scripts/consolidate_skills.py"`
2. Re-run audit: `hermes skills audit`
3. Re-run judge once more if audit indicates regression

**Exit:** Consolidation report updated.

---

## Phase 7: Verify & Report

1. Verify score distribution from `judge_results/summary.md`
2. Verify report at `docs/audit-skills-judge-fix-report.md`
3. Commit: `git add docs/ judge_results/ && git commit -m "chore: skills audit pipeline $(date +%F)"`

**Verification:** user-communication-preferences verification checklist satisfied; no hardcoded Windows paths in patched scripts.
