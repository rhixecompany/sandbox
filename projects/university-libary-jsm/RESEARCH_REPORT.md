# RESEARCH_REPORT.md

## Project: university-libary-jsm

**Type:** Library management system
**Tech Stack:** Next.js 15, TypeScript, Drizzle ORM, Neon PostgreSQL, Redis, NextAuth.js
**Status:** Active

---

## Similar Projects

| Project | URL | Why Relevant |
|---------|-----|--------------|
| Banking | `projects/Banking` | Shared Next.js + Drizzle + Neon + auth stack. |
| rhixe_scans | `projects/rhixe_scans` | Shared Next.js + Prisma + reader/content retrieval patterns. |

---

## Key Findings

### Serverless Postgres + Drizzle
- Neon serverless connection pooling benefits library apps during class registration bursts; prefer short-lived server-side fetches.
- Use cache tags and Redis to keep hot book-metadata responses fast and avoid repeated DB round trips.

### Redis for Library UX
- Use Redis for rate limiting on search reads and session caching; migrating from Upstash-style docs to a local Redis flow needs the same `NEXT_PUBLIC_*` prefix discipline.
- Use Redis sorted sets to build popular-borrow book rankings cheaply.

### Next.js 15 Catalog UX
- Debounce search input in client components and keep the debounced handler memoized to reduce fetches.
- Use search params and route-level caching to preserve filter state during browsing.

---

## Cheatsheets & Quick Reference

| Topic | Resource | Type |
|-------|----------|------|
| Next.js docs | https://nextjs.org/docs | Docs |
| Drizzle docs | https://orm.drizzle.dev/docs | ORM docs |
| Neon docs | https://neon.tech/docs | Serverless Postgres |
| Upstash Redis docs | https://docs.upstash.com/redis | Caching guide |

---

## Best Practices
1. Keep schema search spans lowercase and use trigram indexes for user search flows.
2. Rate-limit public catalog reads in Redis to prevent bot scraping during enrollment windows.
3. Use `select_related()` style Drizzle joins for book + author + branch display.
4. Keep borrow-return mutations inside Server Actions with auth and inventory checks.

---

## Common Pitfalls

| Pitfall | Impact | Avoidance |
|---------|--------|-----------|
| Neon connection exhaustion | Request latency spikes | Use pooled connection string in server components. |
| Client-driven filtering | Unbounded queries | Keep filters in server-only search middleware. |
| Missing borrow uniqueness | Duplicate borrow records | Add DB constraint for one active borrow per book per user. |

---

## Performance
1. Cache author and book summaries for 60 seconds in Redis with `SET NX/EX`.
2. Prefetch related branches on book detail pages with Drizzle relation queries.
3. Use `next/font` and route segment caching for static pages like about and policies.

---

## Security
1. Enforce `NEXTAUTH_SECRET` rotation and never expose it to client bundles.
2. Do not trust query params for borrow approvals; enforce authorship and borrow eligibility server-side.
3. Redact personal member details before returning user lists to admin dashboards.

---

## Related Projects (in workspace)

- **Banking** — shared Next.js + Drizzle + auth stack
- **rhixe_scans** — shared Next.js catalog + media flow

---

## Resources

| Resource | URL | Description |
|----------|-----|-------------|
| Next.js docs | https://nextjs.org/docs | Framework docs |
| Drizzle docs | https://orm.drizzle.dev/docs | Database toolkit |
| Neon docs | https://neon.tech/docs | Serverless Postgres |
| Redis docs | https://redis.io/docs | Cache |
| NextAuth docs | https://authjs.dev | Auth |
