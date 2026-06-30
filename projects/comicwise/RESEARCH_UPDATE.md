# Project 2: comicwise (Next.js 16 + Drizzle/Prisma + Stripe)

## Similar Open-Source Projects

| Project | URL | Stack |
|---------|-----|-------|
| **nextjs/saas-starter** | https://github.com/nextjs/saas-starter | Next.js + Postgres + Drizzle + Stripe + shadcn/ui ⭐15.8k |
| **laribright/stripe-crashcourse** | https://github.com/laribright/stripe-crashcourse | Next.js + Drizzle + Stripe + PostgreSQL |
| **burakorkmez/stripe-subscriptions** | https://github.com/burakorkmez/stripe-subscriptions | Next.js 14 + Prisma + MongoDB + Stripe + Kinde Auth |
| **ixartz/SaaS-Boilerplate** | https://github.com/ixartz/SaaS-Boilerplate | Next.js + Stripe + Prisma + TailwindCSS |
| **next-saas-stripe-starter** | https://github.com/next-saas-stripe-starter | Next.js + Prisma + NextAuth + Stripe |
| **Makerkit Next.js 16 + Drizzle** | https://makerkit.dev/courses/nextjs-drizzle/course | Next.js 16 + React 19 + Drizzle + Stripe B2B SaaS |
| **Vercel Next.js + Stripe guide** | https://vercel.com/kb/guide/getting-started-with-nextjs-typescript-stripe | Official Stripe + Next.js TypeScript guide |
| **DEV Community: Next.js 16 Stripe guide** | https://dev.to/huangyongshan46a11y/how-to-set-up-stripe-subscriptions-in-nextjs-16-complete-guide-phd | Complete Checkout + Webhooks + Portal guide |

## Key Findings

### Next.js 16 + Stripe State-of-Art (2026)
- **Next.js 16 (Oct 2025):** Turbopack is the default bundler (2-5× faster builds), React 19 bundled, Cache Components with `"use cache"` replace PPR, `revalidateTag()` now requires `cacheLife` profile as second arg.
  - Source: https://nextjs.org/blog/next-16
- **Next.js 16.2 (March 2026):** Stable Build Adapters API for non-Vercel platforms (OpenNext, etc.) supporting `proxy.ts`. 13 security advisories patched (7 high-severity including DoS in Server Components, middleware bypass, SSRF).
  - Source: https://makerkit.dev/blog/tutorials/nextjs-16
- **Drizzle vs Prisma (2026):** Drizzle ~7.4 KB gzipped, zero runtime deps, SQL-first. Prisma 7.x: Rust-based query engine (~8 MB), schema-first. Drizzle chosen by MakerKit for its Drizzle kit; Prisma kit still maintained.
  - Source: https://makerkit.dev/blog/tutorials/drizzle-vs-prisma
  - Source: https://designrevision.com/blog/prisma-vs-drizzle

### Webhook Security (Critical)
- **Major anti-pattern:** AI-generated webhook code often parses body as JSON before signature verification — this breaks Stripe signature validation and leaves the endpoint spoofable.
- **Required pattern:** `req.text()` first → verify `stripe-signature` header → parse JSON.
- **Common omission:** Handlers for `payment_failed` and `subscription_deleted` are regularly missing in scaffolded code.
  - Source: https://dev.to/whoffagents/webhook-security-in-nextjs-signatures-idempotency-and-avoiding-common-mistakes-4g6

### Stripe Subscription Billing Patterns
- Full lifecycle: Checkout → `checkout.session.completed` → `customer.subscription.updated` → `customer.subscription.deleted`.
- Customer Portal (billing management) is handled by Stripe-hosted UI. Build a redirect via `stripe.billingPortal.sessions.create()`.
  - Source: https://designrevision.com/blog/best-nextjs-subscription-templates
- Feature gating should track subscription status in your DB (source of truth for access control) — Stripe is source of truth for billing only.

## Cheatsheet

