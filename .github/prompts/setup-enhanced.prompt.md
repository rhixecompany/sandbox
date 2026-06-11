---
description: "Enhanced ComicWise AI agent setup — workflow, implementation strategy, and DRY practices"
agent: "Next.js Expert"
model: "Claude Haiku 4.5 (copilot)"
---

# ComicWise — AI Agent Setup & Implementation Guide

**ComicWise** is a production-grade manga/comic reader built with **Next.js 16.1.6** (App Router), **React 19** Server Components, **Drizzle ORM** + PostgreSQL (Neon), **NextAuth v5** (database sessions), **Zustand 5** + **React Query 5**, **shadcn/Radix UI**, **Tailwind CSS 4**, **Vitest** + **Playwright**, and a database seeding system with CLI + REST API.

This guide covers **HOW** to implement features — workflow, phases, DRY practices, and personas. It does not duplicate content from the reference files below.

> **📖 Cross-References:** Rules & conventions → `.github/copilot-instructions.md` | Complete patterns & code → `docs/dev.content.md` | Entity details → `docs/database-context-map.md`

---

## 1. 🚀 Quick Start

```bash
pnpm install                              # Install dependencies
cp .env.local.example .env.local          # Configure DATABASE_URL, AUTH_SECRET
pnpm db:push                              # Apply schema to database
pnpm type-check                           # Verify zero TypeScript errors
pnpm dev                                  # Start dev server (port 3000)
```

---

## 2. ✅ Quality Gate (Before Every PR)

```bash
pnpm type-check          # 0 TypeScript errors required
pnpm lint:fix            # ESLint + Prettier auto-fix
pnpm test                # Vitest unit tests (jsdom)
pnpm build               # Production build validation
```

All four commands must pass before merging any code.

---

## 3. 📚 Reference Resolution Hierarchy

When implementing features, consult these sources in priority order:

### Tier 1 — Latest Standards (Primary)

| Source | Purpose |
| --- | --- |
| `.github/copilot-instructions.md` | Current architectural standards and coding rules |
| `.github/instructions/*.md` | File-pattern-specific guidelines (TypeScript, Next.js, security, testing, performance) |

### Tier 2 — Entity & Schema Details

| Source | Purpose |
| --- | --- |
| `docs/database-context-map.md` | Entity relationships, constraints, cascade behavior |
| `src/database/schema.ts` | Table definitions, enums, indexes (30+ tables) |

### Tier 3 — Concrete Implementations

| Source | Purpose |
| --- | --- |
| `src/dal/*.ts` | Data Access Layer patterns (`BaseDal<T>`, eager loading) |
| `src/actions/*.ts` | Server Actions with `ActionResult<T>` pattern |
| `src/schemas/*.ts` | Zod validation schemas per domain |
| `src/components/**/*.tsx` | UI components with proper typing |
| `src/app/**/*.tsx` | Page implementations and route structure |

### Context Resolution Rules

1. **Primary Source:** Use patterns from `.github/copilot-instructions.md` (latest approved patterns)
2. **Validation:** Cross-reference with `docs/database-context-map.md` for entity details
3. **Examples:** Find matching patterns in `src/` for concrete implementation
4. **Configuration:** Reference `docs/*` for project-specific settings and conventions
5. **Conflict:** `.github/copilot-instructions.md` is always the source of truth

### DRY Composition Rules

1. **Reuse DAL Patterns** — Extend `BaseDal<T>` from `src/dal/base-dal.ts`, never create new base classes
2. **Common Actions** — Leverage existing `ActionResult<T>` pattern from `src/actions/types.ts`
3. **Schema Validation** — Use established Zod patterns from `src/schemas/` directory
4. **Component Composition** — Build from existing `ui/` components and shadcn primitives
5. **Type Safety** — Extract types with `z.infer<typeof schema>`, never duplicate type definitions

### Merge Strategy

```
❌ WRONG: Duplicating DAL logic in a new class
✅ CORRECT: class NewDal extends BaseDal<T> { /* only new logic */ }
```

When existing code matches your need:

