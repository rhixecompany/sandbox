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

**Goal**: Fix blockers, remove dead weight, establish clean baseline.

### Phase 1A: Fix TypeScript Errors (Debugger)

**File**: `src/components/search/search-results.tsx` (3 errors)

1. Verify bookmark import is `@/components/comics/bookmark-button` (TS2307)
2. Fix `comic.id` string→number mismatch: `Number(comic.id)` or update ComicCard props (TS2322)
3. Fix `comic.synopsis` nullable→optional: `comic.synopsis ?? undefined` (TS2322)
4. **Verify**: `pnpm type-check` → 0 errors

### Phase 1B: Documentation Cleanup (Reviewer)

**DELETE 6 files** (superseded):

- `docs/PHASE_2_COMPLETION.md`, `docs/PHASE_3_COMPLETION.md`
- `docs/PHASE4-3-DAY4-COMPLETE.md`, `docs/PHASE4-3-DAYS4-5-PLAN.md`
- `docs/debugger-context-map.md`, `docs/COMICWISE-PROJECT-STATUS.md`

**KEEP 19 files**: dev.content.md, database-context-map.md, SCRIPTS.md, QUICK_START.md, etc.

### Phase 1C: Components Cleanup (Reviewer)

1. **Resolve reading/reading-progress duplication**: 2 same-named files exist in both dirs (`reading-stats-card.tsx`, `continue-reading-card.tsx`). Grep imports → keep active one → delete duplicate → update imports.
2. **Create barrel exports**: `src/components/bookmarks/index.ts` (4 exports), `src/components/search/index.ts` (5 exports)
3. **Delete**: `src/components/shadcn-studio/` entirely (17 demo files)
4. **Check**: `src/app/admin/data.json` — delete if unused

### Phase 1D: VS Code Config Audit (Reviewer)

1. `settings.json`: Add `.references/` to `files.exclude` + `search.exclude`
2. `tasks.json`: Remove 28 one-time tasks, keep 13 reusable
3. `launch.json`: Verify all 9 configs reference valid scripts
4. `extensions.json`: Verify all 40 extension IDs still valid
5. `mcp.json`: Verify all 5 MCP servers accessible

### Batch 1 Verification

```
pnpm type-check → 0 errors
pnpm test → 241/241 passing
pnpm build → success
grep -r "shadcn-studio" src/ → 0 results
```

---

## Batch 2: Scripts Consolidation

**Goal**: Consolidate 92 reference scripts + 17 existing into unified DRY system.

### Phase 2A: Analyze & Categorize (Reviewer)

Read ALL scripts in `.references/comicwise/scripts/` and `.references/comicr/scripts/`. Categorize: Already Implemented | High-Value Missing | Redundant | Not Applicable. Create `docs/refactor-context.md` with categorized inventory + code samples grouped by Infrastructure, Database, Optimization, DevOps, Quality, Scaffolding.

### Phase 2B: Port New TypeScript Scripts (Implementer)

Create 5 in `src/scripts/` — ALL with `--dry-run`, `--verbose`, `--yes`, `--json`:

1. `project-cleanup.ts` — deep cleanup (duplicates, unused, temp files)
2. `cleanup-duplicates.ts` — pattern-based duplicate detection
3. `optimize-performance.ts` — bundle analysis + caching audit
4. `validate-env.ts` — env validation + `.env.local.example` sync
5. `fix-line-endings.ts` — CRLF→LF normalization

All use `confirmAction.ts` for destructive ops + Logger pattern from seed system.

### Phase 2C: Enhance Existing Scripts (Implementer)

1. `analyze-project.ts` — add security scan patterns
2. `scaffold.ts` — add DAL, schema, action templates
3. Audit ALL scripts for flag consistency (`--dry-run`, `--verbose`, `--yes`, `--json`)

### Phase 2D: Shell Scripts (Implementer)

1. Enhance `setup-dev.sh`/`.ps1` — add `--skip-db`, `--skip-seed`, `--skip-install`
2. Enhance `quality-gate.sh`/`.ps1` — add `tee`/`Tee-Object`, `pnpm build:debug`, timing, JSON summary
3. **NEW**: `dev.sh`/`dev.ps1` — prerequisites + dev server + browser
4. **NEW**: `cleanup.sh`/`cleanup.ps1` — artifact removal with dry-run

