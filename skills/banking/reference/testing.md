---
name: testing
description: "# Testing Reference"
version: 1.0.0
author: Alexa
license: MIT
metadata:
  hermes:
    tags: []
    related_skills: []
---
     1|# Testing Reference
     2|
     3|## Choosing Your Testing Approach
     4|
     5|**Before writing a test, answer these questions:**
     6|
     7|| Question | Unit Test (Vitest) | E2E Test (Playwright) |
     8|| --- | --- | --- |
     9|| **Needs live database?** | No (MSW mocks) | Yes (seeded DB) |
    10|| **Tests UI interaction?** | No (functions only) | Yes (forms, flows) |
    11|| **Can run deterministically?** | Must be stateless | Stateful OK (1 worker) |
    12|| **Needs Plaid/Dwolla?** | MSW HTTP mocking | Mock tokens + scripts |
    13|| **Priority: Speed?** | Yes (< 100ms each) | No (slower, complete) |
    14|
    15|**Decision matrix:**
    16|
    17|- Form validation → Unit test
    18|- User clicks "Link Bank" → E2E with mock tokens
    19|- Transfer business logic → Unit test
    20|- Full wallet flow → E2E test
    21|
    22|---
    23|
    24|## NEVER Do: Testing Anti-Patterns
    25|
    26|**NEVER run Playwright with `workers > 1`**  
    27|E2E tests are stateful (shared DB). Parallel execution corrupts data. Config specifies `workers: 1`. Changing this WILL break everything.
    28|
    29|**NEVER skip port cleanup before E2E**  
    30|Port 3000 must be freed. If you skip, Playwright waits forever with no error message — just silent hang. Always run port guard first.
    31|
    32|**NEVER mock Plaid/Dwolla at HTTP layer**  
    33|Use token detection instead. HTTP mocking breaks real integration testing. E2E's purpose: "does actual Plaid Link work?" Mocking HTTP invalidates that.
    34|
    35|**NEVER mix live and mock tokens in same session**  
    36|Pick one: all tests use `seed-*`/`mock-*` tokens OR all use live sandbox. Mixing confuses SDK state. Document which per test file.
    37|
    38|**NEVER forget `ENCRYPTION_KEY` in `.env.local`**  
    39|Not in `.env.example` for security reasons. Add it manually. Tests silently fail without it — no error message. Required for E2E setup.
    40|
    41|**NEVER seed DB inside individual tests**  
    42|Seed once in `global-setup.ts`, reset in `global-teardown.ts`. Per-test seeding is slow and pollutes state. Use soft deletes instead.
    43|
    44|---
    45|
    46|## Unit Tests (Vitest)
    47|
    48|**Config:** `vitest.config.ts` includes `tests/unit/**/*.test.{ts,tsx}`
    49|
    50|**Run one file:**
    51|
    52|```bash
    53|bun exec vitest run tests/unit/path/to/file.test.ts --config=vitest.config.ts
    54|```
    55|
    56|**Pattern (with MSW):**
    57|
    58|```typescript
    59|import { describe, it, expect, beforeAll, afterAll } from "vitest";
    60|import { server } from "@/tests/mocks/server";
    61|
    62|beforeAll(() => server.listen());
    63|afterAll(() => server.close());
    64|
    65|describe("registerUser", () => {
    66|  it("should create user with valid input", async () => {
    67|    const result = await registerUser({
    68|      email: "test@example.com",
    69|      password: "SecurePassword123!"
    70|    });
    71|    expect(result.ok).toBe(true);
    72|    expect(result.user?.email).toBe("test@example.com");
    73|  });
    74|});
    75|```
    76|
    77|**Mocking with MSW (HTTP layer):**
    78|
    79|```typescript
    80|import { http, HttpResponse } from "msw";
    81|import { server } from "@/tests/mocks/server";
    82|
    83|server.use(
    84|  http.post("https://api.plaid.com/institutions/search", () => {
    85|    return HttpResponse.json({ institutions: [] });
    86|  })
    87|);
    88|```
    89|
    90|---
    91|
    92|## E2E Tests (Playwright)
    93|
    94|**Config:** `playwright.config.ts` is **stateful** (`workers: 1`, no parallel)
    95|
    96|**Run all:**
    97|
    98|```bash
    99|bun run test:ui
   100|```
   101|
   102|**Run one spec:**
   103|
   104|```bash
   105|bunx playwright test tests/e2e/wallet.spec.ts --project=chromium
   106|```
   107|
   108|**Setup:** Global setup/teardown (`global-setup.ts`, `global-teardown.ts`) manages DB. If `PLAYWRIGHT_PREPARE_DB=true`, runs `bun run db:push && bun run db:seed -- --reset`.
   109|
   110|---
   111|
   112|## Mocking: Mock Tokens
   113|
   114|Use `isMockAccessToken()` to detect test tokens (start with `seed-`, `mock-`, `mock_`):
   115|
   116|```typescript
   117|// lib/plaid.ts
   118|export function isMockAccessToken(token: string): boolean {
   119|  if (!token) return false;
   120|  const t = token.toLowerCase();
   121|  return (
   122|    t.startsWith("seed-") ||
   123|    t.startsWith("mock-") ||
   124|    t.startsWith("mock_")
   125|  );
   126|}
   127|```
   128|
   129|**Skip network calls for mock tokens:**
   130|
   131|```typescript
   132|if (isMockAccessToken(accessToken)) {
   133|  return { item_id: "mock-item-id", status: "success" };
   134|}
   135|```
   136|
   137|**Examples of mock tokens (all bypass API calls):**
   138|
   139|```typescript
   140|// Valid mock tokens (detected and skip API)
   141|"seed-plaid-access-token";
   142|"seed-user-wallet-123";
   143|"SEED-TEST-TOKEN";
   144|"mock-dwolla-transfer";
   145|"MOCK-TEST-ACCOUNT";
   146|"mock_bank_account_token";
   147|"MOCK_FUNDING_SOURCE";
   148|
   149|// Invalid mock tokens (treated as real, hit API)
   150|"access-prod-abc123";
   151|"pk_live_abc123def";
   152|"***";
   153|"sometoken"; // no prefix
   154|```
   155|
   156|**Why mock tokens?**
   157|
   158|- **Deterministic:** Same mock token always returns same data
   159|- **No rate limits:** Plaid/Dwolla sandboxes have request limits; mocks don't
   160|- **Offline capability:** Can run tests without network access
   161|- **Cost-free:** No sandbox API calls (no rate limiting)
   162|- **Faster:** Mock responses are instant
   163|
   164|**When to use:**
   165|
   166|- **Unit tests:** Always use mocks (MSW HTTP mocking)
   167|- **E2E tests (happy path):** Use mock tokens to speed up testing
   168|- **E2E tests (integration):** Use real sandbox tokens (but sparingly)
   169|- **Production:** NEVER use mock tokens (verify in pre-release validation)
   170|
   171|---
   172|
   173|## E2E Plaid Mock
   174|
   175|**Inject Plaid Link mock in browser (E2E only):**
   176|
   177|```typescript
   178|// tests/e2e/helpers/plaid.mock.ts
   179|import { Page } from "@playwright/test";
   180|
   181|export async function addMockPlaidInitScript(
   182|  page: Page,
   183|  publicToken = "MOCK_PUBLIC_TOKEN"
   184|): Promise<void> {
   185|  const script = `(() => {
   186|    window.Plaid = {
   187|      create: function(opts) {
   188|        setTimeout(() => {
   189|          if (opts?.onSuccess) {
   190|            opts.onSuccess(${JSON.stringify(publicToken)}, { metadata: {} });
   191|          }
   192|        }, 0);
   193|        return { open: function() {} };
   194|      }
   195|    };
   196|  })();`;
   197|  await page.addInitScript(script);
   198|}
   199|
   200|// Usage in test
   201|test("should link bank", async ({ page }) => {
   202|  await addMockPlaidInitScript(page);
   203|  await page.goto("/dashboard");
   204|  // ... test flow
   205|});
   206|```
   207|
   208|---
   209|
   210|## Port Guard (CRITICAL before E2E)
   211|
   212|**Windows (PowerShell):**
   213|
   214|```powershell
   215|$pids = Get-NetTCPConnection -LocalPort 3000 -State Listen -ErrorAction SilentlyContinue | Select-Object -ExpandProperty OwningProcess -Unique
   216|if ($pids) { $pids | ForEach-Object { Stop-Process -Id $_ -Force } }
   217|```
   218|
   219|**macOS/Linux:**
   220|
   221|```bash
   222|lsof -ti :3000 | xargs kill -9 2>/dev/null || true
   223|```
   224|
   225|---
   226|
   227|## Troubleshooting Common Failures
   228|
   229|**Tests hang indefinitely:** Port 3000 not freed. Re-run port guard above.
   230|
   231|**Playwright can't connect:** Dev server not running. Start with `bun run dev` before E2E tests.
   232|
   233|**ENCRYPTION_KEY missing:** Tests silently fail. Add `ENCRYPTION_KEY=<32-byte-hex>` to `.env.local` (not in `.env.example` for security).
   234|
   235|**DB seed fails in global-setup.ts:** Ensure PostgreSQL is running via `docker-compose up -d postgres`. Check `DATABASE_URL` is set correctly.
   236|
   237|**Flaky Plaid Link tests:** Ensure `addMockPlaidInitScript()` is called BEFORE `page.goto()`. Mock must inject before page loads.
   238|
   239|---
   240|
   241|## Reference: File Locations & Seed User
   242|
   243|**Test locations:**
   244|
   245|- Unit: `tests/unit/**/*.test.{ts,tsx}`
   246|- E2E: `tests/e2e/**/*.spec.ts`
   247|- Helpers: `tests/e2e/helpers/*.ts`
   248|- Mocks: `tests/mocks/server.ts`
   249|
   250|**Seed user (E2E):** Email `seed-user@example.com` / Password `password123`
   251|
   252|**Required environment:** PostgreSQL (`DATABASE_URL`), `ENCRYPTION_KEY`, `NEXTAUTH_SECRET`
   253|