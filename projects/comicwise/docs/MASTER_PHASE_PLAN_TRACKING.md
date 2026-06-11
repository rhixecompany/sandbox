# Master Phase Plan Tracking

Track progress through Phases 4.3–6 with checkpoints and recovery points.

**Current Status**: 🟦 Pre-Implementation | **Date Started**: 2026-03-08 | **Quality Gate**: ✅ 241/241 tests, 0 TS errors

---

## Quick Metrics

| Metric             | Target      | Actual | Status |
| ------------------ | ----------- | ------ | ------ |
| Type Errors        | 0           | TBD    | 🔄     |
| Tests Passing      | 260+        | 241    | ⏳     |
| Dark Mode Coverage | 100%        | TBD    | 🔄     |
| Accessibility      | WCAG 2.1 AA | TBD    | 🔄     |
| Build Time         | <40s        | 35.7s  | ✅     |

---

## Phase Execution Plan

### CLEANUP SPRINT (Pre-Phase 4.3)

**Status**: ⬜ Not Started | **Priority**: 🔴 BLOCKER (before new features)

- [ ] **TASK-CLN-001**: Execute `process-vscode-config-audit-1.md` (49 tasks)
  - Recovery: Branch `cleanup/workspace-hygiene` can be abandoned

- [ ] **TASK-CLN-002**: Execute `process-docs-triage-cleanup-1.md` (63 tasks)
  - Recovery: Same branch

- [ ] **TASK-CLN-003**: Execute `process-app-routes-triage-1.md` (29 tasks)
  - Recovery: Same branch

- [ ] **TASK-CLN-004**: Execute `process-components-triage-1.md` (32 tasks)
  - Recovery: Same branch

- [ ] **TASK-CLN-005**: Execute `process-scripts-triage-1.md` (42 tasks)
  - Recovery: Same branch

**Checkpoint CP-CLN**: Quality gate passes, workspace is clean

- Type-check: ✅ 0 errors
- Tests: ✅ 241/241 passing
- Build: ✅ Production-ready

---

## Phase 4.3: Reading Analytics & History

**Goal**: Implement user reading metrics, history tracking, engagement dashboard

**Timeline**: 3-4 days | **Status**: ⬜ Planned | **Dependency**: CP-CLN

### 4.3.1 — Database Schema

**Tasks**: 4 | **Status**: ⬜ Not Started | **Estimated**: 1 day

- [ ] TASK-4.3.1-001: Create `readingHistory` table in schema.ts
  - File: `src/database/schema.ts`
  - Code: Add `readingHistory` + `readingHistoryRelations`
  - Est: 30 min

- [ ] TASK-4.3.1-002: Add `timeSpentSeconds` to `readingProgress` table
  - File: `src/database/schema.ts`
  - Est: 15 min

- [ ] TASK-4.3.1-003: Generate migration
  - Command: `pnpm db:generate`
  - Est: 5 min

- [ ] TASK-4.3.1-004: Apply schema changes
  - Command: `pnpm db:push`
  - Est: 5 min

**Checkpoint CP-4.3.1**: ✅ Schema applied

- [ ] `pnpm type-check` → 0 errors
- [ ] `pnpm db:push` → Success
- [ ] Tests: 241/241 passing (no regressions)
- **Recovery**: `pnpm db:reset` if needed

---

### 4.3.2 — Data Access Layer

**Tasks**: 6 | **Status**: ⬜ Not Started | **Est**: 1 day | **Depends**: CP-4.3.1

- [ ] TASK-4.3.2-001: Create `reading-history-dal.ts`
  - File: `src/dal/reading-history-dal.ts`
  - Est: 1 hour

- [ ] TASK-4.3.2-002: Implement `recordSession()`
  - Method: Record reading session (userId, comicId, chapterId, timeSpent)
  - Est: 30 min

- [ ] TASK-4.3.2-003: Implement `getHistory()`
  - Method: Paginated reading history with eager loading
  - Est: 30 min

- [ ] TASK-4.3.2-004: Implement `getStats()`
  - Method: Aggregate stats (total time, chapters read, completed comics, genres)
  - Est: 45 min

- [ ] TASK-4.3.2-005: Implement `getRecentlyRead()`
  - Method: Last 10 unique comics read
  - Est: 20 min

- [ ] TASK-4.3.2-006: Implement `getReadingStreak()`
  - Method: Consecutive days with reading activity
  - Est: 30 min

