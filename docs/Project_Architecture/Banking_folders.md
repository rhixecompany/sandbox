# Banking — Folder Structure Blueprint

> **Generated:** 2026-07-24
> **Generator:** folder-structure-blueprint-generator
> **Project:** Banking (Next.js 16 Fintech App)

---

## Complete Directory Tree

```
Banking/
├── AGENTS.md                          # Project context & architecture reference
├── API_REFERENCE.md                   # API documentation
├── ARCHITECTURE.md                    # Architecture overview
├── CHANGELOG.md                       # Version history
├── CODE_STYLE.md                      # Coding conventions
├── CONTRIBUTING.md                    # Contributor guide
├── DATABASE_SCHEMA.md                 # Database schema reference
├── DEPLOYMENT_GUIDE.md                # Deployment instructions
├── DEVELOPMENT_GUIDE.md               # Development setup guide
├── LICENSE                            # License file
├── Makefile                           # Build automation targets
├── README.md                          # Project readme
├── REPOSITORY_SUMMARY.md              # High-level repo overview
├── RESEARCH_REPORT.md                 # Research documentation
├── SECURITY.md                        # Security policy
├── SETUP_GUIDE.md                     # Setup instructions
├── SUPPORT.md                         # Support information
├── SYSTEM.md                          # System documentation
├── TESTING_GUIDE.md                   # Testing guide
├── THE_STORY_OF_THIS_REPO.md          # Repository narrative

├── package.json                       # Dependencies & scripts
├── bun.lock                           # Bun lockfile
├── bunfig.toml                        # Bun configuration
├── tsconfig.json                      # TypeScript config (strict)
├── next.config.ts                     # Next.js configuration
├── next-env.d.ts                      # Next.js type declarations
├── drizzle.config.ts                  # Drizzle ORM configuration
├── eslint.config.mts                  # ESLint flat config
├── postcss.config.mjs                 # PostCSS configuration
├── playwright.config.ts               # Playwright E2E test config
├── vitest.config.ts                   # Vitest unit test config
├── components.json                    # shadcn/ui configuration
├── vercel.json                        # Vercel deployment config
├── Railway.toml                       # Railway deployment config
├── docker-compose.yml                 # Docker Compose setup
├── next-sitemap.config.ts             # Sitemap generation config
├── .prettierrc.ts                     # Prettier formatting config
├── .lintstagedrc.ts                   # Lint-staged config
├── app-config.ts                      # Application configuration

├── src/                               # [MAIN] Application source code
│   ├── app/                           # Next.js App Router pages
│   │   ├── layout.tsx                 # Root layout
│   │   ├── page.tsx                   # Home/landing page
│   │   ├── globals.css                # Global styles (Tailwind)
│   │   ├── global-error.tsx           # Global error boundary
│   │   ├── not-found.tsx              # 404 page
│   │   ├── (root)/                    # Authenticated pages group
│   │   │   ├── layout.tsx             # Root layout wrapper
│   │   │   ├── dashboard/             # Account overview dashboard
│   │   │   │   ├── page.tsx
│   │   │   │   ├── loading.tsx
│   │   │   │   └── error.tsx
│   │   │   ├── my-wallets/            # Linked bank accounts
│   │   │   │   ├── page.tsx
│   │   │   │   ├── loading.tsx
│   │   │   │   └── error.tsx
│   │   │   ├── payment-transfer/      # Send money / ACH transfers
│   │   │   │   ├── page.tsx
│   │   │   │   ├── loading.tsx
│   │   │   │   └── error.tsx
│   │   │   ├── transaction-history/   # Transaction list & search
│   │   │   │   ├── page.tsx
│   │   │   │   ├── loading.tsx
│   │   │   │   └── error.tsx
│   │   │   └── settings/              # User profile & preferences
│   │   │       ├── page.tsx
│   │   │       ├── loading.tsx
│   │   │       └── error.tsx
│   │   ├── (auth)/                    # Authentication pages group
│   │   │   ├── layout.tsx
│   │   │   ├── sign-in/               # Login page
│   │   │   │   ├── page.tsx
│   │   │   │   ├── loading.tsx
│   │   │   │   └── error.tsx
│   │   │   └── sign-up/               # Registration page
│   │   │       ├── page.tsx
│   │   │       ├── loading.tsx
│   │   │       └── error.tsx
│   │   ├── (admin)/                   # Admin panel group
│   │   │   ├── layout.tsx
│   │   │   └── admin/                 # Admin dashboard
│   │   │       ├── page.tsx
│   │   │       ├── loading.tsx
│   │   │       └── error.tsx
│   │   ├── api/                       # API Route Handlers
│   │   │   ├── auth/
│   │   │   │   ├── [...nextauth]/     # NextAuth catch-all route
│   │   │   │   ├── local-create/      # Credentials registration
│   │   │   │   └── local-validate/    # Credentials validation
│   │   │   ├── dwolla/
│   │   │   │   └── webhook/           # Dwolla webhook receiver
│   │   │   └── health/                # Health check endpoint
│   │   └── __playwright__/            # Playwright test helpers
│   │       └── set-cookie/            # Cookie setting route
│   │
│   ├── actions/                       # Server Actions (mutations)
│   │   ├── auth.register.ts           # User registration
│   │   ├── auth.signin.ts             # User sign-in
│   │   ├── plaid.actions.ts           # Plaid link token, exchange
│   │   ├── dwolla.actions.ts          # Dwolla transfer creation
│   │   ├── transaction.actions.ts     # Transaction CRUD
│   │   ├── recipient.actions.ts       # Saved recipient management
│   │   ├── user.actions.ts            # User profile updates
│   │   ├── user.update-profile.ts     # Profile update sub-action
│   │   ├── wallet.actions.ts          # Wallet management
│   │   ├── admin.actions.ts           # Admin operations
│   │   └── admin-stats.actions.ts     # Admin statistics
│   │
│   ├── components/                    # React components
│   │   ├── ui/                        # shadcn/ui primitives (40+)
│   │   │   ├── button.tsx
│   │   │   ├── card.tsx
│   │   │   ├── dialog.tsx
│   │   │   ├── input.tsx
│   │   │   ├── table.tsx
│   │   │   ├── tabs.tsx
│   │   │   ├── form.tsx
│   │   │   ├── select.tsx
│   │   │   ├── sheet.tsx
│   │   │   ├── sidebar.tsx
│   │   │   ├── chart.tsx
│   │   │   ├── calendar.tsx
│   │   │   ├── drawer.tsx
│   │   │   ├── popover.tsx
│   │   │   └── ... (40+ total)
│   │   ├── layouts/                   # Layout & page wrapper components
│   │   │   ├── RootLayoutWrapper.tsx
│   │   │   ├── AuthLayoutWrapper.tsx
│   │   │   ├── AdminLayoutWrapper.tsx
│   │   │   ├── PageShell.tsx
│   │   │   ├── plaid-provider.tsx
│   │   │   ├── page-container/
│   │   │   ├── section-header/
│   │   │   ├── stat-card/
│   │   │   ├── total-balance/
│   │   │   ├── data-table/
│   │   │   ├── form/
│   │   │   ├── card/
│   │   │   ├── row/
│   │   │   ├── generic-* (card, data-table, empty-state,
│   │   │   │              form, modal, page-shell, skeleton, toast)
│   │   │   ├── dashboard-client/
│   │   │   ├── my-wallets-client/
│   │   │   ├── payment-transfer-client/
│   │   │   ├── settings-client/
│   │   │   ├── transaction-history-client/
│   │   │   ├── admin-dashboard/
│   │   │   ├── admin-data/
│   │   │   └── wallet-card/
│   │   ├── dashboard/                 # Dashboard components
│   │   │   ├── dashboard-server-wrapper.tsx
│   │   │   └── dashboard-client-wrapper.tsx
│   │   ├── home/                      # Home/landing page components
│   │   ├── sign-in/                   # Sign-in page wrapper
│   │   ├── sign-up/                   # Sign-up page wrapper
│   │   ├── auth-form/                 # Auth form component
│   │   ├── my-wallets/                # Wallet listing components
│   │   │   ├── my-wallets-server-wrapper.tsx
│   │   │   └── my-wallets-client-wrapper.tsx
│   │   ├── payment-transfer/          # Transfer form components
│   │   │   ├── payment-transfer-server-wrapper.tsx
│   │   │   └── payment-transfer-client-wrapper.tsx
│   │   ├── transaction-history/       # Transaction list components
│   │   │   ├── transaction-history-server-wrapper.tsx
│   │   │   └── transaction-history-client-wrapper.tsx
│   │   ├── settings/                  # Settings page components
│   │   │   ├── settings-server-wrapper.tsx
│   │   │   └── settings-client-wrapper.tsx
│   │   ├── admin/                     # Admin panel components
│   │   │   ├── admin-dashboard-content.tsx
│   │   │   └── admin-dashboard-server-wrapper.tsx
│   │   ├── sidebar/                   # Navigation sidebar
│   │   ├── mobile-nav/                # Mobile navigation
│   │   ├── nav-documents/             # Document navigation links
│   │   ├── nav-secondary/             # Secondary navigation
│   │   ├── plaid-context/             # Plaid Link context provider
│   │   ├── plaid-link-button/         # Plaid Link trigger button
│   │   ├── total-balance-box/         # Total balance display
│   │   ├── animated-counter/          # Animated number counter
│   │   ├── doughnut-chart/            # Doughnut chart widget
│   │   ├── chart-area-interactive/    # Interactive area chart
│   │   ├── section-cards/             # Key metric cards
│   │   ├── header-box/                # Page header component
│   │   ├── footer/                    # Page footer
│   │   ├── global-error/              # Global error UI
│   │   ├── not-found/                 # 404 UI wrapper
│   │   ├── shared/                    # Shared cross-feature components
│   │   └── shadcn-studio/             # Shadcn Studio prebuilt blocks
│   │       └── blocks/
│   │           ├── application-shell-01/
│   │           ├── dashboard-shell-01/
│   │           ├── account-settings-01/
│   │           ├── hero-section-41/
│   │           ├── onboarding-feed-01/
│   │           ├── chart-sales-metrics.tsx
│   │           ├── datatable-transaction.tsx
│   │           ├── statistics-card-01.tsx
│   │           ├── widget-product-insights.tsx
│   │           └── widget-total-earning.tsx
│   │
│   ├── lib/                           # Utilities & service integrations
│   │   ├── plaid.ts                   # Plaid client (Configuration + PlaidApi)
│   │   ├── dwolla.ts                  # Dwolla client (dwolla-v2 Client)
│   │   ├── auth.ts                    # Auth utilities
│   │   ├── auth-options.ts            # NextAuth config options
│   │   ├── session.ts                 # Session helpers
│   │   ├── encryption.ts              # AES-256-GCM encryption utilities
│   │   ├── email.ts                   # Email sending (Nodemailer)
│   │   ├── env.ts                     # Environment variable validation
│   │   ├── logger.ts                  # Application logger
│   │   ├── error-tracking.ts          # Error tracking utilities
│   │   ├── utils.ts                   # General utilities (cn, formatCurrency, etc.)
│   │   ├── validation-utils.ts        # Shared validation helpers
│   │   ├── schemas/                   # Zod schemas
│   │   │   ├── auth.schema.ts
│   │   │   ├── profile.schema.ts
│   │   │   ├── transfer.schema.ts
│   │   │   └── index.ts
│   │   ├── validations/               # Validation functions
│   │   │   ├── auth.ts
│   │   │   ├── transfer.ts
│   │   │   ├── admin.ts
│   │   │   └── index.ts
│   │   └── playwright/                # Playwright test utilities
│   │       └── set-cookie.helper.ts
│   │
│   ├── database/                      # Database schema & connection
│   │   ├── schema.ts                  # Full Drizzle schema (13 tables)
│   │   ├── db.ts                      # Database connection (pg driver)
│   │   ├── index.ts                   # Database re-exports
│   │   └── drizzle/                   # Generated migrations
│   │       ├── 0000_supreme_legion.sql
│   │       └── meta/
│   │           ├── _journal.json
│   │           └── 0000_snapshot.json
│   │
│   ├── dal/                           # Data Access Layer
│   │   ├── index.ts                   # DAL re-exports
│   │   ├── user.dal.ts                # User queries
│   │   ├── wallet.dal.ts              # Wallet queries
│   │   ├── transaction.dal.ts         # Transaction queries
│   │   ├── recipient.dal.ts           # Recipient queries
│   │   ├── dwolla.dal.ts              # Dwolla transfer queries
│   │   ├── admin.dal.ts               # Admin queries
│   │   ├── errors.dal.ts              # Error logging queries
│   │   └── health.ts                  # Health check queries
│   │
│   ├── hooks/                         # Custom React hooks
│   │   ├── use-bank-connection.ts     # Bank connection state
│   │   ├── use-debounce.ts            # Debounced value hook
│   │   ├── use-mobile.tsx             # Mobile detection hook
│   │   ├── use-pagination.ts          # Pagination hook
│   │   ├── use-transaction-filter.ts  # Transaction filter state
│   │   └── use-wallet-balance.ts      # Wallet balance query
│   │
│   ├── stores/                        # Zustand state stores
│   │   ├── index.ts                   # Store re-exports
│   │   ├── ui-store.tsx               # UI state (sidebar, theme)
│   │   ├── filter-store.tsx           # Transaction filter state
│   │   ├── toast-store.tsx            # Toast notification queue
│   │   ├── transfer-store.tsx         # Transfer form state
│   │   ├── session.tsx                # Session React context
│   │   ├── providers.tsx              # Context providers wrapper
│   │   ├── create-filter-store.ts     # Filter store factory
│   │   ├── create-toast-store.ts      # Toast store factory
│   │   ├── create-transfer-store.ts   # Transfer store factory
│   │   └── create-ui-store.ts         # UI store factory
│   │
│   ├── types/                         # TypeScript type definitions
│   │   ├── index.d.ts                 # Global type augmentations
│   │   ├── user.ts                    # User types
│   │   ├── wallet.ts                  # Wallet types
│   │   ├── transaction.ts             # Transaction types
│   │   ├── plaid.ts                   # Plaid response types
│   │   ├── dwolla.ts                  # Dwolla response types
│   │   ├── recipient.ts               # Recipient types
│   │   ├── next-auth.d.ts             # NextAuth type augmentation
│   │   └── *.d.ts                     # ESLint plugin declarations
│   │
│   ├── constants/                     # Application constants
│   │   └── index.ts
│   │
│   ├── assets/                        # Static assets (SVG components)
│   │   └── svg/
│   │       ├── logo.tsx
│   │       ├── bistro-logo.tsx
│   │       └── auth-background-shape.tsx
│   │
│   └── tests/                         # Test suites
│       ├── setup.ts                   # Test setup
│       ├── e2e/                       # Playwright E2E tests
│       │   ├── global-setup.ts
│       │   ├── global-teardown.ts
│       │   ├── auth.spec.ts           # Auth flow tests
│       │   ├── dashboard.spec.ts      # Dashboard tests
│       │   ├── my-wallets.spec.ts     # Wallet tests
│       │   ├── payment-transfer.spec.ts
│       │   ├── transaction-history.spec.ts
│       │   ├── settings.spec.ts
│       │   ├── admin.spec.ts
│       │   ├── wallet-linking.spec.ts
│       │   ├── transfer-idempotency.spec.ts
│       │   ├── soft-delete.spec.ts
│       │   ├── mock-tokens.spec.ts
│       │   ├── helpers/               # E2E test helpers
│       │   │   ├── auth.ts
│       │   │   ├── db.ts
│       │   │   ├── dwolla.ts
│       │   │   ├── plaid.ts
│       │   │   └── plaid.mock.ts
│       │   ├── utils/
│       │   │   └── auth-fixtures.ts
│       │   ├── integration/           # Integration E2E specs
│       │   │   └── link-and-transfer.spec.ts
│       │   └── specs/                 # Additional specs
│       │       └── plaid-script.spec.ts
│       ├── integration/               # Integration tests
│       ├── unit/                      # Unit tests
│       ├── utils/                     # Test utilities
│       ├── fixtures/                  # Test fixtures
│       │   ├── auth.ts
│       │   ├── combined.ts
│       │   └── console-handler.ts
│       ├── mocks/                     # Test mocks
│       └── verify-rules/              # Rule verification tests

├── database/                          # Root-level database artifacts
│   └── drizzle/                       # Drizzle migration outputs
│       ├── 0000_overconfident_jack_murdock.sql
│       └── meta/
│           ├── _journal.json
│           └── 0000_snapshot.json

├── public/                            # Static public assets
│   ├── icons/                         # SVG icons
│   │   ├── logo.svg
│   │   ├── home.svg
│   │   ├── connect-bank.svg
│   │   ├── transaction.svg
│   │   ├── money-send.svg
│   │   ├── shopping-bag.svg
│   │   ├── coins.svg
│   │   ├── dollar-circle.svg
│   │   ├── arrow-left.svg
│   │   ├── logout.svg
│   │   ├── hamburger.svg
│   │   ├── monitor.svg
│   │   ├── auth-image.svg
│   │   ├── gradient-mesh.svg
│   │   └── a-coffee.svg
│   ├── robots.txt
│   ├── sitemap.xml
│   └── sitemap-0.xml

├── scripts/                           # Utility & automation scripts
│   ├── README.md
│   ├── seed/                          # Database seeding
│   │   ├── run.ts                     # Seed runner
│   │   ├── seed-data.ts               # Seed data definitions
│   │   ├── seed-config.ts             # Seed configuration
│   │   ├── seed-ids.ts                # Seed ID constants
│   │   ├── create-plaid-tokens.ts     # Plaid token creation
│   │   └── get-planned-seed-summary.ts
│   ├── ts/                            # TypeScript utilities
│   │   ├── run-ci-checks.ts
│   │   ├── run-verify-and-validate.ts
│   │   ├── mcp-runner.ts
│   │   ├── opencode-mcp.ts
│   │   ├── plugin-repair.ts
│   │   ├── plugin-verify.ts
│   │   ├── read-secrets.ts
│   │   ├── build.ts
│   │   ├── branch-compare.ts
│   │   ├── diagnose-and-fix-git.ts
│   │   ├── aggressive-capture.ts
│   │   ├── cleanup/                   # Cleanup utilities
│   │   ├── deploy/                    # Deployment scripts
│   │   ├── docker/                    # Docker utilities
│   │   ├── docs/                      # Documentation generation
│   │   └── entrypoints/               # CLI entry points
│   ├── generate/                      # Code generators
│   │   ├── component.ts               # Component generator
│   │   ├── action.ts                  # Server action generator
│   │   ├── dal.ts                     # DAL generator
│   │   ├── feature.ts                 # Feature generator
│   │   └── docs-gen.ts                # Documentation generator
│   ├── db/                            # Database scripts
│   │   ├── apply-migrations.ts
│   │   └── apply-select-migrations.ts
│   ├── codemod/                       # Code transformation scripts
│   │   ├── find-process-env.ts
│   │   └── run-codemod.ts
│   ├── maintenance/                   # Maintenance utilities
│   │   ├── analyze-lint-scan.ts
│   │   └── lint-fix-runner.ts
│   ├── provenance/                    # Provenance tracking
│   │   └── generate-provenance.ts
│   ├── transform/                     # Data transformation
│   │   └── zod-meta-to-describe.ts
│   ├── validate.ts                    # Validation runner
│   ├── export-data.ts                 # Data export
│   ├── export-json.ts                 # JSON export
│   ├── generate-readme.ts             # README generation
│   ├── mcp-runner-lib.ts              # MCP runner library
│   ├── orchestartor.ts                # Orchestrator entry point
│   ├── plan-ensure.ts                 # Plan validation
│   ├── report-parser.ts               # CI report parsing
│   ├── verify-rules.ts                # Rules verification
│   ├── verify-agent-iterations.ts     # Agent iteration tracker
│   └── *.bat / *.ps1 / *.sh           # Cross-platform wrappers

├── bin/                               # CLI entry points
│   ├── cleanup/                       # Cleanup scripts
│   ├── deploy/                        # Deployment scripts (+ compose/traefik)
│   ├── docker/                        # Docker quickstart + env generation
│   ├── server/                        # Server setup scripts (cert gen, VPS)
│   └── utils/                         # Utility scripts + CI helpers

├── compose/                           # Docker Compose environments
│   ├── dev/                           # Development compose
│   │   └── node/
│   │       └── Dockerfile             # Node dev container
│   └── prod/                          # Production compose
│       ├── grafana/                   # Grafana monitoring
│       │   └── provisioning/
│       │       ├── dashboards/
│       │       └── datasources/
│       ├── prometheus/                # Prometheus monitoring
│       │   ├── prometheus.yml
│       │   └── rules/
│       │       └── app-alerts.yml
│       └── traefik/                   # Traefik reverse proxy
│           ├── traefik.yml
│           ├── auth/
│           │   └── htpasswd
│           └── dynamic/
│               ├── middlewares.yml
│               └── tls.yml

├── docs/                              # Documentation
│   ├── Project_Architecture/          # Architecture blueprints
│   │   ├── Project_Architecture_Blueprint.md
│   │   ├── Technology_Stack_Blueprint.md
│   │   ├── Project_Folder_Structure.md
│   │   ├── Workflow_Analysis.md
│   │   └── exemplars.md
│   ├── api-payments.md
│   ├── app-pages.md
│   ├── db-schema-audit.md
│   ├── deployment.md
│   ├── PlaidIntegrationGuide.md
│   ├── DwollaIntegrationGuide.md
│   ├── DrizzleORMGuide.md
│   ├── ESLintPluginsGuide.md
│   ├── secrets-management.md
│   ├── security.md
│   ├── scripts.md
│   ├── shadcn.md
│   └── ... (50+ additional docs)

├── templates/                         # Project templates
└── node_modules/                      # Dependencies (gitignored)
```

