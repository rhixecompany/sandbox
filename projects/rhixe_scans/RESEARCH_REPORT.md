# Research Report: rhixe_scans

> **Date:** 2026-06-29  
> **Scope:** Architecture, tech stack & web-backed patterns  
> **Methodology:** Local project inspection + web research (Next.js 15, Prisma 6, dual-payment, NextAuth v5, UploadThing)

---

## 1. Project Overview

**rhixe_scans** (pkg: `rhixescans`) is a full-featured web app for reading comics online, built with **Next.js 15 (App Router, Turbopack)**, **React 19**, **TypeScript** strict mode. Uses **PostgreSQL** via **Prisma ORM 6**, **NextAuth v5**, and **Stripe + PayPal** dual payment integration.

---

## 2. Web-Backed Findings

### 2.1 Next.js 15 + React 19 (Comic Reader Patterns)
- App Router with RSC by default; `"use client"` only for interactive components.
- **Turbopack** for dev (Rust-based, ~10x faster bundling).
- **Source:** App Router file-system routing (`page.tsx`, `layout.tsx`) is the recommended architecture for all new Next.js 15 projects (patterns.dev/react/nextjs). RSCs reduce client JS ~33% on content-heavy pages.

### 2.2 Zustand + TanStack Query (State Management)
- **Zustand** for light UI state; **TanStack Query** for server-state caching & pagination.
- **Source:** This dual-pattern (local + server state separation) is the dominant 2026 full-stack architecture. TanStack Query v5 provides stale-while-revalidate caching and infinite queries for chapter pagination.

### 2.3 Prisma 6 + PostgreSQL
- Schema at `src/db/schema.prisma`. Migrations via `prisma migrate dev`.
- **Source:** Prisma 6 delivers better JOIN strategy config, multi-file schema splitting, and type-safe raw SQL (prisma.io/blog/prisma-6). Singleton PrismaClient pattern critical in Next.js to avoid pool exhaustion during hot-reload.

### 2.4 NextAuth v5 + Prisma Adapter
- `@auth/prisma-adapter` (v2.9.1), JWT session strategy.
- **Source:** NextAuth v5 beta 25 is the standard for Next.js 15. Best practices: extend `DefaultSession` types, use `auth()` in server components, protect API routes via middleware (dev.to/whoffagents/nextauthjs-v5-prisma-postgresql).

### 2.5 Stripe + PayPal Dual Payment
- **Stripe:** `@stripe/react-stripe-js` v3.7 — Payment Element (40+ methods).
- **PayPal:** `@paypal/react-paypal-js` v8.8 — standard button SDK.
- **Source:** Dual integration maximizes conversion. Stripe covers broadest method range; PayPal leverages high buyer trust (pkgpulse.com/guides/stripe-react-vs-paypal-js-sdk-2026).

### 2.6 UploadThing (File Storage)
- `@uploadthing/react` v7.3 for comic page/avatar uploads.
- **Source:** Purpose-built for Next.js App Router. Pattern: `FileRouter` in `app/api/uploadthing/core.ts` with auth middleware and route-level size limits (docs.uploadthing.com/getting-started/appdir).

### 2.7 Supporting Stack
- **Email:** Resend v4.6 + React Email templates; dev preview on port 3001.
- **UI:** Tailwind CSS 3, Radix UI (19+ primitives), Embla Carousel (reader nav), dnd-kit (admin drag-drop), Recharts (analytics), TanStack Table (data tables).
- **Testing:** Jest v30 + ts-jest.
- **Realtime:** WebSocket (ws) for live sessions.

---

## 3. Architecture Summary

| Layer | Pattern | Notes |
|-------|---------|-------|
| Routing | App Router | Parallel routes, loading/error boundaries |
| Data | RSC + TanStack Query | Server initial, client mutations |
| Auth | NextAuth v5 middleware | Protects `/admin/*` & API routes |
| Payments | Server API + client Elements | Stripe/PayPal webhook handlers |
| Uploads | UploadThing FileRouter | Auth middleware + client dropzone |
| Realtime | WebSocket (ws) | Potential live sync |

---

## 4. Recommendations

1. **Prisma multi-file schema** — split `schema.prisma` as models grow (Prisma 6 feature).
2. **Database sessions** — switch from JWT if session invalidation becomes needed.
3. **`next/image` remote patterns** — optimize UploadThing images via WebP/AVIF.
4. **`useInfiniteQuery`** — for virtualized chapter list scrolling.
5. **Stripe Idempotency-Key** — safe webhook retry handling.
6. **Upstash Ratelimit** — configure for public API routes.

---

## 5. References

| Source | URL |
|--------|-----|
| Next.js 15 Architecture | patterns.dev/react/nextjs |
| Prisma 6 Release | prisma.io/blog/prisma-6 |
| NextAuth v5 + Prisma Guide | dev.to/whoffagents/nextauthjs-v5-prisma-postgresql |
| UploadThing App Router | docs.uploadthing.com/getting-started/appdir |
| Stripe vs PayPal SDK 2026 | pkgpulse.com/guides/stripe-react-vs-paypal-js-sdk-2026 |
| Prisma + Next.js Production | digitalapplied.com/blog/prisma-orm-production-guide-nextjs |