**Checkpoint CP-4.3.2**: ✅ DAL complete

- [ ] `pnpm type-check` → 0 errors
- [ ] All DAL methods compile
- **Recovery**: Delete `reading-history-dal.ts`

---

### 4.3.3 — Zod Schemas

**Tasks**: 3 | **Status**: ⬜ Not Started | **Est**: 0.5 day | **Depends**: CP-4.3.2

- [ ] TASK-4.3.3-001: Create `reading-history.schema.ts`
  - File: `src/schemas/reading-history.schema.ts`
  - Include: `RecordReadingSessionSchema`
  - Est: 30 min

- [ ] TASK-4.3.3-002: Create `ReadingHistoryFilterSchema`
  - Include: Date range, pagination, comic filter
  - Est: 20 min

- [ ] TASK-4.3.3-003: Write validation tests
  - File: `src/tests/schemas/reading-history-schema.spec.ts`
  - Est: 45 min

**Checkpoint CP-4.3.3**: ✅ Schemas tested

- [ ] Schema validation tests pass
- [ ] `pnpm type-check` → 0 errors

---

### 4.3.4 — Server Actions

**Tasks**: 5 | **Status**: ⬜ Not Started | **Est**: 1 day | **Depends**: CP-4.3.3

- [ ] TASK-4.3.4-001: Create `reading-history.actions.ts`
  - File: `src/actions/reading-history.actions.ts`
  - Est: 30 min

- [ ] TASK-4.3.4-002: Implement `recordReadingSessionAction()`
  - Pattern: Auth → Validate → DAL → Revalidate
  - Est: 30 min

- [ ] TASK-4.3.4-003: Implement `getReadingHistoryAction()`
  - Pattern: Auth → Validate → DAL
  - Est: 20 min

- [ ] TASK-4.3.4-004: Implement `getReadingStatsAction()`
  - Pattern: Auth → DAL (aggregations)
  - Est: 20 min

- [ ] TASK-4.3.4-005: Write action tests
  - File: `src/tests/reading-history.actions.test.ts`
  - Est: 1 hour

**Checkpoint CP-4.3.4**: ✅ Actions tested

- [ ] All tests pass
- [ ] `pnpm type-check` → 0 errors
- [ ] `pnpm lint` → clean
- **Recovery**: Delete action files

---

### 4.3.5 — UI Components

**Tasks**: 6 | **Status**: ⬜ Not Started | **Est**: 1.5 day | **Depends**: CP-4.3.4

- [ ] TASK-4.3.5-001: `reading-dashboard.tsx`
  - File: `src/components/analytics/reading-dashboard.tsx`
  - Purpose: Main analytics orchestration
  - Est: 1 hour

- [ ] TASK-4.3.5-002: `reading-timeline.tsx`
  - Purpose: Chronological reading history list
  - Est: 1 hour

- [ ] TASK-4.3.5-003: `reading-stats-overview.tsx`
  - Purpose: Stats cards (time, chapters, streak)
  - Est: 45 min

- [ ] TASK-4.3.5-004: `recently-read-widget.tsx`
  - Purpose: Sidebar recent comics (10 last read)
  - Est: 45 min

- [ ] TASK-4.3.5-005: `reading-goals.tsx`
  - Purpose: Set and track reading goals
  - Est: 1 hour

- [ ] TASK-4.3.5-006: Create barrel export `index.ts`
  - Est: 5 min

**Component Requirements**:

- ✅ Dark mode support (100% coverage)
- ✅ WCAG 2.1 AA accessibility
- ✅ TypeScript strict mode (no `any` types)
- ✅ SSR-safe (no direct `new Date()`, etc.)

**Checkpoint CP-4.3.5**: ✅ Components rendered

- [ ] All components render without errors
- [ ] Dark mode verified
- [ ] `pnpm type-check` → 0 errors
- **Recovery**: Delete component files

---

### 4.3.6 — Page Routes

**Tasks**: 4 | **Status**: ⬜ Not Started | **Est**: 0.5 day | **Depends**: CP-4.3.5

- [ ] TASK-4.3.6-001: Update `reading-progress/page.tsx`
  - File: `src/app/(root)/reading-progress/page.tsx`
  - Add: Analytics dashboard integration
  - Est: 30 min

