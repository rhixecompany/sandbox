---
trigger: /audit-skills-judge-fix
description: >-
  Run full skills audit, categorize, dedupe, consolidate, judge in batches of 10,
  remediate all reference files/scripts/SKILL.md, delete duplicates, and verify completion.
tags:
  [
    hermes,
    copilot,
    opencode,
    skills,
    audit,
    judge,
    remediation,
    dedupe,
    consolidation,
  ]
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

### Phase 1: Skills Audit & Inventory

**Goal:** Produce a complete inventory of all local skills.

**Inputs:** None (reads live skill directories)

**Outputs:** `docs/local-skills.md`, `docs/skill-inventory.json`

**Steps:**

| Step | Action                                                                      | Output               |
| ---- | --------------------------------------------------------------------------- | -------------------- |
| 1.1  | Run `hermes skills audit && hermes skills check && hermes skills update`    | Audit results        |
| 1.2  | Run `hermes skills list --source local > docs/local-skills.md`              | Skill inventory file |
| 1.3  | Read and understand `docs/local-skills.md`                                  | Context for Phase 2  |
| 1.4  | Run `batch_skill_judge.py` (inventory mode) to build `skill_inventory.json` | Full path mapping    |

**Tasks:**

- **Task 1.1 — Audit & Update:** Run audit, check, and update commands in background without timeout
- **Task 1.2 — Inventory:** Save full local skill listing to `docs/local-skills.md`
- **Task 1.3 — Read:** Parse inventory to understand skill count and categories
- **Task 1.4 — Build path mapping:** Create `skill_name_to_path.json` mapping each skill name to its canonical disk path (prefer category subdirectories over flat paths)

---

### Phase 2: Categorize Skills

**Goal:** Move each skill to its correct category folder.

**Inputs:** `docs/local-skills.md`

**Outputs:** Skills relocated to correct category directories

**Steps:**

| Step | Action                                                    | Output                                        |
| ---- | --------------------------------------------------------- | --------------------------------------------- |
| 2.1  | Identify uncategorized skills (empty category in listing) | Uncategorized list                            |
| 2.2  | Create categorization plan using `plans-and-specs`        | `.hermes/plans/skills-categorization-plan.md` |
| 2.3  | Create missing category directories (e.g., `blockchain/`) | New category dirs                             |
| 2.4  | Move skills to correct category folders via `mv`          | Reorganized directories                       |
| 2.5  | Verify with `hermes skills list --source local`           | All skills categorized                        |

**Tasks:**

- **Task 2.1 — Identify:** Parse listing for skills with empty category field
- **Task 2.2 — Plan:** Create categorization plan mapping each skill to target category
- **Task 2.3 — Create dirs:** `mkdir -p` for any new category directories needed
- **Task 2.4 — Execute:** `mv` each skill directory to its target category folder
- **Task 2.5 — Verify:** Confirm 0 skills with empty category; count per category

**Category mapping reference:**

| Skill                                  | Target Category      |
| -------------------------------------- | -------------------- |
| chainlink                              | blockchain           |
| distributed-llm-pretraining-torchtitan | mlops                |
| here.now                               | productivity         |
| hermes-breakdown                       | autonomous-ai-agents |
| hermes-hooks                           | devops               |
| hermes-mcp                             | mcp                  |
| hermes-skills                          | devops               |
| hermes-system-maintenance              | devops               |
| huggingface-accelerate                 | mlops                |
| ideation                               | creative-ideation    |
| inference-sh-cli                       | devops               |
| lambda-labs-gpu-cloud                  | devops               |
| modal-serverless-gpu                   | devops               |
| optimizing-attention-flash             | mlops                |
| peft (peft-fine-tuning)                | mlops                |
| profile-maintenance                    | devops               |
| qdrant-vector-search                   | mlops                |
| qwen-code                              | autonomous-ai-agents |
| simpo (simpo-training)                 | mlops                |
| skill-creator                          | development          |
| skill-judge                            | qa                   |
| stable-diffusion-image-generation      | mlops                |
| template                               | autonomous-ai-agents |
| using-git-worktrees                    | development          |
| validate-memories                      | devops               |
| writing-skills                         | development          |

