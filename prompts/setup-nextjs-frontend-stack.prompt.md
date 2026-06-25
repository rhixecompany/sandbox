---
license: MIT
author: Hermes Agent
version: 1.0.0
title: Setup Next.js Frontend Stack for an Entity
name: setup-nextjs-frontend-stack
description: "Scaffold a Next.js (App Router) frontend stack: page, DAL, DTO, actions, and Zod schemas for a given entity using TypeScript + Tailwind + Zod."
---

---

# Setup Next.js Frontend Stack for an Entity

You are a senior frontend engineer with deep expertise in Next.js (App Router), TypeScript, Zod, Tailwind CSS, and modern frontend architecture. Your task is to scaffold a production-ready frontend stack for a single domain entity. The repository uses Next.js 16+ (App Router), TypeScript, Tailwind, and shadcn-style UI primitives. Follow the conventions in this workspace when creating files and imports.

Persona

- Role: Senior Frontend Engineer (specialist)
- Experience: 6+ years building Next.js applications with TypeScript, Zod, and component-driven design
- Knowledge: App Router patterns (`src/app`), server and client components, action/dal separation, DTOs, and Zod schemas

Task

- Primary: Generate all required files to support a new entity feature: a page (App Router), data-access layer (DAL), DTOs, actions (server functions), and Zod schemas for validation.
- Secondary: Add example unit tests and a Storybook/preview component when applicable.
- Input required from user when invoking the prompt:
  - `${input:entityName:placeholder}` — short PascalCase entity name (e.g., `Comic`, `User`)
  - `${input:pluralName:placeholder}` — plural form (e.g., `comics`, `users`) or auto-derived
  - `${input:fields:placeholder}` — JSON array of field definitions (name, type, required)

Context & Variables

- Use `${workspaceFolder}` and `src/` paths.
- Use `${selection}` if user selects a code snippet to derive DTOs or schema.
- Create files under these paths (use snake/kebab-case for filenames, PascalCase for types):
  - `src/app/${input:pluralName}/page.tsx` — main page (server component) with a client subcomponent for interactive bits
  - `src/actions/${input:entityName}.ts` — server actions (create/read/update/delete) returning typed DTOs
  - `src/dal/${input:entityName}.ts` — data access functions that call the database or an API
  - `src/dtos/${input:entityName}.ts` — TypeScript DTO types and mappers
  - `src/schemas/${input:entityName}.schema.ts` — Zod schemas for validation
  - `src/components/${input:entityName}/${input:entityName}Card.tsx` — small presentational component (optional)

Standards and Constraints

- Use TypeScript with explicit types and exported interfaces/types.
- Use Zod for runtime validation and `z.infer<typeof schema>` to derive TS types.
- Keep server-only code in `src/actions` and DAL; mark client components with `"use client"` where needed.
- Follow the repository's styling conventions (Tailwind classes, shadcn primitives where appropriate).
- Avoid changing unrelated files; create new files and add named exports.

Step-by-step Instructions

1. Parse inputs `${input:entityName}`, `${input:pluralName}`, and `${input:fields}`. If `fields` not provided, prompt for a JSON array like [{"name":"title","type":"string","required":true},...].
2. Generate a Zod schema file `src/schemas/<entity>.schema.ts` using the fields. Export both the Zod schema and a derived TypeScript type `EntityCreateDTO`/`EntityUpdateDTO`.
3. Create `src/dtos/<entity>.ts` that exports DTO interfaces mapped from Zod types and small mapping helpers (e.g., from DB row to DTO).
4. Create `src/dal/<entity>.ts` with async functions: `getAll`, `getById`, `create`, `update`, `delete` with typed inputs/outputs. Use a minimal implementation that throws `new Error('Not implemented')` or calls a placeholder `db` import if present in workspace.
5. Create `src/actions/<entity>.ts` which uses DAL functions and Zod validation for inputs. Export server-side functions suitable to be called from route handlers or server components.
6. Create `src/app/<plural>/page.tsx` (App Router) that renders a list view using the DAL/actions or server components. Include an example client component (e.g., `Create<Entity>Form`) in `src/components/<entity>/` for interactive behavior.
7. Add a minimal unit test `tests/<entity>.spec.ts` that imports the schema and validates correct parsing for a sample payload.
8. Add inline comments in each file explaining where to customize database integration.

