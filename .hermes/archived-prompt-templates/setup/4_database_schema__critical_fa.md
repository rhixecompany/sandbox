# 4. Database Schema — Critical Facts

> Extracted from `setup.prompt.md`.

## 4. Database Schema — Critical Facts

Schema defined in `src/database/schema.ts` (604 lines, **27 tables**, 4 enums).

### Enums

```typescript
// Title-Case values for comicStatus
comicStatus: "Ongoing" |
  "Hiatus" |
  "Completed" |
  "Dropped" |
  "Season End" |
  "Coming Soon";

// Lowercase values for userRole
userRole: "user" | "admin" | "moderator";

// RBAC enums (used by permission and auditLog tables)
resourceEnum: "comic" |
  "chapter" |
  "user" |
  "comment" |
  "rating" |
  "bookmark" |
  "notification" |
  "author" |
  "artist" |
  "genre" |
  "type" |
  "system";
actionEnum: "create" | "read" | "update" | "delete" | "manage";
```

### Key Table Facts

| Table | Key Column | Gotcha |
| --- | --- | --- |
| `user` | `id: text` (UUID string) | NOT integer. Password nullable (OAuth users). Has `deletedAt` for soft delete. Has `settings` JSONB column. |
| `comic` | `rating: decimal(10,1)` | Aggregate display rating. NOT integer. `status` must match Title-Case enum. |
| `rating` | `rating: integer` | Per-user 1–5 stars. Different type from `comic.rating`! Use `AVG(rating)` for aggregation. |
| `bookmark` | Composite PK `(userId, comicId)` | Use `onConflictDoUpdate` for upserts |
| `chapter` | Composite unique `(comicId, chapterNumber)` |  |
| All FK cols |  | Must include `{ onDelete: "cascade" }` except `auditLog.userId` → `"set null"` |

### Complete Table List (27 tables)

| Category | Tables |
| --- | --- |
| **Auth/User** | `user`, `account`, `session`, `verificationToken`, `authenticator`, `passwordResetToken` |
| **Content** | `type`, `author`, `artist`, `genre`, `comic`, `chapter`, `comicImage`, `chapterImage`, `comicToGenre` (junction) |
| **User Activity** | `bookmark`, `comment`, `readingProgress`, `readerSettings`, `rating`, `notification`, `userPreference` |
| **RBAC** | `role`, `permission`, `rolePermission`, `userRole2` |
| **Audit** | `auditLog` |

### RBAC Tables

```typescript
role:           { id, name, description, isSystem, createdAt, updatedAt }
permission:     { id, name, resource (resourceEnum), action (actionEnum), createdAt }
rolePermission: { roleId, permissionId }  // Composite PK, cascade deletes both FKs
userRole2:      { userId, roleId, assignedBy (FK → user) }  // Composite PK
```

> **Note:** The JS export is `userRole2` because the enum `userRole` already occupies that name.

### Audit Log Table

```typescript
auditLog: {
  (id,
    userId,
    action,
    resource(resourceEnum),
    resourceId,
    details,
    oldValues,
    newValues,
    ipAddress,
    userAgent,
    sessionId,
    createdAt);
}
// ⚠ EXCEPTION: userId uses onDelete: "set null" (NOT cascade)
// This preserves audit trail when users are deleted
// Has 7 indexes for efficient querying
```

### Supplementary Tables

```typescript
readerSettings:     { userId (1:1 with user), backgroundMode, readingMode, defaultQuality }
passwordResetToken: { email, token (unique), expires }
userPreference:     { userId, ... }
comicImage:         { id, comicId, ... }  // Comic cover/banner images
chapterImage:       { id, chapterId, ... }  // Chapter page images
```

### Soft Delete

`user.deletedAt` exists in schema. **Rule:** Filter `WHERE deletedAt IS NULL` in user queries to exclude soft-deleted users.

### User Settings JSONB

```typescript
user.settings: jsonb("settings").$type<{
  emailNotifications?: boolean;
  profileVisibility?: "private" | "public";
  readingHistoryVisibility?: boolean;
}>()
```

### Search Vector Fields

`comic.searchVector`, `author.searchVector`, `artist.searchVector` — stored as `text` columns (not actual PostgreSQL `tsvector` despite the name). Used for text search indexing.

### Entity Relationships (Simplified)

```
Type ──┐
Author ┼──→ Comic ──→ Chapter ──→ ChapterImage
Artist ┘      │
              ├──→ ComicImage
Genre ←── ComicToGenre (junction)

User ──→ Bookmark, Rating, Comment, ReadingProgress, Notification, ReaderSettings, UserPreference
User ──→ UserRole2 ──→ Role ──→ RolePermission ──→ Permission
User ──→ AuditLog (set null on delete)
```

### Cascade Delete Scenarios

| Scenario | Cascades To | Exception |
| --- | --- | --- |
| **Delete User** | bookmark, rating, comment, readingProgress, notification, readerSettings, userPreference, userRole2 | `auditLog.userId` → SET NULL (not cascade) |
| **Delete Comic** | chapter, bookmark, rating, comment, comicToGenre, comicImage, readingProgress | — |
| **Delete Chapter** | chapterImage, readingProgress (for that chapter) | `bookmark.lastReadChapterId` → SET NULL |

---
