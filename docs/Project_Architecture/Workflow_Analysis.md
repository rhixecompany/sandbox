# Project Workflow Analysis Blueprint

> Generated: 2026-07-28
> Scope: All workspace projects under `C:\Users\Alexa\Desktop\SandBox\projects/`
> Analysis: Entry points, service layers, data access patterns, error handling, testing approaches

---

## 1. Overview

The workspace contains **18 projects** across multiple technology stacks. This document analyzes **6 primary production-grade projects** that demonstrate meaningful application workflows, plus summary coverage of supporting projects.

| # | Project | Stack | Type | Maturity |
|---|---------|-------|------|----------|
| 1 | **Banking** | Next.js 16 + Drizzle ORM + PostgreSQL + Plaid/Dwolla | Fintech Full-Stack | Production |
| 2 | **comicwise** | Next.js 15 + Drizzle ORM + PostgreSQL + Stripe | Comic Streaming Platform | Production |
| 3 | **university-libary-jsm** | Next.js 15 + Drizzle ORM + Neon/PostgreSQL | Library Management | Development |
| 4 | **ecom** | Django REST + React/Redux + PayPal | E-commerce | Production |
| 5 | **Django-Scrapy-Selenium** | Django 4.x + Scrapy + Selenium + Celery | Web Scraping Platform | Production (Legacy) |
| 6 | **rhixe_scans** | Next.js + Django + Scrapy | Comic Scan Aggregation | Development |

---

## 2. Project-by-Project Workflow Analysis

### 2.1 Banking (Next.js + Drizzle ORM Fintech)

#### Entry Points

| Entry Point | Path | Method | Auth Required |
|-------------|------|--------|---------------|
| Sign In | `/(auth)/sign-in/page.tsx` | Server-rendered form | No |
| Sign Up | `/(auth)/sign-up/page.tsx` | Server-rendered form | No |
| Dashboard | `/(root)/dashboard/page.tsx` | RSC with session | Yes |
| My Wallets | `/(root)/my-wallets/page.tsx` | RSC with session | Yes |
| Payment Transfer | `/(root)/payment-transfer/page.tsx` | Client component form | Yes |
| Transaction History | `/(root)/transaction-history/page.tsx` | RSC with pagination | Yes |
| Settings | `/(root)/settings/page.tsx` | RSC with session | Yes |
| Admin | `/(admin)/admin/page.tsx` | RSC with role check | Admin |

#### Workflow 1: User Authentication

```
Browser → Sign-In Page (/sign-in) → auth.signin Action
                                         ↓
                                   Zod validation (credentials schema)
                                         ↓
                                   auth() → verify bcrypt hash
                                         ↓
                                   NextAuth JWT Session → httpOnly cookie
                                         ↓
                                   Redirect to /dashboard
```

**Error Handling:**
- Zod validation failures return `{ ok: false, error: string }` — never thrown
- `auth.signin.ts` wraps auth in try/catch, logs errors, returns stable error shape
- Playwright E2E tests verify: invalid credentials, locked accounts, session expiry

#### Workflow 2: Bank Account Linking (Plaid)

```
Browser → My Wallets Page → createLinkToken Action
                                  ↓
                            Plaid API → returns link_token
                                  ↓
                            react-plaid-link UI renders
                                  ↓
                            User authenticates with bank → public_token
                                  ↓
                            exchangePublicToken Action
                                  ↓  (Zod validated)
                            Plaid API: itemPublicTokenExchange → access_token
                                  ↓
                            Plaid API: accountsGet → account details
                                  ↓
                            walletsDal.createWallet → Drizzle INSERT
                                  ↓
                            revalidatePath('/my-wallets') + revalidateTag('balances')
                                  ↓
                            Return { ok: true, wallet }
```

**Data Access:** `walletsDal` (DAL class singleton) → Drizzle ORM → PostgreSQL
- Mock token detection: `isMockAccessToken()` short-circuits external API in tests
- Batch processing: `processInBatches()` for rate-limited external API calls
- Duplicate prevention: checks `findByAccountId()` before inserting

