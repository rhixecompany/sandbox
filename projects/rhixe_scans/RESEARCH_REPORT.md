# RESEARCH_REPORT.md

## Project: rhixe_scans

**Type:** Comic / scan reader platform  
**Tech Stack:** Next.js 15, React 19, TypeScript strict, Prisma 6, PostgreSQL, Tailwind 3, shadcn/ui, Radix, NextAuth v5, Zustand, TanStack Query, Stripe, PayPal, UploadThing, Resend, WebSocket  
**Status:** Active  

---

## Similar Projects

| Project | URL | Why Relevant |
|---------|-----|--------------|
| comicwise | `projects/comicwise` | Shared Next.js + Tailwind + Stripe reader flows. |
| rhixecompany-comics | `projects/rhixecompany-comics` | Comic reader sibling adding scraping import surface cadence. |
| university-library-jsm | `projects/university-library-jsm` | Next.js + Prisma + PostgreSQL library catalog patterns. |
| banking | `projects/banking` | NextAuth v5 + Prisma + PostgreSQL auth + payment patterns. |

---

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
  Prisma Postgres handles pooling/scaling automatically in production [2].
- **Migration workflow**: `npx prisma migrate dev --name init` → `npx prisma generate` → `npx prisma db seed` → `npx prisma studio` [2].
- **Prisma 7 (Nov 2025)** ditches Rust query engine for TypeScript runtime: up to 3x faster queries, ~90% smaller bundles [3].
- **Use `prisma.config.ts`** for declarative config (schema path, migrations path, datasource URL, seed command) [4].

### NextAuth v5 (Auth.js) JWT Sessions + Multiple Providers (2026)

- **Edge Runtime limitation**: OAuth/OIDC providers **not supported** on Edge runtime (used by Middleware) due to `oidc-token-hash` accessing `process.version` [5]. Use Node.js runtime for middleware or restrict to credential/email providers on Edge.
- **Session callback not invoked on server** in v5 — major breaking change from v4. Workarounds: (a) switch to JWT strategy and use `jwt` callback, (b) add custom fields to User table via DB adapter, or (c) patch `@auth/core` (not recommended) [5].
- **JWT token persistence pattern**: `account` parameter only available during initial sign-in. Must persist tokens in JWT during first `jwt` callback:
  ```typescript
  async jwt({ token, user, account }) {
    if (account && user) {
      return { accessToken: account.access_token, accessTokenExpires: Date.now() + account.expires_in * 1000, refreshToken: account.refresh_token, user };
    }
    return token; // subsequent calls read from token
  }
  ```
  Implement token refresh logic for production [6].
- **Multiple email providers not allowed** — `id` enforced to `"email"` [5].
- **Corporate proxy support** dropped in v5 (migration to `oauth4webapi` uses `fetch`, no agent support) [5].
- **Middleware + `server-only` conflict**: Auth config files marked `server-only` crash middleware. Keep sensitive config out of middleware imports [5].
- **Environment variables**: `NEXTAUTH_SECRET` required in production (generate via `npx auth secret`), `NEXTAUTH_URL` auto-detected on Vercel [7].

### UploadThing Next.js Image Storage + CDN (2026)

- **Core model**: Define type-safe "file routes" server-side specifying allowed types, sizes, auth; UploadThing handles presigned URLs, hosting, CDN delivery, webhooks [8].
- **Server-side file router pattern**:
  ```typescript
  export const imageUploader = createUploadthing({
    image: { maxFileSize: '4MB' },
    middleware: async (req) => { const user = await getCurrentUser(); if (!user) throw new UploadThingError('Unauthorized'); return { userId: user.id } },
    onUploadComplete: async ({ metadata, file }) => { await userFiles.create({ data: { userId: metadata.userId, url: file.url } }) },
  }) satisfies FileRouter;
  ```
- **Client-side**: `<UploadButton endpoint="imageUploader" onClientUploadComplete={...} />` with typed router [8].
- **Pricing 2026**: Free 2GB/1GB BW; Starter $10/mo (50GB); Pro $30/mo (200GB); Enterprise custom [8].
- **Cloudflare R2 comparison**: Zero egress fees ($0.015/GB storage, $4.50/M writes, $0.36/M reads) beats UploadThing at scale (>500GB downloads) [8].
- **Limitations**: No BYO S3 bucket, closed-source backend, $0.08/GB overages, TypeScript/Next.js lock-in [9].
- **Tailwind integration**: `import { withUt } from "uploadthing/tw"; export default withUt({...})` injects UploadThing styles [10].

### Stripe + PayPal Dual Payments Next.js 2026 Webhooks

