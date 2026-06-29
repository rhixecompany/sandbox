# ComicWise — Database Schema

## Overview

ComicWise uses **PostgreSQL 14+** with **Drizzle ORM** and **Neon** serverless PostgreSQL. The schema consists of **27 tables**, **4 pgEnums**, and full referential integrity.

## pgEnums

| Enum | Values | Usage |
| --- | --- | --- |
| `userRole` | `USER, ADMIN, MODERATOR` | Role-based access |
| `comicStatus` | `ONGOING, COMPLETED, HIATUS, CANCELLED` | Comic publication status |
| `resourceEnum` | `COMIC, CHAPTER, USER, COMMENT` | Notification resource types |
| `actionEnum` | `CREATE, UPDATE, DELETE, FOLLOW, LIKE, RATE, COMMENT` | Audit actions |

## Core Tables

### `users`

| Column | Type | Constraints | Description |
| --- | --- | --- | --- |
| `id` | `uuid` | `PK DEFAULT gen_random_uuid()` | Unique ID |
| `email` | `varchar(255)` | `UNIQUE NOT NULL` | Email |
| `username` | `varchar(100)` | `UNIQUE NOT NULL` | Display name |
| `passwordHash` | `text` | `NULLABLE` | bcrypt hash |
| `role` | `userRole` | `DEFAULT 'USER'` | Access level |
| `avatarUrl` | `text` | `NULLABLE` | Profile image |
| `deletedAt` | `timestamptz` | `NULLABLE` | Soft-delete |
| `createdAt` | `timestamptz` | `DEFAULT NOW()` |  |
| `updatedAt` | `timestamptz` | `DEFAULT NOW()` |  |

### `comics`

| Column | Type | Constraints | Description |
| --- | --- | --- | --- |
| `id` | `uuid` | `PK` | Unique ID |
| `title` | `varchar(255)` | `NOT NULL` | Comic title |
| `slug` | `varchar(255)` | `UNIQUE NOT NULL` | URL-friendly |
| `description` | `text` | `NULLABLE` | Synopsis |
| `status` | `comicStatus` | `DEFAULT 'ONGOING'` | Publication status |
| `coverUrl` | `text` | `NULLABLE` | Cover image |
| `authorId` | `uuid` | `FK → authors.id` | Author |
| `artistId` | `uuid` | `FK → artists.id` | Artist |
| `totalChapters` | `integer` | `DEFAULT 0` | Chapter count |
| `averageRating` | `decimal(3,2)` | `DEFAULT 0` | Aggregated rating |
| `createdAt` | `timestamptz` | `DEFAULT NOW()` |  |
| `updatedAt` | `timestamptz` | `DEFAULT NOW()` |  |

### `chapters`

| Column | Type | Constraints | Description |
| --- | --- | --- | --- |
| `id` | `uuid` | `PK` | Unique ID |
| `comicId` | `uuid` | `FK → comics.id CASCADE` | Parent comic |
| `number` | `decimal(10,2)` | `NOT NULL` | Chapter number |
| `title` | `varchar(255)` | `NULLABLE` | Chapter title |
| `imageCount` | `integer` | `DEFAULT 0` | Number of pages |
| `createdAt` | `timestamptz` | `DEFAULT NOW()` |  |

### `chapter_images`

| Column | Type | Constraints | Description |
| --- | --- | --- | --- |
| `id` | `uuid` | `PK` |  |
| `chapterId` | `uuid` | `FK → chapters.id CASCADE` | Parent chapter |
| `pageNumber` | `integer` | `NOT NULL` | Page order |
| `imageUrl` | `text` | `NOT NULL` | Image URL |
| `width` | `integer` | `NULLABLE` | Image width |
| `height` | `integer` | `NULLABLE` | Image height |

### `genres`

| Column | Type           | Constraints       | Description  |
| ------ | -------------- | ----------------- | ------------ |
| `id`   | `uuid`         | `PK`              |              |
| `name` | `varchar(100)` | `UNIQUE NOT NULL` | Genre name   |
| `slug` | `varchar(100)` | `UNIQUE NOT NULL` | URL-friendly |

