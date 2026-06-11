# Sandbox Projects Inventory — rhixecompany-comics Consolidation

**Generated:** 2026-06-01 | **Source:** Prompts/repo.prompts.md

## Target Architecture

`projects/rhixecompany-comics` — Django backend + Next.js 16 App Router frontend + Scrapy/Selenium scraping

## Source Projects

### 1. `projects/comicwise` (Next.js Frontend)

| Aspect | Detail |
|--------|--------|
| **Type** | Next.js 16 comic streaming frontend |
| **Runtime** | TypeScript, pnpm workspace |
| **DB** | Drizzle ORM + PostgreSQL |
| **Auth** | NextAuth v5 + 2FA |
| **UI** | Tailwind CSS v4, shadcn/ui, Radix UI, Framer Motion |
| **Testing** | Vitest + Playwright + Testing Library |
| **CI** | GitHub workflows (test, deploy, Playwright) |
| **Key dirs** | `src/app/` (pages), `src/actions/` (server actions), `src/scripts/` (utilities), `.github/workflows/` |
| **State** | Mature, reference for frontend patterns |

### 2. `projects/Django-Scrapy-Selenium` (Django Backend)

| Aspect | Detail |
|--------|--------|
| **Type** | Django 4.x + Scrapy + Selenium scraping platform |
| **Runtime** | Python 3.12, pip |
| **Apps** | `api/apps/`, `api/home/`, `api/users/`, `crawler/` |
| **Queue** | Celery + Redis |
| **CI** | Docker Compose (Django + PostgreSQL + Redis + Celery) |
| **Lint** | ruff, mypy, djlint |
| **Key files** | `config/settings/` (base, local, production), `requirements/` |
| **State** | Mature, reference for Django patterns |

### 3. `projects/selenium_webdriver` (Node.js Scraper)

| Aspect | Detail |
|--------|--------|
| **Type** | Node.js Selenium WebDriver comic scraper |
| **Runtime** | Node.js 18+, ES Modules |
| **Scripts** | `src/scrape.js`, `src/scrape2.js`, `src/test.js` |
| **State** | Utility tool, simpler scraping scripts |

## Target Project Status (`projects/rhixecompany-comics`)

### Backend (Django) — Scaffolded

| Component | Status |
|-----------|--------|
| `config/` (settings, urls, wsgi, asgi) | ✅ Scaffolded |
| `apps/api/` | ✅ Scaffolded (admin, urls) |
| `apps/comics/` | ✅ Scaffolded (models, serializers, views, admin) |
| `apps/core/` | ✅ Scaffolded (urls, views) |
| `apps/scraping/` | ✅ Scaffolded (app config only) |
| `apps/users/` | ✅ Scaffolded (models, urls) |
| `requirements.txt` | ✅ Core deps listed |
| `.venv/` | ✅ Created |
| Actual model/view/serializer code | ❌ Stubs only |

### Frontend (Next.js 16) — Scaffolded

| Component | Status |
|-----------|--------|
| `src/app/layout.tsx` | ✅ Basic layout |
| `src/app/page.tsx` | ✅ Basic page |
| `src/app/globals.css` | ✅ Tailwind setup |
| `next.config.ts` | ✅ Configured |
| `tsconfig.json` | ✅ Configured |
| `package.json` | ✅ Minimal deps |
| Components, pages, actions | ❌ Not migrated from comicwise |

### Git — Configured

| Item | Status |
|------|--------|
| Branches | ✅ `development` (active), `production` (default) |
| Initial commit | ✅ "chore: initial scaffold" |
| Remote | ❌ Not synced |

## Migration Strategy

1. **Backend**: Migrate models, serializers, views from Django-Scrapy-Selenium `api/apps/` into `apps/comics/`, `apps/api/`, `apps/users/`
2. **Frontend**: Migrate components, pages, actions from comicwise `src/` into `frontend/src/`
3. **Scraping**: Merge scraping scripts from selenium_webdriver into `apps/scraping/`
4. **Infra**: Set up docker-compose from Django-Scrapy-Selenium patterns
5. **CI**: Set up GitHub workflows from comicwise patterns
6. **Cleanup**: Disable/remove legacy comicwise-specific workflows