- **Exact Match** → Use as-is, adjust imports
- **Partial Match** → Extract pattern core, adapt schema/types for new entity
- **No Match** → Create new implementation following adjacent code patterns
- **Conflict** → `.github/copilot-instructions.md` wins

### File Reference Lookup

| Need | Search Location | Reference Example |
| --- | --- | --- |
| DAL Pattern | `src/dal/*.ts` | `comic-dal.ts` for eager loading |
| Server Action | `src/actions/*.ts` | `comic.actions.ts` for `ActionResult<T>` |
| Zod Schema | `src/schemas/*.ts` | `comic-schema.ts` for validation |
| UI Component | `src/components/` | Extend from shadcn primitives |
| Page Layout | `src/app/(root)/` | Mirror existing page structure |
| Type Definition | `src/types/` | Use `z.infer<typeof schema>` |

---

## 4. 🔧 DRY Implementation Practices

Every piece of logic should exist in exactly one place. When implementing features, leverage existing abstractions and extend rather than duplicate.

### Strategy 1: DAL Classes — Parameterized Query Methods

Instead of creating separate methods for each query variation, use a single parameterized method with filter options. See `docs/dev.content.md` Section 7 for the complete `BaseDal<T>` pattern and examples.

```
❌ Separate methods: getByType(), getByStatus(), getByRating()
✅ Single method: listWithFilters(filters: QueryFilters)
```

### Strategy 2: Server Actions — Standardized `ActionResult<T>`

All server actions follow the same structure: `auth → validate → DAL → revalidate → result`. See `docs/dev.content.md` Section 9 for the complete pattern with error handling.

```
type ActionResult<T> = { ok: true; data: T } | { ok: false; error: string }
```

### Strategy 3: Zod Schemas — Extract & Reuse Common Validations

Share field-level validations across create/update schemas. See `docs/dev.content.md` Section 8 for Zod schema composition patterns.

```
❌ Duplicating: z.string().min(1).max(255) in both create and update schemas
✅ Extracting: const titleSchema = z.string().min(1).max(255), then reuse
```

### Strategy 4: React Components — Compose from Primitives

Build page-level components by composing shadcn/ui primitives and existing domain components. See `docs/dev.content.md` Section 12 for component composition patterns.

### Cross-Cutting Concerns (Single Source of Truth)

| Concern | Single Source | Usage Pattern |
| --- | --- | --- |
| **Types** | `z.infer<typeof schema>` | Import from schema only, never redefine |
| **Validation** | Zod schema in `src/schemas/` | Single import, reuse everywhere |
| **DB Access** | Specific DAL class | Never raw `db` queries in actions/pages |
| **Error Handling** | `ActionResult<T>` pattern | Same structure for all actions |
| **Timestamps** | Drizzle `.$onUpdate()` | Auto-updates `updatedAt` column |
| **Auth Checks** | `await auth()` helper | First call in every protected action |
| **Cache Invalidation** | `revalidatePath()` | After every mutation |

### Reference-Driven Development Workflow

1. **Search** — Find existing patterns: `grep -r "extends BaseDal" src/dal/`
2. **Understand** — Read the base class, extract only what your entity needs
3. **Compose** — Extend base classes, import types from schemas, build UI from primitives
4. **Validate** — `pnpm type-check && pnpm lint:fix && pnpm test`

---

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

## 6. 🏗️ Feature Implementation Phases

### Phase Overview

| Phase | Focus | Prerequisites |
| --- | --- | --- |
| 1 | Foundation | Database, DAL, validation infrastructure |
| 2 | User Profile | Auth flow complete |
| 3 | Comics | Phase 1 complete |
| 4 | Chapter Reader | Phase 3 complete |
| 5 | Bookmarks Management | Phase 3 complete |
| 6+ | Advanced Features | Phases 1-5 complete |

---

### Phase 1: Foundation

Infrastructure setup — database schema, base DAL, core validation, auth flow.

**Checklist:**

- [ ] `pnpm install` — dependencies installed
- [ ] `.env.local` — configured with `DATABASE_URL`, `AUTH_SECRET`
- [ ] `pnpm db:push` — schema applied
- [ ] `pnpm type-check` — zero errors
- [ ] `pnpm dev` — server starts on port 3000