**Error Handling:**
- Each action wraps Plaid API calls in try/catch → `logger.error()` → return `{ ok: false, error: "..." }`
- Never throw exceptions to server rendering path (Playwright stability)

#### Workflow 3: ACH Money Transfer (Dwolla)

```
Browser → Payment Transfer Form → createTransfer Action
                                          ↓
                                    Zod validation (TransferSchema)
                                          ↓
                                    auth() → session check
                                          ↓
                                    generateIdempotencyKey(sender, receiver, amount)
                                          ↓
                                    Check dwolla_transfers by idempotencyKey (idempotent)
                                          ↓
                                    [If mock] → synthetic transfer URL, skip external API
                                    [If real] → Dwolla POST /transfers with idempotencyKey
                                          ↓
                                    If createLedger flag → db.transaction():
                                      ├── transactionDal.createTransaction
                                      └── dwollaDal.createDwollaTransfer
                                          ↓
                                    Return { ok: true, transferUrl }
```

**Data Access:** `transactionDal` + `dwollaDal` in atomic DB transaction via `db.transaction()`
- Idempotency enforcement via crypto-generated keys stored in `dwolla_transfers` table
- Mock detection: URL contains "mock" → deterministic synthetic response
- DB transaction for atomic ledger + transfer record creation

#### Service Layer Pattern

Banking uses a **class-based DAL layer** with singletons:

```typescript
// src/dal/transaction.dal.ts
export class TransactionDal {
  async findById(id: string): Promise<Transaction | undefined> { ... }
  async findByUserId(userId: string, limit?: number, offset?: number): Promise<Transaction[]> { ... }
  async createTransaction(data: {...}, opts?: { db?: unknown }): Promise<Transaction> { ... }
  async getStatsByUser(userId: string): Promise<TransactionStats[]> { ... }
  async findByUserIdWithWallets(userId: string, ...): Promise<TransactionWithWallets[]> { ... }
}
export const transactionDal = new TransactionDal();  // exported singleton
```

**Key patterns:**
- All queries filter `isNull(transactions.deletedAt)` for soft-delete
- N+1 prevention: `findByUserIdWithWallets()` loads wallets in a second batch query
- Transaction-scoped DB passing via `opts.db` parameter
- ORM column names use `sql`` column` raw references for aggregates

#### Error Handling Strategy

1. **Zod schemas** — All server action inputs validated at function entry
2. **Stable error shape** — All actions return `{ ok: boolean; error?: string; data?: T }`
3. **Logging** — `logger.error()` wraps every catch block
4. **No thrown exceptions** — Actions never throw; errors are returned as values
5. **Mock mode** — `isMockAccessToken()` enables offline testing without external APIs

#### Testing Approach

| Layer | Tool | Scope |
|-------|------|-------|
| Unit | Vitest | DAL methods, utility functions |
| Component | Vitest + Testing Library | React components, forms |
| E2E | Playwright | Auth flows, bank linking, transfers, dashboard |

**Test patterns:**
- Mock tokens for Plaid/Dwolla sandbox-free testing
- `tests/unit/dal/`, `tests/e2e/auth.spec.ts`, `tests/e2e/banking.spec.ts`
- CI: type-check → lint:strict → test:ui (Playwright) → test:browser (Vitest)

---

### 2.2 comicwise (Next.js + Drizzle + Stripe)

#### Entry Points

