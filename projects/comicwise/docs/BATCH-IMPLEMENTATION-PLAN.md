# ComicWise Batch Implementation Plan

## Master Plan Based on run.prompt.md + setup-enhanced.prompt.md + quality-gate-debugger.prompt.md

**Generated:** March 13, 2026  
**Status:** Ready for Implementation  
**Scope:** 5 Batches across 16 major phases with sub-tasks

---

## Executive Summary

This document outlines the complete batch implementation plan derived from three orchestration prompts:

1. `run.prompt.md` — Master Implementation Plan (5 batches)
2. `setup-enhanced.prompt.md` — Implementation workflow & DRY practices
3. `quality-gate-debugger.prompt.md` — Quality Gate debugging & triage process

**Current Project State:**

- ✅ TypeScript: 0 errors (pnpm type-check passes)
- ✅ Tests: 241/241 passing
- ✅ Type Safety: Production-ready
- ⏳ Build & Lint: Slow (pending optimization)

---

## BATCH 1: Stabilize & Clean

**Goal:** Fix blockers, remove dead weight, establish clean baseline.  
**Priority:** HIGH (Foundation for all subsequent batches)  
**Estimated Duration:** 2-4 hours

### Phase 1A: Fix TypeScript Errors (Debugger)

**File:** `src/components/search/search-results.tsx`  
**Status:** ✅ VERIFIED - 0 errors found

| Issue | Description | Status |
| --- | --- | --- |
| Import validation | Check bookmark import path | ✅ Valid: `@/components/comics/bookmark-button` |
| String/Number mismatch | `comic.id` type validation | ✅ Correct: Already using proper types |
| Nullable handling | `comic.synopsis` optional check | ✅ Correct: Using `?? undefined` |

**Verification:**

```bash
pnpm type-check → ✅ 0 errors
```

**Status:** ✅ PHASE 1A COMPLETE

---

### Phase 1B: Documentation Cleanup (Reviewer)

**Goal:** Delete 6 superseded documentation files  
**Status:** ⚠️ STAGED (Ready to implement)

#### Files to DELETE (6 total)

1. `docs/PHASE_2_COMPLETION.md` — Superseded
2. `docs/PHASE_3_COMPLETION.md` — Superseded
3. `docs/PHASE4-3-DAY4-COMPLETE.md` — Superseded
4. `docs/PHASE4-3-DAYS4-5-PLAN.md` — Superseded
5. `docs/debugger-context-map.md` — Superseded by `database-context-map.md`
6. `docs/COMICWISE-PROJECT-STATUS.md` — Superseded

#### Files to KEEP (19 critical files)

- ✅ `docs/dev.content.md` — Development reference
- ✅ `docs/database-context-map.md` — Entity relationships
- ✅ `docs/SCRIPTS.md` — Script inventory
- ✅ `docs/QUICK_START.md` — Quick reference
- ✅ `docs/MASTER_PHASE_PLAN_4-6.md` — Phase tracking
- ✅ `docs/_archive/` — Historical records (keep)

**Verification:**

```bash
grep -r "PHASE_2_COMPLETION\|PHASE_3_COMPLETION" src/ → 0 results
```

**Status:** ⏳ READY TO IMPLEMENT

---

### Phase 1C: Components Cleanup (Reviewer)

**Goal:** Resolve duplication, create barrel exports, delete demo files  
**Status:** ⚠️ REQUIRES INVESTIGATION

#### Task 1C.1: Reading/Reading-Progress Duplication

**Issue:** 2 same-named files in different directories

- `src/components/reading/reading-stats-card.tsx`
- `src/components/reading-progress/reading-stats-card.tsx`
- `src/components/reading/continue-reading-card.tsx`
- `src/components/reading-progress/continue-reading-card.tsx`

**Action:**

```bash
# Grep imports to identify which is active
grep -r "reading-stats-card" src/ --include="*.tsx" --include="*.ts"
grep -r "continue-reading-card" src/ --include="*.tsx" --include="*.ts"
```

**Decision:** Keep active one, delete duplicate, update imports

**Status:** ⏳ REQUIRES VERIFICATION BEFORE DELETE

---

