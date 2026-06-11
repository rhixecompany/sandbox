# ComicWise Session Prompt

**Project**: Next.js 16.1.6 manga/comic reader with App Router, React 19 Server Components, Drizzle ORM + PostgreSQL, NextAuth v5, Zustand, React Query, shadcn/Radix UI, Tailwind CSS v4, Vitest + Playwright.

**Status** (March 13, 2026):

- ✅ Phase 4.3 (Reading Analytics) COMPLETE
- ✅ Batch 4 (Code Audit) COMPLETE: 98/100 quality score
- ✅ All 241 tests passing | 0 TypeScript errors | Production-ready build

## Quick Commands

```bash
pnpm dev                 # Dev server (Turbopack, port 3000)
pnpm type-check          # Must be 0 errors
pnpm lint:fix            # Auto-fix issues
pnpm test                # Unit tests (241/241)
pnpm build               # Production build
pnpm db:push             # Apply schema changes
pnpm db:studio           # Drizzle GUI browser
pnpm seed:all            # Populate database
```

## Architecture

**Data Flow**: Server Component → await params → DAL query with `.with()` eager loading → pass data as props → Client Component → Zustand/React Query

**Key Directories**:

- `src/app/` — Pages (App Router)
- `src/dal/` — Data Access Layer (Drizzle with eager loading)
- `src/actions/` — Server Actions (mutations, never throw)
- `src/schemas/` — Zod validation (one per domain)
- `src/components/` — React components (120+ with dark mode)
- `src/database/` — Drizzle schema (27 tables, 4 enums)
- `src/scripts/seed/` — Seeding system with dependency orchestration

## Coding Rules (Enforced by ESLint/Compiler)

1. **No `any` types** → Use proper types or `unknown`
2. **No manual memoization** → React Compiler is ON
3. **No raw `process.env`** → Use `getEnv()` from `src/lib/env.ts`
4. **No N+1 queries** → Always `.with()` for eager loading
5. **No API routes for mutations** → Use Server Actions
6. **Async params** (v16) → Must `await` params/searchParams
7. **Cascade deletes** → Preferred; exceptions: `comic.authorId/artistId/typeId`, `bookmark.lastReadChapterId`, `auditLog.userId`
8. **Soft deletes** → Only `user` and `comment` tables have `deletedAt`

## Path Aliases (tsconfig.json)

```
@/*        → src/*
ui         → src/components/ui/*
database   → src/database/*
schemas    → src/schemas/*
hooks      → src/hooks/*
lib        → src/lib/*
components → src/components/*
```

## Key Patterns

### DAL Pattern

```typescript
import { BaseDal } from "./base-dal";
type EntityType = typeof entity.$inferSelect;

export class EntityDal extends BaseDal<EntityType> {
  async list() {
    return db.query.entity.findMany({
      with: { relations: true } // Always eager load
    });
  }
}
export const entityDal = new EntityDal();
```

### Server Action Pattern

```typescript
"use server";
import { auth } from "@/auth";
import type { ActionResult } from "./types";

export async function actionName(
  input: unknown
): Promise<ActionResult<T>> {
  // 1. Auth first
  const session = await auth();
  if (!session?.user?.id)
    return { ok: false, error: "Not authenticated" };

  // 2. Validate
  const parsed = Schema.safeParse(input);
  if (!parsed.success)
    return { ok: false, error: parsed.error.errors[0]?.message };

  try {
    // 3. Mutate
    const result = await dal.create(parsed.data);
    revalidatePath("/path");
    return { ok: true, data: result };
  } catch (error) {
    return { ok: false, error: "Failed to create" };
  }
}
```

### Component Pattern (with JSDoc + Dark Mode)

```typescript
/**
 * Component Name
 * Brief description of purpose and usage
 */
interface ComponentNameProps {
  /** Description of required prop */
  title: string;
  /** Optional prop with default */
  variant?: "primary" | "secondary";
}

export function ComponentName({ title, variant = "primary" }: ComponentNameProps) {
  return (
    <article className="rounded-lg border p-4 dark:border-muted-foreground">
      <h2 className="text-lg font-semibold dark:text-foreground">{title}</h2>
    </article>
  );
}
```

## Database Facts

- `comic.rating` = `decimal(10,1)` (aggregate with AVG)
- `comicStatus` enum: "Ongoing", "Hiatus", "Completed", "Dropped", "Season End", "Coming Soon"
- `user.id` = text (UUID), not integer
- `bookmark` = composite PK on `(userId, comicId)`
- **Enums (4 total)**: `userRole`, `comicStatus`, `resourceEnum`, `actionEnum`
- **Soft deletes**: Only `user` and `comment` tables have `deletedAt`

## Reference Files

- `.github/copilot-instructions.md` — Complete ComicWise guide (2500+ lines)
- `.github/instructions/` — Auto-loaded rules by file pattern
- `docs/dev.content.md` — 26 sections with patterns & examples
- `docs/MASTER_PHASE_PLAN_4-6.md` — Phase planning
- `AGENTS.md` — Quick setup reference

## Quality Gate (Must Pass Before PR)

```bash
pnpm type-check && pnpm lint:fix && pnpm test && pnpm build
```

## Testing

- **Unit**: Vitest (jsdom), setup at `src/tests/setup-env.ts`
- **E2E**: Playwright, use `test.step()` for readability
- **Coverage**: 241/241 tests passing (0 regressions)
- **Mock external deps**: Database, auth in setup-env.ts

## Common Tasks

| Task         | Command                               |
| ------------ | ------------------------------------- |
| Start dev    | `pnpm dev`                            |
| Check health | `pnpm validate` (runs all checks)     |
| Format code  | `pnpm lint:fix`                       |
| Single test  | `pnpm test src/path/to/file.test.tsx` |
| DB migration | `pnpm db:push`                        |
| Seed data    | `pnpm seed:all`                       |

## When Stuck

1. **Architecture questions** → Ask about system design before coding
2. **Component issues** → Reference `.github/instructions/design-system.instructions.md`
3. **Database queries** → Check DAL examples (eager loading with `.with()`)
4. **Type errors** → Use `getEnv()` not `process.env`, import types with `import type`
5. **Tests failing** → Check mocks in `src/tests/setup-env.ts`

## Session Workflow

1. **Start**: `pnpm install && pnpm db:push && pnpm dev`
2. **Work**: Follow patterns above, run quality gates frequently
3. **Commit**: `pnpm validate` must pass (0 errors, 241/241 tests)
4. **Verify**: `pnpm build` for production readiness

## Next Phase

**Phase 4.4 (Social Features)**: Reviews, ratings, sharing (estimated 4-5 days)

Dependencies: ✅ Phase 4.3 complete, all gates passing

---

**Last Updated**: March 13, 2026 | **Quality**: 98/100 | **Production Ready**: ✅
