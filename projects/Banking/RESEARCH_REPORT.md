# Banking — Research Report

## Project

| Field | Value |
|-------|-------|
| **Type** | Fintech Banking Application |
| **Tech Stack** | Next.js 16.2 (App Router), Drizzle ORM 0.45, PostgreSQL, NextAuth v4, Plaid 42, Dwolla v2, shadcn/ui, Tailwind CSS 4, TS 6.0, Bun, Zod 4, Zustand 5, Server Actions |
| **Status** | Active development (v0.1.0) |

## Similar Projects

| Project | Stack |
|---------|-------|
| **Horizon** (JS Mastery) | Next.js 14, Drizzle, Tailwind |
| **Mint** (clones) | Next.js, Plaid, PostgreSQL |
| **Actual Budget** | Node.js, SQLite, React |
| **Firefly III** | Laravel, PHP |

## Key Findings

1. **Server Actions + Zod** — All mutations use `"use server"` with `z.safeParse()` at the boundary, returning `{ ok, error, data }`.
2. **Plaid ↔ Dwolla 4-step flow** — Link Token → exchange public_token → Dwolla Customer → funding source with Plaid processor token. Uses `dwolla-v2` + `react-plaid-link`.
3. **DAL pattern** — Constructor-based classes (`class XDAL {}`) with singleton exports keep Drizzle queries separate from actions.
4. **Drizzle ORM 0.45** — `snake_case` tables, prepared statements, `drizzle-kit` for migrations/push/studio.

## Cheatsheets

| Command | Purpose |
|---------|---------|
| `bun run dev` | Start dev server |
| `bun run db:push` | Push schema (force) |
| `bun run db:generate` | Generate migrations |
| `bun run db:studio` | Drizzle Studio GUI |
| `bun run db:seed` | Seed with Plaid sandbox |
| `bun run type-check` | TS strict check |
| `drizzle-kit studio` | Ad-hoc DB inspection |

## Best Practices

1. **Server-first** — Default to RSC; `"use client"` only for interactivity. All mutations via Server Actions.
2. **Validate at every boundary** — Every action uses `z.safeParse()`. Never trust raw input.
3. **Encrypt PII at rest** — Plaid access tokens encrypted via `lib/utils` helpers before DB storage.
4. **Idempotent transfers** — Dwolla ACH transfers require unique idempotency keys per request.
5. **Soft-delete** — Never hard-delete; use `deleted_at` columns (already on `users` table).

## Common Pitfalls

| Pitfall | Mitigation |
|---------|-----------|
| Client-exposed Plaid tokens | Always exchange/store tokens server-side |
| Missing Dwolla idempotency | Pass unique key on every transfer |
| RSC + Zustand mixing | Keep Zustand in client; Server Actions for server state |
| Raw SQL injection | Always use Drizzle parameterized queries |
| Unhandled Plaid webhooks | Handle `SYNC_UPDATES_AVAILABLE`, `ITEM_LOGIN_REPAIRED` |

## Performance

1. **Drizzle prepared statements** auto-optimize repeated queries.
2. **Upstash Redis** for rate limiting + session cache (edge-optimized).
3. **Next.js Image + Font** via `sharp` + next/font reduces CLS.
4. **Tree-shakeable UI** — Radix/shadcn are fully tree-shakeable.
5. **Drizzle Studio** — Built-in GUI, no external tools needed.

## Security

1. **Server-side token handling** — Plaid/Dwolla tokens never leave server; encrypted in PostgreSQL.
2. **Upstash rate limiting** on auth endpoints and transfers.
3. **Zod validation + Server Action CSRF** protection built-in.
4. **zxcvbn-ts** password strength estimation (client + server).
5. **dotenv-safe** secrets management; no secrets in code.

## Related Projects

| Project | Relationship |
|---------|-------------|
| `projects/Banking/` | This project |

## Resources

| Resource | URL |
|----------|-----|
| Plaid API | https://plaid.com/docs |
| Dwolla ACH | https://docs.dwolla.com |
| Drizzle ORM | https://orm.drizzle.team |
| Next.js 16 | https://nextjs.org/docs |
| shadcn/ui | https://ui.shadcn.com |
| NextAuth v4 | https://next-auth.js.org |
| Zod | https://zod.dev |
