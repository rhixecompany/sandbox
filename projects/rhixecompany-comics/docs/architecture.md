# Architecture — rhixecompany-comics

> Consolidated comic platform | 2026-06-05
> Inherits patterns from: comicwise, Django-Scrapy-Selenium, selenium_webdriver

## System Overview

```
┌─────────────────────────────────────────────────────────────────┐
│                        Next.js 16 Frontend                       │
│  App Router | TypeScript | Tailwind | shadcn/ui | RSC           │
│  Auth: NextAuth v5 + PrismaAdapter (JWT)                        │
│  Payments: Stripe + PayPal (Server Actions + webhooks)          │
│  Uploads: UploadThing (FileRouter + middleware auth)            │
└────────────────────────────┬────────────────────────────────────┘
                             │ API (REST + Server Actions)
┌────────────────────────────▼────────────────────────────────────┐
│                     Django 5.x Backend                           │
│  DRF | PostgreSQL | Celery + Redis                              │
│  Admin dashboard | API endpoints | ORM models                   │
└────────────────────────────┬────────────────────────────────────┘
                             │ Celery tasks
┌────────────────────────────▼────────────────────────────────────┐
│                   Scraping + AutomationLayer                     │
│  Scrapy 2.14+ (AsyncCrawlerProcess)                             │
│  Selenium WebDriver 4.x (explicit waits + retry loops)          │
│  Proxy rotation + rate limiting + TLS fingerprint masking       │
└─────────────────────────────────────────────────────────────────┘
```

## Tech Stack

| Layer | Technology | Source |
|-------|-----------|--------|
| Frontend | Next.js 16, TypeScript | comicwise |
| UI | Tailwind CSS, shadcn/ui, Radix | comicwise |
| Auth | NextAuth v5 + PrismaAdapter (JWT) | comicwise |
| ORM | Prisma (frontend) + Django ORM (backend) | comicwise + Django-Scrapy-Selenium |
| Payments | Stripe SDK + PayPal, Server Actions | comicwise |
| File Uploads | UploadThing | comicwise |
| Backend | Django 5.x + DRF | Django-Scrapy-Selenium |
| Task Queue | Celery + Redis (separated queues) | Django-Scrapy-Selenium |
| Scraping | Scrapy 2.14+ (AsyncCrawlerProcess) | Django-Scrapy-Selenium |
| Browser Automation | Selenium WebDriver 4.x (ES Modules) | selenium_webdriver |
| Database | PostgreSQL | shared |
| Infrastructure | Docker Compose (Django + PG + Redis + Celery + Next.js) | Django-Scrapy-Selenium |

## Key Architecture Decisions

### ADR-001: Frontend uses Next.js App Router with React Server Components
- **Why**: comicwise already implemented this pattern; RSC reduces client JS for data-heavy comic listings
- **Implication**: All data fetching in Server Components; mutations via Server Actions only

### ADR-002: Auth.js v5 split config pattern
- **Why**: PrismaAdapter requires Node.js APIs that crash edge runtime
- **Decision**: `auth.config.ts` (edge-safe, no Prisma imports) + `auth.ts` (full config with PrismaAdapter)
- **Inherited from**: comicwise

### ADR-003: Stripe webhooks for payment confirmation
- **Why**: Client-side redirects alone are unreliable and insecure
- **Decision**: Never grant content access until `checkout.session.completed` webhook fires
- **Inherited from**: comicwise

### ADR-004: Separate Celery queues
- **Why**: Scraping, media processing, and notifications have different latency/reliability requirements
- **Decision**: 3 queues (`scraping`, `media`, `notifications`) with `task_acks_late=True`
- **Inherited from**: Django-Scrapy-Selenium

### ADR-005: Scrapy AsyncCrawlerProcess
- **Why**: Scrapy 2.14+ native asyncio replaces legacy Twisted Deferred chains
- **Decision**: Use `AsyncCrawlerProcess`; set `custom_settings` dict on all spiders
- **Inherited from**: Django-Scrapy-Selenium

### ADR-006: Selenium migration path to Playwright
- **Why**: selenium_webdriver Node.js scraper uses Selenium 4.x; Playwright has 91% satisfaction vs 72% for Cypress
- **Decision**: Keep Selenium 4.x for Node.js utilities; evaluate Playwright for new scraping work
- **Migration cost**: 2-3 weeks per engineer to reach comfort level (not urgent)
- **Inherited from**: selenium_webdriver

### ADR-007: Prisma singleton pattern
- **Why**: Next.js hot-reload creates multiple instances, exhausting PostgreSQL connection pool
- **Decision**: `globalThis` singleton in `lib/prisma.ts`
- **Inherited from**: comicwise

## Security Model

- **Auth**: JWT sessions (JWE-encrypted, HttpOnly, SameSite=Lax, 30-day expiry)
- **Payments**: Webhook signature verification via `stripe.webhooks.constructEvent()`
- **Secrets**: All secrets in environment variables; never in client bundle
- **Scraping**: `ROBOTSTXT_OBEY=True`, `DOWNLOAD_DELAY`, auto-throttle enabled
- **Scraped data**: `bleach.clean()` or Django `escape()` before storage/display
- **API**: DRF `IsAuthenticated` on all sensitive endpoints
- **CSRF/XSS/SQLi**: Django + Next.js defaults + Prisma ORM parameterized queries

## Repository Structure

```
rhixecompany-comics/
├── backend/              # Django 5.x + DRF + Celery
│   ├── config/           # Django settings, Celery config
│   ├── apps/
│   │   ├── comics/       # Comic/chapter models, API
│   │   ├── scraping/     # Scrapy spiders, Selenium utils
│   │   └── users/        # Auth, profiles
│   └── requirements.txt
├── frontend/             # Next.js 16 + TypeScript
│   ├── app/              # App Router pages
│   ├── components/       # shadcn/ui + custom components
│   ├── lib/              # Prisma singleton, auth config, Stripe
│   └── package.json
├── docs/
│   ├── consolidation-patterns.md
│   ├── architecture.md   # This file
│   └── migration-status.md
├── docker-compose.yml
└── .env.example
```

## References

- `docs/consolidation-patterns.md` — Full pattern extraction from 3 source repos
- `docs/migration-status.md` — Current migration progress tracker
