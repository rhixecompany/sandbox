# Comicwise — Comic Streaming Platform

> **Stack:** Next.js 16 + Prisma/Drizzle + Stripe | **Type:** Full-Stack Content Streaming | **Status:** Active

A full-stack comic/manga streaming platform built with Next.js 16, featuring multi-tenant content delivery, subscription management via Stripe, and a comprehensive reader experience.

---

## Technology Stack

| Category | Technology |
|---|---|
| **Framework** | Next.js 16.1.6 (App Router) |
| **Language** | TypeScript ^5.9.3 (strict) |
| **UI** | React 19, Radix UI, shadcn/ui, Tailwind CSS 4, Framer Motion |
| **State Management** | Zustand 5.x, TanStack Query 5.x |
| **Database** | PostgreSQL via Drizzle ORM (Prisma migration in progress) |
| **Authentication** | NextAuth v5 (beta), WebAuthn passkeys |
| **Payments** | Stripe (subscriptions) |
| **Media** | ImageKit, Cloudinary |
| **Email** | Resend, React Email |
| **Async/Queue** | BullMQ, Upstash QStash |
| **Caching** | Upstash Redis |
| **Monitoring** | Sentry |
| **Testing** | Vitest, Playwright |
| **Package Manager** | pnpm 9.12.3 |

## Architecture

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

## Project Structure

```
comicwise/
├── src/
│   ├── app/                 # Next.js App Router
│   │   ├── (auth)/          # Authentication routes
│   │   ├── (root)/          # Main application routes
│   │   │   ├── comics/      # Comic browsing & reading
│   │   │   ├── authors/     # Author profiles
│   │   │   ├── browse/      # Browse & search
│   │   │   ├── subscriptions/
│   │   │   └── settings/    # User settings
│   │   ├── admin/           # Admin dashboard
│   │   └── api/             # API routes
│   ├── components/          # React components
│   ├── actions/             # Server actions
│   ├── lib/                 # Utilities
│   └── styles/              # Global styles
├── tests/                   # Test files
├── public/                  # Static assets
└── docs/Project_Architecture/
```

## Getting Started

```bash
# Prerequisites: Node.js >=18, pnpm 9.12.3+, PostgreSQL

# Install dependencies
pnpm install

# Set up environment
cp .env.example .env.local
# Configure Stripe, database, and other service credentials

# Database setup
npx prisma generate
npx prisma db push

# Start development server
pnpm run dev

# Run quality checks
pnpm run lint:strict
pnpm run type-check

# Run tests
pnpm run test        # Vitest unit tests
pnpm run test:e2e    # Playwright E2E tests
```

## Key Features

- **Comic Browsing** — Browse by genre, author, popularity
- **Reader Interface** — Immersive comic/manga reading experience
- **Subscription Management** — Tiered access via Stripe
- **User Authentication** — NextAuth v5 with WebAuthn passkeys
- **Admin Dashboard** — Full CRUD for comics, chapters, authors, users
- **Bookmarks & Reading Progress** — Track reading across devices
- **Comments & Ratings** — Community engagement
- **Notifications** — Real-time updates via WebSocket

## Development Workflow

```bash
pnpm run dev           # Development server (Turbopack)
pnpm run build         # Production build
pnpm run lint:strict   # ESLint zero-warnings
pnpm run type-check    # TypeScript checking
pnpm run test          # Test suite
pnpm run test:ui       # Vitest UI mode
pnpm run db:*          # Database operations
pnpm run seed:*        # Entity-specific seeding
pnpm run validate      # Full validation suite
pnpm run optimize:*    # Performance optimization
```

## Coding Standards

- **TypeScript strict**: Full type safety
- **App Router**: Server Components by default
- **PascalCase components**: React components
- **camelCase hooks/utils**: Custom hooks and utilities
- **Zod validation**: Schema validation everywhere
- **shadcn/ui components**: Radix composable primitives
- **Server Actions**: `"use server"` for data mutations
- **Import order**: React/Next → third-party → `@/components/` → `@/lib/` → `@/types/`

## Deployment

| Platform | Notes |
|---|---|
| **Vercel** | Primary deployment target |
| **Docker** | Docker support available |
| **Upstash** | Serverless Redis + QStash |

## License

Private (no license specified)