### Phase 2E: Update package.json (Implementer)

Add: `cleanup:project`, `cleanup:project:dry`, `cleanup:duplicates`, `cleanup:duplicates:dry`, `optimize:performance`, `optimize:performance:dry`, `validate:env`, `fix:line-endings`, `fix:line-endings:dry`. Verify existing, remove dead entries.

### Batch 2 Verification

```
pnpm type-check → 0 errors
tsx src/scripts/project-cleanup.ts --dry-run --verbose → runs
tsx src/scripts/validate-env.ts --dry-run → runs
docs/refactor-context.md exists with content
All package.json entries resolve
```

---

## Batch 3: Seeds + Quality Gate + Triage

**Goal**: Enhance seeders, add chunked processing + resume, create quality gate + triage system.

### Part A: Seed System Enhancement (Reviewer → Implementer)

**Audit**: Read all 10 seeders. Identify warnings, type issues, duplication, bottlenecks.

**Enhance User Seeder** (`user-seeder.ts`):

- Default: 10 users (3 admin, 3 moderator, 4 user) — configurable via `--count`
- Avatar URLs, email variations, configurable bcrypt rounds
- `--dry-run` validation

**Enhance Comic Image Seeder** (`comic-image-seeder.ts`):

- Multi-strategy (URL/local/ImageKit), thumbnail refs, dimension validation
- Fallback placeholders, parallel processing, progress tracking

**Enhance Chapter Image Seeder** (`chapter-image-seeder.ts`):

- Sequential page ordering, format validation
- Bulk insert for 150k+ images, resumable, streaming, ETA

**Batch Fix**:

- Standardize error handling, `onConflictDoNothing` vs `onConflictDoUpdate`
- Add missing Zod schemas, ensure transaction rollback

**Chunked Processing & Resume** (chapter-seeder, chapter-image-seeder, comic-seeder):

1. Chunk batches (default 500) with multi-row `db.insert().values(chunkArray)`
2. `.seed-checkpoint.json` in project root (add to `.gitignore`)
3. `--resume` flag — continue from checkpoint
4. Yield intervals between chunks
5. Update `base-seed.ts` with `processInChunks()` helper
6. Update `types.ts`: add `chunkSize?: number`, `resume?: boolean` to SeedOptions

### Part B: Quality Gate Scripts (Implementer)

Enhance `quality-gate.sh`/`.ps1`:

```
pnpm type-check 2>&1 | tee type-check.txt
pnpm lint:fix 2>&1 | tee lint-fixed.txt
pnpm test --run 2>&1 | tee test-report.txt
pnpm build:debug 2>&1 | tee build-report.txt
```

Add: per-gate timing, `--continue-on-error`, skip flags, color logging, JSON summary.

### Part C: Debugger Triage (Debugger)

Create `src/scripts/triage-quality-gate.ts`:

1. Parse 4 .txt files → extract TS errors, ESLint issues, test failures, build errors
2. Triage: CRITICAL → HIGH → MEDIUM → LOW, group by file
3. Output `quality-gate-triage.json` + console summary
4. Suggest auto-fixes, add to package.json as `"triage"`
5. Read triage → fix CRITICAL first → re-run quality gate

### Batch 3 Verification

```
pnpm seed:validate → all pass
pnpm type-check → 0 errors
quality-gate.sh --continue-on-error → produces 4 .txt + JSON
pnpm triage → produces quality-gate-triage.json
```

---

## Batch 4: Full Source Audit (Fix Everything)

**Goal**: Deep audit all 11 directories, fix EVERY issue found.

### Pre-Identified Issues to Fix

