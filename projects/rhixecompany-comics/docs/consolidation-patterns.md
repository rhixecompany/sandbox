# Consolidation Patterns

> Extracted from comicwise, Django-Scrapy-Selenium, and selenium_webdriver  
> Target: rhixecompany-comics (Django + Next.js 16 dual-stack)

## Table of Contents

1. [comicwise — Frontend Patterns](#1-comicwise--frontend-patterns)
2. [Django-Scrapy-Selenium — Scraping Patterns](#2-django-scrapy-selenium--scraping-patterns)
3. [selenium_webdriver — Automation Patterns](#3-selenium_webdriver--automation-patterns)
4. [Discarded Patterns](#4-discarded-patterns)

---

## 1. comicwise — Frontend Patterns

**Stack:** Next.js 15, Prisma 7, NextAuth v5, Stripe, Tailwind 4, shadcn/ui, Zustand, React Query 5, Zod 4

| Pattern | Inherit? | Notes |
|---------|----------|-------|
| RSC chapter pages | ✅ | Render metadata server-side; only interactions need hydration |
| Server Actions in `actions/` dir | ✅ | Use `'use server'` module-level + Zod validation |
| Prisma DAL boundaries | ✅ | Keep access behind `dal/*` modules; precise `select`/`include` |
| Zustand for UI state only | ✅ | Server state → React Query; UI state → Zustand |
| TanStack Query for API data | ✅ | Cache management, auto-refetch |
| Zod as boundary contract | ✅ | Validate before Server Actions and before DB writes |
| Stripe webhooks for subscriptions | ✅ | Use Next.js API routes for webhook endpoints |
| `next/image` with CDN | ✅ | Signed URLs for chapter images |

## 2. Django-Scrapy-Selenium — Scraping Patterns

**Stack:** Django 4.x, DRF, Scrapy, Selenium, Celery + Redis, PostgreSQL

| Pattern | Inherit? | Notes |
|---------|----------|-------|
| Celery + Scrapy integration | ✅ | `shared_task` decorator; `AsyncCrawlerProcess` for spiders |
| Django-Celery config | ✅ | `celery.py` with namespace config |
| Dead-letter scraping logs | ✅ | Store raw HTML + parse failures for reprocessing |
| DRF permissioned endpoints | ✅ | Scraping control restricted to admin users |
| Scrapy concurrent requests (16-50) | ✅ | Tune via `CONCURRENT_REQUESTS` per domain |
| Sanitize scraped HTML before storage | ✅ | Prevent stored XSS |

## 3. selenium_webdriver — Automation Patterns

**Stack:** Node.js 18+, selenium-webdriver 4.x, ChromeDriver

| Pattern | Inherit? | Notes |
|---------|----------|-------|
| Selenium Manager for drivers | ✅ | Zero-config driver management |
| Explicit waits (no `sleep()`) | ✅ | `driver.wait(until.elementLocated(...))` |
| Centralized retry utils | ✅ | `safeClick`, `safeGetText` with stale element retry |
| Session reuse for batch scrapes | ✅ | Single browser session; avoid 3-5s startup each time |
| Headless optimizations | ✅ | `--disable-dev-shm-usage`, `--disable-extensions` |
| Respect `robots.txt` + polite delays | ✅ | 2s+ delays between requests |

## 4. Discarded Patterns

| Pattern | Source | Reason Discarded |
|---------|--------|------------------|
| pnpm package manager | comicwise | rhixecompany-comics uses npm; Bun migration planned separately |
| Prisma ORM | comicwise | rhixecompany-comics uses Drizzle ORM instead |
| Selenium for new scrapers | selenium_webdriver | Playwright is modern alternative; Selenium legacy-only from 2026 |
| Twisted callback chains | Django-Scrapy-Selenium | Async-first (`AsyncCrawlerProcess`) replaces traditional Twisted |
| `time.sleep()` in wait logic | selenium_webdriver | Replaced with explicit `WebDriverWait` conditions |
