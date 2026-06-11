# Copilot Instructions — comicwise

## Naming Conventions
- Components: PascalCase (`ComicCard.tsx`)
- Utilities: camelCase (`formatDate.ts`)
- Server Actions: dot.camelCase (`comic.create.ts`)
- Database tables: snake_case
- Pages: kebab-case for route segments

## Code Patterns
- Use `cn()` from `@/lib/utils` for conditional classes
- Server Components by default, Client Components only when needed
- React Hook Form + Zod for all forms
- TanStack Query for client data fetching
- Zustand for global client state

## Imports Order
1. React/Next.js
2. Third-party libraries
3. Local components (`@/components/`)
4. Lib/utils (`@/lib/`)
5. Types (`@/types/`)

## Security
- Validate all inputs with Zod
- Use NextAuth for authentication
- Rate-limit API routes with Upstash
- Never commit .env files

## Dev Commands
- `npm run dev` - Start dev server
- `npm run format` - Format code
- `npm run lint` - Lint check
- `npx tsc --noEmit` - Type check
