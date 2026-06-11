# Copilot Instructions — university-libary-jsm

## TypeScript/React
- Strict TypeScript mode
- PascalCase for components, camelCase for utilities
- Server Actions use dot notation (e.g., `book.create.ts`)
- shadcn/ui conventions for components
- React Hook Form + Zod 4 for all forms

## Database
- Drizzle ORM with Zod schema validation
- Edit schema in `database/schema.ts`
- Use `db:push` or `db:generate` + `db:migrate` for changes
- Parameterized queries prevent SQL injection

## Security
- Never commit .env files
- Use NextAuth v5 `auth()` for protected routes
- Validate all server action inputs with Zod
- Rate limiting via Upstash Ratelimit
- File uploads via ImageKit signed URLs
