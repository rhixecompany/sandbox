# Plan: Update AI Agent Setup Prompt for ComicWise

**TL;DR:** Update `.github/prompts/setup.prompt.md` from 824 lines/20 sections to ~1200-1400 lines/24 sections. Corrects 6 factual inaccuracies, adds 15 undocumented schema tables/fields, merges ~35 conventions from 6 instruction files, adds 8 missing commands, documents Next.js 16-specific patterns, adds a technical debt register, and prominently flags the Drizzle relations gap. Model stays as "Claude Haiku 4.5 (copilot)".

---

## Phase 1: Fix Inaccuracies (6 items)

### Step 1 — Fix `comic.rating` type in §4

Clarify dual types: `comic.rating` is `decimal(10,1)` (aggregate display), `rating.rating` is `integer` (per-user 1–5 stars). Current doc says only "integer".

### Step 2 — Fix env.ts description in §3

Change "validates all 60+ environment variables" to "validates 6 active fields" (`DATABASE_URL`, `NEON_DATABASE_URL`, `AUTH_SECRET`, `NEXT_PUBLIC_API_URL`, `NODE_ENV`, `DEBUG`). Note 60+ are commented out as stubs for future use.

### Step 3 — Fix `proxy.ts` in §12

Current doc claims both `/dashboard` and `/admin` are protected. Actual `proxy.ts` only checks `/dashboard` via cookie `"auth-token"`. Admin falls through. Flag as incomplete middleware.

### Step 4 — Document raw `process.env` as auth-layer exception

`auth-config.ts`, `auth-providers.ts`, `db.ts` all use raw `process.env`. Add note in §14: "Auth files use raw `process.env` as a known exception (loaded before app initialization)."

### Step 5 — Update version numbers in §19

- React `19.2.4`
- Zod `4.3.6` (v4 — not v3, different API surface)
- Zustand `5.0.11`
- Vitest `4.0.18`
- TypeScript `5.9.3`
- Drizzle ORM `0.45.1`
- NextAuth `5.0.0-beta.30`
- Commander `14.0.3` (devDependency, not runtime)

Note Zod v4 API differences from widely-documented v3.

### Step 6 — Fix ESLint description in §13

Only 3 active rules: `no-explicit-any`, `no-unused-vars`, `no-import-type-side-effects`. Plugins (`better-tailwindcss`, `playwright`, `vitest`, `drizzle`, `zod`) are registered but have no custom rules enabled.

---

## Phase 2: Add Missing Schema Knowledge (9 items)

### Step 7 — Add RBAC tables to §4

- `role` (id, name, description, isSystem)
- `permission` (id, name, resource via resourceEnum, action via actionEnum)
- `rolePermission` (composite PK roleId+permissionId, cascade deletes)
- `userRole2` (composite PK userId+roleId, assignedBy FK to user)

Note: JS export is `userRole2` because enum `userRole` already uses that name.

### Step 8 — Add `auditLog` table to §4

Fields: `userId` (`onDelete: "set null"` — exception to cascade rule), `action`, `resource` (resourceEnum), `resourceId`, `details`, `oldValues`, `newValues`, `ipAddress`, `userAgent`, `sessionId`. 7 indexes.

### Step 9 — Add supplementary tables

- `readerSettings` (backgroundMode, readingMode, defaultQuality — one-to-one with user)
- `passwordResetToken` (email, token unique, expires)
- `userPreference`
- `comicImage`
- `chapterImage`

### Step 10 — Document soft delete

`user.deletedAt` exists in schema. Add rule: "Filter `WHERE deletedAt IS NULL` in user queries."

### Step 11 — Document `user.settings` JSONB

```typescript
settings: jsonb("settings").$type<{
  emailNotifications?: boolean;
  profileVisibility?: "private" | "public";
  readingHistoryVisibility?: boolean;
}>();
```

### Step 12 — Add `searchVector` fields

`comic.searchVector`, `author.searchVector`, `artist.searchVector` — stored as `text` columns (not actual PostgreSQL `tsvector` despite the name).

### Step 13 — Add `resourceEnum` and `actionEnum`

```typescript
resourceEnum: "comic" |
  "chapter" |
  "user" |
  "comment" |
  "rating" |
  "bookmark" |
  "notification" |
  "author" |
  "artist" |
  "genre" |
  "type" |
  "system";
actionEnum: "create" | "read" | "update" | "delete" | "manage";
```

