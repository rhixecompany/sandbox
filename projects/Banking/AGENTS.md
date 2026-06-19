# Banking — Fintech App
## Architecture

- **Blueprint**: [Banking Architecture](../docs/Project_Architecture/Banking_architecture.md)
- **Folders**: [Banking Folder Structure](../docs/Project_Architecture/Banking_folders.md)
- **Tech Stack**: [Banking Technology Stack](../docs/Project_Architecture/Banking_techstack.md)
- **Stack Type**: Next.js


Next.js 16 + Drizzle + Plaid/Dwolla.

## Stack
- TypeScript strict, App Router
- PostgreSQL via Drizzle
- NextAuth.js; Docker + Vercel deploy

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
- `bun`, lockfile `bun.lock`, Node 18+
- Schema in `src/db/schema.ts`
- `.env.local` — never commit
- Plaid sandbox for development
- Webhooks for Plaid/Dwolla events
