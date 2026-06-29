# Verified Codebase State

> Extracted from `plan-comicWiseImplementation.prompt.md`.

## Verified Codebase State

### Project

- **Framework:** Next.js 16.1.6 App Router, Turbopack, React Compiler
- **ORM:** Drizzle + PostgreSQL (Neon)
- **Auth:** NextAuth v5, strategy: "database"
- **Package Manager:** pnpm
- **Location:** `c:\Users\Alexa\Desktop\SandBox\comicbook`

### Schema Enums (verified from `src/database/schema.ts`)

```ts
userRole: "user" | "admin" | "moderator";
comicStatus: "Ongoing" |
  "Hiatus" |
  "Completed" |
  "Dropped" |
  "Season End" |
  "Coming Soon";
resourceEnum: defined in schema;
actionEnum: defined in schema;
```

### Schema Tables (30+ tables verified)

**Auth:** `user`, `account`, `session`, `verificationToken`, `authenticator`, `passwordResetToken` **Content:** `type`, `author`, `artist`, `genre`, `comic`, `chapter`, `comicImage`, `chapterImage`, `comicToGenre` **User Data:** `bookmark` (PK: userId+comicId, `status` text default "Reading", `lastReadChapterId`), `comment`, `readingProgress` (`scrollPercentage`, `progressPercent`, `currentImageIndex`), `readerSettings`, `rating` (**column is `rating` integer, NOT `score`**), `notification` **RBAC:** `role`, `permission`, `rolePermission`, `userRole2` (table "userRole"), `auditLog` **Prefs:** `userPreference` (theme, defaultLayout, pageNavigationStyle, fontSize, notification prefs, privacy prefs)

### Confirmed Bugs

1. `src/auth-config.ts` `signIn` callback — blocks all real users (only allows `@comicwise.app`)
2. `src/auth-config.ts` `redirect` callback — hardcodes `/dashboard`, breaks all URL intent
3. `src/dal/rating-dal.ts` — uses `score` column in SQL; correct column is `rating`
4. `src/dal/bookmark-dal.ts` + `chapter-dal.ts` — `extends BaseDal<typeof table>` missing `.$inferSelect`
5. `src/dal/comment-dal.ts` — missing singleton export `commentDal`
6. `src/actions/bookmark.actions.ts` — `const conditions: any[] = [...]`
7. `src/actions/comic.actions.ts` — `const conditions: any[] = []`, `as any` casts, missing update/delete actions
8. `src/stores/` — **DIRECTORY DOES NOT EXIST**
9. Route layouts missing: `(root)/layout.tsx`, `(auth)/layout.tsx`, `admin/layout.tsx`

### Confirmed Working Patterns

- `BaseDal<T>` abstract class in `src/dal/base-dal.ts` with `handleError()`, `DalOptions`
- `type XType = typeof x.$inferSelect` → `class XDal extends BaseDal<XType>`
- `ActionResult<T> = { ok: true; data: T } | { ok: false; error: string }`
- `layout-provider.tsx` wraps: `SessionProvider → QueryClientProvider → ThemeProvider → TooltipProvider → {children} → Toaster`
- `src/tests/` has only `example.spec.ts` + `fixtures/`

---
