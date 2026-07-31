---

name: setup

title: 'ComicWise — AI Agent Setup & Onboarding'

description: 'Comprehensive AI agent onboarding prompt for ComicWise — architecture, workflows, real code patterns, and conventions.'

version: 1.0.0

license: MIT

author: Hermes Agent

toolsets:

  - file

  - terminal

  - web

scripts: []

skills:

  - subagent-driven-development

formatter: default

plan: None

dependencies:

  - skill:subagent-driven-development

tags:

  - agents

  - architecture

  - backend

  - ml

  - nextjs

  - prompts

  - typescript

  - workflow

trigger: /setup

metadata:

  hermes: {}

---

## Goal

Comprehensive AI agent onboarding prompt for ComicWise — architecture, workflows, real code patterns, and conventions.

## 1. Project Architecture

> ├── app/                    # Next.js App Router pages
> │   ├── (auth)/             # Auth route group (signin, signup, etc.)
> **Full content:**

## 2. Essential Commands

> pnpm dev                         # Start dev server (Turbopack, port 3000)
> pnpm type-check                  # tsc --noEmit — must be 0 errors before PR
> **Full content:**

## 3. Environment Variables

> Create `.env.local` from `.env.local.example`:
> DATABASE_URL="postgresql://user:pass@localhost:5432/comicbook"
> **Full content:**

## 4. Database Schema — Critical Facts

> Schema defined in `src/database/schema.ts` (604 lines, **27 tables**, 4 enums).
> // Title-Case values for comicStatus
> **Full content:**

## 5. Authentication System

### Architecture (4 modular files)