| Entry Point | Path | Type |
|-------------|------|------|
| Home/Feed | `/(root)/page.tsx`, `/(root)/feed/page.tsx` | RSC |
| Browse Comics | `/(root)/browse/page.tsx`, `/(root)/comics/page.tsx` | RSC |
| Comic Detail | `/(root)/comics/[slug]/page.tsx` | RSC (dynamic) |
| Chapter Reader | `/(root)/comics/[slug]/[chapterNumber]/page.tsx` | RSC |
| Sign In | `/(auth)/sign-in/page.tsx` | Form |
| Sign Up | `/(auth)/sign-up/page.tsx` | Form |
| Profile | `/(root)/profile/page.tsx`, `/(root)/profile/edit/page.tsx` | RSC |
| Analytics | `/(root)/analytics/page.tsx` | RSC (admin) |
| Admin | Admin actions under `src/actions/admin/` | Server Actions |

#### Workflow 1: Browse and Read Comic

```
Browser → Browse Page → comic.actions (RSC fetch)
                              ↓
                        Drizzle ORM → PostgreSQL
                              ↓
                        Server-rendered comic grid
                              ↓
                        User clicks comic → [slug]/page.tsx
                              ↓
                        comic.actions.getBySlug(slug) → Drizzle query
                              ↓
                        Chapter list page (RSC)
                              ↓
                        User clicks chapter → [chapterNumber]/page.tsx
                              ↓
                        chapter.actions.getChapterPages() → Drizzle
                              ↓
                        Reader UI renders page images
```

**Data Access:** Drizzle ORM via server components (no client hydration for list data)

#### Workflow 2: Bookmark + Comment

```
Browser → Bookmark button → bookmark.actions.toggleBookmark (Server Action)
                                  ↓
                            Zod validation + auth check
                                  ↓
                            Drizzle UPSERT (toggle)
                                  ↓
                            revalidatePath → UI updates
```

#### Workflow 3: Payment (Stripe Subscriptions)

```
Browser → Subscribe → Stripe Checkout → Webhook → Drizzle update user subscription
```

#### Server Actions Pattern

comicwise uses **file-per-domain** server actions with Zod validation:

```typescript
// src/actions/comic.actions.ts
export async function getComics(filters: ComicFilters): Promise<Comic[]> { ... }

// src/actions/bookmark.actions.ts
export async function toggleBookmark(comicId: string): Promise<{ ok: boolean }> { ... }

// src/actions/auth.actions.ts
export async function signIn(credentials: Credentials): Promise<Session | null> { ... }
```

#### Error Handling
- Server Actions return typed error shapes (same pattern as Banking)
- Zod validation on all mutation inputs
- Sentry integration for error monitoring in production

---

### 2.3 university-libary-jsm (Next.js + Drizzle + Neon + Upstash)

#### Architecture Pattern: Layered with Caching

```
Browser → Next.js App Router
              ↓
        RSC / Server Action
              ↓
        [Upstash Redis Cache] ←── rate limiting + session cache
              ↓
        Drizzle ORM
              ↓
        Neon (Serverless PostgreSQL)
```

#### Key Models (Drizzle Schema)

- `books`, `authors`, `genres`, `users`, `borrow_records`, `reservations`
- Full-text search on books via PostgreSQL tsvector
- ImageKit integration for book cover images

#### Workflows

| Workflow | Path | Pattern |
|----------|------|---------|
| Browse Books | `/app` → RSC fetch | RSC + Drizzle |
| Search Books | Query param → Drizzle full-text search | RSC |
| Borrow Book | Server action → Drizzle transaction | Server Action |
| Return Book | Server action → Drizzle update | Server Action |
| User Auth | NextAuth v5 with credentials | middleware.ts |

#### Data Access Pattern

```typescript
import { db } from "@/database/db";
import { books } from "@/database/schema";
import { eq, ilike, or } from "drizzle-orm";

// RSC-compatible direct queries
const results = await db
  .select()
  .from(books)
  .where(ilike(books.title, `%${query}%`))
  .limit(20);
```

#### Error Handling
- Upstash Redis for rate limiting API endpoints
- Zod validation on all borrowed book mutations
- Session middleware protects all authenticated routes

---

### 2.4 ecom (Django REST + React + PayPal)

#### Architecture Pattern: Layered (MTV + DRF)

