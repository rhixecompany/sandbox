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

- **Partial Prerendering (PPR)** statically pre-renders shell; streams dynamic content
- **Turbopack** default bundler; **Server Actions** stable for mutations
- **Image optimization** for comic assets via `next/image`
- **React 19** support with Server Components by default
- **Async `params`/`searchParams`** in App Router (Next.js 16+)
- **Cache Components** with `"use cache"` directive for granular caching
- **Streaming with `loading.tsx` + Suspense** for progressive loading
- **Middleware renamed** to `proxy.ts` (Next.js 16+)

### Drizzle + Prisma Migration (2026)

- **Drizzle ~7KB bundle** vs Prisma ~1.6MB — main driver for migration
- **Prisma Optimize** debugs N+1; `@@index` on FKs
- **Migration path:** run both ORMs during transition to avoid breaking reads
- **Prisma 7** rewrote engine in TypeScript (dropped Rust binary)
- **Drizzle 0.45+** stable v1; edge-runtime compatible, no codegen step
- **Migration strategy:** migrate one domain at a time; avoid cross-ORM transactions

### Stripe Subscriptions (2026)

- **Server Actions** for Checkout Sessions; **Embedded Checkout** for no-redirect flow
- **Verify webhooks** via `constructEvent()`; **idempotency key** per subscription event
- **Stripe Billing 0.7%** on subscription volume (2026 pricing)
- **Customer Portal** with custom domain ($10/mo extra)
- **Usage-based/metered billing** support for usage-heavy products
- **Webhook idempotency** — check event ID uniqueness; verify `constructEvent` signature

### NextAuth v5 Beta + WebAuthn Passkeys (2026)

- **Auth.js v5** (rebranded from NextAuth) — beta since 2023, stable in practice
- **better-auth** emerging as modern alternative with plugin architecture
- **WebAuthn/Passkeys** supported via `@auth/webauthn` or `better-auth` plugins
- **Migration guide** at `authjs.dev/getting-started/migrating-to-v5`
- **Clerk** remains strongest for hosted auth with org/billing UI
- **NextAuth v5** still on beta tag (`5.0.0-beta.31` as of Feb 2026) but production-ready

### Radix UI + shadcn/ui + Tailwind CSS 4 Comic Reader Components (2026)

- **Tailwind CSS v4** — new Vite-based engine, no config file needed, CSS-first
- **shadcn/ui** compatible with Tailwind 4 via `@tailwindcss/postcss` plugin
- **Radix UI** primitives unchanged — headless, accessible, unstyled
- **Comic reader patterns:** 
  - `Dialog`/`Sheet` for reader modal
  - `Slider` for page navigation
  - `Keyboard` navigation via `useKeyboardShortcuts` hook
  - `ScrollArea` for vertical scroll (webtoon) mode
  - `Separator` for chapter dividers
  - `Tooltip` for chapter info on hover
- **Tailwind 4** uses `@import "tailwindcss"` + `@theme` directive; no `tailwind.config.js` needed

### Image Optimization for Comic/Manga Delivery (2026)

- **ImageKit** — real-time transformations, signed URLs, CDN, auto WebP/AVIF
- **Cloudinary** — generous free tier, advanced transforms, AI-based optimization
- **Next.js `next/image`** — native optimization, but limited to self-hosted/Vercel
- **Comic-specific:** multi-page chapters → serve as individual optimized images
- **Signed URLs** for paywalled content (expire after auth)
- **Preload next chapter** via `<link rel="preload">` or `priority` on `next/image`
- **Cloudinary** leads for manga/comics with smart crop, auto-quality, format selection

### Zustand + TanStack Query State Management for Reader Apps (2026)

- **TanStack Query v5** — server state (catalog, chapters, reading progress via API)
- **Zustand v5** — client-only UI state (reader mode, zoom, theme, sidebar)
- **Pattern:** TanStack Query for async/server data; Zustand for synchronous UI state
- **Integration:** custom hooks combining both — e.g., `useChapterReader(chapterId)`
- **Persistence:** Zustand `persist` middleware for reader preferences (localStorage)
- **React 19** compatible — both libraries fully support concurrent features

---

## Cheatsheets & Quick Reference

