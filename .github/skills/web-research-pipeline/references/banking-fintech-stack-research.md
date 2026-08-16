# Banking Fintech Stack Research (Next.js 16 + Drizzle + Plaid + Dwolla + Auth.js + Upstash + Bun)

## Project Context
Full-stack fintech application with banking dashboard, transaction management, authentication, and webhook handling. Deployed via Docker + Vercel.

## Stack Coverage
| Technology | Version | Research Focus |
|------------|---------|----------------|
| Next.js | 16.2.4 | Turbopack, Cache Components, Server Actions, RSC, App Router |
| TypeScript | 6.0.3 | Strict mode, noUncheckedIndexedAccess, exactOptionalPropertyTypes |
| React | 19 | Server Components, Suspense, streaming |
| Drizzle ORM | 0.45.x | Type-safe schema, relations, migrations, Zod validation |
| PostgreSQL | — | Neon serverless, connection pooling, indexes |
| Auth.js (NextAuth) | v5 | Split config, Drizzle adapter, Edge middleware, Server Actions |
| Plaid | 42.x | Link tokens, processor tokens, Secure Token Exchange, webhooks |
| Dwolla | v2 | Exchange Sessions API, funding sources, ACH transfers |
| Upstash Redis | — | Edge rate limiting, session storage, API caching |
| Zustand | 5.x | Client state management |
| TanStack Table | — | Server-side pagination/sorting |
| Recharts | — | Data visualization |
| Bun | — | Package manager + runtime, 7x faster installs |
| Vitest + Playwright | — | Unit + E2E testing |

## Query Strategy Used (10 searches)
1. Full stack integration query
2. Plaid + Dwolla Next.js integration
3. Drizzle ORM + Next.js 16 + TS strict
4. Plaid + Dwolla + NextAuth security
5. Drizzle + PostgreSQL security fintech
6. Next.js 16 performance (Turbopack, Cache Components)
7. Upstash Redis caching/rate-limiting/sessions
8. NextAuth v4→v5 migration (App Router)
9. Fintech PCI DSS + Plaid/Dwolla compliance
10. Bun + Next.js 16 setup

## Extraction Pattern
- **Phase 1**: Tavily search (10 queries, broad → specific)
- **Phase 2**: Tavily extract (6 priority URLs for deep content)
- **Phase 3**: Synthesize into structured JSON report with topics → bullets → sources

## Key Findings Structure (8 topics)
1. Plaid + Dwolla Integration (Secure Token Exchange flow)
2. Drizzle ORM + TypeScript Strict (schema patterns, relations)
3. Auth.js v5 Migration (split config, Drizzle adapter, Edge)
4. Upstash Redis (caching, rate limiting, sessions, cold starts)
5. Next.js 16 Performance (Turbopack, PPR, RSC, Server Actions)
6. Fintech Security (PCI DSS, tokenization, audit logging, rate limiting)
7. Project Architecture (App Router structure, lib/schema separation)
8. Common Pitfalls (token expiry, cold starts, Edge limits, TS strict, Turbopack compat)

## Output
- `RESEARCH_REPORT.md` (this project's format) - structured JSON with findings
- Each topic: bullets (5-12) + sources (2-4 authoritative URLs)

## Fintech-Specific Patterns
- **Never store raw credentials** - Plaid access tokens encrypted at rest (AES-256)
- **Processor tokens only** - Dwolla STX pattern, no account/routing numbers in app
- **Rate limit at Edge** - @upstash/ratelimit in middleware before request hits app
- **Audit log everything** - Immutable logs for all financial transactions
- **Webhook idempotency** - Plaid/Dwolla webhooks with deduplication keys
- **PCI DSS scope reduction** - Tokenization, no cardholder data in app DB