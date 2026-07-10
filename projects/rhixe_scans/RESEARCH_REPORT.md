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
- **Alternative:** Server-Sent Events (SSE) or Socket.io for serverless-compatible real-time
- SSE is built-in browser API, works over standard HTTP, perfect for notifications/progress
- For WebSocket on serverless: use custom Node server with `ws` library or Socket.io with adapter

### Prisma 6 Singleton Pattern

- Create `lib/prisma.ts` with global singleton to prevent hot-reload connection leaks
- `prisma.config.ts` (new in 6.x) for configuration; migration from 5.x updates setup
- Prisma Accelerate for serverless connection pooling in production
- **Performance:** Prisma 6 offers JOIN strategy selection (`relationLoadStrategy: "join" | "query"`)
- Nested create operations now batched in single round-trip (since v5.11)
- Edge-ready with serverless drivers (Neon, PlanetScale) via driver adapters
- Multi-file schema support (v5.15+) for organizing large schemas

### Stripe + PayPal Integration

- Stripe webhooks in App Router: **must use `request.text()` (not `request.json()`)** for signature verification
- PayPal: `@paypal/react-paypal-js` frontend + server-side order capture validation
- Always idempotent webhook handlers; use database transactions
- Webhook router pattern: typed handlers per event type for maintainability
- Stripe Payment Element supports unified payment methods (cards, PayPal, iDeal, etc.)
- PayPal Standard Checkout: client SDK + server-side order creation/capture

### UploadThing + Media

- Type-safe File Routes; presigned URLs + CDN delivery
- Re-sign URLs on key rotation; never permanent URLs for paywalled content
- Middleware auth + `onUploadComplete` callback for DB persistence
- SSR plugin (`@uploadthing/react/next-ssr-plugin`) avoids loading state
- Next.js 15: wrap SSR plugin in Suspense + `await connection()` for PPR/dynamicIO
- FileRouter supports multiple routes (imageUploader, chapterUploader, etc.) with custom middleware per route

### NextAuth v5 with Supabase Adapter

- **Note:** Auth.js (NextAuth v5) is now part of Better Auth — consider migration
- Supabase adapter: community-maintained, uses separate `next_auth` schema
- Does NOT integrate with Supabase Auth (email/phone/MFA) — separate standalone auth server
- v5 breaking changes: `NextAuthOptions` → `NextAuthConfig`, universal `auth()` function
- Cookie prefix renamed `next-auth` → `authjs`
- Adapters: Prisma, Drizzle, Supabase, Neon, etc. available
- Use `auth()` instead of `getServerSession`, `getSession`, `withAuth`, `getToken`, `useSession`

### WebSocket Real-Time Features for Reading Progress Sync

- **Vercel serverless limitation:** WebSockets require stateful server — use Fly.io, Railway, or custom Node
- **SSE alternative:** Server-Sent Events work on Vercel, unidirectional server→client push
- Perfect for: chapter release notifications, reading progress sync, live progress bars
- Implementation: dedicated WebSocket server + Redis Pub/Sub for multi-instance scaling
- Client: `useWebSocket` hook or native WebSocket API with reconnection logic
- For reading progress: debounce updates (e.g., every 5s), batch sync on chapter change

### TanStack Query + Zustand for Comic Library State Management

- **TanStack Query (v5):** Server state — caching, synchronization, background refetch
- **Zustand:** Client/UI state — modals, theme, reading preferences, draft state
- **Separation principle:** Server state (comics, chapters, user library) → TanStack Query; Client state (reader settings, UI toggles) → Zustand
- With RSC: Server Components fetch directly; TanStack Query for client components needing interactivity
- Comic reader patterns: preload next chapter, cache cover metadata aggressively, chapter content per release
- Zustand persist middleware for reading preferences (theme, scroll direction, fit mode)

### Prisma 6 Performance Optimization for Large Comic Catalogs

