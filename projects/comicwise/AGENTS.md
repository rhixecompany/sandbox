# Comicwise — Comic Streaming

## Architecture
- **Type:** Next.js comic streaming platform
- **Pattern:** App Router with Prisma ORM, Stripe subscriptions
- **Reference:** [Workflow Analysis](docs/Project_Architecture/Workflow_Analysis.md), [Exemplars](docs/Project_Architecture/exemplars.md)

Next.js 15 + Prisma + Stripe. Digital comic storefront with subscription management, user auth, and image-optimized content delivery.

## Stack
- **Frontend:** Next.js 15, TypeScript (strict), App Router
- **Database:** PostgreSQL via Prisma
- **Auth:** NextAuth.js
- **Payments:** Stripe (subscriptions)
- **Deploy:** Vercel
- **Package Manager:** pnpm (`pnpm-lock.yaml`)

## Commands
```bash
npm run dev
npm run build
npm run lint
npx prisma generate
npx prisma db push
npx prisma studio
```

## Conventions
- API routes in `src/app/api/`
- Use Next.js Image optimization for comic assets
- Stripe webhooks for subscription lifecycle events
- `.env.local` — never commit; Stripe keys required
- Node 18+ required

## Notes
- Uses `pnpm` as package manager
- Prisma for schema management and migrations
- Subscription model via Stripe recurring payments
