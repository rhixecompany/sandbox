## Project: rhixe_scans
**Type:** Comic / scan reader platform  
**Tech Stack:** Next.js 15, React 19, TypeScript strict, Prisma 6, PostgreSQL, Tailwind 3, shadcn/ui, Radix, NextAuth v5, Zustand, TanStack Query, Stripe, PayPal, UploadThing, Resend, WebSocket  
**Status:** Active  

## Similar Projects
| Project | URL | Why Relevant |
|---------|-----|--------------|
| comicwise | `projects/comicwise` | Shared Next.js + Tailwind + Stripe reader flows. |
| rhixecompany-comics | `projects/rhixecompany-comics` | Comic reader sibling adding scraping import surface cadence. |
| university-library-jsm | `projects/university-library-jsm` | Next.js + Prisma + PostgreSQL library catalog patterns. |
| banking | `projects/banking` | NextAuth v5 + Prisma + PostgreSQL auth + payment patterns. |

## Key Findings
### Next.js 15 + Prisma 6 + PostgreSQL Migration Patterns (2026)
- **Prisma 6.0.1 had a confirmed migration bug** with `can-connect-to-database` check failing on SQLite; workaround is waiting for patch or checking [GitHub Discussion #25835](https://github.com/prisma/prisma/discussions/25835) [1].
- **Prisma Postgres (serverless) is now the recommended path** for Next.js 15: `npx prisma init --db --output ../app/generated/prisma` creates DB, schema, and generates client in one flow [2].
- **Singleton Prisma Client pattern is mandatory** in development to prevent connection exhaustion during hot reload:
  ```typescript
  const globalForPrisma = global as unknown as { prisma?: PrismaClient };
  const prisma = globalForPrisma.prisma ?? new PrismaClient().$extends(withAccelerate());
  if (process.env.NODE_ENV !== "production") globalForPrisma.prisma = prisma;
  export default prisma;
  ```

## Cheatsheets & Quick Reference
| Topic | Resource | Type |
|-------|----------|------|
| Next.js 15 docs | https://nextjs.org/docs | Docs |
| Prisma 6/7 docs | https://www.prisma.io/docs | ORM docs |

## Best Practices (Updated 2026)
1. **Prisma transaction scope** — keep webhook intake inside a Prisma `$transaction` so reader state stays consistent [existing].
2. **Signed reader access** — require signed chapter URLs when content is paywalled [existing].
3. **Email resend pipeline** — send from background job; do not call Resend inside route handlers [existing].
4. **Route handler validation** — validate Stripe + PayPal headers and event types before trusting payloads [existing].

## Common Pitfalls (Updated 2026)
| Pitfall | Impact | Avoidance |
|---------|--------|-----------|
| UploadThing URLs treated as permanent | Broken chapter images | Re-sign URLs and handle key rotation [existing] |
| Client-chosen payment method | Fraud or inventory inconsistencies | Lock payment method at order-creation server-side [existing] |

## Performance (Updated 2026)
1. **Preload next chapter** response hints in chapter list to reduce perceived load [existing].
2. **Cache reader cover metadata** aggressively; chapter content changes per release [existing].
3. **Reduce bundle size** by splitting `@dnd-kit` into reader-only routes [existing].

## Security (Updated 2026)
1. **Rotate `NEXTAUTH_SECRET`** regularly and never expose to browser bundle [existing].
2. **Rate-limit** chapter generation and download endpoints to reduce scraping risk [existing].
3. **Validate upload content types** server-side before Prisma insert [existing].

## Related Projects (in workspace)
- **comicwise** — shared Stripe + NextAuth + Tailwind reader flow
- **rhixecompany-comics** — shared comic reader and payment concerns
- **university-library-jsm** — Prisma + PostgreSQL catalog patterns
- **banking** — NextAuth v5 + Prisma auth + payment patterns

## Resources
| Resource | URL | Description |
|----------|-----|-------------|
| Next.js docs | https://nextjs.org/docs | Framework docs |
| Prisma docs | https://www.prisma.io/docs | ORM docs |