### `comic_genres` (Junction)

| Column    | Type                 | Constraints              |
| --------- | -------------------- | ------------------------ |
| `comicId` | `uuid`               | `FK → comics.id CASCADE` |
| `genreId` | `uuid`               | `FK → genres.id CASCADE` |
| `PK`      | `(comicId, genreId)` |                          |

### `bookmarks`

| Column | Type | Constraints | Description |
| --- | --- | --- | --- |
| `id` | `uuid` | `PK` |  |
| `userId` | `uuid` | `FK → users.id CASCADE` |  |
| `comicId` | `uuid` | `FK → comics.id CASCADE` |  |
| `createdAt` | `timestamptz` | `DEFAULT NOW()` |  |
| `UNIQUE` | `(userId, comicId)` |  | Prevents duplicates |

### `reading_history`

| Column      | Type          | Constraints                |
| ----------- | ------------- | -------------------------- |
| `id`        | `uuid`        | `PK`                       |
| `userId`    | `uuid`        | `FK → users.id CASCADE`    |
| `chapterId` | `uuid`        | `FK → chapters.id CASCADE` |
| `lastPage`  | `integer`     | `DEFAULT 1`                |
| `completed` | `boolean`     | `DEFAULT false`            |
| `readAt`    | `timestamptz` | `DEFAULT NOW()`            |

### `ratings`

| Column      | Type                | Constraints                   |
| ----------- | ------------------- | ----------------------------- |
| `id`        | `uuid`              | `PK`                          |
| `userId`    | `uuid`              | `FK → users.id CASCADE`       |
| `comicId`   | `uuid`              | `FK → comics.id CASCADE`      |
| `score`     | `integer`           | `CHECK (1-5)`                 |
| `createdAt` | `timestamptz`       | `DEFAULT NOW()`               |
| `UNIQUE`    | `(userId, comicId)` | One rating per user per comic |

### `comments`

| Column      | Type          | Constraints                |
| ----------- | ------------- | -------------------------- |
| `id`        | `uuid`        | `PK`                       |
| `userId`    | `uuid`        | `FK → users.id CASCADE`    |
| `chapterId` | `uuid`        | `FK → chapters.id CASCADE` |
| `content`   | `text`        | `NOT NULL`                 |
| `deletedAt` | `timestamptz` | `NULLABLE` (soft-delete)   |
| `createdAt` | `timestamptz` | `DEFAULT NOW()`            |

### Additional Tables

- `authors` — Author profiles
- `artists` — Artist profiles
- `user_preferences` — Reader settings (theme, language)
- `reader_settings` — Per-user reader configuration
- `notifications` — User notification queue
- `notification_preferences` — Opt-in/out for notification types
- `follows` — Comic follows (user → comic)
- `reading_goals` — User-set reading targets
- `shares` — Share tracking
- `roles` / `permissions` — RBAC configuration
- `user_roles` — Junction table for user roles
- `sessions` — NextAuth sessions
- `accounts` — NextAuth provider accounts
- `verification_tokens` — Email verification

## Key Indexes

| Table | Index | Columns | Purpose |
| --- | --- | --- | --- |
| `comics` | `idx_comics_slug` | `slug` | URL lookups |
| `comics` | `idx_comics_status` | `status` | Status filtering |
| `comics` | `idx_comics_rating` | `average_rating` | Sort by rating |
| `chapters` | `idx_chapters_comic_number` | `comic_id, number` | Chapter ordering |
| `reading_history` | `idx_reading_history_user` | `user_id` | User history queries |

## Drizzle ORM Setup

```typescript
// database/db.ts
import { neon } from "@neondatabase/serverless";
import { drizzle } from "drizzle-orm/neon-http";
import * as schema from "./schema";

const sql = neon(process.env.DATABASE_URL!);
export const db = drizzle(sql, { schema });
```
