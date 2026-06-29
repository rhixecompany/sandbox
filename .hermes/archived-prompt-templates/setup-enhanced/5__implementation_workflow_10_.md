# 5. 📋 Implementation Workflow (10 Steps)

> Extracted from `setup-enhanced.prompt.md` for DRY templating.

## 5. 📋 Implementation Workflow (10 Steps)

Follow these steps for every new feature. Each step references the relevant documentation section.

### Step 1: Search & Document

Find existing patterns before writing any code:

```bash
grep -r "class.*Dal extends BaseDal" src/dal/     # Similar DAL classes
grep -r "ActionResult" src/actions/                # Similar actions
ls src/schemas/                                     # Existing Zod schemas
```

Document findings before proposing implementation. Check `docs/database-context-map.md` for entity relationships.

### Step 2: Design Database

Plan schema additions following existing table patterns. See `docs/dev.content.md` Section 3 for schema design rules.

**Non-negotiable rules:**

- Serial `id` primary key (or composite PK for junction tables)
- `createdAt` and `updatedAt` timestamps on every table
- Foreign keys use `onDelete: "cascade"`
- Enum fields use `pgEnum()`
- Indexes on frequently queried columns

### Step 3: Implement Database

```bash
# Add table to src/database/schema.ts
# Then apply to database:
pnpm db:push
pnpm type-check
```

### Step 4: Implement DAL

Create a new DAL class extending `BaseDal<T>`. See `docs/dev.content.md` Section 7 for the complete DAL pattern.

**Location:** `src/dal/{entity}-dal.ts`

Key requirements:

- Use `.with()` for eager loading (prevent N+1 queries)
- Filter soft-deleted records (`WHERE deletedAt IS NULL`)
- Export a singleton instance

### Step 5: Create Validation Schemas

Define Zod schemas for create/update operations. See `docs/dev.content.md` Section 8 for schema patterns.

**Location:** `src/schemas/{entity}.schema.ts`

Key requirements:

- Strings always have `.min()` and `.max()`
- Enums validate against `pgEnum` values
- Complex logic uses `.refine()` or `.superRefine()`

### Step 6: Implement Server Actions

Create actions following the `ActionResult<T>` pattern. See `docs/dev.content.md` Section 9.

**Location:** `src/actions/{entity}.actions.ts`

Key requirements:

- `"use server"` directive at top
- `await auth()` as first call in protected actions
- Zod validation before any DB operation
- `revalidatePath()` after mutations
- Never throw — always return `ActionResult<T>`

### Step 7: Build Components

Compose UI from shadcn primitives and existing components. See `docs/dev.content.md` Section 12.

Key requirements:

- Server Components by default
- `"use client"` only for interactivity (forms, state, event handlers)
- React Compiler is ON — never use `useMemo`/`useCallback`/`memo()`
- Loading skeletons for async data

### Step 8: Create Page

Set up the route with proper metadata. See `docs/dev.content.md` Section 11.

**Location:** `src/app/(root)/{feature}/page.tsx`

Key requirements:

- `params` and `searchParams` are `Promise` — always `await`
- Use `<Suspense>` boundaries for streaming
- Export `generateMetadata()` for SEO
- Never use `export const dynamic = "force-dynamic"`

### Step 9: Test & Validate

```bash
pnpm type-check          # Zero TypeScript errors
pnpm lint:fix            # Auto-fix linting issues
pnpm test                # All unit tests pass
pnpm build               # Production build succeeds
```

### Step 10: Code Review Checklist

| Check         | Requirement                                    |
| ------------- | ---------------------------------------------- |
| Type Safety   | No `any` types, proper generics                |
| N+1 Queries   | Uses `.with()` or single JOIN                  |
| Auth          | `auth()` is first call in protected actions    |
| Validation    | Zod schemas on all external input              |
| Cascades      | FK columns have `onDelete: "cascade"`          |
| Indexes       | WHERE/JOIN columns are indexed                 |
| Tailwind v4   | `bg-linear-to-br`, `aspect-2/3`, `h-4!` syntax |
| Accessibility | ARIA labels, semantic HTML                     |

---