---

### Phase 3: Deduplicate & Consolidate Skills

**Goal:** Identify and remove/merge duplicate and overlapping skills.

**Inputs:** `skill_inventory.json`, `docs/local-skills.md`

**Outputs:** `docs/dedupe-report.md`, `docs/consolidation-report.md`

**Steps:**

| Step | Action                                                                                          | Output               |
| ---- | ----------------------------------------------------------------------------------------------- | -------------------- |
| 3.1  | Run `dedupe_skills.py` to find duplicate SKILL.md files                                         | Duplicate pairs list |
| 3.2  | For each duplicate pair, compare content (line count, structure)                                | Comparison report    |
| 3.3  | Determine canonical version (prefer category subdirectory, fuller content)                      | Canonical selection  |
| 3.4  | Run `consolidate_skills.py` to identify overlapping/overlapping skills                          | Overlap report       |
| 3.5  | Merge thin skills into umbrella skills using `skill_manage(action='delete', absorbed_into=...)` | Merged skills        |
| 3.6  | Delete true duplicates (identical content, same name) via `rm -rf`                              | Removed duplicates   |
| 3.7  | Verify with `hermes skills list --source local`                                                 | Reduced skill count  |

**Tasks:**

- **Task 3.1 — Find duplicates:** Script scans all SKILL.md files, groups by skill name, identifies multiple paths
- **Task 3.2 — Compare:** For each duplicate pair, compare line count, frontmatter completeness, reference files
- **Task 3.3 — Select canonical:** Prefer the version in a category subdirectory with more complete content
- **Task 3.4 — Find overlaps:** Identify skills with similar descriptions/purposes that should be consolidated
- **Task 3.5 — Merge:** Use `skill_manage(action='delete', absorbed_into='<umbrella>')` to archive thin skills into umbrella
- **Task 3.6 — Delete:** Remove true duplicates (identical content) that are not referenced anywhere
- **Task 3.7 — Verify:** Confirm reduced skill count; update `skill_name_to_path.json`

**Known duplicate/overlap patterns (from 2026-06-17 audit):**

| Canonical                       | Duplicate/Overlap                 | Action                                         |
| ------------------------------- | --------------------------------- | ---------------------------------------------- |
| accelerate                      | huggingface-accelerate            | Merge — same purpose                           |
| cli                             | inference-sh-cli                  | Merge — inference-sh-cli is the fuller version |
| dspy                            | mlops/research/dspy               | Delete if path missing                         |
| docker-management               | devops/docker                     | Delete if path missing                         |
| ideation                        | creative-ideation                 | Merge — same purpose                           |
| lambda-labs                     | lambda-labs-gpu-cloud             | Merge — same purpose                           |
| modal                           | modal-serverless-gpu              | Merge — same purpose                           |
| peft                            | peft-fine-tuning                  | Merge — same purpose                           |
| qdrant                          | qdrant-vector-search              | Merge — same purpose                           |
| simpo                           | simpo-training                    | Merge — same purpose                           |
| stable-diffusion                | stable-diffusion-image-generation | Merge — same purpose                           |
| trl-fine-tuning                 | mlops/trl                         | Delete if path missing                         |
| grok                            | mlops/grok                        | Delete if path missing                         |
| hermes-s6-container-supervision | devops/s6                         | Delete if path missing                         |
| comps-analysis                  | devops/comps                      | Delete if path missing                         |
| adversarial-ux-test             | qa/adversarial                    | Delete if path missing                         |
| dspy                            | mlops/dspy                        | Delete if path missing                         |

**Python scripts to use:**

