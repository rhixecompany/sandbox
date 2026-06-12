# RESEARCH_REPORT.md

## Project: rhixe_scans

**Type:** Comic / scan reader platform
**Tech Stack:** Next.js 15, React 19, TypeScript, Tailwind CSS 3, shadcn/ui, Prisma ORM 6, PostgreSQL, NextAuth v5, Stripe, PayPal, UploadThing, Resend, Jest, ts-jest
**Status:** Active

---

## Similar Projects

| Project | URL | Why Relevant |
|---------|-----|--------------|
| comicwise | `projects/comicwise` | Shared Next.js + Tailwind + Stripe reader flows. |
| rhixecompany-comics | `projects/rhixecompany-comics` | Comic reader sibling adding scraping import surface cadence. |

---

## Key Findings

### Next.js 15 + Reader Experience
- Reader pages benefit from RSC pre-rendering; mark playback and bookmark controls as client-only with `"use client"`.
- Use `params` and `generateMetadata` for chapter SEO and image preview metadata.

### Prisma + UploadThing
- Prisma schema should store `uploadthing.fileKey` and signed URL metadata; never rely solely on client-returned URLs.
- Deleted chapter images should remove storage references with a Prisma after-update hook to avoid broken links.

### Payments + Auth
- NextAuth v5 with Prisma adapter keeps session state tied to the same database used by reader history.
- Split Stripe and PayPal webhook verifiers into separate route handlers to simplify incident response.

### Testing
- Jest + ts-jest works but heavier; add route handler tests for webhooks and Prisma transaction mutations.

---

## Cheatsheets & Quick Reference

| Topic | Resource | Type |
|-------|----------|------|
| Next.js docs | https://nextjs.org/docs | Docs |
| Prisma docs | https://www.prisma.io/docs | ORM docs |
| NextAuth v5 | https://authjs.dev | Auth guide |
| UploadThing docs | https://docs.uploadthing.com | File uploads |
| Stripe docs | https://stripe.com/docs | Payments |

---

## Best Practices
1. **Prisma transaction scope** — keep webhook intake inside a Prisma `$transaction` so reader state stays consistent.
2. **Signed reader access** — require signed chapter URLs when content is paywalled.
3. **Email resend pipeline** — send from background job; do not call Resend inside route handlers.
4. **Route handler validation** — validate Stripe + PayPal headers and event types before trusting payloads.
5. **Reader cache keys** — key cache by slug + chapter number to reduce DB load on popular series.

---

## Common Pitfalls

| Pitfall | Impact | Avoidance |
|---------|--------|-----------|
| UploadThing URLs treated as permanent | Broken chapter images | Re-sign URLs and handle key rotation. |
| Client-chosen payment method | Fraud or inventory inconsistencies | Lock payment method at order-creation server-side. |
| Next.js Image on protected content | Cache leakage | Use signed URLs, not unguarded public image endpoints. |
| Mixed webhook ownership | Duplicate payment intents | Choose one payment source of truth per checkout session. |

---

## Performance
1. Preload next chapter response hints in the chapter list to reduce perceived load.
2. Cache reader cover metadata aggressively; reader chapter content changes with each release.
3. Reduce bundle size by splitting `@dnd-kit` into reader-only routes.
4. Use Prisma query logging in dev to detect hidden N+1s in reader history queries.

---

## Security
1. Rotate `NEXTAUTH_SECRET` regularly and never expose it to the browser bundle.
2. Rate-limit chapter generation and download endpoints to reduce scraping risk.
3. Validate upload content types server-side before Prisma insert.
4. Keep Stripe webhook secret and PayPal client secret in server-only env variables.

---

## Related Projects (in workspace)

- **comicwise** — shared Stripe + NextAuth + Tailwind reader flow
- **rhixecompany-comics** — shared comic reader and payment concerns

---

## Resources

| Resource | URL | Description |
|----------|-----|-------------|
| Next.js docs | https://nextjs.org/docs | Framework docs |
| Prisma docs | https://www.prisma.io/docs | ORM docs |
| NextAuth docs | https://authjs.dev | Auth guide |
| UploadThing docs | https://docs.uploadthing.com | Upload docs |
| Stripe docs | https://stripe.com/docs | Payments |
