# RESEARCH_REPORT.md

## Project: rhixe_scans

**Type:** Comic / scan reader platform
**Tech Stack:** Next.js 15, React 19, TypeScript strict, Prisma 6, PostgreSQL, Tailwind 3, shadcn/ui, Radix, NextAuth v5, Zustand, TanStack Query, Stripe, PayPal, UploadThing, Resend, WebSocket
**Status:** Active

---

## Similar Projects

| Project | URL | Why Relevant |
|---------|-----|--------------|
| comicwise | `projects/comicwise` | shared comic reader; Stripe + NextAuth + Tailwind |
| rhixecompany-comics | `projects/rhixecompany-comics` | shared comic reader; consolidation target |
| university-libary-jsm | `projects/university-libary-jsm` | shared Next.js + Prisma + PostgreSQL catalog |
| Banking | `projects/Banking` | shared NextAuth + payment patterns |

---

## Key Findings

### Next.js 15 App Router + WebSocket
- Server Components by default; `use client` for interactivity
- WebSockets do NOT work on Vercel serverless — require custom Node server or Fly.io
- Alternative: Server-Sent Events (SSE) or Socket.io for serverless-compatible real-time

### Prisma 6 Singleton Pattern
- Create `lib/prisma.ts` with global singleton to prevent hot-reload connection leaks
- `prisma.config.ts` (new in 6.x) for configuration; migration from 5.x updates setup
- Prisma Accelerate for serverless connection pooling in production

### Stripe + PayPal Integration
- Stripe webhooks in App Router: must use `request.text()` (not `request.json()`) for signature verification
- PayPal: `@paypal/react-paypal-js` frontend + server-side order capture validation
- Always idempotent webhook handlers; use database transactions

### UploadThing + Media
- Type-safe File Routes; presigned URLs + CDN delivery
- Re-sign URLs on key rotation; never permanent URLs for paywalled content

---

## Cheatsheets & Quick Reference

| Topic | Resource | Type |
|-------|----------|------|
| Next.js 15 | https://nextjs.org/docs | Docs |
| Prisma 6/7 | https://www.prisma.io/docs | Docs |
| NextAuth v5 | https://authjs.dev/getting-started | Docs |
| UploadThing | https://docs.uploadthing.com | Docs |
| Stripe Webhooks | https://docs.stripe.com/webhooks | Guide |
| TanStack Query | https://tanstack.com/query/latest | Docs |

---

## Best Practices

1. **Singleton Prisma** — global client prevents connection exhaustion during hot-reload
2. **Raw body for webhooks** — `request.text()` for Stripe signature verification
3. **Signed URLs** — re-sign UploadThing on rotation; serve paywalled content only after auth
4. **Server Components** — render catalog server-side; cache with `revalidateTag`
5. **Zod validation** — validate all API inputs before Prisma writes

---

## Common Pitfalls

| Pitfall | Impact | Avoidance |
|---------|--------|-----------|
| Prisma pool exhaustion | 500s on hot-reload | singleton pattern in `lib/prisma.ts` |
| Stripe webhook JSON body | signature verification fails | `request.text()` not `request.json()` |
| WebSocket on Vercel | silent failure | custom server or SSE alternative |
| UploadThing permanent URLs | broken after key rotation | re-sign URLs; short-lived tokens |
| Prisma 6 config breakage | build failures | migrate to `prisma.config.ts` |

---

## Performance

1. **Preload next chapter** — response hints reduce perceived load time
2. **Cache cover metadata** — aggressively; chapter content per release
3. **`next/image` for catalog** — CDN signed URLs for chapter images
4. **ISR for product pages** — Incremental Static Regeneration
5. **Redis Pub/Sub for WebSocket** — broadcast across multiple server instances

---

## Security

1. **Rotate `NEXTAUTH_SECRET`** regularly; never in browser bundle
2. **Rate-limit chapter and download endpoints** — reduce scraping risk
3. **Validate upload content types** server-side — reject non-images before Prisma insert
4. **Verify all webhook signatures** — Stripe `constructEvent()`, PayPal headers
5. **Signed URLs for paywalled chapters** — always auth-check before serving

---

## Related Projects (in workspace)

- **comicwise** — shared Stripe + NextAuth + Tailwind reader flow
- **rhixecompany-comics** — shared comic reader; consolidation target
- **university-libary-jsm** — Prisma + PostgreSQL catalog patterns
- **Banking** — NextAuth + payment patterns

---

## Resources

| Resource | URL | Description |
|----------|-----|-------------|
| Next.js | https://nextjs.org/docs | Framework docs |
| Prisma | https://www.prisma.io/docs | ORM docs |
| Auth.js v5 | https://authjs.dev/getting-started | Auth docs |
| Stripe Webhooks | https://docs.stripe.com/webhooks | Webhook guide |