| Topic | Resource | Type |
|-------|----------|------|
| Next.js 16 | <https://nextjs.org/docs/app> | Docs |
| Drizzle ORM | <https://orm.drizzle.dev> | Docs |
| Stripe Node.js | <https://docs.stripe.com/api> | Docs |
| NextAuth v5 | <https://authjs.dev> | Docs |
| Better Auth | <https://better-auth.com> | Docs |
| BullMQ | <https://docs.bullmq.io/> | Docs |
| Upstash | <https://docs.upstash.com/> | Docs |
| TanStack Query | <https://tanstack.com/query/latest> | Docs |
| Zustand | <https://docs.pmnd.rs/zustand> | Docs |
| ImageKit | <https://imagekit.io/docs> | Docs |
| Cloudinary | <https://cloudinary.com/documentation> | Docs |
| Radix UI | <https://radix-ui.com> | Docs |
| shadcn/ui | <https://ui.shadcn.com> | Docs |
| Tailwind CSS 4 | <https://tailwindcss.com/docs> | Docs |

---

## Best Practices

1. **Server Components** — server-side render catalog; only interactions hydrate
2. **Server Actions for mutations** — `actions/` dir; `useFormState` + Zod; `revalidateTag`
3. **Drizzle DAL boundaries** — `dal/*` modules; precise select/include; `@@index` on FKs
4. **Zod as boundary contract** — validate before Server Actions and DB writes
5. **Stripe webhook idempotency** — check event ID uniqueness; verify `constructEvent`
6. **Radix UI primitives** — compose accessible comic reader UI without reinventing
7. **Tailwind 4 + shadcn** — `@import "tailwindcss"` + `@theme` for design tokens
8. **ImageKit/Cloudinary signed URLs** — protect paywalled comic content
9. **TanStack Query for server state** — cache, dedupe, prefetch next chapter
10. **Zustand for UI state** — reader mode (vertical/horizontal), zoom, theme
11. **Preload next chapter** — perceived performance for sequential reading
12. **Drizzle migration strategy** — one domain at a time; no cross-ORM transactions

---

## Common Pitfalls

| Pitfall | Impact | Avoidance |
|---------|--------|-----------|
| Dual ORM during migration | Data drift | Eschew cross-ORM transactions; migrate one domain at a time |
| Server data in client state | Stale data | TanStack Query for API; Zustand only for UI |
| Missing Stripe webhook secret | 400 errors | Set `STRIPE_WEBHOOK_SECRET`; verify signature |
| Prisma generate omitted | Build failures | Run in build step |
| NextAuth v5 beta assumptions | API changes | Pin version; read migration guide |
| Tailwind 4 config migration | Build breaks | Use `@import "tailwindcss"`; migrate `tailwind.config.js` |
| Unsigned image URLs | Content theft | Sign URLs for subscriber-only content |
| Client-side auth state | Hydration mismatch | NextAuth v5 `useSession` with Server Components |

---

## Performance

1. **`next/image` for catalog** — CDN signed URLs for chapter images
2. **Cache static metadata** — `force-static` + `revalidateTag`
3. **Aggregate in DAL** with `include` + nested `where`
4. **Preload next chapter** hints for perceived load reduction
5. **Partial Prerendering (PPR)** — static shell + dynamic streams
6. **Turbopack** — faster dev/build in Next.js 16+
7. **Drizzle edge runtime** — smaller bundles for serverless
8. **Upstash Redis** — global replication, zero cold starts for caching

---

## Security

1. **Validate image paths** before storage; signed URLs for paywalled content
2. **Strip HTML from reviews** despite client-side sanitization
3. **Secrets in `.env.local` only** — different keys per environment
4. **Rotate `NEXTAUTH_SECRET`** regularly
5. **Verify Stripe webhooks** with `constructEvent()`
6. **WebAuthn/Passkeys** — phishing-resistant auth for subscribers
7. **Rate limit** auth endpoints via Upstash Redis
8. **CSP headers** for comic reader iframe/content security

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
| Next.js 16 | <https://nextjs.org/docs> | Framework docs |
| Drizzle ORM | <https://orm.drizzle.dev> | TypeScript ORM |
| Stripe Webhooks | <https://docs.stripe.com/billing/subscriptions/webhooks> | Webhook guide |
| TanStack Query | <https://tanstack.com/query/latest/docs> | Server state mgmt |
| Zustand | <https://docs.pmnd.rs/zustand> | Client state mgmt |
| NextAuth v5 | <https://authjs.dev> | Auth.js v5 docs |
| Better Auth | <https://better-auth.com> | Modern auth alternative |
| ImageKit | <https://imagekit.io/docs> | Image CDN/optimization |
| Cloudinary | <https://cloudinary.com/documentation> | Media management |
| Radix UI | <https://radix-ui.com> | Headless UI primitives |
| shadcn/ui | <https://ui.shadcn.com> | Component library |
| Tailwind CSS 4 | <https://tailwindcss.com/docs> | CSS framework v4 |
| BullMQ | <https://docs.bullmq.io/> | Queue system |
| Upstash | <https://docs.upstash.com/> | Serverless Redis/QStash |
| WebAuthn Guide | <https://webauthn.guide> | Passkey implementation |

