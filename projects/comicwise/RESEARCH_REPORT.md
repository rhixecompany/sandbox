## Project: comicwise
**Type:** Comic streaming / reader platform
**Tech Stack:** Next.js 15, React 19 Server Components, Prisma 7, PostgreSQL 17, NextAuth.js v5 (Auth.js), Tailwind CSS 4, shadcn/ui, Zustand, React Query 5 (TanStack Query), Zod 4, Stripe (Node.js SDK v17, API 2026-01-28), pnpm
**Status:** Consolidation target (patterns extracted → rhixecompany-comics)

## Similar Projects
| Project | URL | Why Relevant |
|---------|-----|--------------|
| rhixe_scans | `projects/rhixe_scans` | Same comic reader surface area, shared auth + payments + Next.js readers |
| rhixecompany-comics | `projects/rhixecompany-comics` | Current consolidation target; inherits comic reader and DAL patterns |
| university-library-jsm | `projects/university-library-jsm` | Next.js 15 + Prisma + PostgreSQL academic library patterns |
| banking | `projects/banking` | Next.js + Prisma + Stripe subscription patterns |

## Cheatsheets & Quick Reference
| Topic | Resource | Type |
|-------|----------|------|
| Next.js 15 App Router | https://nextjs.org/docs/app | Docs |
| Next.js 15 Breaking Changes | https://nextjs.org/blog/next-15 | Release Notes |

## Best Practices (2026 Update)
1. **RSC chapter pages** — Render chapter imagery and metadata server-side; only reader interactions (drag, bookmark, progress) need hydration via `'use client'`
2. **Server Actions for mutations** — Define at module level (`'use server'`) in `actions/` directory; use `useFormState` + Zod for validation; revalidate via `revalidatePath`/`revalidateTag` after mutation
3. **Prisma 7 DAL boundaries** — Keep Prisma access behind `dal/*` modules; use `select`/`include` precisely; add `@@index` on FKs and composite unique constraints
4. **Zod as boundary contract** — Validate all form payloads before Server Actions and before Zod→Prisma inserts; reuse schemas for client/server

## Common Pitfalls (2026 Update)
| Pitfall | Impact | Avoidance |
|---------|--------|-----------|
| Treating server data as client state | Duplicate sync, stale data, memory pressure | Use TanStack Query for ALL API data; Zustand only for UI state (theme, auth, cart) |
| Storing API responses in Zustand/Redux | Sync issues, cache invalidation complexity | Server state → React Query; Client state → Zustand |

## Performance (2026 Update)
1. **`next/image` with automatic loader** for catalog artwork; reserve large chapter image optimization for CDN flow (signed URLs/short-lived tokens)
2. **Cache static comic metadata** with Next.js 15 `use cache` (experimental) or `force-static` + `revalidateTag` on webhook events
3. **Avoid client-side joins** of review/comment objects; aggregate in DAL with Prisma `include` + nested `where` or raw SQL for complex aggregations

## Security (2026 Update)
1. **Validate all image paths and reader URLs** before storage; never trust raw user uploads; use signed URLs or short-lived tokens for chapter images
2. **Strip HTML tags from review/comment bodies** before DB writes, even with CKEditor sanitization on client side
3. **Store Stripe and auth secrets only in `.env.local`** — never scaffold into example env files; use different keys per environment

## Related Projects (in workspace)
- **rhixe_scans** — comic reader sibling with shared Stripe and NextAuth flows
- **rhixecompany-comics** — consolidation target inheriting ComicWise frontend and reader patterns
- **university-library-jsm** — Next.js 15 + Prisma + PostgreSQL academic patterns
- **banking** — Next.js + Prisma + Stripe subscription patterns
- **comicwise** — should be marked as consolidation source in disposal reports

## Resources
| Resource | URL | Description |
|----------|-----|-------------|
| Next.js 15 Blog | https://nextjs.org/blog/next-15 | Official release notes + breaking changes |
| Next.js Server Actions | https://nextjs.org/docs/13/app/building-your-application/data-fetching/server-actions-and-mutations | Server Actions guide |
