# Consolidation Patterns

> Source: comicwise + Django-Scrapy-Selenium + selenium_webdriver
> Target: rhixecompany-comics
> Date: 2026-06-05

## 1. Frontend Patterns (from comicwise)

### Tech Stack
Next.js 15+, TypeScript, Prisma ORM, NextAuth v5, Stripe/PayPal, UploadThing, Tailwind CSS, shadcn/ui

### Key Patterns
- **Prisma singleton** — `lib/prisma.ts` must use `globalThis` singleton pattern to prevent connection pool exhaustion on Next.js hot reload
- **Auth.js v5 split config** — `auth.config.ts` (edge-safe, no Prisma/Node imports) + `auth.ts` (PrismaAdapter + JWT session). Never import `auth.ts` in middleware.
- **Server Actions for mutations** — Use Server Actions (not client-side API calls) for bookmark, reading progress, payment session creation
- **Stripe webhooks first** — Never grant access based on redirect URL alone; wait for `checkout.session.completed` webhook
- **UploadThing middleware auth** — Always call `auth()` inside `.middleware()` and throw `UploadThingError("Unauthorized")` if no session
- **React Server Components** — Use RSC for comic listings; zero client JS for data-heavy pages
- **Suspense boundaries** — Wrap chapter/comic list pages in `loading.tsx` + Suspense for perceived performance

### What to Inherit
- Next.js App Router structure with Server Components
- Prisma schema (User, Account, Session, VerificationToken from Auth.js)
- Stripe checkout + webhook handling pattern
- UploadThing FileRouter for file uploads
- shadcn/ui component library + Tailwind CSS styling
- NextAuth v5 with PrismaAdapter (JWT strategy)

### What to Discard
- Legacy `/api/` route pattern for Stripe — replace with Server Actions
- Client-side auth checks as primary guard — keep server-side enforcement
- Comic-specific page routes that duplicate reader logic — generalize to content-agnostic patterns

---

## 2. Backend/Scraping Patterns (from Django-Scrapy-Selenium)

### Tech Stack
Python 3.10+, Django 4.x, DRF, Scrapy 2.14+, Selenium, Celery + Redis, Docker

### Key Patterns
- **AsyncCrawlerProcess** — Use Scrapy 2.14+'s native asyncio integration; replace legacy `CrawlerProcess`
- **Separate Celery queues** — Route scraping → `queue=scraping`, image processing → `queue=media`, alerts → `queue=notifications`. Set `task_acks_late=True` and `task_reject_on_worker_lost=True`
- **Explicit waits only in Selenium** — Use `WebDriverWait` + expected conditions; never `time.sleep()` or implicit waits
- **Proxy rotation is not enough** — Combine IP rotation with user-agent rotation, realistic `DOWNLOAD_DELAY`, TLS fingerprint masking
- **Sanitize scraped data** — Treat all scraped HTML as untrusted; escape/validate before ORM insert
- **Django bulk writes** — Use `bulk_create(batch_size=500)` inside Celery tasks wrapped in `transaction.atomic()`
- **Redis result backend TTL** — Set `result_expires=3600` to prevent memory growth from high-frequency jobs

### What to Inherit
- Scrapy spider structure with `custom_settings` dict (not deprecated class attributes)
- Celery task queue with `django-celery-results` + `django-celery-beat`
- Django REST Framework for admin/dashboard API
- Explicit Selenium wait patterns with retry loops for stale elements
- Proxy rotation middleware for Scrapy

### What to Discard
- BeautifulSoup + requests for large crawls — use Scrapy (39x faster on >1000 pages)
- Single-queue Celery setup — always separate queues
- Spider class-attribute settings — use `custom_settings = {}` dict
- Direct rendering of scraped HTML without sanitization

---

## 3. Automation Patterns (from selenium_webdriver)

### Tech Stack
Node.js 18+, ES Modules, selenium-webdriver 4.x, ChromeDriver

### Key Patterns
- **ES Modules** — `"type": "module"` in package.json; top-level `await` available on Node 18+
- **Explicit waits** — `driver.wait(until.elementLocated(By.css(...)), 10000)`; no sleep/implicit
- **Driver cleanup** — Always `await driver.quit()` inside `try/finally`; prevents zombie Chrome processes
- **Re-locate on stale** — In retry wrappers, call `driver.findElement()` fresh inside catch block
- **`--headless=new`** — Mandatory for Chrome 109+; set via `options.addArguments('--headless=new')`
- **`pageLoadStrategy: 'eager'`** — Returns control when DOM is interactive, 20-40% faster

### What to Inherit
- Selenium WebDriver 4.x scraper structure with ES Modules
- Retry logic patterns for stale element handling
- `--headless=new` + Docker-friendly Chrome flags
- Polite scraping hygiene (jitter between page loads, respect robots.txt)
- Page Object pattern for selector centralization

### What to Discard
- Legacy `--headless` flag — removed in Selenium 4.10+
- Implicit waits — replace all with explicit waits
- `driver.sleep()` — replace all with WebDriverWait
- Cached element references for dynamic content — always re-locate

---

## 4. Migration Summary

| Pattern | Source | Target Location | Priority |
|---------|--------|-----------------|----------|
| Auth.js v5 split config | comicwise | rhixecompany-comics Next.js app | P0 |
| Stripe + webhook handling | comicwise | rhixecompany-comics payments module | P0 |
| Prisma singleton + schema | comicwise | rhixecompany-comics lib/prisma.ts | P0 |
| UploadThing file uploads | comicwise | rhixecompany-comics API routes | P1 |
| Scrapy AsyncCrawlerProcess | Django-Scrapy-Selenium | Django management commands | P1 |
| Celery queue separation | Django-Scrapy-Selenium | Django config + Docker | P1 |
| Selenium explicit waits | selenium_webdriver → Django side | Django scraping utils | P2 |
| ES Modules scraper cleanup | selenium_webdriver | Refactored Node utilities | P2 |
| shadcn/ui + Tailwind | comicwise | rhixecompany-comics frontend | P0 |
