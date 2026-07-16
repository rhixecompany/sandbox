---
goal: "Master Phase Plan — All Phase Tasks & Micro-Tasks with checkpoints, recovery points, code samples, diffs, and file references for ComicWise Phases 4.3–6"
version: 1.0
date_created: 2026-03-08
last_updated: 2026-03-08
owner: ComicWise Dev Team
status: "Planned"
tags: [process, master-plan, phases, implementation, architecture]
---

# Master Phase Plan: ComicWise Phases 4.3–6

![Status: Planned](https://img.shields.io/badge/status-Planned-blue)

This is the **Master Phase Plan** for ComicWise, consolidating all remaining work from the completed phases through future phases. It lists every task and micro-task with built-in checkpoints (**CP**) and recovery points (**RP**) for safe, incremental progress. Code samples with diffs and file references are provided where implementation patterns are non-obvious.

**Completed Phases:**

- Phase 1 (Foundation) ✅ | Phase 2 (User Profile) ✅ | Phase 3 (Comics) ✅
- Phase 4 (Chapter Reader) ✅ | Phase 5 (Bookmarks) ✅
- Phase 4.1 (Design System) ✅ | Phase 4.2 (Advanced Search) ✅

**Current Quality Gate:** 0 TS errors | 241/241 tests | Production build passing

---

## 1. Requirements & Constraints

- **REQ-001**: Every phase must maintain the quality gate: `pnpm type-check && pnpm lint:fix && pnpm test && pnpm build`
- **REQ-002**: Each phase must be independently deployable — no half-finished features in production
- **REQ-003**: Database migrations must be backward-compatible (add columns, don't remove until deprecated)
- **REQ-004**: New features must have ≥80% test coverage (unit tests via Vitest)
- **REQ-005**: All new components must support dark mode and meet WCAG 2.1 AA accessibility
- **REQ-006**: Each checkpoint must include a commit with the quality gate passing
- **SEC-001**: New API endpoints or Server Actions must validate authentication first
- **SEC-002**: User input must be Zod-validated before database operations
- **CON-001**: Must not regress existing 241 tests
- **CON-002**: Must maintain backward compatibility with existing URLs/bookmarks
- **GUD-001**: Follow existing DAL pattern, Server Action pattern, and component structure
- **PAT-001**: Data flow: Server Component → DAL (eager load with `.with()`) → props → Client Component

---

## 2. Implementation Steps

---

### CLEANUP SPRINT (Pre-Phase 4.3) — Workspace Hygiene

- GOAL-CLN: Execute the 5 cleanup plans created in this session before starting new features

| Task | Description | Completed | Date |
| --- | --- | --- | --- |
| TASK-CLN-001 | Execute `process-vscode-config-audit-1.md` — Clean all `.vscode/*.json` files (49 tasks) | ⬜ | |
| TASK-CLN-002 | Execute `process-docs-triage-cleanup-1.md` — Triage 84 docs files (63 tasks) | ⬜ | |
| TASK-CLN-003 | Execute `process-app-routes-triage-1.md` — Clean 52 route files (29 tasks) | ⬜ | |
| TASK-CLN-004 | Execute `process-components-triage-1.md` — Clean 153 component files (32 tasks) | ⬜ | |
| TASK-CLN-005 | Execute `process-scripts-triage-1.md` — Clean 49 script files (42 tasks) | ⬜ | |

> **CP-CLN** (Checkpoint): Quality gate passes, workspace is clean, all cruft removed **RP-CLN** (Recovery): Git branch `cleanup/workspace-hygiene` — can be abandoned without affecting main

---

## Phase 4.3: Reading Analytics & History

- GOAL-4.3: Implement user reading analytics, history tracking, and engagement metrics dashboard

### 4.3.1 — Database Schema Extension

| Task | Description | Completed | Date |
| --- | --- | --- | --- |
| TASK-4.3.1-001 | Create `readingHistory` table in `src/database/schema.ts` | ⬜ | |
| TASK-4.3.1-002 | Add `timeSpentSeconds` column to existing `readingProgress` table | ⬜ | |
| TASK-4.3.1-003 | Run `pnpm db:generate` to create migration SQL | ⬜ | |
| TASK-4.3.1-004 | Run `pnpm db:push` to apply schema changes | ⬜ | |

**Code Sample — Schema Addition:**

```diff
// src/database/schema.ts
+ export const readingHistory = pgTable("reading_history", {
+   id: serial("id").primaryKey(),
+   userId: text("user_id")
+     .notNull()
+     .references(() => user.id, { onDelete: "cascade" }),
+   comicId: integer("comic_id")
+     .notNull()
+     .references(() => comic.id, { onDelete: "cascade" }),
+   chapterId: integer("chapter_id")
+     .notNull()
+     .references(() => chapter.id, { onDelete: "cascade" }),
+   startedAt: timestamp("started_at").defaultNow().notNull(),
+   finishedAt: timestamp("finished_at"),
+   timeSpentSeconds: integer("time_spent_seconds").default(0),
+   pagesRead: integer("pages_read").default(0),
+   totalPages: integer("total_pages").default(0),
+   createdAt: timestamp("created_at").defaultNow().notNull(),
+ });
+
+ export const readingHistoryRelations = relations(readingHistory, ({ one }) => ({
+   user: one(user, { fields: [readingHistory.userId], references: [user.id] }),
+   comic: one(comic, { fields: [readingHistory.comicId], references: [comic.id] }),
+   chapter: one(chapter, { fields: [readingHistory.chapterId], references: [chapter.id] }),
+ }));
```

> **CP-4.3.1** (Checkpoint): `pnpm type-check` passes, `pnpm db:push` succeeds, no test regressions **RP-4.3.1** (Recovery): `pnpm db:reset` reverts schema; branch `feature/reading-analytics-schema`

### 4.3.2 — Data Access Layer

| Task | Description | Completed | Date |
| --- | --- | --- | --- |
| TASK-4.3.2-001 | Create `src/dal/reading-history-dal.ts` extending `BaseDal<ReadingHistoryType>` | ⬜ | |
| TASK-4.3.2-002 | Implement `recordSession(userId, comicId, chapterId, timeSpent, pagesRead)` | ⬜ | |
| TASK-4.3.2-003 | Implement `getHistory(userId, { limit, offset })` with eager loading `.with({ comic, chapter })` | ⬜ | |
| TASK-4.3.2-004 | Implement `getStats(userId)` — total time, chapters read, comics completed, favorite genres | ⬜ | |
| TASK-4.3.2-005 | Implement `getRecentlyRead(userId, limit)` — last 10 unique comics read | ⬜ | |
| TASK-4.3.2-006 | Implement `getReadingStreak(userId)` — consecutive days with reading activity | ⬜ | |

**Code Sample — DAL Pattern:**

```typescript
// src/dal/reading-history-dal.ts
import { BaseDal } from "./base-dal";
import { db } from "database/db";
import { eq, desc, sql, and, gte } from "drizzle-orm";
import { readingHistory } from "database/schema";

type ReadingHistoryType = typeof readingHistory.$inferSelect;

export class ReadingHistoryDal extends BaseDal<ReadingHistoryType> {
  async recordSession(data: {
    userId: string;
    comicId: number;
    chapterId: number;
    timeSpentSeconds: number;
    pagesRead: number;
    totalPages: number;
  }): Promise<ReadingHistoryType> {
    const [record] = await db
      .insert(readingHistory)
      .values({
        ...data,
        finishedAt:
          data.pagesRead >= data.totalPages ? new Date() : null
      })
      .returning();
    return record;
  }

  async getHistory(userId: string, limit = 20, offset = 0) {
    return db.query.readingHistory.findMany({
      where: eq(readingHistory.userId, userId),
      with: { comic: true, chapter: true },
      orderBy: [desc(readingHistory.startedAt)],
      limit,
      offset
    });
  }

  async getRecentlyRead(userId: string, limit = 10) {
    return db.query.readingHistory.findMany({
      where: eq(readingHistory.userId, userId),
      with: { comic: true, chapter: true },
      orderBy: [desc(readingHistory.startedAt)],
      limit
    });
  }
}

export const readingHistoryDal = new ReadingHistoryDal();
```

> **CP-4.3.2** (Checkpoint): `pnpm type-check` passes, DAL methods compile **RP-4.3.2** (Recovery): Delete `reading-history-dal.ts`, no other files affected

### 4.3.3 — Zod Schemas

| Task | Description | Completed | Date |
| --- | --- | --- | --- |
| TASK-4.3.3-001 | Create `src/schemas/reading-history.schema.ts` with `RecordReadingSessionSchema` | ⬜ | |
| TASK-4.3.3-002 | Create `ReadingHistoryFilterSchema` (date range, comic filter, pagination) | ⬜ | |
| TASK-4.3.3-003 | Write schema validation tests in `src/tests/schemas/reading-history-schema.spec.ts` | ⬜ | |

**Code Sample — Schema:**

```typescript
// src/schemas/reading-history.schema.ts
import { z } from "zod";

export const RecordReadingSessionSchema = z.object({
  comicId: z.number().int().positive(),
  chapterId: z.number().int().positive(),
  timeSpentSeconds: z.number().int().min(0).max(86400),
  pagesRead: z.number().int().min(0),
  totalPages: z.number().int().min(1)
});

export const ReadingHistoryFilterSchema = z.object({
  startDate: z.string().datetime().optional(),
  endDate: z.string().datetime().optional(),
  comicId: z.number().int().positive().optional(),
  page: z.number().int().min(1).default(1),
  limit: z.number().int().min(1).max(100).default(20)
});

export type RecordReadingSession = z.infer<
  typeof RecordReadingSessionSchema
>;
export type ReadingHistoryFilter = z.infer<
  typeof ReadingHistoryFilterSchema
>;
```

> **CP-4.3.3** (Checkpoint): Schema tests pass, type-check passes

### 4.3.4 — Server Actions

| Task | Description | Completed | Date |
| --- | --- | --- | --- |
| TASK-4.3.4-001 | Create `src/actions/reading-history.actions.ts` | ⬜ | |
| TASK-4.3.4-002 | Implement `recordReadingSessionAction(input)` — auth → validate → DAL → revalidate | ⬜ | |
| TASK-4.3.4-003 | Implement `getReadingHistoryAction(filter)` — auth → validate → DAL | ⬜ | |
| TASK-4.3.4-004 | Implement `getReadingStatsAction()` — auth → DAL (aggregations) | ⬜ | |
| TASK-4.3.4-005 | Write action tests in `src/tests/reading-history.actions.test.ts` | ⬜ | |

**Code Sample — Server Action:**

```typescript
// src/actions/reading-history.actions.ts
"use server";

import { auth } from "@/auth";
import { RecordReadingSessionSchema } from "schemas/reading-history.schema";
import { readingHistoryDal } from "@/dal/reading-history-dal";
import { revalidatePath } from "next/cache";
import type { ActionResult } from "./types";

export async function recordReadingSessionAction(
  input: unknown
): Promise<ActionResult<{ id: number }>> {
  const session = await auth();
  if (!session?.user?.id)
    return { ok: false, error: "Not authenticated" };

  const parsed = RecordReadingSessionSchema.safeParse(input);
  if (!parsed.success)
    return {
      ok: false,
      error: parsed.error.errors[0]?.message ?? "Invalid input"
    };

  try {
    const record = await readingHistoryDal.recordSession({
      userId: session.user.id,
      ...parsed.data
    });
    revalidatePath("/reading-progress");
    return { ok: true, data: { id: record.id } };
  } catch {
    return { ok: false, error: "Failed to record reading session" };
  }
}
```

> **CP-4.3.4** (Checkpoint): All action tests pass, type-check 0 errors, lint clean **RP-4.3.4** (Recovery): Delete action file and test file

### 4.3.5 — UI Components

| Task | Description | Completed | Date |
| --- | --- | --- | --- |
| TASK-4.3.5-001 | Create `src/components/analytics/reading-dashboard.tsx` — Main analytics page component | ⬜ | |
| TASK-4.3.5-002 | Create `src/components/analytics/reading-timeline.tsx` — Chronological reading history | ⬜ | |
| TASK-4.3.5-003 | Create `src/components/analytics/reading-stats-overview.tsx` — Stats cards (total time, chapters, streak) | ⬜ | |
| TASK-4.3.5-004 | Create `src/components/analytics/recently-read-widget.tsx` — Sidebar widget for recent comics | ⬜ | |
| TASK-4.3.5-005 | Create `src/components/analytics/reading-goals.tsx` — Set and track reading goals | ⬜ | |
| TASK-4.3.5-006 | Create `src/components/analytics/index.ts` | ⬜ | |

> **CP-4.3.5** (Checkpoint): All components render without errors, dark mode works, type-check passes

### 4.3.6 — Page Routes

| Task | Description | Completed | Date |
| --- | --- | --- | --- |
| TASK-4.3.6-001 | Update `src/app/(root)/reading-progress/page.tsx` to include analytics dashboard | ⬜ | |
| TASK-4.3.6-002 | Add `loading.tsx` and `error.tsx` for reading-progress route | ⬜ | |
| TASK-4.3.6-003 | Add metadata for SEO | ⬜ | |
| TASK-4.3.6-004 | Integrate `recently-read-widget.tsx` into sidebar or home page | ⬜ | |

> **CP-4.3.6** (Checkpoint): Full quality gate passes: type-check ✅, lint ✅, test ✅, build ✅ **RP-4.3.6** (Recovery): Revert to commit at CP-4.3.5

### 4.3.7 — Integration with Chapter Reader

| Task | Description | Completed | Date |
| --- | --- | --- | --- |
| TASK-4.3.7-001 | Update `ChapterReader` component to call `recordReadingSessionAction` on chapter completion | ⬜ | |
| TASK-4.3.7-002 | Track time spent per chapter (start timer on mount, stop on unmount/navigate) | ⬜ | |
| TASK-4.3.7-003 | Track pages read (count image views) | ⬜ | |

> **CP-4.3** (PHASE CHECKPOINT): All Phase 4.3 features working, quality gate passes, commit tagged `phase-4.3`

---

## Phase 4.4: Social Features (Reviews, Ratings, Sharing)

- GOAL-4.4: Add user reviews, enhanced ratings, and social sharing capabilities

### 4.4.1 — Database Schema

| Task | Description | Completed | Date |
| --- | --- | --- | --- |
| TASK-4.4.1-001 | Add `review` table to `src/database/schema.ts` (userId, comicId, title, body, rating, helpfulCount, createdAt, updatedAt) | ⬜ | |
| TASK-4.4.1-002 | Add `reviewVote` table (userId, reviewId, isHelpful) for helpful/not helpful votes | ⬜ | |
| TASK-4.4.1-003 | Add relations for new tables | ⬜ | |
| TASK-4.4.1-004 | Run `pnpm db:generate && pnpm db:push` | ⬜ | |

> **CP-4.4.1** (Checkpoint): Schema applied, type-check passes

### 4.4.2 — DAL + Schemas + Actions

| Task | Description | Completed | Date |
| --- | --- | --- | --- |
| TASK-4.4.2-001 | Create `src/dal/review-dal.ts` with CRUD + vote operations | ⬜ | |
| TASK-4.4.2-002 | Create `src/schemas/review.schema.ts` with `CreateReviewSchema`, `UpdateReviewSchema`, `ReviewFilterSchema` | ⬜ | |
| TASK-4.4.2-003 | Create `src/actions/review.actions.ts` with `createReviewAction`, `updateReviewAction`, `deleteReviewAction`, `voteReviewAction` | ⬜ | |
| TASK-4.4.2-004 | Write schema validation tests | ⬜ | |
| TASK-4.4.2-005 | Write action tests | ⬜ | |

> **CP-4.4.2** (Checkpoint): Tests pass, type-check clean

### 4.4.3 — UI Components

| Task | Description | Completed | Date |
| --- | --- | --- | --- |
| TASK-4.4.3-001 | Create `src/components/reviews/review-section.tsx` — Review list for comic detail page | ⬜ | |
| TASK-4.4.3-002 | Create `src/components/reviews/review-card.tsx` — Individual review display with vote buttons | ⬜ | |
| TASK-4.4.3-003 | Create `src/components/reviews/review-form.tsx` — Create/edit review form | ⬜ | |
| TASK-4.4.3-004 | Create `src/components/reviews/review-sort.tsx` — Sort by helpful, recent, rating | ⬜ | |
| TASK-4.4.3-005 | Update `src/app/(root)/comics/[slug]/page.tsx` to include review section | ⬜ | |

> **CP-4.4** (PHASE CHECKPOINT): Quality gate passes, reviews working end-to-end

---

## Phase 4.5: Mobile-First Optimization

- GOAL-4.5: Optimize for mobile devices, add touch gestures, prepare for PWA

| Task | Description | Completed | Date |
| --- | --- | --- | --- |
| TASK-4.5-001 | Audit all pages for mobile responsiveness (viewport test: 320px, 375px, 414px) | ⬜ | |
| TASK-4.5-002 | Add touch swipe gesture support to chapter reader (left/right for page navigation) | ⬜ | |
| TASK-4.5-003 | Add pinch-to-zoom support in chapter reader | ⬜ | |
| TASK-4.5-004 | Create `public/manifest.webmanifest` for PWA support | ⬜ | |
| TASK-4.5-005 | Add PWA meta tags to root layout | ⬜ | |
| TASK-4.5-006 | Create service worker for offline reading (cache recently read chapters) | ⬜ | |
| TASK-4.5-007 | Optimize images for mobile (responsive `sizes` attribute, lazy loading) | ⬜ | |
| TASK-4.5-008 | Test touch targets (minimum 44x44px per WCAG 2.5.5) | ⬜ | |
| TASK-4.5-009 | Add mobile-specific bottom navigation bar | ⬜ | |
| TASK-4.5-010 | Performance audit: Lighthouse mobile score ≥ 90 | ⬜ | |

> **CP-4.5** (PHASE CHECKPOINT): Mobile viewport tested, Lighthouse ≥ 90, quality gate passes

---

## Phase 6: Advanced Features (Deferred)

- GOAL-6: Implement remaining advanced features based on priority

### 6.1 — Comments & Discussion

| Task | Description | Completed | Date |
| --- | --- | --- | --- |
| TASK-6.1-001 | Implement comment threading (parent_id column already exists in schema) | ⬜ | |
| TASK-6.1-002 | Add `@username` mention support with autocomplete | ⬜ | |
| TASK-6.1-003 | Add comment reactions (like, love) via `commentReaction` table | ⬜ | |
| TASK-6.1-004 | Add moderation tools (flag, hide, delete for admins) | ⬜ | |
| TASK-6.1-005 | Add reply notifications via existing notification system | ⬜ | |

### 6.2 — Notifications System Enhancement

| Task | Description | Completed | Date |
| --- | --- | --- | --- |
| TASK-6.2-001 | New chapter notifications (when bookmarked comic gets new chapter) | ⬜ | |
| TASK-6.2-002 | Email digest options (daily/weekly summary) | ⬜ | |
| TASK-6.2-003 | Push notifications via service worker (PWA) | ⬜ | |
| TASK-6.2-004 | Notification preferences page | ⬜ | |

### 6.3 — Admin Panel

| Task | Description | Completed | Date |
| --- | --- | --- | --- |
| TASK-6.3-001 | Comic CRUD management (create, edit, delete with confirmation) | ⬜ | |
| TASK-6.3-002 | User management (list, ban, role change) | ⬜ | |
| TASK-6.3-003 | Moderation dashboard (flagged comments, reported content) | ⬜ | |
| TASK-6.3-004 | Analytics dashboard (user signups, reading activity, popular comics) | ⬜ | |
| TASK-6.3-005 | Batch operations (bulk status change, bulk delete) | ⬜ | |

### 6.4 — Full-Text Search Enhancement

| Task | Description | Completed | Date | | ------------ | -------------------------------------------------------------------- | ⬜ | | | TASK-6.4-001 | PostgreSQL `tsvector` indexing on comic title, synopsis, author name | ⬜ | | | TASK-6.4-002 | Search result ranking with `ts_rank` | ⬜ | | | TASK-6.4-003 | Search analytics (track popular queries, zero-result queries) | ⬜ | | | TASK-6.4-004 | Search suggestions based on popular/recent queries | ⬜ | |

---

## 3. Alternatives

- **ALT-001**: Use an external analytics service (PostHog, Mixpanel) instead of custom reading analytics — rejected because reading history is core domain data that should live in the database
- **ALT-002**: Use GraphQL for review queries — rejected because the project uses Server Components + DAL pattern consistently
- **ALT-003**: Skip PWA and focus on native app — rejected because PWA provides most mobile benefits without app store overhead
- **ALT-004**: Use an ORM migration tool (Prisma Migrate) instead of Drizzle Kit — rejected because Drizzle is the established ORM

## 4. Dependencies

- **DEP-001**: PostgreSQL database (Neon) — must be running for schema migrations
- **DEP-002**: Existing `readingProgress` table — Phase 4.3 extends it with `timeSpentSeconds`
- **DEP-003**: Existing `notification` table — Phase 6.2 uses it for chapter notifications
- **DEP-004**: Existing `comment` table — Phase 6.1 extends it with threading and reactions
- **DEP-005**: Service Worker API — Phase 4.5 requires browser support for offline/PWA

## 5. Files

**Phase 4.3 (Reading Analytics):**

- `src/database/schema.ts` — Add `readingHistory` table + relations
- `src/dal/reading-history-dal.ts` — New DAL file
- `src/schemas/reading-history.schema.ts` — New Zod schemas
- `src/actions/reading-history.actions.ts` — New Server Actions
- `src/components/analytics/` — 6 new component files + index.ts
- `src/app/(root)/reading-progress/page.tsx` — Updated page
- `src/tests/schemas/reading-history-schema.spec.ts` — Schema tests
- `src/tests/reading-history.actions.test.ts` — Action tests

**Phase 4.4 (Social Features):**

- `src/database/schema.ts` — Add `review`, `reviewVote` tables
- `src/dal/review-dal.ts` — New DAL file
- `src/schemas/review.schema.ts` — New Zod schemas
- `src/actions/review.actions.ts` — New Server Actions
- `src/components/reviews/` — 5 new component files
- `src/app/(root)/comics/[slug]/page.tsx` — Updated to include reviews

**Phase 4.5 (Mobile):**

- `public/manifest.webmanifest` — PWA manifest
- `src/service-worker.ts` — Offline support
- `src/app/layout.tsx` — PWA meta tags
- Various component files for touch gesture support

## 6. Testing

- **TEST-001**: Phase 4.3 — ≥20 new tests (schema validation + action tests + component tests)
- **TEST-002**: Phase 4.4 — ≥15 new tests (review schema + review actions + integration)
- **TEST-003**: Phase 4.5 — Lighthouse mobile audit ≥ 90 on all metrics
- **TEST-004**: All phases — existing 241 tests must continue passing
- **TEST-005**: All phases — `pnpm build` must succeed after each checkpoint
- **TEST-006**: E2E — Playwright tests for critical user flows (read chapter → analytics recorded, write review → displayed)

## 7. Risks & Assumptions

- **RISK-001**: `readingHistory` table could grow very large (every page view = 1 row) — mitigation: add archiving strategy, partition by date, add indexes on (userId, startedAt)
- **RISK-002**: Time tracking may be inaccurate if user leaves tab open — mitigation: use `visibilitychange` API to pause timer when tab is hidden
- **RISK-003**: Review system could be abused (spam, offensive content) — mitigation: implement rate limiting, profanity filter, admin moderation
- **RISK-004**: PWA service worker caching may serve stale content — mitigation: use `stale-while-revalidate` strategy with version-based cache busting
- **ASSUMPTION-001**: The existing `readingProgress` table can be extended without migration issues
- **ASSUMPTION-002**: Users want to see their reading analytics (validate with user feedback)
- **ASSUMPTION-003**: Mobile users are a significant portion of the audience (manga/comic readers typically mobile-heavy)

## 8. Related Specifications / Further Reading

- [`.github/copilot-instructions.md`](../.github/copilot-instructions.md) — Complete project conventions
- [`AGENTS.md`](../AGENTS.md) — Quick reference for patterns
- [`docs/ALL_PHASES_LIST.md`](ALL_PHASES_LIST.md) — Complete phase inventory
- [`docs/database-context-map.md`](database-context-map.md) — Entity relationships
- [`docs/dev.content.md`](dev.content.md) — 26-section developer reference
- [`.github/plan/process-vscode-config-audit-1.md`](../.github/plan/process-vscode-config-audit-1.md) — VS Code config cleanup plan
- [`.github/plan/process-docs-triage-cleanup-1.md`](../.github/plan/process-docs-triage-cleanup-1.md) — Docs cleanup plan
- [`.github/plan/process-app-routes-triage-1.md`](../.github/plan/process-app-routes-triage-1.md) — Routes cleanup plan
- [`.github/plan/process-components-triage-1.md`](../.github/plan/process-components-triage-1.md) — Components cleanup plan
- [`.github/plan/process-scripts-triage-1.md`](../.github/plan/process-scripts-triage-1.md) — Scripts cleanup plan

---

**Next Steps:** See [`docs/MASTER_PHASE_PLAN_TRACKING.md`](MASTER_PHASE_PLAN_TRACKING.md) for checkpoint and task tracking.
