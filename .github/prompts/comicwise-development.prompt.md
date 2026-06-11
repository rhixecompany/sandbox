---
title: "ComicWise Development Workflow"
description: "Reusable prompt for ComicWise development sessions"
applyTo: "**/*"
tags: ["nextjs", "typescript", "drizzle", "react19", "development"]
---

# ComicWise Development Prompt

**Version**: 1.0 **Last Updated**: March 13, 2026 **Quality Score**: 98/100 **Production Ready**: ✅ Yes

## Project State Summary

**ComicWise** is a production-ready Next.js 16.1.6 manga/comic reader with:

- ✅ Phase 4.3 (Reading Analytics) complete
- ✅ Batch 4 (Code Audit & Standardization) complete
- ✅ 241/241 tests passing (zero regressions)
- ✅ 0 TypeScript errors enforced
- ✅ 100% dark mode coverage
- ✅ WCAG 2.1 AA accessibility
- ✅ 98/100 architecture quality score

### Tech Stack

- **Framework**: Next.js 16.1.6 (App Router, React 19)
- **Database**: PostgreSQL (Neon) + Drizzle ORM (27 tables, 4 enums)
- **Auth**: NextAuth v5 (database sessions, GitHub/Credentials/Keycloak)
- **State**: Zustand (client) + React Query v5 (server)
- **UI**: shadcn/Radix UI + Tailwind CSS v4 (120+ components)
- **Testing**: Vitest (jsdom) + Playwright 1.58.2
- **Build**: Turbopack (dev), Webpack (prod)

## Quick Start (New Session)

```bash
# 1. Install & setup
pnpm install
cp .env.local.example .env.local    # Edit with your DATABASE_URL, AUTH_SECRET
pnpm db:push

# 2. Start development
pnpm dev                            # Port 3000, Turbopack

# 3. Run quality gates
pnpm validate                       # Runs: type-check, lint:fix, test, health checks
```

## Essential Commands

| Command           | Purpose                         | Must Pass   |
| ----------------- | ------------------------------- | ----------- |
| `pnpm dev`        | Start dev server (Turbopack)    | —           |
| `pnpm type-check` | TypeScript validation           | ✅ 0 errors |
| `pnpm lint:fix`   | ESLint + Prettier auto-fix      | ✅ All pass |
| `pnpm test`       | Vitest unit tests (jsdom)       | ✅ 241/241  |
| `pnpm build`      | Production build (Webpack)      | ✅ Success  |
| `pnpm validate`   | All quality gates at once       | ✅ All pass |
| `pnpm db:push`    | Apply schema changes (dev only) | —           |
| `pnpm db:studio`  | Drizzle visual browser          | —           |
| `pnpm seed:all`   | Populate database               | —           |

## Data Flow Architecture

```
HTTP Request
    ↓
Next.js Middleware (src/proxy.ts)
  • Auth check (await auth())
  • Route protection (/profile, /bookmarks, /ratings, /admin)
    ↓
Server Component (App Router page)
  • Await async params/searchParams (v16 breaking change)
  • Call DAL methods for data
    ↓
DAL Layer (src/dal/*-dal.ts)
  • All queries use Drizzle with eager loading (.with())
  • Never use raw SQL or loop queries (no N+1)
  • Return properly typed results ($inferSelect)
    ↓
Client Component / Zustand / React Query
  • Use props data from Server Component
  • Zustand for UI state (reader mode, sidebar toggle)
  • React Query for dynamic server state
    ↓
Server Actions (src/actions/*-actions.ts)
  • Mutations: auth → validate → mutate → revalidate
  • Never throw: return ActionResult<T> (ok + data/error)
    ↓
HTTP Response
```

## Project Structure

