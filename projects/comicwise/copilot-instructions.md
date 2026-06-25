# Comicwise — Comic Streaming

**Naming**: `PascalCase` for components; `camelCase` for utilities/hooks; `dot.camelCase` for Server Actions; `kebab-case` for route segments; `snake_case` for database tables; `kebab-case` for files.

**Patterns**: Server Components by default; client components only when interactivity required; `cn()` for className merging; React Hook Form + Zod for form validation; TanStack Query for server state; Zustand for client state; Stripe webhooks for subscription management; Next.js Image optimization for assets.

**Structure**: `src/app/` (App Router with route groups); `src/app/api/` (API routes); `src/components/` (React components); `src/lib/` (utilities); `src/types/` (TypeScript types).

**TypeScript**: Strict mode; Next.js 15 App Router; `pnpm` for package management (`pnpm-lock.yaml`); Node.js 18+.

**Database**: PostgreSQL via Prisma ORM; schema-first approach; generate with `npx prisma generate`; push schema with `npx prisma db push`; Prisma Studio for browsing; NextAuth.js v5 adapter for auth.

**Auth/Payments**: NextAuth.js for authentication; Stripe for subscription payments; Stripe webhooks for lifecycle events; server-side Stripe keys only.

**Imports**: React/Next.js → third-party → `@/components/` → `@/lib/` → `@/types/`.

**Security**: Zod validation at boundaries; NextAuth for session security; Upstash rate limiting; no `.env` commit; Stripe keys server-side only; HTTPS required.

**Env**: `DATABASE_URL`, `NEXTAUTH_SECRET`, `NEXTAUTH_URL`, Stripe keys, `UPSTASH_REDIS_REST_URL`, `UPSTASH_REDIS_REST_TOKEN`.

**Commands**: `npm run dev` (development); `npm run build` (production build); `npm run lint` (ESLint); `npx prisma generate` (schema client); `npx prisma db push` (migrate); `npx prisma studio` (DB browser); `npm run format` (Prettier).