- **Indexes:** Critical for large datasets — `@@index([fields])` on frequently queried columns
- **JOIN strategy:** Use `relationLoadStrategy: "join"` for related data to avoid n+1
- **Query Insights:** Enable `@prisma/sqlcommenter-query-insights` for Prisma ORM attribution
- **Bulk operations:** `createMany()`, `createManyAndReturn()`, `updateMany()`, `deleteMany()`
- **Connection pooling:** Prisma Accelerate or PgBouncer for serverless
- **Avoid n+1:** Use `include` (2 queries) or `in` filter (2 queries) or `relationLoadStrategy: "join"` (1 query)
- **Pagination:** Cursor-based for infinite scroll, offset for catalog pages
- **Edge support:** Driver adapters for Neon/PlanetScale serverless drivers

---

## Cheatsheets & Quick Reference

| Topic | Resource | Type |
|-------|----------|------|
| Next.js 15 | <https://nextjs.org/docs> | Docs |
| Prisma 6/7 | <https://www.prisma.io/docs> | Docs |
| NextAuth v5 | <https://authjs.dev/getting-started> | Docs |
| UploadThing | <https://docs.uploadthing.com> | Docs |
| Stripe Webhooks | <https://docs.stripe.com/webhooks> | Guide |
| TanStack Query | <https://tanstack.com/query/latest> | Docs |
| Prisma Query Optimization | <https://www.prisma.io/docs/orm/prisma-client/queries/advanced/query-optimization-performance> | Docs |
| Auth.js v5 Migration | <https://authjs.dev/getting-started/migrating-to-v5> | Guide |
| SSE in Next.js | <https://www.pedroalonso.net/blog/sse-nextjs-real-time-notifications> | Tutorial |
| Prisma 6 Blog | <https://www.prisma.io/blog/prisma-6-better-performance-more-flexibility-and-type-safe-sql> | Blog |

---

## Best Practices

1. **Singleton Prisma** — global client prevents connection exhaustion during hot-reload
2. **Raw body for webhooks** — `request.text()` for Stripe signature verification
3. **Signed URLs** — re-sign UploadThing on rotation; serve paywalled content only after auth
4. **Server Components** — render catalog server-side; cache with `revalidateTag`
5. **Zod validation** — validate all API inputs before Prisma writes
6. **State separation** — TanStack Query for server state, Zustand for client/UI state
7. **Index strategy** — add `@@index` on high-cardinality query fields (series, chapter number, user+series)
8. **Connection pooling** — Prisma Accelerate or PgBouncer for serverless production
9. **SSE over WebSocket** — for Vercel deployments, use SSE for real-time features
10. **Typed webhooks** — router pattern with handlers per event type

---

## Common Pitfalls

| Pitfall | Impact | Avoidance |
|---------|--------|-----------|
| Prisma pool exhaustion | 500s on hot-reload | singleton pattern in `lib/prisma.ts` |
| Stripe webhook JSON body | signature verification fails | `request.text()` not `request.json()` |
| WebSocket on Vercel | silent failure | custom server or SSE alternative |
| UploadThing permanent URLs | broken after key rotation | re-sign URLs; short-lived tokens |
| Prisma 6 config breakage | build failures | migrate to `prisma.config.ts` |
| n+1 queries in catalog | exponential slowdown | `include`, `in` filter, or `relationLoadStrategy: "join"` |
| Client-state in TanStack Query | cache pollution | Zustand for UI state, TanStack for server state |
| Supabase adapter + Supabase Auth | confusion | adapter is standalone; doesn't use Supabase Auth |

---

## Performance

1. **Preload next chapter** — response hints reduce perceived load time
2. **Cache cover metadata** — aggressively; chapter content per release
3. **`next/image` for catalog** — CDN signed URLs for chapter images
4. **ISR for product pages** — Incremental Static Regeneration
5. **Redis Pub/Sub for WebSocket** — broadcast across multiple server instances
6. **Cursor pagination** — for infinite scroll chapter lists
7. **Bulk inserts** — `createManyAndReturn()` for batch chapter uploads
8. **Query Insights** — enable `@prisma/sqlcommenter-query-insights` for production monitoring

