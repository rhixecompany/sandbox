# ComicWise Database Context Map

**Purpose:** This document provides a complete reference for understanding the ComicWise database architecture, relationships, business logic, and query patterns. Use this when implementing features or debugging data flow issues.

**Last Updated:** March 1, 2026  
**Schema Version:** 1.0.0

---

## Table of Contents

1. [Entity Relationship Overview](#entity-relationship-overview)
2. [Entity Groups & Purposes](#entity-groups--purposes)
3. [Detailed Entity Reference](#detailed-entity-reference)
4. [Critical Relationships Explained](#critical-relationships-explained)
5. [Cascade Delete Scenarios](#cascade-delete-scenarios)
6. [N+1 Query Problems & Solutions](#n1-query-problems--solutions)
7. [Query Patterns & Examples](#query-patterns--examples)
8. [Performance Considerations](#performance-considerations)
9. [AI-Optimized Schema Reference](#ai-optimized-schema-reference)

---

## Entity Relationship Overview

```text
┌─────────────────────────────────────────────────────────────────┐
│                    COMIC CONTENT ECOSYSTEM                      │
├─────────────────────────────────────────────────────────────────┤
│                                                                 │
│  Type ─────────────┐                                            │
│  Author ───┐       ├──→ Comic ←──── ComicImage                 │
│  Artist ───┼───────┤     ↓                                      │
│  Genre ────┤       │   Chapter ←──── ChapterImage               │
│            └───┤   │     ↓                                      │
│            ComicToGenre  (Junction)                             │
│                                                                 │
│  ┌─────────────────────────────────────────────────────────────┤
│  │                   USER INTERACTION LAYER                     │
│  └─────────┬─────────────────────────────────────────────────────┤
│            │                                                     │
│  User ─────┼──→ Bookmark (userId, comicId) ← reading tracking   │
│    (auth)  │    Comment (userId, chapterId) ← discussions       │
│            │    Rating (userId, comicId) ← user ratings         │
│            │    ReadingProgress (userId, comic, chapter)        │
│            │    Notification (userId) ← alerts                  │
│            │    ReaderSettings (userId) ← UI preferences        │
│            │                                                     │
│  Account ──→ account.userId → user.id (OAuth)                  │
│  Session ──→ session.userId → user.id (active sessions)        │
│                                                                 │
│  ┌─────────────────────────────────────────────────────────────┤
│  │              RBAC & AUDIT SYSTEM                              │
│  └─────────────────────────────────────────────────────────────┤
│    Role ←─→ Permission (many-to-many)                          │
│    User ←─→ Role (many-to-many)                                │
│    AuditLog (tracks all changes)                               │
│                                                                 │
└─────────────────────────────────────────────────────────────────┘
```

---

## Entity Groups & Purposes

### **Group 1: Authentication & Authorization**

| Entity | Purpose | Key Constraint |
| --- | --- | --- |
| `user` | User accounts with settings | Email unique, UUID primary key |
| `account` | OAuth provider links | Links to user via userId |
| `session` | Active login sessions | Expires automatically |
| `verificationToken` | Email verification codes | Email-token unique pair |
| `authenticator` | WebAuthn/2FA credentials | Per-user credential storage |
| `passwordResetToken` | Password reset links | One-time use token |
| `role` | Role definitions | Used with permission system |
| `permission` | Action permissions | Resource-action pair unique |
| `userRole` | User-role mapping | Many-to-many relationship |
| `rolePermission` | Role-permission mapping | Many-to-many relationship |

**Critical Pattern:** User deletion cascades to all dependent records (account, session, bookmarks, comments, etc.)

---

### **Group 2: Comic Content**

| Entity | Purpose | Key Constraint |
| --- | --- | --- |
| `type` | Comic type (manga, manhwa, etc.) | Name unique |
| `author` | Comic authors | Name unique |
| `artist` | Comic artists | Name unique |
| `genre` | Content genres | Name and slug unique |
| `comic` | Main comic entries | Title and slug unique per comic |
| `comicImage` | Cover/preview images | Ordered, unique URL |
| `comicToGenre` | Comic-genre mapping | Composite primary key |
| `chapter` | Comic chapters | Composite unique: (comicId, chapterNumber) |
| `chapterImage` | Chapter pages | Composite unique: (chapterId, pageNumber) |

**Critical Pattern:** Deleting a comic cascades to all chapters, chapter images, bookmarks, and reading progress.

---

### **Group 3: User Interactions**

| Entity | Purpose | Key Constraint |
| --- | --- | --- |
| `bookmark` | User's comic reading list | Composite key: (userId, comicId), optional lastReadChapterId |
| `comment` | Thread discussions per chapter | Supports replies via parentId |
| `rating` | User comic ratings (1-5 stars) | Composite unique: (userId, comicId) |
| `readingProgress` | Detailed reading position | Linked to comic AND chapter |
| `readerSettings` | Per-user reader preferences | One-to-one with user |
| `notification` | User alerts/messages | Can link to comic or chapter |

**Critical Pattern:** All user data is tied to userId via cascade delete.

---

### **Group 4: Audit & Logging**

| Entity | Purpose | Key Constraint |
| --- | --- | --- |
| `auditLog` | Complete action history | JSON fields for details, oldValues, newValues |

---

## Detailed Entity Reference

### **USER TABLE**

```typescript
user: {
  id: text (UUID, primary key),
  name: text (nullable),
  email: text (UNIQUE, NOT NULL),
  emailVerified: timestamp (nullable),
  image: text (profile picture),
  password: text (bcrypt hash, nullable for OAuth-only users),
  role: userRole enum (user | admin | moderator, default: user),
  status: boolean (account active/inactive),
  settings: jsonb {
    emailNotifications?: boolean,
    profileVisibility?: 'private' | 'public',
    readingHistoryVisibility?: boolean
  },
  deletedAt: timestamp (soft delete, nullable),
  createdAt: timestamp,
  updatedAt: timestamp
}

Indexes: userEmailIdx, userRoleIdx
```

**🔴 COMMON MISTAKE:** Forgetting that deleted users (deletedAt IS NOT NULL) should be filtered in queries.

---

### **COMIC TABLE**

```typescript
comic: {
  id: serial (primary key),
  title: text (UNIQUE),
  slug: text (UNIQUE, URL-friendly),
  description: text,
  coverImage: text (image URL),
  status: comicStatus enum (Ongoing | Hiatus | Completed | Dropped | Season End | Coming Soon),
  publicationDate: timestamp,
  rating: decimal(10,1) (aggregate rating, default 0),
  views: integer (view counter, default 0),
  url: text (nullable, external source),
  serialization: text (nullable, serialization info),
  authorId: integer (foreign key → author.id),
  artistId: integer (foreign key → artist.id),
  typeId: integer (foreign key → type.id),
  createdAt: timestamp,
  updatedAt: timestamp,
  searchVector: text (for full-text search)
}

Indexes: 9 indexes covering slug, title, status, rating, views, dates, and foreign keys
Unique: title, slug
```

**⚠️ IMPORTANT:** Use `comicSlugIdx` for lookups. Slug is the primary query parameter in URLs.  
**⚠️ IMPORTANT:** `rating` is a decimal, not computed - it's stored for performance. Update via trigger or explicit calculation.

---

### **CHAPTER TABLE**

```typescript
chapter: {
  id: serial (primary key),
  slug: text (UNIQUE),
  title: text,
  chapterNumber: integer (release order),
  releaseDate: timestamp,
  comicId: integer (foreign key → comic.id, CASCADE DELETE),
  views: integer (default 0),
  url: text (nullable, external source),
  content: text (chapter description),
  createdAt: timestamp,
  updatedAt: timestamp
}

Indexes: chapterSlugIdx, chapterComicIdIdx, chapterNumberIdx, chapterComicChapterIdx
Unique: slug, (comicId, chapterNumber) ← CRITICAL for upserts
```

**🔴 CRITICAL:** The composite unique constraint `(comicId, chapterNumber)` is essential:

- Prevents duplicate chapter numbers for same comic
- Enables idempotent `onConflictDoUpdate` in seeding/imports
- Used heavily in queries: "Get chapter 25 of comic X"

---

### **BOOKMARK TABLE**

```typescript
bookmark: {
  userId: text (foreign key → user.id, CASCADE DELETE),
  comicId: integer (foreign key → comic.id, CASCADE DELETE),
  lastReadChapterId: integer (nullable, foreign key → chapter.id),
  status: text (Reading, Plan to Read, Completed, On Hold, Dropped),
  notes: text (user notes),
  createdAt: timestamp,
  updatedAt: timestamp
}

Primary Key: Composite (userId, comicId)
Indexes: bookmarkUserIdIdx, bookmarkComicIdIdx
```

**✨ CLEVER DESIGN:** Composite primary key prevents duplicates and makes updates idempotent:

```typescript
// Can safely call this multiple times - idempotent
INSERT INTO bookmark (userId, comicId, status)
  VALUES ('user1', 123, 'Reading')
ON CONFLICT (userId, comicId) DO UPDATE
  SET status = EXCLUDED.status, updatedAt = NOW();
```

---

### **READING PROGRESS TABLE**

```typescript
readingProgress: {
  id: serial (primary key),
  userId: text (foreign key → user.id, CASCADE DELETE),
  comicId: integer (foreign key → comic.id, CASCADE DELETE),
  chapterId: integer (foreign key → chapter.id, CASCADE DELETE),
  pageNumber: integer (current page in chapter),
  scrollPosition: integer (pixel scroll position),
  currentImageIndex: integer (current image in chapter),
  scrollPercentage: integer (0-100),
  totalPages: integer (pages in chapter),
  progressPercent: integer (0-100, how far through comic),
  completedAt: timestamp (nullable, when finished reading),
  lastReadAt: timestamp (tracks reading activity),
  createdAt: timestamp,
  updatedAt: timestamp
}

Indexes: userId, comicId, chapterId, lastReadAt, (userId, comicId)
```

**📊 ANALYTICS:** `lastReadAt` and `progressPercent` enable:

- "Recently read" feed
- Progress bar in UI
- "Continue reading" resume point
- Engagement tracking

---

### **NOTIFICATION TABLE**

```typescript
notification: {
  id: serial (primary key),
  userId: text (foreign key → user.id, CASCADE DELETE),
  type: text (new_chapter | comment_reply | system | ...),
  title: text,
  message: text,
  link: text (nullable, URL to navigate to),
  read: boolean (default false),
  comicId: integer (nullable, foreign key → comic.id),
  chapterId: integer (nullable, foreign key → chapter.id),
  createdAt: timestamp
}

Indexes: userId, read, type, createdAt, (userId, read)
```

**🔔 PATTERNS:**

- **New chapter:** type='new_chapter', comicId set, link to chapter
- **Comment reply:** type='comment_reply', chapterId set, link to comment
- Query unread: `WHERE userId = ? AND read = false`

---

### **ROLE-BASED ACCESS CONTROL (RBAC)**

```typescript
role: {
  id: serial,
  name: text (UNIQUE),
  description: text,
  isSystem: boolean (true for system roles)
}

permission: {
  id: serial,
  name: text (UNIQUE),
  resource: resourceEnum (comic | chapter | user | comment | ...),
  action: actionEnum (create | read | update | delete | manage),
  Unique constraint: (resource, action)
}

rolePermission: {
  roleId: integer → role.id,
  permissionId: integer → permission.id,
  Primary key: (roleId, permissionId)
}

userRole: {
  userId: text → user.id,
  roleId: integer → role.id,
  assignedAt: timestamp,
  assignedBy: text (nullable, who assigned this role),
  Primary key: (userId, roleId)
}
```

**🔐 LOOKUP PATTERN:**

```typescript
// Get all permissions for user 'user1'
SELECT DISTINCT p.resource, p.action
FROM permission p
JOIN rolePermission rp ON p.id = rp.permissionId
JOIN role r ON rp.roleId = r.id
JOIN userRole ur ON r.id = ur.roleId
WHERE ur.userId = 'user1';
```

---

## Critical Relationships Explained

### **1. Comics → Chapters → Chapter Images (Cascading Content)**

```text
comic ──┬──→ chapter ──→ chapterImage
        │       ↑
        │       └─ readingProgress links here
        │
        └──→ comicImage

Deletion cascade:
  DELETE comic (id=123)
    → DELETE chapter (comicId=123)
      → DELETE chapterImage (chapterId=*)
      → DELETE readingProgress (comicId=123)
    → DELETE bookmark (comicId=123)
    → DELETE rating (comicId=123)
    → DELETE comment (comicId in linked chapters)
```

**🔴 CRITICAL:** When you delete a comic:

1. All chapters disappear ✓ (cascaded)
2. All reading progress for that comic disappears ✓ (cascaded)
3. Bookmarks are cleaned up ✓ (cascaded)
4. But comments on those chapters... ⚠️ (comment.chapterId cascades)

**VERIFICATION:** These foreign keys use `onDelete: "cascade"`:

- chapter.comicId → comic.id
- chapterImage.chapterId → chapter.id
- comicImage.comicId → comic.id
- readingProgress.chapterId → chapter.id
- bookmark.comicId → comic.id
- comment.chapterId → chapter.id

---

### **2. Users → Bookmarks → Comic/Chapter (User's Library)**

```sql
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

  # Continue reading - get last read chapter
  SELECT b.lastReadChapterId, c.chapterNumber, c.title
  FROM bookmark b
  JOIN chapter c ON b.lastReadChapterId = c.id
  WHERE b.userId = 'user1' AND b.comicId = 123;
```

**⚠️ N+1 TRAP:** Don't loop and query chapters individually. Use JOIN.

---

### **3. Users → Comments (Discussion Threads)**

```sql
user ──→ comment ──→ chapter
                       ↓
                     comic

Threaded comments:
  comment.parentId → comment.id (self-reference for replies)

Query all comments on chapter 42:
  SELECT c.id, c.content, c.userId, u.name, c.parentId, c.createdAt
  FROM comment c
  JOIN user u ON c.userId = u.id
  WHERE c.chapterId = 42
  ORDER BY c.createdAt ASC;

Query top-level comments + their replies:
  SELECT * FROM comment
  WHERE chapterId = 42 AND parentId IS NULL
  UNION ALL
  SELECT * FROM comment
  WHERE chapterId = 42 AND parentId IS NOT NULL
  ORDER BY parentId NULLS FIRST, createdAt ASC;
```

---

### **4. Users → Reading Progress (Detailed Tracking)**

```sql
user ──→ readingProgress ──┬──→ comic
                           ├──→ chapter (current)
                           └──→ chapterImage (current image)

Single record per (user, comic) pair:
  SELECT * FROM readingProgress
  WHERE userId = 'user1' AND comicId = 123;

# Shows: current chapter, page, scroll position, percentage progress
```

---

### **5. Auth Tables (NextAuth)**

```text
user ──┬──→ account (OAuth providers)
       ├──→ session (active login sessions)
       ├──→ authenticator (WebAuthn/2FA)
       └──→ passwordResetToken (for password resets)

NextAuth adapter relies on:
  • account.userId
  • session.userId
  • Session expires when session.expires < NOW()
```

---

## Cascade Delete Scenarios

### **Scenario 1: Delete User (userId='user123')**

```text
DELETES:
  ✓ user record
  ✓ account (→ user.id)
  ✓ session (→ user.id)
  ✓ authenticator (→ user.id)
  ✓ bookmark (→ user.id)
  ✓ comment (→ user.id)
  ✓ rating (→ user.id)
  ✓ readingProgress (→ user.id)
  ✓ readerSettings (→ user.id)
  ✓ notification (→ user.id)
  ✓ userRole (→ user.id)
  ✓ auditLog entries (SET NULL, so oldValues preserved)

Impact: User's entire interaction history is GONE
Action: Consider soft-delete (set deletedAt) instead
```

---

### **Scenario 2: Delete Comic (comicId=456)**

```text
DELETES:
  ✓ comic record
  ✓ comicImage (→ comic.id)
  ✓ comicToGenre (→ comic.id)
  ✓ chapter (→ comic.id)
    → chapterImage (→ chapter.id)
    → readingProgress (→ chapter.id)
    → comment (→ chapter.id)
  ✓ bookmark (→ comic.id)
  ✓ rating (→ comic.id)
  ✓ notification (links to this comic)

Cascade depth: 3 levels (comic → chapter → chapterImage/comment/reading)
```

---

### **Scenario 3: Delete Chapter (chapterId=789)**

```text
DELETES:
  ✓ chapter record
  ✓ chapterImage (→ chapter.id)
  ✓ readingProgress (→ chapter.id)
  ✓ comment (→ chapter.id)

UPDATES (not cascade):
  ⚠️ bookmark.lastReadChapterId = NULL if it was set to this chapter
  ⚠️ notification.chapterId = NULL if linked to this chapter

Note: bookmark doesn't cascade on chapter delete (only comic delete cascades)
      This is intentional - user's bookmark stays, just loses position
```

---

## N+1 Query Problems & Solutions

### **Problem 1: Books with Authors (COMMON MISTAKE)**

```typescript
// ❌ N+1 QUERY PROBLEM
const comics = await db.select().from(comic); // Query 1
for (const c of comics) {
  c.author = await db
    .select()
    .from(author) // Query 2, 3, 4, ...
    .where(eq(author.id, c.authorId));
}
// If 100 comics: 1 + 100 = 101 queries!

// ✅ SOLUTION: Use JOIN
const comicsWithAuthors = await db
  .select({
    comic: comic,
    author: author
  })
  .from(comic)
  .leftJoin(author, eq(comic.authorId, author.id));
// Result: 1 query

// ✅ BETTER: Use Drizzle relations (with)
const comicsWithAuthors = await db.query.comic.findMany({
  with: {
    author: true,
    artist: true,
    type: true,
    genres: true
  }
});
// Result: 1-2 queries (depending on Drizzle's implementation)
```

---

### **Problem 2: Bookmarks with Comic + Genres**

```typescript
// ❌ N+1 PROBLEM
const bookmarks = await db
  .select()
  .from(bookmark)
  .where(eq(bookmark.userId, userId));
for (const b of bookmarks) {
  b.comic = await db
    .select()
    .from(comic)
    .where(eq(comic.id, b.comicId)); // Query per bookmark
  b.comic.genres = await db
    .select()
    .from(comicToGenre)
    .leftJoin(genre, eq(comicToGenre.genreId, genre.id))
    .where(eq(comicToGenre.comicId, b.comicId)); // Query per comic
}
// If 20 bookmarks: 1 + 20 + 20 = 41 queries!

// ✅ SOLUTION: Single joined query
const bookmarksWithComics = await db
  .select({
    bookmark: bookmark,
    comic: comic,
    genre: genre
  })
  .from(bookmark)
  .innerJoin(comic, eq(bookmark.comicId, comic.id))
  .leftJoin(comicToGenre, eq(comic.id, comicToGenre.comicId))
  .leftJoin(genre, eq(comicToGenre.genreId, genre.id))
  .where(eq(bookmark.userId, userId));

// Group results back into bookmarks with nested comics/genres
```

---

### **Problem 3: Comments with Users (Threads)**

```typescript
// ❌ N+1 PROBLEM
const comments = await db.select().from(comment)
  .where(eq(comment.chapterId, chapterId));
for (const c of comments) {
  c.user = await db.select().from(user)
    .where(eq(user.id, c.userId));  // Query per comment
  if (c.parentId) {
    c.parent = await db.select().from(comment)
      .where(eq(comment.id, c.parentId));  // Recursive query
    c.parent.user = ...  // Another query
  }
}
// Exponential queries!

// ✅ SOLUTION: Use with() for eager loading
const comments = await db.query.comment.findMany({
  where: eq(comment.chapterId, chapterId),
  with: {
    user: true,
    parent: {
      with: {
        user: true
      }
    }
  }
});
// Result: 1-2 queries max
```

---

### **Problem 4: Reading Progress with Comic + Chapter**

```typescript
// ❌ N+1 PROBLEM
const progress = await db.query.readingProgress.findMany({
  where: eq(readingProgress.userId, userId)
});
for (const p of progress) {
  p.comic = await db.query.comic.findFirst({
    // Query per progress
    where: eq(comic.id, p.comicId)
  });
  p.chapter = await db.query.chapter.findFirst({
    // Query per progress
    where: eq(chapter.id, p.chapterId)
  });
}

// ✅ SOLUTION: Drizzle with()
const progress = await db.query.readingProgress.findMany({
  where: eq(readingProgress.userId, userId),
  with: {
    comic: true,
    chapter: true
  }
});
```

---

## Query Patterns & Examples

### **Pattern 1: Get Comic Details (Full)**

```typescript
import { db } from "@/database/db";
import { eq } from "drizzle-orm";

const comicWithDetails = await db.query.comic.findFirst({
  where: eq(comic.slug, "my-comic-title"),
  with: {
    author: true,
    artist: true,
    type: true,
    genres: {
      with: {
        genre: true // Get genre details through junction
      }
    },
    chapters: {
      orderBy: [c => desc(c.chapterNumber)],
      limit: 30 // Only recent chapters
    }
  }
});

// Returns:
// {
//   id, title, description, ...,
//   author: { id, name, ... },
//   artist: { id, name, ... },
//   type: { id, name },
//   genres: [{ genreId, genre: { id, name } }, ...],
//   chapters: [{ id, number, title, ... }, ...]
// }
```

---

### **Pattern 2: Get User's Bookmarks for Home Feed**

```typescript
const bookmarksFeed = await db.query.bookmark.findMany({
  where: eq(bookmark.userId, userId),
  with: {
    comic: {
      with: {
        author: true,
        artist: true,
        genres: {
          with: { genre: true }
        }
      }
    },
    lastReadChapter: {
      columns: {
        id: true,
        chapterNumber: true,
        title: true,
        releaseDate: true
      }
    }
  },
  orderBy: b => desc(b.updatedAt),
  limit: 20
});

// Efficiently loads: bookmarks, linked comics with metadata, last read chapter
// Single query with proper eager loading
```

---

### **Pattern 3: Get Reading Progress (Continue Reading)**

```typescript
const currentProgress = await db.query.readingProgress.findFirst({
  where: and(
    eq(readingProgress.userId, userId),
    eq(readingProgress.comicId, comicId)
  ),
  with: {
    chapter: {
      with: {
        comic: true
      }
    }
  }
});

if (currentProgress && !currentProgress.completedAt) {
  // User has unfinished reading - can resume
  return {
    chapterId: currentProgress.chapterId,
    pageNumber: currentProgress.pageNumber,
    scrollPosition: currentProgress.scrollPosition,
    progressPercent: currentProgress.progressPercent
  };
}
```

---

### **Pattern 4: Get Chapter with Images (Reader)**

```typescript
const chapter = await db.query.chapter.findFirst({
  where: eq(chapter.slug, chapterSlug),
  with: {
    comic: {
      columns: {
        id: true,
        title: true,
        slug: true
      }
    },
    images: {
      orderBy: img => asc(img.pageNumber)
    }
  }
});

// Returns chapter + ordered images + comic metadata
// Images are ready to display in correct order
```

---

### **Pattern 5: Get Unread Notifications**

```typescript
const unreadNotifications = await db.query.notification.findMany({
  where: and(
    eq(notification.userId, userId),
    eq(notification.read, false)
  ),
  orderBy: n => desc(n.createdAt),
  limit: 50
});

// Mark as read
await db
  .update(notification)
  .set({ read: true })
  .where(
    and(eq(notification.userId, userId), eq(notification.read, false))
  );
```

---

### **Pattern 6: Get Chapter Comments (Threaded)**

```typescript
const comments = await db.query.comment.findMany({
  where: eq(comment.chapterId, chapterId),
  with: {
    user: {
      columns: {
        id: true,
        name: true,
        image: true,
        role: true
      }
    },
    parent: true // For thread replies
  },
  orderBy: c => asc(c.createdAt)
});

// Build tree structure in application:
// - Top-level: comment.parentId IS NULL
// - Replies: group by comment.parentId
```

---

### **Pattern 7: Recently Read (Last 30 Days)**

```typescript
const thirtyDaysAgo = new Date(Date.now() - 30 * 24 * 60 * 60 * 1000);

const recentlyRead = await db.query.readingProgress.findMany({
  where: and(
    eq(readingProgress.userId, userId),
    gte(readingProgress.lastReadAt, thirtyDaysAgo)
  ),
  with: {
    comic: {
      columns: {
        id: true,
        title: true,
        slug: true,
        coverImage: true
      }
    }
  },
  orderBy: rp => desc(rp.lastReadAt),
  limit: 20
});

// Great for "Previously read" or "Recent activity" feed
```

---

### **Pattern 8: Search Comics (Full-Text)**

```typescript
// Requires: tsVector column + GIN index (not shown in schema)
const searchResults = await db.query.comic.findMany({
  where: sql`searchVector @@ websearch_to_tsquery('${searchTerm}')`,
  limit: 20
});

// Simpler substring search (no full-text setup):
const searchResults = await db.query.comic.findMany({
  where: or(
    ilike(comic.title, `%${searchTerm}%`),
    ilike(comic.description, `%${searchTerm}%`)
  ),
  limit: 20
});
```

---

## Performance Considerations

### **Index Strategy**

The schema includes these key indexes:

| Table | Index Name | Columns | Purpose |
| --- | --- | --- | --- |
| `user` | userEmailIdx | email | Auth login |
| `comic` | comicSlugIdx | slug | URL lookups |
| `comic` | comicStatusIdx | status | Filter by ongoing/completed |
| `chapter` | chapterComicIdIdx | comicId | Get chapters for comic |
| `chapter` | chapterComicChapterIdx | (comicId, chapterNumber) | Get specific chapter |
| `bookmark` | bookmarkUserIdIdx | userId | Get user's bookmarks |
| `readingProgress` | readingProgressUserIdIdx | userId | Continue reading |
| `readingProgress` | readingProgressUserComicIdx | (userId, comicId) | Get progress for comic |
| `comment` | commentUserIdIdx | userId | User's comments |
| `comment` | commentChapterIdIdx | chapterId | Comments on chapter |
| `notification` | notificationUserReadIdx | (userId, read) | Get unread notifications |
| `rating` | ratingUserIdIdx, ratingComicIdIdx | userId, comicId | User ratings |

**✨ GOLDEN RULE:** If your WHERE clause includes a column not in an index, queries will full-table scan.

---

### **Query Optimization Checklist**

- ✅ Use `with()` for eager loading (beats N+1)
- ✅ Use indexes for WHERE/JOIN conditions
- ✅ Use `limit` on large result sets
- ✅ Select only needed columns (don't SELECT \*)
- ✅ Use composite keys for (userId, comicId) lookups
- ✅ Avoid subqueries when JOIN is possible
- ✅ Batch operations where possible

---

### **Common Slow Queries to Avoid**

```typescript
// ❌ SLOW: Full table scan with computed conditions
const query = db
  .select()
  .from(comic)
  .where(sql`CAST(rating AS NUMERIC) > 3.5`);

// ✅ FAST: Direct column comparison
const query = db.select().from(comic).where(gt(comic.rating, "3.5"));

// ❌ SLOW: No index on calculated field
const query = db
  .select()
  .from(readingProgress)
  .where(sql`YEAR(lastReadAt) = 2025`);

// ✅ FAST: Use timestamp range
const start2025 = new Date("2025-01-01");
const end2025 = new Date("2026-01-01");
const query = db
  .select()
  .from(readingProgress)
  .where(
    and(
      gte(readingProgress.lastReadAt, start2025),
      lt(readingProgress.lastReadAt, end2025)
    )
  );
```

---

## AI-Optimized Schema Reference

This section is structured for AI consumption to understand the database context quickly.

### **TABLES**

```json
{
  "tables": {
    "user": {
      "purpose": "User accounts and authentication",
      "primaryKey": "id (UUID text)",
      "uniqueFields": ["email"],
      "deletedAt": true,
      "foreignKeys": [],
      "childTables": [
        "account",
        "session",
        "authenticator",
        "bookmark",
        "comment",
        "rating",
        "readingProgress",
        "readerSettings",
        "notification",
        "userRole",
        "auditLog"
      ],
      "cascadeDelete": true,
      "indexes": ["userEmailIdx", "userRoleIdx"]
    },
    "comic": {
      "purpose": "Comic/manga/manhwa entries",
      "primaryKey": "id (serial)",
      "uniqueFields": ["title", "slug"],
      "enums": {
        "status": [
          "Ongoing",
          "Hiatus",
          "Completed",
          "Dropped",
          "Season End",
          "Coming Soon"
        ]
      },
      "foreignKeys": {
        "authorId": "author.id",
        "artistId": "artist.id",
        "typeId": "type.id"
      },
      "childTables": [
        "chapter",
        "comicImage",
        "comicToGenre",
        "bookmark",
        "rating",
        "readingProgress",
        "notification"
      ],
      "cascadeDelete": true,
      "indexes": [
        "comicSlugIdx",
        "comicTitleIdx",
        "comicStatusIdx",
        "comicRatingIdx",
        "comicViewsIdx"
      ]
    },
    "chapter": {
      "purpose": "Individual chapters of comics",
      "primaryKey": "id (serial)",
      "uniqueFields": ["slug", "(comicId, chapterNumber)"],
      "foreignKeys": {
        "comicId": "comic.id (CASCADE DELETE)"
      },
      "childTables": [
        "chapterImage",
        "readingProgress",
        "comment",
        "notification"
      ],
      "cascadeDelete": true,
      "indexes": [
        "chapterSlugIdx",
        "chapterComicIdIdx",
        "chapterComicChapterIdx"
      ]
    },
    "bookmark": {
      "purpose": "User's comic reading list",
      "primaryKey": "Composite(userId, comicId)",
      "foreignKeys": {
        "userId": "user.id (CASCADE DELETE)",
        "comicId": "comic.id (CASCADE DELETE)",
        "lastReadChapterId": "chapter.id (nullable)"
      },
      "idempotent": true,
      "notes": "Composite key enables upsert without duplication",
      "indexes": ["bookmarkUserIdIdx", "bookmarkComicIdIdx"]
    },
    "readingProgress": {
      "purpose": "Detailed reading position tracking",
      "primaryKey": "id (serial)",
      "foreignKeys": {
        "userId": "user.id (CASCADE DELETE)",
        "comicId": "comic.id (CASCADE DELETE)",
        "chapterId": "chapter.id (CASCADE DELETE)"
      },
      "queryPatterns": [
        "Continue reading",
        "User activity",
        "Progress tracking"
      ],
      "indexes": [
        "readingProgressUserIdIdx",
        "readingProgressComicIdIdx",
        "readingProgressUserComicIdx"
      ]
    },
    "comment": {
      "purpose": "Discussion threads on chapters",
      "primaryKey": "id (serial)",
      "foreignKeys": {
        "userId": "user.id (CASCADE DELETE)",
        "chapterId": "chapter.id (CASCADE DELETE)",
        "parentId": "comment.id (self-reference, nullable)"
      },
      "softDelete": "deletedAt (nullable)",
      "notes": "Supports threaded replies via parentId",
      "indexes": [
        "commentUserIdIdx",
        "commentChapterIdIdx",
        "commentParentIdIdx"
      ]
    },
    "notification": {
      "purpose": "User alerts and notifications",
      "primaryKey": "id (serial)",
      "foreignKeys": {
        "userId": "user.id (CASCADE DELETE)",
        "comicId": "comic.id (nullable, CASCADE DELETE)",
        "chapterId": "chapter.id (nullable, CASCADE DELETE)"
      },
      "types": ["new_chapter", "comment_reply", "system"],
      "indexes": [
        "notificationUserIdIdx",
        "notificationReadIdx",
        "notificationUserReadIdx"
      ]
    }
  }
}
```

### **CRITICAL RELATIONSHIPS**

```json
{
  "criticalRelationships": {
    "comic_chapter_cascade": {
      "description": "Deleting a comic cascades to all chapters, images, reading progress, comments",
      "path": "comic → chapter → chapterImage/readingProgress/comment",
      "cascadeDepth": 3
    },
    "user_interactions_cascade": {
      "description": "Deleting a user cascades to all their bookmarks, comments, ratings, progress",
      "path": "user → bookmark/comment/rating/readingProgress",
      "cascadeDepth": 1
    },
    "composite_key_bookmark": {
      "description": "Bookmark uses composite key (userId, comicId) for idempotent upserts",
      "pattern": "INSERT ... ON CONFLICT (userId, comicId) DO UPDATE",
      "benefit": "No duplicates, safe concurrent operations"
    },
    "chapter_number_uniqueness": {
      "description": "Chapters have composite unique constraint (comicId, chapterNumber)",
      "prevents": "Duplicate chapter numbers per comic",
      "enables": "Idempotent imports and upserts"
    }
  }
}
```

### **N+1 AVOIDANCE STRATEGIES**

```json
{
  "n1Patterns": {
    "example1": {
      "title": "Comics with Authors",
      "badPattern": "Loop comics, query each author individually",
      "goodPattern": "Single query with with({ author: true })",
      "impact": "100x query reduction for 100 comics"
    },
    "example2": {
      "title": "User Bookmarks with Comics and Genres",
      "badPattern": "Query bookmarks, then for each: query comic, then query genres",
      "goodPattern": "Single joined query with eager loading",
      "impact": "40x query reduction for 20 bookmarks"
    },
    "example3": {
      "title": "Reading Progress with Related Data",
      "badPattern": "Query progress, then loop and fetch comic/chapter",
      "goodPattern": "Use with({ comic: true, chapter: true })",
      "impact": "Turns N+2 into 1-2 queries"
    }
  }
}
```

---

## Summary & Key Takeaways

✅ **Authentication:** User cascades to account/session on delete  
✅ **Content:** Comic cascades to chapters, images, comments on delete  
✅ **User Data:** All user interaction data cascades on user delete  
⚠️ **Cascade Depth:** Sometimes 3+ levels deep (comic → chapter → images)  
🔴 **N+1 Risk:** High in comics/chapters/bookmarks relationships  
✨ **Solution:** Always use Drizzle `with()` for eager loading  
🎯 **Indexes:** Cover all WHERE/JOIN conditions in your queries  
🚀 **Performance:** Composite keys enable idempotent upserts

---

**Last Updated:** March 1, 2026 | **Schema Version:** 1.0.0 | **Maintained By:** ComicWise Team
