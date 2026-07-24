# Comicwise — Folder Structure Blueprint

## Project Root

```
comicwise/                              # Project root (pnpm workspace)
├── AGENTS.md                           # AI-assistant context for the repo
├── API_REFERENCE.md                    # Full API endpoint reference
├── ARCHITECTURE.md                     # Project architecture overview
├── CHANGELOG.md                        # Release history
├── CONTRIBUTING.md                     # Contributor guidelines
├── DATABASE_SCHEMA.md                  # Drizzle schema documentation
├── DEPLOYMENT_GUIDE.md                 # Deployment instructions
├── DEVELOPMENT_GUIDE.md                # Local dev setup & conventions
├── README.md                           # Project readme
├── SECURITY.md                         # Security disclosures
├── SETUP_GUIDE.md                      # Onboarding setup
├── TESTING_GUIDE.md                    # Test suite documentation
│
├── package.json                        # Dependencies & 130+ scripts
├── pnpm-workspace.yaml                 # PNPM workspace config
├── pnpm-lock.yaml                      # Dependency lockfile
├── bun.lock                            # Bun lockfile (fallback)
│
├── next.config.ts                      # Next.js 16 config
├── drizzle.config.ts                   # Drizzle Kit configuration
├── tsconfig.json                       # TypeScript configuration
├── eslint.config.mts                   # ESLint 9 flat config
├── .prettierrc.ts                      # Prettier config
├── postcss.config.mjs                  # PostCSS config (Tailwind)
├── vitest.config.mts                   # Vitest config
├── playwright.config.mts               # Playwright E2E config
├── next-sitemap.config.ts              # Sitemap generation
├── components.json                     # shadcn/ui config
├── appConfig.ts                        # Zod-validated env config
│
├── .env.example                        # Environment template
├── .env.local.example                  # Local env template
├── .env.local                          # Local env (gitignored)
├── .env.test                           # Test env
│
├── docker-compose.yml                  # Local services (PostgreSQL, Redis)
├── Dockerfile                          # Production container build
│
├── cleanup.sh / cleanup.ps1            # Project cleanup scripts
├── dev.sh / dev.ps1                    # Dev server launcher
├── setup-dev.sh / setup-dev.ps1        # First-time setup
├── quality-gate.sh / quality-gate.ps1  # Pre-commit quality checks
├── install-vscode-extensions.sh /.ps1  # VS Code extension installer
│
├── .gitignore
├── .editorconfig
├── .dockerignore
├── .gitattributes
├── .all-contributorsrc
├── .codespellrc
├── .cursorrules
├── .cwrc.json
│
├── .github/
│   ├── copilot-instructions.md
│   ├── copilot/copilot-instructions.md
│   ├── dependabot.yml
│   ├── ISSUE_TEMPLATE/
│   │   ├── bug_report.md
│   │   └── feature_request.md
│   ├── PULL_REQUEST_TEMPLATE/pull_request.md
│   ├── plugin/marketplace.json
│   └── workflows/
│       ├── ci.yml                      # CI pipeline
│       ├── test.yml.disabled
│       ├── deploy.yml.disabled
│       ├── playwright.yml.disabled
│       └── copilot-setup-steps.yml.disabled
│
├── .husky/
│   ├── pre-commit                      # Husky pre-commit hook
│   └── _/                              # Husky internal scripts
│
├── .schemas/
│   ├── collection.schema.json
│   ├── cookbook.schema.json
│   ├── my.tools.yml
│   └── tools.schema.json
│
├── .vscode/
│   ├── extensions.json
│   ├── launch.json
│   ├── settings.json
│   └── tasks.json
│
├── docs/
│   ├── architecture.md
│   ├── Project_Architecture/
│   │   ├── Project_Architecture_Blueprint.md
│   │   ├── Project_Folder_Structure.md
│   │   ├── Technology_Stack_Blueprint.md
│   │   ├── Workflow_Analysis.md
│   │   ├── exemplars.md
│   │   ├── comicwise_architecture.md     ← THIS FILE
│   │   ├── comicwise_folders.md          ← THIS FILE
│   │   ├── comicwise_techstack.md        ← THIS FILE
│   │   └── projects/comicwise/           ← Duplicate set
│   ├── ... (30+ doc files)
│
├── public/
│   ├── file.svg
│   ├── globe.svg
│   ├── next.svg
│   ├── vercel.svg
│   ├── window.svg
│   ├── shadcn.jpg
│   ├── placeholder-comic.jpg
│   ├── robots.txt
│   ├── sitemap.xml / sitemap-0.xml
│   └── uploads/.gitkeep
│
├── src/                                 # ← Main source tree
│   ├── app/                             # Next.js App Router pages
│   ├── actions/                         # Server Actions
│   ├── components/                      # React components
│   ├── database/                        # Drizzle schema & migrations
│   ├── lib/                             # Utility functions
│   ├── hooks/                           # Custom React hooks
│   ├── stores/                          # Zustand stores
│   ├── schemas/                         # Zod validation schemas
│   ├── types/                           # TypeScript type definitions
│   ├── styles/                          # Fonts & global CSS
│   ├── assets/                          # SVG assets
│   ├── scripts/                         # CLI utility scripts
│   ├── dal/                             # Data access layer
│   ├── data/                            # Static/data files
│   ├── storages/                        # Storage adapters (ImageKit)
│   ├── tests/                           # Test suites
│   └── backuptests/                     # Backup test snapshots
│
└── *.md / *.json / *.txt               # Reports, logs, analysis docs
```

