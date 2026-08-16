# Comicwise Stack Research Reference

**Project:** comicwise - Comic Streaming Platform  
**Stack:** Next.js 16 + React 19 + TypeScript 5.9 + Drizzle/Prisma + Stripe + NextAuth v5 + WebAuthn + ImageKit/Cloudinary + BullMQ/Upstash + Sentry + Zustand/TanStack Query + shadcn/ui + Framer Motion + pnpm

## Research Queries (13 executed)

1. `comicwise Next.js comic streaming platform`
2. `Next.js 16 Prisma Drizzle ORM migration guide best practices`
3. `NextAuth v5 beta WebAuthn passkeys implementation guide`
4. `Next.js Stripe subscriptions webhooks best practices 2024`
5. `BullMQ Upstash Redis QStash best practices`
6. `ImageKit Cloudinary Next.js image optimization best practices`
7. `Sentry Next.js 15 monitoring error tracking best practices`
8. `TanStack Query 5 Next.js 15 App Router best practices`
9. `Zustand 5 state management Next.js 15 best practices`
10. `Next.js 16 React 19 App Router new features 2025`
11. `Radix UI shadcn/ui Next.js 15 best practices`
12. `Resend React Email Next.js email templates best practices`
13. `Framer Motion Next.js 15 animations best practices performance`

## Key Findings Summary

### Next.js 16 / React 19 / App Router
- **Cache Components** (PPR + `use cache`) for instant navigation
- **Turbopack stable**: 5-10x faster Fast Refresh, 2-5x builds
- **Next.js Devtools MCP** for AI-assisted debugging
- React 19 RC in Next.js 15+, stable in 16

### Prisma / Drizzle Migration
- Prisma: schema-first, Accelerate for serverless pooling
- Drizzle: code-first, SQL-like, smaller bundles, faster cold starts
- Strategy: run both side-by-side, migrate incrementally
- Prisma singleton with `globalThis` prevents pool exhaustion

### NextAuth v5 + WebAuthn (⚠️ Experimental)
- Passkey provider experimental - not production-ready
- Requires `@simplewebauthn/browser@9.0.1` + `@simplewebauthn/server@9.0.3`
- DB adapter must be edge-compatible (Next.js <16)
- Hanko wrapper available: `@teamhanko/passkeys-next-auth-provider`
- **Recommendation**: Evaluate Clerk/Auth0 for production passkeys

### Stripe Subscriptions + Webhooks
- Checkout Sessions for sign-up flow
- Critical webhooks: `customer.subscription.*`, `invoice.payment_*`
- Stripe CLI for local testing: `stripe listen --forward-to localhost:3000/api/webhooks/stripe`
- Server Actions for checkout creation in App Router
- Idempotency with `stripe-event-id` deduplication

### BullMQ + Upstash Redis + QStash
- BullMQ needs managed Redis (Upstash compatible)
- QStash: serverless alternative, pay-per-use
- Fixed Upstash plans recommended for BullMQ workloads
- Separate Redis instances for queues vs caching
- QStash for scheduled/retryable, BullMQ for high-throughput

### ImageKit + Cloudinary Optimization
- `next/image` custom loaders for both
- ImageKit: AVIF, smart cropping, AI-powered DAM
- Blur placeholders: `placeholder="blur"` + `blurDataURL`
- Smart cropping for comic panels (face/region detection)
- Pre-generate blur placeholders at build time

### Sentry Monitoring
- SDK v8+ instruments App Router, Server Components, Server Actions, Edge
- Vercel drains for platform logs + distributed traces
- `tracesSampleRate`: 10-20% in production
- Separate client/server/edge configs
- Scrub PII with `beforeSend`

### TanStack Query 5 + App Router
- Hydration: `dehydrate()` in RSC → `HydrationBoundary` in Client
- Prefetch on server, hydrate on client = zero-waterfall
- `queryKey` factories for consistent invalidation
- Use for client state; Server Components for initial data

### Zustand 5 + Next.js 15
- **Critical**: No global stores - create per-request for SSR
- RSC cannot read/write Zustand (no hooks in RSC)
- Context to initialize store per-request in App Router
- Module-state works with Next.js aggressive caching

### shadcn/ui + Radix + React 19
- Copy-paste components (not npm) = full ownership
- React 19 RC in Next.js 15, stable in 16
- `--legacy-peer-deps` for non-React-19-ready packages
- Structure: `/components/ui` + `/components/forms` + `/components/modals`

### Resend + React Email
- Server Actions (`'use server'`) for sending in App Router
- Domain verification required for production
- `/emails` folder with React Email components
- `@react-email/components` for pre-built responsive components

### Framer Motion + Next.js 15
- Requires `'use client'` → client-rendered
- Dev SSR issue: animations don't play on first load
- Wrap animated sections in Client Components, content in RSC
- CSS animations for simple transitions (smaller bundle)
- Lazy load: `dynamic(() => import('./Animated'), { ssr: false })`

## High-Priority Recommendations

1. **NextAuth v5 Passkeys**: Experimental → evaluate Clerk/Auth0 for production
2. **Prisma/Drizzle**: Complete migration or standardize
3. **Webhook Testing**: Stripe CLI + ngrok for local development

## Source Files Generated

- `research-report.json` — Full structured findings (23KB)
- `RESEARCH_REPORT.md` — Human-readable markdown report (14.7KB)

## Template Used

Followed `references/comprehensive-tech-stack-research.md` pattern: per-technology subsections with Best Practices / Common Pitfalls / Performance Tips / Security Tips.

---

*Generated: July 25, 2026 via web-research-pipeline skill*