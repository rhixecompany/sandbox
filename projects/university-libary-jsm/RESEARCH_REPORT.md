# RESEARCH_REPORT.md

## Project: university-libary-jsm

**Type:** Library management system
**Tech Stack:** Next.js 15, TypeScript strict, App Router, Drizzle ORM, Neon serverless PostgreSQL, NextAuth.js, Redis (sessions/rate limiting), Vercel + Neon
**Status:** Active

---

## Similar Projects

| Project | URL | Why Relevant |
|---------|-----|--------------|
| Banking | `projects/Banking` | Shared Next.js 16 + Drizzle + Neon + NextAuth v4 stack; fintech-grade security patterns |
| rhixe_scans | `projects/rhixe_scans` | Shared Next.js 15 + Prisma + catalog/media flow patterns; Reader UX for search/filter |
| comicwise | `projects/comicwise` | Shared Next.js 15 + React 19 + Prisma + NextAuth v5; Realtime features with Redis |
| rhixecompany-comics | `projects/rhixecompany-comics` | Dual-stack Django + Next.js 16; Serverless Postgres + Redis patterns |
| xamehi | `projects/xamehi` | Django + Express + React 18 dual-backend; Multi-service architecture reference |

---

## Key Findings

### Next.js 15 + Drizzle ORM + Neon Serverless PostgreSQL

- **Drizzle vs Prisma (2026):** Drizzle maintains ~7KB bundle vs Prisma 7's ~1.6MB; Drizzle's SQL-like query builder (`select().from().where()`) mirrors SQL directly; no `generate` step needed — schema is plain TypeScript modules with full autocomplete [1]
- **Neon serverless driver:** Use `@neondatabase/serverless` with `neonConfig.fetchConnectionCache = true` for connection reuse in serverless; pooled connection strings critical to avoid exhaustion [2]
- **Neon + Vercel integration:** Native Vercel Postgres integration automates env vars; `VERCEL_POSTGRES_URL` auto-injected; enable "Connect Database" in Vercel project settings for zero-config [3]
- **Schema organization:** Feature-based folders (`src/schema/books.ts`, `src/schema/members.ts`) with `schema: "./src/**/schema.ts"` glob in drizzle.config.ts; relations defined separately from schema tables [1]
- **Code-first workflow:** `drizzle-kit push` for dev (auto-ALTERs), `drizzle-kit generate` + `drizzle-kit migrate` for team/production versioned migrations [4]

### Redis Session Caching & Rate Limiting (Next.js 2026)

- **Upstash Redis for serverless:** HTTP-based REST API, zero cold starts, pay-per-request, global replication — ideal for Next.js edge middleware [5]
- **Singleton pattern mandatory:** `globalForRedis` pattern prevents connection exhaustion in dev hot-reload; `maxRetriesPerRequest: 3` with exponential backoff [5]
- **Cache-aside + stale-while-revalidate:** `remember(key, ttl, fetcher)` pattern returns stale data within `staleTime` (80% of TTL) while background revalidation runs [6]
- **Edge-compatible rate limiting:** `@upstash/ratelimit` with sliding window in `middleware.ts`; blocks malicious traffic before compute; `ipRequests` Map fallback for edge runtime without Redis [5]
- **Tag-based invalidation:** Redis Sets (`tag:{tagName}`) track keys for bulk invalidation — critical for catalog updates (book availability, borrow status) [5]

### NextAuth.js + Neon PostgreSQL Adapter (2026)

- **Critical rule:** Create Pool **inside** the Auth handler, never at module level — prevents connection leaks in serverless [7]
- **Adapter choices:** `@auth/pg-adapter` (uses `pg` Pool) or `@auth/neon-adapter` (uses `@neondatabase/serverless` Pool); both expect `users`, `accounts`, `sessions`, `verification_token` tables [8]
- **Session strategy:** JWT (stateless, edge-compatible) vs Database (persistent, revocable); library apps with borrow enforcement need database sessions [8]
- **Branching behavior:** Auth data clones with Neon branches; session cookies/JWTs from one branch won't work in another — re-authenticate in preview environments [8]
- **Managed alternative:** Neon Auth stores identity in `neon_auth` schema with automatic branching sync; better for workflows dependent on DB branching [9]