Used by RBAC and audit tables.

### Step 14 — Update table count

27 tables total (not "30+"). Full list: `user`, `account`, `session`, `verificationToken`, `authenticator`, `passwordResetToken`, `type`, `author`, `artist`, `genre`, `comic`, `chapter`, `comicImage`, `chapterImage`, `comicToGenre`, `bookmark`, `comment`, `readingProgress`, `readerSettings`, `rating`, `notification`, `role`, `permission`, `rolePermission`, `userRole2`, `auditLog`, `userPreference`.

### Step 15 — Add Drizzle relations warning (CRITICAL)

New prominent callout in §6:

> **⚠ No explicit `relations()` definitions in schema.ts.** DALs rely on Drizzle's FK inference from `.references()` column declarations. This means:
>
> - Simple FK relations (`comic.authorId → author.id`) auto-infer and `.with({ author: true })` works.
> - Junction tables (`comicToGenre`) are inferred from FKs and `.with({ genres: { with: { genre: true } } })` works.
> - `comment.parentId` has **no** `.references()` call → parent/replies relation **cannot** be used with `db.query`.
> - Self-referential, multi-FK-to-same-table, and custom-named relations **require explicit `relations()` to be added**.
>
> Current DALs work because they only use simple FK-inferred relations. If you need advanced relations, add `relations()` definitions to schema.ts.

---

## Phase 3: Merge Instruction File Conventions (6 items)

### Step 16 — Add TypeScript conventions to §20

From `.github/instructions/typescript.instructions.md`:

- Use `interface` for object shapes, not `type` aliases
- Implement type guards for runtime narrowing (`unknown` → specific type)
- PascalCase component names matching file names
- Export prop interfaces for reusable components
- Create barrel exports (`index.ts`) for directories
- Functional components only — no class components
- No conditional hooks

### Step 17 — Add documentation standards to §20

From `.github/instructions/documentation.instructions.md`:

- TSDoc comments required on functions, classes, hooks, complex types
- Document component props with descriptions
- Comment workarounds with reasons
- Keep docs in sync with code changes

### Step 18 — Add Next.js rules to §14

From `.github/instructions/nextjs.instructions.md`:

- Every route directory needs `loading.tsx` + `error.tsx`
- Never access `Date.now()`, `localStorage`, `window`, `document` in Server Components
- Use Next.js `<Image>` for all images
- Use `next/font` for all fonts
- Prefer static generation over SSR
- All code must be Turbopack-compatible

### Step 19 — Add security rules to §20

From `.github/instructions/security.instructions.md`:

- Validate on both client AND server
- Never string-concatenate DB queries — always use Drizzle query builders
- Rate limiting for API routes
- Never expose stack traces in production
- Escape user-generated content (XSS prevention)
- Don't store sensitive data in localStorage/sessionStorage

### Step 20 — Add testing conventions to §17

From `.github/instructions/testing.instructions.md`:

- Include accessibility checks in component tests
- Use `.env.test` for test configuration
- Tests must clean up after themselves
- Mock auth for unit tests, real auth for E2E
- Use Vitest built-in assertions

### Step 21 — Document React Compiler conflict

Note in §14: `performance.instructions.md` says "Use `React.memo` for expensive components" which **directly contradicts** the React Compiler rule. The setup prompt is authoritative — `memo()`, `useMemo`, `useCallback` are forbidden. The performance instructions file needs updating.

---

## Phase 4: Add Missing Commands & Workflows (4 items)

### Step 22 — Add missing commands to §2

```bash
# ── Database (additional) ──
pnpm db:generate                 # Generate migration SQL files from schema changes
pnpm db:migrate                  # Run migration files (production)
pnpm db:reset                    # Drop + regenerate + push (dev only!)
pnpm db:migration-status         # Check current migration status
pnpm type-gen                    # next typegen (runs automatically in prebuild/predev)

# ── Seeding (additional) ──
pnpm seed:validate               # Dry-run validation only
pnpm seed:clear                  # Clear all seeded data
pnpm seed:reset                  # Delete + reseed (full reset)
```

### Step 23 — Add full seed CLI flags to §8

