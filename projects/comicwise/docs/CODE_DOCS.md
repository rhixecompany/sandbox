# ComicWise Code Documentation

## Overview

ComicWise is a full-stack comic book reading platform built with Next.js 14+ (App Router), TypeScript, PostgreSQL via Drizzle ORM, NextAuth v5, and tRPC. The codebase follows a layered architecture separating database schema, data access, server actions, and UI components.

---

## 1. Database Schema Layer

**File:** `src/database/schema.ts`

The schema defines 30+ PostgreSQL tables via Drizzle ORM, organized into these domains:

### Auth Tables

| Table | Key Fields | Purpose |
|-------|-----------|---------|
| `user` | id (UUID), email (unique), password (hash), role (enum), status (boolean), settings (JSONB), deletedAt (soft delete) | User accounts with role-based access |
| `account` | userId (FK), provider, providerAccountId | OAuth provider accounts (NextAuth) |
| `session` | sessionToken (PK), userId (FK), expires | Session management |
| `verificationToken` | identifier, token, expires | Email verification |
| `authenticator` | credentialID, userId (FK), credentialPublicKey | WebAuthn/passkey support |
| `passwordResetToken` | id, email, token, expires | Password reset flow |

**Enums:** `user_role` = `'user' | 'admin' | 'moderator'`

### Comic Content Tables

| Table | Key Fields | Purpose |
|-------|-----------|---------|
| `type` | id, name (unique), description | Comic type classification (manga, manhwa, etc.) |
| `author` | id, name (unique), bio, image, searchVector | Author profiles with full-text search |
| `artist` | id, name (unique), bio, image, searchVector | Artist profiles with full-text search |
| `genre` | id, name (unique), slug (unique), description, isActive | Genre taxonomy |
| `comic` | id, title (unique), slug (unique), description, coverImage, status, publicationDate, rating, views, authorId, artistId, typeId | Core comic entity with 9 indexes |
| `chapter` | id, slug (unique), title, chapterNumber, releaseDate, comicId (FK), views, content | Chapter with unique(comicId, chapterNumber) |
| `comicImage` | id, comicId (FK), imageUrl (unique), imageOrder | Comic cover/banner images |
| `chapterImage` | id, chapterId (FK), imageUrl, pageNumber | Chapter page images with unique(chapterId, pageNumber) |
| `comicToGenre` | comicId, genreId (composite PK) | Many-to-many comic-genre mapping |

**Enum:** `comic_status` = `'Ongoing' | 'Hiatus' | 'Completed' | 'Dropped' | 'Season End' | 'Coming Soon'`

### User Interaction Tables

| Table | Key Fields | Purpose |
|-------|-----------|---------|
| `bookmark` | userId, comicId (composite PK), lastReadChapterId, status, notes | User bookmarks with reading status |
| `comment` | id, content, userId (FK), chapterId (FK), parentId (self-ref FK), deletedAt | Nested comments with soft-delete |
| `readingProgress` | id, userId, comicId, chapterId, pageNumber, scrollPosition, progressPercent, completedAt | Granular per-chapter reading position |
| `readerSettings` | id, userId (unique), backgroundMode, readingMode, defaultQuality | Per-user reader preferences |
| `rating` | id, userId, comicId, rating (1-5), review | User ratings with unique(userId, comicId) |
| `notification` | id, userId, type, title, message, link, read, comicId, chapterId | In-app notifications |

### RBAC Tables

| Table | Key Fields | Purpose |
|-------|-----------|---------|
| `role` | id, name (unique), description, isSystem | Role definitions |
| `permission` | id, name (unique), resource (enum), action (enum) | Granular permissions with unique(resource, action) |
| `rolePermission` | roleId, permissionId (composite PK) | Role-permission mappings |
| `userRole` | userId, roleId (composite PK), assignedBy | User-role assignments |

**Enums:** `resource_type` = 12 resources, `action_type` = `'create' | 'read' | 'update' | 'delete' | 'manage'`

### Analytics & Social Tables

