# Consolidation Patterns

Inherited patterns, decisions, and discarded ideas from:
- projects/comicwise
- projects/Django-Scrapy-Selenium
- projects/selenium_webdriver

---

## Inherited Patterns

### Frontend (from comicwise)
- Next.js 16 App Router + React Server Components for public-facing reader pages
- shadcn/ui as owned code in frontend/src/components/ui/
- Drizzle-style data access layer modules under frontend/src/dal/
- NextAuth v5 with database sessions
- React Query + revalidation tags for server state synchronization
- Zod-validated Server Actions for mutations
- Vitest + Playwright test gates

### Backend + Scraping (from Django-Scrapy-Selenium)
- Django 5 + DRF for admin, auth, and content APIs
- Celery + Redis for async task processing
- Scrapy 2.14 async-first crawler pattern inside Celery workers
- Docker Compose orchestration with health checks
- Explicit wait + stale-element retry utilities

### Automation Utilities (from selenium_webdriver)
- selenium-webdriver 4.x with Selenium Manager driver handling
- Centralized WebDriverWait helpers
- Retry decorators wrapped in managed driver lifecycle with driver.quit()

---

## Decisions

- Keep Django as the source of truth for content IDs, permissions, and background jobs
- Keep Next.js as the reader experience, SEO pages, and caching layer
- Wire stacks through DRF + django-cors-headers + shared JWT (SimpleJWT)
- Use drf-spectacular OpenAPI output + openapi-typescript for typed API contracts
- Use Celery beat for scheduled crawls; prefer scrapy-playwright for JS targets and keep Selenium for login/MFA flows
- Serve all media through CDN/object storage; never through Django/Gunicorn

---

## Discarded

- Separate Webpack-based frontend build in favor of Next.js standalone output
- Duplicate Express-style API layer from legacy xamehi in the consolidated reader service
- Client-side payment state as source of truth; all payment transitions handled server-side via webhooks
- Implicit Selenium waits and sleep-based scraping flows; replaced with explicit waits and async Scrapy
