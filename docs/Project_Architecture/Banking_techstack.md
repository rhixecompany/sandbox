# Banking — Technology Stack Blueprint

> **Generated:** 2026-07-24
> **Generator:** technology-stack-blueprint-generator
> **Project:** Banking (Next.js 16 Fintech App)
> **Analysis Depth:** Comprehensive

---

## Overview

A full-stack fintech application built with Next.js 16, featuring bank account integration via Plaid and Dwolla, real-time transaction management, and comprehensive authentication.

**Project Type:** Full-Stack Web Application (Fintech)  
**Stack Type:** Next.js 16 + Drizzle ORM + PostgreSQL

---

## Technology Stack

### Languages & Runtimes

| Technology | Version | Usage |
| --- | --- | --- |
| **TypeScript** | ^6.0.3 | Primary language (strict mode, full type safety) |
| **React** | ^19.2.5 | UI framework (Server Components + Client Components) |
| **Next.js** | 16.2.4 | Full-stack framework (App Router, Server Actions, Route Handlers) |
| **Node.js** | >=18 | JavaScript runtime |
| **Bun** | 1.3.14 | Package manager, script runner, JS runtime |

### Package Manager

| Tool | Version | Lockfile |
|---|---|---|
| **Bun** | 1.3.14 | `bun.lock` (binary lockfile) |

---

## Frontend Stack

### Core UI Framework

| Library | Version | Purpose |
| --- | --- | --- |
| `next` | 16.2.4 | App Router, Server Components, Server Actions |
| `react` | ^19.2.5 | UI library (Server + Client Components) |
| `react-dom` | ^19.2.5 | React DOM rendering |

### UI Component Libraries

