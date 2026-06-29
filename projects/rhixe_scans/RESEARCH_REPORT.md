# RESEARCH_REPORT.md

## Project: rhixe_scans

**Type:** Comic / scan reader platform
**Tech Stack:** Next.js 15, React 19, TypeScript strict, Prisma 6, PostgreSQL, Tailwind 3, shadcn/ui, Radix, NextAuth v5, Zustand, TanStack Query, Stripe, PayPal, UploadThing, Resend, WebSocket
**Status:** Active

---

## Similar Projects

| Project | URL | Why Relevant |
|---------|-----|--------------|
| comicwise | `projects/comicwise` | Shared Next.js + Tailwind + Stripe reader flows |
| rhixecompany-comics | `projects/rhixecompany-comics` | Comic reader sibling adding scraping import |
| university-libary-jsm | `projects/university-libary-jsm` | Next.js + Prisma + PostgreSQL catalog patterns |
| Banking | `projects/Banking` | NextAuth v5 + Prisma + PostgreSQL auth |

---

## Key Findings

### Prisma 6/7 (2026)
- Prisma 6.0.1 migration bug: `can-connect-to-database` fails on SQLite (GitHub #25835)
- Prisma 7 rewrote engine in TypeScript — migration recommended for edge
- Singleton Prisma Client prevents connection exhaustion during hot-reload

### NextAuth v5 (2026)
- Universal `auth()` replaces getServerSession/getSession/getToken
- 80+ providers: GitHub, Keycloak, Google, Discord, Credentials
- JWT strategy stateless (no DB per request) — ideal for multi-provider

### UploadThing
- Type-safe File Routes; presigned URLs + CDN delivery
- $10/month for 100GB; 2GB free tier
- URLs short-lived — re-sign on rotation; never permanent

### Stripe + PayPal
- Stripe: Server Actions for Checkout; Embedded for no-redirect
- Verify Stripe `constructEvent()`, PayPal transmission header
- Lock payment method at order-creation server-side

### Zustand + TanStack Query
- TanStack Query ~13KB for server state; Zustand ~1.1KB for client
- Never store API responses in Zustand — causes sync issues

---

## Cheatsheets & Quick Reference

| Topic | Resource | Type |
|-------|----------|------|
| Next.js 15 | https://nextjs.org/docs | Docs |
| Prisma 6/7 | https://www.prisma.io/docs | Docs |
| NextAuth v5 | https://authjs.dev/getting-started | Docs |
| UploadThing | https://docs.uploadthing.com | Docs |
| Stripe Node.js | https://docs.stripe.com/api | Docs |
| Zustand | https://github.com/pmndrs/zustand | Guide |
| TanStack Query | https://tanstack.com/query/latest | Docs |

---

## Best Practices

1. **Prisma transaction scope** — Webhook intake inside `$transaction` for consistent state
2. **Signed reader access** — Signed URLs for paywalled chapters; re-sign UploadThing on rotation
3. **Validate route handler headers** — Stripe/PayPal event types before processing
4. **Payment method lock** — Lock at order-creation server-side to prevent switching
5. **Webhook idempotency** — Check event ID uniqueness; DB unique constraints

---

## Common Pitfalls

| Pitfall | Impact | Avoidance |
|---------|--------|-----------|
| UploadThing URLs as permanent | Broken images after key rotation | Re-sign URLs; short-lived tokens |
| Client-chosen payment method | Fraud, inventory mismatches | Lock method server-side at order creation |
| Prisma 6 migration bug | Failed migrations in CI | Use Prisma 7 or check #25835 |
| Missing webhook verification | Processing forged events | Verify Stripe `constructEvent()` + PayPal headers |

---

## Performance

1. **Preload next chapter** — Response hints reduce perceived load time
2. **Cache cover metadata** — Aggressively; chapter content changes per release
3. **Reduce bundle** — Split `@dnd-kit` into reader-only routes via dynamic imports
4. **Prisma Accelerate** for serverless connection pooling
5. **Server Components for catalog** — Render server-side; cache with `revalidateTag`

---

## Security

1. **Rotate `NEXTAUTH_SECRET`** regularly; never in browser bundle
2. **Rate-limit chapter generation and download** endpoints to reduce scraping
3. **Validate upload content types** server-side — reject non-image before Prisma insert
4. **Verify all webhook signatures** — Stripe `constructEvent()`, PayPal headers
5. **Signed URLs for paywalled chapters** — never serve without auth check

---

## Related Projects (in workspace)

- **comicwise** — shared Stripe + NextAuth + Tailwind reader flow
- **rhixecompany-comics** — shared comic reader and payment concerns
- **university-libary-jsm** — Prisma + PostgreSQL catalog patterns
- **Banking** — NextAuth v5 + Prisma auth + payment patterns

---

## Resources

| Resource | URL | Description |
|----------|-----|-------------|
| Next.js | https://nextjs.org/docs | Framework docs |
| Prisma | https://www.prisma.io/docs | ORM docs |
| Auth.js v5 | https://authjs.dev/getting-started | Auth docs |
| UploadThing | https://docs.uploadthing.com | File upload |
| Stripe Webhooks | https://docs.stripe.com/webhooks | Webhook guide |
| Zustand | https://docs.pmnd.rs/zustand | Client state |