- **2026 architecture shift**: Server Actions + Embedded Checkout (iframe/web component, stays on your domain) replace legacy API routes + hosted redirect [11].
- **Server Action for checkout**:
  ```typescript
  "use server";
  export async function createCheckoutSession(priceId: string) {
    const origin = (await headers()).get("origin");
    const session = await stripe.checkout.sessions.create({
      ui_mode: 'embedded',
      line_items: [{ price: priceId, quantity: 1 }],
      mode: 'subscription',
      return_url: `${origin}/return?session_id={CHECKOUT_SESSION_ID}`,
    });
    return { clientSecret: session.client_secret };
  }
  ```
- **Embedded Checkout client**:
  ```tsx
  <EmbeddedCheckoutProvider stripe={stripePromise} options={{ fetchClientSecret }}>
    <EmbeddedCheckout />
  </EmbeddedCheckoutProvider>
  ```
- **Webhooks still require Route Handlers** (static URL for Stripe to ping). Critical: return 200 within 10s or Stripe retries for 72hrs with exponential backoff [11][12].
- **Webhook signature verification**:
  ```typescript
  const body = await req.text();
  const signature = headers().get('stripe-signature');
  const event = stripe.webhooks.constructEvent(body, signature, process.env.STRIPE_WEBHOOK_SECRET!);
  ```
- **Critical subscription webhook events**: `checkout.session.completed`, `customer.subscription.updated`, `customer.subscription.trial_will_end`, `invoice.payment_succeeded`, `invoice.payment_failed`, `customer.subscription.deleted` [12].
- **PayPal dual-integration**: Split Stripe and PayPal webhook verifiers into separate route handlers for incident isolation [existing finding].
- **Stripe Tax**: Enable `automatic_tax: { enabled: true }` in checkout session (requires dashboard setup) [13].
- **Metadata traceability**: Use `client_reference_id: userId` + `metadata: { userId }` on session AND `subscription_data: { metadata: { userId } }` for webhook linkage [13].

### Zustand + TanStack Query + React 19 State Management (2026)

- **Modern stack for 95% of apps**: **TanStack Query + Zustand + URL state** [14].
- **Decision framework**:
  | State Type | Tool |
  |------------|------|
  | Server data | TanStack Query (always) |
  | Form data | React Hook Form + Zod |
  | Shareable/bookmarkable | URL state (`useSearchParams`) |
  | Component-local | `useState` / `useReducer` |
  | Global client (simple) | Zustand |
  | Global client (granular) | Jotai |
  | Complex enterprise | Redux Toolkit |
  | Read-mostly config | React Context |
- **Zustand advantages**: 1.2KB gzipped, zero boilerplate, selector-based subscriptions (fine-grained re-renders), no providers needed, works outside React tree, TypeScript-first, SSR compatible with Next.js App Router [14].
- **Zustand pattern with middleware**:
  ```typescript
  export const useCartStore = create<CartState>()(
    devtools(persist((set) => ({ items: [], addItem: (item) => set(...), ... }), { name: 'cart-storage' }), { name: 'CartStore' })
  );
  // Component subscribes ONLY to needed slice
  const count = useCartStore((state) => state.items.length);
  ```
- **TanStack Query**: Built-in caching, background refetching, synchronization — essential for API-heavy apps [15].
- **React Context anti-pattern**: Single big context causes unnecessary re-renders on any value change. Split by update frequency + memoize [14].
- **Hybrid approach**: Zustand/Redux for local client state + TanStack Query for server state [15].

---

## Architecture Patterns (2026 Updates)

### Database & ORM
- Use **Prisma Postgres** (serverless) for zero-ops PostgreSQL on Vercel [2].
- **Connection pooling**: Prisma Accelerate extension (`@prisma/extension-accelerate`) for edge/serverless [2][4].
- **Migration naming**: Descriptive names (`--name init`, `--name add-chapter-images`) [2].
- **Seed via `prisma.config.ts`**: `seed: 'tsx prisma/seed.ts'` [4].

### Authentication
- **JWT strategy default** (no adapter needed) — sessions in encrypted cookie [7].
- **Multiple OAuth providers**: Each provider config in `providers` array; use `account.provider` in callbacks to differentiate [5][6].
- **Session data enrichment**: Custom fields via `jwt` callback → `session` callback [6].
- **Middleware auth**: `export { auth as middleware } from '@/auth'` with `matcher` config [5].

### File Uploads
- **UploadThing file routes** = server-side schema + auth + post-upload hook [8][10].
- **Store `fileKey` + `url` + metadata in Prisma** for audit trail and re-signing [existing finding].
- **Tailwind plugin**: `withUt` wrapper required for UploadThing styles [10].

### Payments
- **Server Actions for checkout creation** (eliminates `/api/checkout` routes) [11].
- **Embedded Checkout** = higher conversion, no redirect, PCI handled by Stripe [11].
- **Webhook route handlers** = separate files per provider (`/api/webhooks/stripe`, `/api/webhooks/paypal`) [11][existing].
- **Idempotency**: Handle duplicate webhook events via event ID tracking in DB [12].
- **Customer Portal**: Stripe Billing Portal for self-service subscription management [13].

