# AGENTS.md

> **Refreshed by AGENTS workflow 2026-06-01**

## Project Overview

Rhixescans — a full-featured web application for reading comics online. Built with Next.js 15, TypeScript, Prisma ORM, and Tailwind CSS with Stripe/PayPal payment integration.

**Tech Stack:**
- **Frontend**: Next.js 15 (App Router, Turbopack), TypeScript, React 19
- **Styling**: Tailwind CSS 3, Radix UI primitives (shadcn/ui style), embla-carousel
- **Database**: PostgreSQL via Prisma ORM 6
- **Auth**: NextAuth v5 with Prisma adapter
- **Payments**: Stripe (react-stripe-js), PayPal (@paypal/react-paypal-js)
- **Storage**: UploadThing for file uploads
- **Email**: Resend + React Email
- **Realtime**: WebSocket (ws) support
- **UI**: @dnd-kit for drag-and-drop, @tanstack/react-table for data tables, recharts for charts, sonner for toasts
- **Testing**: Jest with ts-jest

<<<<<<< HEAD
=======
## Hermes and Copilot

- Use the nearest `AGENTS.md` for files under `projects/rhixe_scans/`; this file
  is the local fallback.
- `projects/rhixe_scans/.github/copilot-instructions.md` is the primary Copilot
  guidance file for this project.
- Root Hermes orchestration assets live in `../../.github/agents/hermes.agent.md`
  and `../../.github/prompts/`.
- Keep this file, the local Copilot instructions, and the Prisma/Next.js docs
  aligned when auth, payments, or data flows change.

>>>>>>> 71568c2 (chore: initial local project setup for rhixe_scans)
## Setup Commands

```bash
# Install dependencies
npm install

# Copy environment variables
cp .env.example .env
# Edit .env with your database URL, auth secret, API keys

# Initialize database
npx prisma migrate dev
npm run db:seed

# Start development server
npm run dev
```

## Development Workflow

```bash
# Dev server (Turbopack)
npm run dev

# Linting
npm run lint

# Format code
npx prettier --write .

# Database changes
npx prisma migrate dev --name description_of_change
npm run db:seed  # Re-seed after schema changes
```

## Testing Instructions

```bash
# Run all tests
npm test

# Watch mode
npm run test:watch

# Database checks
npx prisma studio  # Visual DB browser
```

## Code Style

- **TypeScript**: Strict mode, ESLint with Next.js config
- **Components**: PascalCase, shadcn/ui conventions, Radix UI primitives
- **Styling**: Tailwind CSS with cn() utility, tailwind-merge, class-variance-authority
- **Forms**: React Hook Form + Zod validation with @hookform/resolvers
- **Database**: Prisma schema-driven, migrations via Prisma Migrate
- **File naming**: camelCase for utilities/hooks, PascalCase for components, kebab-case for pages

## Build/Deployment

```bash
# Clean and build
npm run clean
npm run build

# Production start
npm start
```

Deploy via Vercel (recommended) or Docker. Requires PostgreSQL database, Stripe/PayPal keys, and UploadThing/Resend API keys configured.

## Security

- Never commit `.env` files
- Use NextAuth v5 for authentication — never custom session management
- All user inputs validated with Zod schemas
- API routes should check authentication via NextAuth
- Rate limiting via Upstash Ratelimit (if configured)
- Stripe/PayPal keys kept server-side only
- Prisma ORM prevents SQL injection
- HTTPS enforced in production

## Troubleshooting

- **Database connection failed**: Verify `DATABASE_URL` in `.env` and ensure PostgreSQL is running
- **Prisma errors**: `npx prisma generate` then `npx prisma migrate dev`
- **Build failures**: `npm run clean` then `npm run build`
- **Auth issues**: Check `NEXTAUTH_SECRET` and `NEXTAUTH_URL` in `.env`
- **Module not found**: Delete `node_modules` and `package-lock.json`, re-run `npm install`
- **Stripe/PayPal sandbox**: Use test keys in development
