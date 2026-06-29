# Phase 5: Add Missing Patterns (8 items)

> Extracted from `plan-updateAiAgentSetupPrompt2.prompt.md`.

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
