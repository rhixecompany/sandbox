# Database Architecture Reference

> Extracted from `plan-dev.prompt.md`.

## Database Architecture Reference

### Key Tables & Relationships

| Table | Primary Purpose | Key Constraint | Cascades To |
| --- | --- | --- | --- |
| `user` | User accounts | Email unique | 10+ tables |
| `comic` | Comic entries | Title/slug unique | chapter, images, bookmarks, ratings |
| `chapter` | Comic chapters | (comicId, chapterNumber) unique | images, reading_progress, comments |
| `bookmark` | Reading list | Composite (userId, comicId) | None (idempotent) |
| `readingProgress` | Reading position | Per (user, comic) | None (update-only) |
| `comment` | Discussions | With parentId for replies | None (soft delete) |
| `notification` | User alerts | Linked to comic/chapter | None |

### Critical Query Patterns

```typescript
// Get comic with relationships
const comic = await db.query.comic.findFirst({
  where: eq(comic.slug, slug),
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
```

### N+1 Solution Pattern

```typescript
// ❌ WRONG: Loops and queries individually (N+1)
const comics = await db.select().from(comic);
for (const c of comics) {
  c.author = await db.select().from(author).where(...);
}

// ✅ CORRECT: Use .with() for eager loading
const comics = await db.query.comic.findMany({
  with: { author: true, genres: { with: { genre: true } } }
});
```

---