---

### Phase 2: User Profile Features

| Task | File | Key Features |
| --- | --- | --- |
| 2.1 Profile View | `src/app/(root)/profile/page.tsx` | Avatar, stats, recent activity, quick actions |
| 2.2 Profile Edit | `src/app/(root)/profile/edit/page.tsx` | Edit form, avatar upload, Zod validation |
| 2.3 Change Password | `src/app/(root)/profile/change-password/page.tsx` | Password validation, strength indicator |
| 2.4 Settings | `src/app/(root)/profile/settings/page.tsx` | Notifications, privacy, theme, danger zone |

**Components:** `ProfileView`, `ProfileStats`, `RecentActivity` **Schema:** `ProfileUpdateSchema`, `ChangePasswordSchema` in `src/schemas/profile.schema.ts` **Actions:** `updateProfileAction`, `changePasswordAction` in `src/actions/profile.actions.ts`

---

### Phase 3: Comic Features

#### Task 3.1: Comics Listing

**File:** `src/app/(root)/comics/page.tsx`

| Feature    | Details                                  |
| ---------- | ---------------------------------------- |
| Layout     | Responsive grid (2/3/4 cols by viewport) |
| Cards      | Lazy-loaded images, metadata badges      |
| Filtering  | Genre, type, status sidebar              |
| Sorting    | Latest, popular, rating                  |
| Search     | Text search with debounce                |
| Pagination | 20 per page                              |

**Components:** `ComicCard`, `ComicFilters`, `ComicSearch`, `ComicPagination`

#### Task 3.2: Comic Details

**File:** `src/app/(root)/comics/[slug]/page.tsx`

| Feature  | Details                           |
| -------- | --------------------------------- |
| Header   | Cover image, title, author/artist |
| Metadata | Rating, status badges, genre tags |
| Content  | Truncated description, statistics |
| Actions  | Bookmark toggle, chapter list     |
| Related  | Recommendations section           |

**Components:** `ComicHeader`, `ComicDescription`, `ComicStats`, `BookmarkActions`, `ChapterList`, `RelatedComics`

#### Task 3.3: Bookmark Components

**Files:** `src/components/comics/AddToBookmarkButton.tsx`, `RemoveFromBookmarkButton.tsx`, `BookmarkStatus.tsx` **Actions:** `addToBookmarksAction`, `removeFromBookmarksAction`, `updateBookmarkStatusAction`

Features: Optimistic UI, status dropdown (Reading, Plan to Read, Completed, On Hold, Dropped), toast notifications.

---

### Phase 4: Chapter Reader

**File:** `src/app/(root)/comics/[slug]/[chapterNumber]/page.tsx`

| Feature | Details |
| --- | --- |
| Reading Modes | Vertical scroll (default), horizontal page |
| Controls | Zoom, fit-to-width/height, fullscreen |
| Navigation | Prev/next chapter, chapter dropdown, keyboard (arrows, space, esc), touch swipe |
| Progress | Automatic reading progress tracking |
| Settings | Background color (white/dark/sepia), image quality, zoom slider |

**Components:** `ChapterReader`, `ImageViewer`, `ChapterNavigation`, `ReadingSettings`, `ReadingProgress`

---

### Phase 5: Bookmarks Management

**File:** `src/app/(root)/bookmarks/page.tsx`

| Feature     | Details                               |
| ----------- | ------------------------------------- |
| Views       | Grid/list toggle                      |
| Cards       | Progress indicator, last read chapter |
| Filtering   | By status (Reading, Completed, etc.)  |
| Sorting     | Date, title, progress                 |
| Search      | Search within bookmarks               |
| Empty State | Helpful empty state with CTA          |

**Components:** `BookmarkCard`, `BookmarkFilters`, `BookmarkSearch`, `BookmarkViewToggle`

---

### Phase 6+: Advanced Features

- Comment discussions on chapters
- User ratings and reviews
- Reading notifications
- User recommendations
- Social features (following, sharing)
- Admin management panel with RBAC
- Full-text search
- Image optimization pipeline

