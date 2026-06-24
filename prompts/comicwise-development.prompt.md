---
license: MIT
author: Hermes Agent
version: 1.0.0
name: comicwise-development
title: "ComicWise Development Workflow"
description: "Reusable prompt for ComicWise development sessions"
applyTo: "**/*"
tags: []
  - nextjs
  - typescript
  - drizzle
  - react19
  - development
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

> ├── app/                     # Next.js App Router pages
> │   ├── (auth)/             # Public auth pages (/sign-in, /sign-up)

> **Full content:** `templates/comicwise-development/project_structure.md`

## Coding Rules (Enforced)

> ### Type Safety & Code Quality
> 1. **No `any` types** — ESLint: `no-explicit-any: "error"`

> **Full content:** `templates/comicwise-development/coding_rules_enforced.md`

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

> ### DAL Query Pattern (with Eager Loading)
> import { BaseDal } from "./base-dal";

> **Full content:** `templates/comicwise-development/common_patterns.md`

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

> ### Unit Tests (Vitest)
> import { describe, it, expect, beforeEach } from "vitest";

> **Full content:** `templates/comicwise-development/testing_patterns.md`

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


## Template References

Detailed templates in `templates/comicwise-development/`:
- `coding_rules_enforced.md`
- `common_patterns.md`
- `project_structure.md`
- `testing_patterns.md`
