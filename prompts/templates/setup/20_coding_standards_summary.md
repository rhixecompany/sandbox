# 20. Coding Standards Summary

> Extracted from `setup.prompt.md`.

## 20. Coding Standards Summary

### Core Rules

- **No `any` types** — ESLint enforces `no-explicit-any: "error"`
- **No manual memoization** — React Compiler is ON (`memo`, `useMemo`, `useCallback` forbidden)
- **No `force-dynamic`** — use Suspense boundaries instead
- **No raw `process.env`** — use `getEnv()` from `src/lib/env.ts` (auth files excepted)
- **No N+1 queries** — use `.with()` in DAL for related data
- **No API routes for mutations** — use Server Actions
- **Always validate inputs** — Zod schemas before DB operations
- **Always check auth** — `auth()` as first line in Server Actions
- **Always return `ActionResult<T>`** — never throw from actions
- **Always cascade deletes** — `{ onDelete: "cascade" }` on all FKs (exception: `auditLog.userId` → `"set null"`)
- **Use Title-Case** for `comicStatus` enum values
- **Use `$inferSelect`** for DAL type parameters, not raw table type
- **Use SSR-safe hooks** for Date/time in components (`useCurrentYear`, `useNow`)

### TypeScript Conventions (from `.github/instructions/typescript.instructions.md`)

- Use `interface` for object shapes, not `type` aliases
- Implement type guards for runtime narrowing (`unknown` → specific type)
- PascalCase component names matching file names
- Export prop interfaces for reusable components
- Create barrel exports (`index.ts`) for directories
- Functional components only — no class components
- No conditional hooks (hooks must always be called in same order)

### Documentation Standards (from `.github/instructions/documentation.instructions.md`)

- TSDoc comments required on functions, classes, hooks, complex types
- Document component props with descriptions
- Comment workarounds with reasons ("Why" not just "What")
- Keep docs in sync with code changes

### Security Standards (from `.github/instructions/security.instructions.md`)

- Validate on both client AND server
- Never string-concatenate DB queries — always use Drizzle query builders
- Escape user-generated content before rendering (XSS prevention)
- Never expose stack traces in production error responses
- Don't store sensitive data in `localStorage` / `sessionStorage`

---