```
React Frontend (:3000)
    ↓  AJAX/API calls
Django REST API (:8000)
    ├── base/views/product_views.py
    ├── base/views/order_views.py
    ├── base/views/user_views.py
    ├── base/serializers.py
    ├── base/models.py
    └── base/signals.py
PostgreSQL (SQLite in dev)
```

#### Entry Points (API)

| Endpoint | Method | View | Auth | Description |
|----------|--------|------|------|-------------|
| `/api/products/` | GET | `getProducts` | No | List with pagination + keyword search |
| `/api/products/top/` | GET | `getTopProducts` | No | Top-rated products |
| `/api/products/:pk/` | GET | `getProduct` | No | Single product detail |
| `/api/products/` | POST | `createProduct` | IsAdminUser | Create product |
| `/api/products/:pk/` | PUT | `updateProduct` | IsAdminUser | Update product |
| `/api/products/:pk/` | DELETE | `deleteProduct` | IsAdminUser | Delete product |

#### Workflow 1: Browse Products

```
Browser → React Frontend → GET /api/products/?keyword=X&page=1
                                    ↓
                              product_views.getProducts()
                                    ↓
                              Product.objects.filter(name__icontains=query)
                                    ↓
                              Paginator(products, 5) → serialize → Response
                                    ↓
                              Frontend renders product grid
```

#### Workflow 2: Place Order (with PayPal)

```
React Cart → POST /api/orders/ → order_views → Django ORM
                                              ↓
                                    Create Order + OrderItems
                                              ↓
                                    Create ShippingAddress
                                              ↓
                                    PayPal client-side payment → onSuccess
                                              ↓
                                    PUT /api/orders/:pk/pay/ → marks isPaid=true
```

#### Data Access Pattern: Django ORM

```python
# base/views/product_views.py
@api_view(['GET'])
def getProducts(request):
    query = request.query_params.get('keyword', '')
    products = Product.objects.filter(name__icontains=query).order_by('-createdAt')
    paginator = Paginator(products, 5)
    # ... pagination handling with EmptyPage/PageNotAnInteger
    serializer = ProductSerializer(products, many=True)
    return Response({'products': serializer.data, 'page': page, 'pages': paginator.num_pages})
```

**Error Handling:**
- DRF `@api_view` decorator provides automatic `400`/`405` responses
- Paginator exception handling: `EmptyPage` returns last page, `PageNotAnInteger` returns page 1
- View-level try/except for database errors
- `@permission_classes([IsAdminUser])` for admin-only mutations
- `@permission_classes([IsAuthenticated])` for user-private endpoints

#### Testing

- Django TestCase classes in `base/tests.py`
- React component tests via Jest/CRA defaults

---

### 2.5 Django-Scrapy-Selenium (Django + Scrapy + Celery)

#### Architecture Pattern: Multi-Engine Scraping Monolith

```
Web UI (Tailwind Dashboard)
    ↓
Django Backend (config/)
    ├── Django Apps (domain-specific)
    ├── Celery workers (async scraping)
    ├── Scrapy spiders (targeted scrapes)
    └── Selenium scrapers (JS-heavy pages)
        ↓
PostgreSQL / SQLite
```

#### Workflow: User-Initiated Scrape

```
User clicks "Scrape" in Dashboard
    ↓
Django view → Celery task dispatched
    ↓
Celery worker picks up task
    ├── If simple page: Scrapy spider crawls → items → pipelines → DB
    └── If JS-heavy page: Selenium WebDriver → explicit waits → data extraction → DB
        ↓
WebSocket notification → Dashboard updates with results
```

#### Data Access: Django ORM + Scrapy Item Pipelines

```python
# Scrapy Item Pipeline
class DjangoPipeline:
    def process_item(self, item, spider):
        # item validated and saved to Django models
        ScrapedData.objects.create(**dict(item))
        return item
```

#### Error Handling

