# Batch 4: Full Source Audit (Fix Everything)

> Extracted from `run.prompt.md`.

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
