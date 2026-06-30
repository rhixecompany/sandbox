# Audit Skills Judge Fix — Phases

> Full operational phases for `prompts/audit-skills-judge-fix.prompt.md`.

## Phase 1: Skills Audit & Inventory
- Run skills audit and inventory across `~/AppData/Local/hermes/skills/`.
- Produce `docs/local-skills.md`, `skill_inventory.json`, and `skill_name_to_path.json`.
- Gate: inventory artifacts exist and paths are valid.

## Phase 2: Categorize Skills
- Categorize skills into correct category folders.
- Gate: 0 empty categories; mapping saved.

## Phase 3: Deduplicate & Consolidate
- Detect duplicate/overlapping skills; merge or delete with `skill_manage`.
- Write `docs/dedupe-report.md`.
- Gate: duplicates resolved and report written.

## Phase 4: Judge Skills
- Judge skills in batches of 10 using `batch_skill_judge.py` in `~/AppData/Local/hermes/scripts/`.
- Save to `judge_results/all_results.tsv` and `judge_results/summary.md`.
- Gate: all skills scored and results written.

## Phase 5: Remediate Skills
- Patch skills scoring < 80 using remediation scripts.
- Write `judge_results/remediation_report.md`.
- Gate: no skill remains below 80.

## Phase 6: Consolidate Umbrella Skills
- Merge thin/overlapping skills into umbrella skills; update absorbed skill records.
- Write `docs/consolidation-report.md`.
- Gate: consolidation report written.

## Phase 7: Final Verification
- Re-run validator/size checks; confirm categorization, dedupe, and judging.
- Write `docs/final-verification.md`.
- Gate: final report shows pass with zero unresolved issues.