| Table | Key Fields | Purpose |
|-------|-----------|---------|
| `auditLog` | id (UUID), userId, action, resource, resourceId, details, oldValues, newValues, ipAddress, userAgent | Comprehensive audit trail |
| `userPreference` | id, userId (unique), theme, defaultLayout, pageNavigationStyle, fontSize, notification toggles, privacy flags | User preferences |
| `readingHistory` | id, userId, comicId, chapterId, startedAt, completedAt, timeSpentSeconds, progress | Reading analytics time-series |
| `readingGoal` | id, userId, type (daily_chapters/weekly_comics/monthly_minutes), target, currentCount, startDate, endDate | Goal tracking |
| `searchIndex` | id, comicId (unique), denormalized title/synopsis/authors/artists/genres, searchVector (tsvector), popularity, rating | Full-text search optimization |
| `follow` | followerId, followingId (composite PK) | User-user following |
| `share` | id, userId, resourceType, resourceId, message | Share to activity feed |

### Relations

All tables have explicit `relations()` definitions enabling Drizzle ORM's `with()` eager loading. Key relationship chains:
- `comic -> author, artist, type, chapters, images, genres, bookmarks, ratings, readingProgress, searchIndex`
- `user -> accounts, sessions, bookmarks, comments, ratings, notifications, roles, followers/following`

---

## 2. Server Action Layer

**File:** `src/actions/` (27 files)

Server actions are Next.js Server Actions using `"use server"` pattern. Each action file follows:

```typescript
// Pattern: validate input with Zod -> call DAL -> return result
export async function actionName(input: InputType): Promise<ActionResult> {
  const validated = schema.parse(input); // or safeParse
  // authorize (RBAC check)
  // call DAL
  // revalidate path
  // return { success, data }
}
```

**Auth:** `auth.actions.ts`, `credentials.actions.ts`, `password-reset.actions.ts`
**Content:** `comic.actions.ts`, `chapter.actions.ts`, `author.actions.ts`, `artist.actions.ts`, `genre.actions.ts`
**User Interaction:** `bookmark.actions.ts`, `comment-rating.actions.ts`, `follow.actions.ts`, `reading.actions.ts`, `reading-progress.actions.ts`, `profile.actions.ts`, `notification.actions.ts`
**Search:** `search.actions.ts`, `search-filters.actions.ts`, `browse.actions.ts`
**Admin:** `admin/` subdirectory with `comic.actions.ts`, `chapter.actions.ts`, `author.actions.ts`, `artist.actions.ts`, `genre.actions.ts`, `type.actions.ts`, `user.actions.ts`, `role.actions.ts`, `permission.actions.ts`, `audit-log.actions.ts`
**System:** `share.actions.ts`, `user-preferences.actions.ts`, `goals.actions.ts`, `rbac.actions.ts`, `admin.actions.ts`

---

## 3. Data Access Layer

**File:** `src/dal/` (28 files)

Each entity has a dedicated DAL file providing CRUD operations:

```typescript
// Pattern: DB query using Drizzle ORM
export async function findById(id: number): Promise<Entity | null> {
  return db.query.entity.findFirst({
    where: eq(entity.id, id),
    with: { relations... }
  });
}
```

Key DAL files: `base-dal.ts` (shared utilities), `comic-dal.ts`, `chapter-dal.ts`, `chapter-image-dal.ts`, `comic-image-dal.ts`, `author-dal.ts`, `artist-dal.ts`, `genre-dal.ts`, `type-dal.ts`, `bookmark-dal.ts`, `comment-rating-dal.ts`, `follow-dal.ts`, `reading-progress-dal.ts`, `reading-history-dal.ts`, `reading-goals-dal.ts`, `notification-dal.ts`, `search-dal.ts`, `share-dal.ts`, `recommendation-dal.ts`, `user-dal.ts`, `user-preferences-dal.ts`, `user-role-dal.ts`, `role-dal.ts`, `permission-dal.ts`, `auth-db.ts`, `password-reset-dal.ts`, `audit-log-dal.ts`

---

## 4. Application Routes

**File:** `src/app/`

Three route groups under Next.js App Router:

### `(auth)` — Authentication
- `sign-in/page.tsx` — Sign-in with credentials/OAuth
- `sign-up/page.tsx` — Registration