| # | File | Issue | Fix |
| --- | --- | --- | --- |
| 1 | `src/actions/auth-db.ts` | Not a Server Action (no `"use server"`) | Move to `src/dal/auth-db.ts` |
| 2 | `src/dal/search-dal.ts` | Only DAL not extending `BaseDal<T>` | Make it extend `BaseDal<ComicType>` |
| 3 | `src/dal/search-dal.ts` L116,118 | 2 `any` types | Replace with proper interfaces |
| 4 | `src/actions/goals.actions.ts` | Wrong import `./actions-types` | Change to `@/types/actions-types` |
| 5 | `src/schemas/comic-schema.ts` | Dead file — imported nowhere | Delete |
| 6 | `src/tests/example.spec.ts` | Playwright placeholder | Delete |
| 7 | `src/tests/schemas/comic-schema.spec.ts` | Name doesn't match what it tests | Rename to `comic.schema.spec.ts` |
| 8 | `src/actions/reading-progress.actions.ts` + `reading-progress.ts` | Potential duplicates | Investigate and merge |
| 9 | `src/dal/comment-rating-dal.ts` | Bundles 2 DALs in one file | Investigate if should split |
| 10 | 12 files (20 usages) | `process.env` used directly | Migrate ALL to `getEnv()` |

### process.env Violations to Fix (ALL 20)

**Auth/service configs (8 usages):**

- `src/auth-providers.ts` — GITHUB*CLIENT_ID, KEYCLOAK*\* (4)
- `src/auth-config.ts` — AUTH_SECRET (1)
- `src/lib/cache/redis.ts` — UPSTASH*REDIS_REST*\* (2)
- `src/scripts/seed/images/image-kit-uploader.ts` — IMAGEKIT\_\* (3 — counted separately but 3 env vars)

**NODE_ENV checks (12 usages in 8 files):**

- `src/database/db.ts`, `src/lib/query-client.ts`, `src/lib/performance-metrics.ts`
- `src/hooks/use-performance-monitoring.tsx`, `src/app/api/seed/route.ts`
- `src/scripts/seed/run.ts`, `src/components/layout/layout-provider.tsx`
- `src/components/optimized/performance-monitoring-provider.tsx`

### Directory-by-Directory Audit

**Directory 1: `docs/**`\*\* — Delete superseded files, verify critical references exist

**Directory 2: `src/app/**`\*\* — Verify async params (Next.js 16), no browser APIs in Server Components, error boundaries, loading states, metadata exports

**Directory 3: `src/components/**`** — Duplicate components, barrel exports, `"use client"`correctness, no`useMemo`/`useCallback`/`memo()`, no `any` in props, dark mode tokens

**Directory 4: `src/actions/**`** — Pattern: auth → validate → mutate → revalidate → ActionResult<T>. Move `auth-db.ts` to dal. Fix goals.actions.ts import. Investigate reading-progress duplicates.

**Directory 5: `src/dal/**`** — Extend BaseDal<T> (fix SearchDAL). `.with()`eager loading.`$inferSelect`types.`null`not`undefined`. Fix 2 `any` types. Investigate comment-rating bundling.

**Directory 6: `src/hooks/**`\*\* — 6 files, ALL CLEAN (verified). Check SSR-safe dates.

**Directory 7: `src/lib/**`\*\* — 8 files, ALL CLEAN (verified). Fix process.env in redis.ts.

**Directory 8: `src/schemas/**`** — Delete dead `comic-schema.ts`. Verify Zod v4 syntax, composition, type inference.

**Directory 9: `src/tests/**`** — Delete `example.spec.ts`. Rename `comic-schema.spec.ts`→`comic.schema.spec.ts`. Verify setup-env.ts current.

**Directory 10: `src/types/**`** — 7 files, ALL CLEAN (verified). No `any`, uses `$inferSelect`.

**Directory 11: `src/scripts/**`** — Consistent kebab-case naming. All have `--dry-run`/`--verbose`/`--yes`. All in package.json.

### Batch 4 Verification

```
pnpm type-check → 0 errors
pnpm test → all passing (may change count after deletes)
pnpm build → success
grep -r "process\.env\." src/ --include="*.ts" --include="*.tsx" | grep -v "lib/env.ts" | grep -v node_modules → 0 results
grep -r "any" src/dal/ --include="*.ts" → 0 results for unconstrained any
```

---

## Batch 5: CI/CD + Phase Master Plan

**Goal**: Modernize CI/CD workflows, create comprehensive phase task document.

### Part A: CI/CD Workflow Modernization (Implementer)

**test.yml**:

