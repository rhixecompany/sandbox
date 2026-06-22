# RESEARCH_REPORT.md

## Project: Banking

**Type:** Fintech (Next.js 16 + banking integrations)
**Tech Stack:** Next.js 16, TypeScript, PostgreSQL, Drizzle ORM, NextAuth v4, Plaid, Dwolla, shadcn/ui, Tailwind CSS, Bun
**Status:** Active

## Similar Projects

| Project | URL | Why Relevant |
|---------|-----|--------------|
| comicwise | `projects/comicwise` | Same Next.js + shadcn/ui + payment patterns |
| rhixe_scans | `projects/rhixe_scans` | Shared Next.js + auth + media-payment concerns |
| rhixecompany-comics | `projects/rhixecompany-comics` | Shared PostgreSQL + Drizzle + Next.js conventions |
| university-libary-jsm | `projects/university-libary-jsm` | Next.js 16 + Drizzle + PostgreSQL + auth patterns |

## Key Findings

### Next.js 16 + Fintech (2026)
- Server Components default; 400% faster dev via Turbopack
- Server Actions stable for mutations
- Edge Middleware for auth

### Drizzle ORM (2026)
- Code-first, no codegen; TypeScript schema as source of truth
- Schema by bounded context; unique indexes on financial keys

### Plaid: Sandbox vs Production
- OAuth redirect URIs must be in Production Dashboard
- Sandbox data is idealized; real institutions vary

### Dwolla: Idempotency
- Generate idempotency key per transfer intent
- Correlation IDs for multi-leg tracing

## Cheatsheets & Quick Reference

| Topic | Resource |
|-------|----------|
| Next.js 16 | https://nextjs.org/docs/app |
| Drizzle ORM | https://orm.drizzle.dev |
| Plaid Docs | https://plaid.com/docs |
| Dwolla API | https://developers.dwolla.com/docs |
| NextAuth v4 | https://next-auth.js.org/getting-started/upgrade-v4 |

## Best Practices

1. Server Components by default; `'use client'` only for interactivity
2. Idempotency-first transfers with key-per-intent
3. Schema by bounded context (`accounts/`, `transfers/`, `audit/`)
4. Validate all external payloads with Zod before DB writes
5. Sandbox and Production credentials never shared

## Common Pitfalls

| Pitfall | Avoidance |
|---------|-----------|
| Assuming Sandbox = Production | Test OAuth flows in Production Trial |
| Missing idempotency keys | `transfer_attempts` table with unique constraint |
| Provider secrets in client code | Keys server-side only |
| Missing OAuth redirect URIs | Register all in Production Dashboard |

## Performance

1. Server Components for dashboard; cache with `revalidate`
2. Drizzle `.with()` to avoid N+1 queries
3. Background jobs for Plaid/Dwolla webhook processing
4. Edge Middleware for low-latency auth

## Security

1. Validate all external payloads with Zod
2. Verify webhook signatures (Plaid `Plaid-Verification` header)
3. Append-only audit logging for financial events
4. Rate-limit sensitive endpoints via middleware
5. Rotate Plaid credentials quarterly

## Related Projects (in workspace)

- **comicwise** — Shared Next.js + auth + payment flows
- **rhixe_scans** — Shared Next.js + auth patterns
- **rhixecompany-comics** — PostgreSQL + Drizzle conventions
- **university-libary-jsm** — Next.js 16 + Drizzle reference

## Resources

| Resource | URL |
|----------|-----|
| Next.js Docs | https://nextjs.org/docs |
| Drizzle ORM | https://orm.drizzle.dev |
| Plaid Docs | https://plaid.com/docs |
| Dwolla API | https://developers.dwolla.com/docs |
| NextAuth v4 | https://next-auth.js.org |
| OWASP Finance | https://cheatsheetseries.owasp.org/cheatsheets/Financial_Applications_Cheat_Sheet.html |