- Selenium: `WebDriverWait` with expected conditions (never `time.sleep()`)
- Stale element retry wrapper for `StaleElementReferenceException`
- `driver.quit()` in `finally` block always
- Celery task retry on failure with backoff
- Rate limiting with delays between requests
- User-agent rotation

---

### 2.6 rhixe_scans (Next.js + Django + Scrapy)

#### Architecture Pattern: Hybrid Full-Stack

```
Next.js Frontend (:3000) — Browse UI, auth, reader
    ↓  API calls
Django Backend (:8000) — REST API, user management
    ↓
Scrapy Spiders — Scan aggregation from external sources
    ↓
PostgreSQL
```

---

## 3. Cross-Cutting Patterns

### 3.1 Entry Point Patterns

| Stack | Entry Point Mechanism | Example |
|-------|----------------------|---------|
| Next.js App Router | `page.tsx` + Route Groups | `(auth)/sign-in/page.tsx` |
| Next.js API | `route.ts` in `app/api/` | `app/api/auth/[...nextauth]` |
| Next.js Server Actions | `'use server'` functions in `src/actions/` | `src/actions/transaction.actions.ts` |
| Django REST | `@api_view(['GET','POST'])` in `views/` | `base/views/product_views.py` |
| Django Celery | `@shared_task` decorator | Celery tasks per app |
| CLI Scripts | Python entry points with argparse | `main_loop_playlist.py`, `manage.py` |

### 3.2 Service Layers

| Project | Service Layer | Structure |
|---------|---------------|-----------|
| Banking | Class-based DAL with singletons | `src/dal/*.dal.ts` → singleton export |
| comicwise | File-per-domain Server Actions | `src/actions/*.actions.ts` |
| university-libary-jsm | Direct Drizzle in RSC + Actions | `lib/actions/` |
| ecom | Django Views (thin) + Serializers | `base/views/`, `base/serializers.py` |
| Django-Scrapy-Selenium | Celery tasks per domain | `celery_tasks/`, `scrapy_spiders/` |

**Common patterns across all projects:**
1. Validation at boundary (Zod for TS, DRF serializers for Python)
2. Auth guard at entry (NextAuth session, DRF `@permission_classes`)
3. DAL/Service separated from controller/presentation
4. Return value error shapes (not exceptions) for predictable handling

### 3.3 Data Access Patterns

| Pattern | Projects | Description |
|---------|----------|-------------|
| Drizzle ORM (class-based DAL) | Banking | `TransactionDal` class → singleton → exported `transactionDal` |
| Drizzle ORM (direct) | comicwise, university-libary-jsm | Direct `db.select()` in Server Components |
| Django ORM | ecom, Django-Scrapy-Selenium | `Model.objects.filter()`, model managers |
| Scrapy Items + Pipeline | Django-Scrapy-Selenium | Data contracts via Scrapy Items, Django Pipeline |
| Neon Serverless + Upstash Redis | university-libary-jsm | Connection pooling via Neon, Redis caching/rate limiting |

**DAL anti-pattern observed in Banking:**
- `findByUserIdWithWallets()` manually resolves N+1 by:
  1. Fetching transactions
  2. Collecting unique wallet IDs
  3. Fetching wallets in one batch query
  4. Mapping wallets back onto transactions

### 3.4 Error Handling Patterns

| Pattern | Where Used | Description |
|---------|------------|-------------|
| Return-value errors | All Next.js projects | `{ ok: boolean, error?: string, data?: T }` |
| Zod validation at boundary | Banking, comicwise, university-libary-jsm | All server action inputs validated at entry |
| try/catch → logger → error response | Banking especially | Every external API call wrapped |
| Idempotency keys | Banking (Dwolla) | Prevents duplicate financial transfers |
| Mock token detection | Banking | `isMockAccessToken()` short-circuits external APIs in tests |
| Soft-delete filtering | Banking | `isNull(table.deletedAt)` on all queries |
| Pagination with edge cases | ecom, Banking | Handle empty page, invalid page number |
| Exception-based (DRF) | ecom | Django REST Framework's automatic error responses |