```
src/
├── app/                     # Next.js App Router pages
│   ├── (auth)/             # Public auth pages (/sign-in, /sign-up)
│   ├── (root)/             # Main app pages
│   ├── admin/              # Admin-only routes (middleware-protected)
│   └── api/                # API routes (auth/, health-checks)
│
├── dal/                    # Data Access Layer (Drizzle queries)
│   ├── base-dal.ts         # Abstract BaseDal<T> base class
│   ├── comic-dal.ts        # Comic queries with .with() eager loading
│   ├── chapter-dal.ts      # Chapter queries
│   ├── bookmark-dal.ts     # Bookmark queries
│   └── ...                 # One DAL per entity
│
├── actions/                # Server Actions (mutations)
│   ├── types.ts            # ActionResult<T> discriminated union
│   ├── comic.actions.ts    # Comic mutations
│   ├── bookmark.actions.ts # Bookmark mutations
│   └── ...                 # One file per domain
│
├── schemas/                # Zod validation schemas
│   ├── comic.schema.ts     # Comic validation (create, update, filter)
│   ├── bookmark.schema.ts  # Bookmark validation
│   └── ...                 # One schema per domain
│
├── components/             # React components (120+)
│   ├── ui/                 # shadcn/Radix primitives
│   ├── comics/             # Comic-specific components
│   ├── bookmarks/          # Bookmark components
│   ├── reading/            # Reader components
│   ├── analytics/          # Analytics dashboard
│   └── layout/             # Layout components (Sidebar, Header)
│
├── database/
│   ├── db.ts               # Drizzle singleton (postgres-js driver)
│   └── schema.ts           # 27 table definitions, 4 enums, relations
│
├── hooks/                  # Custom React hooks
│   ├── use-now.tsx         # SSR-safe useCurrentYear()
│   ├── use-debounce.ts     # Debounced values
│   ├── use-mobile.ts       # Mobile detection
│   └── ...
│
├── stores/                 # Zustand client state
│   ├── use-bookmark-store.ts
│   ├── use-reader-store.ts
│   └── ...
│
├── lib/
│   ├── env.ts              # Zod-validated getEnv() singleton
│   ├── utils.ts            # cn() tailwind class merger
│   ├── query-client.ts     # React Query config
│   └── ...
│
├── scripts/                # CLI scripts
│   └── seed/               # Seeding system with dependency orchestration
│
├── tests/                  # Test setup
│   └── setup-env.ts        # Vitest jsdom mocks + setup
│
├── auth.ts                 # NextAuth init
├── auth-config.ts          # Session strategy, callbacks
├── auth-providers.ts       # OAuth/Credentials/OIDC providers
├── auth-adapter.ts         # Drizzle adapter
└── proxy.ts                # Middleware for route protection

docs/                       # Documentation
├── dev.content.md          # 26 sections with patterns & examples
├── DEVELOPMENT.md          # Developer guide
├── database-context-map.md # Entity relationships
└── MASTER_PHASE_PLAN_4-6.md # Phase planning

.github/
├── copilot-instructions.md # Complete 2500+ line guide
├── instructions/           # Auto-loaded by file pattern:
│   ├── design-system.instructions.md
│   ├── security-and-owasp.instructions.md
│   ├── performance-optimization.instructions.md
│   ├── testing.instructions.md
│   ├── typescript.instructions.md
│   ├── nextjs.instructions.md
│   └── ...                 # 15+ instruction files
└── prompts/
    ├── comicwise-session.prompt.md       # Quick reference
    └── comicwise-development.prompt.md   # This file
```

## Coding Rules (Enforced)

### Type Safety & Code Quality

1. **No `any` types** — ESLint: `no-explicit-any: "error"`
2. **No manual memoization** — React Compiler is ON (`useMemo`/`useCallback`/`memo()` forbidden)
3. **No raw `process.env`** — Use `getEnv()` from `src/lib/env.ts`
4. **No N+1 queries** — Always use `.with()` for eager loading in DAL
5. **No API routes for mutations** — Use Server Actions (`"use server"`)
6. **No `export const dynamic = "force-dynamic"`** — Use `<Suspense>` instead

### Next.js & React

7. **Async params (v16 breaking change)** — `params` and `searchParams` are `Promise`, must `await`
8. **Server Components by default** — Only mark with `"use client"` if hooks/browser APIs needed
9. **No browser APIs in Server Components** — Never `localStorage`, `window`, `Date.now()`

### Database & Mutations

10. **ActionResult<T> pattern** — Server Actions never throw; return `{ ok, data } | { ok, error }`
11. **Auth first** — First line in every Server Action: `const session = await auth()`
12. **Zod validate** — All external input → Zod schema → DB
13. **Cascade deletes preferred** — FK: `{ onDelete: "cascade" }`. Exceptions: `comic.authorId/artistId/typeId`, `bookmark.lastReadChapterId`, `auditLog.userId` (`set null`)
14. **$inferSelect for types** — Use `typeof table.$inferSelect`, not manual types
15. **Return null not undefined** — DAL methods return `null` when not found

### UI & Styling

16. **Tailwind v4 syntax** — `bg-linear-to-br` (not `bg-gradient-to-br`), `aspect-2/3`, `h-4!`
17. **Dark mode via semantic tokens** — `bg-card`, `text-foreground`, `border-muted-foreground` (not hardcoded colors)
18. **shadcn/ui components** — Use established components; add to registry via shadcn-cli if missing

## Path Aliases (tsconfig.json)