#### Task 1C.2: Create Barrel Exports (4 files)

| Directory | New File | Exports |
| --- | --- | --- |
| `src/components/bookmarks/` | `index.ts` | 4 exports (identify from directory) |
| `src/components/search/` | `index.ts` | 5 exports (identify from directory) |

**Implementation:**

```typescript
// src/components/bookmarks/index.ts
export { BookmarkCard } from "./bookmark-card";
export { BookmarkFilters } from "./bookmark-filters";
// ... (auto-generate based on actual files)
```

**Status:** ⏳ READY TO IMPLEMENT

---

#### Task 1C.3: Delete Demo Files

**Directory:** `src/components/shadcn-studio/` (17 files)

**Action:**

```bash
rm -rf src/components/shadcn-studio/
```

**Verification:**

```bash
grep -r "shadcn-studio" src/ → 0 results
```

**Status:** ⏳ READY TO IMPLEMENT

---

#### Task 1C.4: Audit App Data File

**File:** `src/app/admin/data.json`

**Action:** Verify if used, if not → delete

**Status:** ⏳ REQUIRES VERIFICATION

---

### Phase 1D: VS Code Config Audit (Reviewer)

**Goal:** Optimize VS Code settings, tasks, and extensions  
**Status:** ⚠️ PARTIALLY STAGED

#### Task 1D.1: settings.json

- [ ] Add `.references/` to `files.exclude`
- [ ] Add `.references/` to `search.exclude`

**Status:** ⏳ READY

---

#### Task 1D.2: tasks.json

- [ ] Remove 28 one-time tasks
- [ ] Keep 13 reusable tasks

**Status:** ⏳ REQUIRES REVIEW

---

#### Task 1D.3: launch.json

- [ ] Verify all 9 debug configs reference valid scripts

**Status:** ⏳ REQUIRES VERIFICATION

---

#### Task 1D.4: extensions.json

- [ ] Verify all 40 extension IDs still valid

**Status:** ⏳ REQUIRES VERIFICATION

---

#### Task 1D.5: mcp.json

- [ ] Verify all 5 MCP servers accessible

**Status:** ⏳ REQUIRES VERIFICATION

---

### Batch 1 Verification Checklist

- [ ] `pnpm type-check` → 0 errors
- [ ] `pnpm test` → 241/241 passing
- [ ] `pnpm build` → success
- [ ] `grep -r "shadcn-studio" src/` → 0 results
- [ ] All superseded docs deleted
- [ ] Barrel exports created
- [ ] VS Code configs optimized

**Status:** ⏳ IMPLEMENTATION PENDING

---

## BATCH 2: Scripts Consolidation

**Goal:** Consolidate 92 reference scripts + enhance existing system  
**Priority:** HIGH  
**Estimated Duration:** 4-6 hours

### Phase 2A: Analyze & Categorize (Reviewer)

**Task:** Read ALL scripts in `.references/` and categorize into:

- Already Implemented
- High-Value Missing
- Redundant
- Not Applicable

**Output:** `docs/refactor-context.md` with:

- Categorized inventory
- Code samples grouped by Infrastructure, Database, Optimization, DevOps, Quality, Scaffolding

**Status:** ⏳ READY TO EXECUTE

---

### Phase 2B: Port New TypeScript Scripts (Implementer)

**Goal:** Create 5 new scripts in `src/scripts/` with standard flags

#### Scripts to Create

| Script | Purpose | Flags | Status |
| --- | --- | --- | --- |
| `project-cleanup.ts` | Deep cleanup (duplicates, unused, temp) | `--dry-run`, `--verbose`, `--yes` | ⏳ |
| `cleanup-duplicates.ts` | Pattern-based duplicate detection | `--dry-run`, `--verbose` | ⏳ |
| `optimize-performance.ts` | Bundle analysis + caching audit | `--dry-run`, `--verbose`, `--json` | ⏳ |
| `validate-env.ts` | Env validation + .env sync | `--dry-run`, `--verbose` | ⏳ |
| `fix-line-endings.ts` | CRLF→LF normalization | `--dry-run`, `--verbose`, `--yes` | ⏳ |

