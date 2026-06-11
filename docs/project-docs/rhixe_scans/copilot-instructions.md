# Copilot Instructions — rhixe_scans

## TypeScript/React
- Strict TypeScript mode
- PascalCase for components, camelCase for utilities
- shadcn/ui component conventions
- React Hook Form + Zod for forms

## Database
- Prisma schema-driven development
- Always generate migrations for schema changes
- Use Prisma adapter for NextAuth

## Security
- Never commit .env files
- Use NextAuth v5 for authentication
- Validate all inputs with Zod
- Stripe/PayPal keys kept server-side only
