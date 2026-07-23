# 6. 🏗️ Feature Implementation Phases

> Extracted from `setup-enhanced.prompt.md` for DRY templating.

## 6. 🏗️ Feature Implementation Phases

### Phase Overview

| Phase | Focus | Prerequisites |
| --- | --- | --- |
| 1 | Foundation | Database, DAL, validation infrastructure |
| 2 | User Profile | Auth flow complete |
| 3 | Comics | Phase 1 complete |
| 4 | Chapter Reader | Phase 3 complete |
| 5 | Bookmarks Management | Phase 3 complete |
| 6+ | Advanced Features | Phases 1-5 complete |

---

### Phase 1: Foundation

Infrastructure setup — database schema, base DAL, core validation, auth flow.

**Checklist:**

- [ ] `pnpm install` — dependencies installed
- [ ] `.env.local` — configured with `DATABASE_URL`, `AUTH_SECRET`
- [ ] `pnpm db:push` — schema applied
- [ ] `pnpm type-check` — zero errors
- [ ] `pnpm dev` — server starts on port 3000

---

### Phase 2: User Profile Features

| Task | File | Key Features |
| --- | --- | --- |
| 2.1 Profile View | `src/app/(root)/profile/page.tsx` | Avatar, stats, recent activity, quick actions |
| 2.2 Profile Edit | `src/app/(root)/profile/edit/page.tsx` | Edit form, avatar upload, Zod validation |
| 2.3 Change Password | `src/app/(root)/profile/change-password/page.tsx` | Password validation, strength indicator |
| 2.4 Settings | `src/app/(root)/profile/settings/page.tsx` | Notifications, privacy, theme, danger zone |

**Components:** `ProfileView`, `ProfileStats`, `RecentActivity` **Schema:** `ProfileUpdateSchema`, `ChangePasswordSchema` in `src/schemas/profile.schema.ts` **Actions:** `updateProfileAction`, `changePasswordAction` in `src/actions/profile.actions.ts`

---

### Phase 3: Comic Features

#### Task 3.1: Comics Listing

**File:** `src/app/(root)/comics/page.tsx`

| Feature    | Details                                  |
| ---------- | ---------------------------------------- |
| Layout     | Responsive grid (2/3/4 cols by viewport) |
| Cards      | Lazy-loaded images, metadata badges      |
| Filtering  | Genre, type, status sidebar              |
| Sorting    | Latest, popular, rating                  |
| Search     | Text search with debounce                |
| Pagination | 20 per page                              |

**Components:** `ComicCard`, `ComicFilters`, `ComicSearch`, `ComicPagination`

#### Task 3.2: Comic Details

**File:** `src/app/(root)/comics/[slug]/page.tsx`

| Feature  | Details                           |
| -------- | --------------------------------- |
| Header   | Cover image, title, author/artist |
| Metadata | Rating, status badges, genre tags |
| Content  | Truncated description, statistics |
| Actions  | Bookmark toggle, chapter list     |
| Related  | Recommendations section           |

**Components:** `ComicHeader`, `ComicDescription`, `ComicStats`, `BookmarkActions`, `ChapterList`, `RelatedComics`

#### Task 3.3: Bookmark Components

**Files:** `src/components/comics/AddToBookmarkButton.tsx`, `RemoveFromBookmarkButton.tsx`, `BookmarkStatus.tsx` **Actions:** `addToBookmarksAction`, `removeFromBookmarksAction`, `updateBookmarkStatusAction`

Features: Optimistic UI, status dropdown (Reading, Plan to Read, Completed, On Hold, Dropped), toast notifications.

---

### Phase 4: Chapter Reader

**File:** `src/app/(root)/comics/[slug]/[chapterNumber]/page.tsx`

| Feature | Details |
| --- | --- |
| Reading Modes | Vertical scroll (default), horizontal page |
| Controls | Zoom, fit-to-width/height, fullscreen |
| Navigation | Prev/next chapter, chapter dropdown, keyboard (arrows, space, esc), touch swipe |
| Progress | Automatic reading progress tracking |
| Settings | Background color (white/dark/sepia), image quality, zoom slider |

**Components:** `ChapterReader`, `ImageViewer`, `ChapterNavigation`, `ReadingSettings`, `ReadingProgress`

---

### Phase 5: Bookmarks Management

**File:** `src/app/(root)/bookmarks/page.tsx`

| Feature     | Details                               |
| ----------- | ------------------------------------- |
| Views       | Grid/list toggle                      |
| Cards       | Progress indicator, last read chapter |
| Filtering   | By status (Reading, Completed, etc.)  |
| Sorting     | Date, title, progress                 |
| Search      | Search within bookmarks               |
| Empty State | Helpful empty state with CTA          |

**Components:** `BookmarkCard`, `BookmarkFilters`, `BookmarkSearch`, `BookmarkViewToggle`

---

### Phase 6+: Advanced Features

- Comment discussions on chapters
- User ratings and reviews
- Reading notifications
- User recommendations
- Social features (following, sharing)
- Admin management panel with RBAC
- Full-text search
- Image optimization pipeline

---
