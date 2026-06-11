# ComicWise Project Documentation

## Overview

ComicWise is a full-featured comic book reading platform that allows users to discover, read, and engage with comic content. The platform supports multiple comic types (manga, manhwa, comics), provides a rich reading experience with customizable settings, and includes social features for community engagement.

**Repository:** https://github.com/Rhixe-company/comicwise  
**Stack:** Next.js 14+ (App Router) | TypeScript | PostgreSQL | Drizzle ORM | NextAuth v5 | tRPC | Tailwind CSS  
**Status:** Active Development

---

## Architecture

### Application Structure

```
┌─────────────────────────────────────────────────────────┐
│                    Next.js App Router                     │
│  ┌──────────────┐  ┌──────────────┐  ┌──────────────┐   │
│  │  (auth)       │  │  (root)      │  │  admin/       │   │
│  │  sign-in      │  │  comics/*    │  │  users/*      │   │
│  │  sign-up      │  │  browse      │  │  roles/*      │   │
│  └──────────────┘  │  search       │  │  permissions/*│   │
│                     │  profile/*    │  └──────────────┘   │
│                     │  bookmarks    │                     │
│                     │  analytics    │                     │
│                     │  settings     │                     │
│                     └──────────────┘                     │
├─────────────────────────────────────────────────────────┤
│              Server Actions (src/actions/)                │
│  Auth | Content | Search | Social | Admin                 │
├─────────────────────────────────────────────────────────┤
│            Data Access Layer (src/dal/)                   │
│  28 DAL files providing CRUD + complex queries            │
├─────────────────────────────────────────────────────────┤
│              Database (src/database/)                     │
│  Drizzle ORM | PostgreSQL | 30+ tables | Full-text search │
└─────────────────────────────────────────────────────────┘
```

### Key Architectural Decisions

1. **Server Components by Default** — All pages are React Server Components; `"use client"` only where interactivity is required (forms, reader, search input)
2. **Server Actions for Mutations** — All data mutations use Next.js Server Actions with Zod validation, replacing traditional API routes
3. **DAL Pattern** — All database access goes through dedicated DAL files, preventing N+1 queries and centralizing query logic
4. **Composite Primary Keys** — Junction tables (comicToGenre, bookmark, follow, rolePermission, userRole) use composite PKs for data integrity
5. **Soft Deletes** — User accounts and comments support soft delete with `deletedAt` timestamp
6. **Full-Text Search** — PostgreSQL tsvector with denormalized searchIndex table for efficient full-text search
7. **RBAC** — Role-based access control with granular permissions, system roles, and audit logging

---

## Setup Guide

### Prerequisites

- Node.js 18+
- PostgreSQL 14+ (local or Neon)
- Redis (optional, for rate limiting)
- ImageKit or Cloudinary account (image hosting)

### Environment Variables

Create `.env.local` with these variables:

```env
# Database
DATABASE_URL=postgresql://user:pass@localhost:5432/comicwise
NEON_DATABASE_URL=postgresql://user:pass@ep-xxx.us-east-2.aws.neon.tech/comicwise

# Auth
AUTH_SECRET=your-auth-secret
AUTH_URL=http://localhost:3000
GITHUB_ID=your-github-oauth-id
GITHUB_SECRET=your-github-oauth-secret
GOOGLE_CLIENT_ID=your-google-client-id
GOOGLE_CLIENT_SECRET=your-google-client-secret

# Email
GMAIL_APP_PASSWORD=your-gmail-app-password
GMAIL_EMAIL=your-email@gmail.com
RESEND_API_KEY=your-resend-api-key

# Image Hosting
IMAGEKIT_PUBLIC_KEY=your-imagekit-public-key
IMAGEKIT_PRIVATE_KEY=your-imagekit-private-key
IMAGEKIT_URL_ENDPOINT=https://ik.imagekit.io/your-endpoint
NEXT_PUBLIC_CLOUDINARY_CLOUD_NAME=your-cloud-name

# Queue/Cache
REDIS_URL=redis://localhost:6379
QSTASH_CURRENT_SIGNING_KEY=your-qstash-key
QSTASH_NEXT_SIGNING_KEY=your-qstash-next-key

# Monitoring
SENTRY_AUTH_TOKEN=your-sentry-token
NEXT_PUBLIC_SENTRY_DSN=your-sentry-dsn

# Cache
UPSTASH_REDIS_REST_URL=https://xxx.upstash.io
UPSTASH_REDIS_REST_TOKEN=your-upstash-token

# App
NEXT_PUBLIC_APP_URL=http://localhost:3000
```

### Installation

```bash
# Install dependencies
bun install

# Generate Drizzle migrations
bun run db:generate

# Apply migrations
bun run db:migrate

# Seed the database
bun run db:seed

# Start development server
bun run dev
```

### Database Management

```bash
# Generate new migration
bun run db:generate

# Apply pending migrations
bun run db:migrate

# View database with Drizzle Studio
bun run db:studio

# Push schema (dev only)
bun run db:push
```

---

## Feature Guide

### Authentication

- **Credentials** — Email/password with bcrypt hashing
- **OAuth** — GitHub and Google OAuth via NextAuth v5
- **Session Management** — JWT sessions with automatic refresh
- **Password Reset** — Email-based password reset flow with tokens
- **Account Recovery** — Email verification for new accounts

### Comic Management

- **Comic CRUD** — Full lifecycle with slug generation, image upload, status tracking
- **Chapter Management** — Ordered chapters with unique constraint per comic
- **Image Handling** — Chapter page images ordered by page number
- **Genre Classification** — Many-to-many genre tagging with taxonomy
- **Author/Artist Profiles** — Dedicated profiles with search support

