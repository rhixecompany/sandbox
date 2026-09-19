---
name: skills-library-overhaul-2026-09-19
title: "Skills Library Overhaul — Implementation Plan"
description: "Gated plan: inventory → categorize/migrate → dedupe/consolidate → delete residuals → judge ≥98 batches → final report"
version: 1.0.0
date_created: 2026-09-19
status: Approved
goal: "Execute the skills overhaul pipeline with a verify gate after every phase"
---

# Skills Library Overhaul Plan (2026-09-19)

Spec: `.hermes/specs/skills-library-overhaul-2026-09-19.md`. Approval: clarify 2026-09-19 (A1-A5). Canonical judge: `qa/skill-judge` (5 dims × 20).

## Phase 0 — Docs (DONE when verified)

- [x] Spec written
- [x] Plan written
- [x] Prompts written: prompts/skills-library-overhaul.prompt.md
- [x] VERIFY: 3 files exist, frontmatter parse, required sections present

## Phase 1 — Inventory snapshot (execute the requested command)

1. `cd ~/Desktop/SandBox && hermes skills list --source local > ./local-skills.txt`
2. VERIFY: DONE — 1112 lines (≈1106 skills) vs find=1267 (known delta). local-skills.txt at repo root.
3. Artifact: `./local-skills.txt` (repo root). ✅

## Phase 2 — Analysis (uncategorized / duplicates / mapping)

1. Python inventory script: walk `~/AppData/Local/hermes/skills/` (depth 2) collecting per-SKILL.md: name (frontmatter), dir path, category field, lines, mtime. CRLF-normalize before frontmatter parsing.
2. Reports → `.hermes/results/skills-inventory-2026-09-19.json` + `.md`: uncategorized (no category:, or flat-root), duplicate-name groups `grep -rh "^name:" | sort | uniq -d`, near-dup name clusters (normalized prefix equality).
3. Build category mapping table (A3 conventions; see spec) for every uncategorized skill → artifact `.hermes/results/skills-category-map-2026-09-19.md`.
4. VERIFY: DONE — inventory json 1267 rows; dup groups 75 (150 files); map table 1622 lines; MISCS resolved: 343 → 14 (desc-pass) → 0 (manual); 100% assigned; name-set equality verified.

## Phase 3 — Categorize & migrate

1. For each uncategorized skill: patch frontmatter to add `category: <assigned>`; physically `mv` into `<skills>/<category>/<name>/`.
2. Prefer `scripts_unified/categorize_skills.py` if compatible (REQ-11); else python script with dry-run first.
3. VERIFY: re-scan → 0 skills without category:; every path matches `skills/<category>/<name>/SKILL.md`.

## Phase 4 — Dedupe & consolidate (canonical-name)

1. For each duplicate-name group: prove ≥2 paths (REQ-04); pick canonical = more lines/richer frontmatter; merge unique references/templates/scripts/pitfalls into canonical; `rm -rf` copies.
2. Near-name clusters (e.g. `verify-frontmatter` vs `verify-frontmatter-cjs`): keep, but only where genuinely distinct (skip ambiguous — report to user).
3. VERIFY: `uniq -d` name scan = empty; deletions manifest (kept/deleted + proof) → `.hermes/results/skills-dedupe-manifest-2026-09-19.md`.

## Phase 5 — Delete residuals (A1)

1. Re-scan uncategorized (no category: field AND flat-root): expected 0. Any found: hard delete per A1; log each.
2. VERIFY: `find` + grep → 100% categorized, 0 duplicates.

## Phase 6 — Judge to ≥98 (iterative batches)

1. Baseline: `python scripts_unified/batch_skill_judge.py --folder <skills_dir>` (or repo script) → `.hermes/results/judge_results/baseline.tsv`. NOTE batch_skill_judge.py path must not double-append SKILL.md; CRLF-normalize; fence-aware (pitfalls in qa/skill-judge).
2. Loop (batches of 7, per skill-judge batch mode): pick lowest scorers → apply fixes (REQ-08 order) → re-judge those → update `.hermes/results/judge_results/summary.tsv` + plan checkboxes + progress artifact.
3. Unsalvageable stubs → documented exceptions list (final report) if score <98 after two fix passes.
4. VERIFY: re-judge ALL → every categorized skill ≥98 (or on exceptions list).

## Phase 7 — Final verification & report

- [ ] local-skills.txt present; inventory/mapping/dedupe manifests present
- [ ] 100% categorized; 0 dups; deletions sum check (verified copies + A1 residuals)
- [ ] Score dashboard (before → after); exceptions list
- [ ] No key material, no cross-profile damage (spot-check another profile untouched)
- [ ] Completion report to user with full mapping table + manifests + evidence
- [ ] Then: resume 39-paste actionable queue (A5)

## Risks

- ~1106 skills to judge to ≥98 = many turns; mitigated by batches, progress artifact, resume-capable summary.tsv, parallel subagent batches where safe (10 parallel, each judged offline).
- Physical moves may break in-session skill index until reload — acceptable (path-based; verified via find).
- Bundled/hub skills: patch-only, never delete (per judge pitfalls).
- Judge drift across batches: calibrate thresholds on batch 1 (qa/skill-judge calibration lesson).

## PROGRESS (2026-09-19)

- Phase 0: docs verified PASS (spec/plan/prompt).
- Phase 1: `hermes skills list --source local > ./local-skills.txt` exit 0; 1112 lines.
- Phase 2: skills-inventory-2026-09-19.json (1267 SKILL.md; states: flat=523, folder-no-fm=660, categorized=84; dup groups=75/150 files); skills-category-map-2026-09-19.md (full table; assignments: development 335, devops 113, creative 63, software-development 58, productivity 49, mcp 47, qa 41, mlops 37, research 31, oh-my-hermes 31, …; misc-review 343).
- NEXT: Phase 3 migrate (dry-run first via scripts_unified/categorize_skills.py) → Phase 4 dedupe (75 groups: canonical=richer, merge, delete verified copies) → Phase 5 residuals → Phase 6 judge batches → Phase 7 report.


## PROGRESS 2 (2026-09-19 — Phases 3-5 COMPLETE)

- Phase 3 (categorize+migrate): all flat skills migrated to `skills/<cat>/<name>/`; `category:` added to every SKILL.md (660 folder skills + 483 migrated); merge-on-collision for 3 orphaned dest dirs (references/templates preserved); 2 frontmatter fixes (hermes-skills→devops, honcho-legacy name).
- Phase 4 (dedupe): 74 flat duplicate dirs deleted with canonical-twin proof; honcho false positive (frontmatter name) fixed; manifest `.hermes/results/skills-dedupe-manifest-2026-09-19.md`.
- Phase 5 (residuals): re-scan → flat=0, no_category=0 → nothing left to delete; backup tarball secured before any destructive step.
- Gate: 1267 → 1193 SKILL.md; 0 duplicates; 100% categorized (frontmatter + folder).
- NEXT: Phase 6 judge-to-≥98 bootstrapping (baseline via scripts_unified/batch_skill_judge.py → batches) + Phase 7 report.