**Pattern:** All use `confirmAction.ts` for destructive ops + Logger from seed system

**Status:** ⏳ READY TO IMPLEMENT

---

### Phase 2C: Enhance Existing Scripts (Implementer)

| Script               | Enhancement                       | Status |
| -------------------- | --------------------------------- | ------ |
| `analyze-project.ts` | Add security scan patterns        | ⏳     |
| `scaffold.ts`        | Add DAL, schema, action templates | ⏳     |
| All scripts          | Audit flags consistency           | ⏳     |

**Status:** ⏳ READY TO IMPLEMENT

---

### Phase 2D: Shell Scripts (Implementer)

#### Enhance (2 pairs)

| Script | Enhancements |
| --- | --- |
| `setup-dev.sh`/`.ps1` | Add `--skip-db`, `--skip-seed`, `--skip-install` |
| `quality-gate.sh`/`.ps1` | Add `tee`/`Tee-Object`, timing, JSON summary |

#### Create NEW (2 pairs)

| Script | Purpose |
| --- | --- |
| `dev.sh`/`dev.ps1` | Prerequisites + dev server + auto-open browser |
| `cleanup.sh`/`cleanup.ps1` | Artifact removal with dry-run |

**Status:** ⏳ READY TO IMPLEMENT

---

### Phase 2E: Update package.json (Implementer)

**New Scripts to Add:**

```json
{
  "cleanup:duplicates": "tsx src/scripts/cleanup-duplicates.ts",
  "cleanup:duplicates:dry": "tsx src/scripts/cleanup-duplicates.ts --dry-run",
  "cleanup:project": "tsx src/scripts/project-cleanup.ts",
  "cleanup:project:dry": "tsx src/scripts/project-cleanup.ts --dry-run",
  "fix:line-endings": "tsx src/scripts/fix-line-endings.ts --yes",
  "fix:line-endings:dry": "tsx src/scripts/fix-line-endings.ts --dry-run",
  "optimize:performance": "tsx src/scripts/optimize-performance.ts --analyze",
  "optimize:performance:dry": "tsx src/scripts/optimize-performance.ts --dry-run",
  "validate:env": "tsx src/scripts/validate-env.ts",
  "validate:env:dry": "tsx src/scripts/validate-env.ts --dry-run"
}
```

**Status:** ⏳ READY TO IMPLEMENT

---

### Batch 2 Verification Checklist

- [ ] `pnpm type-check` → 0 errors
- [ ] `tsx src/scripts/project-cleanup.ts --dry-run --verbose` → runs
- [ ] `tsx src/scripts/validate-env.ts --dry-run` → runs
- [ ] `docs/refactor-context.md` exists with content
- [ ] All `package.json` scripts resolve
- [ ] Shell scripts executable

**Status:** ⏳ IMPLEMENTATION PENDING

---

## BATCH 3: Seeds + Quality Gate + Triage

**Goal:** Enhance seeders, add chunked processing + resume, quality gate automation  
**Priority:** HIGH  
**Estimated Duration:** 4-6 hours

### Phase 3A: Seed System Enhancement (Reviewer → Implementer)

#### Task 3A.1: User Seeder Enhancement

**File:** `src/scripts/seed/seeders/user-seeder.ts`

**Changes:**

- Default: 10 users (3 admin, 3 moderator, 4 user)
- Configurable via `--count` flag
- Avatar URLs, email variations
- Configurable bcrypt rounds
- `--dry-run` validation

**Status:** ⏳ READY TO IMPLEMENT

---

#### Task 3A.2: Comic Image Seeder Enhancement

**File:** `src/scripts/seed/seeders/comic-image-seeder.ts`

**Changes:**

- Multi-strategy (URL/local/ImageKit)
- Thumbnail refs, dimension validation
- Fallback placeholders
- Parallel processing
- Progress tracking

**Status:** ⏳ READY TO IMPLEMENT

---

#### Task 3A.3: Chapter Image Seeder Enhancement

**File:** `src/scripts/seed/seeders/chapter-image-seeder.ts`

**Changes:**

- Sequential page ordering
- Format validation
- Bulk insert for 150k+ images
- Resumable operation
- Streaming with ETA

