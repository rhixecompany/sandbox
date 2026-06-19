# University Library JSM
## Architecture

- **Blueprint**: [university-libary-jsm Architecture](../docs/Project_Architecture/university_libary_jsm_architecture.md)
- **Folders**: [university-libary-jsm Folder Structure](../docs/Project_Architecture/university_libary_jsm_folders.md)
- **Tech Stack**: [university-libary-jsm Technology Stack](../docs/Project_Architecture/university_libary_jsm_techstack.md)
- **Stack Type**: Next.js


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
