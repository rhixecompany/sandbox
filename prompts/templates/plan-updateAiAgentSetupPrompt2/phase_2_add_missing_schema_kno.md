# Phase 2: Add Missing Schema Knowledge (9 items)

> Extracted from `plan-updateAiAgentSetupPrompt2.prompt.md`.

## Phase 2: Add Missing Schema Knowledge (9 items)

### Step 7 — Add RBAC tables to §4

- `role` (id, name, description, isSystem)
- `permission` (id, name, resource via resourceEnum, action via actionEnum)
- `rolePermission` (composite PK roleId+permissionId, cascade deletes)
- `userRole2` (composite PK userId+roleId, assignedBy FK to user)

Note: JS export is `userRole2` because enum `userRole` already uses that name.

### Step 8 — Add `auditLog` table to §4

Fields: `userId` (`onDelete: "set null"` — exception to cascade rule), `action`, `resource` (resourceEnum), `resourceId`, `details`, `oldValues`, `newValues`, `ipAddress`, `userAgent`, `sessionId`. 7 indexes.

### Step 9 — Add supplementary tables

- `readerSettings` (backgroundMode, readingMode, defaultQuality — one-to-one with user)
- `passwordResetToken` (email, token unique, expires)
- `userPreference`
- `comicImage`
- `chapterImage`

### Step 10 — Document soft delete

`user.deletedAt` exists in schema. Add rule: "Filter `WHERE deletedAt IS NULL` in user queries."

### Step 11 — Document `user.settings` JSONB

```typescript
settings: jsonb("settings").$type<{
  emailNotifications?: boolean;
  profileVisibility?: "private" | "public";
  readingHistoryVisibility?: boolean;
}>();
```

### Step 12 — Add `searchVector` fields

`comic.searchVector`, `author.searchVector`, `artist.searchVector` — stored as `text` columns (not actual PostgreSQL `tsvector` despite the name).

### Step 13 — Add `resourceEnum` and `actionEnum`

```typescript
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

Used by RBAC and audit tables.

### Step 14 — Update table count

27 tables total (not "30+"). Full list: `user`, `account`, `session`, `verificationToken`, `authenticator`, `passwordResetToken`, `type`, `author`, `artist`, `genre`, `comic`, `chapter`, `comicImage`, `chapterImage`, `comicToGenre`, `bookmark`, `comment`, `readingProgress`, `readerSettings`, `rating`, `notification`, `role`, `permission`, `rolePermission`, `userRole2`, `auditLog`, `userPreference`.

### Step 15 — Add Drizzle relations warning (CRITICAL)

New prominent callout in §6:

> **⚠ No explicit `relations()` definitions in schema.ts.** DALs rely on Drizzle's FK inference from `.references()` column declarations. This means:
>
> - Simple FK relations (`comic.authorId → author.id`) auto-infer and `.with({ author: true })` works.
> - Junction tables (`comicToGenre`) are inferred from FKs and `.with({ genres: { with: { genre: true } } })` works.
> - `comment.parentId` has **no** `.references()` call → parent/replies relation **cannot** be used with `db.query`.
> - Self-referential, multi-FK-to-same-table, and custom-named relations **require explicit `relations()` to be added**.
>
> Current DALs work because they only use simple FK-inferred relations. If you need advanced relations, add `relations()` definitions to schema.ts.

---
