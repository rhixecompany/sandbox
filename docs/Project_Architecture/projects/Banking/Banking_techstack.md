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
|---|---|---|
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

| Category | Libraries |
|---|---|
| **UI Framework** | `next@16.2.4`, `react@19.2.5`, `react-dom@19.2.5` |
| **UI Components** | `@radix-ui/react-*` (15+ packages), `@base-ui/react`, `radix-ui`, `cmdk`, `vaul`, `sonner`, `embla-carousel-react` |
| **Styling** | `tailwindcss@4.2.4`, `@tailwindcss/postcss`, `tailwind-merge`, `class-variance-authority`, `clsx`, `tw-animate-css` |
| **State** | `zustand@5.0.12` |
| **Forms** | `react-hook-form@7.75.0`, `zod@4.4.3`, `@hookform/resolvers`, `input-otp` |
| **Charts** | `recharts@3.8.1`, `chart.js@4.5.1`, `react-chartjs-2`, `react-countup` |
| **Data Table** | `@tanstack/react-table@8.21.3` |
| **Drag & Drop** | `@dnd-kit/core`, `@dnd-kit/modifiers`, `@dnd-kit/sortable`, `@dnd-kit/utilities` |
| **Date Handling** | `react-day-picker@9.14.0`, `date-fns@4.1.0` |
| **Icons** | `lucide-react@1.14.0` |

---

## Backend / Database Stack

| Category | Libraries |
|---|---|
| **Database Driver** | `pg@8.20.0`, `postgres@3.4.9` |
| **ORM** | `drizzle-orm@0.45.2`, `drizzle-kit@0.31.10` |
| **Auth Framework** | `next-auth@4.24.14`, `@auth/drizzle-adapter@1.11.2` |
| **Password Hashing** | `bcryptjs@3.0.3` |
| **Password Strength** | `@zxcvbn-ts/core@3.0.4` |

### Database Schema (13 tables)

| Table | Key Columns | Purpose |
|---|---|---|
| `users` | email, password, isAdmin, role (enum) | Core user auth & profile |
| `account` | provider, providerAccountId, userId FK | NextAuth OAuth links |
| `session` | sessionToken, userId FK | NextAuth session storage |
| `verificationToken` | identifier, token | Email verification |
| `authenticator` | credentialID, userId FK | WebAuthn passkeys |
| `user_profiles` | userId FK, address, DOB, ssnEncrypted | KYC data (encrypted SSN) |
| `plaid_items` | itemId, accessTokenEncrypted, userId FK | Plaid item registry |
| `wallets` | sharableId UK, fundingSourceUrl, userId FK | Linked bank accounts |
| `transactions` | amount, status (enum), plaidTransactionId UK | Financial ledger |
| `dwolla_transfers` | idempotencyKey UK, dwollaTransferId | Dwolla ACH metadata |
| `recipients` | email, name, userId FK | Saved transfer recipients |
| `errors` | message, severity, stack, userId FK | Error logging |
| `audit_logs` | action, metadata, userId FK | Append-only compliance trail |

### Database Enums (4)

| Enum | Values |
|---|---|
| `user_role` | `user` \| `admin` \| `moderator` |
| `transaction_status` | `pending` \| `processing` \| `completed` \| `failed` \| `cancelled` |
| `transaction_type` | `credit` \| `debit` |
| `transaction_channel` | `online` \| `in_store` \| `other` |

---

## Financial Integration

| Service | Library | Version | Role |
|---|---|---|---|
| **Plaid API** | `plaid` | ^42.2.0 | Bank linking, transaction sync |
| **Plaid Link** | `react-plaid-link` | ^4.1.1 | Client-side Plaid OAuth |
| **Dwolla API** | `dwolla-v2` | ^3.4.0 | ACH transfers, customer mgmt |

### Architecture

