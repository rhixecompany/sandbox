<<<<<<< HEAD
# AGENTS.md

> **Refreshed by AGENTS workflow 2026-06-01**

## Project Overview

University Library Management System (BookWise) — a full-stack Next.js application for managing library book requests, user accounts, and administrative workflows. Built with modern tooling including Drizzle ORM, Neon PostgreSQL, Upstash Redis/Workflows, and ImageKit for media.

**Tech Stack:**
- **Frontend**: Next.js 15 (Turbopack), TypeScript 5, React 19, Tailwind CSS 4
- **UI**: shadcn/ui with Radix UI primitives, @dnd-kit drag-and-drop, @tanstack/react-table, recharts
- **Database**: PostgreSQL (Neon serverless via @neondatabase/serverless) with Drizzle ORM
- **Auth**: NextAuth v5 (beta) with Upstash Redis for rate limiting
- **Storage**: ImageKit for image uploads
- **Email**: React Email + Nodemailer
- **Workflows**: Upstash Workflow + QStash for async job processing
- **Validation**: Zod 4 with react-hook-form
- **Styling**: Tailwind CSS 4, class-variance-authority, tailwind-merge, lucide-react icons

## Setup Commands

```bash
# Install dependencies
npm install

# Copy environment variables
cp .env.example .env
# Edit .env with database URL, auth secret, ImageKit keys, etc.

# Push database schema
npm run db:push

# Seed sample data
npm run db:seed

# Start development server
npm run dev
```

## Development Workflow

```bash
# Dev server with Turbopack (fast refresh)
npm run dev

# Lint and format
npm run lint
npm run format

# Database changes
# 1. Edit schema in database/schema.ts
# 2. Generate migration: npm run db:generate
# 3. Apply migration: npm run db:migrate

# Browse database
npm run db:studio

# Email preview
npm run dev:email
```

## Testing Instructions

```bash
# Next.js linting
npm run lint

# TypeScript check
npx tsc --noEmit

# Format check
npm run format:check
```

(No formal test suite configured — testing via manual verification and ESLint.)

## Code Style

- **TypeScript**: Strict mode, ESLint 9 with Next.js config + Prettier + plugins for drizzle, zod, jsx-a11y
- **Components**: PascalCase, shadcn/ui conventions, Radix UI primitives
- **Styling**: Tailwind CSS 4 with `cn()` utility, tailwind-merge, CVA
- **Forms**: React Hook Form + Zod 4 resolvers
- **Database**: Drizzle ORM with Zod schema validation for type safety
- **Server Actions**: Use Next.js Server Actions for mutations, Zod for input validation
- **File naming**: PascalCase for components, camelCase for utilities/hooks, dot notation for actions

## Build/Deployment

```bash
# Production build
npm run build

# Start production server
npm start

# Database migration (production)
npm run db:migrate
```

Deploy on Vercel (recommended for Next.js) with Neon PostgreSQL and Upstash Redis. Requires environment variables for database, auth, ImageKit, and Upstash.

## Security

- Never commit `.env` files or secrets
- NextAuth v5 handles session management — use `auth()` helper for protected routes
- All server actions validate inputs with Zod schemas
- Rate limiting via Upstash Ratelimit in API routes
- File uploads go through ImageKit (server-side signed URLs)
- Drizzle ORM with parameterized queries prevents SQL injection
- Rate limit exceeded page at `/too-fast`
- Unauthorized access redirects to `/unauthorized`

## Troubleshooting

- **Database connection**: Verify `DATABASE_URL` (Neon connection string) in `.env`
- **Drizzle errors**: `npm run db:push` for schema sync, or `npm run db:generate` + `npm run db:migrate`
- **Build fails**: Check TypeScript errors with `npx tsc --noEmit`, fix type issues
- **Auth not working**: Ensure `AUTH_SECRET` and `AUTH_URL` are set correctly in `.env`
- **ImageKit not loading**: Verify `IMAGEKIT_PUBLIC_KEY`, `IMAGEKIT_PRIVATE_KEY`, `IMAGEKIT_URL_ENDPOINT`
- **Upstash Workflow errors**: Check QStash token and Upstash Redis URL
- **prettier/eslint conflicts**: Config uses eslint-config-prettier to avoid conflicts
=======
# University Library JSM - Library Management Context

Next.js 15 library management system with Drizzle, Neon, and Redis.

## Architecture
- **Framework**: Next.js 15 (App Router)
- **Language**: TypeScript
- **Database**: Drizzle ORM + Neon (serverless Postgres)
- **Cache**: Redis
- **Auth**: NextAuth.js
- **Deployment**: Vercel + Neon

## Conventions
- TypeScript strict mode
- Server Components by default
- API routes in `src/app/api/`
- Drizzle schema in `src/db/schema.ts`
- Redis for session caching
- Environment variables in `.env.local`

## Commands
```bash
# Dev server
npm run dev

# Build
npm run build

# Database
npm run db:generate
npm run db:push
npm run db:studio

# Lint
npm run lint
```

## Important Notes
- Neon connection string in `.env.local` — never commit
- Redis for rate limiting and caching
- Drizzle migrations managed via `db:push`
>>>>>>> 770ece9 (chore: initial local project setup for university-libary-jsm)
