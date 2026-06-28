---
license: MIT
author: Hermes Agent
version: 1.0.0
title: Audit Skills Judge Fix
name: audit-skills-judge-fix
trigger: /audit-skills-judge-fix
description: >-
  Run full skills audit, categorize, dedupe, consolidate, judge in batches of 10,
  remediate all reference files/scripts/SKILL.md, delete duplicates, and verify completion.
tags:
  - hermes
  - copilot
  - opencode
  - skills
  - audit
  - judge
  - remediation
  - dedupe
  - consolidation
dependencies:
  - skill:using-superpowers
  - skill:user-communication-preferences
  - skill:plans-and-specs
  - skill:skill-judge
  - skill:hermes-skills
  - skill:skill-creator
  - skill:writing-skills
skills:
  - using-superpowers
  - user-communication-preferences
  - plans-and-specs
  - skill-judge
  - hermes-skills
  - skill-creator
  - writing-skills
---

# Audit Skills Judge Fix

> Orchestrates a comprehensive skills audit, categorization, deduplication, consolidation, judging, and remediation workflow.

## Description

This prompt runs a full skills audit pipeline: inventory all local skills, categorize them into correct folders, deduplicate and consolidate overlapping skills, judge each skill's quality in batches of 10, remediate all issues (reference files, scripts, SKILL.md), delete duplicate skills, and verify the entire plan is complete. Execution is sequential — each phase must finish before the next begins.

**Critical rules:**

- Execute `hermes skills audit` in background without timeout; wait before proceeding
- Judge in batches of 10; raise ALL scores above 80
- Deduplicate BEFORE judging — merge or delete duplicate skills first
- Consolidate overlapping skills into umbrella skills using `skill_manage(action='delete', absorbed_into=...)`
- Do not stop until plan and specs are fully completed
- All Python scripts go to `~/AppData/Local/hermes/scripts/`

## Context

- **Source reference:** (removed; canonical `.prompt.md` kept)
- **Target scope:** All local skills in `~/AppData/Local/hermes/skills/`
- **Phase 1 output:** `docs/local-skills.md`
- **Phase 2 output:** `docs/categorization-plan.md`
- **Phase 3 output:** `docs/dedupe-report.md`
- **Phase 4 output:** `judge_results/all_results.tsv`, `judge_results/summary.md`
- **Phase 5 output:** `judge_results/remediation_report.md`
- **Phase 6 output:** `docs/consolidation-report.md`
- **Phase 7 output:** `docs/final-verification.md`
- **Execution environment:** Windows 11, bash (git-bash/MSYS), Hermes CLI

## Skills Required

| Skill                            | Purpose                                           |
| -------------------------------- | ------------------------------------------------- |
| `using-superpowers`              | Establishes workflow foundation                   |
| `user-communication-preferences` | Loads user prefs for execution style              |
| `plans-and-specs`                | Creates implementation plan from goal             |
| `skill-judge`                    | Evaluates skill quality against criteria (v1.1.0) |
| `hermes-skills`                  | Skills discovery, install, management             |
| `skill-creator`                  | Author in-repo SKILL.md                           |
| `writing-skills`                 | Write clear skill prose and structure             |

## Rules

1. **Sequential execution** — Each phase must complete before the next begins ("only then" constraint)
2. **Batch size** — Judge skills in batches of 10
3. **Quality gate** — All skill scores must exceed 80
4. **Dedupe first** — Identify and remove/merge duplicate skills BEFORE judging
5. **Consolidate overlaps** — Merge thin/overlapping skills into umbrella skills
6. **Completeness** — Do not stop until plan and specs are fully completed
7. **Scripts location** — All Python scripts in `~/AppData/Local/hermes/scripts/`

## Phases

> ### Phase 1: Skills Audit & Inventory
> **Goal:** Produce a complete inventory of all local skills.

> **Full content:** `templates/audit-skills-judge-fix/phases.md`

## Actions Summary

1. Run skills audit & inventory → `docs/local-skills.md`
2. Categorize skills into correct folders
3. Deduplicate & consolidate overlapping skills → `docs/dedupe-report.md`
4. Judge all skills in batches of 10 → `judge_results/all_results.tsv`
5. Remediate skills scoring < 80 → patched/rewritten SKILL.md files
6. Consolidate umbrella skills → `docs/consolidation-report.md`
7. Verify all skills ≥ 80, categorized, deduped → `docs/final-verification.md`

## Python Scripts Reference

All scripts located at `~/AppData/Local/hermes/scripts/`:

| Script                     | Purpose                                                     | Phase |
| -------------------------- | ----------------------------------------------------------- | ----- |
| `batch_skill_judge.py`     | Batch score all skills on 5 dimensions (skill-judge v1.1.0) | 4, 7  |
| `batch_remediate.py`       | Patch skills scoring 60-79 (frontmatter, structure)         | 5     |
| `batch_remediate_42_59.py` | Patch skills scoring 42-59 (more aggressive)                | 5     |
| `batch_rewrite_worst.py`   | Full rebuild of skills scoring <60                          | 5     |
| `dedupe_skills.py`         | Find duplicate SKILL.md files across skill directories      | 3     |
| `consolidate_skills.py`    | Identify overlapping skills for merge                       | 3, 6  |
| `merge_skill.py`           | Merge thin skill into umbrella skill                        | 3, 6  |
| `audit_prompts.py`         | Audit prompt files for formatting/structural issues         | 1     |
| `skill_inventory.json`     | Generated mapping of all SKILL.md paths                     | 1     |
| `skill_name_to_path.json`  | Generated mapping of skill name → canonical path            | 1     |

## Verification Checklist

- [ ] Phase 1: Audit complete, inventory saved, path mapping built
- [ ] Phase 2: All skills categorized (0 empty categories)
- [ ] Phase 3: Duplicates identified and removed/merged
- [ ] Phase 4: All skills judged, results saved to `judge_results/`
- [ ] Phase 5: All skills scoring < 80 remediated
- [ ] Phase 6: Umbrella skills consolidated with absorbed skills sections
- [ ] Phase 7: Final verification — all skills ≥ 80, categorized, deduped
- [ ] `SESSION_REPORT.md` updated with results

## Pitfalls

- **Stale cache:** Never use `skill_view()` to verify your own edits — read file from disk
- **Profile visibility:** `skill_manage()` from `default` profile may not see all skills; use absolute paths with `write_file`/`patch`
- **Dedupe before judge:** Judging before deduplicating wastes time on skills that will be deleted
- **Batch drift:** Calibrate scoring on first batch, then lock thresholds
- **Context limits:** Process in batches of 10; write results after each batch; don't retain full skill text
- **Protected skills:** Do NOT edit bundled/hub-installed skills; pinned skills can be patched but not deleted
- **skill_manage delete:** Delete archives rather than removes; `absorbed_into` must reference existing skill by bare name
- **Pagination awareness:** Always `read_file(path)` without offset/limit before constructing patch `old_string`
**Path handling (MSYS/Windows):** Use `os.environ["HOME"]` or `os.environ["USERPROFILE"]` to derive paths in Python scripts (portable across MSYS and Windows native). Avoid hardcoded `C:\\Users\\...` or `C:/Users/...` — derive from environment variables instead.

## Template References

Detailed section templates in `templates/audit-skills-judge-fix/`:
- `phases.md`
