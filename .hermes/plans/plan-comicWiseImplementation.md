---
title: "ComicWise Implementation Plan (Phases 3-11)"
category: "IMPL_PLAN"
source: "prompts/plan-comicWiseImplementation.prompt.md"
---

# ComicWise Implementation Plan

**Version:** 5.0.0 | **Date:** March 1, 2026 | **Scope:** Phases 3–11 (79 file operations)

---

## Decision Log

### Question 5.3: Coding Standards to Enforce

**Answer: D (All existing patterns)**

Enforced standards across entire codebase:

- ✅ **A)** Eager loading with `.with()` to prevent N+1 queries
- ✅ **B)** Composite PK usage for bookmarks (upserts with `onConflictDoUpdate`)
- ✅ **C)** `onDelete: "cascade"` on all FK references
- ✅ **D)** Zustand with `devtools(persist(...))`
- ✅ **E)** React Query singleton pattern
- ✅ **F)** All patterns from `.instructions.md` files (code-review, documentation, NextJS, performance, security, testing, TypeScript)

---

## Phase 1 Completion Summary

✅ **COMPLETED** — All TypeScript & Auth fixes applied

| Task | Status | Files Changed |
| --- | --- | --- |
| DAL Base Class | ✅ | base-dal.ts |
| Comic DAL | ✅ | comic-dal.ts |
| Other DAL Files | ✅ | bookmark-dal.ts, chapter-dal.ts, rating-dal.ts, comment-dal.ts |
| Auth System | ✅ | auth-config.ts (signIn & redirect bugs fixed) |
| Chart Component | ✅ | components/ui/chart.tsx |
| Action Files | ✅ | bookmark.actions.ts, comic.actions.ts, rating.actions.ts |
| Schema Fixes | ✅ | rating-schema.ts (score → rating), ratings/page.tsx |

**Result:** Phase 1 TypeScript fixes complete. Remaining type errors are architectural (DAL inheritance pattern).

---

## Phase 2 Progress

✅ **Setup Documentation Created**

| Item | Status | Location |
| --- | --- | --- |
| Environment template | ✅ | `.env.local.example` |
| Database setup guide | ✅ | `docs/DATABASE_SETUP.md` |
| Dev setup scripts | ✅ | `scripts/setup-dev.sh`, `scripts/setup-dev.ps1` |
| Setup checklist | ✅ | `docs/DEV_SETUP_CHECKLIST.md` |

**Next:** Database connection validation (requires user env setup)

---

## Verified Codebase State

> - **Framework:** Next.js 16.1.6 App Router, Turbopack, React Compiler
> - **ORM:** Drizzle + PostgreSQL (Neon)

> **Full content:** `templates/plan-comicWiseImplementation/verified_codebase_state.md`

## Phase 3: TypeScript & Auth Fixes (9 edits — HARD GATE)

> > Run `pnpm type-check` after each fix. Must reach 0 errors before Phase 4.
> ### Fix 1 — `src/dal/bookmark-dal.ts`

> **Full content:** `templates/plan-comicWiseImplementation/phase_3_typescript__auth_fixes.md`

## Phase 4: Config Edits (5 edits)

> ### 4.1 — `next.config.ts`
> Add image domains, CDN/proxy support, security headers:

> **Full content:** `templates/plan-comicWiseImplementation/phase_4_config_edits_5_edits.md`

## Phase 5: Route Layouts (3 new files)

> ### 5.1 — `src/app/(root)/layout.tsx`
> import { auth } from "@/auth";

> **Full content:** `templates/plan-comicWiseImplementation/phase_5_route_layouts_3_new_fi.md`

## Phase 6: New DAL Files (9 new files)

> ### 6.1 — `src/dal/artist-dal.ts`
> import { db } from "@/database/db";

> **Full content:** `templates/plan-comicWiseImplementation/phase_6_new_dal_files_9_new_fi.md`

## Phase 7: New Action Files + Redis Cache (7 new files)

> ### 7.1 — `src/lib/cache/redis.ts`
> import { env } from "@/lib/env";

> **Full content:** `templates/plan-comicWiseImplementation/phase_7_new_action_files__redi.md`

## Phase 8: Utility Files (2 new files)

> ### 8.1 — `src/hooks/use-debounce.ts`
> import { useState, useEffect } from "react";

> **Full content:** `templates/plan-comicWiseImplementation/phase_8_utility_files_2_new_fi.md`

## Phase 9A: Zustand Stores (7 new files)

> > Directory: `src/stores/` — must be created. All stores use `devtools(persist(.
> ### Pattern for all stores:

> **Full content:** `templates/plan-comicWiseImplementation/phase_9a_zustand_stores_7_new_.md`

## Phase 9B: Components (14 new files + 1 root file)

> ### 9B.1 — `src/app/global-error.tsx`
> import { useEffect } from "react";

> **Full content:** `templates/plan-comicWiseImplementation/phase_9b_components_14_new_fil.md`

## Phase 10: Admin Pages (20 new files)

> ### Admin Route Structure
> ├── page.tsx                    (dashboard)

> **Full content:** `templates/plan-comicWiseImplementation/phase_10_admin_pages_20_new_fi.md`

## Phase 11: Testing (6 new files)

> ### 11.1 — `src/tests/setup-env.ts`
> import { vi } from "vitest";

> **Full content:** `templates/plan-comicWiseImplementation/phase_11_testing_6_new_files.md`

## Validation Gates

> pnpm type-check    # Must be 0 errors
> pnpm lint:fix      # Auto-fix

> **Full content:** `templates/plan-comicWiseImplementation/validation_gates.md`

## File Operation Summary

| Phase     | Operation                     | Count  |
| --------- | ----------------------------- | ------ |
| 3         | Edits (TypeScript/Auth fixes) | 9      |
| 4         | Edits (Config)                | 5      |
| 5         | New (Route Layouts)           | 3      |
| 6         | New (DAL files + barrel)      | 9      |
| 7         | New (Action files + Redis)    | 7      |
| 8         | New (Utilities)               | 2      |
| 9A        | New (Zustand stores)          | 7      |
| 9B        | New (Components)              | 8      |
| 10        | New (Admin pages)             | 8      |
| 11        | New (Tests)                   | 6      |
| **Total** |                               | **64** |

---

## Key Reminders

- **auth-config.ts signIn bug** is the single highest-priority fix — blocks all user authentication
- **rating column** is `rating` not `score` — affects all rating statistics queries
- **`$inferSelect`** is required on all BaseDal type parameters — not `typeof table`
- **`src/stores/`** must be created as a directory before store files
- **`src/lib/cache/`** must be created before redis.ts
- All admin pages require the `admin/layout.tsx` auth guard from Phase 5.3
- Never use `export const dynamic = "force-dynamic"` per-page — use Suspense or client wrappers
- All fixtures follow the `ActionResult<T>` return pattern without exception

## Template References

Detailed section templates in `templates/plan-comicWiseImplementation/`:
- `phase_10_admin_pages_20_new_fi.md`
- `phase_11_testing_6_new_files.md`
- `phase_3_typescript__auth_fixes.md`
- `phase_4_config_edits_5_edits.md`
- `phase_5_route_layouts_3_new_fi.md`
- `phase_6_new_dal_files_9_new_fi.md`
- `phase_7_new_action_files__redi.md`
- `phase_8_utility_files_2_new_fi.md`
- `phase_9a_zustand_stores_7_new_.md`
- `phase_9b_components_14_new_fil.md`
- `validation_gates.md`
- `verified_codebase_state.md`