### `(root)` — Main Application
- `/` — Home page with continue-reading, recommended, feed
- `comics/page.tsx` — Browse all comics
- `comics/[slug]/page.tsx` — Comic detail page
- `comics/[slug]/[chapterNumber]/page.tsx` — Chapter reader
- `browse/page.tsx` — Browse with filters
- `search/page.tsx` — Search with advanced filters
- `bookmarks/page.tsx` — User bookmarks
- `feed/page.tsx` — Activity feed
- `profile/page.tsx` — User profile
- `profile/[id]/followers` — Follower list
- `profile/[id]/following` — Following list
- `profile/edit/page.tsx` — Profile editing
- `profile/settings/page.tsx` — User settings
- `profile/change-password/page.tsx` — Password change
- `profile/delete-account/page.tsx` — Account deletion
- `settings/page.tsx` — Application settings
- `analytics/page.tsx` — Reading analytics dashboard
- `notifications/page.tsx` — Notification center
- `comments/page.tsx` — Comments overview
- `ratings/page.tsx` — Ratings overview
- `reading-progress/page.tsx` — Reading progress tracking

### `admin/` — Admin Panel
- `page.tsx` — Admin dashboard
- `comics/page.tsx` — Comic management
- `chapters/page.tsx` — Chapter management
- `authors/page.tsx` — Author management
- `artists/page.tsx` — Artist management
- `genres/page.tsx` — Genre management
- `types/page.tsx` — Type management
- `users/page.tsx` — User management
- `roles/page.tsx` — Role management
- `permissions/page.tsx` — Permission management
- `audit-logs/page.tsx` — Audit log viewer

### `api/` — API Routes
- `api/auth/[...nextauth]/route.ts` — NextAuth v5 handler
- `api/seed/route.ts` — Database seeding

---

## 5. Component Library

**File:** `src/components/`

### UI Primitives (src/components/ui/)
60+ shadcn/ui components: button, card, dialog, dropdown-menu, form, input, select, table, tabs, sidebar, sheet, popover, accordion, alert-dialog, avatar, badge, breadcrumb, calendar, carousel, chart, checkbox, command, context-menu, data-table, drawer, hover-card, menubar, navigation-menu, pagination, radio-group, resizable, scroll-area, separator, skeleton, slider, sonner (toast), switch, textarea, toggle, tooltip, multi-select, input-otp, password-input, number-input, combobox, field

### Feature Components
- **auth/:** sign-in-form, sign-up-form, sign-in-wrapper, sign-up-wrapper
- **comics/:** comic-card, comic-detail-wrapper, comic-filters, comic-list-skeleton, comic-pagination-controls, comics-wrapper, bookmark-button, share-button, empty-state
- **reading/:** chapter-reader, chapter-reader-wrapper, image-viewer, reader-controls, reader-settings, reader-view, progress-bar, continue-reading-card, continue-reading-section
- **bookmarks/:** bookmark-card, bookmarks-filter, bookmarks-wrapper, resume-button, status-editor
- **comments/:** chapter-comments-section, comment-card, comment-form, comment-list, comments-wrapper
- **ratings/:** comic-ratings-display, comic-ratings-section, rating-button, rating-form, rating-stats, ratings-wrapper
- **search/:** advanced-search-form, search-input, search-results, search-results-content, search-suggestions-dropdown, search-wrapper
- **profile/:** profile-edit-form, settings-form, change-password-form, delete-account-form, profile-wrapper
- **layout/:** app-sidebar, navbar, site-header, footer, nav-main, nav-secondary, nav-user, nav-documents, logo, layout-provider, section-cards, data-table, chart-area-interactive
- **admin/:** admin-wrapper, 10 admin entity wrappers
- **analytics/:** reading-dashboard, reading-goals-widget, reading-history-timeline, reading-stats-card

---

## 6. Validation Schemas

**File:** `src/schemas/`

