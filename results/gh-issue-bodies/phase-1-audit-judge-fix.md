## Objective

Audit, categorize, deduplicate, judge, and remediate the 370+ local skills in `~/AppData/Local/hermes/skills/`, then produce inventory and final-verification artifacts.

## Source Plan

`plan/prompt-orchestration-comprehensive-plan.md` → Phase 1 (§4.2), sub-phases 1.1–1.7

## Deliverables

- D1 `docs/local-skills.md` — skills inventory
- D2 `docs/skill_name_to_path.json` — path mapping
- D3 `docs/categorization-plan.md` — categorization plan
- D4 `docs/dedupe-report.md` — dedupe report
- D5 `judge_results/all_results.tsv` — judge results
- D6 `judge_results/batch_*.md` — 35 batch files
- D7 `judge_results/summary.md` — summary stats
- D8 `docs/remediation-report.md`
- D9 `docs/consolidation-report.md`
- D10 `docs/final-verification.md`

## Sub-phases

1.1 Audit & Inventory · 1.2 Categorize · 1.3 Deduplicate & Consolidate · 1.4 Judge (batches of 10) · 1.5 Remediate (<80 scores) · 1.6 Consolidate Umbrellas · 1.7 Verify & Finalize

## Success Criteria

100% skills inventoried; 0 uncategorized; 0 duplicate names; avg judge score ≥ 75; FAIL (<60) = 0; 350+ skills scored.

## Safety Gates

- G1.1: `hermes skills audit` must return non-zero skills (retry once → BLOCK)
- G1.3: Verify canonical copy exists before deleting any duplicate
- G1.4: ≤10% FAIL in judge results, else stop & recalibrate
- G1.5: Remediation must improve average score (re-judge 10-skill sample)

## Dependencies

Phase 0 complete. Blocks Phase 2.
