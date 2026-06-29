# Complete Entity Reference

> Extracted from `debugger.prompt.md`.

## Complete Entity Reference

### Entity Groups & Organization

**Group 1: Authentication & Authorization (10 tables)**

- `user`, `account`, `session`, `authenticator`, `verificationToken`, `passwordResetToken`
- `role`, `permission`, `userRole`, `rolePermission`

**Group 2: Comic Content (9 tables)**

- `type`, `author`, `artist`, `genre`, `comic`, `comicImage`, `comicToGenre`
- `chapter`, `chapterImage`

**Group 3: User Interactions (6 tables)**

- `bookmark`, `comment`, `rating`, `readingProgress`, `readerSettings`, `notification`

**Group 4: Audit & Logging (1 table)**

- `auditLog`

### Detailed Table Schemas

#### USER TABLE

```typescript
user: {
  id: text (UUID, primary key),
  name: text (nullable),
  email: text (UNIQUE, NOT NULL),
  emailVerified: timestamp (nullable),
  image: text (profile picture),
  password: text (bcrypt hash, nullable for OAuth),
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

**🔴 COMMON MISTAKE:** Forgetting that deleted users (`deletedAt IS NOT NULL`) should be filtered in queries.

---

#### COMIC TABLE

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

Indexes: 9 indexes covering slug, title, status, rating, views
Unique: title, slug
```

**⚠️ IMPORTANT:** Use `comicSlugIdx` for lookups. Slug is the primary query parameter in URLs.

---

#### CHAPTER TABLE

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

Indexes: chapterSlugIdx, chapterComicIdIdx, chapterComicChapterIdx
Unique: slug, (comicId, chapterNumber) ← CRITICAL for upserts
```

**🔴 CRITICAL:** The composite unique constraint `(comicId, chapterNumber)`:

- Prevents duplicate chapter numbers for same comic
- Enables idempotent `onConflictDoUpdate` in seeding/imports
- Used heavily in queries: "Get chapter 25 of comic X"

---

#### BOOKMARK TABLE

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

**✨ CLEVER DESIGN:** Composite primary key enables idempotent upserts:

```typescript
// Can safely call this multiple times
INSERT INTO bookmark (userId, comicId, status)
  VALUES ('user1', 123, 'Reading')
ON CONFLICT (userId, comicId) DO UPDATE
  SET status = EXCLUDED.status, updatedAt = NOW();
```

---

#### READING PROGRESS TABLE

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

### Other Critical Tables

**NOTIFICATION TABLE**

```typescript
notification: {
  id: serial (primary key),
  userId: text (foreign key → user.id, CASCADE DELETE),
  type: text (new_chapter | comment_reply | system),
  title: text,
  message: text,
  link: text (nullable, URL to navigate to),
  read: boolean (default false),
  comicId: integer (nullable, CASCADE DELETE),
  chapterId: integer (nullable, CASCADE DELETE),
  createdAt: timestamp
}

Indexes: userId, read, type, createdAt, (userId, read)
```

**COMMENT TABLE**

```typescript
comment: {
  id: serial (primary key),
  userId: text (foreign key → user.id, CASCADE DELETE),
  chapterId: integer (foreign key → chapter.id, CASCADE DELETE),
  content: text,
  parentId: integer (nullable, self-reference for replies),
  deletedAt: timestamp (soft delete, nullable),
  createdAt: timestamp,
  updatedAt: timestamp
}

Indexes: userId, chapterId, parentId
```

**Supports threaded replies:** `parentId → comment.id` (self-reference)

---
