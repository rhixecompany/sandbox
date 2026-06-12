# Comicwise - Comic Streaming Platform Context

Next.js 15 comic streaming frontend with Prisma and Stripe.

## Architecture
- **Framework**: Next.js 15 (App Router)
- **Language**: TypeScript
- **Database**: Prisma + PostgreSQL
- **Payments**: Stripe
- **Auth**: NextAuth.js
- **Deployment**: Vercel

## Conventions
- Use TypeScript strict mode
- Server Components by default
- API routes in `src/app/api/`
- Prisma schema in `prisma/schema.prisma`
- Stripe webhooks for subscriptions
- Package manager: `pnpm`; lockfile: `pnpm-lock.yaml`; runtime: Node 18+

## Commands
```bash
# Dev server
npm run dev

# Build
npm run build

# Database
npx prisma generate
npx prisma db push
npx prisma studio

# Lint
npm run lint
```

## Important Notes
- Stripe keys in `.env.local` — never commit
- Stripe webhook secret required for subscriptions
- Image optimization via Next.js Image component