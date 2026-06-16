# University Library JSM

Next.js 15 + Drizzle + Neon + Redis.

## Stack
- TypeScript strict, App Router
- PostgreSQL via Drizzle/Neon
- NextAuth.js; Vercel + Neon

## Commands
```bash
npm run dev
npm run build
npm run lint
npm run db:generate
npm run db:push
npm run db:studio
```

## Notes
- Redis for session caching/rate limiting
- `.env.local` — never commit
- Migrations via `db:push`