### State Management
- **Server state** → TanStack Query (caching, deduping, background refresh) [14][15].
- **Client state** → Zustand (global UI: cart, modals, theme toggle, reader settings) [14].
- **URL state** → `useSearchParams` for filters, pagination, reader view mode (shareable URLs) [14].
- **Forms** → React Hook Form + Zod validation [14].

---

## Cheatsheets & Quick Reference

| Topic | Resource | Type |
|-------|----------|------|
| Next.js 15 docs | https://nextjs.org/docs | Docs |
| Prisma 6/7 docs | https://www.prisma.io/docs | ORM docs |
| NextAuth v5 (Auth.js) | https://authjs.dev | Auth guide |
| UploadThing docs | https://docs.uploadthing.com | File uploads |
| Stripe docs | https://stripe.com/docs | Payments |
| PayPal docs | https://developer.paypal.com | Payments |
| Zustand docs | https://zustand.docs.pmnd.rs | State mgmt |
| TanStack Query docs | https://tanstack.com/query | Data fetching |
| React 19 docs | https://react.dev | Framework |

---

## Best Practices (Updated 2026)

1. **Prisma transaction scope** — keep webhook intake inside a Prisma `$transaction` so reader state stays consistent [existing].
2. **Signed reader access** — require signed chapter URLs when content is paywalled [existing].
3. **Email resend pipeline** — send from background job; do not call Resend inside route handlers [existing].
4. **Route handler validation** — validate Stripe + PayPal headers and event types before trusting payloads [existing].
5. **Reader cache keys** — key cache by slug + chapter number to reduce DB load on popular series [existing].
6. **Server Actions for mutations** — use `"use server"` for checkout, mutations, form submissions; eliminates API routes [11].
7. **Embedded Checkout** — prefer `ui_mode: 'embedded'` over hosted redirect for conversion [11].
8. **Zustand selector subscriptions** — subscribe to minimal state slices to avoid re-renders [14].
9. **TanStack Query keys** — structured keys `['chapters', seriesSlug, chapterNum]` for invalidation [14].
10. **Webhook idempotency** — store processed `event.id` in DB with unique constraint [12].

---

## Common Pitfalls (Updated 2026)

| Pitfall | Impact | Avoidance |
|---------|--------|-----------|
| UploadThing URLs treated as permanent | Broken chapter images | Re-sign URLs and handle key rotation [existing] |
| Client-chosen payment method | Fraud or inventory inconsistencies | Lock payment method at order-creation server-side [existing] |
| Next.js Image on protected content | Cache leakage | Use signed URLs, not unguarded public image endpoints [existing] |
| Mixed webhook ownership | Duplicate payment intents | Choose one payment source of truth per checkout session [existing] |
| Prisma 6.0.1 migration bug | `can-connect-to-database` failure | Wait for patch; track GitHub #25835 [1] |
| Edge middleware + OAuth | Build crash (`oidc-token-hash`) | Use Node.js runtime for auth middleware [5] |
| Session callback not on server | Custom user data inaccessible | Use JWT strategy + `jwt` callback [5] |
| Single big React Context | Unnecessary re-renders | Split contexts by update frequency + memoize [14] |
| Missing webhook idempotency | Duplicate subscriptions/charges | Store `event.id` with unique constraint [12] |
| No token refresh logic | Expired access tokens break API calls | Implement refresh in `jwt` callback [6] |

---

## Performance (Updated 2026)

1. **Preload next chapter** response hints in chapter list to reduce perceived load [existing].
2. **Cache reader cover metadata** aggressively; chapter content changes per release [existing].
3. **Reduce bundle size** by splitting `@dnd-kit` into reader-only routes [existing].
4. **Prisma query logging in dev** to detect hidden N+1s in reader history queries [existing].
5. **TanStack Query `staleTime`** — set 30-60s for reader metadata to dedupe requests [14].
6. **Zustand `persist` middleware** — hydrate cart/reader settings from localStorage on load [14].
7. **Embedded Checkout** — no full-page redirect reduces navigation overhead [11].
8. **Server Components for data fetching** — move DB queries to RSC, pass data to client components [2].
9. **Image optimization** — `next/image` with UploadThing signed URLs, `placeholder="blur"` [existing+10].
10. **WebSocket for real-time** — reader presence, chapter updates, notifications without polling [existing].

---

## Security (Updated 2026)

