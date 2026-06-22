# Architecture Decision Record

> Consolidation status for rhixecompany-comics  
> Sources: comicwise, Django-Scrapy-Selenium, selenium_webdriver

## Current Architecture

**Stack:** Django 5 + Next.js 16 + Celery + Scrapy + PostgreSQL + Drizzle ORM

| Layer | Technology | Source |
|-------|-----------|--------|
| Backend | Django 5.x + DRF | rhixecompany-comics (original) |
| Frontend | Next.js 16 App Router | comicwise → inherited |
| Scraping | Celery + Scrapy + Selenium | Django-Scrapy-Selenium → inherited |
| ORM | Drizzle (backend), Prisma (legacy) | rhixecompany-comics (original) |
| Database | PostgreSQL | Shared across all |
| Auth | NextAuth v5 / Django allauth | Dual-stack |
| Payments | Stripe | comicwise → inherited |

## Decisions

| Decision | Rationale |
|----------|-----------|
| Keep dual-stack (Django + Next.js) | Both stacks have distinct advantages; Django for admin/scraping, Next.js for user-facing reader |
| Adopt Playwright for new scrapers | Selenium is legacy-only from 2026; Playwright has native async, auto-wait, better anti-detection |
| Migrate to Drizzle fully | Drizzle is code-first, no codegen, ~7KB bundle, better for edge/serverless |
| Inherit comicwise frontend patterns | RSC by default, Server Actions, Zod validation, Zustand + TanStack Query |

## Pending Migrations

| Item | Status | Target |
|------|--------|--------|
| Frontend patterns from comicwise | 📋 Documented | ✅ Patterns extracted |
| Scraping pipeline from Django-Scrapy-Selenium | 📋 Documented | ✅ Patterns extracted |
| Selenium utilities from selenium_webdriver | 📋 Documented | ✅ Patterns extracted |
| Frontend DAL migration Prisma → Drizzle | ⏳ Pending | Future phase |
| Frontend migration Next.js 15 → 16 | ⏳ Pending | Future phase |