```bash
--dry-run                        # Validate without writing (already documented)
--verbose                        # Detailed output (already documented)
--image-strategy=urls|local|imagekit  # Image handling (already documented)
--batch-size=N                   # Records per batch (already documented)
--concurrency=N                  # Parallel batch limit (default: 3)
--skip-validation                # Skip Zod validation (dangerous)
--no-transaction                 # Disable per-batch transactions
--force                          # Upsert mode (onConflictDoUpdate)
```

### Step 24 — Add seed REST API request body schema to §8

```json
{
  "entities": "all" | "comics" | "chapters" | "...",
  "options": {
    "batchSize": 100,
    "concurrency": 3,
    "verbose": false,
    "dryRun": false,
    "skipValidation": false,
    "useTransaction": true,
    "forceOverwrite": false,
    "imageStrategy": "urls"
  }
}
```

Note: In production, seed API endpoints require admin role authentication (401 without it).

### Step 25 — Document setup automation scripts

```bash
# Automated dev environment setup
bash scripts/setup-dev.sh        # Linux/macOS
.\scripts\setup-dev.ps1          # Windows PowerShell
```

---

## Phase 5: Add Missing Patterns (8 items)

### Step 26 — Add Next.js 16 `searchParams` pattern to §14

In Next.js 16, `searchParams` is a **Promise** that must be `await`ed:

```typescript
// ❌ WRONG (Next.js 15 pattern)
export default function Page({
  searchParams
}: {
  searchParams: { page?: string };
}) {
  const page = searchParams.page;
}

// ✅ CORRECT (Next.js 16)
export default async function Page({
  searchParams
}: {
  searchParams: Promise<{ page?: string }>;
}) {
  const params = await searchParams;
  const page = params.page;
}
```

### Step 27 — Add cascade delete scenarios to §4

| Scenario | Cascades To | Exception |
| --- | --- | --- |
| **Delete User** | bookmark, rating, comment, readingProgress, notification, readerSettings, userPreference | `auditLog.userId` → SET NULL (not cascade) |
| **Delete Comic** | chapter, bookmark, rating, comment, comicToGenre, comicImage, readingProgress | — |
| **Delete Chapter** | chapterImage, readingProgress (for that chapter) | `bookmark.lastReadChapterId` → SET NULL |

### Step 28 — Add N+1 anti-pattern catalog to §6

| Trap | Wrong | Right |
| --- | --- | --- |
| Comics + Authors | `for (comic of comics) { await getAuthor(comic.authorId) }` | `.with({ author: true })` |
| Bookmarks + Comics + Genres | Loop through bookmarks, fetch each comic | `db.query.bookmark.findMany({ with: { comic: { with: { genres: true } } } })` |
| Comment Threading | `comment.parentId` has no FK ref — can't use `.with()` | Manual SQL JOIN or add `relations()` to schema |
| Reading Progress Dashboard | Separate queries for each stat | `count()`, `sum()`, `avg()` in single aggregate query |

### Step 29 — Add pagination metadata shape

```typescript
interface PaginatedResponse<T> {
  success: boolean;
  data: T[];
  meta: {
    page: number;
    limit: number;
    total: number;
    totalPages: number;
    hasNextPage: boolean;
    hasPrevPage: boolean;
  };
}
```

### Step 30 — Add feature discovery checklist to §16

Before implementing any feature, answer:

1. **What entity/entities are involved?** → Check `schema.ts` for existing tables
2. **What relationships exist?** → Check FK references + junction tables
3. **What validation rules apply?** → Define/check Zod schemas (create + update split)
4. **What auth level is required?** → Public, authenticated, admin, or role-based
5. **What cache paths need invalidation?** → List all `revalidatePath()` targets
6. **Does a DAL already exist?** → Check `src/dal/` for existing implementations
7. **Are there composite keys?** → Override BaseDal methods to redirect (e.g., `"Use getUserRating(userId, comicId) instead"`)
8. **What tests are needed?** → Unit (mock DB/auth), integration (real DB), E2E (Playwright)

### Step 31 — Add missing env vars to §3

