# Special Patterns

> Extracted from `debugger.prompt.md`.

## Special Patterns

### Idempotent Operations (Bookmarks)

```typescript
export async function addBookmarkAction(input: unknown) {
  const parsed = CreateBookmarkSchema.safeParse(input);
  if (!parsed.success) return { ok: false, error: "Invalid" };

  // Use onConflictDoUpdate to avoid duplicate entries
  const [result] = await db
    .insert(bookmark)
    .values(parsed.data)
    .onConflictDoUpdate({
      target: [bookmark.userId, bookmark.comicId],
      set: { status: parsed.data.status, updatedAt: new Date() }
    })
    .returning();

  return { ok: true, data: result };
}
```

---

### Soft Deletes

For data you want to preserve (comments, users):

```typescript
const visibleComments = await db
  .select()
  .from(comment)
  .where(
    and(
      eq(comment.chapterId, chapterId),
      isNull(comment.deletedAt) // Only non-deleted
    )
  );
```

---
