# University Library JSM — Library Management

**Naming**: `PascalCase` for React components; `camelCase` for utils/hooks; `dot.camelCase` for Server Actions; `kebab-case` for route segments and files; `snake_case` for database tables.

**Patterns**: Next.js Server Actions with `"use server"` for data mutations; Drizzle ORM for PostgreSQL with Neon serverless; Zod validation at all entry points; NextAuth.js for authentication; Redis for session caching and rate limiting; `cn()` for className merging.

**Structure**: `src/app/` (App Router route groups); `src/components/` (React components); `src/actions/` (Server Actions); `src/lib/` (utilities — db, auth, redis); `src/db/schema.ts` (Drizzle schema); `src/types/` (TypeScript types).

**TypeScript**: Strict mode; Next.js 15 App Router; Drizzle ORM with Neon PostgreSQL; TypeScript strict enabled; ES Modules; `npm` for package management.

**Database**: PostgreSQL via Drizzle ORM + Neon (serverless); schema in `src/db/schema.ts`; generate migrations with `npm run db:generate`; push with `npm run db:push` (note: migrations via `db:push`); Drizzle Studio for browsing.

**Auth/Caching**: NextAuth.js for authentication; Redis for session caching and rate limiting; serverless-friendly architecture.

**Security**: No `.env.local` in VCS; Zod validation at all boundaries; Redis rate limiting for API routes; Neon connection pooling; parameterized queries via Drizzle prevent SQL injection; HTTPS required.

**Env**: `DATABASE_URL` (Neon serverless), `NEXTAUTH_SECRET`, `NEXTAUTH_URL`, `REDIS_URL`, `REDIS_TOKEN`.

**Commands**: `npm run dev` (development); `npm run build` (production build); `npm run lint` (ESLint); `npm run db:generate` (schema generation); `npm run db:push` (apply migrations); `npm run db:studio` (DB browser).
