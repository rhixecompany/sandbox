# Technology Stack Blueprint

## Project: rhixe_scans — Comic Reader

> **Generated:** 2026-06-25  
> **Generator:** technology-stack-blueprint-generator  
> **Analysis Depth:** Comprehensive

---

## Overview

A full-featured comic/manga reading platform built with Next.js 15, featuring Prisma 6 ORM, authentication, payment processing, file uploads, and real-time capabilities.

**Project Type:** Full-Stack Web Application (Comic Reader)  
**Stack Type:** Next.js

---

## Technology Stack

### Languages & Runtimes

| Technology | Version | Usage |
|---|---|---|
| TypeScript | ^5 | Primary language (strict mode) |
| React | ^19.1.0 | UI framework |
| Next.js | ^15.3.3 | Full-stack framework |
| Node.js | — | JavaScript runtime |
| npm | — | Package manager |

### Package Manager

| Tool | Version |
|---|---|
| npm | — |

### Core Dependencies

| Category | Dependencies |
|---|---|
| **UI Framework** | next ^15.3.3, react ^19.1.0, react-dom ^19.1.0 |
| **UI Components** | @radix-ui/* (18+ packages), embla-carousel, cmdk, vaul, sonner |
| **Styling** | tailwindcss ^3.4.1, tailwind-merge, tailwindcss-animate, class-variance-authority, clsx |
| **Icons** | lucide-react |
| **Forms & Validation** | react-hook-form ^7.58.1, @hookform/resolvers, zod ^3.25.67 |
| **Data Display** | @tanstack/react-table, recharts ^2.15.3 |
| **Database** | @prisma/client ^6.10.0, prisma 6.10.0 |
| **ORM** | Prisma 6 (schema: `src/db/schema.prisma`) |
| **Authentication** | next-auth ^5.0.0-beta.25, @auth/prisma-adapter |
| **Payments** | stripe ^18.2.1, @stripe/react-stripe-js, @stripe/stripe-js, @paypal/react-paypal-js |
| **File Uploads** | @uploadthing/react ^7.3.1, uploadthing ^7.7.2 |
| **Email** | resend ^4.6.0, @react-email/components, react-email ^4.0.16 |
| **Real-time** | ws ^8.18.2 |
| **Supabase** | @supabase/ssr |
| **Utilities** | uuid ^11.1.0, slugify, pretty-bytes, use-debounce, query-string |

### Dev Dependencies

| Category | Dependencies |
|---|---|
| **Testing** | jest ^30.0.0, ts-jest ^29.4.0 |
| **Linting** | eslint ^9, eslint-config-next 15.3.3 |
| **Utilities** | dotenv, npm-check-updates, shx, ts-node, supabase |
| **Types** | @types/node, @types/react, @types/react-dom, @types/jest, @types/ws |

---

## Licensing

| Component | License |
|---|---|
| rhixe_scans | Private |

---

## Database Schema

- **ORM**: Prisma 6
- **Client**: @prisma/client
- **Schema**: `src/db/schema.prisma`
- **Seed**: Custom seed script at `src/lib/seed`

---

## External Integrations

| Service | Package | Purpose |
|---|---|---|
| Stripe | stripe, @stripe/react-stripe-js | Payment processing |
| PayPal | @paypal/react-paypal-js | Payment processing |
| UploadThing | uploadthing, @uploadthing/react | File uploads |
| Resend | resend | Email delivery |
| Supabase | @supabase/ssr | Auth/Storage (optional) |
| WebSocket | ws | Real-time features |

---

## Key Scripts

| Script | Description |
|---|---|
| `dev` | Next.js dev with Turbopack |
| `build` | Production build |
| `db:migrate` | Prisma migrations |
| `db:seed` | Database seeding |
| `db:studio` | Prisma Studio |
| `test` | Jest tests |
| `lint` | Next.js linting |

---

## Coding Conventions

- **TypeScript**: Strict mode
- **Components**: PascalCase
- **Hooks/Utils**: camelCase
- **Pages**: kebab-case
- **Zod validation**: Schema validation
- **`cn()` utility**: Tailwind class merging
- **shadcn/ui**: Radix-based components (via CVA)
- **Migrations**: Use `prisma migrate` (not `db:push` in production)

---

## Architecture Diagram

```
┌──────────────────────────────────────────────────────────┐
│              rhixe_scans (Next.js 15)                     │
├──────────────────────────────────────────────────────────┤
│  App Router Pages                                        │
│  ├── /                    Browse comics                   │
│  ├── /comics/[id]        Reader interface                 │
│  ├── /auth               NextAuth v5                      │
│  ├── /account            User settings                    │
│  └── /admin              Administration                   │
├──────────────────────────────────────────────────────────┤
│  Core Services                                            │
│  ├── Prisma 6 → PostgreSQL                                │
│  ├── NextAuth v5                                          │
│  ├── Stripe + PayPal                                     │
│  ├── UploadThing (file uploads)                           │
│  ├── Resend (email)                                       │
│  └── WebSocket (real-time)                                │
├──────────────────────────────────────────────────────────┤
│  Quality                                                  │
│  ├── Jest + ts-jest                                       │
│  ├── ESLint + Next eslint config                          │
│  └── Prettier + Tailwind plugin                          │
└──────────────────────────────────────────────────────────┘
```

---

## Deployment

| Platform | Notes |
|---|---|
| Vercel | Primary target |
| Docker | Available as alternative |