**Status:** ⏳ READY TO IMPLEMENT

---

#### Task 3A.4: Batch Fixes

- [ ] Standardize error handling across all seeders
- [ ] Audit `onConflictDoNothing` vs `onConflictDoUpdate` usage
- [ ] Add missing Zod schemas
- [ ] Ensure transaction rollback

**Status:** ⏳ READY TO IMPLEMENT

---

#### Task 3A.5: Chunked Processing & Resume

**Affected Files:**

- `src/scripts/seed/seeders/chapter-seeder.ts`
- `src/scripts/seed/seeders/chapter-image-seeder.ts`
- `src/scripts/seed/seeders/comic-seeder.ts`

**Implementation:**

1. Chunk batches (default 500) with multi-row insert
2. `.seed-checkpoint.json` in project root (gitignored)
3. `--resume` flag to continue from checkpoint
4. Yield intervals between chunks
5. Update `base-seed.ts` with `processInChunks()` helper
6. Update `src/scripts/seed/types.ts` with new options

**Status:** ⏳ READY TO IMPLEMENT

---

### Phase 3B: Quality Gate Scripts (Implementer)

**File:** `quality-gate.sh` / `quality-gate.ps1`

**Enhancements:**

```bash
pnpm type-check 2>&1 | tee type-check.txt
pnpm lint:fix 2>&1 | tee lint-fixed.txt
pnpm test --run 2>&1 | tee test-report.txt
pnpm build:debug 2>&1 | tee build-report.txt
```

**Features:**

- Per-gate timing
- `--continue-on-error` flag
- Skip flags for individual gates
- Color logging
- JSON summary output

**Status:** ⏳ READY TO IMPLEMENT

---

### Phase 3C: Debugger Triage (Debugger)

**File:** NEW `src/scripts/triage-quality-gate.ts`

**Functionality:**

1. Parse 4 .txt files → extract TS errors, ESLint, tests, build errors
2. Triage: CRITICAL → HIGH → MEDIUM → LOW, grouped by file
3. Output `quality-gate-triage.json` + console summary
4. Suggest auto-fixes
5. Add to `package.json` as `"triage"` command

**Process:**

1. Read triage JSON
2. Fix CRITICAL issues first
3. Re-run quality gate
4. Iterate until all pass

**Status:** ⏳ READY TO IMPLEMENT

---

### Batch 3 Verification Checklist

- [ ] `pnpm seed:validate` → all pass
- [ ] `pnpm type-check` → 0 errors
- [ ] `quality-gate.sh --continue-on-error` → produces 4 .txt + JSON
- [ ] `pnpm triage` → produces quality-gate-triage.json
- [ ] Checkpoint file mechanism works

**Status:** ⏳ IMPLEMENTATION PENDING

---

## BATCH 4: Full Source Audit (Fix Everything)

**Goal:** Deep audit all 11 src/ directories, fix EVERY issue found  
**Priority:** CRITICAL  
**Estimated Duration:** 6-8 hours

### Phase 4A: Pre-Identified Issues to Fix (10 issues)

| # | File | Issue | Fix | Status |
| --- | --- | --- | --- | --- |
| 1 | `src/actions/auth-db.ts` | Not a Server Action (no `"use server"`) | Move to `src/dal/auth-db.ts` | ⏳ |
| 2 | `src/dal/search-dal.ts` | Only DAL not extending `BaseDal<T>` | Make it extend `BaseDal<ComicType>` | ⏳ |
| 3 | `src/dal/search-dal.ts` L116,118 | 2 `any` types | Replace with proper interfaces | ⏳ |
| 4 | `src/actions/goals.actions.ts` | Wrong import `./actions-types` | Change to `@/types/actions-types` | ⏳ |
| 5 | `src/schemas/comic-schema.ts` | Dead file — imported nowhere | Delete | ⏳ |
| 6 | `src/tests/example.spec.ts` | Playwright placeholder | Delete | ⏳ |
| 7 | `src/tests/schemas/comic-schema.spec.ts` | Naming mismatch | Rename to `comic.schema.spec.ts` | ⏳ |
| 8 | `src/actions/reading-progress.actions.ts` + `reading-progress.ts` | Potential duplicates | Investigate and merge | ⏳ |
| 9 | `src/dal/comment-rating-dal.ts` | Bundles 2 DALs in one file | Investigate if should split | ⏳ |
| 10 | 12 files (20 usages) | `process.env` used directly | Migrate ALL to `getEnv()` | ⏳ |