---

## 2026 Research Updates (Section 2 Queries)

### Query 1: Next.js 15/16 App Router comic streaming platform patterns
**Key findings (2026):**
- Next.js 16.2.6 (May 2026) ships Turbopack default, React 19.2, Cache Components (`"use cache"`), async `params`, renamed `proxy.ts` middleware
- Partial Prerendering (PPR) enables static shell + dynamic streaming
- Server Actions stable for mutations; use with `useFormState` + Zod
- Streaming via `loading.tsx` + Suspense boundaries for progressive comic page loads
- App Router patterns: Server Components by default, Client Components for reader UI

### Query 2: Prisma to Drizzle migration guide 2026
**Key findings (2026):**
- Drizzle v1 stable (0.45+), Prisma 7 rewrote engine in TypeScript
- Bundle size: Drizzle ~50KB vs Prisma ~500KB+ — major factor for serverless/edge
- Migration path: dual-ORM during transition, migrate domain-by-domain
- Drizzle: SQL-first, type-safe, no codegen, edge-compatible
- Prisma: schema-first, Prisma Studio, wider DB support (MongoDB), mature migrations

### Query 3: Stripe subscription management for digital content platforms
**Key findings (2026):**
- Stripe Billing 0.7% on subscription volume
- Embedded Checkout (no redirect), Customer Portal ($10/mo custom domain)
- Server Actions for checkout session creation
- Webhook idempotency via `constructEvent()` + event ID deduplication
- Usage-based/metered billing supported for consumption-based models
- Paywall patterns: webhook-driven access control + signed content URLs

### Query 4: NextAuth v5 beta with WebAuthn passkeys implementation
**Key findings (2026):**
- Auth.js v5 (NextAuth rebrand) in beta since 2023, production-ready
- WebAuthn via `@auth/webauthn` or `better-auth` plugins
- Migration guide at `authjs.dev/getting-started/migrating-to-v5`
- Better Auth gaining traction: plugin model, TypeScript-first, self-hosted
- Clerk leads for hosted auth with org/billing UI
- NextAuth v5 still beta tag but widely used in production

### Query 5: Radix UI + shadcn/ui + Tailwind 4 comic reader components
**Key findings (2026):**
- Tailwind 4: Vite-based, CSS-first, `@import "tailwindcss"`, `@theme` directive
- shadcn/ui compatible via `@tailwindcss/postcss` plugin
- Radix primitives: Dialog (reader modal), Slider (page nav), ScrollArea (webtoon), Keyboard navigation hooks
- Comic reader patterns: vertical scroll (webtoon), horizontal paginated (manga), zoom/pan, chapter selector
- Design tokens in CSS via `@theme` — no `tailwind.config.js` needed

### Query 6: Image optimization for comic/manga delivery (ImageKit, Cloudinary)
**Key findings (2026):**
- ImageKit: real-time transforms, signed URLs, auto WebP/AVIF, global CDN
- Cloudinary: generous free tier, AI smart crop, auto quality/format, advanced transforms
- Next.js `next/image` limited to self-hosted/Vercel; less flexible for comic pipelines
- Signed URLs essential for subscriber-only chapter images
- Preload next chapter via `<link rel="preload">` or `priority` on `next/image`
- Multi-page chapters served as individual optimized images

### Query 7: Zustand + TanStack Query state management for reader apps
**Key findings (2026):**
- TanStack Query v5: server state (catalog, chapters, reading progress sync)
- Zustand v5: client UI state (reader mode, zoom, theme, sidebar, preferences)
- Pattern separation: async/server → TanStack Query; sync/UI → Zustand
- Custom hooks combine both: `useChapterReader(chapterId)`
- Zustand `persist` middleware for localStorage reader preferences
- Both fully React 19 compatible with concurrent features