# Relevant Files

> Extracted from `run.prompt.md`.

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
