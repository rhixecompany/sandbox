---
agent: "Next.js Expert"
description: "Comprehensive ComicWise development plan with database architecture, feature implementation, quality gates, and systematic task execution"
model: "Claude Haiku 4.5"
tools:
  [
    "vscode",
    "execute",
    "read",
    "agent",
    "edit",
    "search",
    "file_management",
    "terminal",
    "runSubagent",
    "manage_todo_list"
  ]
---

# ComicWise Development Master Plan (v6.0)

**Purpose:** Unified development guide consolidating database architecture, implementation workflows, quality gates, and complete task execution strategy.

**Last Updated:** March 1, 2026  
**Framework:** Next.js 16 + React Server Components + Drizzle ORM + TypeScript  
**Total Estimated Duration:** 25-37 hours | **By Phase:** See Breakdown Below

---

## Table of Contents

1. [Executive Summary & Current Status](#executive-summary--current-status)
2. [Critical Path & Blockers](#critical-path--blockers)
3. [Complete Implementation Phases](#complete-implementation-phases)
4. [Database Architecture Reference](#database-architecture-reference)
5. [Development Workflow & Quality Gates](#development-workflow--quality-gates)
6. [Task Execution Strategy](#task-execution-strategy)

---

## Executive Summary & Current Status

### Project Overview

**ComicWise** is a modern comic reading platform with:

- Reader features: Browse, search, read, bookmark, rate comics
- Creator features: Upload and manage content
- Admin features: Full CRUD, user management, moderation
- Tech Stack: Next.js 16 + React 19 + PostgreSQL + Drizzle ORM + TypeScript 5.x

### Current Progress

| Component | Status | Notes |
| --- | --- | --- |
| Infrastructure & Config | ✅ Complete | .env, VS Code setup, eslint config |
| Database Schema (19 tables) | ✅ Complete | All tables defined, migrations ready |
| Authentication System | ✅ Complete | NextAuth v5 with role-based access |
| Base DAL Pattern | ✅ Complete | `BaseDal<T>` established |
| **TypeScript Validation** | 🔴 **BLOCKER** | 20+ errors in DAL files - MUST FIX FIRST |
| Core Component Structure | ⏳ Pending | Awaiting TypeScript clearance |
| Feature Implementation | ⏳ Pending | 5 phases: User → Comics → Reader → Bookmarks → Admin |
| Testing & Documentation | ⏳ Pending | Post-feature implementation |
| Deployment | ⏳ Pending | Final phase after validation |

### Success Criteria (Must ALL Pass)

- ✅ Zero TypeScript errors (`pnpm type-check`)
- ✅ Zero ESLint errors (`pnpm lint`)
- ✅ 80%+ test coverage
- ✅ Production build succeeds
- ✅ All pages functional and accessible
- ✅ Core Web Vitals passing

**TOTAL ESTIMATED EFFORT:** 25-37 hours across 9 phases

---

## Critical Path & Blockers

### BLOCKER #1: TypeScript Compilation 🔴 CRITICAL

**Status:** Cannot proceed until resolved  
**Affected Files:**

- `src/dal/base-dal.ts` - Base class definition
- `src/dal/comic-dal.ts` - 15+ errors
- `src/dal/rating-dal.ts` - 3+ errors
- `src/dal/comment-dal.ts` - 2+ errors
- `src/auth.ts` - Auth callback signature issues
- `src/components/ui/chart.tsx` - Recharts type issues

**Required Actions:**

1. Fix DAL imports and type definitions
2. Resolve auth callback signatures
3. Add proper Recharts type guards
4. Run `pnpm type-check` - must show 0 errors
5. Unblock remaining features

**Time Estimate:** 1-2 hours

### BLOCKER #2: Feature Verification 🟡 YELLOW

**Status:** Phases 3-5 marked complete but unverified  
**Required Actions:**

1. Run dev server: `pnpm dev`
2. Test all routes manually
3. Verify database connectivity
4. Check API functionality

**Time Estimate:** 1-2 hours

---

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

## Database Architecture Reference

### Key Tables & Relationships

| Table | Primary Purpose | Key Constraint | Cascades To |
| --- | --- | --- | --- |
| `user` | User accounts | Email unique | 10+ tables |
| `comic` | Comic entries | Title/slug unique | chapter, images, bookmarks, ratings |
| `chapter` | Comic chapters | (comicId, chapterNumber) unique | images, reading_progress, comments |
| `bookmark` | Reading list | Composite (userId, comicId) | None (idempotent) |
| `readingProgress` | Reading position | Per (user, comic) | None (update-only) |
| `comment` | Discussions | With parentId for replies | None (soft delete) |
| `notification` | User alerts | Linked to comic/chapter | None |

### Critical Query Patterns

```typescript
// Get comic with relationships
const comic = await db.query.comic.findFirst({
  where: eq(comic.slug, slug),
  with: {
    author: true,
    artist: true,
    genres: { with: { genre: true } },
    chapters: { orderBy: [c => desc(c.chapterNumber)] }
  }
});

// Get user's bookmarks
const bookmarks = await db.query.bookmark.findMany({
  where: eq(bookmark.userId, userId),
  with: { comic: true, lastReadChapter: true },
  orderBy: b => desc(b.updatedAt)
});
```

### N+1 Solution Pattern

```typescript
// ❌ WRONG: Loops and queries individually (N+1)
const comics = await db.select().from(comic);
for (const c of comics) {
  c.author = await db.select().from(author).where(...);
}

// ✅ CORRECT: Use .with() for eager loading
const comics = await db.query.comic.findMany({
  with: { author: true, genres: { with: { genre: true } } }
});
```

---

## Development Workflow & Quality Gates

### Before Each Feature Implementation

1. **Create Zod Schema** (validation)

   ```typescript
   // src/schemas/feature-schema.ts
   export const createSchema = z.object({
     field1: z.string().min(1),
     field2: z.number()
   });
   export type CreateInput = z.infer<typeof createSchema>;
   ```

2. **Create DAL Class** (if new entity)

   ```typescript
   // src/dal/feature-dal.ts
   export class FeatureDal extends BaseDal<FeatureType> {
     async create(data: CreateInput) {
       /* ... */
     }
   }
   ```

3. **Create Server Actions** (mutations)

   ```typescript
   // src/actions/feature-actions.ts
   "use server";
   export async function createFeatureAction(input: unknown) {
     const parsed = schema.safeParse(input);
     if (!parsed.success) return { ok: false, error: "..." };
     try {
       const result = await featureDal.create(parsed.data);
       revalidatePath("/feature");
       return { ok: true, data: result };
     } catch (error) {
       return { ok: false, error: "Failed to create" };
     }
   }
   ```

4. **Create UI Components** (server + client)

   ```typescript
   // src/components/feature-list.tsx (Server Component)
   async function FeatureList() {
     const items = await featureDal.list();
     return <FeatureListClient items={items} />;
   }

   // src/components/feature-list-client.tsx ('use client')
   export function FeatureListClient({ items }) {
     return <div>{items.map(...)}</div>;
   }
   ```

5. **Add Tests** (unit + component)
   ```typescript
   // src/tests/feature.spec.ts
   describe("Feature", () => {
     it("validates correctly", () => {
       /* ... */
     });
   });
   ```

### Quality Gate Checklist (Before Each Commit)

```bash
# Type safety
pnpm type-check          # Must: 0 errors

# Code quality
pnpm lint:fix            # Must: auto-fix all issues
pnpm format              # Auto-format code

# Testing
pnpm test                # Must: all tests pass
                         # Goal: 80%+ coverage

# Build validation
pnpm build --debug-prerender  # Must: succeeds

# Performance checks
pnpm analyze             # Verify bundle size
```

### Token Management Strategy

To avoid rate limiting:

1. **Work in focused batches** - Group 3-4 related edits per batch
2. **Use efficient prompts** - Be specific about what you need
3. **Cache context** - Reference files once, reuse knowledge
4. **Complete features** - Finish one feature before moving to next
5. **Batch fixes** - Group similar fixes together
6. **Monitor token usage** - Check copilot status periodically

---

## Task Execution Strategy

### Implementation Order

**PHASE 1 (BLOCKING):** Fix TypeScript errors → Everything else depends on this

**PHASE 2 (FOUNDATION):** Verify database, auth, dev environment

**PHASES 3-7 (FEATURES):** Implement features in order (User → Comics → Reader → Bookmarks → Admin)

**PHASE 8 (QUALITY):** Testing and performance optimization

**PHASE 9 (DEPLOYMENT):** Documentation and production deployment

### Systematic Approach

For each task:

1. **Create Zod schema** if new entity
2. **Create/update DAL** with proper eager loading
3. **Create server actions** with validation and error handling
4. **Build UI components** (server + client as needed)
5. **Add tests** hitting 80%+ coverage goal
6. **Manual testing** in dev environment
7. **Commit** with clear message linking to task

### Token Efficiency Tips

- **Parallel reads:** Read multiple files at once when planning
- **Batch edits:** Make multiple edits with single tool call
- **Focused prompts:** Ask for specific guidance, not broad reviews
- **Cache knowledge:** Reference files once, reuse understanding
- **Complete features:** Finish one before starting next
- **Avoid re-asks:** Plan implementation before requesting

---

## Quick Reference: Core Patterns

### Server Action Pattern

```typescript
"use server";
type ActionResult<T> =
  | { ok: true; data: T }
  | { ok: false; error: string };

export async function myAction(
  input: unknown
): Promise<ActionResult<MyType>> {
  const session = await auth();
  if (!session?.user?.id)
    return { ok: false, error: "Not authenticated" };

  const parsed = schema.safeParse(input);
  if (!parsed.success)
    return { ok: false, error: parsed.error.errors[0]?.message };

  try {
    const result = await dal.create(parsed.data);
    revalidatePath("/path");
    return { ok: true, data: result };
  } catch (error) {
    console.error("[myAction]", error);
    return { ok: false, error: "Operation failed" };
  }
}
```

### DAL Pattern

```typescript
export class MyDal extends BaseDal<MyType> {
  async list(options?: { limit?: number; offset?: number }) {
    return db.query.myTable.findMany({
      limit: options?.limit ?? 20,
      offset: options?.offset ?? 0,
      with: {
        /* eager load relationships */
      },
      orderBy: t => desc(t.createdAt)
    });
  }

  async getById(id: number) {
    return db.query.myTable.findFirst({
      where: eq(myTable.id, id),
      with: {
        /* relationships */
      }
    });
  }
}
```

### Protected Route Pattern

```typescript
import { auth } from "@/auth";
import { redirect } from "next/navigation";

export default async function AdminPage() {
  const session = await auth();
  if (!session?.user) redirect("/auth/signin");

  const user = session.user as { role?: unknown };
  if (typeof user.role !== "string" || user.role !== "admin") {
    redirect("/");
  }

  return <div>Admin Content</div>;
}
```

---

## Success Metrics

### Phase-by-Phase Success Criteria

| Phase | Success Criteria | Validation Method |
| --- | --- | --- |
| 1 | `pnpm type-check` = 0 errors | CI command output |
| 2 | Dev server starts, db connected | Manual testing |
| 3 | Profile pages work, auth flows complete | Manual testing + unit tests |
| 4 | All comic pages render, search/filter work | Manual testing + component tests |
| 5 | Reader works with progress tracking | Manual testing |
| 6 | Bookmarks CRUD and filtering work | Manual testing |
| 7 | Admin CRUD operations work, role checks pass | Manual testing + integration tests |
| 8 | 80%+ test coverage achieved | Coverage report |
| 9 | Prod build succeeds, deployed | Build output + deployment verification |

### Overall Success Criteria (ALL must pass)

- ✅ Zero TypeScript errors
- ✅ Zero ESLint errors
- ✅ 80%+ test coverage
- ✅ Production build succeeds
- ✅ All pages functional
- ✅ Core Web Vitals passing
- ✅ Deployment successful

---

**NEXT STEP:** Begin Phase 1 - Fix TypeScript compilation errors. This is the blocking issue preventing all other work. See Phase 1 tasks above for detailed steps.
