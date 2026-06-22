# Master Implementation Plan: ComicWise Codebase Overhaul

## TL;DR

5-batch plan to stabilize the codebase, consolidate 92 reference scripts, enhance the seed system + quality gate automation, deep-audit all 11 source directories (fixing every issue found), modernize CI/CD, and produce a phase master plan. 6 prompt files orchestrate execution with verification gates between each batch.

## Prompt Files (6 total)

| # | File | Persona | Scope |
| --- | --- | --- | --- |
| 0 | `master.prompt.md` | Architect | Orchestrates all 5 batches in sequence |
| 1 | `batch-1-stabilize-clean.prompt.md` | Debugger + Reviewer | TS fixes, docs/component/VS Code cleanup |
| 2 | `batch-2-scripts-consolidation.prompt.md` | Reviewer + Implementer | Reference analysis, refactor-context.md, new scripts, shell scripts, package.json |
| 3 | `batch-3-seeds-quality-gate.prompt.md` | Reviewer + Implementer + Debugger | Seed enhancement, quality gate scripts, triage system |
| 4 | `batch-4-source-audit.prompt.md` | Reviewer | Deep audit of all 11 src/ directories — fix every issue |
| 5 | `batch-5-cicd-phase-plan.prompt.md` | Implementer + Architect | CI/CD modernization, phase master plan |

---

## Batch 1: Stabilize & Clean

> **Goal**: Fix blockers, remove dead weight, establish clean baseline.
> ### Phase 1A: Fix TypeScript Errors (Debugger)

> **Full content:** `templates/run/batch_1_stabilize__clean.md`

## Batch 2: Scripts Consolidation

> **Goal**: Consolidate 92 reference scripts + 17 existing into unified DRY system
> ### Phase 2A: Analyze & Categorize (Reviewer)

> **Full content:** `templates/run/batch_2_scripts_consolidation.md`

## Batch 3: Seeds + Quality Gate + Triage

> **Goal**: Enhance seeders, add chunked processing + resume, create quality gate 
> ### Part A: Seed System Enhancement (Reviewer → Implementer)

> **Full content:** `templates/run/batch_3_seeds__quality_gate__t.md`

## Batch 4: Full Source Audit (Fix Everything)

> **Goal**: Deep audit all 11 directories, fix EVERY issue found.
> ### Pre-Identified Issues to Fix

> **Full content:** `templates/run/batch_4_full_source_audit_fix_.md`

## Batch 5: CI/CD + Phase Master Plan

> **Goal**: Modernize CI/CD workflows, create comprehensive phase task document.
> ### Part A: CI/CD Workflow Modernization (Implementer)

> **Full content:** `templates/run/batch_5_cicd__phase_master_pla.md`

## Relevant Files

> - `src/components/search/search-results.tsx` — fix 3 TS errors
> - `src/components/reading/index.ts`, `src/components/reading-progress/index.ts` 

> **Full content:** `templates/run/relevant_files.md`

## Decisions Log

1. **5 batches** (consolidated from original 4 + expanded scope)
2. **Full consolidation** of 92 reference scripts into unified superset
3. **Direct deletion** with git as backup
4. **TS errors** fixed in Batch 1 as foundation
5. **TypeScript scripts** in `src/scripts/`, **shell scripts** in root
6. **All scripts** must have `--dry-run`, `--verbose`, `--yes`, `--json`
7. **auth-db.ts** → move to `src/dal/` (does DB queries)
8. **SearchDAL** → make it extend `BaseDal<T>`
9. **process.env** → fix ALL 20 violations (including NODE_ENV checks)
10. **Dead files** → delete `comic-schema.ts` + `example.spec.ts`
11. **Reading-progress duplicates** → investigate and merge
12. **comment-rating bundling** → investigate before splitting
13. **User seeder** → 10 users default (3 admin, 3 mod, 4 user)
14. **Checkpoint file** → project root `.seed-checkpoint.json` (gitignored)
15. **Batch 4 depth** → fix ALL issues (not just list)
16. **Test rename** → `comic-schema.spec.ts` → `comic.schema.spec.ts`
17. **Scope includes**: everything in user's 10-part request + all research findings
18. **Scope excludes**: Phase 4.4/4.5 implementation (only planned), MCP changes, auth system changes

---

## Integrated Considerations (No Loose Ends)

| Item | Resolution |
| --- | --- |
| `.references/` in .gitignore | Already done (line 37). VS Code exclusion in Batch 1 |
| CI/CD integration | Batch 5 — modernize all 4 workflows + add triage step |
| Seed streaming/resume | Batch 3, Phase 3F — chunked for chapter-seeder (50k), chapter-image-seeder (150k), comic-seeder (2k) |
| process.env violations | Batch 4 — fix all 20 across 12 files |
| Dead code | Batch 4 — delete comic-schema.ts, example.spec.ts |
| DAL consistency | Batch 4 — SearchDAL extends BaseDal, auth-db.ts moved to dal/ |
| Action correctness | Batch 4 — fix goals.actions.ts import, investigate reading-progress dupes |


## Template References

Detailed templates in `templates/run/`:
- `batch_1_stabilize__clean.md`
- `batch_2_scripts_consolidation.md`
- `batch_3_seeds__quality_gate__t.md`
- `batch_4_full_source_audit_fix_.md`
- `batch_5_cicd__phase_master_pla.md`
- `relevant_files.md`
