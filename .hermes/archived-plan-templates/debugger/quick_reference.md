# Quick Reference

> Extracted from `debugger.prompt.md`.

## Quick Reference

### Key Tables at a Glance

| Table | Purpose | Key Constraint | Cascades To |
| --- | --- | --- | --- |
| `user` | User accounts | Email unique, UUID PK | 10+ tables (account, session, bookmark, comment, etc.) |
| `comic` | Comic entries | Title/slug unique | chapter, comicImage, comicToGenre, bookmark, rating, readingProgress |
| `chapter` | Comic chapters | (comicId, chapterNumber) unique | chapterImage, readingProgress, comment |
| `bookmark` | User's reading list | Composite (userId, comicId) | None (idempotent upserts) |
| `readingProgress` | Reading position | Per (user, comic) pair | None (update-only) |
| `comment` | Thread discussions | With parentId for replies | None (soft delete via deletedAt) |
| `notification` | User alerts | Linked to comic/chapter | None (can link to deleted records) |

### Common Query Patterns

```typescript
// Get comic with full details
const comic = await db.query.comic.findFirst({
  where: eq(comic.slug, "comic-title"),
  with: {
    author: true,
    artist: true,
    genres: { with: { genre: true } },
    chapters: { orderBy: [c => desc(c.chapterNumber)] }
  }
});

// Get user's bookmarks
const bookmarks = await db.query.bookmark.findMany({
  where: eq(bookmark.userId, userId),
  with: { comic: true, lastReadChapter: true },
  orderBy: b => desc(b.updatedAt)
});

// Get reading progress
const progress = await db.query.readingProgress.findFirst({
  where: and(
    eq(readingProgress.userId, userId),
    eq(readingProgress.comicId, comicId)
  ),
  with: { chapter: true }
});
```

### Critical Rules ⚠️

- ✅ Always use Drizzle `with()` for relationships - never loop and query individually
- ✅ Filter deleted users: `WHERE deletedAt IS NULL`
- ✅ Use composite keys for idempotent operations: `(userId, comicId)`
- ✅ All foreign keys use `onDelete: "cascade"` for referential integrity
- ✅ Update `updatedAt` on every mutation

---