```typescript
@/*        → ./src/*
ui         → ./src/components/ui/*
database   → ./src/database/*
schemas    → ./src/schemas/*
env        → ./src/lib/env.ts
hooks      → ./src/hooks/*
appConfig  → ./appConfig.ts
lib        → ./src/lib/*
types      → ./src/types/*
components → ./src/components/*
utils      → ./src/lib/utils.ts
assets     → ./src/assets/*
styles     → ./src/styles/*
tests      → ./src/tests/*
```

## Common Patterns

### DAL Query Pattern (with Eager Loading)

```typescript
import { BaseDal } from "./base-dal";
type ComicType = typeof comic.$inferSelect;

export class ComicDal extends BaseDal<ComicType> {
  async list() {
    return db.query.comic.findMany({
      with: {
        author: true,
        genres: { with: { genre: true } },
        chapters: { orderBy: [c => desc(c.chapterNumber)] }
      }
    });
  }
}
export const comicDal = new ComicDal();
```

### Server Action Pattern (auth → validate → mutate → revalidate)

```typescript
"use server";
import { auth } from "@/auth";
import type { ActionResult } from "./types";

export async function createComicAction(
  input: unknown
): Promise<ActionResult<Comic>> {
  // 1. AUTH FIRST
  const session = await auth();
  if (!session?.user?.id)
    return { ok: false, error: "Not authenticated" };

  // 2. VALIDATE
  const parsed = CreateComicSchema.safeParse(input);
  if (!parsed.success)
    return { ok: false, error: parsed.error.errors[0]?.message };

  try {
    // 3. MUTATE
    const comic = await comicDal.create(parsed.data);

    // 4. REVALIDATE
    revalidatePath("/comics");
    revalidateTag("comics");

    // 5. RETURN ActionResult
    return { ok: true, data: comic };
  } catch (error) {
    return { ok: false, error: "Failed to create comic" };
  }
}
```

### Component Pattern (with JSDoc + Dark Mode)

```typescript
/**
 * Comic Card Component
 * Displays a comic in grid/list view with optional status/type overlay
 */
interface ComicCardProps {
  /** Comic object with all required fields */
  comic: Comic;
  /** Display variant */
  variant?: "grid" | "list";
}

export function ComicCard({ comic, variant = "grid" }: ComicCardProps) {
  return (
    <article className="rounded-lg border p-4 dark:border-muted-foreground">
      <h2 className="text-lg font-semibold dark:text-foreground">{comic.title}</h2>
      <p className="text-sm text-muted-foreground dark:text-muted-foreground">
        {comic.synopsis}
      </p>
    </article>
  );
}
```

### Zod Schema Composition

```typescript
// Base schema
const BaseComicSchema = z.object({
  title: z.string().min(1).max(255),
  slug: z.string().regex(/^[a-z0-9-]+$/),
  synopsis: z.string().min(10).max(5000)
});

// Extend for create
export const CreateComicSchema = BaseComicSchema.extend({
  authorId: z.string().uuid(),
  genreIds: z.array(z.string().uuid()).min(1)
});

// Extend for update (all optional)
export const UpdateComicSchema = BaseComicSchema.partial();

// Infer type automatically
export type Comic = z.infer<typeof CreateComicSchema>;
```

## Database Schema Facts

- **`comic.rating`** = `decimal(10,1)` — aggregate with `AVG(rating)`. The `rating.rating` column = `integer` (1–5 stars)
- **`comicStatus` enum**: "Ongoing", "Hiatus", "Completed", "Dropped", "Season End", "Coming Soon"
- **`user.id`** = `text` (UUID string), not integer
- **`bookmark`** = composite PK on `(userId, comicId)` → use `onConflictDoUpdate` for upserts
- **`bookmark.status`** = `text` field (default "Reading"), not pgEnum
- **4 enums total**: `userRole`, `comicStatus`, `resourceEnum`, `actionEnum`
- **Soft deletes**: Only `user` and `comment` tables have `deletedAt` → filter on those tables only
- **Cascade deletes**: Most FKs have `{ onDelete: "cascade" }`. Exceptions: `comic.authorId/artistId/typeId`, `bookmark.lastReadChapterId` (no cascade); `auditLog.userId` (`set null`)

## Testing Patterns

### Unit Tests (Vitest)

```typescript
import { describe, it, expect, beforeEach } from "vitest";
import { comicDal } from "@/dal/comic-dal";

describe("ComicDal", () => {
  beforeEach(() => {
    // Setup mocks from src/tests/setup-env.ts
  });

  it("should list comics with eager loading", async () => {
    const comics = await comicDal.list();
    expect(comics).toHaveLength(5);
    expect(comics[0].author).toBeDefined(); // Eager loaded
  });
});
```

