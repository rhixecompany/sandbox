# Query Patterns & N+1 Solutions

> Extracted from `debugger.prompt.md`.

## Query Patterns & N+1 Solutions

### Problem 1: Comics with Authors (N+1)

```typescript
// ❌ N+1 PROBLEM: 101 queries for 100 comics
const comics = await db.select().from(comic);
for (const c of comics) {
  c.author = await db
    .select()
    .from(author)
    .where(eq(author.id, c.authorId));
}

// ✅ SOLUTION: Single query with eager loading
const comicsWithAuthors = await db.query.comic.findMany({
  with: {
    author: true,
    artist: true,
    type: true,
    genres: true
  }
});
// Result: 1-2 queries max
```

---

### Problem 2: Bookmarks with Comic + Genres (N+1)

```typescript
// ❌ N+1 PROBLEM: 41 queries for 20 bookmarks
const bookmarks = await db
  .select()
  .from(bookmark)
  .where(eq(bookmark.userId, userId));
for (const b of bookmarks) {
  b.comic = await db
    .select()
    .from(comic)
    .where(eq(comic.id, b.comicId));
  b.comic.genres = await db
    .select()
    .from(comicToGenre)
    .leftJoin(genre, eq(comicToGenre.genreId, genre.id))
    .where(eq(comicToGenre.comicId, b.comicId));
}

// ✅ SOLUTION: Single joined query with eager loading
const bookmarksWithComics = await db.query.bookmark.findMany({
  where: eq(bookmark.userId, userId),
  with: {
    comic: {
      with: {
        author: true,
        artist: true,
        genres: { with: { genre: true } }
      }
    },
    lastReadChapter: true
  },
  orderBy: b => desc(b.updatedAt)
});
```

---

### Problem 3: Comments with Users (Exponential Queries)

```typescript
// ❌ N+1 PROBLEM: Exponential for threaded replies
const comments = await db.select().from(comment)
  .where(eq(comment.chapterId, chapterId));
for (const c of comments) {
  c.user = await db.select().from(user)
    .where(eq(user.id, c.userId));
  if (c.parentId) {
    c.parent = await db.select().from(comment)
      .where(eq(comment.id, c.parentId));
    c.parent.user = ...  // Another query
  }
}

// ✅ SOLUTION: Use eager loading with nesting
const comments = await db.query.comment.findMany({
  where: eq(comment.chapterId, chapterId),
  with: {
    user: { columns: { id: true, name: true, image: true } },
    parent: { with: { user: true } }
  }
});
```

---

### Performance Index Strategy

| Table | Index | Columns | Purpose |
| --- | --- | --- | --- |
| `user` | userEmailIdx | email | Auth login |
| `comic` | comicSlugIdx | slug | URL lookups |
| `comic` | comicStatusIdx | status | Filter by status |
| `chapter` | chapterComicIdIdx | comicId | Get chapters for comic |
| `chapter` | chapterComicChapterIdx | (comicId, chapterNumber) | Get specific chapter |
| `bookmark` | bookmarkUserIdIdx | userId | Get user's bookmarks |
| `readingProgress` | readingProgressUserComicIdx | (userId, comicId) | Get progress for comic |
| `comment` | commentChapterIdIdx | chapterId | Comments on chapter |
| `notification` | notificationUserReadIdx | (userId, read) | Get unread notifications |

**✨ GOLDEN RULE:** If your WHERE clause includes a column not indexed, queries will full-table scan.

---