- Node 18→20, pnpm v8→latest via `pnpm/action-setup@v3`
- `actions/cache@v3`→v4, `upload-artifact@v3`→v4, `codecov@v3`→v4
- Add quality gate artifact uploads + triage step

**playwright.yml**:

- Replace `npm install -g pnpm` with `pnpm/action-setup@v3`
- Add pnpm cache, pin Node 20

**deploy.yml**:

- Docker actions: buildx@v2→v3, login@v2→v3, metadata@v4→v5, build-push@v4→v5
- `github-script@v6`→v7, remove non-existent `notify-deployment.yml` reference

**copilot-setup-steps.yml**:

- `checkout@v5`→v4 (v5 doesn't exist)

**All**: Add `.references/` to `paths-ignore`, standardize Node 20 + pnpm latest.

### Part B: Phase Task Master Plan (Architect)

Create `docs/PHASE-MASTER-PLAN.md`:

1. Inventory all phases (1→4.5+) with micro-tasks and status
2. Completed phases: summary + links to completion reports
3. Pending phases: detailed tasks with ID, files, dependencies, complexity
4. Checkpoints: specific `pnpm` commands after each sub-phase
5. Recovery points: `git stash`, `git checkout .`, migration rollback
6. Code samples with diff for key changes
7. Dependency graph between tasks

### Batch 5 Verification

```
All 4 workflow files are valid YAML
No v5 for checkout, no v2 for docker actions
docs/PHASE-MASTER-PLAN.md exists with all phases
Final: pnpm type-check && pnpm lint:fix && pnpm test && pnpm build → ALL PASS
```

---

## Relevant Files

### Batch 1

- `src/components/search/search-results.tsx` — fix 3 TS errors
- `src/components/reading/index.ts`, `src/components/reading-progress/index.ts` — dedup
- `src/components/bookmarks/index.ts`, `src/components/search/index.ts` — create
- `src/components/shadcn-studio/` — delete (17 files)
- `docs/` — delete 6 files
- `.vscode/settings.json`, `.vscode/tasks.json` — audit

### Batch 2

- `src/scripts/*.ts` — 17 existing (enhance) + 5 new
- `docs/refactor-context.md` — NEW
- `quality-gate.sh`, `quality-gate.ps1` — enhance
- `dev.sh`, `dev.ps1`, `cleanup.sh`, `cleanup.ps1` — NEW
- `package.json` — update scripts

### Batch 3

- `src/scripts/seed/seeders/user-seeder.ts` — enhance (10 users default)
- `src/scripts/seed/seeders/comic-image-seeder.ts` — enhance
- `src/scripts/seed/seeders/chapter-image-seeder.ts` — enhance + chunked
- `src/scripts/seed/seeders/chapter-seeder.ts` — chunked + resume
- `src/scripts/seed/seeders/comic-seeder.ts` — chunked
- `src/scripts/seed/seeders/base-seed.ts` — add processInChunks()
- `src/scripts/seed/types.ts` — add chunkSize, resume
- `.seed-checkpoint.json` — NEW (gitignored)
- `quality-gate.sh`, `quality-gate.ps1` — tee streaming
- `src/scripts/triage-quality-gate.ts` — NEW

### Batch 4

- `src/actions/auth-db.ts` → move to `src/dal/auth-db.ts`
- `src/dal/search-dal.ts` — extend BaseDal, fix 2 any types
- `src/actions/goals.actions.ts` — fix import path
- `src/schemas/comic-schema.ts` — delete (dead)
- `src/tests/example.spec.ts` — delete (placeholder)
- `src/tests/schemas/comic-schema.spec.ts` → rename to `comic.schema.spec.ts`
- `src/actions/reading-progress.actions.ts` + `reading-progress.ts` — investigate/merge
- `src/dal/comment-rating-dal.ts` — investigate
- 12 files — fix 20 process.env violations

### Batch 5

- `.github/workflows/test.yml` — modernize
- `.github/workflows/deploy.yml` — fix Docker versions
- `.github/workflows/playwright.yml` — fix pnpm setup
- `.github/workflows/copilot-setup-steps.yml` — fix checkout
- `docs/PHASE-MASTER-PLAN.md` — NEW

---

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