---

## Security

1. **Rotate `NEXTAUTH_SECRET`** regularly; never in browser bundle
2. **Rate-limit chapter and download endpoints** — reduce scraping risk
3. **Validate upload content types** server-side — reject non-images before Prisma insert
4. **Verify all webhook signatures** — Stripe `constructEvent()`, PayPal headers
5. **Signed URLs for paywalled chapters** — always auth-check before serving
6. **UploadThing middleware auth** — verify user before generating upload URLs
7. **CSP headers** — restrict script/style sources for XSS protection
8. **CSRF protection** — NextAuth v5 handles automatically with cookie-based sessions

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
| Next.js | <https://nextjs.org/docs> | Framework docs |
| Prisma | <https://www.prisma.io/docs> | ORM docs |
| Auth.js v5 | <https://authjs.dev/getting-started> | Auth docs |
| Stripe Webhooks | <https://docs.stripe.com/webhooks> | Webhook guide |
| UploadThing | <https://docs.uploadthing.com> | Upload docs |
| TanStack Query | <https://tanstack.com/query/latest> | Query docs |
| Prisma Query Optimization | <https://www.prisma.io/docs/orm/prisma-client/queries/advanced/query-optimization-performance> | Performance guide |
| Auth.js v5 Migration | <https://authjs.dev/getting-started/migrating-to-v5> | Migration guide |
| SSE in Next.js | <https://www.pedroalonso.net/blog/sse-nextjs-real-time-notifications> | SSE tutorial |
| Prisma 6 Blog | <https://www.prisma.io/blog/prisma-6-better-performance-more-flexibility-and-type-safe-sql> | Release notes |

---

## Query-Specific Deep Dives (Section 8 from per-project-research-queries.md)

### 1. Next.js 15 + Prisma 6 Comic Reader Platform Patterns

**Key findings from research:**
- Prisma 6 introduces `relationLoadStrategy` for JOIN vs query-level strategy selection
- Nested create operations batched in single round-trip (v5.11+)
- Edge-ready with serverless drivers (Neon, PlanetScale) via driver adapters
- Multi-file schema support for organizing large comic catalog schemas
- `createManyAndReturn()` for bulk chapter/page creation with returned records
- `omit` option to exclude sensitive fields (e.g., `password`) from query results
- TypedSQL for type-safe raw SQL when needed for complex analytics queries

**Comic-specific patterns:**
- Chapter reader: Server Component for initial page, Client Component for navigation controls
- Catalog: ISR with `revalidateTag` on new chapter publish
- Image delivery: `next/image` with UploadThing signed URLs + `Cache-Control` headers
- Reading progress: debounced sync to DB via Server Action or API route

### 2. Dual Payment Provider (Stripe + PayPal) Integration Next.js

**Stripe (Primary):**
- App Router webhook: `request.text()` for raw body → `stripe.webhooks.constructEvent()`
- Payment Element for unified UI (cards, PayPal, local methods)
- Subscription management: Stripe Billing Portal + webhook sync
- Webhook router pattern: typed handlers per event type (`invoice.payment_succeeded`, `customer.subscription.updated`)

**PayPal (Secondary):**
- `@paypal/react-paypal-js` for client-side SDK loading
- Server-side: Orders v2 API (`/v2/checkout/orders` create + capture)
- Webhook verification: check `PAYPAL-TRANSMISSION-SIG` header + `PAYPAL-CERT-URL`
- Supports: one-time payments, subscriptions (billing plans)

**Integration pattern:**
- Unified payment service abstraction
- Database: `PaymentProvider` enum (STRIPE | PAYPAL)
- Idempotency keys on all payment operations
- Transactional webhook handlers with Prisma `$transaction`