**Status:** ⏳ READY TO EXECUTE

---

### Phase 4B: process.env Violations (20 usages across 12 files)

#### Auth/Service Configs (8 usages)

| File | Violation | Fix |
| --- | --- | --- |
| `src/auth-providers.ts` | GITHUB*CLIENT_ID, KEYCLOAK*\* (4 usages) | Use `getEnv()` |
| `src/auth-config.ts` | AUTH_SECRET (1 usage) | Use `getEnv()` |
| `src/lib/cache/redis.ts` | UPSTASH*REDIS_REST*\* (2 usages) | Use `getEnv()` |
| `src/scripts/seed/images/image-kit-uploader.ts` | IMAGEKIT\_\* (3 usages) | Use `getEnv()` |

**Status:** ⏳ READY TO IMPLEMENT

---

#### NODE_ENV Checks (12 usages in 8 files)

| Files | Pattern | Fix |
| --- | --- | --- |
| `src/database/db.ts` | NODE_ENV check | Use `getEnv()` |
| `src/lib/query-client.ts` | NODE_ENV check | Use `getEnv()` |
| `src/lib/performance-metrics.ts` | NODE_ENV check | Use `getEnv()` |
| `src/hooks/use-performance-monitoring.tsx` | NODE_ENV check | Use `getEnv()` |
| `src/app/api/seed/route.ts` | NODE_ENV check | Use `getEnv()` |
| `src/scripts/seed/run.ts` | NODE_ENV check | Use `getEnv()` |
| `src/components/layout/layout-provider.tsx` | NODE_ENV check | Use `getEnv()` |
| `src/components/optimized/performance-monitoring-provider.tsx` | NODE_ENV check | Use `getEnv()` |

**Status:** ⏳ READY TO IMPLEMENT

---

### Phase 4C: Directory-by-Directory Audit

#### Directory 1: `docs/**`

- [ ] Delete superseded files
- [ ] Verify critical references exist

**Status:** ⏳ (Covered in Batch 1B)

---

#### Directory 2: `src/app/**`

**Checks:**

- [ ] Async params (Next.js 16) — all await
- [ ] No browser APIs in Server Components
- [ ] Error boundaries present
- [ ] Loading states defined
- [ ] Metadata exports present

**Status:** ⏳ AUDIT REQUIRED

---

#### Directory 3: `src/components/**`

**Checks:**

- [ ] No duplicate components (covered in 1C)
- [ ] Barrel exports created (covered in 1C)
- [ ] `"use client"` correctness
- [ ] No `useMemo`/`useCallback`/`memo()`
- [ ] No `any` in props
- [ ] Dark mode tokens present

**Status:** ⏳ AUDIT REQUIRED

---

#### Directory 4: `src/actions/**`

**Pattern Check:**

- [ ] auth → validate → mutate → revalidate → ActionResult<T>
- [ ] Move `auth-db.ts` to dal
- [ ] Fix goals.actions.ts import
- [ ] Investigate reading-progress duplicates

**Status:** ⏳ AUDIT REQUIRED

---

#### Directory 5: `src/dal/**`

**Pattern Check:**

- [ ] ALL extend BaseDal<T> (fix SearchDAL)
- [ ] `.with()` eager loading on all queries
- [ ] `$inferSelect` types (no raw types)
- [ ] Return `null` not `undefined`
- [ ] Fix 2 `any` types
- [ ] Investigate comment-rating bundling

**Status:** ⏳ AUDIT REQUIRED

---

#### Directory 6: `src/hooks/**`

**Status:** ✅ 6 files, ALL CLEAN (verified)

---

#### Directory 7: `src/lib/**`

**Status:** ✅ 8 files, MOSTLY CLEAN **Action:** Fix process.env in redis.ts

---

#### Directory 8: `src/schemas/**`

**Checks:**

