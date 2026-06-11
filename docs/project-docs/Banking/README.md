# Banking — Next.js 16 Fintech Application

A fintech banking application built with Next.js 16, PostgreSQL, Drizzle ORM, and Plaid/Dwolla integrations.

## Tech Stack
- **Frontend**: Next.js 16, React 19, TypeScript 6, Tailwind CSS 4, shadcn/ui
- **Backend**: Next.js Server Actions, Drizzle ORM, PostgreSQL
- **Auth**: NextAuth.js v4 with credentials provider
- **Integrations**: Plaid (bank linking), Dwolla (ACH transfers), Upstash (rate limiting)
- **Testing**: Vitest, Playwright
- **Package Manager**: Bun 1.3.14

## Quick Start

```bash
bun install
cp .env.example .env.local
# Fill in environment variables
bun run db:push
bun run dev
```

## Commands

| Command | Purpose |
|---------|---------|
| `bun run dev` | Start development server |
| `bun run build` | Production build |
| `bun run db:studio` | Open Drizzle Studio |
| `bun run format` | Format code |
| `bun run lint:strict` | Strict linting |
| `bun run type-check` | TypeScript validation |

## Project Structure

```
src/
├── actions/     # Server Actions
├── app/         # Next.js App Router
├── components/  # React components
├── dal/         # Data Access Layer
├── database/    # Drizzle schema
├── lib/         # Utilities
├── stores/      # Zustand state
└── types/       # TypeScript types
```

## Documentation
- [Technology Stack](technology-stack.md)
- [Architecture](architecture.md)
- [Project Workflow](project-workflow.md)
- [Folder Structure](folder-structure.md)
- [Code Exemplars](code-exemplars.md)
- [Copilot Instructions](copilot-instructions.md)