- Plaid: read-only bank account linking + transaction history sync
- Dwolla: write operations — ACH transfers, funding sources, customer verification
- Access tokens encrypted with AES-256-GCM at rest
- Idempotency keys prevent duplicate Dwolla transfers
- Webhook endpoint: `POST /api/dwolla/webhook`

---

## Caching & Rate Limiting

| Service | Library | Version | Purpose |
|---|---|---|---|
| **Upstash Redis** | `@upstash/redis` | ^1.37.0 | Serverless caching |
| **Upstash Rate Limit** | `@upstash/ratelimit` | ^2.0.8 | API rate limiting |
| **Upstash QStash** | `@upstash/qstash-cli` | — | Scheduled tasks |

---

## Security

| Layer | Technology |
|---|---|
| Auth tokens | NextAuth JWT (HTTP-only cookies) |
| Password hashing | bcryptjs |
| Data encryption | AES-256-GCM (Plaid tokens, SSNs, account numbers) |
| Input validation | Zod schemas (forms, API, env) |
| Rate limiting | Upstash Redis |
| Secret detection | eslint-plugin-no-secrets |
| Compliance | Append-only audit_logs table |

---

## Testing Stack

| Tool | Version | Scope |
|---|---|---|
| **Playwright** | ^1.59.1 | E2E browser tests (12+ spec files) |
| **Vitest** | ^4.1.5 | Unit + integration tests |
| **@testing-library/react** | ^16.3.2 | React component tests |
| **msw** | ^2.14.2 | HTTP mocking |
| **happy-dom** | ^20.9.0 | DOM environment |

---

## Code Quality

| Area | Tools |
|---|---|
| **Linting** | `eslint@10.3.0`, `typescript-eslint@8.59.1`, `eslint-config-next`, 15+ plugins |
| **Formatting** | `prettier@3.8.3`, `markdownlint-cli2`, `cspell@10.0.0` |
| **Pre-commit** | `husky@9.1.7`, `lint-staged@16.4.0` |
| **Type Checking** | `typescript@6.0.3` with `tsc --noEmit` |

---

## CI/CD & Deployment

| Platform | Config | Notes |
|---|---|---|
| **Vercel** | `vercel.json` | Primary production target |
| **Docker** | `docker-compose.yml`, `compose/prod/` | Self-hosted with Traefik, Grafana, Prometheus |
| **Railway** | `Railway.toml` | Alternative cloud deployment |

---

## Environment Variables

| Variable | Purpose |
|---|---|
| `DATABASE_URL` | PostgreSQL connection string |
| `NEXTAUTH_URL` / `NEXTAUTH_SECRET` | NextAuth config |
| `PLAID_CLIENT_ID` / `PLAID_SECRET` / `PLAID_ENV` | Plaid integration |
| `DWOLLA_KEY` / `DWOLLA_SECRET` / `DWOLLA_ENV` | Dwolla integration |
| `UPSTASH_REDIS_URL` / `UPSTASH_REDIS_TOKEN` | Redis caching |
| `ENCRYPTION_KEY` | AES-256-GCM key |
| `SMTP_HOST` / `SMTP_PORT` | Email configuration |

---

## Key Scripts

| Script | Purpose |
|---|---|
| `bun run dev` | Development server |
| `bun run build` | Production build |
| `bun run test` | Playwright + Vitest |
| `bun run db:generate` | Drizzle migrations |
| `bun run db:studio` | Drizzle Studio UI |
| `bun run lint:strict` | Zero-warnings ESLint |
| `bun run type-check` | TypeScript verification |
| `bun run validate` | Full validation suite |

---

## Coding Conventions

- **TypeScript strict** mode enabled
- **Server Components by default**, `"use client"` only for interactivity
- **PascalCase** for React components, **camelCase** for hooks/utils
- **Zod schemas** for all form, API, and env validation
- **DAL pattern** — all DB queries through `src/dal/`, never inline
- **Soft deletes** on users, wallets, transactions
- **AES-256-GCM encryption** for all sensitive data at rest

---

*Generated by technology-stack-blueprint-generator — comprehensive analysis*
