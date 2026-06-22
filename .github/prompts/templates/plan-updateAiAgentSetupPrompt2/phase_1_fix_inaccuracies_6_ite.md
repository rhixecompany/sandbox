# Phase 1: Fix Inaccuracies (6 items)

> Extracted from `plan-updateAiAgentSetupPrompt2.prompt.md`.

## Phase 1: Fix Inaccuracies (6 items)

### Step 1 — Fix `comic.rating` type in §4

Clarify dual types: `comic.rating` is `decimal(10,1)` (aggregate display), `rating.rating` is `integer` (per-user 1–5 stars). Current doc says only "integer".

### Step 2 — Fix env.ts description in §3

Change "validates all 60+ environment variables" to "validates 6 active fields" (`DATABASE_URL`, `NEON_DATABASE_URL`, `AUTH_SECRET`, `NEXT_PUBLIC_API_URL`, `NODE_ENV`, `DEBUG`). Note 60+ are commented out as stubs for future use.

### Step 3 — Fix `proxy.ts` in §12

Current doc claims both `/dashboard` and `/admin` are protected. Actual `proxy.ts` only checks `/dashboard` via cookie `"auth-token"`. Admin falls through. Flag as incomplete middleware.

### Step 4 — Document raw `process.env` as auth-layer exception

`auth-config.ts`, `auth-providers.ts`, `db.ts` all use raw `process.env`. Add note in §14: "Auth files use raw `process.env` as a known exception (loaded before app initialization)."

### Step 5 — Update version numbers in §19

- React `19.2.4`
- Zod `4.3.6` (v4 — not v3, different API surface)
- Zustand `5.0.11`
- Vitest `4.0.18`
- TypeScript `5.9.3`
- Drizzle ORM `0.45.1`
- NextAuth `5.0.0-beta.30`
- Commander `14.0.3` (devDependency, not runtime)

Note Zod v4 API differences from widely-documented v3.

### Step 6 — Fix ESLint description in §13

Only 3 active rules: `no-explicit-any`, `no-unused-vars`, `no-import-type-side-effects`. Plugins (`better-tailwindcss`, `playwright`, `vitest`, `drizzle`, `zod`) are registered but have no custom rules enabled.

---