### E2E Tests (Playwright)

```typescript
import { test, expect } from "@playwright/test";

test.describe("Comic Reader", () => {
  test.beforeEach(async ({ page }) => {
    await page.goto("http://localhost:3000/comics/test-comic");
  });

  test("should load chapter and display reader controls", async ({
    page
  }) => {
    await test.step("Load page", async () => {
      await expect(
        page.getByRole("heading", { name: "Chapter 1" })
      ).toBeVisible();
    });

    await test.step("Change reading mode", async () => {
      await page
        .getByRole("button", { name: /reading mode/i })
        .click();
      await expect(
        page.locator("[data-reading-mode]")
      ).toHaveAttribute("data-reading-mode", "scroll");
    });
  });
});
```

## Quality Gate (Must Pass Before Commits)

```bash
# Run all quality gates at once
pnpm validate

# Or run individually
pnpm type-check     # Must be 0 errors (blocks deployment)
pnpm lint:fix       # Auto-fix and validate
pnpm test           # Must pass 241/241 (no regressions)
pnpm build          # Must succeed (production build)
```

## Environment Variables

**Required** (in `.env.local`):

```
DATABASE_URL=postgresql://user:password@host:port/database
AUTH_SECRET=openssl rand -hex 32
```

**Optional** (see `.env.local.example` for full list):

- `AUTH_GITHUB_ID`, `AUTH_GITHUB_SECRET`
- `AUTH_KEYCLOAK_URL`, etc.
- `NEXTAUTH_URL` (override default)

All validated via `src/lib/env.ts` at startup using Zod.

## Reference Documentation

| File | Purpose | Scope |
| --- | --- | --- |
| `.github/copilot-instructions.md` | Complete guide (2500+ lines) | Global |
| `.github/prompts/comicwise-session.prompt.md` | Quick reference (400 lines) | Session shortcuts |
| `.github/instructions/*.md` | Auto-loaded by file pattern (15+ files) | Specific file types |
| `docs/dev.content.md` | 26 sections with patterns & examples | Development reference |
| `docs/MASTER_PHASE_PLAN_4-6.md` | Phase planning & task tracking | Project roadmap |
| `AGENTS.md` | This project's quick setup guide | Quick start |

## Common Troubleshooting

| Issue | Solution |
| --- | --- |
| Type errors (TS2307) | Check import path aliases in `tsconfig.json` |
| N+1 query errors | Add `.with({ relations: true })` to DAL queries |
| Action throws instead of returns | Wrap in try-catch, return `ActionResult<T>` |
| Styling not applying | Check Tailwind v4 syntax (`bg-linear-to-br` not `bg-gradient-to-br`) |
| DB connection fails | Verify `DATABASE_URL` and run `pnpm db:studio` to test |
| Tests fail in CI but pass locally | Check mocks in `src/tests/setup-env.ts` |
| Hydration mismatch | Use `useCurrentYear()` hook not `new Date()` in server code |

## When Stuck

1. **Architecture questions** — Check `.github/copilot-instructions.md` (2500+ lines) or ask about system design
2. **Component issues** — Reference `.github/instructions/design-system.instructions.md`
3. **Database/ORM** — Review DAL examples (eager loading with `.with()`)
4. **Type errors** — Use `getEnv()` not `process.env`, import types with `import type`
5. **Tests failing** — Check mocks in `src/tests/setup-env.ts`
6. **Performance** — Reference `.github/instructions/performance-optimization.instructions.md`

## Development Workflow

1. **Start session**: `pnpm install && pnpm db:push && pnpm dev`
2. **Make changes**: Follow patterns above, run `pnpm validate` frequently
3. **Commit**: Ensure `pnpm validate` passes (0 errors, 241/241 tests)
4. **Deploy**: Run `pnpm build` for production readiness
5. **Debug**: Use `pnpm test --watch` or `pnpm test:ui --debug` for debugging

## Next Phase

**Phase 4.4 (Social Features)**: Reviews, ratings, sharing

- **Estimated Duration**: 4-5 days
- **Dependencies**: ✅ Phase 4.3 complete, all gates passing
- **Success Criteria**: 0 type errors, 250+ passing tests, production build

**Future Phases**:

- **Phase 4.5** — Mobile optimization & PWA
- **Phase 6** — Advanced features

---

**Last Updated**: March 13, 2026 **Quality Score**: 98/100 **Production Status**: ✅ Ready **Support**: See docs/ and .github/instructions/ for detailed guides