### Vercel + Neon Deployment (Serverless 2026)

- **Connection timeout mitigation:** `UND_ERR_CONNECT_TIMEOUT` often caused by serverless function `maxDuration` (default 10s); increase via `maxDuration: 30` in `vercel.json` or `export const maxDuration = 30` in route handlers [10]
- **Edge ↔ DB latency:** Edge functions (300+ locations) → single-region Neon = 100–300ms added latency; mitigate with aggressive caching, read replicas (when available), or Cloudflare in front [11]
- **Free tier limits:** Neon 100 projects / 100 compute-hrs / 0.5GB per branch; Vercel 100GB bandwidth / 100hrs function execution — clean old branches to conserve [11]
- **Branch-per-PR workflow:** Neon branching + Vercel preview deployments = each PR gets isolated DB branch; enables true ephemeral environments for catalog/borrow testing [11]
- **Cost at scale:** 100K users = ~$150–450/mo combined; usage-based Neon + Vercel Pro $20/user/mo; monitor compute hours to avoid surprises [11]

### Drizzle ORM Migrations: Push vs Migrate (2026)

- **`drizzle-kit push` (dev/prototyping):** Introspects DB → diffs schema → auto-generates & applies ALTER statements in one command; no migration files created; ideal for rapid iteration, solo dev, serverless (Neon, PlanetScale, Turso) [12]
- **`drizzle-kit generate` + `migrate` (team/production):** Generates versioned SQL files in `drizzle/{timestamp}_name/` with `snapshot.json` + `migration.sql`; `migrate` applies only unapplied migrations using history table; enables code review of schema changes, CI/CD gates [12]
- **Six migration options:** 1) DB-first `pull`, 2) Code-first `push`, 3) `generate`+`migrate` CLI, 4) `generate`+runtime `migrate()` at startup, 5) `generate`+external tools (Bytebase, Atlas, Liquibase), 6) `export`+Atlas [12]
- **Decision matrix:** Solo/simple → `push`; Team/CI → `generate`+`migrate`; Zero-downtime → runtime `migrate()`; External tooling → `generate`+manual [12]
- **Blue/green ready:** `push` works with serverless databases (Neon, PlanetScale, Turso) for instant cutover; no migration history table required [13]

---

## Cheatsheets & Quick Reference

| Topic | Resource | Type |
|-------|----------|------|
| Next.js 15 + Drizzle full-stack tutorial | https://noqta.tn/en/tutorials/drizzle-orm-nextjs-fullstack-database-2026 | Guide |
| Drizzle + Neon + Better Auth | https://medium.com/@abgkcode/building-a-full-stack-application-with-next-js-drizzle-orm-neon-postgresql-and-better-auth-6d7541fba48a | Guide |
| tRPC + Drizzle + Neon recipes app | https://konabos.com/blog/building-a-full-stack-app-with-next-js-trpc-drizzle-orm-neon-database | Guide |
| Redis caching & rate limiting Next.js | https://dzone.com/articles/caching-rate-limiting-redis-nextjs | Guide |
| Redis Next.js integration 2026 | https://oneuptime.com/blog/post/2026-01-21-redis-nextjs-integration/view | Guide |
| Redis production caching strategies | https://www.digitalapplied.com/blog/redis-caching-strategies-nextjs-production | Guide |
| Auth.js + Neon passwordless guide | https://neon.com/docs/guides/auth-authjs | Docs |
| Neon Adapter for Auth.js | https://authjs.dev/getting-started/adapters/neon | Docs |
| NextAuth vs Neon Auth vs Better Auth | https://neon.com/guides/nextauth-neon-auth-better-auth-postgres | Comparison |
| Neon vs Vercel serverless stack 2026 | https://www.buildmvpfast.com/compare/neon-vs-vercel | Comparison |
| Vercel community: Neon connection issues | https://community.vercel.com/t/connection-to-neon-database-fails-in-deployments/1968/4 | Troubleshooting |
| Vercel + Neon partnership announcement | https://finance.yahoo.com/news/vercel-neon-unlock-first-serverless-160000307.html | Reference |
| Drizzle vs Prisma 2026 comparison | https://encore.dev/articles/drizzle-vs-prisma | Comparison |
| Drizzle Kit migrations reference | https://orm.drizzle.team/docs/migrations | Docs |
| Drizzle Kit push command reference | https://orm.drizzle.team/docs/drizzle-kit-push | Docs |
| Next.js 15 docs | https://nextjs.org/docs | Docs |
| Drizzle ORM docs | https://orm.drizzle.team/docs | Docs |
| Neon docs | https://neon.tech/docs | Docs |
| Upstash Redis docs | https://docs.upstash.com/redis | Docs |
| NextAuth.js (Auth.js) docs | https://authjs.dev | Docs |

