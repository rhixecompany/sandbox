# Copilot Instructions — Banking

## Naming Conventions
- Server Actions: `dot.camelCase` (e.g., `auth.signin.ts`)
- Components: PascalCase (e.g., `BankInfo.tsx`)
- Utils/Hooks: camelCase (e.g., `formUrlQuery.ts`)
- Database Tables: snake_case (e.g., `user_profiles`)
- DAL Files: `dot.camelCase` (e.g., `user.dal.ts`)

## Code Patterns to Follow
1. All mutations use Next.js Server Actions with "use server"
2. Validate all inputs with Zod at entry points
3. Use constructor-based DAL classes for queries
4. Return `{ ok: boolean, error?: string }` from actions
5. Use shadcn/ui components from `@/components/ui/`
6. Use `cn()` from `@/lib/utils` for class merging
7. Soft-delete user data; never hard-delete

## File Organization
- Components go in `src/components/`
- Pages go in `src/app/` route groups
- Server Actions go in `src/actions/`
- DAL goes in `src/dal/`
- DB schema goes in `src/database/schema.ts`
- Types go in `src/types/`

## Environment Variables Required
- DATABASE_URL, NEXTAUTH_SECRET, NEXTAUTH_URL
- PLAID_CLIENT_ID, PLAID_SECRET, PLAID_ENV
- DWOLLA_KEY, DWOLLA_SECRET, DWOLLA_ENV

## Before Committing
Run: `bun run format && bun run type-check && bun run lint:strict`

## Security Rules
- Never commit secrets
- Encrypt sensitive data
- Validate all inputs with Zod
- Use soft-delete for user data
- Implement idempotency for financial transactions