---

## 7. 🔗 Content Integration Rules (DRY Enforcement)

### When Adding Documentation

- ✅ Link to relevant sections in existing docs rather than duplicating content
- ✅ Reference specific code in `src/` with file paths
- ✅ Add new patterns to `.github/instructions/` only if they don't already exist
- ✅ Update `docs/database-context-map.md` when schema changes

### When Finding Reference Code

- ✅ Copy implementation **patterns**, not full files — adapt for your entity
- ✅ Always extend `BaseDal<T>` rather than creating a new base class
- ✅ Use same `ActionResult<T>` structure for all server actions
- ✅ Import types: `type CreateInput = z.infer<typeof CreateSchema>`

### When Writing New Code

- ✅ If similar code exists elsewhere, ask why — it might be a DRY violation
- ✅ Extract common logic to utilities/DAL/actions before shipping
- ✅ Use file paths in comments to reference context when helpful
- ✅ Document in `docs/` why a new pattern was created if it diverges from existing ones

### Time-Saving Tips

1. **Copy-Paste Strategy:** Copying existing code is faster than reading docs when you need an exact pattern match — just adapt entity names and imports
2. **Two-Document Reading:** Read `.github/copilot-instructions.md` (WHY) alongside `src/` code (HOW)
3. **Grep for Patterns:**
   ```bash
   grep -r "ActionResult" src/actions/        # Find all actions
   grep -r "extends BaseDal" src/dal/         # Find all DAL classes
   grep -r "safeParse" src/actions/           # Find validation usage
   ```

---

## 8. 🧭 How to Use This Guide

### For New Features

1. Identify which **Phase** (Section 6) your feature belongs to
2. Follow the **Implementation Workflow** (Section 5) step by step
3. Apply **DRY Practices** (Section 4) throughout
4. Run the **Quality Gate** (Section 2) before submitting

### For Bug Fixes

1. Check the **Reference Resolution Hierarchy** (Section 3) to find relevant code
2. Apply the correct pattern from the appropriate reference file
3. Run `pnpm type-check && pnpm lint:fix && pnpm test` to validate

### For Questions

1. Check the **Reference Resolution Hierarchy** (Section 3) for the right source file
2. Consult `docs/dev.content.md` for expanded technical details
3. Look at existing implementations in `src/` for concrete examples
4. Check git history for similar patterns

---

## 9. 🎭 AI Personas for Copilot CLI

Use these personas when running tasks in Copilot CLI to get specialized behavior:

### Architect Persona

```
You are a senior software architect for ComicWise. Focus on:
- System design decisions and tradeoffs
- Data flow optimization (Server → DAL → Client)
- Database schema design with proper indexes and composite keys
- Scalability patterns (batch processing, caching, lazy loading)
Reference: docs/dev.content.md sections 3, 6, 22, 24
```

### Implementer Persona

```
You are a senior full-stack developer implementing ComicWise features. Follow:
- Server Components by default, "use client" only for interactivity
- DAL pattern for ALL reads (BaseDal<T>, .with() for eager loading)
- Server Actions for ALL mutations (auth → validate → DAL → revalidate)
- React Compiler is ON — never use useMemo/useCallback/memo()
- searchParams and params are Promise types — always await
Reference: docs/dev.content.md sections 7-9, 14, 23
```

### Reviewer Persona

```
You are a code reviewer for ComicWise PRs. Check:
- Type safety (no `any`, use unknown + type guards for external data)
- N+1 queries (must use .with() or single JOIN, never loop+query)
- Auth in Server Actions (auth() must be first call)
- Tailwind v4 syntax (bg-linear-to-br, aspect-2/3)
- Zero TypeScript errors (pnpm type-check)
Reference: docs/dev.content.md sections 14, 17, 18, 25
```

### Debugger Persona

```
You are debugging a ComicWise issue. Process:
1. Reproduce with minimal test case
2. Check console + Next.js MCP for runtime errors
3. Verify auth state (auth() in Server Components)
4. Check DAL queries (Drizzle Studio: pnpm db:studio)
5. Verify env variables (Zod validation in src/lib/env.ts)
Reference: docs/dev.content.md sections 5, 20, 25
```