### Stripe Checkout API Route
```typescript
// app/api/stripe/checkout/route.ts
import { NextResponse } from "next/server";
import { stripe } from "@/lib/stripe";

export async function POST(req: Request) {
  const { priceId, userId } = await req.json();
  const session = await stripe.checkout.sessions.create({
    mode: "subscription",
    payment_method_types: ["card"],
    line_items: [{ price: priceId, quantity: 1 }],
    metadata: { userId },
    success_url: `${process.env.NEXT_PUBLIC_APP_URL}/success?session_id={CHECKOUT_SESSION_ID}`,
    cancel_url: `${process.env.NEXT_PUBLIC_APP_URL}/cancel`,
  });
  return NextResponse.json({ url: session.url });
}
```

### Stripe Webhook Route — Correct Pattern
```typescript
// app/api/stripe/webhook/route.ts
export const config = { api: { bodyParser: false } };

export async function POST(req: Request) {
  const body = await req.text();  // raw body required for signature
  const sig = req.headers.get("stripe-signature");
  if (!sig) return NextResponse.json({ error: "No signature" }, { status: 400 });

  let event: Stripe.Event;
  try {
    event = stripe.webhooks.constructEvent(body, sig, process.env.STRIPE_WEBHOOK_SECRET!);
  } catch {
    return NextResponse.json({ error: "Invalid signature" }, { status: 400 });
  }

  switch (event.type) {
    case "checkout.session.completed":
    case "customer.subscription.updated":
    case "invoice.payment_failed":
    case "customer.subscription.deleted":
      // Store stripeEventId for idempotency
      // Upsert subscription in DB using metadata.userId
      break;
    default:
      console.log(`Unhandled event: ${event.type}`);
  }
  return NextResponse.json({ received: true });
}
```

### Drizzle ORM Quick Reference
```typescript
// Setup
import { drizzle } from 'drizzle-orm/postgres-js';
import { eq, and } from 'drizzle-orm';

// Select with relations (v0.30+)
const users = await db.query.users.findMany({ with: { subscriptions: true } });

// Insert
await db.insert(subscriptions).values({ stripeId: 'sub_xxx', userId: '1', plan: 'pro' });

// Upsert
await db.insert(subscriptions).values({...}).onConflictDoUpdate({
  target: subscriptions.stripeId,
  set: { plan: 'pro', updatedAt: new Date() }
});

// Migrations: drizzle-kit generate → drizzle-kit migrate
```

### Next.js 16 Caching Cheatsheet
```typescript
import { revalidateTag } from 'next/cache';

// v16: cacheLife profile is now REQUIRED as second arg
revalidateTag('subscriptions', 'hours');  // or 'days', 'max'

// Cache Components (new PPR model)
async function ServerComponent() {
  'use cache';
  return <div>Cached shell</div>;
}

// In next.config.ts — enable Cache Components
export const cacheComponents = true;
```

## Best Practices

1. **Idempotent webhook handlers:** Store `stripeEventId` per event, skip if already processed. Stripe retries failed webhooks for up to 3+ days.
2. **Separate billing source of truth:** Stripe = billing truth; your DB = access/entitlement truth. Sync via webhooks.
3. **Use `drizzle-kit studio`** for schema exploration during development (`npx drizzle-kit studio`).
4. **Separate DATABASE_URL per environment** for dev/test/prod. Drizzle has no built-in env switching.
 - Source: https://stackoverflow.com/questions/77093723/how-to-have-both-production-and-test-databases-in-drizzle-orm
5. **Stripe CLI local testing:** `stripe listen --forward-to localhost:3000/api/stripe/webhook`
6. **Customer Portal redirect:** Use `stripe.billingPortal.sessions.create()` — don't build your own cancellation UI.
7. **NextAuth + Stripe sync:** On `checkout.session.completed`, link the Stripe customer to the NextAuth user in your DB.
8. **Upgrade path to Next.js 16:** Upgrade to v15 first, resolve deprecations (middleware, caching), then upgrade to v16.
 - Source: https://dev.to/abhilashlr/migrating-to-nextjs-16-react-19-a-platform-upgrade-that-paid-off-4j6f