Zod schemas for runtime validation:
- `auth.schema.ts` — Login/register/password reset validation
- `comic.schema.ts` — Comic creation/update validation
- `chapter.schema.ts` — Chapter creation/update validation
- `author.schema.ts` — Author CRUD validation
- `artist.schema.ts` — Artist CRUD validation
- `bookmark-schema.ts` — Bookmark operations
- `comment.schema.ts` — Comment creation/update
- `follow.schema.ts` — Follow/unfollow
- `audit-log.schema.ts` — Audit log queries

---

## 7. Hooks & Utilities

### Custom Hooks (src/hooks/)
| Hook | Signature | Purpose |
|------|-----------|---------|
| `use-debounce.ts` | `useDebounce<T>(value: T, delay: number): T` | Debounces a value by specified ms for search-as-you-type |
| `use-keyboard-navigation.tsx` | `useKeyboardNavigation(keyMap: KeyMap): void` | Maps arrow keys, Enter, Escape for reader keyboard shortcuts |
| `use-mobile.ts` | `useMobile(): boolean` | Detects mobile viewport (<768px) for responsive UI switching |
| `use-now.tsx` | `useNow(interval?: number): Date` | SSR-safe reactive clock used for reading time tracking |
| `use-pagination.ts` | `usePagination<T>(items: T[], pageSize: number): PaginationResult<T>` | Client-side pagination state with currentPage, totalPages, handlers |
| `use-performance-monitoring.tsx` | `usePerformanceMonitoring(componentName: string): void` | Tracks render times and interaction metrics for analytics |

### Library Utilities (src/lib/)
| File | Key Export | Purpose |
|------|-----------|---------|
| `utils.ts` | `cn(...inputs)` | Tailwind class merging with clsx + tailwind-merge |
| `accessibility.ts` | `skipToContent`, `announceToScreenReader` | ARIA helpers for keyboard nav and live regions |
| `image-optimization.ts` | `getOptimizedImageUrl`, `generateSrcSet` | Generates responsive image URLs with quality/size params |
| `image-processor.ts` | `processClientImage`, `validateFileType` | Client-side validation (size, dimensions, type) before upload |
| `performance-metrics.ts` | `trackMetric`, `MetricCollector` | Collects and batches Web Vitals and custom metrics |
| `query-client.ts` | `queryClient`, `trpcClient` | React Query and tRPC client configuration with SSR hydration |

### Zustand Stores (src/stores/)
| Store | Key State | Persisted |
|-------|-----------|-----------|
| `use-bookmark-store.ts` | `bookmarks[]`, `addBookmark`, `removeBookmark` | Yes |
| `use-reader-store.ts` | `layout`, `direction`, `zoom`, `currentPage` | Yes |
| `use-reading-progress-store.ts` | `progressByChapter`, `syncProgress` | Yes |
| `use-notification-store.ts` | `notifications[]`, `unreadCount`, `markRead` | No |
| `use-ui-store.ts` | `sidebar`, `theme`, `mobileMenu` | Partial |

---

## 8. TypeScript Types & Interfaces

### Entity Types
All entity types are derived from Drizzle ORM's `$inferSelect`:
```typescript
type ComicType = typeof comic.$inferSelect;        // Full comic row type
type ChapterType = typeof chapter.$inferSelect;     // Full chapter row type
type UserType = typeof user.$inferSelect;            // Full user row type
```

### Action Result Pattern
```typescript
type ActionResult<T> =
  | { data: T; ok: true }
  | { error: string; ok: false };
```

### Server Action Input Types
Located in `src/schemas/`, each entity has Zod-inferred input types:
```typescript
type CreateComicInput = z.infer<typeof createComicSchema>;
type UpdateComicInput = z.infer<typeof updateComicSchema>;
type ComicFilter = z.infer<typeof comicFilterSchema>;
```

### Key Type Patterns
- **Null vs Undefined:** DAL methods return `null` (not `undefined`) when records are not found — enforced by convention
- **Composite PK types:** Bookmark, Follow, UserRole use compound key types for upsert operations  
- **Enum types:** All enum values (user_role, comic_status, resource_type, action_type) have matching TypeScript `const` enums in `schema.ts`
- **Relation types:** Drizzle generates relation types via `relations()` — no hand-written join types needed
