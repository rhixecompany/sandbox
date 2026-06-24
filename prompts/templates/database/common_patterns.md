# Common Patterns

> Extracted from `database.prompt.md`.

## Common Patterns

### Get Comic with All Details

```typescript
const comic = await db.query.comic.findFirst({
  where: eq(comic.slug, "comic-title"),
  with: {
    author: true,
    artist: true,
    type: true,
    genres: { with: { genre: true } },
    chapters: { orderBy: [c => desc(c.chapterNumber)] }
  }
});
```

### Get User's Bookmarks

```typescript
const bookmarks = await db.query.bookmark.findMany({
  where: eq(bookmark.userId, userId),
  with: { comic: true, lastReadChapter: true },
  orderBy: b => desc(b.updatedAt)
});
```

### Get Reading Progress

```typescript
const progress = await db.query.readingProgress.findFirst({
  where: and(
    eq(readingProgress.userId, userId),
    eq(readingProgress.comicId, comicId)
  ),
  with: { chapter: true }
});
```