- [ ] Delete dead `comic-schema.ts`
- [ ] Zod v4 syntax
- [ ] Schema composition
- [ ] Type inference correctness

**Status:** ⏳ AUDIT REQUIRED

---

#### Directory 9: `src/tests/**`

**Checks:**

- [ ] Delete `example.spec.ts`
- [ ] Rename `comic-schema.spec.ts` → `comic.schema.spec.ts`
- [ ] Verify setup-env.ts current

**Status:** ⏳ AUDIT REQUIRED

---

#### Directory 10: `src/types/**`

**Status:** ✅ 7 files, ALL CLEAN (verified)

---

#### Directory 11: `src/scripts/**`

**Checks:**

- [ ] Consistent kebab-case naming
- [ ] ALL have `--dry-run`/`--verbose`/`--yes` flags
- [ ] ALL in package.json

**Status:** ⏳ AUDIT REQUIRED

---

### Batch 4 Verification Checklist

- [ ] `pnpm type-check` → 0 errors
- [ ] `pnpm test` → all passing
- [ ] `pnpm build` → success
- [ ] `grep -r "process\.env\." src/ --include="*.ts" --include="*.tsx" | grep -v "lib/env.ts"` → 0 results
- [ ] `grep -r "^[^/]*any" src/dal/ --include="*.ts"` → 0 unconstrained any types

**Status:** ⏳ IMPLEMENTATION PENDING

---

## BATCH 5: CI/CD + Phase Master Plan

**Goal:** Modernize CI/CD workflows, create comprehensive phase task document  
**Priority:** HIGH  
**Estimated Duration:** 3-4 hours

### Phase 5A: CI/CD Workflow Modernization (Implementer)

#### Task 5A.1: test.yml

**Updates:**

- Node 18→20
- pnpm v8→latest via `pnpm/action-setup@v3`
- `actions/cache@v3`→v4
- `upload-artifact@v3`→v4
- `codecov@v3`→v4
- Add quality gate artifact uploads + triage step

**Status:** ⏳ READY TO IMPLEMENT

---

#### Task 5A.2: playwright.yml

**Updates:**

- Replace `npm install -g pnpm` with `pnpm/action-setup@v3`
- Add pnpm cache
- Pin Node 20

**Status:** ⏳ READY TO IMPLEMENT

---

#### Task 5A.3: deploy.yml

**Updates:**

- Docker actions: buildx@v2→v3
- buildx: login@v2→v3
- docker: metadata@v4→v5
- build-push@v4→v5
- `github-script@v6`→v7
- Remove non-existent `notify-deployment.yml` reference

**Status:** ⏳ READY TO IMPLEMENT

---

#### Task 5A.4: copilot-setup-steps.yml

**Updates:**

