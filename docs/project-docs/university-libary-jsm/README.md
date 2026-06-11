# university-libary-jsm — Library Management System (BookWise)

A full-stack Next.js application for managing library book requests, user accounts, and administrative workflows.

## Tech Stack
- **Frontend**: Next.js 15 (Turbopack), React 19, TypeScript, Tailwind CSS 4, shadcn/ui
- **Database**: Neon PostgreSQL with Drizzle ORM
- **Auth**: NextAuth v5
- **Cache/Jobs**: Upstash Redis + Workflow + QStash
- **Media**: ImageKit

## Quick Start
```bash
npm install
cp .env.example .env
npm run db:push
npm run db:seed
npm run dev
```

## Documentation
- [Technology Stack](technology-stack.md)
- [Architecture](architecture.md)
- [Code Exemplars](code-exemplars.md)