> src/auth.ts             → NextAuth({ ...authConfig })  → exports { handlers, aut

## 6. Data Access Layer (DAL)

### Base Class (`src/dal/base-dal.ts`)

>
> export interface DalOptions {
> **Full content:**

## 7. Server Actions — Primary Mutation Pattern

### ActionResult Type (`src/actions/types.ts`)

>
> export type ActionResult<T
> =
>
> **Full content:**

## 8. Seeding System (CLI + REST API)

### Seeder Template (`BaseSeed<T

> `)>
> All seeders extend`BaseSeed<T>` and override 4 methods:
> **Full content:**

## 9. Next.js Configuration (`next.config.ts`)

Key settings active in this project:```typescript{  reactCompiler: true,          // React Compiler is ON — do NOT use useMemo/useCallback/memo  typedEnv: true,               // Typed process.env  typedRoutes: true,            // Typed Link href  cacheComponents: true,        // "use cache" directive enabled  staleTimes: { dynamic: 30, static: 180 },  serverExternalPackages: ["postgres", "bcryptjs", "sharp", "nodemailer"],  serverActions: { bodySizeLimit: "10mb" },  images: {    formats: ["image/avif", "image/webp"],    minimumCacheTTL: 31536000,  // 1 year    remotePatterns: [/* mangadex, imgur, imagekit, etc. */],  },  // Security headers: HSTS, X-Frame-Options DENY, X-Content-Type-Options, Referrer-Policy}```---

## 10. Provider Stack & Root Layout

### Root Layout (`src/app/layout.tsx`)

- 7 custom fonts loaded via `next/font/local` (IBM Plex Sans, Bebas Neue, Schibsted Grotesk, Martian Mono, Fira Sans, Fira Mono)- Metadata: title "ComicWise", Open Graph, viewport with light/dark theme colors- Body → `<Suspense

> ` → `<LayoutProvider>`

### Provider Order (`src/components/layout/layout-provider.tsx`)

```tsx
SessionProvider → QueryClientProvider → ThemeProvider → TooltipProvider → children + lazy Toaster
```

- `ReactQueryDevtools` rendered only in development
- `Toaster` lazy-loaded
- `ThemeProvider` receives theme config props

---

## 11. React Query Keys (`src/lib/query-client.ts`)

> export const queryKeys = {
> list: (filters: Record<string, unknown>) =
> [
> **Full content:**

## 12. Middleware (`src/proxy.ts`)

```typescriptexport function proxy(request: NextRequest) {  const token = request.cookies.get("auth-token");  if (request.nextUrl.pathname.startsWith("/dashboard")) {    if (!token)      return NextResponse.redirect(new URL("/login", request.url));  }  return NextResponse.next();}export const config = {  matcher: ["/dashboard/:path*", "/admin/:path*"]};```

> **⚠ Incomplete middleware:** Only `/dashboard` is actually protected. Despite `/admin/:path*` being in the matcher, the function has no `admin` check — it falls through to `NextResponse.next()`. Additionally, it checks for a cookie named `"auth-token"`, not a NextAuth session — this may not integrate with the actual auth system. See §21 (Technical Debt).---

## 13. TypeScript & Tooling Conventions

### tsconfig.json

- `strict: true`, `target: ES2022`, `module: esnext`, `jsx: "react-jsx"`- Path aliases: `@/*` → `./src/*`, plus shortcuts: `@database`, `@env`, `@hooks`, `@lib`, `@schemas`, `@ui`, etc.- Next.js plugin enabled, incremental builds

### ESLint (Flat Config — `eslint.config.mts`)

- Extends `next/core-web-vitals` + `next/typescript`- **Plugins registered:** `prettier`, `better-tailwindcss`, `playwright`, `vitest`, `drizzle`, `zod`- **Only 3 active custom rules:** `no-explicit-any: "error"`, `no-unused-vars` (ignore `^_` prefix), `no-import-type-side-effects`- **Note:** Plugins like `better-tailwindcss`, `playwright`, `vitest`, `drizzle`, `zod` are registered but have **no custom rules enabled**. Their built-in recommended configs may still apply through the plugin registration.

### Vitest (`vitest.config.mts`)

- Environment: `jsdom`- Setup: `src/tests/setup-env.ts`- Include: `src/**/*.test.{ts,tsx}`- Exclude: `.references/`, `tests/e2e/`, `node_modules/`---

## 14. Unique Project Conventions

### React Compiler is ON

> **Do NOT** manually add `useMemo`, `useCallback`, or `memo()`. The React Compile

## 15. VSCode Configuration>

### Settings (`.vscode/settings.json`)

>
> "editor.defaultFormatter": "esbenp.prettier-vscode",
> **Full content:**

## 16. Common Tasks — Step-by-Step

### Feature Discovery Checklist

> Before implementing any feature, answer these questions:

## 17. Testing

### Unit Tests (Vitest)

> pnpm test                        # Run all

## 18. Key Files Quick Reference

| File | Purpose || --- | --- || `src/database/schema.ts` | 27 tables, 4 enums, no `relations()` (604 lines) || `src/dal/base-dal.ts` | Abstract `BaseDal<T

> ` + error normalization || `src/dal/comic-dal.ts` | Reference DAL with eager loading via `.with()` || `src/actions/comic.actions.ts` | Reference Server Action with auth + Zod + DAL || `src/actions/types.ts` | `ActionResult<T>` discriminated union || `src/actions/auth-db.ts` | `getUserByUsername`,`verifyPassword` (bcryptjs) || `src/auth.ts` | NextAuth init — `{ handlers, auth, signIn, signOut }` || `src/auth-config.ts` | Session strategy, all callbacks (known bugs noted) || `src/auth-providers.ts` | GitHub + Credentials + Keycloak providers || `src/auth-adapter.ts` | DrizzleAdapter wiring || `src/lib/env.ts` | Zod-validated env vars — `getEnv()` not `process.env` (6 active fields) || `src/lib/query-client.ts` | React Query key factory + singleton || `src/hooks/use-now.tsx` | SSR-safe Date hook || `src/components/layout/layout-provider.tsx` | Provider stack order || `src/proxy.ts` | Middleware — protects `/dashboard` only (⚠ `/admin` unguarded) || `next.config.ts` | React Compiler, Turbopack, images, security headers || `appConfig.ts` | Structured config — mostly stubs (see §21) || `src/scripts/seed/seeders/baseSeed.ts` | Template method for all seeders || `src/scripts/seed/seedOrchestrator.ts` | Seed dependency resolution + orchestration || `src/app/api/seed/route.ts` | Seed REST API (5 HTTP methods) || `drizzle.config.ts` | Drizzle Kit config (schema path, dialect, pool) |---

## 19. External Dependencies Map

| Category | Package | Version | Purpose || --- | --- | --- | --- || **Framework** | `next` | 16.1.6 | App Router, Server Components, Turbopack || **React** | `react` / `react-dom` | 19.2.4 | UI rendering, Server Components || **ORM** | `drizzle-orm` / `drizzle-kit` | 0.45.1 | Type-safe SQL, migrations || **DB Driver** | `postgres` | — | PostgreSQL client || **Auth** | `next-auth` | 5.0.0-beta.30 | Authentication, database sessions || **Auth Adapter** | `@auth/drizzle-adapter` | — | NextAuth ↔ Drizzle bridge || **Validation** | `zod` | 4.3.6 | Runtime schema validation (⚠ v4 — different API from v3) || **State** | `zustand` | 5.0.11 | Client state management || **Data Fetching** | `@tanstack/react-query` | 5.x | Client-side caching || **UI** | `@radix-ui/*` | — | Accessible primitives (via shadcn) || **Styling** | `tailwindcss` | 4.x | Utility-first CSS || **Icons** | `@tabler/icons-react` | — | Icon library || **Password** | `bcryptjs` | — | Password hashing || **CLI** | `commander` | 14.0.3 | Seed CLI (devDependency, not runtime) || **Monitoring** | `@sentry/nextjs` | — | Error tracking || **Testing** | `vitest` | 4.0.18 | Unit tests (jsdom) || **E2E Testing** | `playwright` | — | Browser E2E tests || **TypeScript** | `typescript` | 5.9.3 | Static type checking |

> **⚠ Zod v4 note:** This project uses Zod 4.3.6, which has a different API surface from the widely-documented Zod v3. Key differences include schema definition syntax, error formatting, and validation methods. Consult Zod v4 docs, not v3 tutorials.---

## 20. Coding Standards Summary

> - **No `any` types** — ESLint enforces `no-explicit-any: "error"`
> - **No manual memoization** — React Compiler is ON (`memo`, `useMemo`, `useCallb
> **Full content:**

## 21. Known Technical Debt

| Item | Impact | Location || --

- | --- | --- || `proxy.ts` only protects `/dashboard`, not `/admin` | Admin routes unguarded | `src/proxy.ts` || `proxy.ts` checks cookie `"auth-token"`, not NextAuth session | May not integrate with actual auth system | `src/proxy.ts` || Raw `process.env` in auth files | Convention violation (accepted exception) | `auth-config.ts`, `auth-providers.ts`, `db.ts` || `env.ts` has ~60 commented-out field stubs | Only 6 active validations | `src/lib/env.ts` || No Drizzle `relations()` definitions | `.with()` limited to FK-inferred relations; `comment.parentId` broken | `src/database/schema.ts` || `performance.instructions.md` contradicts React Compiler | Says "use React.memo" — wrong per project config | `.github/instructions/performance.instructions.md` || `comment-rating-dal.ts` has no matching schema table | DAL references non-existent `commentRating` table | `src/dal/comment-rating-dal.ts` || Two comic schema files coexist | `comic-schema.ts` and `comic.schema.ts` — unclear which is canonical | `src/schemas/` || `appConfig.ts` mostly empty stubs | Only `database`, `auth.secret`, and `app` sections active; providers, email, redis, imageKit, cloudinary, sentry all commented out | `appConfig.ts` |---

## 22. Feature Implementation Workflow

Full template — Discovery → Schema → DAL → Zod → Action → Component → Test → Docs:1. **Discovery** — Run the Feature Discovery Checklist (§16)2. **Schema** — Define table in `src/database/schema.ts` with types, FKs (`onDelete: "cascade"`), indexes. Add `relations()` if needed for complex relationships.3. **DAL** — Create `src/dal/my-entity-dal.ts` extending `BaseDal<typeof myEntity.$inferSelect

> `. Export as singleton.4. **Zod Schemas** — Create`src/schemas/my-entity-schema.ts` with separate `createMyEntitySchema` and `updateMyEntitySchema`. Remember: Zod v4 API.5. **Server Action** — Create`src/actions/my-entity.actions.ts`:`"use server"` → `auth()` → Zod validate → DAL call → `revalidatePath()` → return `ActionResult<T>`6. **Server Component Page** —`src/app/(root)/my-feature/page.tsx` + `loading.tsx` + `error.tsx`7. **Client Component** (if needed) —`"use client"`, no manual memo, SSR-safe hooks8. **Tests** — Unit tests in`src/tests/`, mock DB/auth, test behavior not implementation, include accessibility checks9. **Docs** — Update related documentation, add TSDoc comments to all public functions---

## 23. Instruction Files Reference

Seven instruction files in `.github/instructions/` provide file-pattern-specific conventions for AI agents:| File | Applies To | Purpose || --- | --- | --- || `code-review.instructions.md` | `**/*` | Code review standards and GitHub review guidelines || `documentation.instructions.md` | `**/*.md, **/*.ts, **/*.tsx` | TSDoc, README, and architecture documentation standards || `nextjs.instructions.md` | `**/app/**/*.tsx, **/app/**/*.ts` | App Router, Server/Client Components, data fetching || `performance.instructions.md` | `**/*.ts, **/*.tsx, **/*.css` | React, Next.js, DB, and runtime performance (**⚠ React.memo rule is outdated — contradicts React Compiler**) || `security.instructions.md` | `**/*.ts, **/*.tsx, **/*.js, **/*.jsx` | Auth, input validation, data protection, XSS prevention || `testing.instructions.md` | `**/*.test.ts, **/*.test.tsx, **/*.spec.ts` | Vitest unit tests, Playwright E2E, test environment setup || `typescript.instructions.md` | `**/*.ts, **/*.tsx` | Strict mode, interfaces, type guards, React component standards |Key conventions from these files are merged into this setup prompt (§14, §17, §20). When conflicts exist between instruction files and this setup prompt, **this prompt is authoritative**.---

## 24. Quality Gate Debugger

> When debugging and fixing errors/warnings/deprecations, follow this workflow:>>

### Phase 1: Run Validation Scripts

## Template References

Detailed section templates in `templates/setup/`:- `1_project_architecture.md`- `11_react_query_keys_srclibquer.md`- `14_unique_project_conventions.md`- `15_vscode_configuration.md`- `16_common_tasks__step-by-step.md`- `17_testing.md`- `2_essential_commands.md`- `20_coding_standards_summary.md`- `24_quality_gate_debugger.md`- `3_environment_variables.md`- `4_database_schema__critical_fa.md`- `5_authentication_system.md`- `6_data_access_layer_dal.md`- `7_server_actions__primary_muta.md`- `8_seeding_system_cli__rest_api.md`

## Personas

See [`templates/_shared/personas.md`](templates/_shared/personas.md) for shared persona templates.

| Persona | When to Use |
| ------- | ----------- |
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
| --- | ------ | ----------- |
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
| ------- | --------- |
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