- `checkout@v5`→v4 (v5 doesn't exist)

**Status:** ⏳ READY TO IMPLEMENT

---

#### Task 5A.5: All Workflows

**Updates:**

- Add `.references/` to `paths-ignore`
- Standardize Node 20 + pnpm latest

**Status:** ⏳ READY TO IMPLEMENT

---

### Phase 5B: Phase Task Master Plan (Architect)

**Output File:** NEW `docs/PHASE-MASTER-PLAN.md`

**Contents:**

1. Inventory all phases (1→4.5+) with micro-tasks and status
2. Completed phases: summary + links to completion reports
3. Pending phases: detailed tasks with ID, files, dependencies, complexity
4. Checkpoints: specific `pnpm` commands after each sub-phase
5. Recovery points: `git stash`, `git checkout .`, migration rollback
6. Code samples with diff for key changes
7. Dependency graph between tasks

**Status:** ⏳ READY TO IMPLEMENT

---

### Batch 5 Verification Checklist

- [ ] All 4 workflow files are valid YAML
- [ ] No v5 for checkout action
- [ ] No v2 for Docker actions
- [ ] `docs/PHASE-MASTER-PLAN.md` exists with all phases
- [ ] Final: `pnpm type-check && pnpm lint:fix && pnpm test && pnpm build` → ALL PASS

**Status:** ⏳ IMPLEMENTATION PENDING

---

## Implementation Priority Matrix

| Batch | Phase | Priority | Duration | Blocker? | Dependencies |
| --- | --- | --- | --- | --- | --- |
| 1 | Fix TS Errors | CRITICAL | 30m | No | None |
| 1 | Doc Cleanup | HIGH | 30m | No | None |
| 1 | Components | HIGH | 1h | No | None |
| 1 | VS Code | MEDIUM | 1h | No | None |
| 2 | Analyze Scripts | HIGH | 1h | No | Batch 1 |
| 2 | Port Scripts | HIGH | 2h | No | Batch 1 |
| 2 | Enhance Scripts | HIGH | 1h | No | Port Scripts |
| 2 | Shell Scripts | MEDIUM | 1h | No | Port Scripts |
| 2 | package.json | HIGH | 30m | No | Port Scripts |
| 3 | Seed Enhancement | HIGH | 2h | No | Batch 2 |
| 3 | Quality Gate | HIGH | 1h | No | Batch 2 |
| 3 | Triage | HIGH | 1h | No | Quality Gate |
| 4 | Pre-identified | CRITICAL | 2h | Yes | Batch 1-3 |
| 4 | process.env | CRITICAL | 2h | Yes | Batch 1-3 |
| 4 | Directory Audit | HIGH | 3h | Yes | Pre-identified |
| 5 | CI/CD | HIGH | 1.5h | No | Batch 4 |
| 5 | Phase Plan | MEDIUM | 1.5h | No | All Batches |

**Total Estimated Time:** 24-32 hours

---

## Execution Strategy

### Sequential Approach (Recommended)

1. ✅ Batch 1 (foundation) → COMMIT
2. → Batch 2 (scripts) → COMMIT
3. → Batch 3 (seeds) → COMMIT
4. → Batch 4 (audit) → COMMIT
5. → Batch 5 (CI/CD) → COMMIT + DEPLOY

### Parallel Approach (If resources available)

- Batch 1 (foundation-blocking)
- THEN Batches 2, 3, 4 in parallel
- THEN Batch 5

---

## Decision Log

1. ✅ **5 batches** (consolidated from original 4 + expanded scope)
2. ✅ **Full consolidation** of 92 reference scripts into unified superset
3. ✅ **Direct deletion** with git as backup
4. ✅ **TS errors** fixed in Batch 1 as foundation
5. ✅ **TypeScript scripts** in `src/scripts/`, **shell scripts** in root
6. ✅ **All scripts** must have `--dry-run`, `--verbose`, `--yes`, `--json`
7. ✅ **auth-db.ts** → move to `src/dal/` (does DB queries)
8. ✅ **SearchDAL** → make it extend `BaseDal<T>`
9. ✅ **process.env** → fix ALL 20 violations (including NODE_ENV checks)
10. ✅ **Dead files** → delete `comic-schema.ts` + `example.spec.ts`
11. ✅ **Reading-progress duplicates** → investigate and merge
12. ✅ **comment-rating bundling** → investigate before splitting
13. ✅ **User seeder** → 10 users default (3 admin, 3 mod, 4 user)
14. ✅ **Checkpoint file** → project root `.seed-checkpoint.json` (gitignored)
15. ✅ **Batch 4 depth** → fix ALL issues (not just list)

---

## Next Steps

### Immediate (Next Session)

1. **Batch 1 Implementation** (Foundation)
   - [ ] Verify TS errors (DONE ✅)
   - [ ] Delete superseded docs
   - [ ] Resolve component duplicates
   - [ ] Create barrel exports
   - [ ] Delete shadcn-studio/
   - [ ] Audit VS Code config
   - [ ] Run `pnpm type-check && pnpm test` → Verify ✅

2. **Create docs/refactor-context.md** (for Batch 2A)

3. **Begin Batch 2** (Scripts Consolidation)

---

## References

- **run.prompt.md** — Master Implementation Plan
- **setup-enhanced.prompt.md** — Implementation Workflow
- **quality-gate-debugger.prompt.md** — Quality Gate Debugging

---

**Document Generated:** March 13, 2026  
**Status:** READY FOR IMPLEMENTATION  
**Next Update:** After Batch 1 completion
