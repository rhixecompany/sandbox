# ComicWise Project Folder Structure Blueprint

**Project Type:** Node.js / Next.js 16.1.6 (React 19 Full-Stack) **Architecture:** Single Application (Monolithic) **Frontend:** React 19 Server Components + Client Components **Backend:** Node.js with Drizzle ORM + PostgreSQL **Database:** PostgreSQL (Neon) **Build Tool:** Turbopack / webpack **Package Manager:** pnpm

**Document Version:** 1.0 **Last Updated:** 2026-03-07 **Maintainer:** ComicWise Development Team

---

## Table of Contents

1. [Structural Overview](#1-structural-overview)
2. [Directory Visualization](#2-directory-visualization)
3. [Key Directory Analysis](#3-key-directory-analysis)
4. [File Placement Patterns](#4-file-placement-patterns)
5. [Naming and Organization Conventions](#5-naming-and-organization-conventions)
6. [Navigation and Development Workflow](#6-navigation-and-development-workflow)
7. [Build and Output Organization](#7-build-and-output-organization)
8. [Technology-Specific Organization](#8-technology-specific-organization)
9. [Extension and Evolution](#9-extension-and-evolution)
10. [Structure Templates](#10-structure-templates)
11. [Structure Enforcement](#11-structure-enforcement)
12. [Maintenance Documentation](#12-maintenance-documentation)

---

## 1. Structural Overview

### Architectural Approach

ComicWise follows a **Next.js App Router (v16) full-stack architecture** with a **feature-driven organization** strategy. The project separates concerns across clearly defined layers:

- **Presentation Layer:** React Server/Client Components in `src/app/` and `src/components/`
- **Business Logic Layer:** Server Actions in `src/actions/` and Zustand stores in `src/stores/`
- **Data Access Layer:** Drizzle ORM queries in `src/dal/`
- **Validation Layer:** Zod schemas in `src/schemas/`
- **Infrastructure:** Database config, authentication, utilities, hooks

### Organizational Principles

1. **Feature-Driven Organization:** Pages and components grouped by domain (comics, bookmarks, search, ratings, etc.)
2. **Layered Architecture:** Clear separation between presentation, business logic, and data access
3. **Server-First Design:** Async Server Components as default entry points; Client Components only where necessary
4. **Colocated Code:** Related files (actions, schemas, DAL) mapped to feature domains
5. **Path Aliases:** Consistent use of `@/`, `ui/`, `database/`, `schemas/`, `components/` aliases to avoid relative imports
6. **Type Safety:** TypeScript strict mode throughout; Zod runtime validation bridge between API and database

### Key Structural Patterns

| Pattern | Location | Example |
| --- | --- | --- |
| **Data Flow** | Server Component → DAL query → Props → Client | `src/app/(root)/comics/page.tsx` → `comic-dal.ts` → `ComicCard` |
| **Mutations** | Server Actions with validation → DAL → revalidate | `src/actions/bookmark.actions.ts` |
| **Validation** | Zod schemas → Server Actions → Database | `src/schemas/bookmark-schema.ts` |
| **State Management** | Zustand for UI state, React Query for server state | `src/stores/reader-store.ts` |
| **API Routes** | Minimal; only for external webhooks/seeding | `src/app/api/seed/` |

---

## 2. Directory Visualization

### Root-Level Structure

```
comicbook/
├── .github/                          # GitHub configuration
│   ├── instructions/                 # Coding standards (auto-applied)
│   ├── prompts/                      # AI agent prompts
│   ├── skills/                       # Domain-specific AI skills
│   └── plan/                         # Implementation plans
│
├── .next/                            # [GENERATED] Next.js build output
├── .turbo/                           # [GENERATED] Turbo cache
├── .husky/                           # Git hooks
├── .vscode/                          # VS Code workspace settings
│
├── src/                              # ⭐ APPLICATION SOURCE CODE
│   ├── app/                          # 📄 Next.js App Router pages
│   ├── components/                   # ⚛️  React components
│   ├── dal/                          # 🗄️  Data access layer
│   ├── actions/                      # ⚡ Server actions
│   ├── schemas/                      # 🔍 Zod validation schemas
│   ├── stores/                       # 🏪 Zustand state (client)
│   ├── hooks/                        # 🪝 React custom hooks
│   ├── lib/                          # 🛠️  Utilities & helpers
│   ├── database/                     # 🗄️  Drizzle config & schema
│   ├── scripts/                      # 📝 Automation scripts
│   ├── styles/                       # 🎨 Global CSS
│   ├── types/                        # 📘 TypeScript types
│   ├── assets/                       # 📦 Static assets
│   ├── tests/                        # 🧪 Test utilities
│   ├── auth.ts                       # NextAuth initialization
│   ├── auth-config.ts                # Auth callbacks & session
│   ├── auth-providers.ts             # OAuth/credential providers
│   ├── auth-adapter.ts               # Drizzle auth adapter
│   └── proxy.ts                      # Middleware (auth, routing)
│
├── public/                           # 📁 Static files (images, icons)
├── docs/                             # 📚 Documentation
├── .cursorrules                      # Cursor AI rules
├── next.config.ts                    # Next.js configuration
├── tsconfig.json                     # TypeScript configuration
├── vitest.config.mts                 # Unit test config
├── playwright.config.mts             # E2E test config
├── drizzle.config.ts                 # Drizzle ORM config
├── package.json                      # Dependencies & scripts
├── pnpm-lock.yaml                    # Lock file
├── tailwind.config.ts                # Tailwind CSS config
├── postcss.config.mjs                # PostCSS config
└── appConfig.ts                      # App configuration singleton
```

### Source Code Deep Dive (Level 3-4)

#### `src/app/` — Next.js Pages (App Router)

```
src/app/
├── (auth)/                           # 🔐 Route group: Auth pages
│   ├── sign-in/page.tsx              # Login page
│   ├── sign-up/page.tsx              # Registration page
│   ├── forgot-password/page.tsx      # Password reset
│   └── layout.tsx                    # Auth layout wrapper
│
├── (root)/                           # 📍 Route group: Main app pages
│   ├── layout.tsx                    # App layout (sidebar, header)
│   ├── page.tsx                      # Home page
│   ├── authors/page.tsx              # Authors directory
│   ├── bookmarks/                    # Bookmark management
│   │   ├── page.tsx                  # Bookmarks list
│   │   └── layout.tsx
│   ├── browse/page.tsx               # Discovery/browse
│   ├── comics/                       # Comics feature
│   │   ├── page.tsx                  # Comics listing
│   │   ├── [slug]/                   # Dynamic comic detail
│   │   │   ├── page.tsx              # Comic detail view
│   │   │   ├── layout.tsx            # Comic layout
│   │   │   └── [chapterId]/          # Chapter reader
│   │   │       ├── page.tsx          # Reader view
│   │   │       └── layout.tsx        # Reader layout
│   │   └── page.test.tsx             # Comics page tests
│   ├── comments/page.tsx             # Comments management
│   ├── genres/page.tsx               # Genre directory
│   ├── notifications/page.tsx        # User notifications
│   ├── profile/                      # User profile
│   │   ├── page.tsx                  # Profile view
│   │   ├── edit/page.tsx             # Profile edit
│   │   └── settings/page.tsx         # Settings
│   ├── ratings/page.tsx              # User ratings
│   ├── reading-progress/page.tsx     # Reading history
│   ├── search/page.tsx               # Advanced search
│   └── settings/page.tsx             # App settings
│
├── admin/                            # 👮 Admin-only routes
│   ├── dashboard/page.tsx            # Admin dashboard
│   ├── users/page.tsx                # User management
│   └── content/page.tsx              # Content management
│
├── api/                              # 🔌 API route handlers
│   ├── auth/[...nextauth]/route.ts   # NextAuth endpoints
│   ├── search/route.ts               # Search handler
│   └── seed/route.ts                 # Seeding endpoint
│
├── layout.tsx                        # 🌳 Root layout
├── loading.tsx                       # Loading skeleton
├── global-error.tsx                  # Error boundary
├── not-found.tsx                     # 404 handler
└── favicon.ico                       # App icon
```

#### `src/components/` — React Components

```
src/components/
├── ui/                               # 🧩 shadcn/Radix UI primitives
│   ├── button.tsx
│   ├── card.tsx
│   ├── dialog.tsx
│   ├── input.tsx
│   ├── dropdown-menu.tsx
│   └── ... (30+ shared components)
│
├── layout/                           # 📐 Layout components
│   ├── app-sidebar.tsx               # Main sidebar
│   ├── app-header.tsx                # Header/navbar
│   ├── app-footer.tsx                # Footer
│   ├── breadcrumbs.tsx               # Navigation breadcrumbs
│   ├── layout-provider.tsx           # Provider stack
│   └── main-nav.tsx                  # Main navigation
│
├── comics/                           # 📕 Comics-specific components
│   ├── comic-card.tsx                # Comics list card
│   ├── comic-detail.tsx              # Detail view
│   ├── comic-filters.tsx             # Filter sidebar
│   ├── comic-grid.tsx                # Grid layout
│   ├── comic-image.tsx               # Optimized images
│   └── comic-metadata.tsx            # Comic info display
│
├── reading/                          # 👀 Chapter reader components
│   ├── chapter-reader.tsx            # Main reader
│   ├── chapter-images.tsx            # Image viewer
│   ├── reading-settings.tsx          # Reader options
│   ├── page-navigator.tsx            # Page nav controls
│   └── zoom-controls.tsx             # Zoom/pan
│
├── bookmarks/                        # 🔖 Bookmark components
│   ├── bookmark-button.tsx           # Add/remove bookmark
│   ├── bookmark-list.tsx             # Bookmarks list
│   ├── bookmark-status-badge.tsx     # Status indicator
│   └── bookmark-filters.tsx          # Filter bookmarks
│
├── search/                           # 🔍 Search components
│   ├── search-input.tsx              # Search box
│   ├── search-results.tsx            # Results display
│   ├── search-filters.tsx            # Filter options
│   ├── advanced-search-form.tsx      # Advanced search
│   └── search-suggestions-dropdown.tsx # Autocomplete
│
├── ratings/                          # ⭐ Rating components
│   ├── rating-button.tsx             # Rate comic
│   ├── rating-display.tsx            # Display ratings
│   ├── rating-stats.tsx              # Rating statistics
│   └── user-rating-history.tsx       # User's ratings
│
├── comments/                         # 💬 Comment components
│   ├── comment-form.tsx              # Post comment
│   ├── comment-list.tsx              # Comments display
│   ├── comment-item.tsx              # Single comment
│   └── comment-rating.tsx            # Comment rating
│
├── profile/                          # 👤 Profile components
│   ├── profile-header.tsx            # Profile banner
│   ├── profile-edit-form.tsx         # Edit form
│   ├── profile-stats.tsx             # User statistics
│   └── reading-stats.tsx             # Reading metrics
│
├── notifications/                    # 🔔 Notification components
│   ├── notification-bell.tsx         # Bell icon + drawer
│   ├── notification-item.tsx         # Single notification
│   └── notification-list.tsx         # Notifications list
│
├── recommendations/                  # 💡 Recommendation components
│   ├── recommended-section.tsx       # Recommendations widget
│   ├── recommended-comic-card.tsx    # Card variant
│   └── trending-section.tsx          # Trending comics
│
├── reading-progress/                 # 📊 Progress tracking
│   ├── reading-progress-bar.tsx      # Progress indicator
│   ├── reading-history-card.tsx      # History item
│   └── reading-stats-chart.tsx       # Statistics chart
│
├── theme/                            # 🎨 Theme management
│   ├── theme-provider.tsx            # Theme context
│   └── theme-toggle.tsx              # Light/dark switch
│
├── search/                           # 🔍 Search UI
│   ├── search-form.tsx               # Search input
│   └── search-results.tsx            # Results grid
│
├── optimized/                        # ⚡ Performance-optimized
│   ├── lazy-image.tsx                # Lazy-loaded images
│   ├── virtual-list.tsx              # Virtualized lists
│   └── infinite-scroll.tsx           # Infinite scrolling
│
├── a11y/                             # ♿ Accessibility components
│   ├── skip-link.tsx                 # Skip to content
│   ├── focus-trap.tsx                # Focus management
│   └── aria-live-region.tsx          # Live regions
│
├── settings/                         # ⚙️  Settings UI
│   ├── settings-form.tsx             # Settings form
│   └── preference-switcher.tsx       # Preference toggles
│
└── shadcn-studio/                    # 🎭 Component showcase
    └── component-showcase.tsx        # Design system browser
```

#### `src/dal/` — Data Access Layer (Drizzle Queries)

```
src/dal/
├── base-dal.ts                       # Abstract base class for all DALs
├── comic-dal.ts                      # Comic queries + eager loading
├── chapter-dal.ts                    # Chapter queries
├── bookmark-dal.ts                   # Bookmark queries (upsert)
├── user-dal.ts                       # User queries
├── author-dal.ts                     # Author queries
├── artist-dal.ts                     # Artist queries
├── genre-dal.ts                      # Genre queries
├── rating-dal.ts                     # Rating queries
├── comment-dal.ts                    # Comment queries
├── comment-rating-dal.ts             # Comment rating queries
├── reading-progress-dal.ts           # Reading progress tracking
├── notification-dal.ts               # Notification queries
├── user-preferences-dal.ts           # User preferences
├── recommendation-dal.ts             # Recommendation engine
├── search-dal.ts                     # Full-text search
├── chapter-image-dal.ts              # Chapter image metadata
├── comic-image-dal.ts                # Comic cover metadata
├── type-dal.ts                       # Comic type queries
└── index.ts                          # DAL exports (singleton instances)
```

**Pattern:** Each DAL class extends `BaseDal<T>`, returns `$inferSelect` typed results, uses `.with()` for eager loading, and is exported as a singleton instance.

#### `src/actions/` — Server Actions (Mutations)

```
src/actions/
├── types.ts                          # ActionResult<T> discriminated union
├── comic.actions.ts                  # Comic CRUD operations
├── bookmark.actions.ts               # Bookmark add/remove/status
├── chapter.actions.ts                # Chapter operations
├── rating.actions.ts                 # Rating CRUD
├── comment.actions.ts                # Comment CRUD
├── comment-rating-actions.ts         # Comment rating
├── profile.actions.ts                # Profile update
├── reading-progress.actions.ts       # Reading progress tracking
├── reading-progress.ts               # Reading progress helpers
├── user-preferences.ts               # Preferences mutations
├── notification.actions.ts           # Notification management
├── author.actions.ts                 # Author CRUD (admin)
├── artist.actions.ts                 # Artist CRUD (admin)
├── genre.actions.ts                  # Genre CRUD (admin)
├── admin.actions.ts                  # Admin operations
├── auth-actions.ts                   # Auth-specific mutations
├── auth-db.ts                        # Auth DB operations
├── credentials.actions.ts            # Credential authentication
└── search.actions.ts                 # Search operations
```

**Pattern:** All follow `ActionResult<T> = { ok: true; data: T } | { ok: false; error: string }` with auth check first, Zod validation, DAL mutation, revalidation.

#### `src/schemas/` — Zod Validation

```
src/schemas/
├── auth-schema.ts                    # Sign-in/up validation
├── user-schema.ts                    # User data validation
├── profile-schema.ts                 # Profile update validation
├── comic-schema.ts                   # Comic validation (create, update, filter)
├── chapter-schema.ts                 # Chapter validation
├── bookmark-schema.ts                # Bookmark validation
├── rating-schema.ts                  # Rating validation (1-5 stars)
├── comment-schema.ts                 # Comment validation
├── comment-rating-schema.ts          # Comment rating validation
├── reading-progress-schema.ts        # Progress tracking validation
├── search.schema.ts                  # Search query + filters
├── reading-settings-schema.ts        # Reader settings
├── preferences.schema.ts             # User preferences
└── seed/                             # Seeding schemas
    └── seed-schemas.ts               # Data validation for seeds
```

**Pattern:** Base schema → Create/Update/Filter variants via `.extend()`, `.partial()`, `.pick()` for DRY composition.

#### `src/database/` — Drizzle ORM

```
src/database/
├── db.ts                             # Drizzle singleton (postgres-js)
├── schema.ts                         # 27 table definitions (604 lines)
│                                     # - 4 pgEnums: userRole, comicStatus, resourceEnum, actionEnum
│                                     # - Relations with eager loading patterns
│                                     # - Soft deletes (user, comment tables only)
│                                     # - Cascade deletes (most FKs)
│                                     # - Updated timestamps via .$onUpdate()
└── migrations/                       # Auto-generated SQL migrations
    ├── 0001_init_schema.sql
    ├── 0002_add_bookmarks.sql
    └── ...
```

#### `src/scripts/` — Automation & CLI Tools

```
src/scripts/
├── shared/                           # Shared utilities
│   ├── confirmAction.ts              # Interactive confirmations (destructive ops)
│   └── logger.ts                     # Colored console output
│
├── seed/                             # Database seeding
│   ├── seedOrchestrator.ts           # Dependency resolution + execution
│   ├── baseSeed.ts                   # Template method for seeders
│   ├── seeders/                      # Individual entity seeders
│   │   ├── comicSeeder.ts
│   │   ├── chapterSeeder.ts
│   │   ├── userSeeder.ts
│   │   └── ...
│   ├── run.ts                        # CLI entry point
│   └── data/                         # Seed data files
│       ├── comics.json
│       ├── chapters.json
│       └── ...
│
├── analyze-project.ts                # Project analysis tool
├── camel-case-converter2025.ts       # Naming convention fixer
├── check-db.ts                       # Database connectivity check
├── check-redis.ts                    # Redis connectivity check
├── clear-cache.ts                    # Cache clearing (with confirmations)
├── git-commit.ts                     # Conventional commit helper
├── git-init.ts                       # Git setup
├── health-check.ts                   # System health verification
├── master-setup.ts                   # Documentation generator
├── merge-seed-data.ts                # Seed data merging
├── rename-to-kebab-case.ts          # File renaming utility
├── replace-imports-enhanced.ts       # Import path fixer
├── scaffold.ts                       # Component scaffolding
├── uninstall-unused-packages.ts      # Dependency cleanup
├── update-any-types.ts               # Type safety improvements
└── validate-docs.ts                  # Documentation validation
```

#### `src/lib/` — Utilities & Helpers

```
src/lib/
├── env.ts                            # Zod-validated environment variables (getEnv())
├── utils.ts                          # clsx, cn() utility (Tailwind merge)
├── query-client.ts                   # React Query config + key factory
├── security.ts                       # Security utilities
├── accessibility.ts                  # Accessibility helpers
├── image-optimization.ts             # Next/Image utilities
├── performance-metrics.ts            # Performance tracking
└── cache/                            # Caching utilities
    ├── cache-keys.ts                 # Cache key constants
    └── cache-utils.ts                # Cache helpers
```

#### `src/stores/` — Zustand State (Client-Side Only)

```
src/stores/
├── use-ui-store.ts                   # UI state (sidebar, theme, modals)
├── use-reader-store.ts               # Chapter reader state (mode, zoom)
├── use-bookmark-store.ts             # Bookmark optimistic updates
├── use-notification-store.ts         # Notification management
├── use-reading-progress-store.ts     # Reading progress UI
└── use-search-store.ts               # Search UI state (filters, sorting)
```

#### `src/hooks/` — Custom React Hooks

```
src/hooks/
├── use-now.tsx                       # SSR-safe Date hook
├── use-debounce.ts                   # Debounced values
├── use-mobile.ts                     # Mobile detection
├── use-pagination.ts                 # Pagination logic
├── use-keyboard-navigation.tsx       # Keyboard navigation
├── use-performance-monitoring.tsx    # Perf metrics collection
└── use-infinite-scroll.ts            # Infinite scroll hook
```

#### `src/types/` — Global Type Definitions

```
src/types/
├── index.ts                          # Type exports
├── db.ts                             # Database-derived types
├── api.ts                            # API response types
├── user.ts                           # User-related types
├── comic.ts                          # Comic-related types
└── actions.ts                        # Action return types
```

#### `src/tests/` — Test Utilities

```
src/tests/
├── setup-env.ts                      # Vitest jsdom setup, global mocks
├── mocks/                            # Mock factories
│   ├── mock-auth.ts                  # Auth mocking
│   ├── mock-db.ts                    # Database mocking
│   └── mock-router.ts                # Next.js router mocking
└── fixtures/                         # Test data fixtures
    ├── comic-fixtures.ts
    └── user-fixtures.ts
```

---

## 3. Key Directory Analysis

### `src/app/` — Next.js Pages (App Router)

**Purpose:** Define routes and page structure using Next.js App Router v16. **Organization:** Route groups `(auth)` and `(root)` for visual organization; dynamic routes `[slug]` for detail pages. **Key Patterns:**

- **Server Components by default** — Async pages fetch data, pass as props
- **Route groups** — `(parentheses)` organizes without affecting URL
- **Dynamic routes** — `[slug]/page.tsx` for detail views with `generateStaticParams()`
- **Layouts** — Nested `layout.tsx` for route-specific UI wrappers

**When to add:** Create new feature directory under `(root)/`, add `page.tsx`, create `layout.tsx` if custom layout needed.

### `src/components/` — React Components

**Purpose:** Reusable UI components, grouped by feature domain. **Organization:**

- `ui/` — shadcn/Radix primitives (Button, Card, Dialog, etc.) — not feature-specific
- Feature directories — Comics, Search, Bookmarks, Rating, etc. — domain-specific components
- `layout/` — Layout wrappers used across pages

**Key Patterns:**

- **Server Components by default** — Components are `async` or Server Components unless requiring browser APIs
- **Client Components marked explicitly** — `"use client"` at top for interactivity
- **Props-driven** — Data passed as props from Server Component parents
- **Composition** — Smaller components combined (ComicCard uses BookmarkButton)

**Naming:** PascalCase files, default export as component name, `.tsx` extension.

### `src/dal/` — Data Access Layer

**Purpose:** All database queries using Drizzle ORM; single source of truth for DB access. **Organization:** One file per entity (comic, chapter, bookmark, user, etc.); all extend `BaseDal<T>`. **Key Patterns:**

- **Eager loading via `.with()`** — Always include related data to prevent N+1 queries
- **Type-safe results** — Return `typeof table.$inferSelect` typed data
- **No filtering on DAL** — DAL returns raw results; filtering done in actions or components
- **Soft-delete filtering** — Filter `deletedAt IS NULL` only on `user` and `comment` tables
- **Singleton exports** — Each DAL exported as `const comicDal = new ComicDal()`

**When to add:** Create `src/dal/[entity]-dal.ts`, extend `BaseDal<T>`, implement methods with eager loading.

### `src/actions/` — Server Actions

**Purpose:** Mutations and write operations; always server-side only. **Organization:** Grouped by domain (bookmark.actions, rating.actions, etc.). **Key Pattern (Template):**

```typescript
"use server";
export async function actionName(
  input: unknown
): Promise<ActionResult<T>> {
  // 1. Auth check
  const session = await auth();
  if (!session?.user?.id)
    return { ok: false, error: "Not authenticated" };

  // 2. Validate input
  const parsed = ZodSchema.safeParse(input);
  if (!parsed.success)
    return { ok: false, error: parsed.error.errors[0]?.message };

  try {
    // 3. Mutate via DAL
    const result = await dal.create(parsed.data);

    // 4. Revalidate
    revalidatePath("/path");
    revalidateTag("tag-name");

    // 5. Return result
    return { ok: true, data: result };
  } catch (error) {
    return { ok: false, error: "Failed" };
  }
}
```

### `src/schemas/` — Zod Validation

**Purpose:** Runtime type safety bridge between API/UI and database. **Organization:** One file per domain (comic-schema.ts, bookmark-schema.ts, etc.); schemas composed from base. **Key Pattern:**

```typescript
const BaseSchema = z.object({
  /* common fields */
});
export const CreateSchema = BaseSchema.extend({
  /* create-specific */
});
export const UpdateSchema = BaseSchema.partial().extend({
  id: z.string().uuid()
});
export const FilterSchema = z.object({
  /* filter fields */
});
```

### `src/database/` — Drizzle ORM Schema

**Purpose:** Define database structure; auto-generate migrations. **File:** `schema.ts` contains all 27 table definitions, 4 pgEnums, relations, and constraints. **Key Constraints:**

- **Cascade deletes:** Most FK relations include `{ onDelete: "cascade" }`
- **Exceptions:** `comic.authorId`, `comic.artistId`, `comic.typeId`, `bookmark.lastReadChapterId` (no cascade)
- **Soft deletes:** Only `user` and `comment` have `deletedAt` column
- **Auto-updated:** All tables include `updatedAt` via `.$onUpdate()`
- **Enums (4):** `userRole`, `comicStatus`, `resourceEnum`, `actionEnum`

### `src/stores/` — Zustand State

**Purpose:** Client-side UI state management; never server data. **Examples:**

- `reader-store.ts` — Chapter reader mode, zoom level, settings
- `ui-store.ts` — Sidebar open/closed, theme, modal states
- `bookmark-store.ts` — Optimistic bookmark status updates

**Key Rule:** Server data comes from Server Components; Zustand only for UI chrome.

### `src/scripts/` — Automation Tools

**Purpose:** CLI utilities for development, testing, seeding, analysis. **Organization:**

- `seed/` — Database population with dependency orchestration
- Individual scripts — Database checks, cache clearing, naming fixes, etc.
- `shared/` — Reusable confirmations and logging utilities

---

## 4. File Placement Patterns

### Configuration Files

| Type | Location | File | Purpose |
| --- | --- | --- | --- |
| **Next.js** | Root | `next.config.ts` | Framework setup, React Compiler, Turbopack |
| **TypeScript** | Root | `tsconfig.json` | Type checking, path aliases |
| **Tailwind CSS** | Root | `tailwind.config.ts` | Design tokens, theme |
| **PostCSS** | Root | `postcss.config.mjs` | CSS processing |
| **Drizzle ORM** | Root | `drizzle.config.ts` | Database connection, migrations |
| **Prettier** | Root | `.prettierrc.ts` | Code formatting |
| **ESLint** | Root | `eslint.config.mts` | Linting rules |
| **Vitest** | Root | `vitest.config.mts` | Unit test setup |
| **Playwright** | Root | `playwright.config.mts` | E2E test setup |
| **GitHub Actions** | `.github/workflows/` | `*.yml` | CI/CD pipelines |
| **Environment** | Root | `.env.local` | Secrets and API keys (gitignored) |

### Model/Entity Definitions

| Purpose | Location | Pattern |
| --- | --- | --- |
| **Database schema** | `src/database/schema.ts` | Drizzle table definitions (all in one file) |
| **Type exports** | `src/types/[entity].ts` | TypeScript interfaces derived from `$inferSelect` |
| **API request/response** | `src/schemas/[entity]-schema.ts` | Zod schemas for validation |
| **Form validation** | `src/schemas/[entity]-schema.ts` | Zod schemas with `.extend()` for forms |

### Business Logic

| Type | Location | Pattern |
| --- | --- | --- |
| **Queries** | `src/dal/[entity]-dal.ts` | Drizzle queries, eager loading, singletons |
| **Mutations** | `src/actions/[entity].actions.ts` | Server Actions with ActionResult pattern |
| **State logic** | `src/stores/use-[entity]-store.ts` | Zustand stores (UI state only) |
| **Hooks** | `src/hooks/use-[name].ts` | Custom React hooks for logic reuse |
| **Utilities** | `src/lib/[feature].ts` | Helper functions (never database access) |

### Display Logic

| Type | Location | Pattern |
| --- | --- | --- |
| **Page routes** | `src/app/[route]/page.tsx` | Server Components, async, `await params` |
| **Layouts** | `src/app/[route]/layout.tsx` | Nested layout wrappers |
| **Components** | `src/components/[feature]/Component.tsx` | Reusable UI, Server or Client |
| **UI elements** | `src/components/ui/Button.tsx` | shadcn/Radix primitives |

### Test Files

| Type | Location | Pattern |
| --- | --- | --- |
| **Unit tests** | `src/**/*.test.ts`, `src/**/*.spec.ts` | Vitest (jsdom), mocks external deps |
| **E2E tests** | `tests/**/*.spec.ts` | Playwright, browser-based |
| **Test utilities** | `src/tests/` | Mocks, fixtures, setup |

### Documentation Files

| Type | Location |
| --- | --- |
| **API documentation** | `docs/` (\*.md files) |
| **Implementation plans** | `.github/plan/` |
| **Architecture decisions** | `docs/dev.content.md`, `AGENTS.md` |
| **Coding standards** | `.github/instructions/` (auto-applied by filename) |
| **Code comments** | Inline in code files (docstrings for complex functions) |

---

## 5. Naming and Organization Conventions

### File Naming Patterns

| File Type | Convention | Examples |
| --- | --- | --- |
| **React Components** | PascalCase | `ComicCard.tsx`, `SearchResults.tsx`, `BookmarkButton.tsx` |
| **Custom Hooks** | camelCase, `use-` prefix | `use-debounce.ts`, `use-mobile.ts`, `use-keyboard-navigation.tsx` |
| **DAL Classes** | PascalCase, `-dal` suffix | `ComicDal`, `BookmarkDal`, `SearchDal` |
| **DAL files** | kebab-case, `-dal` suffix | `comic-dal.ts`, `bookmark-dal.ts` |
| **Server Actions** | camelCase, `-actions` suffix | `bookmark.actions.ts`, `rating.actions.ts` |
| **Zod Schemas** | camelCase, `-schema` suffix | `comic-schema.ts`, `bookmark-schema.ts` |
| **Stores** | camelCase, `use-` prefix | `use-reader-store.ts`, `use-bookmark-store.ts` |
| **Utility files** | kebab-case | `query-client.ts`, `image-optimization.ts` |
| **Test files** | Match source name, `.test.ts` or `.spec.ts` | `comic-dal.test.ts`, `search-schema.spec.ts` |
| **Configuration** | camelCase or kebab-case | `next.config.ts`, `vitest.config.mts` |

### Folder Naming Patterns

| Folder Type | Convention | Examples |
| --- | --- | --- |
| **Feature domains** | lowercase | `comics/`, `bookmarks/`, `search/` |
| **Type groupings** | lowercase, descriptive | `components/`, `hooks/`, `stores/`, `types/` |
| **Internal organization** | lowercase | `shared/`, `utils/`, `mocks/`, `fixtures/` |
| **Generated output** | dot-prefixed | `.next/`, `.turbo/`, `.husky/` |

### Component Prop Naming

```typescript
// Consistent prop naming across all components
interface ComicCardProps {
  comic: Comic; // Object data
  onBookmark?: () => void; // Event handlers
  isLoading?: boolean; // Boolean flags
  className?: string; // Styling overrides
}
```

### Import Organization

```typescript
// Standard import order (ESLint enforces)
import React from "react"; // React imports
import { useState } from "react";

import Image from "next/image"; // Next.js imports
import { useRouter } from "next/navigation";

import { Button } from "@/components/ui/button"; // Internal imports (path aliases)
import { comicDal } from "@/dal/comic-dal";
import type { Comic } from "@/types/comic";

import { cn } from "@/lib/utils"; // Utilities

// Blank line

export function MyComponent() {} // Component body
```

### Namespace/Module Mapping

**Path Alias → Folder Location:**

```typescript
import X from "@/lib/utils"; // src/lib/utils.ts
import X from "ui/button"; // src/components/ui/button.tsx
import X from "database/db"; // src/database/db.ts
import X from "schemas/comic"; // src/schemas/comic.schema.ts
import X from "components/ComicCard"; // src/components/comics/comic-card.tsx
```

---

## 6. Navigation and Development Workflow

### Entry Points & Getting Started

| Task | Starting Point |
| --- | --- |
| **Understand architecture** | Read `AGENTS.md`, `.github/copilot-instructions.md`, `docs/dev.content.md` |
| **View database schema** | `src/database/schema.ts` (604 lines, all tables & relations) |
| **Understand a feature** | Navigate feature directory: `src/app/(root)/[feature]/` → `src/dal/[entity]-dal.ts` → `src/actions/[entity].actions.ts` → `src/components/[feature]/` |
| **Add new page** | Create `src/app/(root)/[new-feature]/page.tsx` as Server Component |
| **Add new component** | Create `src/components/[feature]/NewComponent.tsx` with proper typing |
| **Add new API** | Create Server Action in `src/actions/[entity].actions.ts`, not API routes |

### Common Development Tasks

#### **Add a New Feature (Full Stack)**

```
1. Database
   └─ src/database/schema.ts: Add table definition
   └─ pnpm db:push: Apply schema change

2. Data Access
   └─ src/dal/new-entity-dal.ts: Create DAL class (extend BaseDal<T>)
   └─ src/dal/index.ts: Export singleton instance

3. Validation
   └─ src/schemas/new-entity-schema.ts: Create Zod schemas

4. Business Logic
   └─ src/actions/new-entity.actions.ts: Create Server Actions

5. UI
   └─ src/app/(root)/new-feature/page.tsx: Create page
   └─ src/components/[feature]/: Create components
   └─ src/stores/use-new-store.ts: If UI state needed
   └─ src/hooks/use-new-hook.ts: If logic reuse needed

6. Tests
   └─ src/tests/schemas/new-entity-schema.spec.ts: Unit tests
   └─ tests/new-feature.spec.ts: E2E tests
```

#### **Add a New Component**

```
1. Create file: src/components/[feature]/NewComponent.tsx
2. Props interface: Define `interface NewComponentProps { }`
3. Exports: Server Component (default) + CSS module or Tailwind
4. If interactive: Add "use client" at top
5. Test: src/components/[feature]/NewComponent.test.tsx
```

#### **Fix a Bug in a Feature**

```
1. Identify layer where bug occurs:
   - Page: src/app/(root)/[feature]/page.tsx
   - Component: src/components/[feature]/Component.tsx
   - Action: src/actions/[entity].actions.ts
   - DAL: src/dal/[entity]-dal.ts

2. Check test file for that layer: *.test.ts or *.spec.ts

3. Write failing test first (TDD), then fix code

4. Run tests: pnpm test --watch
```

#### **Add a New API Endpoint** (Rare)

```
⚠️  Prefer Server Actions (src/actions/) over API routes.

If absolute must: Create src/app/api/[route]/route.ts
- Avoid if data is internal
- Use only for external webhooks or third-party integration
```

### Dependency Patterns

**Data Flow (Server-side):**

```
Page (src/app/)
  └─ await params/searchParams
  └─ DAL query with .with() eager loading
  └─ props to Client Component
```

**Mutations:**

```
Server Action (src/actions/)
  └─ Validate with Zod schema
  └─ DAL mutation
  └─ revalidateTag/revalidatePath
  └─ Return ActionResult<T>
```

**Client State:**

```
useClient Component
  └─ Zustand store for UI state
  └─ useTransition for Server Action calls
  └─ useState only for form inputs
```

### File Navigation Quick Tips

1. **Jump to related files:**
   - In VSCode: Ctrl+Click on imports
   - Feature in URLS → folder in `src/app/(root)/[feature]/`
   - DAL class in imports → `src/dal/[entity]-dal.ts`
   - Schema in imports → `src/schemas/[entity]-schema.ts`

2. **Search across codebase:**
   - Component usage: Cmd+Shift+F, search `<ComicCard`
   - Function calls: Cmd+Shift+F, search `comicDal.`
   - Type usage: Cmd+Shift+F, search `type.*Comic`

3. **Understand scope:**
   - `src/components/ui/` → Primitives (shared across all)
   - `src/components/[feature]/` → Feature-specific UI
   - `src/dal/` → Always queries, never mutations
   - `src/actions/` → Always mutations, never queries

---

## 7. Build and Output Organization

### Build Process

```
Input Files (src/)
  ↓
TypeScript Compilation (tsconfig.json)
  ↓
Next.js App Router Processing
  ├─ Page routes → static/dynamic routes
  ├─ API routes → serverless functions
  ├─ Automatic code splitting
  └─ Component optimization (React Compiler)
  ↓
Turbopack Bundling
  ├─ CSS (Tailwind v4) → bundled
  ├─ Assets → optimized (next/image)
  └─ JavaScript → code-split by route
  ↓
Output (.next/)
  ├─ .next/standalone/ — Production runtime
  ├─ .next/static/ — Assets, CSS, JS
  └─ .next/cache/ — Build cache
```

### Build Commands

| Command | Purpose | Output |
| --- | --- | --- |
| `pnpm dev` | Development server (Turbopack, hot reload) | Port 3000; no build artifact |
| `pnpm build` | Production build (optimized) | `.next/` directory (~34s) |
| `pnpm start` | Run production build locally | Port 3000 (from `.next/`) |
| `pnpm build:analyze` | Build with bundle analysis | `.next/` + bundle report |
| `pnpm build:debug` | Build with debug prerendering | `.next/` + prerender log |

### Output Structure

```
.next/
├── standalone/                       # Self-contained app (for Docker)
│   └── node_modules/
│   └── .next/
│   └── package.json
│
├── static/                           # Assets
│   ├── chunks/                       # Code splits per route
│   ├── css/                          # Tailwind CSS bundles
│   ├── media/                        # Optimized images
│   └── pages/                        # Page markup
│
├── cache/                            # Build cache
│   ├── webpack/                      # Webpack cache
│   └── turbo/                        # Turbo cache
│
└── server/                           # Server runtime
    └── app/                          # App Router compiled
```

### Environment-Specific Builds

**Development:**

- No optimization
- Source maps included
- Fast rebuild on file change
- Client + Server Components both rendered

**Production:**

- Full optimization (tree-shaking, minification)
- No source maps (unless `NEXT_SOURCE_MAPS=1`)
- Static generation where possible (`generateStaticParams`)
- React Compiler optimizations applied

---

## 8. Technology-Specific Organization

### Node.js / Next.js Patterns

#### Module Organization

```typescript
// ESM (ECMAScript modules) throughout
import X from "@/lib/utils"; // Path aliases resolve to src/
import X from "./relative/path"; // Relative imports
import X from "npm-package"; // npm packages

// Type-only imports
import type { Comic } from "@/types/comic";
```

#### Script Organization

**npm/pnpm scripts (package.json) are organized in 5 tiers:**

```json
{
  "scripts": {
    "dev": "next dev", // TIER 1: Essential (daily use)
    "build": "next build",
    "test": "vitest",
    "db:push": "drizzle-kit push", // TIER 2: Database
    "health:db": "tsx src/scripts/checkDb.ts", // TIER 3: Health
    "lint:fix": "eslint --fix", // TIER 4: Code quality
    "scaffold": "tsx src/scripts/scaffold.ts" // TIER 5: Generation
  }
}
```

#### Configuration Management

```typescript
// src/lib/env.ts — Zod-validated singleton
const env = z
  .object({
    DATABASE_URL: z.string().url(),
    AUTH_SECRET: z.string().min(32),
    NEXT_PUBLIC_API_URL: z.string().url().optional()
  })
  .parse(process.env);

export function getEnv() {
  return env; // Validated at startup
}

// Usage in any module
const { DATABASE_URL } = getEnv(); // Type-safe, no process.env.
```

### React-Specific Patterns

#### Server vs. Client Components

```typescript
// SERVER COMPONENT (default)
export default async function Page() {
  const data = await fetch( /* ... */ );
  return <Client data={data} />;  // Pass as prop
}

// CLIENT COMPONENT (explicit)
"use client";
export function Client({ data }) {
  const [state, setState] = useState();
  return <div>{ /* browser APIs */ }</div>;
}
```

#### React Compiler (Enabled)

- ✅ Auto-memoization of components and values
- ❌ Never use manual `useMemo()`, `useCallback()`, `memo()` — they block optimization
- ✅ Write plain code; compiler handles optimization

#### Hooks Patterns

```typescript
// Custom hook for logic reuse (client-side)
export function usePagination(items: T[], pageSize: number) {
  const [page, setPage] = useState(1);
  const paged = items.slice((page - 1) * pageSize, page * pageSize);
  return { paged, page, setPage };
}

// Usage
const { paged, page, setPage } = usePagination(comics, 10);
```

### Next.js App Router Patterns

#### Dynamic Routes

```
src/app/comics/[slug]/page.tsx
  └─ Accessed as: /comics/attack-on-titan

export async function generateStaticParams() {
  const comics = await comicDal.list();
  return comics.map(c => ({ slug: c.slug }));  // Pre-render
}

export default async function Page({ params }: { params: Promise<{ slug: string }> }) {
  const { slug } = await params;  // v16 breaking change: await params
  const comic = await comicDal.getBySlug(slug);
  return <ComicDetail comic={comic} />;
}
```

#### Nested Routes with Layouts

```
src/app/(root)/comics/layout.tsx → shared layout
  └─ src/app/(root)/comics/page.tsx → list
  └─ src/app/(root)/comics/[slug]/page.tsx → detail
  └─ src/app/(root)/comics/[slug]/[chapterId]/page.tsx → reader
```

#### Route Groups (Non-URL)

```
src/app/(auth)/sign-in/page.tsx → /sign-in (route group doesn't affect URL)
src/app/(root)/comics/page.tsx → /comics (different layout group)
```

---

## 9. Extension and Evolution

### Adding New Features While Maintaining Conventions

#### Step 1: Plan the Feature

Create implementation plan in `.github/plan/`:

```
features/
├─ feature-core-features-X.md (comprehensive roadmap)
└─ [FEATURE]-IMPLEMENTATION.md (execution steps)
```

#### Step 2: Extend Database Schema

```typescript
// src/database/schema.ts
export const newTable = pgTable('new_table', {
  id: serial().primaryKey(),
  name: varchar(255).notNull(),
  createdAt: timestamp().defaultNow(),
  updatedAt: timestamp().defaultNow().$onUpdate(() => new Date()),
  // ... relations
});

// Migrate to database
$ pnpm db:push
```

#### Step 3: Create DAL Class

```typescript
// src/dal/new-entity-dal.ts
import { BaseDal } from "./base-dal";
import { db } from "@/database/db";

type NewEntityType = typeof newTable.$inferSelect;

export class NewEntityDal extends BaseDal<NewEntityType> {
  async list() {
    return db.query.newTable.findMany({
      with: { relations: true } // Eager load
    });
  }
}

export const newEntityDal = new NewEntityDal();
```

#### Step 4: Create Validation Schemas

```typescript
// src/schemas/new-entity-schema.ts
import { z } from "zod";

const BaseSchema = z.object({
  name: z.string().min(1).max(255)
});

export const CreateSchema = BaseSchema;
export const UpdateSchema = BaseSchema.partial().extend({
  id: z.number().int()
});
```

#### Step 5: Create Server Actions

```typescript
// src/actions/new-entity.actions.ts
"use server";
import { auth } from "@/auth";
import type { ActionResult } from "./types";

export async function createNewEntityAction(
  input: unknown
): Promise<ActionResult<NewEntity>> {
  const session = await auth();
  if (!session?.user?.id)
    return { ok: false, error: "Not authenticated" };

  const parsed = CreateSchema.safeParse(input);
  if (!parsed.success)
    return { ok: false, error: parsed.error.errors[0]?.message };

  try {
    const entity = await newEntityDal.create(parsed.data);
    revalidatePath("/new-feature");
    return { ok: true, data: entity };
  } catch (error) {
    return { ok: false, error: "Failed to create" };
  }
}
```

#### Step 6: Create UI Components

```typescript
// src/components/new-feature/NewEntityCard.tsx
import { BookmarkButton } from '@/components/comics/BookmarkButton';

export function NewEntityCard({ entity }: { entity: NewEntity }) {
  return (
    <article className="card">
      {/* Component content */}
    </article>
  );
}

// src/components/new-feature/NewEntityList.tsx
"use client";

export function NewEntityListClient({
  entities
}: {
  entities: NewEntity[]
}) {
  return (
    <div className="grid gap-4">
      {entities.map(e => <NewEntityCard key={e.id} entity={e} />)}
    </div>
  );
}
```

#### Step 7: Create Page Route

```typescript
// src/app/(root)/new-feature/page.tsx
import { NewEntityListClient } from '@/components/new-feature/NewEntityList';
import { newEntityDal } from '@/dal/new-entity-dal';

export default async function NewFeaturePage() {
  const entities = await newEntityDal.list();

  return (
    <main>
      <h1>New Feature</h1>
      <NewEntityListClient entities={entities} />
    </main>
  );
}
```

#### Step 8: Add Tests

```typescript
// src/tests/schemas/new-entity-schema.spec.ts
import { describe, it, expect } from "vitest";
import { CreateSchema } from "@/schemas/new-entity-schema";

describe("CreateSchema", () => {
  it("validates valid input", () => {
    const result = CreateSchema.safeParse({ name: "Test" });
    expect(result.success).toBe(true);
  });
});

// tests/new-feature.spec.ts
import { test, expect } from "@playwright/test";

test("user can view new feature", async ({ page }) => {
  await page.goto("/new-feature");
  await expect(page.getByRole("heading")).toContainText(
    "New Feature"
  );
});
```

### Scalability Patterns

#### Breaking Down Large Modules

**Before (monolithic):**

```
src/components/comics/
├── ComicCard.tsx (200 lines, too large)
└── ...
```

**After (decomposed):**

```
src/components/comics/
├── ComicCard.tsx (50 lines, composed)
├── ComicCardImage.tsx (60 lines)
├── ComicCardMetadata.tsx (80 lines)
└── ComicCardActions.tsx (40 lines)
```

#### Code Splitting Strategies

- **Route-based:** Pages automatically code-split
- **Dynamic imports:** `const Component = dynamic(() => import('./'))`
- **Lazy components:** Split heavy features like search or admin dashboard

### Refactoring Patterns

**When to refactor:**

- Component grows >200 lines → Extract sub-components
- Repeated logic in 2+ places → Extract hook or utility
- Complex DAL queries → Add helper method to DAL class
- Type duplication → Extract to `src/types/`

**Safe refactoring:**

1. Write tests first (capture current behavior)
2. Refactor code
3. Verify tests still pass
4. Commit with descriptive message

---

## 10. Structure Templates

### Template 1: New Feature (Full Stack)

**Use when:** Adding a new domain (e.g., Forums, Discussions)

```
1. Create folders:
   - src/app/(root)/[new-feature]/
   - src/components/[new-feature]/
   - src/dal/[new-entities]*.ts
   - src/actions/[new-entities]*.ts
   - src/schemas/[new-entities]*.ts

2. Create database tables:
   - src/database/schema.ts (add tables + relations)
   - pnpm db:push

3. Create DAL:
   - src/dal/new-entity-dal.ts (extend BaseDal)
   - src/dal/index.ts (export instance)

4. Create validation:
   - src/schemas/new-entity-schema.ts (Zod schemas)

5. Create actions:
   - src/actions/new-entity.actions.ts (CRUD + special operations)

6. Create components:
   - src/components/[new-feature]/NewEntityCard.tsx
   - src/components/[new-feature]/NewEntityList.tsx (client)
   - src/components/[new-feature]/NewEntityForm.tsx (form)

7. Create pages:
   - src/app/(root)/[new-feature]/page.tsx (list)
   - src/app/(root)/[new-feature]/[id]/page.tsx (detail, if needed)

8. Create tests:
   - src/tests/schemas/new-entity-schema.spec.ts (schema validation)
   - src/[dal/new-entity-dal].test.ts (DAL queries)
   - tests/[new-feature].spec.ts (E2E)

9. Create store (if complex UI state):
   - src/stores/use-new-feature-store.ts (Zustand)

10. Create hooks (if logic reuse):
    - src/hooks/use-new-feature-logic.ts
```

### Template 2: New Component

**Use when:** Adding a reusable UI component

```
// src/components/[feature]/NewComponent.tsx

import { ReactNode } from 'react';

interface NewComponentProps {
  title: string;
  subtitle?: string;
  children: ReactNode;
  onAction?: () => void;
  className?: string;
}

export function NewComponent({
  title,
  subtitle,
  children,
  onAction,
  className
}: NewComponentProps) {
  return (
    <div className={className}>
      <h2>{title}</h2>
      {subtitle && <p>{subtitle}</p>}
      <div>{children}</div>
      {onAction && <button onClick={onAction}>Action</button>}
    </div>
  );
}
```

**Test template:**

```typescript
// src/components/[feature]/NewComponent.test.tsx

import { describe, it, expect } from 'vitest';
import { render, screen } from '@testing-library/react';
import { NewComponent } from './NewComponent';

describe('NewComponent', () => {
  it('renders title and subtitle', () => {
    render(
      <NewComponent title="Test" subtitle="Sub">
        <p>Content</p>
      </NewComponent>
    );

    expect(screen.getByText('Test')).toBeInTheDocument();
    expect(screen.getByText('Sub')).toBeInTheDocument();
  });
});
```

### Template 3: New Server Action

```typescript
// src/actions/new-entity.actions.ts

"use server";

import { auth } from "@/auth";
import type { ActionResult } from "./types";
import { newEntityDal } from "@/dal/new-entity-dal";
import {
  CreateSchema,
  UpdateSchema
} from "@/schemas/new-entity-schema";
import { revalidatePath } from "next/cache";

export async function createNewEntityAction(
  input: unknown
): Promise<ActionResult<NewEntity>> {
  // 1. AUTH CHECK
  const session = await auth();
  if (!session?.user?.id) {
    return { ok: false, error: "Must be logged in" };
  }

  // 2. VALIDATE INPUT
  const parsed = CreateSchema.safeParse(input);
  if (!parsed.success) {
    return {
      ok: false,
      error: parsed.error.errors[0]?.message ?? "Invalid input"
    };
  }

  try {
    // 3. MUTATE (via DAL)
    const entity = await newEntityDal.create({
      ...parsed.data,
      createdById: session.user.id
    });

    // 4. REVALIDATE CACHE
    revalidatePath("/new-feature");

    // 5. RETURN RESULT
    return { ok: true, data: entity };
  } catch (error) {
    console.error("Failed to create entity:", error);
    return { ok: false, error: "Failed to create, please try again" };
  }
}

export async function updateNewEntityAction(
  input: unknown
): Promise<ActionResult<NewEntity>> {
  const session = await auth();
  if (!session?.user?.id) {
    return { ok: false, error: "Not authenticated" };
  }

  const parsed = UpdateSchema.safeParse(input);
  if (!parsed.success) {
    return { ok: false, error: parsed.error.errors[0]?.message };
  }

  try {
    const entity = await newEntityDal.update(parsed.data.id, {
      ...parsed.data,
      updatedBy: session.user.id
    });
    revalidatePath("/new-feature");
    return { ok: true, data: entity };
  } catch (error) {
    return { ok: false, error: "Update failed" };
  }
}

export async function deleteNewEntityAction(
  id: number
): Promise<ActionResult<void>> {
  const session = await auth();
  if (!session?.user?.id) {
    return { ok: false, error: "Not authenticated" };
  }

  try {
    await newEntityDal.delete(id);
    revalidatePath("/new-feature");
    return { ok: true, data: undefined };
  } catch (error) {
    return { ok: false, error: "Delete failed" };
  }
}
```

### Template 4: Test Structure

**Unit Test (Vitest, jsdom):**

```typescript
// src/dal/new-entity-dal.test.ts

import { describe, it, expect, beforeEach, vi } from "vitest";
import { NewEntityDal } from "./new-entity-dal";

describe("NewEntityDal", () => {
  let dal: NewEntityDal;

  beforeEach(() => {
    dal = new NewEntityDal();
    // Mock database if needed
    vi.mock("@/database/db");
  });

  it("returns all entities with eager loading", async () => {
    const entities = await dal.list();
    expect(entities).toBeInstanceOf(Array);
  });

  it("filters entities by criteria", async () => {
    const filtered = await dal.listByCriteria({ status: "active" });
    expect(filtered).toBeDefined();
  });
});
```

**E2E Test (Playwright):**

```typescript
// tests/new-feature.spec.ts

import { test, expect } from "@playwright/test";

test.describe("New Feature", () => {
  test.beforeEach(async ({ page }) => {
    await page.goto("/new-feature");
  });

  test("displays list of entities", async ({ page }) => {
    await expect(
      page.getByRole("heading", { name: /New Feature/i })
    ).toBeVisible();

    const cards = page.getByRole("article");
    await expect(cards).toBeDefined();
  });

  test("user can create new entity", async ({ page }) => {
    await test.step("Open creation form", async () => {
      await page.getByRole("button", { name: /Create/i }).click();
      await expect(page.getByRole("dialog")).toBeVisible();
    });

    await test.step("Fill and submit form", async () => {
      await page.getByLabel("Title").fill("New Entity");
      await page
        .getByRole("button", { name: /Create/i })
        .first()
        .click();
    });

    await test.step("Verify success", async () => {
      await expect(
        page.getByText("New Entity Created")
      ).toBeVisible();
    });
  });
});
```

---

## 11. Structure Enforcement

### Automated Validation

**Type Safety:**

```bash
pnpm type-check     # TypeScript strict mode, 0 errors required
                    # Catches: missing imports, wrong types, unused vars
```

**Code Quality:**

```bash
pnpm lint           # ESLint rules
                    # Catches: import ordering, prop sorting, naming conventions
pnpm lint:fix       # Auto-fix common issues

pnpm format:check   # Prettier formatting
pnpm format         # Auto-format
```

**Testing:**

```bash
pnpm test           # Vitest unit tests (jsdom environment)
pnpm test:ui        # Playwright E2E tests
                    # All tests must pass
```

**Build Verification:**

```bash
pnpm build          # Production build validation
                    # Catches: dead code, unused imports, build errors
```

### Quality Gate (Pre-commit)

```bash
# All 4 must pass before committing
pnpm type-check && pnpm lint:fix && pnpm test && pnpm build
```

### ESLint Rules for Structure

| Rule | Enforces |
| --- | --- |
| `no-explicit-any` | No raw `any` types (use proper TypeScript) |
| `import/order` | Standard import grouping (React, Next.js, internal, utils) |
| `jsx-a11y/*` | Accessibility (alt text, ARIA labels, semantic HTML) |
| `@next/next/*` | Next.js best practices (Image, Link, etc.) |
| `react/jsx-sort-props` | Consistent prop ordering |
| `@typescript-eslint/no-unused-vars` | No unused declarations |

### Documentation Practices

**Documenting Changes:**

1. Update implementation plan in `.github/plan/`
2. Update Architecture as Code in `AGENTS.md`
3. Add inline code comments for non-obvious logic
4. Update `docs/dev.content.md` for cross-cutting concerns

**Recording Decisions:**

```markdown
// docs/dev.content.md — Section 5: Architecture Decisions

## Decision: Feature X Uses Pattern Y

**Context:** Problem statement **Decision:** Chosen approach **Rationale:** Why this was selected **Tradeoffs:** What we gave up **Alternative:** Other options considered **Date:** 2026-03-07
```

### Structure Evolution

**When structure needs updating:**

1. Create RFC (Request for Comments) in `.github/plan/RFC-*.md`
2. Implement incrementally (don't refactor entire codebase at once)
3. Update this blueprint (Section 12: Maintenance)
4. Update ESLint rules if new conventions introduced
5. Update AGENTS.md with new patterns

**Example Evolution:**

- Phase 1: Add new folder structure
- Phase 2: Gradually migrate existing code to new structure
- Phase 3: Enforce new structure via linting rules
- Phase 4: Remove old structure when fully migrated

---

## 12. Maintenance Documentation

### Updating This Blueprint

**When to update:**

- New folder structure added
- File naming convention changed
- New technology integrated
- New pattern established

**How to update:**

1. Edit this file (architecture.md`)
2. Update relevant section (use Cmd+F to find)
3. Include version bump and date
4. Commit with message: `docs: update folder structure blueprint`

### Version History

| Version | Date | Changes |
| --- | --- | --- |
| 1.0 | 2026-03-07 | Initial blueprint for ComicWise phase 4+ structure |

### Key Metrics to Track

- **Code distribution:** Which folders have most code (src/components/, src/dal/)?
- **Test coverage:** Ratio of test files to source files
- **Build time:** Turbopack compilation time (target: <40s)
- **Bundle size:** CSS/JS bundle sizes per route (monitor on builds)
- **Type safety:** Zero TypeScript errors (enforced)
- **Test pass rate:** 100% passing tests required

### Onboarding Resources

**New developer checklist:**

1. Read `AGENTS.md` (quick reference - 15 min)
2. Read `.github/copilot-instructions.md` (comprehensive guide - 30 min)
3. Read `docs/dev.content.md` sections 1-5 (patterns - 20 min)
4. Explore one feature end-to-end:
   - Page: `src/app/(root)/[feature]/page.tsx`
   - DAL: `src/dal/[entity]-dal.ts`
   - Actions: `src/actions/[entity].actions.ts`
   - Components: `src/components/[feature]/`
5. Run quality gate: `pnpm type-check && pnpm test && pnpm build`
6. Make first contribution following template patterns

### Troubleshooting Structure Issues

| Problem | Solution |
| --- | --- |
| **Can't find component** | Check `src/components/[feature]/`, search for filename |
| **Type error after adding file** | Run `pnpm type-check`, verify imports use path aliases |
| **DAL query missing field** | Check `.with()` eager loading, verify schema has field |
| **Circular imports** | Restructure to avoid A→B→A imports; move shared code to utils |
| **Component too large** | Decompose into smaller components, extract hooks |
| **Test fails after refactor** | Generated SQL migrations may have broken; run `pnpm db:reset` |

---

## Summary

ComicWise uses a **feature-driven, layered architecture** with clear separation of concerns:

- **Presentation:** `src/app/` (pages) + `src/components/` (UI)
- **Business Logic:** `src/actions/` (mutations) + `src/stores/` (UI state)
- **Data Access:** `src/dal/` (queries) + `src/database/` (schema)
- **Validation:** `src/schemas/` (Zod validation)
- **Infrastructure:** Authentication, utilities, hooks, types

**Consistency is enforced via:**

- TypeScript strict mode (0 errors)
- ESLint rules (auto-fixable)
- Mandatory tests (100% pass)
- Production build validation

**Extensibility is built-in via:**

- Clear templates for new features
- DAL pattern prevents N+1 queries
- Server Actions standardize mutations
- Path aliases avoid relative imports

Follow the templates in Section 10 and refer to implementation plans in `.github/plan/` when adding new features.

---

**Last Updated:** 2026-03-07 **Maintainer:** ComicWise Development Team **Next Review:** After Phase 5 implementation completion
