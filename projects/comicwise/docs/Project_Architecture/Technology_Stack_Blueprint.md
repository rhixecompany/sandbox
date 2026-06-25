# Technology Stack Blueprint

## Project: comicwise — Comic Streaming

> **Generated:** 2026-06-25  
> **Generator:** technology-stack-blueprint-generator  
> **Analysis Depth:** Comprehensive

---

## Overview

A full-stack comic/manga streaming platform built with Next.js, featuring multi-tenant content delivery, subscription management, and a comprehensive reader experience.

**Project Type:** Full-Stack Web Application (Content Streaming)  
**Stack Type:** Next.js

---

## Technology Stack

### Languages & Runtimes

| Technology | Version | Usage |
|---|---|---|
| TypeScript | ^5.9.3 | Primary language (strict mode) |
| React | 19.2.4 | UI framework |
| Next.js | 16.1.6 | Full-stack framework (App Router) |
| Node.js | >=18 | JavaScript runtime |
| pnpm | 9.12.3 | Package manager |

### Package Manager

| Tool | Version |
|---|---|
| pnpm | 9.12.3 |

### Core Dependencies

| Category | Dependencies |
|---|---|
| **UI Framework** | next, react, react-dom |
| **UI Components** | @radix-ui/* (15+ packages), @base-ui/react, framer-motion ^12.36.0, embla-carousel-react, cmdk, vaul, sonner |
| **Styling** | tailwindcss ^4, @tailwindcss/postcss, tailwind-merge, tw-animate-css, class-variance-authority, clsx |
| **Icons** | lucide-react ^0.577.0, @tabler/icons-react |
| **State Management** | zustand ^5.0.11 |
| **Server State** | @tanstack/react-query ^5.90.21, @tanstack/react-query-devtools |
| **Forms & Validation** | react-hook-form ^7.71.2, @hookform/resolvers ^5.2.2, zod ^4.3.6 |
| **Data Display** | @tanstack/react-table ^8.21.3, recharts 3.8.0 |
| **Database** | drizzle-orm ^0.45.1, drizzle-kit ^0.31.9, postgres ^3.4.8, drizzle-zod |
| **Authentication** | next-auth 5.0.0-beta.30, @auth/core ^0.34.3, @auth/drizzle-adapter ^1.11.1, bcryptjs |
| **WebAuthn** | @simplewebauthn/server |
| **Payments** | Stripe (via stripe) |
| **Image/Media** | imagekit ^6.0.0, @imagekit/next, cloudinary ^2.9.0 |
| **Email** | nodemailer ^8.0.2, @react-email/components, react-email ^5.2.9 |
| **Async/Queue** | @upstash/qstash ^2.9.0, @upstash/workflow ^1.1.1, bullmq ^5.71.0 |
| **Caching** | @upstash/ratelimit ^2.0.8, @upstash/redis ^1.37.0, ioredis ^5.10.0 |
| **Monitoring** | @sentry/nextjs ^10.43.0 |
| **Utilities** | date-fns ^4.1.0, slugify ^1.6.8, chalk ^5.6.2, ora ^9.3.0, fs-extra, xxhash-wasm |

### Dev Dependencies

| Category | Dependencies |
|---|---|
| **Testing** | @playwright/test ^1.58.2, vitest ^4.1.0, @testing-library/react, happy-dom, jsdom |
| **Linting** | eslint ^9.0.0, eslint-config-next 16.1.6, typescript-eslint ^8.57.0, eslint-plugin-* (15+ plugins) |
| **Formatting** | prettier ^3.8.1, prettier-plugin-* (4 plugins) |
| **Database Tools** | drizzle-kit ^0.31.9 |
| **Utilities** | husky ^9.1.7, lint-staged ^16.3.3, tsx ^4.21.0, rimraf, cspell, npm-check-updates |
| **React Compiler** | babel-plugin-react-compiler 1.0.0 |

---

## Licensing

| Component | License |
|---|---|
| comicwise | Private (no license specified) |

---

## Database Schema

- **ORM**: Drizzle ORM (with drizzle-zod for validation)
- **Database**: PostgreSQL
- **Migrations**: via `drizzle-kit`
- **Seed system**: Comprehensive seeding for all entities

---

## Authentication & Authorization

- **Framework**: NextAuth v5 (beta)
- **Adapter**: @auth/drizzle-adapter
- **WebAuthn**: @simplewebauthn/server for passkeys
- **Password Strength**: @zxcvbn-ts/core

---

## External Integrations

| Service | Package | Purpose |
|---|---|---|
| Stripe | stripe | Payment processing |
| ImageKit | imagekit, @imagekit/next | Image optimization & delivery |
| Cloudinary | cloudinary | Media storage |
| Upstash Redis | @upstash/redis | Caching & rate limiting |
| Upstash QStash | @upstash/qstash | Job scheduling |
| Sentry | @sentry/nextjs | Error monitoring |
| Resend | (via nodemailer) | Email delivery |

---

## Key Scripts

| Script | Description |
|---|---|
| `dev` | Development server |
| `build` | Production build |
| `lint` / `lint:strict` | ESLint with zero-warnings |
| `type-check` | TypeScript type checking |
| `test` / `test:ui` | Vitest unit tests + Playwright E2E |
| `db:*` | Database operations (generate, push, migrate, studio, seed) |
| `health:*` | Health check scripts (db, redis, all) |
| `seed:*` | Entity-specific seeding (25+ seed commands) |
| `validate` | Full validation suite |
| `optimize:*` | Performance & code quality optimization |

---

## Coding Conventions

- **TypeScript strict**: Full type safety
- **App Router**: Server Components by default
- **PascalCase components**: React components
- **camelCase hooks/utils**: Custom hooks
- **Zod validation**: Schema validation everywhere
- **shadcn/ui components**: Radix composable primitives
- **NextAuth v5**: Modern auth patterns with edge support

---

## Architecture Diagram

```
┌──────────────────────────────────────────────────────────┐
│              comicwise (Next.js 16 + pnpm)                │
├──────────────────────────────────────────────────────────┤
│  App Router Pages                                        │
│  ├── /                    Home / browse                    │
│  ├── /comics/[id]        Comic detail & reader            │
│  ├── /subscriptions      Subscription management          │
│  ├── /auth               Authentication                    │
│  └── /admin              Admin dashboard                   │
├──────────────────────────────────────────────────────────┤
│  Core Services                                            │
│  ├── Database: Drizzle ORM → PostgreSQL                   │
│  ├── Cache: Upstash Redis / ioredis                      │
│  ├── Queue: BullMQ / Upstash QStash                      │
│  └── Media: ImageKit + Cloudinary                        │
├──────────────────────────────────────────────────────────┤
│  External Services                                        │
│  ├── Stripe (subscriptions)                               │
│  ├── Sentry (monitoring)                                 │
│  └── Resend (email)                                      │
└──────────────────────────────────────────────────────────┘
```

---

## Deployment

| Platform | Notes |
|---|---|
| Vercel | Primary deployment target |
| Docker | Docker support available |
| Upstash | Serverless Redis + QStash |
