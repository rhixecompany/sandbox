# Verified 2026 Framework Facts (July 2026)

All confirmed via Tavily search + web_extract in July 2026.

## Next.js 16

- **16.2 (March 2026)**: Turbopack default (2-5× faster prod builds, ~400% faster dev startup, 10× Fast Refresh). `proxy.ts` replaces `middleware.ts`. Build Adapters API stable (OpenNext, Cloudflare, Amplify). `"use cache"` directive; `revalidateTag('key', 'max')` in 16.2. Server Fast Refresh (fine-grained server-side HMR).
- **May 2026 security release**: 13 advisories patched (DoS, middleware/proxy bypass, SSRF, cache poisoning, XSS, CVE-2026-23870). Upgrade to 16.2.6+.
- **Partial Prerendering (PPR)**: static shell + streamed dynamic content.
- **React Compiler, Server Actions, `use()` hook**: all production-stable.

## Drizzle ORM 0.45

- ~55KB bundle (min+gzip ~12KB) vs Prisma 7's ~1.6MB — critical for serverless cold starts.
- Prepared statements: `db.select().prepare("name")` precompiles SQL.
- Driver per platform: `neon-http` for edge, `node-postgres` for traditional servers.
- **Never `db push` in production** — use `generate` + `migrate`. `strict: true` catches column renames.
- Migration audit: review generated SQL before applying. No built-in rollback.

## Auth.js v5 (NextAuth v5)

- Stable since 2025. Clean server/client API split. `@auth/drizzle-adapter` supports custom table references.
- Database sessions recommended for systems needing revocation (library, fintech). JWT for stateless.
- Credentials provider caveat: known orphaned-token bug with database session strategy. Use OAuth or JWT strategy for credentials flow.

## Stripe (2026)

- Embedded Checkout promoted (iframe/web-component, users stay on-domain).
- Webhooks: `req.text()` (never `req.json()`), `constructEvent()` with secret, return 200 fast, process async.
- Events: `checkout.session.completed`, `customer.subscription.updated/deleted`, `invoice.payment_failed`.
- Webhooks require Route Handlers (not Server Actions) — static URL for Stripe to ping.

## Prisma 6/7

- Prisma 6: global singleton on `globalThis`, `connection_limit` + `pool_timeout` in URL, PgBouncer for serverless. Dual connection strings: `DATABASE_URL` (pooled) + `DATABASE_DIRECT_URL` (migrations).
- Prisma 7: TypeScript-only engine (dropped Rust binary), ~1.6MB bundle, 3× faster queries claimed. Accelerate for production pooling ($49/mo Starter, free tier available).

## Neon (Serverless PostgreSQL)

- HTTP driver (`@neondatabase/serverless` + `drizzle-orm/neon-http`): zero cold start, ideal for Vercel Edge.
- WebSocket driver for long-running processes (QStash workers).
- Built-in PgBouncer pooling. Branches for preview deployments (copy-on-write, seconds).
- Free tier: 0.5GB storage, 10 branches, 100 compute hrs/month.

## Plaid + Dwolla

- Dedicated Plaid service layer: single boundary for token exchange, webhooks.
- Event-driven pipeline: webhooks feed background workers. Reconciliation jobs catch silent failures.
- Idempotency: `Idempotency-Key` header + DB constraint prevents duplicate ACH transfers.
- Sandbox → Production Trial → Production: never skip Trial.

## Celery + Redis

- Critical: `task_acks_late=True`, `task_reject_on_worker_lost=True`, `worker_prefetch_multiplier=1`.
- Queue separation: dedicated queues for high-priority vs bulk scraping.
- `django-celery-beat` for DB-backed periodic scheduling.
