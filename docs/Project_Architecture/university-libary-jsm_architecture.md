# university-libary-jsm — Architecture

## Overview
University Library Management System (BookWise) — a full-stack Next.js application for managing library book requests, user accounts, and administrative workflows.

## Architecture Pattern
- **Type:** Full-stack Next.js Application
- **Pattern:** Next.js 15 App Router with Server Actions
- **Database:** Drizzle ORM on Neon PostgreSQL
- **Auth:** NextAuth v5 with Upstash Redis rate limiting

## Components
- **`app/`** — Next.js App Router pages and layouts
- **`components/`** — shadcn/ui components with Radix UI primitives
- **`database/`** — Drizzle ORM schema, migrations, seeds
- **`lib/`** — Utility functions, API helpers
- **`hooks/`** — React hooks
- **`emails/`** — React Email templates
- **`constants/`** — Application constants
- **`assets/`** — Static assets
- **`public/`** — Public static files

## Cross-Cutting Concerns
- **Auth:** NextAuth v5 with JWT sessions
- **Rate Limiting:** Upstash Redis Ratelimit
- **File Uploads:** ImageKit (server-side signed URLs)
- **Async Workflows:** Upstash Workflow + QStash
- **Validation:** Zod 4 + react-hook-form
- **Email:** React Email + Nodemailer

## Data Flow
1. Server Components fetch data directly via Drizzle ORM
2. Client Components interact via Server Actions (form submissions)
3. Auth state managed by NextAuth v5 `auth()` helper
4. File uploads go through ImageKit signed URLs
5. Background jobs via Upstash Workflow
