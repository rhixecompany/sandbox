# Banking
**Naming**: `dot.camelCase` Server Actions; PascalCase components; `camelCase` utils/hooks; `dot.camelCase` DAL; `snake_case` tables.
**Patterns**: Next.js Server Actions with `"use server"`; Zod at entry; constructor-based DAL classes; `{ ok, error? }` returns; `cn()`; soft-delete never hard-delete.
**Structure**: `src/components/`, `src/app/` route groups, `src/actions/`, `src/dal/`, `src/database/schema.ts`, `src/types/`.
**Env**: `DATABASE_URL`, `NEXTAUTH_SECRET`, `NEXTAUTH_URL`, Plaid + Dwolla credentials.
**Pre-commit**: `bun run format && bun run type-check && bun run lint:strict`.
**Security**: no secrets; encrypt sensitive data; Zod validation; soft-delete; idempotent financial transactions.