- [ ] TASK-4.3.6-002: Add route file structure
  - Files: `loading.tsx`, `error.tsx`
  - Est: 20 min

- [ ] TASK-4.3.6-003: Add metadata for SEO
  - Est: 10 min

- [ ] TASK-4.3.6-004: Integrate `recently-read-widget` into sidebar/home
  - Est: 20 min

**Checkpoint CP-4.3.6**: ✅ Full quality gate

- [ ] `pnpm type-check` → 0 errors
- [ ] `pnpm lint:fix` → clean
- [ ] `pnpm test` → 241+ passing
- [ ] `pnpm build` → success
- **Recovery**: Revert to CP-4.3.5

---

### 4.3.7 — Chapter Reader Integration

**Tasks**: 3 | **Status**: ⬜ Not Started | **Est**: 0.5 day | **Depends**: CP-4.3.6

- [ ] TASK-4.3.7-001: Update `ChapterReader` to record sessions
  - File: `src/components/reading/chapter-reader.tsx`
  - Call: `recordReadingSessionAction` on completion
  - Est: 45 min

- [ ] TASK-4.3.7-002: Track time spent per chapter
  - Implement: Timer on mount, pause on visibilitychange
  - Est: 30 min

- [ ] TASK-4.3.7-003: Track pages read
  - Implement: Count image views
  - Est: 20 min

**Checkpoint CP-4.3**: ✅ **PHASE 4.3 COMPLETE**

- [ ] Full quality gate passes: type-check ✅, lint ✅, test 250+ ✅, build ✅
- [ ] Create commit: `git tag phase-4.3`
- [ ] All features working end-to-end

---

## Phase 4.4: Social Features (Reviews, Ratings, Sharing)

**Goal**: User reviews, enhanced ratings, social sharing

**Timeline**: 3-4 days | **Status**: 🟦 Planned | **Dependency**: CP-4.3

### 4.4.1 — Database Schema

**Tasks**: 4 | **Status**: ⬜ Not Started | **Est**: 1 day

- [ ] TASK-4.4.1-001: Add `review` table
  - Columns: userId, comicId, title, body, rating, helpfulCount, createdAt, updatedAt
  - Est: 30 min

- [ ] TASK-4.4.1-002: Add `reviewVote` table
  - Columns: userId, reviewId, isHelpful
  - Est: 15 min

- [ ] TASK-4.4.1-003: Add table relations
  - Est: 10 min

- [ ] TASK-4.4.1-004: Generate and apply migration
  - Commands: `pnpm db:generate && pnpm db:push`
  - Est: 5 min

**Checkpoint CP-4.4.1**: ✅ Schema applied

- [ ] `pnpm type-check` → 0 errors

---

### 4.4.2 — DAL + Schemas + Actions

**Tasks**: 5 | **Status**: ⬜ Not Started | **Est**: 1.5 day

- [ ] TASK-4.4.2-001: Create `review-dal.ts` with CRUD + votes
  - Est: 1.5 hours

- [ ] TASK-4.4.2-002: Create `review.schema.ts` with 3 schemas
  - Est: 45 min

- [ ] TASK-4.4.2-003: Create `review.actions.ts` with 4 actions
  - Est: 1 hour

- [ ] TASK-4.4.2-004: Write schema validation tests
  - Est: 45 min

- [ ] TASK-4.4.2-005: Write action tests
  - Est: 1 hour

**Checkpoint CP-4.4.2**: ✅ DAL/Schemas/Actions complete

- [ ] Tests pass: 15+ new tests
- [ ] `pnpm type-check` → 0 errors

---

### 4.4.3 — UI Components

**Tasks**: 5 | **Status**: ⬜ Not Started | **Est**: 1.5 day

- [ ] TASK-4.4.3-001: Create `review-section.tsx`
  - Est: 45 min

- [ ] TASK-4.4.3-002: Create `review-card.tsx`
  - Est: 45 min

- [ ] TASK-4.4.3-003: Create `review-form.tsx`
  - Est: 1 hour

- [ ] TASK-4.4.3-004: Create `review-sort.tsx`
  - Est: 30 min

- [ ] TASK-4.4.3-005: Update comic detail page
  - Est: 20 min

**Checkpoint CP-4.4**: ✅ **PHASE 4.4 COMPLETE**

