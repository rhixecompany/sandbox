# Phase 3: TypeScript & Auth Fixes (9 edits — HARD GATE)

> Extracted from `plan-comicWiseImplementation.prompt.md`.

## Phase 3: TypeScript & Auth Fixes (9 edits — HARD GATE)

> Run `pnpm type-check` after each fix. Must reach 0 errors before Phase 4.

### Fix 1 — `src/dal/bookmark-dal.ts`

**Problem:** `extends BaseDal<typeof bookmark>` (raw table type, not row type). Missing singleton.

```ts
// Replace type
type BookmarkType = typeof bookmark.$inferSelect;
export class BookmarkDal extends BaseDal<BookmarkType> {
  // fix getById to return BookmarkType | null
  async getById(id: number): Promise<BookmarkType | null> {
    const result = await db
      .select()
      .from(bookmark)
      .where(eq(bookmark.id, id))
      .limit(1);
    return result[0] ?? null;
  }
}
// Add at bottom:
export const bookmarkDal = new BookmarkDal();
```

### Fix 2 — `src/dal/chapter-dal.ts`

**Problem:** Missing `.$inferSelect`, orderBy callbacks may be incorrect. Missing singleton.

```ts
import { chapter, chapterImage } from "@/database/schema";
type ChapterType = typeof chapter.$inferSelect;
export class ChapterDal extends BaseDal<ChapterType> {
  async list(options?: DalOptions & { comicId?: number }) {
    return db.query.chapter.findMany({
      where: options?.comicId
        ? eq(chapter.comicId, options.comicId)
        : undefined,
      limit: options?.limit ?? 20,
      offset: options?.offset ?? 0,
      orderBy: (c, { asc }) => [asc(c.chapterNumber)],
      with: {
        images: { orderBy: (i, { asc }) => [asc(i.pageNumber)] }
      }
    });
  }
}
export const chapterDal = new ChapterDal();
```

### Fix 3 — `src/dal/comic-dal.ts`

**Problem:** Missing `ComicStatusEnum` cast, missing singleton export.

```ts
import { comic, comicStatus } from "@/database/schema";
type ComicType = typeof comic.$inferSelect;
type ComicStatusEnum = (typeof comicStatus.enumValues)[number];

// In filterByStatus:
async filterByStatus(status: ComicStatusEnum) {
  return db.select().from(comic).where(eq(comic.status, status as ComicStatusEnum));
}
// Add at bottom:
export const comicDal = new ComicDal();
```

### Fix 4 — `src/dal/rating-dal.ts`

**Problem:** SQL template strings use `score` but column is `rating`.

```ts
// getComicRatingStats — change ALL occurrences:
// AVG(score)  →  AVG(rating)
// score = 5   →  rating = 5
// score = 4   →  rating = 4
// etc.

// getTopRatedComics — same fix:
// AVG(score)  →  AVG(rating)
```

### Fix 5 — `src/dal/comment-dal.ts`

**Problem:** Missing singleton.

```ts
// Add at bottom:
export const commentDal = new CommentDal();
```

### Fix 6 — `src/actions/bookmark.actions.ts`

**Problem:** `const conditions: any[] = [...]`

```ts
import { SQL, and, eq, inArray } from "drizzle-orm";
// Replace:
const conditions: SQL[] = [];
// Replace all `as any` casts with proper ComicStatusEnum or typed casts
```

### Fix 7 — `src/auth-config.ts` ⚠️ CRITICAL

**Problem:** `signIn` blocks all users; `redirect` hardcodes `/dashboard`.

```ts
// signIn callback — REPLACE:
async signIn({ user }) {
  if (!user?.email) return false;
  return true; // allow any authenticated user
},

// redirect callback — REPLACE:
async redirect({ url, baseUrl }) {
  if (url.startsWith("/")) return `${baseUrl}${url}`;
  if (new URL(url).origin === baseUrl) return url;
  return `${baseUrl}/dashboard`;
},
```

### Fix 8 — `src/components/ui/chart.tsx`

**Problem:** `(item: any)` untyped parameter.

```ts
// Replace:
// eslint-disable-next-line @typescript-eslint/no-explicit-any
(item: Record<string, unknown>) =>
```

### Fix 9 — `src/actions/comic.actions.ts`

**Problem:** `any[]` conditions, missing update/delete actions.

```ts
import { SQL, and, eq, ilike, inArray } from "drizzle-orm";
type ComicStatusEnum = (typeof comicStatus.enumValues)[number];

// Replace conditions array:
const conditions: SQL[] = [];

// Fix status cast:
eq(comic.status, dbStatus as ComicStatusEnum);

// Add missing actions:
export async function updateComicAction(
  id: number,
  input: unknown
): Promise<ActionResult<ComicType>> {
  const session = await auth();
  if (!session?.user)
    return { ok: false, error: "Not authenticated" };
  const parsed = UpdateComicSchema.safeParse(input);
  if (!parsed.success)
    return {
      ok: false,
      error: parsed.error.errors[0]?.message ?? "Invalid"
    };
  try {
    const comic = await comicDal.update(id, parsed.data);
    if (!comic) return { ok: false, error: "Comic not found" };
    revalidatePath("/comics");
    revalidatePath(`/comics/${id}`);
    return { ok: true, data: comic };
  } catch (e) {
    console.error("[updateComicAction]", e);
    return { ok: false, error: "Failed to update comic" };
  }
}

export async function deleteComicAction(
  id: number
): Promise<ActionResult<void>> {
  const session = await auth();
  const u = session?.user as { role?: unknown };
  if (typeof u?.role !== "string" || u.role !== "admin")
    return { ok: false, error: "Forbidden" };
  try {
    await comicDal.delete(id);
    revalidatePath("/comics");
    revalidatePath("/admin/comics");
    return { ok: true, data: undefined };
  } catch (e) {
    console.error("[deleteComicAction]", e);
    return { ok: false, error: "Failed to delete comic" };
  }
}
```

**Gate:** `pnpm type-check` → 0 errors before continuing.

---
