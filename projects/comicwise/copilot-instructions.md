# comicwise
**Naming**: PascalCase components; `camelCase` utilities; `dot.camelCase` Server Actions; `kebab-case` route segments; `snake_case` tables.
**Patterns**: `cn()` for classes; Server Components first; React Hook Form + Zod; TanStack Query; Zustand.
**Imports**: React/Next.js → third-party → `@/components/` → `@/lib/` → `@/types/`.
**Security**: Zod validation; NextAuth; Upstash rate limit; no `.env` commit.
**Commands**: `npm run dev`, `npm run format`, `npm run lint`, `npx tsc --noEmit`.