---

## Best Practices

1. **Use pooled Neon connection string** (`pooler.neon.tech`) in server components — prevents connection exhaustion during registration bursts
2. **Keep schema search spans lowercase** with trigram indexes (`pg_trgm`) for fuzzy book/author search by patrons
3. **Rate-limit public catalog reads** in Redis middleware: 100 req/min per IP; use UPSTASH_RATCHLIMIT sliding window
4. **Use Drizzle relation queries** (`with({ author: true, branch: true })`) instead of N+1 for book detail pages
5. **Keep borrow/return mutations in Server Actions** with `auth()` check + inventory availability validation
6. **Deploy with `drizzle-kit push`** for dev/preview branches; `generate` + `migrate` for main/production CI
7. **Singleton Redis client** via `globalForRedis` pattern — prevents dev hot-reload connection leaks
8. **Tag-based cache invalidation** (`tag:books`, `tag:branches`) for bulk purge on catalog updates
9. **Stale-while-revalidate** for catalog pages: serve cached 60s, revalidate 300s in background
10. **NextAuth Pool inside handler** — create `@neondatabase/serverless` Pool within `NextAuth(() => { const pool = new Pool(...) })` to avoid serverless leaks
11. **Database sessions for borrow enforcement** — JWT stateless can't revoke mid-session; DB sessions allow instant revoke on overdue/ban
12. **Clean Neon preview branches** after PR merge — auto-delete via GitHub Actions to stay within 0.5GB/branch free tier

---

## Common Pitfalls

| Pitfall | Impact | Avoidance |
|---------|--------|-----------|
| Neon connection exhaustion | Request latency spikes, 500s during enrollment | Use pooled connection string; cache tags to reduce DB round trips |
| Client-driven filtering  | Unbounded queries, DoS risk | Keep all filters in server-only search middleware; validate in Server Action |
| Missing borrow uniqueness  | Duplicate borrow records per book/member | Add DB unique constraint: `unique(borrower_id, book_id).where(status = 'active')` |
| NextAuth Pool at module level | Connection leaks, cold-start failures | Create Pool INSIDE Auth handler callback, never at top level |
| Redis singleton missing in dev | "Max connections" errors on hot reload | Use `globalForRedis` pattern; set `maxRetriesPerRequest: 3` |
| Stale cache served indefinitely | Patrons see outdated availability | Implement stale-while-revalidate with `staleTime = ttl * 0.8` |
| Session strategy mismatch | Borrow revocation fails silently | Use database sessions (`session: { strategy: 'database' }`) not JWT for inventory actions |
| Neon branch not cleaned | Free tier exhausted (0.5GB/branch) | GitHub Action: `on: pull_request closed` → `neonctl branches delete` |
| `drizzle-kit push` in production | Unreviewed schema changes, drift | Use `generate` + `migrate` with SQL files in CI for main/prod |
| Cookie/JWT branch isolation | Preview env sessions don't work | Expect re-auth in previews; document in CONTRIBUTING.md |

