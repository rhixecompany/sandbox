# Migration Status — rhixecompany-comics

> Tracks consolidation progress from 3 source repos
> Last updated: 2026-06-05

## Overview

| Source Repo | Status | Priority | Notes |
|-------------|--------|----------|-------|
| comicwise | Patterns extracted | P0 | Frontend + auth + payments |
| Django-Scrapy-Selenium | Patterns extracted | P0 | Backend + scraping + Celery |
| selenium_webdriver | Patterns extracted | P2 | Node.js automation utilities |

## Phase Completion

| Phase | Description | Status |
|-------|-------------|--------|
| Phase 1 | Pattern extraction from 3 source repos | COMPLETE |
| Phase 2 | Write consolidation-patterns.md + architecture.md + migration-status.md | COMPLETE |
| Phase 3 | Branch normalization (remaining 11 repos) | PENDING |
| Phase 4 | Ignore file audit | PENDING |
| Phase 5 | Dependency audit | PENDING |
| Phase 6 | Bun migration | PENDING |
| Phase 7 | CI workflow setup | PENDING |

## Pattern Migration Tracker

### From comicwise (Frontend)
- [ ] Next.js App Router page structure
- [ ] Prisma schema (User, Account, Session, VerificationToken)
- [ ] Auth.js v5 split config (`auth.config.ts` + `auth.ts`)
- [ ] Stripe checkout + webhook handler (Server Actions)
- [ ] UploadThing FileRouter with middleware auth
- [ ] React Server Components for comic listings
- [ ] Suspense boundaries + `loading.tsx`
- [ ] shadcn/ui component library setup
- [ ] Tailwind CSS + `cn()` utility
- [ ] Zod validation schemas for forms

### From Django-Scrapy-Selenium (Backend)
- [ ] Django 5.x + DRF project structure
- [ ] Celery config with separated queues (`scraping`, `media`, `notifications`)
- [ ] `django-celery-results` + `django-celery-beat` setup
- [ ] Scrapy project with `AsyncCrawlerProcess`
- [ ] Scrapy proxy rotation middleware
- [ ] Explicit Selenium wait patterns
- [ ] Django bulk write utilities (`bulk_create`, `transaction.atomic`)
- [ ] Admin dashboard for scraping management

### From selenium_webdriver (Automation)
- [ ] ES Modules selenium-webdriver 4.x structure
- [ ] Retry logic for `StaleElementReferenceException`
- [ ] `--headless=new` + Docker Chrome flags
- [ ] Page Object pattern for selector centralization
- [ ] Polite scraping delays + robots.txt compliance

## Source Repo Status Updates

The following source repos have been marked as `Status: Consolidation target (→ rhixecompany-comics)` in their RESEARCH_REPORT.md files:
- comicwise ✅
- Django-Scrapy-Selenium ✅
- selenium_webdriver ✅
