# Comicwise — Technology Stack Blueprint

## Tech Stack Overview

```
┌─────────────────────────────────────────────────────────────────────┐
│                    COMICWISE — Tech Stack Map                       │
├─────────────────────────────────────────────────────────────────────┤
│                                                                     │
│  Presentation Layer                                                 │
│  ┌───────────────────────────────────────────────────────────────┐  │
│  │  React 19.2.4  │  Next.js 16.1.6  │  Tailwind CSS 4          │  │
│  │  Radix UI / shadcn  │  Framer Motion  │  Lucide Icons        │  │
│  └───────────────────────────────────────────────────────────────┘  │
│                              │                                      │
│  State & Data Layer                                                 │
│  ┌───────────────────────────────────────────────────────────────┐  │
│  │  TanStack React Query 5     │  Zustand 5     │  Zod 4        │  │
│  │  React Hook Form 7          │  react-hook-form/resolvers     │  │
│  └───────────────────────────────────────────────────────────────┘  │
│                              │                                      │
│  API & Auth Layer                                                    │
│  ┌───────────────────────────────────────────────────────────────┐  │
│  │  NextAuth v5 (beta)  │  @auth/drizzle-adapter                 │  │
│  │  Server Actions (src/actions/)  │  API Routes (app/api/)      │  │
│  │  @simplewebauthn/server  │  bcryptjs  │  @zxcvbn-ts          │  │
│  └───────────────────────────────────────────────────────────────┘  │
│                              │                                      │
│  Data & Storage Layer                                                │
│  ┌───────────────────────────────────────────────────────────────┐  │
│  │  PostgreSQL  │  Drizzle ORM 0.45  │  Drizzle Kit 0.31        │  │
│  │  Upstash Redis  │  ioredis 5  │  BullMQ 5                   │  │
│  │  ImageKit 6  │  Cloudinary 2  │  @imagekit/next             │  │
│  └───────────────────────────────────────────────────────────────┘  │
│                              │                                      │
│  External Services                                                   │
│  ┌───────────────────────────────────────────────────────────────┐  │
│  │  Stripe (subscriptions)  │  Sentry  │  Resend / Nodemailer   │  │
│  │  Upstash QStash  │  Vercel (deploy)  │  Docker               │  │
│  └───────────────────────────────────────────────────────────────┘  │
│                                                                     │
│  Quality & DX                                                       │
│  ┌───────────────────────────────────────────────────────────────┐  │
│  │  TypeScript 5.9  │  ESLint 9  │  Prettier 3.8               │  │
│  │  Vitest 4  │  Playwright 1.58  │  Husky 9  │  lint-staged   │  │
│  │  TSX 4  │  pnpm 9.12.3  │  React Compiler                   │  │
│  └───────────────────────────────────────────────────────────────┘  │
│                                                                     │
└─────────────────────────────────────────────────────────────────────┘
```

## Languages & Runtimes

| Technology   | Version     | Usage                                     |
|--------------|-------------|-------------------------------------------|
| TypeScript   | ^5.9.3      | Primary language (strict mode throughout) |
| React        | 19.2.4      | UI framework (RSC + RCC hybrid)           |
| Next.js      | 16.1.6      | Full-stack framework (App Router)         |
| Node.js      | >=18        | JavaScript runtime                        |
| pnpm         | 9.12.3      | Package manager (workspace monorepo)      |

## Frontend

### UI Framework & Styling

| Package                | Version    | Purpose                          |
|------------------------|------------|----------------------------------|
| next                   | 16.1.6     | Framework (App Router, SSR/SSG)  |
| react / react-dom      | 19.2.4     | UI rendering                     |
| tailwindcss            | 4.x        | Utility-first CSS                |
| @tailwindcss/postcss   | 4.x        | Tailwind PostCSS plugin          |
| tailwind-merge         | ^3.5.0     | Tailwind class merging           |
| tw-animate-css         | ^1.4.0     | Tailwind animation utilities     |
| class-variance-authority | ^0.7.1   | Component variant system         |
| clsx                   | ^2.1.1     | Conditional class building       |

### UI Component Libraries

