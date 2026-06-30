# RESEARCH_REPORT.md

## Project: comicwise

**Type:** Comic streaming / reader platform
**Tech Stack:** Next.js 16, TypeScript strict, React 19, Drizzle ORM (Prisma migration in progress), PostgreSQL, NextAuth v5 beta, Stripe, ImageKit, Cloudinary, BullMQ, Upstash QStash, Upstash Redis, Sentry, Vitest, Playwright, pnpm
**Status:** Consolidation target (patterns extracted → rhixecompany-comics)

---

## Similar Projects

| Project | URL | Why Relevant |
|---------|-----|--------------|
| rhixe_scans | `projects/rhixe_scans` | comic reader; shared Stripe + NextAuth + Tailwind |
| rhixecompany-comics | `projects/rhixecompany-comics` | consolidation target |
| university-libary-jsm | `projects/university-libary-jsm` | Next.js 15 + Prisma + PostgreSQL |
| Banking | `projects/Banking` | Next.js + payment flows |

---

## Key Findings

### Next.js 16 Comic Reader (2026)
- Partial Prerendering (PPR) statically pre-renders shell; streams dynamic content
- Turbopack default bundler; Server Actions stable for mutations
- Image optimization for comic assets via `next/image`

### Drizzle + Prisma Migration
- Drizzle ~7KB bundle vs Prisma ~1.6MB — main driver for migration
- Prisma Optimize debugs N+1; `@@index` on FKs
- Migration path: run both ORMs during transition to avoid breaking reads

### Stripe Subscriptions
- Server Actions for Checkout Sessions; Embedded Checkout for no-redirect
- Verify webhooks via `constructEvent()`; idempotency key per subscription event

### BullMQ + Upstash
- BullMQ for async jobs (email, image processing); QStash for serverless cron
- Upstash Redis as broker; global replication, zero cold starts

---

## Cheatsheets & Quick Reference

| Topic | Resource | Type |
|-------|----------|------|
| Next.js 16 | https://nextjs.org/docs/app | Docs |
| Drizzle ORM | https://orm.drizzle.dev | Docs |
| Stripe Node.js | https://docs.stripe.com/api | Docs |
| BullMQ | https://docs.bullmq.io/ | Docs |
| Upstash | https://docs.upstash.com/ | Docs |
| TanStack Query | https://tanstack.com/query/latest | Docs |

---

## Best Practices

1. **Server Components** — server-side render catalog; only interactions hydrate
2. **Server Actions for mutations** — `actions/` dir; useFormState + Zod; revalidateTag
3. **Drizzle DAL boundaries** — `dal/*` modules; precise select/include; `@@index` on FKs
4. **Zod as boundary contract** — validate before Server Actions and DB writes
5. **Stripe webhook idempotency** — check event ID uniqueness; verify `constructEvent`

---

## Common Pitfalls

| Pitfall | Impact | Avoidance |
|---------|--------|-----------|
| Dual ORM during migration | Data drift | Eschew cross-ORM transactions; migrate one domain at a time |
| Server data in client state | Stale data | TanStack Query for API; Zustand only for UI |
| Missing Stripe webhook secret | 400 errors | Set `STRIPE_WEBHOOK_SECRET`; verify signature |
| Prisma generate omitted | Build failures | Run in build step |

---

## Performance

1. **`next/image` for catalog** — CDN signed URLs for chapter images
2. **Cache static metadata** — `force-static` + `revalidateTag`
3. **Aggregate in DAL** with `include` + nested `where`
4. **Preload next chapter** hints for perceived load reduction

---

## Security

1. **Validate image paths** before storage; signed URLs for paywalled content
2. **Strip HTML from reviews** despite client-side sanitization
3. **Secrets in `.env.local` only** — different keys per environment
4. **Rotate `NEXTAUTH_SECRET`** regularly
5. **Verify Stripe webhooks** with `constructEvent()`

---

## Related Projects (in workspace)

- **rhixe_scans** — comic reader; shared Stripe + NextAuth + Tailwind
- **rhixecompany-comics** — consolidation target inheriting reader patterns
- **university-libary-jsm** — Next.js 15 + Prisma + PostgreSQL
- **Banking** — Next.js + payment flows

---

## Resources

| Resource | URL | Description |
|----------|-----|-------------|
| Next.js 16 | https://nextjs.org/docs | Framework docs |
| Drizzle ORM | https://orm.drizzle.dev | TypeScript ORM |
| Stripe Webhooks | https://docs.stripe.com/billing/subscriptions/webhooks | Webhook guide |
| TanStack Query | https://tanstack.com/query/latest/docs | Server state mgmt |
| Zustand | https://docs.pmnd.rs/zustand | Client state mgmt |