1. **Rotate `NEXTAUTH_SECRET`** regularly and never expose to browser bundle [existing].
2. **Rate-limit** chapter generation and download endpoints to reduce scraping risk [existing].
3. **Validate upload content types** server-side before Prisma insert [existing].
4. **Keep Stripe webhook secret + PayPal client secret** in server-only env variables [existing].
5. **JWT token encryption** — NextAuth v5 uses JWE by default; do not disable [7].
6. **Webhook signature verification** — mandatory on every request; reject invalid signatures with 400 [11][12].
7. **Embedded Checkout** — PCI compliance handled by Stripe iframe; no card data touches your server [11].
8. **Metadata traceability** — `client_reference_id` + `metadata.userId` on session AND subscription [13].
9. **CORS on UploadThing** — file routes enforce auth in middleware before presign [8].
10. **Content Security Policy** — restrict `frame-src` to Stripe domains for Embedded Checkout [11].

---

## Related Projects (in workspace)

- **comicwise** — shared Stripe + NextAuth + Tailwind reader flow
- **rhixecompany-comics** — shared comic reader and payment concerns
- **university-library-jsm** — Prisma + PostgreSQL catalog patterns
- **banking** — NextAuth v5 + Prisma auth + payment patterns

---

## Resources

| Resource | URL | Description |
|----------|-----|-------------|
| Next.js docs | https://nextjs.org/docs | Framework docs |
| Prisma docs | https://www.prisma.io/docs | ORM docs |
| NextAuth v5 docs | https://authjs.dev | Auth guide |
| UploadThing docs | https://docs.uploadthing.com | Upload docs |
| Stripe docs | https://stripe.com/docs | Payments |
| PayPal docs | https://developer.paypal.com | Payments |
| Zustand docs | https://zustand.docs.pmnd.rs | State mgmt |
| TanStack Query docs | https://tanstack.com/query | Data fetching |
| React 19 docs | https://react.dev | Framework |
| Prisma 7 announcement | https://tech-insider.org/prisma-orm-tutorial-typescript-postgres-13-steps-2026 | 3x faster, 90% smaller |

---

## References

[1] Stack Overflow: "Error at migration: Prisma 6.0.1 to NextJs 15: can-connect-to-database" — https://stackoverflow.com/questions/79266546/error-at-migration-prisma-6-0-1-to-nextjs-15-can-connect-to-database  
[2] DEV Community: "Build a Next.js App with Prisma Postgres" — https://dev.to/aidankmcalister/build-a-nextjs-app-with-prisma-postgres-53g7  
[3] Tech Insider: "Prisma ORM Tutorial: Type-Safe API in 13 Steps [2026]" — https://tech-insider.org/prisma-orm-tutorial-typescript-postgres-13-steps-2026  
[4] Prisma Docs: "How to use Prisma ORM and Prisma Postgres with Next.js and Vercel" — https://www.prisma.io/docs/guides/frameworks/nextjs  
[5] GitHub Discussion: "Discuss NextAuth.js v5" — https://github.com/nextauthjs/next-auth/discussions/8487  
[6] Stack Overflow: "NextAuth.js (v5) - Is there a way to obtain the jwt at every callback call?" — https://stackoverflow.com/questions/78041071/nextauth-js-v5-is-there-a-way-to-obtain-the-jwt-at-every-callback-call  
[7] NextAuth.js Options Reference — https://next-auth.js.org/configuration/options  
[8] APIScout: "Uploadthing vs Cloudflare R2 vs S3 for Next.js 2026" — https://apiscout.dev/guides/uploadthing-vs-cloudflare-r2-vs-s3-nextjs-2026  
[9] Puter Blog: "Top 5 UploadThing Alternatives (2026)" — https://developer.puter.com/blog/uploadthing-alternatives  
[10] Koda School: "Next.js file uploads made easy with uploadthing" — https://kodaschool.com/blog/next-js-file-uploads-made-easy-with-uploadthing-an-alternate-to-s3-bucket  
[11] DEV Community: "The Ultimate Guide to Stripe + Next.js (2026 Edition)" — https://dev.to/sameer_saleem/the-ultimate-guide-to-stripe-nextjs-2026-edition-2f33  
[12] Digital Applied: "Stripe Payment Integration: Complete Dev Guide 2026" — https://www.digitalapplied.com/blog/stripe-payment-integration-developer-guide-2026  
[13] TheFrontKit: "Add Stripe Payments to a Next.js Template (2026)" — https://thefrontkit.com/blogs/add-stripe-payments-to-nextjs-template-2026  
[14] NextFuture: "React State Management 2026: Zustand vs Redux vs Jotai" — https://nextfuture.io.vn/blog/ultimate-guide-react-state-management-2026  
[15] LinkedIn Pulse: "Modern State Management in React: Comparing Zustand, Redux, and TanStack Query" — https://www.linkedin.com/pulse/modern-state-management-react-comparing-zustand-redux-saber-v7a3c