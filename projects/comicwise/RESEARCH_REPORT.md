# RESEARCH_REPORT.md

## Project: comicwise

**Type:** Comic streaming / reader platform **Tech Stack:** Next.js 15, React 19 Server Components, Prisma 7, PostgreSQL 17, NextAuth.js v5 (Auth.js), Tailwind CSS 4, shadcn/ui, Zustand, React Query 5 (TanStack Query), Zod 4, Stripe (Node.js SDK v17, API 2026-01-28), pnpm **Status:** Consolidation target (patterns extracted → rhixecompany-comics)

---

## Similar Projects

| Project | URL | Why Relevant |
| --- | --- | --- |
| rhixe_scans | `projects/rhixe_scans` | Same comic reader, shared auth + payments |
| rhixecompany-comics | `projects/rhixecompany-comics` | Consolidation target; inherits reader patterns |
| university-libary-jsm | `projects/university-libary-jsm` | Next.js 15 + Prisma + PostgreSQL academic |
| Banking | `projects/Banking` | Next.js + Prisma + Stripe subscription patterns |

---

## Key Findings

### Next.js 15 + React 19 (2026)

- Turbopack default bundler; Edge runtime + streaming for AI recs
- Server Components render chapter data; only interactions need `'use client'`
- React 19 forms with Server Actions (useFormState + Zod) standard

### Prisma 7 (2026)

- Engine rewritten in TypeScript (dropped Rust binary)
- Prisma Optimize debugs N+1; Accelerate for serverless pooling
- DAL boundaries: precise `select`/`include`; `@@index` on FKs

### NextAuth v5 (2026)

- Universal `auth()` replaces getServerSession/getSession/getToken
- Multiple providers: GitHub, Keycloak, Google, Credentials
- Sessions: database (persistent) or JWT (stateless)

### Stripe Subscriptions (2026)

- Server Actions for Checkout Sessions; Embedded Checkout for no-redirect
- Verify webhook signatures via `constructEvent()`

### React Query 5 + Zustand (2026)

- TanStack Query ~13KB for server state; Zustand ~1.1KB for client state
- Never store API responses in Zustand — causes sync issues

---

## Cheatsheets & Quick Reference

| Topic            | Resource                           | Type  |
| ---------------- | ---------------------------------- | ----- |
| Next.js 15       | https://nextjs.org/docs/app        | Docs  |
| Prisma 7         | https://www.prisma.io/docs         | Docs  |
| NextAuth v5      | https://authjs.dev/getting-started | Docs  |
| Stripe Node.js   | https://docs.stripe.com/api        | Docs  |
| TanStack Query 5 | https://tanstack.com/query/latest  | Docs  |
| Zustand          | https://github.com/pmndrs/zustand  | Guide |

---

## Best Practices

1. **RSC chapter pages** — Render metadata server-side; only interactions hydrate
2. **Server Actions for mutations** — `actions/` dir; useFormState + Zod; revalidateTag
3. **Prisma 7 DAL boundaries** — `dal/*` modules; precise select/include; @@index on FKs
4. **Zod as boundary contract** — Validate before Server Actions and Prisma inserts
5. **Stripe webhook idempotency** — Check event ID uniqueness; verify with `constructEvent`

---

## Common Pitfalls

| Pitfall | Impact | Avoidance |
| --- | --- | --- |
| Server data in client state | Duplicate sync, stale data | TanStack Query for API; Zustand only for UI |
| API responses in Zustand | Sync issues, cache invalidation | Server → React Query; Client → Zustand |
| Missing Stripe webhook secret | 400 errors on endpoints | Set `STRIPE_WEBHOOK_SECRET`; verify signature |
| Prisma generate omitted | Build failures | Run `prisma generate` in build step |

---

## Performance

1. **`next/image` for catalog**; CDN signed URLs for chapter images
2. **Cache static metadata** with `force-static` + `revalidateTag`
3. **Aggregate in DAL** with `include` + nested `where`; avoid client joins
4. **Preload next chapter** hints for perceived load reduction
5. **Prisma Optimize** to catch N+1 before production

---

## Security

1. **Validate image paths** before storage; signed URLs for paywalled content
2. **Strip HTML from reviews** despite client-side sanitization
3. **Secrets in .env.local only** — different keys per environment
4. **Rotate `NEXTAUTH_SECRET`** regularly; never in browser bundle
5. **Verify Stripe webhooks** with `constructEvent()` before processing

---

## Related Projects (in workspace)

- **rhixe_scans** — comic reader, shared Stripe + NextAuth flows
- **rhixecompany-comics** — consolidation target inheriting reader patterns
- **university-libary-jsm** — Next.js 15 + Prisma + PostgreSQL
- **Banking** — Next.js + Prisma + Stripe subscriptions

---

## Resources

| Resource | URL | Description |
| --- | --- | --- |
| Next.js 15 | https://nextjs.org/docs/app | Framework docs |
| Prisma | https://www.prisma.io/docs | ORM docs |
| Auth.js v5 | https://authjs.dev/getting-started | Migration guide |
| Stripe Webhooks | https://docs.stripe.com/billing/subscriptions/webhooks | Webhook guide |
| TanStack Query | https://tanstack.com/query/latest/docs | Server state mgmt |
| Zustand | https://docs.pmnd.rs/zustand | Client state mgmt |
