# Phase 6: New Sections (4 items)

> Extracted from `plan-updateAiAgentSetupPrompt2.prompt.md`.

## Phase 6: New Sections (4 items)

### Step 34 — Add §21: Known Technical Debt

| Item | Impact | Location |
| --- | --- | --- |
| `proxy.ts` only protects `/dashboard`, not `/admin` | Admin routes unguarded | `src/proxy.ts` |
| `proxy.ts` uses cookie `"auth-token"`, not NextAuth session | May not integrate with actual auth | `src/proxy.ts` |
| Raw `process.env` in auth files | Convention violation (accepted exception) | `auth-config.ts`, `auth-providers.ts`, `db.ts` |
| `env.ts` has 60+ commented-out field stubs | Only 6 active validations | `src/lib/env.ts` |
| No Drizzle `relations()` definitions | `.with()` limited to FK-inferred relations; `comment.parentId` broken | `src/database/schema.ts` |
| `performance.instructions.md` contradicts React Compiler | Says "use React.memo" — wrong | `.github/instructions/performance.instructions.md` |
| `comment-rating-dal.ts` has no matching schema table | DAL references non-existent `commentRating` table | `src/dal/comment-rating-dal.ts` |
| Two comic schema files coexist | `comic-schema.ts` and `comic.schema.ts` — unclear which is canonical | `src/schemas/` |
| `appConfig.ts` mostly empty stubs | Only 3 of ~10 sections have active config | `appConfig.ts` |

### Step 35 — Add §22: Feature Implementation Workflow

Full template — Discovery → Schema → DAL → Zod → Action → Component → Test → Docs:

1. **Discovery** — Run feature checklist (Step 30)
2. **Schema** — Define table in `schema.ts` with types, FKs (`onDelete: "cascade"`), indexes
3. **DAL** — Create `src/dal/my-entity-dal.ts` extending `BaseDal<typeof myEntity.$inferSelect>`, singleton export
4. **Zod Schemas** — Create `src/schemas/my-entity-schema.ts` with separate `createMyEntitySchema` and `updateMyEntitySchema`
5. **Server Action** — Create `src/actions/my-entity.actions.ts`: `"use server"` → `auth()` → Zod validate → DAL call → `revalidatePath()` → return `ActionResult<T>`
6. **Server Component Page** — `src/app/(root)/my-feature/page.tsx` + `loading.tsx` + `error.tsx`
7. **Client Component** (if needed) — `"use client"`, no manual memo, SSR-safe hooks
8. **Tests** — Unit tests in `src/tests/`, mock DB/auth, test behavior not implementation
9. **Docs** — Update related documentation, add TSDoc comments

### Step 36 — Add §23: Instruction Files Reference

| File | Applies To | Purpose |
| --- | --- | --- |
| `code-review.instructions.md` | `**/*` | Code review standards and GitHub review guidelines |
| `documentation.instructions.md` | `**/*.md,**/*.ts,**/*.tsx` | TSDoc, README, and architecture documentation standards |
| `nextjs.instructions.md` | `**/app/**/*.tsx,**/app/**/*.ts` | App Router, Server/Client Components, data fetching |
| `performance.instructions.md` | `**/*.ts,**/*.tsx,**/*.css` | React, Next.js, DB, and runtime performance (**⚠ React.memo rule outdated**) |
| `security.instructions.md` | `**/*.ts,**/*.tsx,**/*.js,**/*.jsx` | Auth, input validation, data protection, XSS prevention |
| `testing.instructions.md` | `**/*.test.ts,**/*.test.tsx,**/*.spec.ts` | Vitest unit tests, Playwright E2E, test environment setup |
| `typescript.instructions.md` | `**/*.ts,**/*.tsx` | Strict mode, interfaces, type guards, React component standards |

### Step 37 — Keep model as "Claude Haiku 4.5 (copilot)"

Frontmatter model field stays as-is per user preference.

---
