# rhixe_scans — Comic Reader

**Naming**: `PascalCase` for React components; `camelCase` for hooks and utilities; `kebab-case` for page segments and files; `snake_case` for database tables; `UPPER_SNAKE_CASE` for environment variables.

**Patterns**: Server Components by default; client components only when interactivity needed; `cn()` + `class-variance-authority` (CVA) for component styling; React Hook Form + Zod schema validation; TanStack Query for server state; Zustand for client/global state; Prisma schema-first for database; NextAuth v5 for authentication; `@dnd-kit` for drag-and-drop; `recharts` for charts.

**Structure**: `src/app/` (App Router route groups + pages); `src/components/` (UI components with shadcn/ui); `src/lib/` (utilities, API helpers); `src/hooks/` (custom hooks); `prisma/` (schema + migrations); `public/` (static assets).

**TypeScript**: Strict mode; React 19; Next.js 15 App Router; TypeScript strict enabled; Tailwind CSS 3 + Radix UI primitives (`shadcn/ui`); TanStack Query for server state; Zustand for client state.

**Database**: PostgreSQL via Prisma 6 ORM; schema-first approach; always use `npx prisma migrate dev` for migrations (never `db:push` except prototyping); Prisma Studio for browsing; NextAuth v5 adapter.

**Payments**: Stripe for subscriptions; PayPal as secondary payment provider; server-side keys only; webhook handling for payment lifecycle events.

**File Uploads**: UploadThing for user file uploads; Resend for transactional emails; WebSocket for real-time features.

**Security**: No `.env` commit; Zod validation at all API boundaries; Stripe/PayPal keys server-side only; Prisma parameterization prevents SQL injection; rate limiting; HTTPS required.

**Env**: `DATABASE_URL`, `NEXTAUTH_SECRET`, `NEXTAUTH_URL`, Stripe keys, PayPal keys, UploadThing keys, Resend API key.

**Commands**: `npm install && cp .env.example .env` (setup); `npx prisma migrate dev && npm run db:seed` (DB); `npm run dev` (dev); `npm run lint && npx prettier --write .` (format); `npm run build && npm start` (production); `npm test` (test); `npm run clean` (reset).
