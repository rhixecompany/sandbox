# RESEARCH_REPORT.md

## Project: university-libary-jsm (BookWise)

**Type:** University library management system
**Tech Stack:** Next.js 15, Drizzle ORM, Neon PostgreSQL, NextAuth v5, Upstash Redis/Workflows, ImageKit, Tailwind CSS 4, shadcn/ui, Zod 4
**Status:** Active

## Similar Projects

| Project | URL | Why Relevant |
|---------|-----|--------------|
| JavaScript Mastery BookWise | https://www.jsmastery.pro | Original course project & learning resource |
| Bibliotech | https://github.com/topics/library-management | Open-source library management systems |
| InvenTree | https://inventree.org | Inventory management with similar patterns |

## Key Findings

### Drizzle ORM + Neon Serverless (2026)
- Drizzle provides type-safe SQL-like queries with minimal overhead vs Prisma (orm.drizzle.team)
- Neon's `@neondatabase/serverless` HTTP driver eliminates persistent connection management
- Drizzle Kit migrations work seamlessly with Neon's branching model for preview deployments

### Next.js 15 + Server Actions
- Server Actions with Zod validation replace traditional API routes for mutations
- Turbopack delivers ~400% faster dev server startup vs webpack (nextjs.org)
- Rate limiting via Upstash Redis is essential for exposed Server Action endpoints

## Cheatsheets & Quick Reference

| Topic | Resource | Type |
|-------|----------|------|
| Next.js 15 Docs | https://nextjs.org/docs | Official Docs |
| Drizzle ORM | https://orm.drizzle.team | ORM Docs |
| Neon Serverless Postgres | https://neon.tech/docs | Database Docs |
| Upstash Redis | https://upstash.com/docs | Redis Docs |

## Best Practices

1. **Zod-first validation** — Validate all Server Action inputs before DB queries (already implemented)
2. **Drizzle DAL pattern** — Separate query files (`lib/queries/`) for maintainable data access
3. **Rate limit auth routes** — Upstash Ratelimit (5 req/min) prevents brute force (already implemented)
4. **Server Components by default** — Minimize client JS; use Client Components only for interactivity
5. **ImageKit signed URLs** — Server-side auth for uploads prevents unauthorized media access

## Common Pitfalls

| Pitfall | Impact | Avoidance |
|---------|--------|-----------|
| No migration versioning | Schema drift between dev/prod | Use Drizzle Kit `db:migrate` in CI/CD |
| Credentials-only auth | No OAuth fallback | Add GitHub/Google providers in next-auth config |
| Missing rate limit on all routes | Abuse of unprotected Server Actions | Apply Upstash middleware globally |
| JWT size bloat | Vercel edge function size limits | Keep JWT payload minimal |

## Performance

1. **Neon HTTP driver** eliminates cold start latency from persistent connections
2. **Drizzle tree-shakeable queries** produce minimal bundle size vs Prisma
3. **Upstash HTTP-based Redis** avoids TCP connection overhead in serverless functions
4. **Next.js ISR** for static pages (book catalog) reduces DB load
5. **ImageKit CDN** offloads image optimization from the server

## Security

1. **Server Action validation** with Zod prevents injection via untrusted input
2. **Upstash rate limiting** on auth routes prevents brute force attacks
3. **NextAuth v5 JWT** strategy means no session store vulnerability
4. **ImageKit signed URLs** ensure only authorized uploads
5. **Database credentials** in environment variables only — never in code

## Related Projects (in workspace)

- **comicwise** — Next.js 15 + Prisma, similar NextAuth + Zod patterns
- **rhixe_scans** — Next.js 15 + Prisma + Stripe, shares NextAuth v5 architecture
- **Banking** — Next.js 16 + Drizzle + Plaid, shares Drizzle ORM patterns
- **rhixecompany-comics** — Django + Next.js 16, shares Next.js App Router patterns

## Resources

| Resource | URL | Description |
|----------|-----|-------------|
| Next.js 15 Docs | https://nextjs.org/docs | Framework documentation |
| Drizzle ORM | https://orm.drizzle.team | ORM with Neon adapter |
| Neon Docs | https://neon.tech/docs/serverless/serverless-driver | Serverless PostgreSQL |
| Upstash Ratelimit | https://upstash.com/docs/redis/sdks/ratelimit-ts/overview | Rate limiting SDK |
