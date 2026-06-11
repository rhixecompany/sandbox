# ComicWise — Development Guide

## Development Workflow

### Daily Commands

```bash
pnpm dev              # Start dev server (Turbopack)
pnpm type-check       # TypeScript validation
pnpm lint:strict      # ESLint (zero warnings required)
pnpm test             # Run unit tests
```

### Quality Gates (Required Before Every PR)

All five checks MUST pass with exit code 0:

```bash
pnpm lint:strict   # ESLint with zero warnings
pnpm triage        # Quality gate triage
pnpm type-check    # TypeScript compilation
pnpm test          # Vitest unit tests (jsdom)
pnpm build         # Production build (~35s)
```

## Code Conventions

### Critical Rules

| Rule | Enforcement | Alternative |
|------|-------------|-------------|
| **No `any` types** | ESLint `no-explicit-any: error` | Use `unknown` with type guards |
| **No manual memoization** | React Compiler enabled | Never use `useMemo`, `useCallback`, `memo` |
| **No raw `process.env`** | ESLint + appConfig.ts | Use `getEnv()` from `appConfig.ts` |
| **DAL returns `null`** | Convention | Not `undefined` when record not found |
| **Async params** | Next.js v16 | `const { id } = await params` |
| **ActionResult pattern** | Server Actions | Return `{ ok, data }` or `{ ok, error }` |
| **No N+1 queries** | Always use `.with()` | Eager loading in DAL |
| **No raw SQL** | Use Drizzle query builders | `eq()`, `and()`, `or()` |
| **No API routes for mutations** | Server Actions only | Use `"use server"` |
| **Auth check first** | Every action | `const session = await auth()` |

### Naming Conventions

| Type | Convention | Example |
|------|-----------|---------|
| Components | PascalCase | `ComicCard.tsx` |
| DAL files | kebab-case | `comic-dal.ts` |
| Actions | kebab-case | `comic.actions.ts` |
| Database tables | snake_case | `comic_genres` |
| Types/Interfaces | PascalCase | `ComicType` |

### DAL Pattern

```typescript
// dal/comic-dal.ts
import { db } from "@/database/db";
import { comics } from "@/database/schema";

export class ComicDAL {
  async findById(id: string) {
    return db.query.comics.findFirst({
      where: eq(comics.id, id),
      with: {
        chapters: { orderBy: [desc(chapters.number)] },
        genres: true,
      },
    }); // Returns Comic | null
  }
}

export const comicDal = new ComicDAL();
```

### Server Action Pattern

```typescript
"use server";
import { z } from "zod";
import { auth } from "@/lib/auth";

const Schema = z.object({ /* ... */ });

export async function action(input: unknown): Promise<ActionResult<Data>> {
  const session = await auth();
  if (!session?.user) return { ok: false, error: "Unauthorized" };

  const parsed = Schema.safeParse(input);
  if (!parsed.success) return { ok: false, error: parsed.error.message };

  try {
    const data = await db.insert(/* ... */).returning();
    return { ok: true, data };
  } catch (e) {
    return { ok: false, error: "Operation failed" };
  }
}
```

## Adding a New Feature

1. **Schema** — Add table to `src/database/schema/`
2. **DAL** — Create `src/dal/entity-dal.ts`
3. **Schema Validation** — Add Zod schema in `src/schemas/`
4. **Actions** — Create `src/actions/entity.actions.ts`
5. **Components** — Create UI in `src/components/`
6. **Route** — Add page under `src/app/`
7. **Tests** — Write unit and E2E tests

## Scripts

| Command | Purpose |
|---------|---------|
| `pnpm scaffold:component` | Scaffold new component |
| `pnpm scaffold:action` | Scaffold new server action |
| `pnpm scaffold:hook` | Scaffold new hook |
| `pnpm format` | Format all code |
| `pnpm triage` | Quality gate analysis |
| `pnpm health:all` | Full project health check |
| `pnpm optimize:performance` | Performance analysis |
| `pnpm docs:generate` | Generate documentation |

## State Management

- **Client State**: Zustand stores (7 stores: reader, UI, preferences, etc.)
- **Server State**: TanStack React Query with revalidation
- **Auth State**: NextAuth `useSession()` hook

## Testing

```bash
pnpm test             # Unit tests (Vitest)
pnpm test:ui          # E2E tests (Playwright)
pnpm test:ui:codegen  # Interactive test recorder
```
