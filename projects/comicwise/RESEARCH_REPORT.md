# RESEARCH_REPORT.md

## Project: comicwise

**Type:** Comic streaming / reader platform
**Tech Stack:** Next.js 15, React 19 Server Components, Prisma 7, PostgreSQL 17, NextAuth.js v5 (Auth.js), Tailwind CSS 4, shadcn/ui, Zustand, React Query 5 (TanStack Query), Zod 4, Stripe (Node.js SDK v17, API 2026-01-28), pnpm
**Status:** Active development / consolidation target

---

## Similar Projects

| Project | URL | Why Relevant |
|---------|-----|--------------|
| rhixe_scans | `projects/rhixe_scans` | Same comic reader surface area, shared auth + payments + Next.js readers |
| rhixecompany-comics | `projects/rhixecompany-comics` | Current consolidation target; inherits comic reader and DAL patterns |
| university-library-jsm | `projects/university-library-jsm` | Next.js 15 + Prisma + PostgreSQL academic library patterns |
| banking | `projects/banking` | Next.js + Prisma + Stripe subscription patterns |

---

## 2026 Key Findings

### Next.js 15 + React 19 Server Components
- **Async Request APIs are now mandatory**: `cookies()`, `headers()`, `draftMode()`, `params`, `searchParams` are all async in Next.js 15; codemod available via `npx @next/codemod@canary next-async-request-api .` [Next.js 15 Blog](https://nextjs.org/blog/next-15)
- **Caching defaults changed**: GET Route Handlers and Client Router Cache are **uncached by default** (`staleTime: 0`); opt-in with `dynamic = 'force-static'` or `experimental.staleTimes` config [Next.js 15 Blog](https://nextjs.org/blog/next-15)
- **Server Actions are the primary mutation pattern**: Use `'use server'` directive at module level for Client Components, inline for Server Components; integrate with Next.js cache/revalidation for single-roundtrip updates [Next.js Server Actions Docs](https://nextjs.org/docs/13/app/building-your-application/data-fetching/server-actions-and-mutations)
- **React 19 Compiler (experimental)**: Enable via `experimental: { reactCompiler: true }` in `next.config.ts` for automatic memoization, reducing `useMemo`/`useCallback` boilerplate [Next.js 15 Blog](https://nextjs.org/blog/next-15)
- **Turbopack Dev is stable**: `next dev --turbo` delivers 76.7% faster startup, 96.3% faster Fast Refresh, used in production at vercel.com/nextjs.org [Next.js 15 Blog](https://nextjs.org/blog/next-15)
- **`unstable_after` API**: Execute code after response finishes streaming for logging, analytics, sync; enable via `experimental: { after: true }` [Next.js 15 Blog](https://nextjs.org/blog/next-15)

### Prisma 7 + PostgreSQL 17 Performance
- **Prisma 7 architecture overhaul (Nov 2025)**: Rust query engine replaced with pure TypeScript runtime — **3x faster queries, 90% smaller bundles (~1.6 MB min+gzip), 70% faster TypeScript type checking** [Tech Insider Prisma 2026](https://tech-insider.org/prisma-orm-tutorial-typescript-postgres-13-steps-2026)
- **Generated client moves out of `node_modules`** to source directory; new `prisma.config.ts` for dynamic configuration; native mapped enums support [MakerKit Drizzle vs Prisma 2026](https://makerkit.dev/blog/tutorials/drizzle-vs-prisma)
- **Connection pooling critical for serverless/edge**: Use PgBouncer or Prisma Data Proxy; configure `connection_limit` in connection string for Prisma 7's improved pool handling [Tech Insider Prisma 2026](https://tech-insider.org/prisma-orm-tutorial-typescript-postgres-13-steps-2026)
- **Index strategy**: Add `@@index` on foreign keys (`user_id`, `comic_id`), composite indexes for query patterns (`user_id, chapter_id`), and `@@unique` on `Comic.slug` + `UserComic(user_id, comic_id)` to prevent duplicates [Dev.to Prisma vs Drizzle 2026](https://dev.to/pockit_tools/drizzle-orm-vs-prisma-in-2026-the-honest-comparison-nobody-is-making-3n6g)
- **Use `findMany` with `select`/`include` judiciously**: Avoid over-fetching; prefer Drizzle-style SQL query builder for complex joins, but Prisma's `include` with nested `where` is sufficient for most comic reader queries [Dev.to Prisma vs Drizzle 2026](https://dev.to/pockit_tools/drizzle-orm-vs-prisma-in-2026-the-honest-comparison-nobody-is-making-3n6g)
- **Migration workflow**: `prisma migrate dev` (timestamped folders) + shadow database required; seed via `tsx prisma/seed.ts` script [Tech Insider Prisma 2026](https://tech-insider.org/prisma-orm-tutorial-typescript-postgres-13-steps-2026)

### NextAuth.js v5 (Auth.js) + Database Sessions + Providers
- **Session callback runs client-side only in v5**: Server-side `session` callback is **not invoked**; workaround: use JWT strategy with `jwt` callback to embed custom claims (`orgId`, `defaultCurrency`), then expose via `session` callback [NextAuth v5 Discussion #8487](https://github.com/nextauthjs/next-auth/discussions/8487)
- **Middleware must use Node.js runtime for OAuth**: Edge runtime fails with `oidc-token-hash` (`process.version` access); configure `export const config = { runtime: 'nodejs' }` [NextAuth v5 Discussion #8487](https://github.com/nextauthjs/next-auth/discussions/8487)
- **Database sessions with credentials provider**: Community requests `session: { strategy: 'database' }` support for credentials; currently JWT is recommended path [NextAuth v5 Discussion #8487](https://github.com/nextauthjs/next-auth/discussions/8487)
- **Keycloak provider (built-in OIDC)**: Configure via `Keycloak({ clientId, clientSecret, issuer })`; **issuer must include realm** (e.g., `https://keycloak-domain.com/realms/My_Realm`); create confidential OpenID Connect client in Keycloak [NextAuth Keycloak Provider](https://github.com/nextauthjs/next-auth/blob/main/packages/core/src/providers/keycloak.ts)
- **Server Component auth pattern**: Use `const session = await auth()` (no req/res); redirect unauthenticated via `redirect('/api/auth/signin')` or directly to provider via middleware (see Discussion #4078) [NextAuth Discussion #9672](https://github.com/nextauthjs/next-auth/discussions/9672)
- **Reverse proxy / Cloud Run deployment**: Patch request URL origin in route handler to handle `localhost` vs public URL mismatch [NextAuth v5 Discussion #8487](https://github.com/nextauthjs/next-auth/discussions/8487)

### Stripe Subscriptions + Webhooks (Node.js SDK v17, API 2026-01-28)
- **Pin API version explicitly**: Current `2026-03-25.dahlia`; un-pinned integrations break silently on Stripe API updates [Cuebytes Stripe Subscriptions 2026](https://cuebytes.com/blog/stripe-subscriptions-implementation-guide)
- **Use Stripe Checkout (`mode=subscription`)** for 95% of SaaS: handles trials, Smart Retries, dunning emails, proration, 3DS, PCI compliance — never build custom payment forms unless Checkout cannot provide required UI [DigitalApplied Stripe 2026](https://www.digitalapplied.com/blog/stripe-payment-integration-developer-guide-2026)
- **Pass internal `userId` in BOTH `session` and `subscription` metadata** when creating Checkout session — Stripe does not auto-map subscriptions to your users; metadata required to link webhook events to DB [Cuebytes Stripe Subscriptions 2026](https://cuebytes.com/blog/stripe-subscriptions-implementation-guide)
- **NEVER grant access on success URL hit**: Users close tabs, refresh mid-transaction, or have flaky internet; **webhook is the source of truth** [Cuebytes Stripe Subscriptions 2026](https://cuebytes.com/blog/stripe-subscriptions-implementation-guide)
- **Critical webhook events to handle**:
  - `checkout.session.completed` → create subscription record, grant access
  - `customer.subscription.updated` → update status/plan in DB
  - `customer.subscription.trial_will_end` (3 days before) → send reminder
  - `invoice.payment_succeeded` → update `period_end`, send receipt
  - `invoice.payment_failed` → email user to update payment method
  - `customer.subscription.deleted` → revoke access, send confirmation [DigitalApplied Stripe 2026](https://www.digitalapplied.com/blog/stripe-payment-integration-developer-guide-2026)
- **Webhook handler non-negotiables**: (1) Verify HMAC signature via `stripe.webhooks.constructEvent(rawBody, sig, secret)` — **capture raw body before JSON parsing**; (2) Return 2xx within seconds (exponential backoff up to 72 hours); (3) Be idempotent (track processed event IDs with TTL); (4) Log all events for debugging [Hookdeck Stripe Webhooks 2026](https://hookdeck.com/webhooks/platforms/guide-to-stripe-webhooks-features-and-best-practices)
- **Stripe retries up to 3 days in live mode**, then disables endpoint; test mode has shorter window [Hookdeck Stripe Webhooks 2026](https://hookdeck.com/webhooks/platforms/guide-to-stripe-webhooks-features-and-best-practices)

### React Query 5 (TanStack Query) + Zustand Patterns
- **2026 Mental Model — 4 Layers of State**: (1) Local UI State (`useState`/`useReducer`) → modals, inputs; (2) Derived State (`useMemo`, selectors) → filtered lists; (3) Global Client State (Zustand/Redux Toolkit) → theme, auth user, cart; (4) Server State (TanStack Query) → API data, caching [C# Corner React State 2026](https://www.c-sharpcorner.com/article/state-management-in-react-2026-best-practices-tools-real-world-patterns)
- **Recommended stack for most apps**: TanStack Query + Zustand + URL State (`useSearchParams`) covers 95% of use cases without over-engineering [NextFuture React State 2026](https://nextfuture.io.vn/blog/ultimate-guide-react-state-management-2026)
- **Zustand advantages (1.2 KB gzipped)**: No providers, selector-based subscriptions (fine-grained re-renders), TypeScript-first, SSR-compatible, middleware support (`persist`, `devtools`), framework-agnostic [NextFuture React State 2026](https://nextfuture.io.vn/blog/ultimate-guide-react-state-management-2026)
- **React Query 5 for server state**: Automatic caching, background refetching, request deduplication, optimistic updates via `onMutate`/`onError`/`onSettled`; **never store API responses in Zustand/Redux** [C# Corner React State 2026](https://www.c-sharpcorner.com/article/state-management-in-react-2026-best-practices-tools-real-world-patterns)
- **Server Components shift data fetching to server**: Client components focus on interactions; client state becomes smaller/simpler — used primarily for UI transitions and optimistic updates [C# Corner React State 2026](https://www.c-sharpcorner.com/article/state-management-in-react-2026-best-practices-tools-real-world-patterns)
- **Form state**: Use React Hook Form + Zod (uncontrolled components = fewer re-renders, built-in validation) [NextFuture React State 2026](https://nextfuture.io.vn/blog/ultimate-guide-react-state-management-2026)
- **URL State for shareable state**: Filters, pagination, tabs, modals → `useSearchParams` + `router.push` for free persistence/shareability [NextFuture React State 2026](https://nextfuture.io.vn/blog/ultimate-guide-react-state-management-2026)

---

## Cheatsheets & Quick Reference

| Topic | Resource | Type |
|-------|----------|------|
| Next.js 15 App Router | https://nextjs.org/docs/app | Docs |
| Next.js 15 Breaking Changes | https://nextjs.org/blog/next-15 | Release Notes |
| Prisma 7 Tutorial (2026) | https://tech-insider.org/prisma-orm-tutorial-typescript-postgres-13-steps-2026 | Tutorial |
| Drizzle vs Prisma 2026 | https://makerkit.dev/blog/tutorials/drizzle-vs-prisma | Comparison |
| NextAuth.js v5 (Auth.js) | https://authjs.dev | Auth Guide |
| NextAuth v5 Discussion | https://github.com/nextauthjs/next-auth/discussions/8487 | Community |
| Keycloak Provider | https://github.com/nextauthjs/next-auth/blob/main/packages/core/src/providers/keycloak.ts | Source |
| Stripe Node.js SDK v17 | https://github.com/stripe/stripe-node | SDK |
| Stripe Webhooks Guide | https://hookdeck.com/webhooks/platforms/guide-to-stripe-webhooks-features-and-best-practices | Guide |
| TanStack Query v5 | https://tanstack.com/query/latest | Docs |
| Zustand | https://github.com/pmndrs/zustand | Repo |
| React State Management 2026 | https://nextfuture.io.vn/blog/ultimate-guide-react-state-management-2026 | Guide |

---

## Best Practices (2026 Update)

1. **RSC chapter pages** — Render chapter imagery and metadata server-side; only reader interactions (drag, bookmark, progress) need hydration via `'use client'`
2. **Server Actions for mutations** — Define at module level (`'use server'`) in `actions/` directory; use `useFormState` + Zod for validation; revalidate via `revalidatePath`/`revalidateTag` after mutation
3. **Prisma 7 DAL boundaries** — Keep Prisma access behind `dal/*` modules; use `select`/`include` precisely; add `@@index` on FKs and composite unique constraints
4. **Zod as boundary contract** — Validate all form payloads before Server Actions and before Zod→Prisma inserts; reuse schemas for client/server
5. **Revalidation tags + React Query** — Use `revalidateTag` in Server Actions + React Query `queryClient.invalidateQueries` for list updates after mutations
6. **Stripe webhook idempotency** — Track processed `event.id` with TTL (e.g., Redis/Upstash); verify signature with raw body; return 2xx fast
7. **NextAuth v5 JWT strategy** — Embed custom claims in `jwt` callback; expose via `session` callback; use `auth()` in Server Components, `useSession()` in Client Components
8. **Test gates** — Keep `lint + typecheck + unit + e2e` green in single `validate` script; Playwright with route interception for sub-3-min suites
9. **URL State for filters/pagination** — Use `useSearchParams` + `router.push` for shareable, persistent comic catalog state

---

## Common Pitfalls (2026 Update)

| Pitfall | Impact | Avoidance |
|---------|--------|-----------|
| Treating server data as client state | Duplicate sync, stale data, memory pressure | Use TanStack Query for ALL API data; Zustand only for UI state (theme, auth, cart) |
| Storing API responses in Zustand/Redux | Sync issues, cache invalidation complexity | Server state → React Query; Client state → Zustand |
| Updating Stripe state from client/success URL | Payment fraud, revenue leak, access granted without payment | **Only** transition subscription state in verified webhook handlers |
| Skipping webhook signature verification | Spoofed events grant free access | `stripe.webhooks.constructEvent(rawBody, sig, secret)` — capture raw body first |
| NextAuth v5 Edge middleware with OAuth | `oidc-token-hash` crashes (`process.version`) | `export const config = { runtime: 'nodejs' }` in middleware |
| NextAuth v5 server-side `session` callback | Custom claims (orgId, roles) missing from session | Use JWT strategy: embed in `jwt` callback, expose in `session` callback |
| Missing `@@index` on FK columns | Slow chapter/page queries at scale | Add `@@index([userId])`, `@@index([comicId])`, `@@unique([userId, comicId])` |
| Client-only pagination on huge catalogs | Memory/perf issues, hydration waterfalls | Server Components with cursor-based pagination; defer client hydrate |
| Overusing React Context for state | Unnecessary re-renders (all consumers update) | Split contexts by update frequency; memoize values; use Zustand for frequent updates |
| Unpinned Stripe API version | Silent breakage on Stripe API updates | Pin to `2026-03-25.dahlia` (or current) in Stripe SDK init |

---

## Performance (2026 Update)

1. **`next/image` with automatic loader** for catalog artwork; reserve large chapter image optimization for CDN flow (signed URLs/short-lived tokens)
2. **Cache static comic metadata** with Next.js 15 `use cache` (experimental) or `force-static` + `revalidateTag` on webhook events
3. **Avoid client-side joins** of review/comment objects; aggregate in DAL with Prisma `include` + nested `where` or raw SQL for complex aggregations
4. **Prisma connection pooling**: Configure `connection_limit` in `DATABASE_URL`; use PgBouncer for serverless; enable `prisma postgres link` for managed pooling
5. **React Query `staleTime` tuning**: Set `staleTime: 30_000`–`60_000` for comic catalog; `staleTime: 5_000` for real-time progress; use `persistQueryClient` for offline support
6. **Zustand `persist` middleware** for cart/reading preferences; avoid large objects in persisted state (hydration cost)
7. **Playwright tests**: Use route interception + fast fixtures; target sub-3-minute full suite; test webhook handlers with Stripe CLI trigger
8. **Turbopack Dev** (`next dev --turbo`) for 76.7% faster startup, 96.3% faster Fast Refresh in development

---

## Security (2026 Update)

1. **Validate all image paths and reader URLs** before storage; never trust raw user uploads; use signed URLs or short-lived tokens for chapter images
2. **Strip HTML tags from review/comment bodies** before DB writes, even with CKEditor sanitization on client side
3. **Store Stripe and auth secrets only in `.env.local`** — never scaffold into example env files; use different keys per environment
4. **RBAC checks must stay server-side** — never gate protected routes purely with client redirects; use `auth()` in Server Components / middleware
5. **Stripe webhook signature verification is mandatory** — capture raw request body BEFORE any JSON parsing; verify via SDK
6. **NextAuth v5: use `NEXTAUTH_URL` and `AUTH_SECRET`** in production; patch request origin behind reverse proxies (Cloud Run, etc.)
7. **Prisma: enable `preventCrossSiteRequestForgery` equivalent** — validate CSRF on Server Actions via `origin` header check or same-site cookies
8. **Keycloak: enforce confidential client type**; validate `issuer` includes realm; map `email_verified` claim to user verification status
9. **Content Security Policy**: Configure `next.config.ts` headers for `script-src`, `img-src` (CDN domains), `frame-src` (Stripe Checkout)

---

## Related Projects (in workspace)

- **rhixe_scans** — comic reader sibling with shared Stripe and NextAuth flows
- **rhixecompany-comics** — consolidation target inheriting ComicWise frontend and reader patterns
- **university-library-jsm** — Next.js 15 + Prisma + PostgreSQL academic patterns
- **banking** — Next.js + Prisma + Stripe subscription patterns
- **comicwise** — should be marked as consolidation source in disposal reports

---

## Resources

| Resource | URL | Description |
|----------|-----|-------------|
| Next.js 15 Blog | https://nextjs.org/blog/next-15 | Official release notes + breaking changes |
| Next.js Server Actions | https://nextjs.org/docs/13/app/building-your-application/data-fetching/server-actions-and-mutations | Server Actions guide |
| Prisma 7 Tutorial 2026 | https://tech-insider.org/prisma-orm-tutorial-typescript-postgres-13-steps-2026 | 13-step production tutorial |
| Prisma vs Drizzle 2026 | https://makerkit.dev/blog/tutorials/drizzle-vs-prisma | Practical comparison |
| Prisma vs Drizzle Deep Dive | https://dev.to/pockit_tools/drizzle-orm-vs-prisma-in-2026-the-honest-comparison-nobody-is-making-3n6g | Honest comparison |
| NextAuth v5 Discussion | https://github.com/nextauthjs/next-auth/discussions/8487 | Community issues + solutions |
| NextAuth Keycloak Provider | https://github.com/nextauthjs/next-auth/blob/main/packages/core/src/providers/keycloak.ts | Built-in provider source |
| NextAuth Redirect to Provider | https://github.com/nextauthjs/next-auth/discussions/9672 | Server Component redirect pattern |
| Stripe Dev Guide 2026 | https://www.digitalapplied.com/blog/stripe-payment-integration-developer-guide-2026 | Complete integration guide |
| Stripe Subscriptions 2026 | https://cuebytes.com/blog/stripe-subscriptions-implementation-guide | Step-by-step production guide |
| Stripe Webhooks Best Practices | https://hookdeck.com/webhooks/platforms/guide-to-stripe-webhooks-features-and-best-practices | Webhook reliability guide |
| React State Management 2026 | https://www.c-sharpcorner.com/article/state-management-in-react-2026-best-practices-tools-real-world-patterns | 4-layer mental model |
| React State Ultimate Guide | https://nextfuture.io.vn/blog/ultimate-guide-react-state-management-2026 | Tool decision framework |
| shadcn/ui | https://ui.shadcn.com | Component system |
| Tailwind CSS 4 | https://tailwindcss.com | Utility-first CSS |
| Zod 4 | https://zod.dev | Schema validation |