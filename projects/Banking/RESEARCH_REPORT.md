# RESEARCH_REPORT.md

## Project: Banking

**Type:** Fintech (Next.js 16 + banking integrations)
**Tech Stack:** Next.js 16 (App Router), TypeScript, PostgreSQL, Drizzle ORM, NextAuth v4, Plaid, Dwolla, shadcn/ui, Tailwind CSS, Playwright
**Status:** Active

---

## Similar Projects

| Project | URL | Why Relevant |
|---------|-----|--------------|
| comicwise | `projects/comicwise` | Same Next.js + shadcn/ui + payment-integration surface; crossover for schema validation, webhook flow, and RSC state patterns. |
| rhixe_scans | `projects/rhixe_scans` | Shared Next.js + Prisma + authentication + media-payment concerns. |

---

## Key Findings

### Next.js 16 + Fintech State
- App Router + Server Components reduce client JS for public pages; keep transaction-sensitive mutations in Server Actions with Zod validation.
- Use `output: "standalone"` plus edge runtime checks when multiple financial providers must reconcile token freshness.

### Plaid + Dwolla Flows
- Plaid Link is the highest-ROI frontend integration; keep it in a client component, but route tokens through Server Actions to avoid exposing secrets.
- Dwolla transfers require idempotency keys; store one per transaction intent in the database before calling the transfer API.

### Drizzle + PostgreSQL Patterns
- Drizzle schema modules compose better when split by bounded context (`accounts/`, `transfers/`, `audit/`).
- Add database-level unique constraints on `transfer_idempotency_key` and `plaid_item_id`.

### Security + Compliance
- Ledger tables should be append-only; never expose `UPDATE` to application code for financial records.
- NextAuth session callbacks should verify `user.active` and allowlist transfer statuses server-side; client checks are insufficient for fintech.

---

## Cheatsheets & Quick Reference

| Topic | Resource | Type |
|-------|----------|------|
| Next.js 16 App Router | https://nextjs.org/docs/app | Docs |
| Drizzle ORM | https://orm.drizzle.dev | Docs |
| Plaid Docs | https://plaid.com/docs | Docs |
| Dwolla API | https://docs.dwolla.com | Docs |
| shadcn/ui | https://ui.shadcn.com | Component system |

---

## Best Practices
1. **Server Actions for financial mutations** — route all balance-affecting writes through server-side validation and audit logging.
2. **Idempotency-first transfers** — generate one idempotency key per intent before calling Dwolla; retries are then safe.
3. **Schema ownership** — keep Drizzle migrations and schema definitions in versioned modules, not inline queries.
4. **Environment isolation** — Plaid sandbox, Dwolla sandbox, and local `.env.local` should never share credentials.
5. **Test transactions first** — run Plaid `auth` and Dwolla `customers` test flows before live production traffic.

---

## Common Pitfalls

| Pitfall | Impact | Avoidance |
|---------|--------|-----------|
| Storing Dwolla secrets in client code | Full account-compromise risk | Store keys server-side; pass only non-secret tokens to Next.js. |
| Omitting idempotency keys | Duplicate transfers | Create `transfer_attempts` table keyed by `idempotency_key` before API call. |
| Trusting client-calculated balances | Reconciliation drift | Compute balances from ledger queries on every request or cache with Redis + DB write-through. |
| Missing Plaid webhook verification | Forged status events | Verify webhook signatures before dispatching async jobs. |

---

## Performance
1. Use Server Components for dashboard cards and statement lists; cache static product metadata with `"use cache"`.
2. Avoid N+1 on transfer history by selecting related `counterparty` and `ledger` rows in Drizzle `.with()`.
3. Move Plaid token refresh and Dwolla webhook processing to Celery/background jobs so UI routes stay sub-200 ms.

---

## Security
1. Treat Drizzle schema migrations as privileged code; review all new columns affecting financial state.
2. Validate all external payloads with Zod before mapping to Drizzle inserts.
3. Rotate Plaid `client_id`/`secret` on a calendar schedule and verify sandbox-only staging behavior.
4. Log all financial events to an append-only audit table with actor, source IP, and provider trace IDs.
5. Enable `redirect` origin allowlists in Plaid and Dwolla so injected sites cannot complete linking flows.

---

## Related Projects (in workspace)

- **comicwise** — shared Next.js + authentication + payment flow patterns
- **rhixe_scans** — shared Next.js + auth + media upload patterns
- **rhixecompany-comics** — shares PostgreSQL + Drizzle + Next.js full-stack conventions

---

## Resources

| Resource | URL | Description |
|----------|-----|-------------|
| Next.js Docs | https://nextjs.org/docs | Official documentation |
| Drizzle ORM | https://orm.drizzle.dev | Type-safe SQL |
| Plaid Docs | https://plaid.com/docs | Banking integrations |
| Dwolla Docs | https://docs.dwolla.com | ACH + transfers |
| shadcn/ui | https://ui.shadcn.com | Component system |
| OWASP Finance Top 10 | https://cheatsheetseries.owasp.org/cheatsheets/Financial_Applications_Cheat_Sheet.html | Security baseline |