- [ ] `pnpm type-check` → 0 errors
- [ ] `pnpm test` → 250+ passing
- [ ] `pnpm build` → success
- [ ] Reviews end-to-end working

---

## Phase 4.5: Mobile-First Optimization

**Goal**: Mobile responsiveness, PWA, touch gestures

**Timeline**: 2-3 days | **Status**: 🟦 Planned | **Dependency**: CP-4.4

### Tasks Summary

- [ ] TASK-4.5-001: Mobile responsiveness audit (320px, 375px, 414px)
  - Est: 2 hours

- [ ] TASK-4.5-002: Touch swipe gestures in chapter reader
  - Est: 1.5 hours

- [ ] TASK-4.5-003: Pinch-to-zoom support
  - Est: 1 hour

- [ ] TASK-4.5-004: Create `manifest.webmanifest`
  - Est: 30 min

- [ ] TASK-4.5-005: Add PWA meta tags
  - Est: 20 min

- [ ] TASK-4.5-006: Implement service worker
  - Est: 2 hours

- [ ] TASK-4.5-007: Optimize images (responsive sizes, lazy loading)
  - Est: 1.5 hours

- [ ] TASK-4.5-008: Validate touch targets (44x44px minimum)
  - Est: 1 hour

- [ ] TASK-4.5-009: Mobile bottom navigation bar
  - Est: 1 hour

- [ ] TASK-4.5-010: Lighthouse mobile audit
  - Est: 1 hour

**Checkpoint CP-4.5**: ✅ **PHASE 4.5 COMPLETE**

- [ ] Lighthouse mobile ≥ 90 on all metrics
- [ ] Touch targets validated
- [ ] Full quality gate passes

---

## Phase 6: Advanced Features (Deferred)

**Goal**: Comments, notifications, admin panel, search enhancements

**Timeline**: 2+ weeks | **Status**: 🟦 Deferred | **Dependency**: CP-4.5

### 6.1 — Comments & Discussion (5 tasks)

- [ ] Comment threading implementation
- [ ] @username mention support
- [ ] Comment reactions system
- [ ] Moderation tools for admins
- [ ] Reply notifications

### 6.2 — Notifications Enhancement (4 tasks)

- [ ] New chapter notifications
- [ ] Email digest options
- [ ] PWA push notifications
- [ ] Notification preferences

### 6.3 — Admin Panel (5 tasks)

- [ ] Comic CRUD management
- [ ] User management
- [ ] Moderation dashboard
- [ ] Analytics dashboard
- [ ] Batch operations

### 6.4 — Full-Text Search Enhancement (4 tasks)

- [ ] PostgreSQL tsvector indexing
- [ ] Search result ranking with ts_rank
- [ ] Search analytics tracking
- [ ] Popular/recent query suggestions

---

## Milestone Checkpoints

| Milestone | Target Date | Status | Notes |
| --- | --- | --- | --- |
| CP-CLN | TBD | ⬜ | Cleanup complete, workspace clean |
| CP-4.3 | TBD | ⬜ | Reading Analytics complete |
| CP-4.4 | TBD | ⬜ | Social Features complete |
| CP-4.5 | TBD | ⬜ | Mobile optimization complete |
| **PHASE 4 COMPLETE** | TBD | ⬜ | All phases 4.1–4.5 done |

---

## Quality Gate Commands

Run these at each checkpoint:

```bash
# Type check (must be 0 errors)
pnpm type-check

# Lint and format
pnpm lint:fix

# Unit tests (must pass all)
pnpm test

# Production build (must succeed)
pnpm build

# Complete quality gate
pnpm type-check && pnpm lint:fix && pnpm test && pnpm build
```

---

## Notes & Decisions

- **2026-03-08**: Master plan created with 4.3-6 tasks documented
- **Cleanup Sprint**: Execute 5 cleanup plans before starting Phase 4.3
- **Sequential Execution**: 4.3 → 4.4 → 4.5 (Phase 6 deferred)
- **Recovery Points**: Each task group has a recovery point documented in master plan
- **Testing Target**: Minimum 250+ tests by phase completion (from current 241)

---

## References

- [Master Phase Plan (Detailed)](MASTER_PHASE_PLAN_4-6.md)
- [AGENTS.md](../AGENTS.md)
- [Copilot Instructions](../.github/copilot-instructions.md)
- [Development Guide](dev.content.md)
- [Database Context Map](database-context-map.md)
