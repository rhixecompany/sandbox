# Complete Implementation Phases

> Extracted from `plan-dev.prompt.md`.

## Complete Implementation Phases

### Phase 1: IMMEDIATE - Fix TypeScript Errors (1-2 hours)

**Goal:** Achieve zero TypeScript compilation errors

#### Task 1.1: Fix DAL Base Class

- Review `src/dal/base-dal.ts`
- Verify class export and generic typing
- Ensure proper inheritance chain
- **Time:** 20 min | **Complexity:** Low

#### Task 1.2: Fix Comic DAL

- Import BaseDal correctly
- Define ComicType enum handling
- Add missing DalOptions type
- Fix status property comparisons
- **Time:** 30 min | **Complexity:** Medium

#### Task 1.3: Fix Other DAL Files

- Apply pattern to rating-dal.ts, comment-dal.ts
- Fix type mismatches and imports
- **Time:** 20 min | **Complexity:** Medium

#### Task 1.4: Fix Auth System

- Resolve callback signature issues
- Align User types with @auth/core
- **Time:** 20 min | **Complexity:** Medium

#### Task 1.5: Fix Chart Component

- Add proper Recharts type guards
- Implement unknown payload handling
- Document rationale with ESLint comments
- **Time:** 20 min | **Complexity:** High

#### Task 1.6: Validation

- Run `pnpm type-check` → 0 errors
- Run `pnpm lint:fix` → auto-fix formatting
- Run `pnpm build` → succeeds
- **Time:** 20 min | **Complexity:** Low

---

### Phase 2: Verify & Deploy Foundation (1-2 hours)

**Goal:** Confirm database, auth, and infrastructure working

#### Task 2.1: Database Setup

- Verify `.env.local` configuration
- Run `pnpm db:push` for schema
- Test database connection
- **Time:** 20 min | **Complexity:** Low

#### Task 2.2: Development Environment

- Start dev server: `pnpm dev`
- Verify no startup errors
- Check hot module reloading
- **Time:** 15 min | **Complexity:** Low

#### Task 2.3: Authentication Flow Test

- Test NextAuth configuration
- Verify provider setup (Google, GitHub)
- Test credentials login
- **Time:** 20 min | **Complexity:** Medium

#### Task 2.4: Base DAL Testing

- Create simple test for BaseDal
- Test basic CRUD pattern
- Verify eager loading with `.with()`
- **Time:** 30 min | **Complexity:** Medium

---

### Phase 3: User Profile Features (4-6 hours)

**Goal:** Complete user profile system with edit/settings

#### Task 3.1: Profile View Page (`src/app/(root)/profile/page.tsx`)

**Components:** ProfileHeader, ProfileStats, RecentActivity, ProfileActions

- Server Component for data fetching
- Display user info, stats, activity
- Link to edit/settings
- Responsive layout
- **Time:** 1.5 hours | **Complexity:** Medium

#### Task 3.2: Profile Edit Page (`src/app/(root)/profile/edit/page.tsx`)

**Components:** EditProfileForm with validation

- Update name, image, bio
- Zod validation schema
- Server Action for mutation
- Optimistic UI updates
- Error handling
- **Time:** 1.5 hours | **Complexity:** Medium

#### Task 3.3: Settings Page (`src/app/(root)/profile/settings/page.tsx`)

**Components:** NotificationSettings, PrivacySettings, ThemeSettings

- Notification preferences
- Privacy controls
- Theme selection
- Server Actions for persistence
- **Time:** 1.5 hours | **Complexity:** Medium

#### Task 3.4: Profile DAL & Actions

- Extract ProfileDal methods
- Create profile.actions.ts
- Implement useUserProfile hook
- **Time:** 1 hour | **Complexity:** Medium

#### Task 3.5: Testing & Validation

- Unit tests for ProfileDal
- Component tests for UI
- Manual testing on dev server
- **Time:** 1 hour | **Complexity:** Low

---

### Phase 4: Comic Features (6-8 hours)

**Goal:** Browse, search, filter comics with full details

#### Task 4.1: Comics Listing Page (`src/app/(root)/comics/page.tsx`)

**Components:** ComicGrid, FilterPanel, SearchBar, Pagination

- Grid layout (responsive)
- Filters: Status, Genre, Author
- Search by title
- Pagination/infinite scroll
- Server-side filtering
- **Time:** 2 hours | **Complexity:** High

#### Task 4.2: Comic Details Page (`src/app/(root)/comics/[slug]/page.tsx`)

**Components:** ComicHeader, ChapterList, RelatedComics, DetailsPanel

- Full comic information
- Chapter listing with progress
- Related comics (same genre)
- Bookmark/rating buttons
- Responsive layout
- **Time:** 1.5 hours | **Complexity:** Medium

#### Task 4.3: Bookmark Management

**Components:** BookmarkButton, BookmarkStatusDropdown, BookmarkFeedback

- Add to bookmarks (idempotent upsert)
- Status selection (Reading, Completed, etc.)
- Last read chapter tracking
- Optimistic UI updates
- **Time:** 1.5 hours | **Complexity:** Medium

