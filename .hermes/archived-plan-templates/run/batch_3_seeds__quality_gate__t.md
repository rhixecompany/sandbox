# Batch 3: Seeds + Quality Gate + Triage

> Extracted from `run.prompt.md`.

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