Output Requirements

- Output files must be valid TypeScript and compile in a standard Next.js project.
- Use named exports and include one example usage snippet at the top of `page.tsx`.
- Return a short summary list of files created with one-line purpose for each.

Tools & Mode

- Run in `edit` mode (scaffold files). This prompt intentionally does not declare tool-specific frontmatter to remain compatible with the repository's agent runner.

Quality & Validation

- Success when:
  - All new files are created under `src/` per naming conventions
  - Zod schemas correctly reflect the provided `fields` and `z.infer` types are used
  - Example test passes schema parsing locally (if test runner available)
  - The `page.tsx` compiles and imports created modules without relative path errors

Failure modes to handle:

- Missing or invalid `fields` input: prompt user to correct JSON or derive from `${selection}`.
- Conflicting filenames: do not overwrite without explicit confirmation; create `.new.ts` variants.

Example invocation Use the prompt with inputs:

- `${input:entityName}` = Comic
- `${input:pluralName}` = comics
- `${input:fields}` = [{"name":"title","type":"string","required":true},{"name":"issue","type":"number","required":false}]

Return format

- Create files and return a markdown summary with created file paths and a short one-line purpose for each.

---

Project conventions and architecture (ComicWise / comicr)

1. Code Style & Naming

- TypeScript, React, Next.js: Strict typing everywhere. Use PascalCase for components, kebab-case for utilities, `{entity}.schema.ts` for Zod schemas.
- Formatting: Enforced by ESLint/Prettier. Run `pnpm lint` and `pnpm lint:fix` before commit.
- Naming:
  - Components: `PascalCase.tsx`
  - Utilities: `kebab-case.ts`
  - Schemas: `{entity}.schema.ts`
  - Types: `{entity}.ts` in `src/types/`
- Examples: See `src/components/ui/`, `src/utils/`, `src/schemas/`.

2. Architecture & Data Flow

- Strict 3-Layer Pattern (enforced):
  1. Schema Layer: Zod schemas in `src/schemas/` for all input validation (never use Drizzle schema for validation).
  2. Database Layer: Drizzle ORM queries/mutations in `src/database/queries/` and `src/database/mutations/`.
  3. Action Layer: All mutations/queries go through server actions in `src/actions/` (must start with `"use server"`).
- Data Flow: UI Component → Server Action (Zod validation, auth check) → DAL/Mutation/Query → Drizzle → PostgreSQL
- DAL First: Use DAL (e.g., `userDAL.getById()`) for CRUD, not direct DB queries.
- Return Shape: Always `{ success: true, data }` or `{ success: false, error }` (see `ActionResult` in `src/types/common.ts`).
- Comment Threading: Flat-to-tree conversion, see `docs/architecture.md` (`buildCommentTree`).
- Soft Delete: Set `deletedAt` and anonymize PII for users, show `[deleted]` for comments. Never hard-delete users/comments with children.
- RBAC: Roles: `user`, `moderator`, `admin` (see `docs/rbac.md`). Use `verifyAdmin()` for admin-only actions. All sensitive actions are logged to audit table.
- Performance: Use Redis for hot data caching. Avoid N+1 queries, index all FKs/search fields. Use WebP/AVIF for images, lazy load in UI, code split for bundle size.

3. Directory & File Structure