1. **`dedupe_skills.py`** — Scans `~/AppData/Local/hermes/skills/` for all SKILL.md files, groups by name, outputs duplicate pairs with line counts and paths
2. **`consolidate_skills.py`** — Identifies overlapping skills by comparing descriptions and tags, suggests merge targets
3. **`merge_skill.py`** — Merges a thin skill into an umbrella skill (copies references, updates umbrella's "Absorbed Skills" section)

---

### Phase 4: Judge Skills

**Goal:** Evaluate all skills and raise scores above 80.

**Inputs:** `skill_name_to_path.json` (updated after dedupe)

**Outputs:** `judge_results/all_results.tsv`, `judge_results/summary.md`, `judge_results/batch_NNNN_results.md`

**Steps:**

| Step | Action                                                                | Output               |
| ---- | --------------------------------------------------------------------- | -------------------- |
| 4.1  | Run `batch_skill_judge.py` on first batch of 10 skills                | Batch 1 results      |
| 4.2  | Repeat for remaining batches                                          | All batches complete |
| 4.3  | Generate `summary.md` with score distribution                         | Summary report       |
| 4.4  | Identify skills scoring ≤ 80                                          | `below_80_list.txt`  |
| 4.5  | Split into `needs_work_list.txt` (60-79) and `rewrite_list.txt` (<60) | Remediation lists    |

**Tasks:**

- **Task 4.1 — Batch Judge:** Judge skills in batches of 10 using `skill-judge` v1.1.0 criteria
- **Task 4.2 — Aggregate:** Combine all batch results into `all_results.tsv`
- **Task 4.3 — Summarize:** Generate score distribution, top/bottom 10, common issues
- **Task 4.4 — Filter:** Extract skills scoring ≤ 80 for remediation
- **Task 4.5 — Prioritize:** Split into needs-work (60-79) and rewrite (<60) lists

**Scoring criteria (skill-judge v1.1.0):**

| Dimension   | Max | Criteria                                                                 |
| ----------- | --- | ------------------------------------------------------------------------ |
| Frontmatter | 20  | name, title, description, version, author, license, tags                 |
| Structure   | 20  | Skills Required table, ≥3 phases, pitfalls, verification checklist, refs |
| Content     | 20  | Resumability, error handling, platform notes, examples, no placeholders  |
| DRY         | 20  | No duplicates, <250 lines, cross-ref consistency                         |
| References  | 20  | All 3 ref types, substantive, cited, no orphans                          |

**Score bands:**

| Score | Rating            | Action           |
| ----- | ----------------- | ---------------- |
| ≥80   | [PASS] AI-ready   | Minor fixes only |
| 60-79 | [WARN] Needs work | Targeted patches |
| <60   | [RED] Rewrite     | Full rebuild     |

**Python scripts:**

- **`batch_skill_judge.py`** — Main batch judging script. Reads `skill_name_to_path.json`, scores each skill on 5 dimensions, writes `judge_results/batch_NNNN_results.md` per batch, writes `judge_results/all_results.tsv` with all results. Supports `--resume` to skip existing batch files.

---

### Phase 5: Remediate Skills

**Goal:** Fix all skills scoring below 80.

**Inputs:** `judge_results/needs_work_list.txt`, `judge_results/rewrite_list.txt`

**Outputs:** All reference files, scripts, and SKILL.md created/updated

**Steps:**

| Step | Action                                                   | Output                            |
| ---- | -------------------------------------------------------- | --------------------------------- |
| 5.1  | Run `batch_remediate.py` on skills scoring 60-79         | Patched skills                    |
| 5.2  | Run `batch_rewrite_worst.py` on skills scoring <60       | Rewritten skills                  |
| 5.3  | Run `batch_skill_judge.py --verify` on remediated skills | Re-scored results                 |
| 5.4  | Identify any still below 80                              | Second-pass list                  |
| 5.5  | Apply targeted fixes to remaining issues                 | Final pass                        |
| 5.6  | Verify all skills ≥ 80                                   | `judge_results/final_results.tsv` |

**Tasks:**

- **Task 5.1 — Patch (60-79):** Add missing frontmatter fields, Skills Required table, pitfalls section, verification checklist
- **Task 5.2 — Rewrite (<60):** Full rebuild with complete structure, concrete examples, reference files
- **Task 5.3 — Re-score:** Re-run judge on all remediated skills to confirm improvement
- **Task 5.4 — Second pass:** Identify skills still below 80 after first remediation
- **Task 5.5 — Final fix:** Targeted fixes for remaining issues (usually content depth, examples)
- **Task 5.6 — Verify:** Confirm all skills ≥ 80; generate final report

**Python scripts:**

1. **`batch_remediate.py`** — Reads `needs_work_list.txt`, patches each skill: adds missing frontmatter fields, Skills Required table, pitfalls section, verification checklist. Uses `read_file`/`write_file` with absolute paths.
2. **`batch_remediate_42_59.py`** — Variant for skills scoring 42-59 needing more aggressive patching.
3. **`batch_rewrite_worst.py`** — Reads `rewrite_list.txt`, does full rebuild of skills scoring <60 with complete structure.
4. **`batch_skill_judge.py --verify`** — Re-scores remediated skills to confirm improvement.

---

### Phase 6: Consolidate Umbrella Skills

**Goal:** Merge overlapping skills into well-structured umbrella skills.

**Inputs:** `docs/consolidation-report.md`, Phase 3 overlap analysis

**Outputs:** Consolidated umbrella skills with "Absorbed Skills" sections

**Steps:**

| Step | Action                                                           | Output                  |
| ---- | ---------------------------------------------------------------- | ----------------------- |
| 6.1  | Identify umbrella candidates (skills that absorbed others)       | Umbrella list           |
| 6.2  | For each umbrella, verify absorbed skills are listed in SKILL.md | Verification            |
| 6.3  | Move reference files from absorbed skills to umbrella            | Consolidated refs       |
| 6.4  | Update umbrella SKILL.md with absorbed skills section            | Updated umbrellas       |
| 6.5  | Verify with `read_file` and `skill_view` (on disk, not cache)    | Confirmed consolidation |

**Tasks:**

- **Task 6.1 — Identify:** List all skills that have absorbed others via `skill_manage(action='delete', absorbed_into=...)`
- **Task 6.2 — Verify:** Each umbrella's SKILL.md has "Recently Absorbed Skills" section listing all absorbed skills
- **Task 6.3 — Consolidate refs:** Copy unique reference files from absorbed skills to umbrella's `references/` directory
- **Task 6.4 — Update:** Add absorbed skills section to umbrella SKILL.md
- **Task 6.5 — Verify:** Confirm umbrella skills are complete and absorbed skills are archived

**Python scripts:**

- **`consolidate_skills.py`** — Identifies overlapping skills, suggests merge targets, generates consolidation plan
- **`merge_skill.py`** — Merges a thin skill into an umbrella: copies references, updates umbrella's absorbed skills section

---

### Phase 7: Verify & Finalize

**Goal:** Verify the entire pipeline is complete and all skills meet quality standards.

**Inputs:** All previous phase outputs

**Outputs:** `docs/final-verification.md`

**Steps:**

| Step | Action                                                 | Output                  |
| ---- | ------------------------------------------------------ | ----------------------- |
| 7.1  | Run `hermes skills audit` — verify all pass            | Audit clean             |
| 7.2  | Run `hermes skills list --source local` — verify count | Final count             |
| 7.3  | Run `batch_skill_judge.py --final` — score all skills  | Final scores            |
| 7.4  | Verify all skills ≥ 80                                 | Quality gate pass       |
| 7.5  | Verify all skills have categories                      | Categorization complete |
| 7.6  | Verify no duplicate skills remain                      | Dedupe complete         |
| 7.7  | Generate `docs/final-verification.md`                  | Final report            |
| 7.8  | Update `SESSION_REPORT.md` with results                | Session report          |

**Tasks:**

- **Task 7.1 — Audit:** Run full security audit; confirm no new issues
- **Task 7.2 — Count:** Verify final skill count matches expected (post-dedupe)
- **Task 7.3 — Final score:** Re-score all skills; confirm all ≥ 80
- **Task 7.4 — Quality gate:** If any skill < 80, return to Phase 5
- **Task 7.5 — Categories:** Confirm 0 skills with empty category
- **Task 7.6 — Dedupe:** Confirm no duplicate skill names remain
- **Task 7.7 — Report:** Generate final verification report with before/after metrics
- **Task 7.8 — Session report:** Update SESSION_REPORT.md with work completed

---

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
- **Windows paths:** Use absolute `C:\Users\...` paths in Python scripts; normalize MSYS paths