---

## Component Architecture

### Server/Client Component Split

```
Feature Page (Server Component)
├── Server Wrapper (fetches data via DAL)
│   ├── Client Wrapper (interactive UI)
│   │   ├── Data Table (client: sort, filter, paginate)
│   │   ├── Forms (client: validation, submit)
│   │   ├── Charts (client: recharts)
│   │   └── Plaid Link (client: OAuth flow)
│   └── Stat Cards (server: rendered data)
```

### Component Category Summary

| Category | Count | Examples |
| --- | --- | --- |
| **shadcn/ui primitives** | 40+ | button, card, dialog, input, table, tabs, select, form, chart, sidebar, sheet, calendar, drawer, popover, etc. |
| **Layout wrappers** | 30+ | RootLayoutWrapper, AuthLayoutWrapper, PageShell, data-table, form, card, generic-* (8 templates) |
| **Feature components** | 18 | dashboard-server-wrapper, payment-transfer-client-wrapper, my-wallets-server-wrapper, etc. |
| **Navigation** | 4 | sidebar, mobile-nav, nav-documents, nav-secondary |
| **Plaid integration** | 2 | plaid-context, plaid-link-button |
| **Charts & widgets** | 5 | doughnut-chart, chart-area-interactive, animated-counter, section-cards, total-balance-box |
| **Shared/generic** | 10+ | header-box, footer, global-error, not-found, shared/wallets-overview, etc. |
| **Shadcn Studio blocks** | 7+ | application-shell, dashboard-shell, account-settings, hero-section, onboarding-feed, etc. |

