# Copilot Instructions

Project-wide guidance for Rhixescans.

## Source of truth

- `projects/rhixe_scans/AGENTS.md`
- `README.md`
- `src/`
- `tests/`
- `docs/`

## Commands

Run from the project root:

```bash
npm install
npx prisma migrate dev
npm run db:seed
npm run dev
npm run lint
npx prettier --write .
npm test
npm run test:watch
npx prisma studio
npm run build
```

## Architecture

- Next.js 15 App Router frontend with Prisma-backed PostgreSQL data access.
- Auth uses NextAuth v5 with a Prisma adapter.
- Payments, uploads, email, and realtime features are separate integration areas.

## Conventions

- Keep TypeScript strict and component code shadcn/ui-compatible.
- Prefer Prisma schema changes plus migrations for data model work.
- Keep route, component, and utility naming aligned with the repo structure.
- Use environment variables for all secrets and provider credentials.