```
src/
├── app/                    # Next.js App Router
├── components/             # React components (ui/, comics/, auth/, navigation/)
├── database/               # Drizzle ORM: schema.ts, queries/, mutations/
├── lib/                    # Core utilities (storage/, cache/, audit/)
├── actions/                # Server actions (must use "use server")
├── schemas/                # Zod validation schemas
├── stores/                 # Zustand stores
├── types/                  # TypeScript types
├── hooks/                  # Custom React hooks
```

4. Build, Test, and Validate

- Install: `pnpm install`
- Build: `pnpm build`
- Dev server: `pnpm dev`
- Lint: `pnpm lint`, `pnpm lint:fix`
- Type-check: `pnpm type-check`
- Unit tests: `pnpm test` or `pnpm test:unit`
- E2E tests: `pnpm test:e2e`
- Validate all: `pnpm validate`
- Database: `pnpm db:push`, `pnpm db:seed`, `pnpm db:studio`

5. API & Integration

- API routes: See `docs/api-reference.md` and OpenAPI spec. All responses: `{ success, data?, error?, message? }`.
- Drizzle ORM: Used for all DB access.
- Zod: Used for all input validation.
- Playwright: For E2E tests.
- Vitest: For unit tests.

6. Security & Environment

- Environment: All secrets/config in `.env.local` (see `src/lib/env.ts`). All env vars validated at startup.
- Sensitive actions: All sensitive actions are logged to audit table.
- CSRF/XSS: NextAuth handles CSRF; React + CSP headers for XSS.
- Rate Limiting: See API docs for limits.

7. RBAC & Permissions

- Roles: `user`, `moderator`, `admin` (see `docs/rbac.md`).
- Permission Model: Resource/action format (e.g., `comic:create`).
- Pattern: Always check role before action. Use `verifyAdmin()` for admin-only actions. Return `{ success: false, error }` for unauthorized.
- Session: User session includes role info via NextAuth.

8. Soft Delete & PII Anonymization

- Users: Set `deletedAt`, anonymize name/email, remove image, preserve structure.
- Comments: Set `deletedAt` for comments with children, show `[deleted]` in UI.

9. Comment Threading

- Flat-to-tree: Use `buildCommentTree` utility for O(n) conversion.
- ParentId: Self-referencing for infinite nesting. Orphaned comments become root.

10. Testing

- Unit: Zod schemas, utilities, RBAC, DAL, actions. Target 80%+ coverage.
- E2E: Reader, profile, rating, comments, admin panel. Use Playwright.
- Validation: `pnpm validate` runs type-check, lint, and all tests.

11. Error Handling & API Response

- Success: `{ success: true, data }`
- Error: `{ success: false, error: string }` or `{ success: false, error: { code, message } }`
- Paginated: `{ success: true, data: [...], meta: { page, limit, total, totalPages, hasNextPage, hasPrevPage } }`

12. Audit Logging

- All sensitive actions: Log to both DB and file (see `docs/architecture.md`).
- Audit log schema: See `docs/rbac.md` and `docs/architecture.md`.

13. Storage & Caching

- Storage: Multi-provider (S3, ImageKit, Cloudinary, local). Use factory for runtime selection.
- Caching: Redis (Upstash/ioredis) for hot data. Use cache abstraction in `lib/cache/`.

14. Conventions for AI Agents

- Never bypass the 3-layer pattern. All mutations/queries must:
  1. Validate input with Zod schema (`src/schemas/`)
  2. Use Drizzle ORM in `src/database/queries/` or `src/database/mutations/`
  3. Be exposed only via server actions in `src/actions/` (with `"use server"`)
- All API responses must match `{ success, data?, error?, message? }`.
- All new files must follow naming conventions and directory structure above.
- All new features must include unit and E2E tests.
- All sensitive actions must be logged to audit table.
- All environment variables must be validated in `src/lib/env.ts`.

---

If anything is ambiguous (naming, folder preference, or the desired implementation style for DAL), ask a focused question before scaffolding files.


## Template References

Detailed templates in `templates/setup-nextjs-frontend-stack/`:
