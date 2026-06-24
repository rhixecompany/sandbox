---
license: MIT
author: Hermes Agent
version: 1.0.0
title: ComicWise — AI Agent Setup & Onboarding
name: setup
description: "Comprehensive AI agent onboarding prompt for ComicWise — architecture, workflows, real code patterns, and conventions"
agent: "Next.js Expert"
model: "Claude Haiku 4.5 (copilot)"
---

# ComicWise — AI Agent Setup & Onboarding

**ComicWise** is a production-grade manga/comic reader built with Next.js 16.1.6 (App Router), React 19.2.4 Server Components, Drizzle ORM 0.45.1 + PostgreSQL (Neon), NextAuth v5 (database sessions), Zustand 5 + React Query 5, shadcn/Radix UI, Tailwind CSS 4, Vitest + Playwright, and a complete database seeding system with CLI + REST API.

---

## 1. Project Architecture

> ├── app/                    # Next.js App Router pages
> │   ├── (auth)/             # Auth route group (signin, signup, etc.)

> **Full content:** `templates/setup/1_project_architecture.md`

## 2. Essential Commands

> pnpm dev                         # Start dev server (Turbopack, port 3000)
> pnpm type-check                  # tsc --noEmit — must be 0 errors before PR

> **Full content:** `templates/setup/2_essential_commands.md`

## 3. Environment Variables

> Create `.env.local` from `.env.local.example`:
> DATABASE_URL="postgresql://user:pass@localhost:5432/comicbook"

> **Full content:** `templates/setup/3_environment_variables.md`

## 4. Database Schema — Critical Facts

> Schema defined in `src/database/schema.ts` (604 lines, **27 tables**, 4 enums).
> // Title-Case values for comicStatus

> **Full content:** `templates/setup/4_database_schema__critical_fa.md`

## 5. Authentication System

