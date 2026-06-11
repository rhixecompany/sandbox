# comicwise — Comic Streaming Frontend

A Next.js-based comic streaming frontend built with TypeScript, Tailwind CSS, shadcn/ui, and Prisma ORM.

## Tech Stack
- **Frontend**: Next.js 16.1, React 19, TypeScript 5, Tailwind CSS 4
- **Database**: PostgreSQL with Drizzle ORM
- **Auth**: NextAuth v5
- **Payments**: Stripe / PayPal
- **Storage**: ImageKit / Cloudinary

## Quick Start

```bash
npm install
cp .env.example .env
npx prisma migrate dev
npm run db:seed
npm run dev
```

## Key Commands
| Command | Purpose |
|---------|---------|
| `npm run dev` | Start dev server (Turbopack) |
| `npm run build` | Production build |
| `npm run lint` | ESLint |
| `npm test` | Run tests |

## Documentation Links
- [Technology Stack](technology-stack.md)
- [Architecture](architecture.md)
- [Project Workflow](project-workflow.md)
- [Folder Structure](folder-structure.md)
- [Code Exemplars](code-exemplars.md)
- [Copilot Instructions](copilot-instructions.md)
