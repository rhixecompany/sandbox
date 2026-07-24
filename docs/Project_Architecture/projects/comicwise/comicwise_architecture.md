# Comicwise — Architecture Blueprint

## Overview

- **Project Name:** Comicwise (package: `comicbook`)
- **Project Type:** Full-stack digital comic/manga streaming platform
- **Architecture Pattern:** Next.js 16 App Router (full-stack RSC + RCC hybrid)
- **Package Manager:** pnpm 9.12.3 (monorepo-capable)
- **Target:** Vercel (primary), Docker (secondary)

## Architecture Diagram

```mermaid
C4Context
  title System Context — Comicwise

  Person(user, "Reader", "A user browsing, reading, and managing comics")
  Person(admin, "Admin", "An administrator managing content and users")

  System_Boundary(comicwise, "Comicwise Platform") {
    System(web, "Next.js App", "Renders UI, handles SSR/SSG/ISR")
    System(api, "API Routes & Server Actions", "Backend logic, auth, data ops")
    System(db, "PostgreSQL", "Primary data store (via Drizzle ORM)")
    System(cache, "Upstash Redis", "Session cache, rate limiting, queues")
    System(media, "ImageKit / Cloudinary", "Image optimization & CDN delivery")
  }

  System_Ext(stripe, "Stripe", "Subscription billing")
  System_Ext(sentry, "Sentry", "Error monitoring & tracing")
  System_Ext(email, "Resend / Nodemailer", "Transactional email")
  System_Ext(qstash, "Upstash QStash", "Async job scheduling")
  System_Ext(bullmq, "BullMQ + ioredis", "Background job processing")

  Rel(user, web, "HTTPS", "Browser")
  Rel(admin, web, "HTTPS", "Browser")
  Rel(api, db, "Drizzle ORM", "SQL")
  Rel(api, cache, "ioredis", "Redis protocol")
  Rel(api, media, "REST/SDK", "Image ops")
  Rel(api, stripe, "REST API", "Payments")
  Rel(api, sentry, "SDK", "Telemetry")
  Rel(api, email, "SMTP/API", "Emails")
  Rel(api, qstash, "REST", "Scheduling")
  Rel(api, bullmq, "ioredis", "Jobs")
```

```mermaid
C4Container
  title Container Diagram — Next.js App

  Container_Boundary(nextapp, "Next.js 16 Application") {
    Container(rsc, "Server Components (RSC)", "React Server Components — data fetching, rendering")
    Container(rcc, "Client Components (RCC)", "Interactive UI — 'use client' boundary")
    Container(actions, "Server Actions", "src/actions/ — mutation logic")
    Container(routes, "API Routes", "src/app/api/ — REST endpoints")
    Container(auth, "NextAuth v5", "Authentication & session management")
  }

  ContainerDb(pg, "PostgreSQL", "Drizzle ORM", "Comic, user, subscription data")
  ContainerDb(redis, "Upstash Redis", "ioredis", "Rate limiting, cache, queues")

  Rel(rsc, pg, "Drizzle queries", "Read")
  Rel(rcc, actions, "Server Action call", "Mutation")
  Rel(actions, pg, "Drizzle", "CRUD")
  Rel(actions, redis, "ioredis", "Cache set/inval")
  Rel(routes, pg, "Drizzle", "Read/Write")
```

## Architectural Patterns

### Rendering Strategy

| Strategy      | Pages                                                   |
|---------------|---------------------------------------------------------|
| **SSR**       | Auth pages, user profile, admin panel                   |
| **SSG + ISR** | Public comic listing, genre pages, author pages         |
| **CSR**       | Comic reader (client-heavy), search, interactive charts |

### Route Groups

| Group       | Layout          | Routes                                                     |
|-------------|-----------------|------------------------------------------------------------|
| `(auth)`    | Minimal         | `/sign-in`, `/sign-up`                                     |
| `(root)`    | Nav + Footer    | Home, browse, comics, authors, genres, profile, search, etc |
| `admin`     | Admin sidebar   | Users, comics, chapters, roles, permissions, audit-logs     |

### Data Access Layer

- **Server Actions** (`src/actions/`) — Primary mutation path; Drizzle queries inside exported async functions called from Client Components
- **API Routes** (`src/app/api/`) — Auth callback handlers and seed endpoints
- **Drizzle ORM** — Direct SQL query building via `drizzle-orm`; schema defined in `src/database/schema.ts`
- **TanStack React Query** — Client-side data fetching with query key factory (`src/lib/query-client.ts`)

### State Management

| Type            | Tool              | Usage                                    |
|-----------------|-------------------|------------------------------------------|
| **Server state** | TanStack Query    | Comics, chapters, users, bookmarks       |
| **Client state** | Zustand           | UI preferences, reader state, notifications |

### Subscription & Payment Flow

```mermaid
sequenceDiagram
  actor User
  participant Web as Next.js App
  participant Stripe
  participant DB as PostgreSQL
  participant Redis

  User->>Web: Select subscription plan
  Web->>Stripe: Create checkout session
  Stripe-->>User: Redirect to Stripe Checkout
  User->>Stripe: Complete payment
  Stripe->>Web: Webhook (checkout.session.completed)
  Web->>DB: Update user subscription
  Web->>Redis: Invalidate cache
  DB-->>Web: Subscription active
  Web-->>User: Access granted
```

## Key Architecture Decisions

1. **Dual ORM (Prisma legacy → Drizzle)** — Migration underway from Prisma to Drizzle for better type safety, smaller bundle, and direct SQL control
2. **pnpm workspaces** — Disk-efficient monorepo management with strict dependency isolation
3. **RSC-first (App Router)** — Server Components as default, Client Components only for interactivity
4. **NextAuth v5 beta** — Modern auth with edge runtime support, Drizzle adapter for DB-backed sessions
5. **ImageKit + Cloudinary dual CDN** — Redundant image optimization pipeline; ImageKit primary, Cloudinary fallback
6. **BullMQ + Upstash QStash** — Redis-backed background jobs via BullMQ for heavy tasks; QStash for lightweight serverless scheduling
7. **React Compiler (experimental)** — Automatic memoization via `babel-plugin-react-compiler`
8. **Full-text search** — PostgreSQL `tsvector` columns for in-DB comic/manga search

## Security

- **Headers**: HSTS, X-Frame-Options, X-Content-Type-Options, CSP, Permissions-Policy (configured in `next.config.ts`)
- **Auth**: NextAuth with credentials, OAuth (Google, GitHub), and WebAuthn/passkey support
- **Rate limiting**: Upstash Ratelimit (Redis-backed)
- **Input validation**: Zod schemas validated server-side and client-side
- **Password strength**: zxcvbn-ts
- **RBAC**: User roles (`user`, `admin`, `moderator`) with granular permission system

## Monitoring & Observability

- **Sentry**: Error tracking, performance traces, release health
- **Logging**: Next.js fetch logging (full URL), environment-aware log levels
- **Health checks**: `/api/health` — checks DB, Redis, system status (via `src/scripts/unified-project-health.ts`)

## Extensibility

- Add new Route Groups in `src/app/(group)/`
- New Server Actions in `src/actions/`
- New entities via Drizzle schema additions and `drizzle-kit generate`
- New subscription tiers via Stripe product configuration
- New UI components via `pnpm dlx shadcn@latest add <component>`