### Reading Interface

- **Multiple Layouts** — Webtoon (vertical scroll), Comic (page flip), Book layout
- **Image Optimization** — Lazy loading with progressive quality selection
- **Reading Progress** — Auto-saves scroll position, page number, and percentage
- **Reader Settings** — Background mode, reading direction, font size

### Social Features

- **Bookmarks** — Save comics with status (Reading, Completed, Plan to Read, Dropped) and notes
- **Comments** — Threaded comments on chapters with soft-delete
- **Ratings** — 1-5 star rating with optional review text
- **Follow System** — Follow other users to see their activity
- **Activity Feed** — See friends' reading activity and shares
- **Notifications** — In-app notifications for new chapters, replies, and system alerts

### Search

- **Full-Text Search** — PostgreSQL tsvector with stemmed search across titles, synopses, authors, artists, genres
- **Advanced Filters** — Filter by status, genre, rating range, type, publication date
- **Autocomplete** — Real-time search suggestions

### Admin Panel

- **Dashboard** — Overview of platform metrics
- **Content Management** — CRUD for comics, chapters, authors, artists, genres, types
- **User Management** — View/manage users with role assignment
- **RBAC** — Role and permission management with audit logging
- **Audit Logs** — Comprehensive action tracking with filtering

---

## Security Architecture

### Authentication & Authorization
- **NextAuth v5** with GitHub, Google OAuth, and Credentials providers
- **RBAC** with granular permissions (12 resource types × 5 action types)
- **System roles** (User, Moderator, Admin) with immutable base permissions
- **Audit logging** — every state-changing action logs user, resource, old/new values, IP, user agent

### Input Validation
- **Zod schemas** in `src/schemas/` validate all external input at runtime
- **Server Actions** always call `.parse()` or `.safeParse()` before processing
- **Env validation** via `src/lib/env.ts` with Zod schema at startup

### Data Protection
- **SQL injection prevention** — All queries use Drizzle ORM parameterized queries (no raw SQL)
- **Soft deletes** — User accounts and comments use `deletedAt` timestamp, preserving referential integrity
- **Cascade deletes** — Child records cleaned up when parent is removed (except historical references)
- **Password hashing** — bcryptjs with salt rounds for credential auth

### Rate Limiting & Abuse Prevention
- **Upstash Ratelimit** configured in package.json for optional Redis-based rate limiting
- **CSRF protection** — All mutations use Next.js Server Actions which include built-in CSRF tokens
- **Middleware guards** — Protected routes redirect unauthenticated users; auth routes redirect authenticated users

### Environment Security
- **No raw `process.env`** — All environment access goes through `appConfig.ts` (ESLint enforced)
- **Zod-validated env schema** — Missing/invalid variables fail at startup, not silently at runtime
- **Credential rotation** — `.env.local` uses placeholder values; production secrets managed via host secrets

## Performance Optimization

### Database Performance
- **Eager loading** — All DAL queries use Drizzle `.with()` to prevent N+1 queries
- **Indexed columns** — Foreign keys, search fields, and sort columns are indexed (30+ indexes across all tables)
- **Full-text search** — Dedicated `searchIndex` table with PostgreSQL tsvector for efficient text search
- **Pagination** — All list queries support `limit`/`offset` pagination with total count

### Frontend Performance
- **React Compiler** enabled — No manual `useMemo`/`useCallback`/`memo` needed (ESLint enforced)
- **Server Components by default** — Minimal JavaScript sent to client
- **Suspense streaming** — Dynamic content sections stream in independently
- **Image optimization** — Lazy loading with progressive quality selection via ImageKit/Cloudinary
- **Code splitting** — Automatic route-level code splitting via Next.js App Router
- **Turbopack builds** — ~35s production builds with 0 TypeScript errors

### Caching Strategy
- **React Query** — Client-side cache with stale-while-revalidate for non-auth data
- **Server-side revalidation** — `revalidatePath()` and `revalidateTag()` after mutations
- **Static assets** — CDN-hosted images with automatic cache busting on upload

## Testing

```bash
# Run unit tests (Vitest)
bun run test

# Run E2E tests (Playwright)
bun run test:e2e

# Run with UI
bun run test:ui
```

### Test Coverage
- **Unit Tests:** Auth operations, DAL CRUD methods, Zod schema validation, server action logic
- **E2E Tests:** Sign-in/sign-up flow, comic browsing and search, chapter reading, admin CRUD, comments, follow system, RBAC enforcement, visual snapshots

### Quality Gates
```bash
# Full validation pipeline (required before every PR)
pnpm lint:strict && pnpm triage && pnpm type-check && pnpm test && pnpm build
```

## Deployment

### Build

```bash
bun run build
bun run start
```

### Docker

```dockerfile
FROM node:20-alpine AS base
WORKDIR /app
COPY package.json bun.lock ./
RUN bun install --frozen-lockfile
COPY . .
RUN bun run build

FROM node:20-alpine AS runner
WORKDIR /app
COPY --from=base /app/.next ./.next
COPY --from=base /app/public ./public
COPY --from=base /app/node_modules ./node_modules
COPY --from=base /app/package.json ./
EXPOSE 3000
ENV NODE_ENV=production
CMD ["bun", "run", "start"]
```

### Environment

- Deploy to **Vercel** (recommended) — Automatic builds, serverless PostgreSQL via Neon, edge caching
- **Docker** — Multi-stage build for minimal image size (~150MB)
- **Railway** — One-click deploy with managed PostgreSQL
- Configure all secrets via platform secrets manager (never bake into images)
- Enable Upstash Redis for rate limiting in production