> ### Architecture (4 modular files)
> src/auth.ts             → NextAuth({ ...authConfig })  → exports { handlers, aut

> **Full content:** `templates/setup/5_authentication_system.md`

## 6. Data Access Layer (DAL)

> ### Base Class (`src/dal/base-dal.ts`)
> export interface DalOptions {

> **Full content:** `templates/setup/6_data_access_layer_dal.md`

## 7. Server Actions — Primary Mutation Pattern

> ### ActionResult Type (`src/actions/types.ts`)
> export type ActionResult<T> =

> **Full content:** `templates/setup/7_server_actions__primary_muta.md`

## 8. Seeding System (CLI + REST API)

> ### Seeder Template (`BaseSeed<T>`)
> All seeders extend `BaseSeed<T>` and override 4 methods:

> **Full content:** `templates/setup/8_seeding_system_cli__rest_api.md`

## 9. Next.js Configuration (`next.config.ts`)

Key settings active in this project:

```typescript
{
  reactCompiler: true,          // React Compiler is ON — do NOT use useMemo/useCallback/memo
  typedEnv: true,               // Typed process.env
  typedRoutes: true,            // Typed Link href
  cacheComponents: true,        // "use cache" directive enabled
  staleTimes: { dynamic: 30, static: 180 },
  serverExternalPackages: ["postgres", "bcryptjs", "sharp", "nodemailer"],
  serverActions: { bodySizeLimit: "10mb" },
  images: {
    formats: ["image/avif", "image/webp"],
    minimumCacheTTL: 31536000,  // 1 year
    remotePatterns: [/* mangadex, imgur, imagekit, etc. */],
  },
  // Security headers: HSTS, X-Frame-Options DENY, X-Content-Type-Options, Referrer-Policy
}
```

---

## 10. Provider Stack & Root Layout

### Root Layout (`src/app/layout.tsx`)

- 7 custom fonts loaded via `next/font/local` (IBM Plex Sans, Bebas Neue, Schibsted Grotesk, Martian Mono, Fira Sans, Fira Mono)
- Metadata: title "ComicWise", Open Graph, viewport with light/dark theme colors
- Body → `<Suspense>` → `<LayoutProvider>`

### Provider Order (`src/components/layout/layout-provider.tsx`)

```
SessionProvider → QueryClientProvider → ThemeProvider → TooltipProvider → children + lazy Toaster
```

- `ReactQueryDevtools` rendered only in development
- `Toaster` lazy-loaded
- `ThemeProvider` receives theme config props

---

## 11. React Query Keys (`src/lib/query-client.ts`)

> export const queryKeys = {
> list: (filters: Record<string, unknown>) => [

> **Full content:** `templates/setup/11_react_query_keys_srclibquer.md`

## 12. Middleware (`src/proxy.ts`)

```typescript
export function proxy(request: NextRequest) {
  const token = request.cookies.get("auth-token");
  if (request.nextUrl.pathname.startsWith("/dashboard")) {
    if (!token)
      return NextResponse.redirect(new URL("/login", request.url));
  }
  return NextResponse.next();
}

export const config = {
  matcher: ["/dashboard/:path*", "/admin/:path*"]
};
```

> **⚠ Incomplete middleware:** Only `/dashboard` is actually protected. Despite `/admin/:path*` being in the matcher, the function has no `admin` check — it falls through to `NextResponse.next()`. Additionally, it checks for a cookie named `"auth-token"`, not a NextAuth session — this may not integrate with the actual auth system. See §21 (Technical Debt).

---

## 13. TypeScript & Tooling Conventions

### tsconfig.json

- `strict: true`, `target: ES2022`, `module: esnext`, `jsx: "react-jsx"`
- Path aliases: `@/*` → `./src/*`, plus shortcuts: `@database`, `@env`, `@hooks`, `@lib`, `@schemas`, `@ui`, etc.
- Next.js plugin enabled, incremental builds

### ESLint (Flat Config — `eslint.config.mts`)

- Extends `next/core-web-vitals` + `next/typescript`
- **Plugins registered:** `prettier`, `better-tailwindcss`, `playwright`, `vitest`, `drizzle`, `zod`
- **Only 3 active custom rules:** `no-explicit-any: "error"`, `no-unused-vars` (ignore `^_` prefix), `no-import-type-side-effects`
- **Note:** Plugins like `better-tailwindcss`, `playwright`, `vitest`, `drizzle`, `zod` are registered but have **no custom rules enabled**. Their built-in recommended configs may still apply through the plugin registration.

### Vitest (`vitest.config.mts`)

- Environment: `jsdom`
- Setup: `src/tests/setup-env.ts`
- Include: `src/**/*.test.{ts,tsx}`
- Exclude: `.references/`, `tests/e2e/`, `node_modules/`

---

## 14. Unique Project Conventions

> ### React Compiler is ON
> **Do NOT** manually add `useMemo`, `useCallback`, or `memo()`. The React Compile

> **Full content:** `templates/setup/14_unique_project_conventions.md`

## 15. VSCode Configuration

> ### Settings (`.vscode/settings.json`)
> "editor.defaultFormatter": "esbenp.prettier-vscode",

> **Full content:** `templates/setup/15_vscode_configuration.md`

## 16. Common Tasks — Step-by-Step

> ### Feature Discovery Checklist
> Before implementing any feature, answer these questions:

> **Full content:** `templates/setup/16_common_tasks__step-by-step.md`

## 17. Testing

> ### Unit Tests (Vitest)
> pnpm test                        # Run all

> **Full content:** `templates/setup/17_testing.md`

## 18. Key Files Quick Reference

| File | Purpose |
| --- | --- |
| `src/database/schema.ts` | 27 tables, 4 enums, no `relations()` (604 lines) |
| `src/dal/base-dal.ts` | Abstract `BaseDal<T>` + error normalization |
| `src/dal/comic-dal.ts` | Reference DAL with eager loading via `.with()` |
| `src/actions/comic.actions.ts` | Reference Server Action with auth + Zod + DAL |
| `src/actions/types.ts` | `ActionResult<T>` discriminated union |
| `src/actions/auth-db.ts` | `getUserByUsername`, `verifyPassword` (bcryptjs) |
| `src/auth.ts` | NextAuth init — `{ handlers, auth, signIn, signOut }` |
| `src/auth-config.ts` | Session strategy, all callbacks (known bugs noted) |
| `src/auth-providers.ts` | GitHub + Credentials + Keycloak providers |
| `src/auth-adapter.ts` | DrizzleAdapter wiring |
| `src/lib/env.ts` | Zod-validated env vars — `getEnv()` not `process.env` (6 active fields) |
| `src/lib/query-client.ts` | React Query key factory + singleton |
| `src/hooks/use-now.tsx` | SSR-safe Date hook |
| `src/components/layout/layout-provider.tsx` | Provider stack order |
| `src/proxy.ts` | Middleware — protects `/dashboard` only (⚠ `/admin` unguarded) |
| `next.config.ts` | React Compiler, Turbopack, images, security headers |
| `appConfig.ts` | Structured config — mostly stubs (see §21) |
| `src/scripts/seed/seeders/baseSeed.ts` | Template method for all seeders |
| `src/scripts/seed/seedOrchestrator.ts` | Seed dependency resolution + orchestration |
| `src/app/api/seed/route.ts` | Seed REST API (5 HTTP methods) |
| `drizzle.config.ts` | Drizzle Kit config (schema path, dialect, pool) |

---

## 19. External Dependencies Map

| Category | Package | Version | Purpose |
| --- | --- | --- | --- |
| **Framework** | `next` | 16.1.6 | App Router, Server Components, Turbopack |
| **React** | `react` / `react-dom` | 19.2.4 | UI rendering, Server Components |
| **ORM** | `drizzle-orm` / `drizzle-kit` | 0.45.1 | Type-safe SQL, migrations |
| **DB Driver** | `postgres` | — | PostgreSQL client |
| **Auth** | `next-auth` | 5.0.0-beta.30 | Authentication, database sessions |
| **Auth Adapter** | `@auth/drizzle-adapter` | — | NextAuth ↔ Drizzle bridge |
| **Validation** | `zod` | 4.3.6 | Runtime schema validation (⚠ v4 — different API from v3) |
| **State** | `zustand` | 5.0.11 | Client state management |
| **Data Fetching** | `@tanstack/react-query` | 5.x | Client-side caching |
| **UI** | `@radix-ui/*` | — | Accessible primitives (via shadcn) |
| **Styling** | `tailwindcss` | 4.x | Utility-first CSS |
| **Icons** | `@tabler/icons-react` | — | Icon library |
| **Password** | `bcryptjs` | — | Password hashing |
| **CLI** | `commander` | 14.0.3 | Seed CLI (devDependency, not runtime) |
| **Monitoring** | `@sentry/nextjs` | — | Error tracking |
| **Testing** | `vitest` | 4.0.18 | Unit tests (jsdom) |
| **E2E Testing** | `playwright` | — | Browser E2E tests |
| **TypeScript** | `typescript` | 5.9.3 | Static type checking |

> **⚠ Zod v4 note:** This project uses Zod 4.3.6, which has a different API surface from the widely-documented Zod v3. Key differences include schema definition syntax, error formatting, and validation methods. Consult Zod v4 docs, not v3 tutorials.

---

## 20. Coding Standards Summary

> - **No `any` types** — ESLint enforces `no-explicit-any: "error"`
> - **No manual memoization** — React Compiler is ON (`memo`, `useMemo`, `useCallb

> **Full content:** `templates/setup/20_coding_standards_summary.md`

## 21. Known Technical Debt

| Item | Impact | Location |
| --- | --- | --- |
| `proxy.ts` only protects `/dashboard`, not `/admin` | Admin routes unguarded | `src/proxy.ts` |
| `proxy.ts` checks cookie `"auth-token"`, not NextAuth session | May not integrate with actual auth system | `src/proxy.ts` |
| Raw `process.env` in auth files | Convention violation (accepted exception) | `auth-config.ts`, `auth-providers.ts`, `db.ts` |
| `env.ts` has ~60 commented-out field stubs | Only 6 active validations | `src/lib/env.ts` |
| No Drizzle `relations()` definitions | `.with()` limited to FK-inferred relations; `comment.parentId` broken | `src/database/schema.ts` |
| `performance.instructions.md` contradicts React Compiler | Says "use React.memo" — wrong per project config | `.github/instructions/performance.instructions.md` |
| `comment-rating-dal.ts` has no matching schema table | DAL references non-existent `commentRating` table | `src/dal/comment-rating-dal.ts` |
| Two comic schema files coexist | `comic-schema.ts` and `comic.schema.ts` — unclear which is canonical | `src/schemas/` |
| `appConfig.ts` mostly empty stubs | Only `database`, `auth.secret`, and `app` sections active; providers, email, redis, imageKit, cloudinary, sentry all commented out | `appConfig.ts` |

---

## 22. Feature Implementation Workflow

Full template — Discovery → Schema → DAL → Zod → Action → Component → Test → Docs:

1. **Discovery** — Run the Feature Discovery Checklist (§16)
2. **Schema** — Define table in `src/database/schema.ts` with types, FKs (`onDelete: "cascade"`), indexes. Add `relations()` if needed for complex relationships.
3. **DAL** — Create `src/dal/my-entity-dal.ts` extending `BaseDal<typeof myEntity.$inferSelect>`. Export as singleton.
4. **Zod Schemas** — Create `src/schemas/my-entity-schema.ts` with separate `createMyEntitySchema` and `updateMyEntitySchema`. Remember: Zod v4 API.
5. **Server Action** — Create `src/actions/my-entity.actions.ts`: `"use server"` → `auth()` → Zod validate → DAL call → `revalidatePath()` → return `ActionResult<T>`
6. **Server Component Page** — `src/app/(root)/my-feature/page.tsx` + `loading.tsx` + `error.tsx`
7. **Client Component** (if needed) — `"use client"`, no manual memo, SSR-safe hooks
8. **Tests** — Unit tests in `src/tests/`, mock DB/auth, test behavior not implementation, include accessibility checks
9. **Docs** — Update related documentation, add TSDoc comments to all public functions

---

## 23. Instruction Files Reference

Seven instruction files in `.github/instructions/` provide file-pattern-specific conventions for AI agents:

| File | Applies To | Purpose |
| --- | --- | --- |
| `code-review.instructions.md` | `**/*` | Code review standards and GitHub review guidelines |
| `documentation.instructions.md` | `**/*.md, **/*.ts, **/*.tsx` | TSDoc, README, and architecture documentation standards |
| `nextjs.instructions.md` | `**/app/**/*.tsx, **/app/**/*.ts` | App Router, Server/Client Components, data fetching |
| `performance.instructions.md` | `**/*.ts, **/*.tsx, **/*.css` | React, Next.js, DB, and runtime performance (**⚠ React.memo rule is outdated — contradicts React Compiler**) |
| `security.instructions.md` | `**/*.ts, **/*.tsx, **/*.js, **/*.jsx` | Auth, input validation, data protection, XSS prevention |
| `testing.instructions.md` | `**/*.test.ts, **/*.test.tsx, **/*.spec.ts` | Vitest unit tests, Playwright E2E, test environment setup |
| `typescript.instructions.md` | `**/*.ts, **/*.tsx` | Strict mode, interfaces, type guards, React component standards |

Key conventions from these files are merged into this setup prompt (§14, §17, §20). When conflicts exist between instruction files and this setup prompt, **this prompt is authoritative**.

---

## 24. Quality Gate Debugger

> When debugging and fixing errors/warnings/deprecations, follow this workflow:
> ### Phase 1: Run Validation Scripts

> **Full content:** `templates/setup/24_quality_gate_debugger.md`

## Template References

Detailed section templates in `templates/setup/`:
- `1_project_architecture.md`
- `11_react_query_keys_srclibquer.md`
- `14_unique_project_conventions.md`
- `15_vscode_configuration.md`
- `16_common_tasks__step-by-step.md`
- `17_testing.md`
- `2_essential_commands.md`
- `20_coding_standards_summary.md`
- `24_quality_gate_debugger.md`
- `3_environment_variables.md`
- `4_database_schema__critical_fa.md`
- `5_authentication_system.md`
- `6_data_access_layer_dal.md`
- `7_server_actions__primary_muta.md`
- `8_seeding_system_cli__rest_api.md`