#### Task 4.4: Comic DAL & Actions

- Implement full ComicDal with eager loading
- Create comic.actions.ts
- Search and filter methods
- **Time:** 1 hour | **Complexity:** High

#### Task 4.5: Testing & Validation

- Mock data seeding
- Component tests
- Manual UI testing
- **Time:** 1 hour | **Complexity:** Low

---

### Phase 5: Chapter Reader (3-4 hours)

**Goal:** Full-featured comic chapter reader with progress tracking

#### Task 5.1: Chapter Reader Page (`src/app/(root)/comics/[slug]/[chapterNumber]/page.tsx`)

**Components:** ChapterViewer, ImageViewer, NavigationPanel, SettingsPanel

- Image gallery display
- Zoom controls
- Keyboard navigation (← →)
- Settings panel (brightness, theme)
- Progress tracking
- **Time:** 2 hours | **Complexity:** High

#### Task 5.2: Chapter Navigation

**Components:** ChapterNav, PageIndicator

- Previous/next chapter links
- Page indicator
- Thumbnail preview
- **Time:** 1 hour | **Complexity:** Low

#### Task 5.3: Reading Progress Tracking

- Track current chapter/page
- Persist scroll position
- "Continue reading" feature
- Last read timestamp
- **Time:** 1 hour | **Complexity:** Medium

---

### Phase 6: Bookmarks Management (2-3 hours)

**Goal:** User's reading list with filtering and organization

#### Task 6.1: Bookmarks Page (`src/app/(root)/bookmarks/page.tsx`)

**Components:** BookmarkGrid, BookmarkCard, FilterPanel

- Grid/list view toggle
- Filter by status (Reading, Completed, etc.)
- Search bookmarks
- Progress indicators
- Sort by (date, rating, progress)
- **Time:** 1.5 hours | **Complexity:** Medium

#### Task 6.2: Bookmark Components

- Improve BookmarkCard display
- Add progress bar
- Show last read info
- Quick status update
- **Time:** 0.75 hours | **Complexity:** Low

#### Task 6.3: Bookmark DAL & Actions

- Complete BookmarkDal
- Implement filtering/sorting
- **Time:** 0.75 hours | **Complexity:** Medium

---

### Phase 7: Admin Features (4-6 hours)

**Goal:** Admin dashboard with comics, users, moderation

#### Task 7.1: Admin Dashboard (`src/app/admin/page.tsx`)

**Components:** StatsPanel, RecentActivity, QuickActions

- Key metrics (comics, users, comments)
- Recent activity feed
- Quick action buttons
- **Time:** 1 hour | **Complexity:** Medium

#### Task 7.2: Comics Management

- List, create, edit, delete comics
- TanStack Table for data grid
- Bulk actions
- Image upload
- **Time:** 1.5 hours | **Complexity:** High

#### Task 7.3: Users Management

- User listing with search
- Role assignment
- Ban/deactive users
- View user statistics
- **Time:** 1 hour | **Complexity:** Medium

#### Task 7.4: Moderation Panel

- Comment moderation
- Rating management
- Content flags
- **Time:** 1 hour | **Complexity:** High

#### Task 7.5: Admin Testing

- Auth checks (admin only)
- CRUD operations
- Bulk operations
- **Time:** 1 hour | **Complexity:** Low

---

### Phase 8: Testing & Optimization (3-4 hours)

**Goal:** 80%+ coverage, performance optimization

#### Task 8.1: Unit Tests

- DAL tests (database operations)
- Action tests (server actions)
- Hook tests (custom hooks)
- Utility tests
- **Target:** 70%+ coverage
- **Time:** 1.5 hours | **Complexity:** Medium

#### Task 8.2: Component Tests

- UI component tests
- Form validation tests
- Error boundary tests
- **Target:** 60%+ coverage
- **Time:** 1 hour | **Complexity:** Medium

#### Task 8.3: E2E Tests (Playwright)

- Critical user flows
- Authentication flow
- Reading flow
- Admin operations
- **Target:** 80%+ scenarios
- **Time:** 1 hour | **Complexity:** High

#### Task 8.4: Performance Optimization

- Image optimization (next/image defaults)
- Bundle analysis
- Database query optimization
- Caching strategy
- **Time:** 0.5 hours | **Complexity:** Medium

---

### Phase 9: Documentation & Deployment (2-3 hours)

**Goal:** Complete documentation and production deployment

#### Task 9.1: Documentation

- README with setup instructions
- API reference
- Database schema documentation
- Deployment guide
- **Time:** 1 hour | **Complexity:** Low

#### Task 9.2: Deployment Preparation

- Environment configuration (.env.production)
- GitHub Actions CI/CD setup
- Vercel deployment config
- Database migration scripts
- **Time:** 1 hour | **Complexity:** Medium

#### Task 9.3: Final Validation

- Production build test
- All tests passing (80%+ coverage)
- Zero errors in type-check
- Zero ESLint violations
- Core Web Vitals meeting targets
- **Time:** 0.5 hours | **Complexity:** Low

---
