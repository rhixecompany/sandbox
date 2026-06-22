## Project: university-libary-jsm
**Type:** Library management system
**Tech Stack:** Next.js 15, TypeScript strict, App Router, Drizzle ORM, Neon serverless PostgreSQL, NextAuth.js, Redis (sessions/rate limiting), Vercel + Neon
**Status:** Active

## Similar Projects
| Project | URL | Why Relevant |
|---------|-----|--------------|
| Banking | `projects/Banking` | Shared Next.js 16 + Drizzle + Neon + NextAuth v4 stack; fintech-grade security patterns |
| rhixe_scans | `projects/rhixe_scans` | Shared Next.js 15 + Prisma + catalog/media flow patterns; Reader UX for search/filter |
| comicwise | `projects/comicwise` | Shared Next.js 15 + React 19 + Prisma + NextAuth v5; Realtime features with Redis |
| rhixecompany-comics | `projects/rhixecompany-comics` | Dual-stack Django + Next.js 16; Serverless Postgres + Redis patterns |

## Key Findings
### Next.js 15 + Drizzle ORM + Neon Serverless PostgreSQL
- **Drizzle vs Prisma (2026):** Drizzle maintains ~7KB bundle vs Prisma 7's ~1.6MB; Drizzle's SQL-like query builder (`select().from().where()`) mirrors SQL directly; no `generate` step needed — schema is plain TypeScript modules with full autocomplete [1]
- **Neon serverless driver:** Use `@neondatabase/serverless` with `neonConfig.fetchConnectionCache = true` for connection reuse in serverless; pooled connection strings critical to avoid exhaustion [2]
- **Neon + Vercel integration:** Native Vercel Postgres integration automates env vars; `VERCEL_POSTGRES_URL` auto-injected; enable "Connect Database" in Vercel project settings for zero-config [3]
- **Schema organization:** Feature-based folders (`src/schema/books.ts`, `src/schema/members.ts`) with `schema: "./src/**/schema.ts"` glob in drizzle.config.ts; relations defined separately from schema tables [1]
- **Code-first workflow:** `drizzle-kit push` for dev (auto-ALTERs), `drizzle-kit generate` + `drizzle-kit migrate` for team/production versioned migrations [4]
### Redis Session Caching & Rate Limiting (Next.js 2026)
- **Upstash Redis for serverless:** HTTP-based REST API, zero cold starts, pay-per-request, global replication — ideal for Next.js edge middleware [5]

## Cheatsheets & Quick Reference
| Topic | Resource | Type |
|-------|----------|------|
| Next.js 15 + Drizzle full-stack tutorial | https://noqta.tn/en/tutorials/drizzle-orm-nextjs-fullstack-database-2026 | Guide |

## Best Practices
1. **Use pooled Neon connection string** (`pooler.neon.tech`) in server components — prevents connection exhaustion during registration bursts
2. **Keep schema search spans lowercase** with trigram indexes (`pg_trgm`) for fuzzy book/author search by patrons
3. **Rate-limit public catalog reads** in Redis middleware: 100 req/min per IP; use UPSTASH_RATCHLIMIT sliding window

## Common Pitfalls
| Pitfall | Impact | Avoidance |
|---------|--------|-----------|
| Neon connection exhaustion | Request latency spikes, 500s during enrollment | Use pooled connection string; cache tags to reduce DB round trips |

## Performance
1. **Cache author & book summaries** 60s in Redis with `SET NX/EX` — reduces Drizzle SELECTs by 80% on catalog pages
2. **Prefetch related branches** on book detail with Drizzle relation query: `{ with: { branches: { with: { branch: true } } } }`

## Security
1. **Enforce `NEXTAUTH_SECRET` rotation** (every 90 days) — never expose to client bundles; store in Vercel encrypted env
2. **Never trust query params** for borrow approvals — enforce authorship + eligibility server-side in Server Action

## Related Projects (in workspace)
- **Banking** — shared Next.js + Drizzle + Neon + NextAuth stack; fintech security patterns applicable to borrow enforcement
- **rhixe_scans** — shared Next.js 15 catalog + media flow patterns; search/filter UX for library discovery
- **comicwise** — shared Next.js 15 + Prisma + NextAuth v5 + Redis; realtime notifications via WebSocket
- **rhixecompany-comics** — dual-stack Django + Next.js 16; serverless Postgres + Redis infra patterns
- **xamehi** — Django + Express + React 18 dual-backend; multi-service auth patterns

## Resources
| Resource | URL | Description |
|----------|-----|-------------|
| Next.js 15 docs | https://nextjs.org/docs | Framework documentation |
