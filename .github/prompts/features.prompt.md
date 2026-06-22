---
agent: agent

description: Complete feature implementation tasks for profiles, comics, chapters, bookmarks
tools:
  [
    vscode,
    execute,
    read,
    agent,
    edit,
    search,
    web,
    "context7/*",
    "modelcontextprotocol-servers-sequentialthinking/*",
    "next-devtools/*",
    "nextjs-docs-mcp/*",
    "sentry/*",
    "shadcn/*",
    "github/*",
    "github/*",
    "io.github.chromedevtools/chrome-devtools-mcp/*",
    "io.github.upstash/context7/*",
    "playwright/*",
    vscode.mermaid-chat-features/renderMermaidDiagram,
    github.vscode-pull-request-github/issue_fetch,
    github.vscode-pull-request-github/suggest-fix,
    github.vscode-pull-request-github/searchSyntax,
    github.vscode-pull-request-github/doSearch,
    github.vscode-pull-request-github/renderIssues,
    github.vscode-pull-request-github/activePullRequest,
    github.vscode-pull-request-github/openPullRequest,
    ms-azuretools.vscode-containers/containerToolsConfig,
    prisma.prisma/prisma-migrate-status,
    prisma.prisma/prisma-migrate-dev,
    prisma.prisma/prisma-migrate-reset,
    prisma.prisma/prisma-studio,
    prisma.prisma/prisma-platform-login,
    prisma.prisma/prisma-postgres-create-database,
    todo
  ]
---

# ComicWise - Feature Implementation Guide

---

## Implementation Principles

1. **Use Existing Patterns** - Reference admin panel patterns
2. **Type Safety** - No `any` types, strict TypeScript
3. **Zod Validation** - Validate all user input
4. **Server Actions** - Use for all mutations
5. **Error Handling** - Comprehensive user feedback
6. **Component Reusability** - Create reusable components
7. **Performance** - Optimize images, queries, bundles
8. **Accessibility** - WCAG compliant UI

---

## Phase 2: User Profile Features

> ### Task 2.1: Profile View Page ✅
> **File:** `src/app/(root)/profile/page.tsx`

> **Full content:** `templates/features/phase_2_user_profile_features.md`

## Phase 3: Comic Features

> ### Task 3.1: Comics Listing Page ✅
> **File:** `src/app/(root)/comics/page.tsx` (373 lines)

> **Full content:** `templates/features/phase_3_comic_features.md`

## Phase 4: Chapter Reader

> ### Task 4.1: Chapter Reader Page ✅
> **File:** `src/app/(root)/comics/[slug]/[chapterNumber]/page.tsx`

> **Full content:** `templates/features/phase_4_chapter_reader.md`

## Phase 5: Bookmarks Management

### Task 5.1: Bookmarks Listing Page ✅

**File:** `src/app/(root)/bookmarks/page.tsx`

**Features:**

- [x] Grid/list view toggle
- [x] Bookmark cards with progress
- [x] Filter by status
- [x] Sort by date/title/progress
- [x] Search bookmarks
- [x] Empty state handling

**Components:**

- `BookmarkCard` - Card component
- `BookmarkFilters` - Filter controls
- `BookmarkSearch` - Search input
- `BookmarkViewToggle` - View switcher

---

## UI/UX Decision Matrix

| Feature | Decision | Rationale |
| --- | --- | --- |
| Comic Detail Description | Truncated (250 chars) | Prevent layout issues, faster loading |
| Chapter Reader Default | Vertical scroll | Most popular mobile experience |
| Bookmark Status | Dropdown | Fits limited space, clear options |
| Image Loading | Lazy + Skeleton | Performance + user feedback |
| Search | Debounced (300ms) | Reduce API calls |
| Pagination | Server-side | Better for large datasets |

---

## Root Pages

> ### Task: Home Page Enhancement
> **File:** `src/app/(root)/page.tsx`

> **Full content:** `templates/features/root_pages.md`

## Server Actions Reference

> ### Profile Actions (`src/actions/profile.actions.ts`)
> ### Bookmark Actions (`src/actions/bookmark.actions.ts`)

> **Full content:** `templates/features/server_actions_reference.md`

## Zod Schemas Reference

**Location:** `src/schemas/`

| Schema                  | File                         | Status |
| ----------------------- | ---------------------------- | ------ |
| `ProfileUpdateSchema`   | `profile.schema.ts`          | ✅     |
| `ChangePasswordSchema`  | `profile.schema.ts`          | ✅     |
| `CreateBookmarkSchema`  | `bookmark.schema.ts`         | ✅     |
| `UpdateBookmarkSchema`  | `bookmark.schema.ts`         | ✅     |
| `ComicFilterSchema`     | `comic.schema.ts`            | ✅     |
| `ChapterSchema`         | `chapter.schema.ts`          | ✅     |
| `ReadingProgressSchema` | `reading-progress.schema.ts` | ✅     |

---

## Component Checklist

### Core UI Components

- [x] `ComicCard` - Comic display card
- [x] `ChapterList` - Chapter listing
- [x] `BookmarkCard` - Bookmark display
- [x] `ProfileView` - Profile display
- [x] `ImageViewer` - Image gallery

### Action Components

- [x] `BookmarkActions` - Add/remove/status
- [x] `ChapterNavigation` - Reader navigation
- [x] `ReadingSettings` - Reader settings

### Loading States

- [x] `ComicCardSkeleton`
- [x] `ChapterListSkeleton`
- [x] `ProfileSkeleton`
- [x] `BookmarkCardSkeleton`

---

## Validation Commands

```bash
# Type check all feature files
pnpm type-check

# Lint feature components
pnpm lint src/app/\(root\) src/components

# Run feature-related tests
pnpm test:unit:run tests/unit/features

# E2E test user flows
pnpm test:e2e tests/e2e/user-flows.spec.ts
```

---

## Success Criteria

- [ ] All pages accessible and responsive
- [ ] TypeScript: 0 errors (`pnpm type-check`)
- [ ] ESLint: 0 errors (`pnpm lint`)
- [ ] Tests: All passing, 80%+ coverage
- [ ] Build: Successful (`pnpm build`)
- [ ] Performance: Core Web Vitals in green

---

**Document Version:** 1.0.0 | **Last Updated:** 2026-02-01


## Template References

Detailed templates in `templates/features/`:
- `phase_2_user_profile_features.md`
- `phase_3_comic_features.md`
- `phase_4_chapter_reader.md`
- `root_pages.md`
- `server_actions_reference.md`
