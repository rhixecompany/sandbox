# Critical Relationships & Cascades

> Extracted from `debugger.prompt.md`.

## Critical Relationships & Cascades

### Relationship 1: Comics → Chapters → Images

```
comic ──┬──→ chapter ──→ chapterImage
        │       ↑
        │       └─ readingProgress links here
        │
        └──→ comicImage

Deletion cascade (3 levels deep):
  DELETE comic (id=123)
    → DELETE chapter (comicId=123)
      → DELETE chapterImage (chapterId=*)
      → DELETE readingProgress (chapterId=*)
      → DELETE comment (chapterId=*)
    → DELETE bookmark (comicId=123)
    → DELETE rating (comicId=123)
```

**🔴 CRITICAL:** When deleting a comic, cascading is 3 levels deep. Always verify this is intentional.

---

### Relationship 2: Users → Bookmarks → Comics

```
user ──→ bookmark ──┬──→ comic
                    │
                    └──→ chapter (lastReadChapterId)

Common queries:
  # Get user's bookmarks
  SELECT b.* FROM bookmark b
  WHERE b.userId = 'user1'
  ORDER BY b.updatedAt DESC;

  # Get user's "currently reading" list with comic info
  SELECT b.*, c.title, c.coverImage
  FROM bookmark b
  JOIN comic c ON b.comicId = c.id
  WHERE b.userId = 'user1' AND b.status = 'Reading'
  ORDER BY b.updatedAt DESC;
```

**⚠️ N+1 TRAP:** Don't loop and query chapters individually. Use eager loading with `with()`.

---

### Relationship 3: Users → Comments → Chapters

```
user ──→ comment ──→ chapter
                       ↓
                     comic

Threaded comments:
  comment.parentId → comment.id (self-reference for replies)

Query all comments on chapter:
  SELECT c.id, c.content, c.userId, u.name, c.parentId, c.createdAt
  FROM comment c
  JOIN user u ON c.userId = u.id
  WHERE c.chapterId = 42
  ORDER BY c.createdAt ASC;
```

---

### Cascade Delete Scenarios

#### Scenario 1: Delete User

```
DELETES:
  ✓ user record
  ✓ account, session, authenticator (→ user.id)
  ✓ bookmark, comment, rating, readingProgress (→ user.id)
  ✓ readerSettings, notification, userRole (→ user.id)
  ✓ auditLog entries (SET NULL, oldValues preserved)

Impact: User's ENTIRE interaction history is GONE
Action: Consider soft-delete (set deletedAt) instead
```

#### Scenario 2: Delete Comic

```
DELETES (3-level cascade):
  ✓ comic record
  ✓ comicImage, comicToGenre (→ comic.id)
  ✓ chapter (→ comic.id)
    → chapterImage (→ chapter.id)
    → readingProgress (→ chapter.id)
    → comment (→ chapter.id)
  ✓ bookmark, rating (→ comic.id)
  ✓ notification (links to this comic)

Cascade depth: 3 levels
```

#### Scenario 3: Delete Chapter

```
DELETES:
  ✓ chapter record
  ✓ chapterImage, readingProgress, comment (→ chapter.id)

UPDATES (not cascade):
  ⚠️ bookmark.lastReadChapterId = NULL if set
  ⚠️ notification.chapterId = NULL if linked

Note: Intentional design - bookmark survives, just loses position
```

---