| Library | Version | Components |
| --- | --- | --- |
| **@radix-ui/react-*** | ^1.x | 15+ primitive packages (accordion, dialog, dropdown, select, tabs, tooltip, popover, sheet, etc.) |
| **@base-ui/react** | ^1.4.1 | Base UI primitives |
| **radix-ui** | ^1.4.3 | Meta-package for Radix primitives |
| **cmdk** | ^1.1.1 | Command menu (⌘K-style) |
| **vaul** | ^1.1.2 | Drawer component |
| **sonner** | ^2.0.7 | Toast notifications |
| **embla-carousel-react** | ^8.6.0 | Carousel/slider |
| **@dnd-kit/** | ^6.x | Drag & drop (core, modifiers, sortable, utilities) |
| **react-resizable-panels** | ^4.11.0 | Resizable panel layouts |

### Styling

| Library | Version | Purpose |
| --- | --- | --- |
| **tailwindcss** | ^4.2.4 | Utility-first CSS framework |
| **@tailwindcss/postcss** | ^4.2.4 | Tailwind PostCSS plugin |
| **tailwind-merge** | ^3.5.0 | Smart class merging |
| **tailwindcss-animate** | ^1.0.7 | Animation utilities |
| **tw-animate-css** | ^1.4.0 | Tailwind CSS animations |
| **class-variance-authority** | ^0.7.1 | Component variant API |
| **clsx** | ^2.1.1 | Conditional class joining |
| **postcss** | ^8.5.13 | CSS transformations |
| **postcss-import** | ^16.1.1 | CSS @import resolution |
| **postcss-nested** | ^7.0.2 | CSS nesting |
| **postcss-preset-env** | ^11.2.1 | Modern CSS features |
| **tailwind-scrollbar** | ^4.0.2 | Scrollbar styling |

### Icons

| Library | Version | Purpose |
|---|---|---|
| **lucide-react** | ^1.14.0 | Primary icon set |

### Charts & Data Visualization

| Library | Version | Purpose |
| --- | --- | --- |
| **recharts** | 3.8.1 | React charting library (line, bar, area, pie) |
| **chart.js** | ^4.5.1 | General-purpose charting |
| **react-chartjs-2** | ^5.3.1 | React wrapper for Chart.js |
| **react-countup** | ^6.5.3 | Animated number counters |

### Data Display

| Library | Version | Purpose |
| --- | --- | --- |
| **@tanstack/react-table** | ^8.21.3 | Headless table with sorting, filtering, pagination |
| **react-day-picker** | ^9.14.0 | Date picker component |
| **input-otp** | ^1.4.2 | OTP input component |

---

## State Management

| Library | Version | Purpose |
|---|---|---|
| **zustand** | ^5.0.12 | Global state (UI, filters, toasts, transfers) |

### State Store Breakdown

| Store | Scope | Type |
| --- | --- | --- |
| UI Store | sidebar, theme, mobile nav | Zustand |
| Filter Store | transaction search/filter state | Zustand |
| Toast Store | notification queue | Zustand |
| Transfer Store | transfer form state | Zustand |
| Session | auth session context | React Context |
| Plaid Context | Plaid Link OAuth flow | React Context |

---

## Form Handling & Validation

| Library | Version | Purpose |
| --- | --- | --- |
| **react-hook-form** | ^7.75.0 | Performant form state management |
| **@hookform/resolvers** | ^5.2.2 | Schema resolvers (zod) for react-hook-form |
| **zod** | ^4.4.3 | Schema validation (forms, API, env) |

### Validation Schemas

| Schema File | Purpose |
| --- | --- |
| `src/lib/schemas/auth.schema.ts` | Sign-in / sign-up validation |
| `src/lib/schemas/profile.schema.ts` | Profile update validation |
| `src/lib/schemas/transfer.schema.ts` | Transfer amount/recipient validation |
| `src/lib/validations/auth.ts` | Auth-specific validation logic |
| `src/lib/validations/transfer.ts` | Transfer-specific validation logic |
| `src/lib/validations/admin.ts` | Admin operation validation |

---

## Backend / Database Stack

### Database

| Technology | Version | Purpose |
| --- | --- | --- |
| **PostgreSQL** | Any 14+ | Primary relational database |
| **pg** | ^8.20.0 | PostgreSQL Node.js driver (for Drizzle) |
| **postgres** | ^3.4.9 | Alternative PostgreSQL driver |

### ORM & Migrations

| Library | Version | Purpose |
| --- | --- | --- |
| **drizzle-orm** | ^0.45.2 | Type-safe SQL ORM (query builder + relational) |
| **drizzle-kit** | ^0.31.10 | Migration generation, push, studio |
| **@auth/drizzle-adapter** | ^1.11.2 | NextAuth adapter for Drizzle ORM |

### Database Schema (13 tables)

| Table | Enums | Key Indexes |
| --- | --- | --- |
| `users` | user_role | email (unique), deleted_at |
| `account` | — | user_id, composite PK (provider, providerAccountId) |
| `session` | — | user_id |
| `verificationToken` | — | identifier, composite PK (identifier, token) |
| `authenticator` | — | user_id, credentialID (unique) |
| `user_profiles` | — | user_id (unique) |
| `plaid_items` | — | item_id |
| `wallets` | — | user_id, sharable_id (unique), customer_url, funding_source_url, deleted_at, (user_id, deleted_at) |
| `transactions` | transaction_status, transaction_type, transaction_channel | user_id, sender/receiver wallet, status, created_at, deleted_at, plaidTransactionId (unique), (user_id, status), (user_id, deleted_at) |
| `dwolla_transfers` | — | user_id, status, created_at, idempotencyKey (unique) |
| `recipients` | — | user_id, email |
| `errors` | — | created_at, user_id, severity |
| `audit_logs` | — | user_id, action, (resourceType, resourceId), created_at, result |

---

## Authentication & Authorization

| Library | Version | Purpose |
| --- | --- | --- |
| **next-auth** | ^4.24.14 | Authentication framework (JWT strategy) |
| **@auth/drizzle-adapter** | ^1.11.2 | Database adapter for NextAuth |
| **bcryptjs** | ^3.0.3 | Password hashing |
| **@zxcvbn-ts/core** | ^3.0.4 | Password strength estimation |
| **@zxcvbn-ts/language-common** | ^3.0.4 | Common password patterns |
| **@zxcvbn-ts/language-en** | ^3.0.2 | English language patterns |

### Auth Configuration

| Feature | Detail |
| --- | --- |
| **Strategy** | JWT (stateless, no DB session lookup) |
| **Providers** | Credentials (email + password), OAuth-ready |
| **Session** | HTTP-only cookies via JWT |
| **Password** | bcrypt with salt rounds |
| **Roles** | user, admin, moderator (user_role enum) |
| **Rate Limiting** | Upstash Redis + @upstash/ratelimit |

---

## Financial / Banking Integration

| Service | Library | Version | Purpose |
| --- | --- | --- | --- |
| **Plaid** | `plaid` | ^42.2.0 | Bank account linking, transaction sync, identity verification |
| **Plaid Link** | `react-plaid-link` | ^4.1.1 | Client-side Plaid Link OAuth widget |
| **Dwolla** | `dwolla-v2` | ^3.4.0 | ACH transfer processing, customer creation, funding sources |

### Integration Architecture

```
┌────────────────────────────────────────────────────────────┐
│                   Banking App                               │
├────────────────────────────────────────────────────────────┤
│                                                             │
│  ┌─────────────┐    ┌──────────────┐    ┌────────────────┐ │
│  │  Plaid Link  │    │  Plaid API   │    │  Dwolla API    │ │
│  │  (Client)    │───▶│  (Server)    │    │  (Server)      │ │
│  └─────────────┘    └──────┬───────┘    └───────┬────────┘ │
│                            │                    │          │
│                     ┌──────▼───────┐     ┌──────▼───────┐  │
│                     │  Encrypted   │     │  Idempotent  │  │
│                     │  Token Store │     │  Transfer    │  │
│                     │  (AES-256)   │     │  (UUID key)  │  │
│                     └──────────────┘     └──────────────┘  │
│                                                             │
│  External Webhooks:                                         │
│    Dwolla → POST /api/dwolla/webhook (transfer updates)     │
│    Plaid  → (via webhook, event-driven sync)                │
└────────────────────────────────────────────────────────────┘
```

### Plaid Configuration

| Setting | Value |
| --- | --- |
| Environment | `sandbox` (dev), `production` (prod) |
| Products | transactions, auth, identity |
| Country Codes | US |
| Language | en |

### Dwolla Configuration

| Setting | Value |
| --- | --- |
| Environment | `sandbox` (dev), `production` (prod) |
| API Base | `https://api-sandbox.dwolla.com` (sandbox) |
| Transfer Type | ACH (standard) |
| Idempotency | UUID-based key per transfer |

---

## Caching & Rate Limiting

| Service | Library | Version | Purpose |
| --- | --- | --- | --- |
| **Upstash Redis** | `@upstash/redis` | ^1.37.0 | Serverless Redis caching |
| **Upstash Rate Limit** | `@upstash/ratelimit` | ^2.0.8 | API rate limiting |
| **Upstash QStash** | `@upstash/qstash-cli` | — | Scheduled/async tasks |

---

## Email & Notifications

| Library | Version | Purpose |
|---|---|---|
| **nodemailer** | ^8.0.7 | Email sending (transfer confirmations, notifications) |

---

## Security

### Encryption

| Technology | Algorithm | Usage |
| --- | --- | --- |
| **AES-256-GCM** | Symmetric key | Plaid access tokens, SSNs, account numbers |
| **bcrypt** | Password hashing | User passwords (salt rounds: default) |
| **JWT** | Token-based auth | NextAuth session tokens |

### Security Libraries

| Library | Version | Purpose |
| --- | --- | --- |
| `bcryptjs` | ^3.0.3 | Password hashing |
| `@zxcvbn-ts/core` | ^3.0.4 | Password strength checking |
| `eslint-plugin-no-secrets` | ^2.3.3 | Secret detection in code |
| `eslint-plugin-security` | ^4.0.0 | Security best practices |

---

## Testing Stack

| Library | Version | Purpose |
| --- | --- | --- |
| **@playwright/test** | ^1.59.1 | E2E browser tests (Chromium) |
| **vitest** | ^4.1.5 | Unit & integration test runner |
| **@testing-library/react** | ^16.3.2 | React component testing |
| **@testing-library/jest-dom** | ^6.9.1 | DOM matchers |
| **@testing-library/dom** | ^10.4.1 | DOM testing utilities |
| **@vitest/browser-playwright** | ^4.1.5 | Vitest browser mode (Playwright) |
| **@vitest/coverage-v8** | ^4.1.5 | Code coverage |
| **msw** | ^2.14.2 | HTTP mocking (API routes) |
| **happy-dom** | ^20.9.0 | DOM environment for Vitest |

### Test Configuration

| Config File | Runner | Tests |
| --- | --- | --- |
| `playwright.config.ts` | Playwright | `src/tests/e2e/` (12+ spec files) |
| `vitest.config.ts` | Vitest | `src/tests/unit/`, `src/tests/integration/` |

---

## Code Quality & Linting

### ESLint Configuration

| Package | Version | Purpose |
| --- | --- | --- |
| **eslint** | ^10.3.0 | Linter (flat config: `eslint.config.mts`) |
| **eslint-config-next** | 16.2.4 | Next.js ESLint preset |
| **typescript-eslint** | ^8.59.1 | TypeScript linting |
| **eslint-plugin-react** | ^7.37.5 | React best practices |
| **eslint-plugin-react-hooks** | ^7.1.1 | React Hooks rules |
| **eslint-plugin-react-refresh** | ^0.5.2 | React Fast Refresh |
| **@eslint-react/eslint-plugin** | ^5.7.1 | React-specific rules |
| **eslint-plugin-jsx-a11y** | ^6.10.2 | Accessibility |
| **eslint-plugin-import-x** | ^4.16.2 | Import rules |
| **eslint-plugin-drizzle** | ^0.2.3 | Drizzle ORM rules |
| **eslint-plugin-playwright** | ^2.10.2 | Playwright test rules |
| **eslint-plugin-testing-library** | ^7.16.2 | Testing Library rules |
| **eslint-plugin-perfectionist** | ^5.9.0 | Code organization |
| **eslint-plugin-unicorn** | ^64.0.0 | Modern JS best practices |
| **eslint-plugin-sonarjs** | ^4.0.3 | Code quality rules |
| **eslint-plugin-security** | ^4.0.0 | Security rules |
| **eslint-plugin-no-secrets** | ^2.3.3 | Leaked secret detection |
| **eslint-plugin-regexp** | ^3.1.0 | Regex safety |
| **eslint-plugin-zod** | ^3.12.0 | Zod validation rules |
| **eslint-plugin-zod** | ^3.12.0 | Zod usage rules |
| **eslint-plugin-jest** | ^29.15.2 | Jest-compatible rules |
| **eslint-plugin-jsdoc** | ^62.9.0 | JSDoc enforcement |
| **@eslint/markdown** | ^8.0.1 | Markdown linting |
| **@eslint/js** | ^10.0.1 | ESLint JS rules |
| **@eslint/eslintrc** | ^3.3.5 | ESLint config compat |
| **eslint-config-prettier** | ^10.1.8 | Prettier integration |

### Formatting

| Tool | Version | Plugins |
| --- | --- | --- |
| **prettier** | ^3.8.3 | organize-imports, packagejson, sort-json, tailwindcss |
| **markdownlint-cli2** | ^0.22.1 | Markdown format checking |
| **cspell** | ^10.0.0 | Spell checking |

### Pre-commit

| Tool | Version | Purpose |
| --- | --- | --- |
| **husky** | ^9.1.7 | Git hooks |
| **lint-staged** | ^16.4.0 | Staged file linting |

---

## Build & CI/CD

### Build Tools

| Tool | Version | Purpose |
| --- | --- | --- |
| **TypeScript** | ^6.0.3 | Type checking (`tsc --noEmit`) |
| **tsx** | ^4.21.0 | TypeScript execution (scripts) |
| **ts-node** | ^10.9.2 | Alternative TS execution |
| **rimraf** | ^6.1.3 | Cross-platform rm -rf |
| **cross-env** | ^10.1.0 | Cross-platform env vars |
| **next-sitemap** | ^4.2.3 | Sitemap generation |

### CI Scripts

| Script | Purpose |
| --- | --- |
| `bun run ci:checks:run` | Run CI validation suite |
| `bun run ci:helpers:lint-fix` | Auto-fix lint issues |
| `bun run ci:helpers:seed-prep` | Prepare seed data |
| `bun run ci:helpers:targeted-test` | Run targeted tests |
| `bun run ci:helpers:report` | Parse CI reports |
| `bun run validate` | Full validation (type-check + build + lint + test) |
| `bun run verify:rules` | Run rule verification |

---

## Deployment

| Platform | Config | Details |
| --- | --- | --- |
| **Vercel** | `vercel.json`, `next.config.ts` | Primary deployment (serverless) |
| **Docker** | `docker-compose.yml`, `compose/` | Self-hosted with full monitoring stack |
| **Railway** | `Railway.toml` | Alternative cloud deployment |
| **Docker Compose** stacks | `compose/dev/`, `compose/prod/` | Development + production variants |

### Production Monitoring Stack

| Service | Purpose | Config Location |
| --- | --- | --- |
| **Traefik** | Reverse proxy + TLS | `compose/prod/traefik/` |
| **Grafana** | Dashboard visualization | `compose/prod/grafana/` |
| **Prometheus** | Metrics + alerting | `compose/prod/prometheus/` |
| **Alert Rules** | Application alerts | `compose/prod/prometheus/rules/app-alerts.yml` |

---

## Code Generators

| Generator | Command | Purpose |
| --- | --- | --- |
| **Component** | `bun run generate:component` | Scaffold new React components |
| **Action** | `bun run generate:action` | Scaffold new Server Actions |
| **DAL** | `bun run generate:dal` | Scaffold new DAL modules |
| **Feature** | `bun run generate:feature` | Scaffold complete feature module |

---

## Key Dependencies Summary

### Production Dependencies (52+)

| Category | Key Packages |
| --- | --- |
| **Framework** | `next@16.2.4`, `react@19.2.5`, `react-dom@19.2.5` |
| **UI Components** | `@radix-ui/*` (15+), `@base-ui/react`, `radix-ui`, `cmdk`, `vaul`, `sonner` |
| **Styling** | `tailwindcss@4.2.4`, `tailwind-merge`, `class-variance-authority`, `clsx` |
| **Database** | `drizzle-orm@0.45.2`, `pg@8.20.0`, `postgres@3.4.9` |
| **Auth** | `next-auth@4.24.14`, `@auth/drizzle-adapter`, `bcryptjs`, `@zxcvbn-ts/core` |
| **Fintech** | `plaid@42.2.0`, `dwolla-v2@3.4.0`, `react-plaid-link@4.1.1` |
| **Forms** | `react-hook-form@7.75.0`, `zod@4.4.3`, `@hookform/resolvers` |
| **Charts** | `recharts@3.8.1`, `chart.js@4.5.1`, `react-chartjs-2` |
| **State** | `zustand@5.0.12` |
| **Table** | `@tanstack/react-table@8.21.3` |
| **Caching** | `@upstash/redis@1.37.0`, `@upstash/ratelimit@2.0.8` |
| **Utilities** | `date-fns@4.1.0`, `lucide-react`, `sharp@0.34.5`, `nodemailer@8.0.7` |

### Dev Dependencies (50+)

| Category | Key Packages |
| --- | --- |
| **Testing** | `@playwright/test@1.59.1`, `vitest@4.1.5`, `msw@2.14.2`, `@testing-library/react` |
| **Linting** | `eslint@10.3.0`, `typescript-eslint@8.59.1`, `eslint-config-next`, 15+ plugins |
| **Formatting** | `prettier@3.8.3`, `markdownlint-cli2`, `cspell` |
| **DB Tools** | `drizzle-kit@0.31.10` |
| **Deploy** | `vercel@53.1.0` |
| **Scripting** | `tsx@4.21.0`, `ts-node@10.9.2`, `rimraf`, `cross-env` |

---

## Environment Variables

| Variable | Purpose |
| --- | --- |
| `DATABASE_URL` | PostgreSQL connection string |
| `NEXT_PUBLIC_APP_URL` | Application base URL |
| `NEXTAUTH_URL` | NextAuth callback URL |
| `NEXTAUTH_SECRET` | JWT encryption secret |
| `PLAID_CLIENT_ID` | Plaid API client ID |
| `PLAID_SECRET` | Plaid API secret |
| `PLAID_ENV` | Plaid environment (`sandbox` / `production`) |
| `PLAID_BASE_URL` | Plaid API base URL (optional override) |
| `DWOLLA_KEY` | Dwolla API key |
| `DWOLLA_SECRET` | Dwolla API secret |
| `DWOLLA_ENV` | Dwolla environment (`sandbox` / `production`) |
| `DWOLLA_BASE_URL` | Dwolla API base URL (optional override) |
| `UPSTASH_REDIS_URL` | Upstash Redis endpoint |
| `UPSTASH_REDIS_TOKEN` | Upstash Redis auth token |
| `ENCRYPTION_KEY` | AES-256-GCM encryption key |
| `SMTP_HOST` / `SMTP_PORT` / etc. | Email server configuration |

---

## Project Scripts (30+)

| Script | Purpose |
| --- | --- |
| `bun run dev` | Start development server |
| `bun run build` | Production build (with prebuild checks) |
| `bun run start` | Start production server |
| `bun run lint` / `lint:strict` | ESLint with optional zero-warnings |
| `bun run format` | Prettier formatting |
| `bun run type-check` | TypeScript type checking |
| `bun run test` | Run all tests (UI + browser) |
| `bun run test:ui` | Playwright E2E tests |
| `bun run test:browser` | Vitest browser tests |
| `bun run db:generate` | Generate Drizzle migrations |
| `bun run db:push` | Push schema to database |
| `bun run db:migrate` | Apply migrations |
| `bun run db:studio` | Open Drizzle Studio |
| `bun run db:seed` | Seed database from Plaid tokens |
| `bun run db:reset` | Drop, generate, and push schema |
| `bun run validate` | Full validation suite |
| `bun run type-gen` | Generate Next.js type definitions |
| `bun run clean` | Clean build artifacts |

---

## Coding Conventions

- **TypeScript strict**: Full `strict` mode enabled in `tsconfig.json`
- **App Router**: Server Components by default; `"use client"` only for interactivity
- **File naming**: PascalCase for React components, camelCase for hooks/utils, kebab-case for page files
- **Component pattern**: Server Wrapper → Client Wrapper split for feature pages
- **Validation**: Zod schemas for forms, API input, and environment variables
- **CSS**: Tailwind CSS utility classes with `cn()` utility for class merging
- **shadcn/ui**: Radix-based composable components in `src/components/ui/`
- **DAL pattern**: All database queries through `src/dal/` modules, not inline in components
- **Encryption at rest**: AES-256-GCM for all sensitive tokens and PII
- **Soft deletes**: All major entities support `deletedAt` timestamp

---

*Generated by technology-stack-blueprint-generator — comprehensive analysis*