---

## Server Actions (10 total)

| Action File | Exports | Purpose |
| --- | --- | --- |
| `auth.register.ts` | `registerUser` | Create user account |
| `auth.signin.ts` | `signInWithCredentials` | Authenticate user |
| `plaid.actions.ts` | `createLinkToken`, `exchangePublicToken` | Plaid Link flow |
| `dwolla.actions.ts` | `createDwollaCustomer`, `createTransfer` | Dwolla operations |
| `transaction.actions.ts` | `createTransaction`, `getTransactions` | Transaction CRUD |
| `recipient.actions.ts` | `addRecipient`, `getRecipients` | Recipient management |
| `user.actions.ts` | `updateUser`, `getUser` | User operations |
| `user.update-profile.ts` | `updateProfile` | Profile update |
| `wallet.actions.ts` | `linkWallet`, `unlinkWallet` | Wallet operations |
| `admin.actions.ts` | `getAdminStats`, `manageUsers` | Admin operations |
| `admin-stats.actions.ts` | `getAdminDashboardStats` | Admin statistics |

---

## Data Access Layer (8 DAL modules)

| DAL Module | Primary Tables | Key Operations |
| --- | --- | --- |
| `user.dal.ts` | users, user_profiles | CRUD, soft delete, email lookup |
| `wallet.dal.ts` | wallets | CRUD, soft delete, by user, by sharableId |
| `transaction.dal.ts` | transactions | CRUD, by user, by wallet, filter, paginate |
| `recipient.dal.ts` | recipients | CRUD, by user, by email |
| `dwolla.dal.ts` | dwolla_transfers | CRUD, by idempotency key |
| `admin.dal.ts` | users, transactions, wallets | Aggregation queries |
| `errors.dal.ts` | errors | Insert, query by severity/date |
| `health.ts` | (pg connection) | Database connectivity check |

---

## Zustand Stores (4 active stores)

| Store | State | Actions |
| --- | --- | --- |
| `ui-store.tsx` | sidebarOpen, theme, isMobile | toggleSidebar, setTheme |
| `filter-store.tsx` | dateRange, status, category, type | setFilters, resetFilters |
| `toast-store.tsx` | toasts[] | addToast, removeToast, clearToasts |
| `transfer-store.tsx` | amount, recipientId, description | setAmount, setRecipient, reset |

---

## Custom React Hooks (6)

| Hook | Purpose |
| --- | --- |
| `use-bank-connection.ts` | Plaid link token lifecycle, connection status |
| `use-debounce.ts` | Debounce value for search inputs |
| `use-mobile.tsx` | Responsive breakpoint detection |
| `use-pagination.ts` | Client-side pagination logic |
| `use-transaction-filter.ts` | Transaction list filter orchestration |
| `use-wallet-balance.ts` | Real-time wallet balance queries |

---

*Generated by folder-structure-blueprint-generator — comprehensive analysis*
