# RESEARCH_REPORT.md

## Project: comicwise

**Type:** Comic streaming / reader platform
**Tech Stack:** Next.js 16, React 19, TypeScript, Tailwind CSS 4, shadcn/ui, Drizzle ORM, PostgreSQL, NextAuth.js v5, Zustand, React Query, Zod 4, Vitest, Playwright
**Status:** Consolidation target

---

## Similar Projects

| Project | URL | Why Relevant |
|---------|-----|--------------|
| rhixe_scans | `projects/rhixe_scans` | Same comic reader surface area, shared auth + payments + Next.js readers. |
| rhixecompany-comics | `projects/rhixecompany-comics` | Current consolidation target; inherits comic reader and DAL patterns. |

---

## Key Findings

### Next.js 16 + Comic Reader UX
- Server Components should render chapter indexes and metadata pages; mark page-level drag, bookmark, and progress utilities with `"use client"`.
- Use Drizzle eager/relation loading on chapter detail routes to avoid client-side hydration fetch waterfalls.

### Drizzle + PostgreSQL Data Model
- Keep soft deletes on `comments` and `progress` tables; avoid expunging reader history.
- Add unique constraints on `Comic.slug` and composite `UserComic(user_id, comic_id)` to avoid duplicate state.

### Auth + Payments UX
- Prefer NextAuth v5 database sessions for session continuity across readers and checkout pages.
- Stripe checkout + webhook state is best modeled as outbox events; never trust UI redirect alone.

### Frontend State Discipline
- Zustand remains valid for low-frequency UI state; use React Query + revalidation tags for list updates instead of manual stores.

---

## Cheatsheets & Quick Reference

| Topic | Resource | Type |
|-------|----------|------|
| Next.js App Router | https://nextjs.org/docs/app | Docs |
| Drizzle ORM + relations | https://orm.drizzle.dev/docs/relational-queries/quick-start | Guide |
| shadcn/ui | https://ui.shadcn.com | Component system |
| NextAuth v5 | https://authjs.dev | Auth guide |
| Playwright | https://playwright.dev | E2E testing |

---

## Best Practices
1. **RSC chapter pages** — render chapter imagery and metadata server-side; only reader interactions need hydration.
2. **DAL boundaries** — keep Drizzle access behind `dal/*` modules so schema refactors do not leak into UI.
3. **Zod as boundary contract** — validate all form payloads before Server Actions and before Zod→Drizzle inserts.
4. **Revalidation tags** — use React Query revalidation plus Next.js revalidate patterns after mutations.
5. **Test gates** — keep lint + typecheck + unit + E2E green in a single `validate` script before merge.

---

## Common Pitfalls

| Pitfall | Impact | Avoidance |
|---------|--------|-----------|
| Mixing store and server state | Duplicate sync logic | Keep reader progress in server-backed query cache when possible. |
| Updating Stripe state from client | Payment fraud surface | Move subscription transitions to webhook handlers. |
| Soft-delete inconsistency | Ghost rows in analytics | Apply `deletedAt` checks in all DAL queries that feed metrics. |
| Client-only pagination on huge catalogs | Memory/performance issues | Prefer server cursors loaded in Server Components. |

---

## Performance
1. Use `next/image` with automatic `loader` for catalog artwork; reserve large chapter image optimization for CDN flow.
2. Cache static comic metadata with `"use cache"` and revalidate on webhook events.
3. Avoid client-side joins of review objects; aggregate in the DAL with Drizzle `.with()` instead.
4. Playwright tests should use route interception and fast fixtures to keep suites sub-3 minutes.

---

## Security
1. Validate all image paths and reader URLs before storage; never trust raw user uploads.
2. Strip HTML tags from review bodies before database writes, even when CKEditor sanitization is enabled on the editor side.
3. Store Stripe and auth secrets only in `.env`; never scaffold them into example env files.
4. RBAC checks must stay server-side; never gate protected routes purely with client redirects.
5. Use signed URLs or short-lived tokens for chapter images instead of exposing raw origin permissions.

---

## Related Projects (in workspace)

- **rhixe_scans** — comic reader sibling with shared Stripe and NextAuth flows
- **rhixecompany-comics** — consolidation target inheriting ComicWise frontend and reader patterns
- **comicwise** — should be marked as consolidation source in disposal reports

---

## Resources

| Resource | URL | Description |
|----------|-----|-------------|
| Next.js Docs | https://nextjs.org/docs | Official documentation |
| Drizzle ORM | https://orm.drizzle.dev | SQL toolkit |
| shadcn/ui | https://ui.shadcn.com | UI components |
| NextAuth | https://authjs.dev | Authentication |
| Playwright | https://playwright.dev | Browser tests |
| Comic reader OSS patterns | https://github.com/onggiabayluon/fullstack-comic-app | Reference monorepo |