## Source Tree Detail (`src/`)

```
src/
├── app/                                 # Next.js App Router
│   ├── layout.tsx                       # Root layout
│   ├── global-error.tsx                 # Global error boundary
│   ├── loading.tsx                      # Root loading state
│   ├── not-found.tsx                    # 404 page
│   ├── favicon.ico
│   │
│   ├── (auth)/                          # Auth route group (minimal layout)
│   │   ├── layout.tsx
│   │   ├── sign-in/page.tsx
│   │   └── sign-up/page.tsx
│   │
│   ├── (root)/                          # Main app route group (nav + footer)
│   │   ├── layout.tsx
│   │   ├── page.tsx                     # Home / landing
│   │   ├── analytics/layout.tsx + page.tsx
│   │   ├── authors/[id]/page.tsx
│   │   ├── bookmarks/page.tsx
│   │   ├── browse/page.tsx
│   │   ├── comments/page.tsx
│   │   ├── feed/page.tsx
│   │   ├── genres/[id]/page.tsx
│   │   ├── notifications/page.tsx
│   │   ├── ratings/page.tsx
│   │   ├── reading-progress/page.tsx
│   │   ├── search/page.tsx + error.tsx
│   │   ├── settings/page.tsx
│   │   └── profile/
│   │       ├── page.tsx + error.tsx + loading.tsx
│   │       ├── [id]/followers/page.tsx
│   │       ├── [id]/following/page.tsx
│   │       ├── edit/page.tsx + error.tsx + loading.tsx
│   │       ├── settings/page.tsx + error.tsx + loading.tsx
│   │       ├── change-password/page.tsx
│   │       └── delete-account/page.tsx
│   │
│   ├── admin/                           # Admin panel (sidebar layout)
│   │   ├── layout.tsx + page.tsx
│   │   ├── artists/page.tsx
│   │   ├── audit-logs/page.tsx
│   │   ├── authors/page.tsx
│   │   ├── chapters/page.tsx
│   │   ├── comics/page.tsx
│   │   ├── genres/page.tsx
│   │   ├── permissions/page.tsx
│   │   ├── roles/page.tsx
│   │   ├── types/page.tsx
│   │   └── users/page.tsx
│   │
│   └── api/                             # API route handlers
│       └── auth/[...nextauth]/route.ts   # NextAuth handler
│       └── seed/route.ts                 # Data seeding endpoint
│
├── actions/                             # Server Actions (mutations)
│   ├── admin.actions.ts                 # Admin aggregation
│   ├── artist.actions.ts
│   ├── auth.actions.ts
│   ├── author.actions.ts
│   ├── bookmark.actions.ts
│   ├── browse.actions.ts
│   ├── chapter.actions.ts
│   ├── comic.actions.ts
│   ├── comment-rating.actions.ts
│   ├── credentials.actions.ts
│   ├── follow.actions.ts
│   ├── genre.actions.ts
│   ├── goals.actions.ts
│   ├── notification.actions.ts
│   ├── password-reset.actions.ts
│   ├── profile.actions.ts
│   ├── rbac.actions.ts
│   ├── reading.actions.ts
│   ├── reading-progress.actions.ts
│   ├── search.actions.ts
│   ├── search-filters.actions.ts
│   ├── share.actions.ts
│   ├── user-preferences.actions.ts
│   └── admin/                           # Admin sub-actions
│       ├── index.ts
│       ├── artist.actions.ts
│       ├── audit-log.actions.ts
│       ├── author.actions.ts
│       ├── chapter.actions.ts
│       ├── comic.actions.ts
│       ├── genre.actions.ts
│       ├── permission.actions.ts
│       ├── role.actions.ts
│       ├── type.actions.ts
│       └── user.actions.ts
│
├── components/                          # React components (domain-grouped)
│   ├── ui/                              # Base / shadcn primitives
│   ├── layout/                          # Navigation, headers, footers
│   ├── auth/                            # Sign-in / sign-up forms
│   │   ├── sign-in/
│   │   └── sign-up/
│   ├── home/                            # Home page components
│   ├── browse/                          # Browse & filtering
│   ├── comics/                          # Comic cards, detail, reader
│   ├── reading/                         # Chapter reader
│   ├── reading-progress/               # Progress tracking
│   ├── bookmarks/                       # Bookmark list
│   ├── comments/                        # Comment threads
│   ├── ratings/                         # Rating widgets
│   ├── feed/                            # Activity feed
│   ├── recommendations/                 # Recommendation cards
│   ├── genres/                          # Genre tags & lists
│   ├── search/                          # Search bar & results
│   ├── notifications/                   # Notification items
│   ├── profile/                         # Profile display & edit
│   ├── admin/                           # Admin dashboard widgets
│   ├── analytics/                       # Charts & metrics
│   ├── settings/                        # User settings forms
│   ├── users/                           # User-related components
│   ├── theme/                           # Theme toggler
│   └── activity/                        # Activity log
│
├── database/                            # Drizzle ORM
│   ├── schema.ts                        # Main schema (~934 lines)
│   └── drizzle/                         # Migration artifacts
│       ├── meta/
│       └── *.sql                        # Generated migrations
│
├── hooks/                               # Custom React hooks
├── lib/                                 # Shared utilities
│   ├── query-client.ts                  # TanStack Query client & keys
│   ├── utils.ts                         # cn(), common helpers
│   ├── image-optimization.ts
│   ├── image-processor.ts
│   ├── performance-metrics.ts
│   └── accessibility.ts
│
├── stores/                              # Zustand state stores
│   ├── index.ts
│   ├── reader-store.ts
│   ├── use-bookmark-store.ts
│   ├── use-notification-store.ts
│   ├── use-reader-store.ts
│   ├── use-reading-progress-store.ts
│   └── use-ui-store.ts
│
├── schemas/                             # Zod schemas
│   ├── *.schema.ts                      # Per-entity schemas
│   ├── validators.ts                    # Shared validators
│   └── seed/                            # Seed data schemas (20+ files)
│
├── types/                               # TypeScript types
│   ├── index.ts
│   ├── actions-types.ts
│   ├── comic.ts / bookmark.ts / comment.ts / ...
│   └── *.d.ts                           # Ambient declarations
│
├── styles/                              # Global styles & fonts
│   ├── globals.css                      # Tailwind entrypoint
│   └── fonts/                           # Bebas Neue, Fira Mono/Sans,
│                                        # IBM Plex Sans, Martian Mono,
│                                        # Schibsted Grotesk
├── assets/svg/
│   ├── logo.tsx
│   └── auth-background-shape.tsx
│
├── scripts/                             # CLI utility scripts (tsx)
│   ├── master-setup.ts                  # Orchestrated multi-task runner
│   ├── unified-dev-setup.ts
│   ├── unified-db-operations.ts
│   ├── unified-performance-ops.ts
│   ├── unified-project-health.ts
│   ├── unified-schema-refactor.ts
│   ├── scaffold.ts                      # Component/page generator
│   ├── clear-cache.ts / cache-stats.ts
│   ├── git-commit.ts / git-init.ts
│   ├── uninstall-unused-packages.ts
│   ├── updateAnyTypes.ts / camelCaseConverter2025.ts
│   ├── fix-duplicate-paths.ts / fix-line-endings.ts
│   ├── triage-quality-gate.ts
│   └── seed/                            # Seed system (25+ entities)
│       ├── run.ts / index.ts
│       ├── config.ts / types.ts / logger.ts
│       ├── dependency-graph.ts
│       ├── data-loader.ts
│       ├── seed-orchestrator.ts
│       ├── database/                    # Batch, tx mgmt, conflict res.
│       ├── seeders/                     # Per-entity seeders (22 seeders)
│       └── helpers/                     # Image, date, creator utilities
│
├── storages/                            # Media storage adapters
│   ├── index.ts
│   ├── image-strategy.ts
│   ├── image-downloader.ts
│   └── image-kit-uploader.ts
│
├── dal/                                 # Data Access Layer
├── data/                                # Static reference data
│
├── tests/
│   ├── e2e/                             # Playwright E2E tests
│   │   ├── admin/                       # Admin panel tests
│   │   ├── auth-pages/                  # Auth-related tests
│   │   ├── pages/                       # Page-level tests
│   │   └── fixtures/                    # Auth & admin fixtures
│   ├── unit/                            # Vitest unit tests
│   │   ├── actions/                     # Server Action unit tests
│   │   └── setup-env.ts
│   └── fixtures/
│
├── auth.ts                              # NextAuth initialization
├── auth-adapter.ts                      # Drizzle auth adapter
└── auth-config.ts                       # NextAuth provider config
```

## Conventions

| Convention              | Pattern               | Example                    |
|-------------------------|-----------------------|----------------------------|
| Route groups            | `(group-name)`        | `(auth)`, `(root)`         |
| Page files              | `page.tsx`            | Always `page.tsx`          |
| Loading states          | `loading.tsx`         | Co-located with route      |
| Error boundaries        | `error.tsx`           | Co-located with route      |
| Server Actions          | `*.actions.ts`        | `comic.actions.ts`         |
| Components              | PascalCase files      | `ComicCard.tsx`            |
| Utilities               | kebab-case files      | `query-client.ts`          |
| Stores                  | `use-*-store.ts`      | `use-ui-store.ts`          |
| Database schema         | `src/database/`       | `schema.ts`, `drizzle/`    |
| Fonts                   | `src/styles/fonts/`   | Per-family subdirectory    |