```bash
# Required for NextAuth
AUTH_URL="http://localhost:3000"          # Base URL for auth callbacks

# OAuth — Keycloak (optional)
KEYCLOAK_CLIENT_ID="comicwise"
KEYCLOAK_CLIENT_SECRET="your_secret"
KEYCLOAK_ISSUER="https://keycloak.example.com/realms/comicwise"

# Image CDN — ImageKit (optional, for imagekit seed strategy)
IMAGEKIT_PUBLIC_KEY="..."
IMAGEKIT_PRIVATE_KEY="..."
IMAGEKIT_URL_ENDPOINT="https://ik.imagekit.io/youraccount"
```

Mark which are active vs commented in `env.ts`.

### Step 32 — Add client-side `signIn()` patterns to §5

```typescript
// Client Component — OAuth sign-in
import { signIn } from "next-auth/react";
await signIn("github", { redirectTo: "/dashboard" });

// Client Component — Credentials sign-in (no redirect, handle in-page)
const result = await signIn("credentials", {
  username: "user",
  password: "pass",
  redirect: false
});
if (result?.error) showError(result.error);
```

### Step 33 — Document `appConfig.ts` current state

Most sections are stubs (providers, email, redis, imageKit, cloudinary, sentry all commented out). Active sections:

- `database` — `url`, `neonUrl`
- `auth` — `secret` only
- `app` — `name: "ComicWise"`, `url`, `environment`, `debug`

All other fields are placeholder comments for future integration.

---

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

## Verification Checklist

- [ ] Cross-check every table name against actual `src/database/schema.ts` (27 tables verified)
- [ ] Cross-check every command against `package.json` scripts
- [ ] Validate env var list against active + commented fields in `src/lib/env.ts`
- [ ] Verify all DAL query patterns match actual code (`db.query.*.findMany/findFirst` with `.with()` primary; `db.select()` for simple lookups)
- [ ] Confirm all instruction file conventions are accurately merged
- [ ] Run `pnpm type-check` after implementation
- [ ] Run `pnpm lint:fix` after implementation

---

## Decisions Log

| Decision | Rationale |
| --- | --- |
| **Model:** Keep "Claude Haiku 4.5 (copilot)" | User preference |
| **`comic.rating` dual-type:** Document both columns | `comic.rating` = decimal(10,1), `rating.rating` = integer — prevents confusion |
| **Raw `process.env` in auth:** Document as known exception | Auth files load before app init; pragmatic choice |
| **No Drizzle `relations()`:** Flag prominently in §6 + §21 | Explain FK inference works for simple cases, list what breaks (parentId, custom names) |
| **RBAC tables:** Document as present in schema | Available for use — don't write aspirational middleware |
| **React Compiler conflict:** Setup prompt is authoritative | Flag performance instructions as needing update |
| **All code samples:** Real, not aspirational | Only include patterns verified in actual source files |
| **Estimated final size:** ~1200-1400 lines (up from 824) | Significant expansion justified by discovered gaps |

---

## Sources Analyzed

| Source | Files Read | Key Findings |
| --- | --- | --- |
| `.github/prompts/setup.prompt.md` | 1 (824 lines) | Existing 20-section prompt — baseline |
| `.github/instructions/*.md` | 7 files | 35+ conventions missing from setup prompt |
| `docs/*.md` | 9 files | Gaps in schema, auth, seeding, feature patterns |
| `src/database/schema.ts` | 1 (604 lines) | 27 tables, 4 enums, no `relations()`, soft delete, JSONB settings |
| `src/dal/*.ts` | 18 files | `db.query.*` with `.with()` primary pattern; `db.select()` for simple lookups |
| `src/auth*.ts` + `proxy.ts` | 5 files | Raw `process.env` violations, proxy only guards `/dashboard` |
| `src/lib/env.ts` | 1 (165 lines) | Only 6 active validations, 60+ commented |
| `package.json` | 1 | Zod v4, Zustand v5, Vitest v4, Commander in devDeps |
| `next.config.ts` | 1 (174 lines) | staleTimes, staticGeneration tuning, webpack polyfill fallbacks |
| `appConfig.ts` | 1 (101 lines) | Mostly empty stubs |
| `.references/comicr/*` | 5 files | Architecture blueprint, RBAC, requirements, system patterns |
| `.references/comicwise/*` | 2 files | Architecture, onboarding patterns |
| `eslint.config.mts` | 1 (39 lines) | Only 3 active rules, plugins registered without rules |
