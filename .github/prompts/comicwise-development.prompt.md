---
name: comicwise-development
title: ComicWise Development Workflow
description: Reusable prompt for ComicWise development sessions.
version: 1.0.0
license: MIT
author: Hermes Agent
toolsets:
  - file
  - terminal
  - web
scripts: []
skills: []
formatter: default
plan: 'None'
tags:
  - architecture
  - audit
  - nextjs
  - prompts
  - testing
  - typescript
  - workflow
trigger: /comicwise-development
applyTo: '**/*'
dependencies: []
metadata:
  hermes: {}
---

## Goal

Reusable prompt for ComicWise development sessions.

# ComicWise Development Prompt**Version**: 1.0 **Last Updated**: March 13, 2026 **Quality Score**: 98/100 **Production Ready**: ✅ Yes

## Project State Summary

**ComicWise** is a production-ready Next.js 16.1.6 manga/comic reader with:- ✅ Phase 4.3 (Reading Analytics) complete- ✅ Batch 4 (Code Audit & Standardization) complete- ✅ 241/241 tests passing (zero regressions)- ✅ 0 TypeScript errors enforced- ✅ 100% dark mode coverage- ✅ WCAG 2.1 AA accessibility- ✅ 98/100 architecture quality score

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
# 1. Install & setuppnpm installcp .env.local.example .env.local    # Edit with your DATABASE_URL, AUTH_SECRETpnpm db:push# 2. Start developmentpnpm dev                            # Port 3000, Turbopack# 3. Run quality gatespnpm validate                       # Runs: type-check, lint:fix, test, health checks
```

## Essential Commands

| Command           | Purpose                         | Must Pass   || ----------------

- | ------------------------------- | ----------- || `pnpm dev`        | Start dev server (Turbopack)    | —           || `pnpm type-check` | TypeScript validation           | ✅ 0 errors || `pnpm lint:fix`   | ESLint + Prettier auto-fix      | ✅ All pass || `pnpm test`       | Vitest unit tests (jsdom)       | ✅ 241/241  || `pnpm build`      | Production build (Webpack)      | ✅ Success  || `pnpm validate`   | All quality gates at once       | ✅ All pass || `pnpm db:push`    | Apply schema changes (dev only) | —           || `pnpm db:studio`  | Drizzle visual browser          | —           || `pnpm seed:all`   | Populate database               | —           |

## Data Flow Architecture

```HTTP
 Request    ↓Next.js Middleware (src/proxy.ts)  • Auth check (await auth())  • Route protection (/profile, /bookmarks, /ratings, /admin)    ↓Server Component (App Router page)  • Await async params/searchParams (v16 breaking change)  • Call DAL methods for data    ↓DAL Layer (src/dal/*-dal.ts)  • All queries use Drizzle with eager loading (.with())  • Never use raw SQL or loop queries (no N+1)  • Return properly typed results ($inferSelect)    ↓Client Component / Zustand / React Query  • Use props data from Server Component  • Zustand for UI state (reader mode, sidebar toggle)  • React Query for dynamic server state    ↓Server Actions (src/actions/*-actions.ts)  • Mutations: auth → validate → mutate → revalidate  • Never throw: return ActionResult<T

> (ok + data/error)    ↓HTTP Response
```

## Project Structure

> ├── app/                     # Next.js App Router pages
> │   ├── (auth)/             # Public auth pages (/sign-in, /sign-up)
> **Full content:**

## Coding Rules (Enforced)

### Type Safety & Code Quality

> 1. **No `any` types** — ESLint: `no-explicit-any: "error"`

## Path Aliases (tsconfig.json)

```typescript
@/*        → ./src/*ui         → ./src/components/ui/*database   → ./src/database/*schemas    → ./src/schemas/*env        → ./src/lib/env.tshooks      → ./src/hooks/*appConfig  → ./appConfig.tslib        → ./src/lib/*types      → ./src/types/*components → ./src/components/*utils      → ./src/lib/utils.tsassets     → ./src/assets/*styles     → ./src/styles/*tests      → ./src/tests/*
```

## Common Patterns

### DAL Query Pattern (with Eager Loading)

> import { BaseDal } from "./base-dal";

## Database Schema Facts

- **`comic.rating`** = `decimal(10,1)` — aggregate with `AVG(rating)`. The `rating.rating` column = `integer` (1–5 stars)- **`comicStatus` enum**: "Ongoing", "Hiatus", "Completed", "Dropped", "Season End", "Coming Soon"- **`user.id`** = `text` (UUID string), not integer- **`bookmark`** = composite PK on `(userId, comicId)` → use `onConflictDoUpdate` for upserts- **`bookmark.status`** = `text` field (default "Reading"), not pgEnum- **4 enums total**: `userRole`, `comicStatus`, `resourceEnum`, `actionEnum`- **Soft deletes**: Only `user` and `comment` tables have `deletedAt` → filter on those tables only- **Cascade deletes**: Most FKs have `{ onDelete: "cascade" }`. Exceptions: `comic.authorId/artistId/typeId`, `bookmark.lastReadChapterId` (no cascade); `auditLog.userId` (`set null`)

## Test

ing Patterns>

### Unit Tests (Vitest)

> import { describe, it, expect, beforeEach } from "vitest";

## Quality Gate (Must Pass Before Commits)

```bash
# Run all quality gates at oncepnpm validate# Or run individuallypnpm type-check     # Must be 0 errors (blocks deployment)pnpm lint:fix       # Auto-fix and validatepnpm test           # Must pass 241/241 (no regressions)pnpm build          # Must succeed (production build)
```

## Environment Variables

**Required** (in `.env.local`):

```DATABASE_URL=postgresql://user:password@host:port/databaseAUTH_SECRET=openssl rand -hex 32```**Optional** (see `.env.local.example` for full list):

- `AUTH_GITHUB_ID`, `AUTH_GITHUB_SECRET`- `AUTH_KEYCLOAK_URL`, etc.
- `NEXTAUTH_URL` (override default)All validated via `src/lib/env.ts` at startup using Zod.

## Reference Documentation

| File | Purpose | Scope || --

- | --- | --- || `.github/copilot-instructions.md` | Complete guide (2500+ lines) | Global || `prompts/comicwise-session.prompt.md` | Quick reference (400 lines) | Session shortcuts || `.github/instructions/*.md` | Auto-loaded by file pattern (15+ files) | Specific file types || `docs/dev.content.md` | 26 sections with patterns & examples | Development reference || `docs/MASTER_PHASE_PLAN_4-6.md` | Phase planning & task tracking | Project roadmap || `AGENTS.md` | This project's quick setup guide | Quick start |

## Common Troubleshooting

| Issue | Solution || --- | --- || Type errors (TS2307) | Check import path aliases in `tsconfig.json` || N+1 query errors | Add `.with({ relations: true })` to DAL queries || Action throws instead of returns | Wrap in try-catch, return `ActionResult<T

> `|| Styling not applying | Check Tailwind v4 syntax (`bg-linear-to-br` not `bg-gradient-to-br`) || DB connection fails | Verify`DATABASE_URL` and run `pnpm db:studio` to test || Tests fail in CI but pass locally | Check mocks in `src/tests/setup-env.ts` || Hydration mismatch | Use `useCurrentYear()` hook not `new Date()` in server code |

## When Stuck

1. **Architecture questions** — Check `.github/copilot-instructions.md` (2500+ lines) or ask about system design2. **Component issues** — Reference `.github/instructions/design-system.instructions.md`3. **Database/ORM** — Review DAL examples (eager loading with `.with()`)4. **Type errors** — Use `getEnv()` not `process.env`, import types with `import type`5. **Tests failing** — Check mocks in `src/tests/setup-env.ts`6. **Performance** — Reference `.github/instructions/performance-optimization.instructions.md`

## Development Workflow

1. **Start session**: `pnpm install && pnpm db:push && pnpm dev`2. **Make changes**: Follow patterns above, run `pnpm validate` frequently3. **Commit**: Ensure `pnpm validate` passes (0 errors, 241/241 tests)4. **Deploy**: Run `pnpm build` for production readiness5. **Debug**: Use `pnpm test --watch` or `pnpm test:ui --debug` for debugging

## Next Phase

**Phase 4.4 (Social Features)**: Reviews, ratings, sharing

- **Estimated Duration**: 4-5 days- **Dependencies**: ✅ Phase 4.3 complete, all gates passing- **Success Criteria**: 0 type errors, 250+ passing tests, production build**Future Phases**:- **Phase 4.5** — Mobile optimization & PWA- **Phase 6** — Advanced features---**Last Updated**: March 13, 2026 **Quality Score**: 98/100 **Production Status**: ✅ Ready **Support**: See docs/ and .github/instructions/ for detailed guides

## Template References

Detailed templates in `templates/comicwise-development/`:- `coding_rules_enforced.md`- `common_patterns.md`- `project_structure.md`- `testing_patterns.md`

## Personas

See [`templates/_shared/personas.md`](templates/_shared/personas.md) for shared persona templates.

| Persona | When to Use |
|| ------- | ----------- ||
| **Developer** | Implementation, debugging, refactoring |
| **Reviewer** | Code review, quality assurance |
| **User** | General purpose, operations |

## Personality

See [`templates/_shared/personality.md`](templates/_shared/personality.md) for shared personality guidelines.

- **Tone**: Direct, practical, actionable
- **Style**: Structured with clear steps and verification
- **Avoid**: Ambiguity, assumptions, scope creep
- **Encourage**: Evidence-based decisions, minimal changes

## Context

Use when fixing, repairing, or synchronizing files or configs. Diagnose first, apply minimal changes, verify each fix.

## Rules

See core rules: [`templates/_shared/rules-core.md`](templates/_shared/rules-core.md)

### Domain Rules

- Fix root causes, not symptoms.
- Check siblings for the same flaw.
- Restore from git clean before retrying.

### Standing Rules

1. **Map before touch** — Understand before making changes.
2. **Smallest safe change** — Minimal change that achieves the goal.
3. **Verify before claim** — Test before reporting complete.
4. **Report blockers** — State clearly when something fails.

## Phases

### Phase 1: Intake

- Read the request and identify scope.
- Locate relevant files, diffs, references.

### Phase 2: Execute

- Perform work with smallest safe change set.
- Keep steps explicit and reproducible.

### Phase 3: Verify

- Check result against goal, rules, inputs.
- Confirm output is usable and complete.

### Phase 4: Hand Off

- Return final artifact or findings clearly.
- Stop once the requested result is delivered.

## Best Practices

See [`templates/_shared/best-practices.md`](templates/_shared/best-practices.md) for cross-cutting best practices.

1. **DRY** — Reference shared templates instead of duplicating content.
2. **Structured output** — Use clear sections with consistent heading levels.
3. **Verification gates** — Always verify before claiming completion.
4. **Minimal changes** — Fix root cause, not symptoms.

## Verification Checklist

| # | Gate | Criterion |
|| --- | ------ | ----------- ||
| 1 | Scope | Change matches the original request |
| 2 | Quality | Meets project standards |
| 3 | Tests | Tests pass (if applicable) |
| 4 | Regression | No unintended side effects |
| 5 | Docs | Changes documented if needed |

## Dependencies

See [`templates/_shared/deps-core.md`](templates/_shared/deps-core.md) for shared dependency patterns.

## Subgoals

1. **Prepare** — Understand requirements and prerequisites.
2. **Execute** — Follow structured workflow with incremental progress.
3. **Verify** — Confirm output meets requirements and standards.
4. **Document** — Record results, decisions, and lessons learned.

## Skills Required

See [`templates/_shared/skills-table-core.md`](templates/_shared/skills-table-core.md) for shared skills table.

| Skill | Purpose |
|| ------- | --------- ||
| `using-superpowers` | Foundational skill workflow |
| `systematic-debugging` | Root cause analysis and fix |
| `git-patch-management` | Patch creation and management |
| `executing-plans` | Execute plans step by step |
| `verification-before-completion` | Validate before claiming done |

## MCP Servers & Tools

The following MCP servers and tools are available for this task. Use them in preference to native equivalents per MCP-first tooling policy.

| `ast-grep` | AST-based code search and replace |
| `filesystem` | File read/write operations |
| `sequential-thinking` | Structured reasoning for complex problems |
| `fetch` | Web page content extraction |
| `playwright` | Browser automation for interactive pages |
| `github` | GitHub API operations |

## Tasks

- [ ] Understand requirements and scope
- [ ] Plan approach and identify resources
- [ ] Execute work incrementally
- [ ] Verify against acceptance criteria
- [ ] Document results and decisions