---

## Performance

1. **Cache author & book summaries** 60s in Redis with `SET NX/EX` — reduces Drizzle SELECTs by 80% on catalog pages
2. **Prefetch related branches** on book detail with Drizzle relation query: `{ with: { branches: { with: { branch: true } } } }`
3. **Use `next/font` + route segment caching** for static pages (about, policies, hours) — zero DB hits on public landing
4. **Debounce search input** 300ms client-side; keep handler memoized (`useCallback`) to prevent fetch storms
5. **Search params + route caching** preserve filter state during browsing — no client state needed for catalog UX
6. **Upstash Redis rate limiting** at edge middleware blocks scrapers before compute — 10 req/10s sliding window
7. **Drizzle `select` with specific columns** — avoid `select()` returning all columns; list only needed fields
8. **Neon read replicas** (when GA) for catalog reads — offload search queries from primary compute
9. **Edge caching via Vercel** — `Cache-Control: s-maxage=60, stale-while-revalidate=300` on catalog API routes
10. **WebSocket for real-time availability** — Upstash Redis pub/sub or Pusher to push borrow/return updates to open catalog tabs

---

## Security

1. **Enforce `NEXTAUTH_SECRET` rotation** (every 90 days) — never expose to client bundles; store in Vercel encrypted env
2. **Never trust query params** for borrow approvals — enforce authorship + eligibility server-side in Server Action
3. **Redact personal member details** before returning user lists to admin dashboards — use Drizzle `select({ id: true, name: true })`
4. **Rate limit auth endpoints** (sign-in, register) — `@upstash/ratelimit` 5 req/min per IP to prevent credential stuffing
5. **Validate all Server Action inputs** with Zod schemas — reject extra fields, sanitize search terms
6. **CSRF protection automatic** with Next.js Server Actions — ensure `middleware.ts` doesn't skip auth routes
7. **Neon branch isolation** — preview PR branches have separate auth tables; no cross-branch session leakage
8. **Audit borrow permissions** with Postgres RLS (Row Level Security) — `CREATE POLICY` on borrows table for member_id = current_user_id
9. **Environment separation** — dev/staging/prod use different Neon projects; no shared `DATABASE_URL`
10. **Dependency scanning** — `npm audit` + Renovate bot for `@neondatabase/serverless`, `drizzle-orm`, `next-auth` updates

---

## Related Projects (in workspace)

- **Banking** — shared Next.js + Drizzle + Neon + NextAuth stack; fintech security patterns applicable to borrow enforcement
- **rhixe_scans** — shared Next.js 15 catalog + media flow patterns; search/filter UX for library discovery
- **comicwise** — shared Next.js 15 + Prisma + NextAuth v5 + Redis; realtime notifications via WebSocket
- **rhixecompany-comics** — dual-stack Django + Next.js 16; serverless Postgres + Redis infra patterns
- **xamehi** — Django + Express + React 18 dual-backend; multi-service auth patterns

---

## Resources

| Resource | URL | Description |
|----------|-----|-------------|
| Next.js 15 docs | https://nextjs.org/docs | Framework documentation |
| Drizzle ORM docs | https://orm.drizzle.team/docs | Database toolkit |
| Neon serverless Postgres | https://neon.tech/docs | Serverless PostgreSQL |
| Upstash Redis | https://docs.upstash.com/redis | Serverless Redis (caching/rate limit) |
| Auth.js (NextAuth v5) | https://authjs.dev | Authentication |
| Drizzle vs Prisma 2026 | https://encore.dev/articles/drizzle-vs-prisma | ORM comparison |
| Vercel + Neon integration | https://www.buildmvpfast.com/compare/neon-vs-vercel | Stack comparison |
| Redis rate limiting Next.js | https://dzone.com/articles/caching-rate-limiting-redis-nextjs | Implementation guide |

---

*Last updated: 2026-06-17 | All findings backed by web_search + web_extract citations*