| Package             | Version   | Purpose                          |
|---------------------|-----------|----------------------------------|
| @radix-ui/*         | 15+ pkgs  | Accessible UI primitives         |
| @base-ui/react      | ^1.3.0    | Base UI primitives               |
| shadcn/ui           | ^4.0.6    | CLI-managed component library    |
| framer-motion       | ^12.36.0  | Animation & transitions          |
| embla-carousel-react| ^8.6.0    | Carousel / slider                |
| cmdk                | ^1.1.1    | Command menu (search palette)    |
| vaul                | ^1.1.2    | Bottom sheet drawer              |
| sonner              | ^2.0.7    | Toast notifications              |
| react-resizable-panels | ^4     | Resizable panel layouts          |
| react-day-picker    | ^9.14.0   | Date picker                      |
| input-otp           | ^1.4.2    | One-time-password input          |

### Icons

| Package                | Version   | Purpose                      |
|------------------------|-----------|------------------------------|
| lucide-react           | ^0.577.0  | Primary icon set (8k+ icons) |
| @tabler/icons-react    | ^3.40.0   | Secondary icon set           |

### State Management

| Package                    | Version   | Purpose                          |
|----------------------------|-----------|----------------------------------|
| @tanstack/react-query      | ^5.90.21  | Server state (fetching, caching) |
| @tanstack/react-query-devtools | ^5.91.3 | DevTools for Query              |
| zustand                    | ^5.0.11   | Client state (reader, UI, etc.)  |
| @tanstack/react-table      | ^8.21.3   | Data tables (admin panels)       |
| recharts                   | 3.8.0     | Charts & analytics               |

### Forms & Validation

| Package                  | Version   | Purpose                        |
|--------------------------|-----------|--------------------------------|
| react-hook-form          | ^7.71.2   | Performant form management     |
| @hookform/resolvers     | ^5.2.2    | Zod/validation resolver        |
| zod                      | ^4.3.6    | Schema validation (universal)  |
| drizzle-zod              | ^0.8.3    | Drizzle schema → Zod inference |

## Backend / Database

### Database

| Technology    | Version       | Purpose                        |
|---------------|---------------|--------------------------------|
| PostgreSQL    | (cloud/vendor)| Primary relational database    |
| Drizzle ORM   | ^0.45.1       | Type-safe SQL query builder    |
| Drizzle Kit   | ^0.31.9       | Schema management, migrations  |
| postgres      | ^3.4.8        | PostgreSQL client driver       |

### Database Schema Structure (Drizzle ORM)

**Entities:** user, account, session, verificationToken, comic, chapter, chapterImage, author, artist, genre, bookmark, comment, rating, follow, notification, share, readingProgress, readingGoal, userPreference, role, permission, type, auditLog

**Features:** PostgreSQL enums (`user_role`, `comic_status`), tsvector full-text search, JSONB settings columns, composite indexes.

**Auth tables:** NextAuth-compatible account/session/verificationToken tables via `@auth/drizzle-adapter`.

### Caching & Queues

| Package              | Version   | Purpose                       |
|----------------------|-----------|-------------------------------|
| @upstash/redis       | ^1.37.0   | Serverless Redis (caching)    |
| @upstash/ratelimit   | ^2.0.8    | Rate limiting                 |
| ioredis              | ^5.10.0   | Redis client (BullMQ)         |
| bullmq               | ^5.71.0   | Background job queue          |
| @upstash/qstash      | ^2.9.0    | Serverless job scheduling     |
| @upstash/workflow    | ^1.1.1    | Workflow orchestration        |

## Authentication & Authorization

| Package                   | Version          | Purpose                    |
|---------------------------|------------------|----------------------------|
| next-auth                 | 5.0.0-beta.30    | Auth framework             |
| @auth/core                | ^0.34.3          | Auth core library          |
| @auth/drizzle-adapter     | ^1.11.1          | Drizzle DB adapter         |
| @simplewebauthn/server    | ^13.3.0          | WebAuthn / passkeys        |
| bcryptjs                  | ^3.0.3           | Password hashing           |
| @zxcvbn-ts/core           | ^3.0.4           | Password strength meter    |

**Providers:** Credentials (email+password), Google OAuth, GitHub OAuth, Keycloak OIDC.

**Roles:** `user` (default), `admin`, `moderator` — granular permission system via RBAC.

## Payments

| Package   | Version | Purpose                         |
|-----------|---------|---------------------------------|
| stripe    | (NPM)   | Payment processing (server-side)|

**Flow:** Stripe Checkout → subscription plans → Stripe webhook events → status update in DB.

## Media & Images

| Package              | Version   | Purpose                            |
|----------------------|-----------|------------------------------------|
| imagekit             | ^6.0.0    | ImageKit server SDK                |
| @imagekit/next       | ^2.1.5    | ImageKit Next.js integration       |
| cloudinary           | ^2.9.0    | Cloudinary SDK (fallback)          |
| sharp                | ^0.34.5   | Server-side image processing       |

## Email

| Package                  | Version   | Purpose                       |
|--------------------------|-----------|-------------------------------|
| nodemailer               | ^8.0.2    | SMTP email transport          |
| @react-email/components  | ^1.0.9    | React email component library |
| react-email              | ^5.2.9    | Email preview & build         |

## Monitoring & Observability

| Package            | Version   | Purpose                         |
|--------------------|-----------|---------------------------------|
| @sentry/nextjs     | ^10.43.0  | Error tracking & performance    |
| web-vitals         | ^5.1.0    | Web vitals monitoring           |

## Development & Quality

### Testing

| Package                | Version   | Purpose                       |
|------------------------|-----------|-------------------------------|
| vitest                 | ^4.1.0    | Unit test runner              |
| @testing-library/react | ^16.3.2   | React component testing       |
| @testing-library/dom   | ^10.4.1   | DOM testing utilities         |
| happy-dom              | ^20.8.4   | DOM environment (Vitest)      |
| jsdom                  | ^28.1.0   | DOM environment (alternative) |
| @playwright/test       | ^1.58.2   | E2E browser testing           |

### Linting & Formatting

| Package                      | Version   | Purpose                         |
|------------------------------|-----------|---------------------------------|
| eslint                       | ^9.0.0    | Linter (flat config)            |
| eslint-config-next           | 16.1.6    | Next.js lint rules              |
| typescript-eslint            | ^8.57.0   | TypeScript ESLint                |
| eslint-plugin-* (15+ pkgs)  | various   | Plugin rules (unicorn, sonarjs, security, drizzle, perfectionist, etc.) |
| prettier                     | ^3.8.1    | Code formatter                   |
| prettier-plugin-* (4 pkgs)  | various   | Import, package.json, sort-json, tailwind plugins |
| cspell                       | ^9.7.0    | Spell checker                   |

### Build & DX

| Package                    | Version   | Purpose                          |
|----------------------------|-----------|----------------------------------|
| tsx                        | ^4.21.0   | TypeScript execution (scripts)   |
| typescript                 | ^5.9.3    | TypeScript compiler               |
| husky                      | ^9.1.7    | Git hooks                        |
| lint-staged                | ^16.3.3   | Staged file linting              |
| rimraf                     | ^6.1.3    | Cross-platform rm -rf            |
| next-sitemap               | ^4.2.3    | Sitemap generation                |
| npm-check-updates         | ^19.6.3   | Dependency version checker        |
| dotenv / dotenv-safe       | latest    | Env file loading                  |
| jscodeshift                | ^17.3.0   | Code transformation (codemods)    |
| ts-morph                   | ^27.0.2   | TypeScript AST manipulation       |
| vite-tsconfig-paths        | ^6.1.1    | Path alias resolution             |
| babel-plugin-react-compiler| 1.0.0     | React compiler (auto-memoization) |
| glob / globby              | latest    | File globbing                     |
| commander                  | ^14.0.3   | CLI argument parsing (scripts)    |
| inquirer                   | ^13.3.0   | Interactive prompts (scripts)     |
| dts-gen                    | ^0.10.9   | TypeScript declaration generation |
| update-browserslist-db     | ^1.2.3    | Browser list DB updates           |
| ms                         | ^2.1.3    | Time duration parsing             |

## Infrastructure & Deployment

| Service         | Purpose                              |
|-----------------|--------------------------------------|
| Vercel          | Primary hosting (Next.js optimized)  |
| Docker          | Containerized deployment (Dockerfile)|
| Upstash Redis   | Serverless Redis caching             |
| Upstash QStash  | Scheduled job execution              |
| Neon / Supabase | PostgreSQL hosting (DB_URL pattern)  |
| GitHub Actions  | CI pipeline                          |
| ImageKit        | Image CDN & optimization             |
| Cloudinary      | Media storage (fallback)             |
| Sentry          | Error & performance monitoring       |
| Resend          | Transactional email delivery          |

## Environment Configuration

The project uses a **Zod-validated env schema** (`appConfig.ts`) covering:

| Category       | Variables (count)                |
|----------------|----------------------------------|
| Database       | DATABASE_URL, NEON_DATABASE_URL  |
| Auth           | AUTH_SECRET, GOOGLE/GITHUB/KEYCLOAK_* |
| Redis          | REDIS_*, UPSTASH_REDIS_*        |
| Image Services | IMAGEKIT_*, CLOUDINARY_*, AWS_* |
| Monitoring     | SENTRY_*, POSTHOG_*             |
| Payment        | STRIPE_*                        |
| Email          | RESEND_API_KEY, NODEMAILER_*    |
| Security       | JWT_*, RATE_LIMIT_*, ALLOWED_ORIGINS |
| Seeding        | SEED_* (API key, concurrency, batch size, timeouts) |
| Feature Flags  | ENABLE_SEEDING, ENABLE_ANALYTICS, ENABLE_ERROR_TRACKING |

## Scripts Overview

The package.json defines **130+ scripts** organized in tiers:

| Tier              | Example Scripts                                      |
|-------------------|------------------------------------------------------|
| Essential Workflow| `dev`, `build`, `lint`, `type-check`, `test`         |
| Database Ops      | `db:generate`, `db:push`, `db:migrate`, `db:studio`  |
| Seeding           | `seed:*` (25+ entity-specific seeders)               |
| Health Monitoring | `health:*` (db, redis, all — with JSON & verbose)    |
| Performance       | `optimize:*` (types, camelCase, kebab-case, perf)    |
| Code Quality      | `validate`, `lint:strict`, `imports:*`               |
| Code Generation   | `scaffold:*` (components, actions, hooks)             |
| Cleanup           | `clean`, `clean:all`, `cleanup:*`, `cache:clear`     |
| Git               | `git:commit`, `git:push`, `git:init`                  |
| Docker            | docker-compose.yml + Dockerfile                       |