9. **Schema splitting in Drizzle:** Use glob patterns in `drizzle.config.ts` to split schemas across multiple files.
 - Source: https://www.thisdot.co/blog/configure-your-project-with-drizzle-for-local-and-deployed-databases
10. **Vercel env setup:** Generate `AUTH_SECRET` via `openssl rand -base64 32`. Set `STRIPE_WEBHOOK_SECRET` from dashboard (not CLI).

## Common Pitfalls

1. **AI webhook anti-patterns:** JSON parsing before signature verification; missing `payment_failed` + `subscription_deleted` handlers.
 - Source: https://www.reddit.com/r/nextjs/comments/1sz1edp/nextjs_stripe_webhooks_the_default_pattern_ai
2. **Vercel webhook timeouts:** Next.js Serverless Functions have a 10s timeout on Hobby/Pro. Move heavy processing to queues.
 - Source: https://github.com/vercel/next.js/discussions/48885
3. **Wrong STRIPE_WEBHOOK_SECRET in prod:** CLI secret (`whsec_...`) differs from production dashboard secret. Hardcoded secrets in env files are a common deployment failure.
4. **Next.js 16 breaking: `cacheLife` required in `revalidateTag()`:** Omitting this throws an error. Old code from v15 will break.
5. **Drizzle edge runtime MySQL issue:** MySQL driver's `stream` module crashes Next.js Edge Middleware. Use `postgres-js` adapter or externalize queries to Server Actions.
 - Source: https://github.com/drizzle-team/drizzle-orm/issues/4142

## Performance Tips

1. **Drizzle bundle advantage:** ~7 KB gzipped vs Prisma's ~8 MB query engine binary. Significant cold-start improvement in serverless.
 - Source: https://listiak.dev/blog/drizzle-orm-the-typescript-orm-that-thinks-in-sql
2. **Server Components first:** Keep subscription display pages as Server Components. Only wrap interactive buttons/forms with `'use client'`.
3. **Suspense + Streaming:** Wrap slow subscription data fetches in `<Suspense>` for progressive rendering.
4. **Turbopack:** Default in Next.js 16 — 2-5× faster production builds, 5× faster Fast Refresh.
5. **Caching:** Use `updateTag()` to invalidate subscription caches immediately on webhook events.
6. **Image optimization:** Use `next/image` for comic covers/thumbnails with explicit `sizes` attribute.

## Security Considerations

1. **STRIPE_SECRET_KEY must be server-only.** Only `NEXT_PUBLIC_STRIPE_PUBLISHABLE_KEY` can be exposed to the browser.
2. **Webhook signature verification is non-negotiable.** Faking a Stripe webhook can trigger free product delivery.
   - Source: https://dev.to/whoffagents/webhook-security-in-nextjs-signatures-idempotency-and-avoiding-common-mistakes-4g6
3. **Content Security Policy (CSP):** Configure headers in `next.config.ts`. Stripe SDK requires specific `script-src` and `frame-src` rules.
   - Source: https://www.authgear.com/post/nextjs-security-best-practices
4. **Zod input validation:** Validate all API route inputs (price IDs, user IDs, checkout metadata).
   - Source: https://www.turbostarter.dev/blog/complete-nextjs-security-guide-2025
5. **Rate limiting on checkout API:** Prevent abuse from session-spamming. Use `@upstash/ratelimit` or Vercel Edge Middleware.
6. **Next.js 16 security patches:** Upgrade to ≥16.2.6 to fix DoS (Server Components), middleware bypass, SSRF (WebSocket upgrades), XSS, RSC cache poisoning.
   - Source: https://makerkit.dev/blog/tutorials/nextjs-16
7. **PCI DSS:** Stripe Checkout reduces scope to SAQ A. Don't store raw card data ever.
