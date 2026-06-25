# Technology Stack Blueprint

## Project: university-libary-jsm — Library Management

> **Generated:** 2026-06-25  
> **Generator:** technology-stack-blueprint-generator  
> **Analysis Depth:** Comprehensive

---

## Overview

A university library management system built with Next.js 15, using Drizzle ORM with Neon (serverless PostgreSQL), Upstash Redis for caching/rate limiting, and NextAuth for authentication.

**Project Type:** Full-Stack Web Application (Library Management)  
**Stack Type:** Next.js

---

## Technology Stack

### Languages & Runtimes

| Technology | Version | Usage |
|---|---|---|
| TypeScript | ^5 | Primary language |
| React | 19.1.0 | UI framework |
| Next.js | 15.4.2 | Full-stack framework (App Router) |
| Node.js | — | JavaScript runtime |
| npm | — | Package manager |

### Core Dependencies

| Category | Dependencies |
|---|---|
| **UI Framework** | next 15.4.2, react 19.1.0, react-dom 19.1.0 |
| **UI Components** | @radix-ui/* (14+ packages), vaul, sonner |
| **Styling** | tailwindcss ^4.1.11, @tailwindcss/postcss, tailwind-merge, tw-animate-css, class-variance-authority, clsx, autoprefixer |
| **Icons** | lucide-react, @tabler/icons-react ^3.34.0 |
| **State/Data** | @tanstack/react-table |
| **Forms & Validation** | react-hook-form ^7.60.0, @hookform/resolvers ^3.9.1, zod ^4.0.5 |
| **Database** | drizzle-orm ^0.44.3, drizzle-kit ^0.31.4 |
| **Serverless DB** | @neondatabase/serverless ^1.0.1 |
| **Auth** | next-auth ^5.0.0-beta.25 |
| **Caching** | @upstash/ratelimit ^2.0.5, @upstash/redis ^1.35.1, @upstash/workflow ^0.2.16 |
| **Email** | nodemailer ^7.0.5, @react-email/components 0.3.2, react-email 4.2.3 |
| **Media** | imagekit ^6.0.0, imagekitio-next ^1.0.1 |
| **Utilities** | dayjs ^1.11.13, slugify, react-colorful, recharts ^2.15.4 |

### Dev Dependencies

| Category | Dependencies |
|---|---|
| **Linting** | eslint ^9, eslint-config-next 15.4.2, eslint-config-prettier, eslint-plugin-* (drizzle, jsx-a11y, prettier, react, zod) |
| **Formatting** | prettier ^3.6.2, prettier-plugin-tailwindcss |
| **Types** | @types/node, @types/react, @types/react-dom, @types/ms, @types/nodemailer |
| **Utilities** | npm-check-updates, tsx ^4.20.3, react-email 4.2.3 |

---

## Licensing

| Component | License |
|---|---|
| university-libary-jsm | Private |

---

## Database Schema

- **ORM**: Drizzle ORM
- **Database**: PostgreSQL (Neon serverless)
- **Migrations**: Drizzle Kit (generate, push, migrate)
- **Seed**: `npx tsx database/seed.ts`

---

## Authentication

- **Framework**: NextAuth v5 (beta)
- **Adapter**: Drizzle adapter

---

## External Integrations

| Service | Package | Purpose |
|---|---|---|
| Neon (PostgreSQL) | @neondatabase/serverless | Serverless database |
| Upstash Redis | @upstash/redis | Caching & rate limiting |
| Upstash QStash | @upstash/workflow | Async workflows |
| ImageKit | imagekit, imagekitio-next | Media optimization |

---

## Key Scripts

| Script | Description |
|---|---|
| `dev` | Dev server with Turbopack |
| `build` | Production build |
| `db:*` | Database operations (generate, push, migrate, studio) |
| `lint` | ESLint |
| `format` / `format:check` | Prettier |

---

## Coding Conventions

- **TypeScript strict**: Full type safety
- **App Router**: Next.js App Router
- **Tailwind CSS 4**: Utility-first styling
- **Zod**: Schema validation
- **shadcn/ui**: Radix-based components

---

## Architecture Diagram

```
┌──────────────────────────────────────────────────────────┐
│         university-libary-jsm (Next.js 15)               │
├──────────────────────────────────────────────────────────┤
│  App Router Pages                                        │
│  ├── /                    Library dashboard               │
│  ├── /books               Book catalog                    │
│  ├── /members             Member management               │
│  ├── /loans               Loan tracking                   │
│  └── /auth                Authentication                  │
├──────────────────────────────────────────────────────────┤
│  Database Layer                                           │
│  ├── Drizzle ORM → Neon (Serverless PostgreSQL)          │
│  └── Redis (Upstash) for caching                         │
├──────────────────────────────────────────────────────────┤
│  External Services                                        │
│  ├── NextAuth v5 (authentication)                        │
│  ├── ImageKit (media/images)                             │
│  ├── Upstash (Redis cache + QStash)                      │
│  └── Resend/Nodemailer (email)                           │
└──────────────────────────────────────────────────────────┘
```
