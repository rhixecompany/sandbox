# Comicwise — Comic Streaming
## Architecture

- **Blueprint**: [comicwise Architecture](../docs/Project_Architecture/comicwise_architecture.md)
- **Folders**: [comicwise Folder Structure](../docs/Project_Architecture/comicwise_folders.md)
- **Tech Stack**: [comicwise Technology Stack](../docs/Project_Architecture/comicwise_techstack.md)
- **Stack Type**: Next.js


Next.js 15 + Prisma + Stripe.

## Stack
- TypeScript strict, App Router
- PostgreSQL via Prisma
- NextAuth.js, Vercel deploy

## Commands
```bash
npm run dev
npm run build
npm run lint
npx prisma generate
npx prisma db push
npx prisma studio
```

## Notes
- `pnpm`, lockfile `pnpm-lock.yaml`, Node 18+
- API routes in `src/app/api/`
- Stripe webhooks for subscriptions
- Use Next.js Image optimization
- `.env.local` — never commit; Stripe keys required
