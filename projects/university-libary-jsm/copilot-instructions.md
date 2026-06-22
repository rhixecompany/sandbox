# university-libary-jsm
**React/TS**: strict TS, PascalCase components, `cn()` utility, shadcn/ui.
**Forms**: React Hook Form + Zod 4.
**Server Actions**: dot notation (e.g., `book.create.ts`).
**DB**: Drizzle schema in `database/schema.ts`; `db:push` or `db:generate` + `db:migrate`; parameterized queries.
**Security**: no `.env` commit; NextAuth v5 `auth()` for protected routes; validate inputs with Zod; Upstash Ratelimit; ImageKit signed uploads.
