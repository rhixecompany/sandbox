# REPOSITORY_SUMMARY.md

# rhixecompany-comics — Dual-Stack Comics Platform

**Generated:** 2026-07-25  
**Status:** Active  
**Path:** `projects/rhixecompany-comics/`

---

## Architecture

| Property | Value |
|----------|-------|
| **Type** | Dual-stack web platform (Django backend + Next.js frontend) |
| **Pattern** | Two independent stacks sharing PostgreSQL, Celery for async |
| **Reference** | [Workflow Analysis](../docs/Project_Architecture/Workflow_Analysis.md) |

Django 4.x + DRF (backend API) + Next.js 16 App Router (frontend) + Celery + Redis. Scraping and comics management platform with separate frontend and backend services.

---

## Technology Stack

### Backend
| Layer | Technology |
|-------|------------|
| **Framework** | Django 4.x + Django REST Framework |
| **Language** | Python 3.10+ |
| **Auth** | SimpleJWT + django-cors-headers |
| **Database** | PostgreSQL (shared) |
| **Async** | Celery + Redis |
| **Infra** | Docker Compose, Gunicorn |

### Frontend
| Layer | Technology |
|-------|------------|
| **Framework** | Next.js 16 App Router |
| **Language** | TypeScript (strict) |
| **UI** | Tailwind CSS, MUI/Radix |
| **State** | Redux Toolkit |
| **Auth** | NextAuth.js |

---

## Project Structure

```
rhixecompany-comics/
├── backend/                    # Django project
│   ├── config/                # Settings (base/local/production)
│   ├── apps/
│   │   ├── comics/           # Comic management
│   │   ├── scrapers/         # Scrapy/Selenium integration
│   │   ├── users/            # User management
│   │   └── tasks.py          # Celery tasks
│   ├── requirements/
│   │   ├── base.txt
│   │   ├── local.txt
│   │   └── production.txt
│   └── manage.py
├── frontend/                   # Next.js project
│   ├── src/
│   │   ├── app/              # App Router pages
│   │   ├── components/       # React components
│   │   ├── lib/              # Utilities
│   │   └── store/            # Redux store
│   ├── package.json
│   └── next.config.js
├── docker-compose.yml
└── README.md
```

---

## Commands

```bash
# Backend
cd backend
python -m venv .venv && source .venv/bin/activate
pip install -r requirements/local.txt
python manage.py migrate
python manage.py runserver

# Celery
celery -A config worker -l info

# Frontend
cd frontend
npm install
npm run dev
npm run build
npm test
```

---

## Key Features

| Feature | Implementation |
|---------|----------------|
| **Comic Management** | Django models + DRF serializers + Next.js UI |
| **Scraping** | Scrapy spiders + Selenium utils + Celery tasks |
| **Real-time** | WebSocket notifications (Redis) |
| **Auth** | JWT (backend) + NextAuth (frontend) |
| **Shared DB** | PostgreSQL with Django ORM + Prisma (frontend) |

---

## Consolidation Target (P1)

Receives scraping logic from:
- `Django-Scrapy-Selenium` — Scrapy spiders, Selenium utils, Celery tasks
- `selenium_webdriver` — Node.js Selenium scripts (rewrite in Python)
- `comicwise` — Feature overlap (comic reader)

---

## CI/CD

**Workflow:** `.github/workflows/rhixecompany-comics-ci.yml`  
**Jobs:** Backend (Python: ruff, mypy, pytest) + Frontend (TypeScript, ESLint, Next.js build)