---

## 10. 🔄 Anti-Rate-Limiting Strategy

When using this prompt with Copilot CLI, follow these practices to avoid token exhaustion:

### Chunked Execution

1. **Never paste full documentation files into a prompt** — reference by path
2. **Work in focused phases** — one feature/section at a time
3. **Use section numbers** — "Implement pattern from Section 23.2" instead of quoting code
4. **Batch related changes** — edit multiple files in one turn, not sequential turns

### Efficient Prompting

```bash
# ✅ Good: Reference by section
"Add reading progress tracking using the idempotent upsert pattern from docs/dev.content.md Section 23.2"

# ❌ Bad: Paste entire code blocks into prompt
"Here's the full schema... [500 lines] ... now implement this"

# ✅ Good: Focused task with persona
"As Implementer, add a DAL method for comic search following docs/dev.content.md Section 22.4"

# ❌ Bad: Open-ended request
"Implement all features for the entire application"
```

### Session Management

- **Start fresh sessions** for each phase (Foundation → Features → QA → Deploy)
- **Commit between phases** to save state and reduce context window
- **Use `pnpm type-check` after each batch** to catch issues early
- **Keep prompts under 500 words** — reference docs instead of quoting

---

## 11. 📋 Phase Execution Checklists

### Phase 1: Foundation

- [ ] `pnpm install` — dependencies installed
- [ ] `.env.local` — configured with `DATABASE_URL`, `AUTH_SECRET`
- [ ] `pnpm db:push` — schema applied
- [ ] `pnpm type-check` — zero errors
- [ ] `pnpm dev` — server starts on port 3000

### Phase 2: Core Features

- [ ] Auth flow (sign-in, sign-up, sign-out, session)
- [ ] Comic CRUD (DAL + Server Actions + Pages)
- [ ] Chapter CRUD with image handling
- [ ] Reading progress tracking (see `docs/dev.content.md` Section 23.2)
- [ ] Bookmark management (composite key upsert)
- [ ] Rating system (see `docs/dev.content.md` Section 23.1)
- [ ] Comment system with threading

### Phase 3: Advanced Features

- [ ] Full-text search (see `docs/dev.content.md` Section 22.4)
- [ ] Admin dashboard with RBAC
- [ ] Notification system
- [ ] Image optimization pipeline
- [ ] Batch seeding (CLI + REST API)

### Phase 4: Quality & Polish

- [ ] Unit tests — Vitest (80%+ coverage)
- [ ] E2E tests — Playwright (critical paths)
- [ ] Performance audit (Core Web Vitals)
- [ ] Security review (auth, XSS, CSRF)
- [ ] Accessibility check (WCAG 2.1 AA)

### Phase 5: Deployment

- [ ] Production build: `pnpm build`
- [ ] Sentry integration (error tracking)
- [ ] CI/CD pipeline (GitHub Actions)
- [ ] Database backup strategy
- [ ] Monitoring & alerting

### Pre-Implementation Checklist (Every Feature)

- [ ] Feature requirements are clear and documented
- [ ] Database schema is designed and validated
- [ ] Cascade delete implications understood
- [ ] N+1 query risks identified and mitigated
- [ ] Similar patterns found in codebase
- [ ] Task broken down into manageable pieces

---

## 12. 📖 Full Reference Files

| File | Purpose |
| --- | --- |
| `docs/dev.content.md` | Complete developer reference (25 sections) — patterns, code examples, architecture |
| `docs/database-context-map.md` | Entity relationship details, constraints, cascade behavior |
| `.github/copilot-instructions.md` | Quick-reference coding rules and conventions |
| `.github/instructions/` | File-pattern coding standards (TypeScript, Next.js, security, testing, performance) |
| `src/database/schema.ts` | All 30+ Drizzle tables, enums, relations |
| `src/dal/base-dal.ts` | Abstract `BaseDal<T>` base class |
| `src/actions/types.ts` | `ActionResult<T>` type definition |
| `src/lib/env.ts` | Zod-validated environment variables |

---

**Last Updated:** March 2026
