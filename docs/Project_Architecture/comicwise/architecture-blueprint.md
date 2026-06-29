# Architecture Blueprint: comicwise

**Generated:** 2026-06-29  
**Generator:** architecture-blueprint-generator  

---

## 1. Architecture Detection and Analysis

### Technology Stack

| Category | Technology |
|---|---|
| **Framework** | Next.js 15 (App Router) |
| **Language** | TypeScript (strict) |
| **Database** | PostgreSQL |
| **ORM** | Drizzle ORM |
| **Authentication** | NextAuth v5 (credentials/OAuth, JWT) |
| **Client State** | Zustand |
| **Server State** | TanStack Query |
| **Caching** | Upstash Redis |
| **Payments** | Stripe, PayPal |
| **Image Storage** | ImageKit, Cloudinary |
| **Email** | Resend |
| **Monitoring** | Sentry |
| **Rate Limiting** | Upstash |
| **UI Components** | shadcn/ui (Radix UI) |
| **Styling** | Tailwind CSS |
| **Package Manager** | pnpm |

### Architectural Pattern Detected

**Pattern:** Modern Next.js App Router with RSC + Server Actions  
The project uses React Server Components for data fetching and Server Actions for mutations, with client-side interactivity via TanStack Query and Zustand.

### Architecture Layers

| Layer | Implementation |
|---|---|
| **Presentation** | Next.js App Router with route groups, RSC + Client Components |
| **Data** | Drizzle ORM, Server Actions, TanStack Query |
| **State** | Server State (RSC), Client State (Zustand), Cache (Upstash Redis) |
| **Auth** | NextAuth v5 with JWT session management |
| **External** | ImageKit/Cloudinary, Stripe/PayPal, Resend, Sentry |

---

## 2. Architectural Overview

### Guiding Principles

1. **Server-first rendering**: React Server Components by default, Client Components only for interactivity
2. **Mutations via Server Actions**: All data writes use Next.js Server Actions
3. **External caching**: Upstash Redis for rate limiting and cache state
4. **Payment integration**: Dual payment provider support (Stripe + PayPal)

### Data Flow

```
Browser → Next.js App Router → RSC/Server Action → Drizzle ORM → PostgreSQL
                                      ↓
                                Upstash Redis (cache)
                                      ↓
                     ImageKit/Cloudinary (images), Stripe/PayPal (payments)
```

---

## 3. Implementation Patterns

### Server Action Pattern
All mutations use `"use server"` directives with Zod validation and typed error returns.

### Data Access
Drizzle ORM with typed queries and migrations via `drizzle-kit`.

### Payment Flow
Stripe webhooks for subscription lifecycle events; PayPal as secondary provider.

---

## 4. Key Architectural Decisions

| Decision | Rationale |
|---|---|
| Drizzle ORM over Prisma | Lightweight, SQL-like, better TypeScript integration |
| pnpm over npm | Faster installs, disk efficiency |
| Dual payments (Stripe + PayPal) | Maximum user payment flexibility |
| Upstash Redis | Serverless-friendly caching and rate limiting |

---

## 5. Extensibility Points

1. **New comic genres/categories**: Extend database schema and add route groups
2. **Additional payment providers**: Follow Stripe integration pattern
3. **Enhanced search**: Integrate with Upstash or Algolia
4. **Reader analytics**: Add tracking via existing external services pattern

---

*End of architecture blueprint.*