### 3. UploadThing File Upload for Comic/Manga Images

**FileRouter design for comics:**
```typescript
// Multiple routes for different upload types
imageUploader: f({ image: { maxFileSize: '8MB', maxFileCount: 1 } })
  .middleware(authMiddleware)
  .onUploadComplete(saveToDB),

chapterUploader: f({ image: { maxFileSize: '4MB', maxFileCount: 50 } })
  .middleware(adminAuthMiddleware)
  .onUploadComplete(saveChapterPages),

coverUploader: f({ image: { maxFileSize: '4MB', maxFileCount: 1 } })
  .middleware(authMiddleware)
  .onUploadComplete(updateSeriesCover),
```

**Security:**
- Middleware validates user permissions before presigned URL generation
- `onUploadComplete` runs on YOUR server — persist metadata, associate with chapter/series
- Never trust client-provided file paths; use UploadThing's `file.ufsUrl`

**Performance:**
- SSR plugin eliminates loading flash
- CDN delivery via UploadThing's global edge network
- Automatic image optimization (WebP conversion, resize)

### 4. NextAuth v5 with Supabase Adapter Patterns

**Important caveat:** Auth.js (NextAuth v5) is now part of **Better Auth**. Consider migration path.

**Supabase Adapter:**
- Community-maintained (`@auth/supabase-adapter`)
- Stores users/sessions in separate `next_auth` schema in Supabase PostgreSQL
- Does NOT integrate with Supabase Auth (email/password, MFA, phone)
- Use if: you want NextAuth providers + Supabase Postgres as DB

**v5 Migration highlights:**
- Config: `NextAuthOptions` → `NextAuthConfig`
- Universal `auth()` function replaces `getServerSession`, `getSession`, `withAuth`, `getToken`, `useSession`
- Cookie prefix: `next-auth` → `authjs`
- Adapter types re-exported from `@auth/core/adapters`
- Route handler: `createRouteHandler(config)` exports `GET`, `POST`

### 5. WebSocket Real-Time Features for Reading Progress Sync

**Architecture options:**

| Approach | Vercel Compatible | Bidirectional | Complexity |
|----------|-------------------|---------------|------------|
| Native WebSocket + custom Node server | ❌ | ✅ | High |
| Socket.io + custom Node server | ❌ | ✅ | Medium |
| **SSE (Server-Sent Events)** | ✅ | ❌ (server→client only) | **Low** |
| Pusher/Ably (managed) | ✅ | ✅ | Low (paid) |
| Upstash QStash + SSE | ✅ | ✅ (via webhook) | Low |

**Recommended for rhixe_scans on Vercel:**
- **SSE for notifications:** Chapter releases, comments, system alerts
- **Reading progress:** Debounced API calls (every 5-10s) → DB → SSE broadcast to other tabs/devices
- **Multi-tab sync:** BroadcastChannel API for local tabs + SSE for cross-device

**Implementation pattern:**
```typescript
// app/api/reading-progress/stream/route.ts (SSE)
export async function GET(req: Request) {
  const stream = new ReadableStream({
    start(controller) {
      // Subscribe to Redis channel for user's progress updates
      const encoder = new TextEncoder();
      controller.enqueue(encoder.encode(`data: ${JSON.stringify({ type: 'connected' })}\n\n`));
    }
  });
  return new Response(stream, { headers: { 'Content-Type': 'text/event-stream' } });
}
```

### 6. TanStack Query + Zustand for Comic Library State Management

**State separation:**
| State Type | Examples | Library |
|------------|----------|---------|
| **Server State** | Comic catalog, chapters, reading history, user library, subscriptions | TanStack Query |
| **Client State** | Reader settings (theme, fit, direction), UI modals, draft comments, reading progress (unsynced) | Zustand |