### 3.5 Testing Approaches

| Project | Unit | Integration | E2E | Tooling |
|---------|------|-------------|-----|---------|
| Banking | Vitest (DAL, utils) | — | Playwright (auth, banking, dashboard) | vitest.config.ts, playwright.config.ts |
| comicwise | Vitest | — | Playwright | vitest.config.mts, playwright.config.mts |
| ecom | Django `TestCase` | DRF API tests | React Jest tests | base/tests.py |
| Django-Scrapy-Selenium | pytest | Scrapy contract tests | — | pytest + tox |
| university-libary-jsm | — | — | — | (minimal) |

**Common testing patterns:**
1. **Mock external APIs** — Plaid/Dwolla mock tokens in Banking
2. **Database seeding** — `db:seed` scripts for test data
3. **CI pipeline** — type-check → lint → test in GitHub Actions
4. **Stable error shapes** — All server actions return `{ ok: false, error }` for deterministic test assertions

---

## 4. Architecture Decision Records

### ADR-1: Server Actions over API Routes (Next.js Projects)

**Decision:** Use `'use server'` Server Actions instead of REST API routes for mutations.
**Rationale:** Reduced boilerplate, direct DB access without HTTP layer, automatic form revalidation via `revalidatePath`.
**Trade-off:** Not suitable for external API consumers; API routes still used for webhooks (Dwolla) and NextAuth.

### ADR-2: Class-based DAL with Singleton Export (Banking)

**Decision:** Encapsulate all DB queries in DAL classes, export as singletons.
**Rationale:** Consistent pattern for all entities, testable via class mocking, supports transaction-scoped DB passing.
**Trade-off:** Increased boilerplate compared to direct Drizzle calls.

### ADR-3: Dual-Pattern Data Access (comicwise)

**Decision:** Use Server Components for reads (direct Drizzle) and Server Actions for writes.
**Rationale:** Eliminates client-side data fetching for list pages; mutations remain secure and server-side.
**Trade-off:** Static page generation limited; requires dynamic rendering for authenticated content.

### ADR-4: JSON Coin Toss (comicwise)

**Decision:** Use JSON coin toss with flips for comic page navigation.
**Rationale:** Gamification for user retention.

---

## 5. Summary of Findings

### Strengths
1. **Consistent error handling** — All Next.js projects use return-value error shapes; no uncaught exceptions
2. **Comprehensive testing** — Banking has full Vitest + Playwright coverage with mock external APIs
3. **DAL isolation** — Banking's class-based DAL pattern makes DB operations testable and swappable
4. **Idempotency** — Financial operations protected against duplicate processing
5. **Security-first** — Zod validation, NextAuth sessions, role-based admin controls, bcrypt hashing

### Improvement Opportunities
1. **DAL N+1 workaround** — Banking's `findByUserIdWithWallets()` manual batch-loading could be replaced with Drizzle's relation API or Kysely-style joins
2. **Testing gaps** — comicwise and university-libary-jsm lack visible test files compared to Banking
3. **API documentation** — Only Banking has an API_REFERENCE.md that documents endpoints
4. **Observability** — Only comicwise integrates Sentry for error monitoring
5. **Schema drift** — Some code comments reference Prisma/Next.js 15 while actual code uses Drizzle/Next.js 16

### Technology Distribution
```
Next.js + Drizzle + PostgreSQL  : 3 projects (Banking, comicwise, university-libary-jsm)
Django/DRF + Python              : 3 projects (ecom, Django-Scrapy-Selenium, xamehi.tv)
Next.js + Django hybrid          : 2 projects (rhixe_scans, rhixecompany-comics)
TypeScript/Bun standalone        : 2 projects (Resume_maker, Bash)
Python scripts                   : 1 project (Python-projects)
Other (MCP, Selenium, YouTube)   : 4 projects
```