**TanStack Query patterns for comics:**
```typescript
// Query keys for invalidation
const queryKeys = {
  series: (id: string) => ['series', id],
  chapters: (seriesId: string) => ['chapters', seriesId],
  chapterPages: (chapterId: string) => ['chapter-pages', chapterId],
  library: (userId: string) => ['library', userId],
  readingProgress: (userId: string, seriesId: string) => ['progress', userId, seriesId],
};

// Prefetch next chapter
queryClient.prefetchQuery({
  queryKey: queryKeys.chapterPages(nextChapterId),
  queryFn: () => fetchChapterPages(nextChapterId),
});
```

**Zustand store for reader:**
```typescript
interface ReaderState {
  fitMode: 'width' | 'height' | 'original';
  readingDirection: 'ltr' | 'rtl' | 'vertical';
  theme: 'light' | 'dark' | 'sepia';
  setFitMode: (mode: FitMode) => void;
  // persist to localStorage
}
```

### 7. Prisma 6 Performance Optimization for Large Comic Catalogs

**Schema indexing strategy:**
```prisma
model Series {
  id          String   @id @default(cuid())
  slug        String   @unique
  title       String
  author      String
  status      SeriesStatus
  createdAt   DateTime @default(now())
  updatedAt   DateTime @updatedAt

  @@index([status, updatedAt]) // For "latest updates" query
  @@index([author])            // Author pages
  @@index([title])             // Search
}

model Chapter {
  id        String   @id @default(cuid())
  seriesId  String
  number    Float
  title     String?
  publishedAt DateTime?
  pages     Page[]

  @@index([seriesId, number])      // Chapter list for series
  @@index([seriesId, publishedAt]) // Published chapters
  @@unique([seriesId, number])
}

model Page {
  id        String   @id @default(cuid())
  chapterId String
  number    Int
  imageUrl  String
  width     Int?
  height    Int?

  @@index([chapterId, number]) // Page order in chapter
}

model ReadingProgress {
  id        String   @id @default(cuid())
  userId    String
  seriesId  String
  chapterId String
  pageNumber Int
  updatedAt DateTime @updatedAt

  @@unique([userId, seriesId])
  @@index([userId, updatedAt]) // Recent reading history
}
```

**Query optimization patterns:**
- Chapter reader: `relationLoadStrategy: "join"` for `chapter.pages`
- Catalog: cursor pagination with `findMany({ take: 20, cursor: { id: lastId } })`
- Library: `include: { series: { include: { latestChapter: true } } }` (2 queries)
- Bulk chapter creation: `createManyAndReturn()` for upload workflows
- Query Insights: `@prisma/sqlcommenter-query-insights` for production monitoring

**Connection pooling:**
- Development: singleton pattern in `lib/prisma.ts`
- Production (Vercel): Prisma Accelerate or PgBouncer
- Edge: Neon/PlanetScale serverless drivers with driver adapters

---

## Resources

| Resource | URL | Description |
|----------|-----|-------------|
| Next.js | <https://nextjs.org/docs> | Framework docs |
| Prisma | <https://www.prisma.io/docs> | ORM docs |
| Auth.js v5 | <https://authjs.dev/getting-started> | Auth docs |
| Stripe Webhooks | <https://docs.stripe.com/webhooks> | Webhook guide |
| UploadThing | <https://docs.uploadthing.com> | Upload docs |
| TanStack Query | <https://tanstack.com/query/latest> | Query docs |
| Prisma Query Optimization | <https://www.prisma.io/docs/orm/prisma-client/queries/advanced/query-optimization-performance> | Performance guide |
| Auth.js v5 Migration | <https://authjs.dev/getting-started/migrating-to-v5> | Migration guide |
| SSE in Next.js | <https://www.pedroalonso.net/blog/sse-nextjs-real-time-notifications> | SSE tutorial |
| Prisma 6 Blog | <https://www.prisma.io/blog/prisma-6-better-performance-more-flexibility-and-type-safe-sql> | Release notes |