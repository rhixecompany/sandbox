# RhixeCompany Comics — Dual-Stack Comics Platform

> **Stack:** Django 4.x + Next.js 16 + Celery | **Type:** Dual-Stack Web Application | **Status:** Active

A dual-stack comic platform combining a Django REST Framework backend (API, admin, async tasks) with a Next.js 16 frontend (modern App Router, TypeScript). Uses Celery + Redis for asynchronous task processing.

---

## Technology Stack

### Backend (Django)

| Category | Technology |
|---|---|
| **Web Framework** | Django 4.x |
| **API Framework** | Django REST Framework (DRF) |
| **Language** | Python ^3.10+ |
| **Async Tasks** | Celery + Redis |
| **Database** | PostgreSQL |
| **Serving** | Gunicorn |
| **Dev Tools** | pytest, Black, ruff, mypy, pre-commit |

### Frontend (Next.js)

| Category | Technology |
|---|---|
| **Framework** | Next.js ^16.0.0 (App Router) |
| **UI** | React ^19.0.0 |
| **Styling** | Tailwind CSS ^4.0.0 |
| **Components** | Radix UI (accordion, dialog, dropdown, tabs, tooltip) |
| **Utilities** | clsx, tailwind-merge, class-variance-authority, lucide-react |
| **Testing** | Vitest |

## Architecture

```
┌──────────────────────────────────────────────────────────┐
│           rhixecompany-comics (Dual-Stack)               │
├──────────────────────────┬───────────────────────────────┤
│   Backend (Django 4.x)   │   Frontend (Next.js 16)       │
│                          │                               │
│   Django REST Framework  │   React 19 + TypeScript       │
│   Celery + Redis         │   Tailwind CSS 4              │
│   PostgreSQL             │   Radix UI primitives          │
│   Gunicorn               │   App Router / Server Comp.   │
│                          │                               │
│   API: /api/             │   API: /api/                  │
│   Tasks: tasks.py        │   Build: next build           │
├──────────────────────────┴───────────────────────────────┤
│  Shared Infrastructure                                    │
│  ├── PostgreSQL Database                                  │
│  ├── Redis (Celery broker)                               │
│  ├── Docker Compose                                      │
│  └── Shared environment variables                        │
└──────────────────────────────────────────────────────────┘
```

## Project Structure

```
rhixecompany-comics/
├── backend/                   # Django backend
│   ├── config/                # Django settings
│   │   ├── settings/
│   │   ├── urls.py
│   │   ├── wsgi.py
│   │   └── celery.py          # Celery configuration
│   ├── apps/                  # Django applications
│   │   ├── comics/            # Comic management
│   │   ├── users/             # User management
│   │   └── api/               # REST API endpoints
│   ├── tasks.py               # Celery task definitions
│   ├── requirements.txt
│   └── manage.py
├── frontend/                  # Next.js frontend
│   ├── src/
│   │   ├── app/               # App Router pages
│   │   ├── components/        # React components
│   │   └── lib/               # Utilities
│   ├── package.json
│   └── next.config.ts
├── scripts/scraper/           # Scrapy scraper scripts
├── docker-compose.yml
└── docs/Project_Architecture/
```

## Getting Started

### Backend

```bash
cd backend
pip install -r requirements.txt
python manage.py migrate
python manage.py runserver
python manage.py test

# Start Celery worker
celery -A config worker -l info
```

### Frontend

```bash
cd frontend
npm install
npm run dev
npm test
```

### Docker

```bash
docker compose up -d
```

## Key Features

- **Dual-Stack Architecture** — Django REST API backend + Next.js frontend
- **Async Task Processing** — Celery with Redis for background jobs
- **Comic Management** — Full CRUD for comic catalog
- **User Management** — Authentication and profiles
- **REST API** — Consistent `/api/` endpoints on both stacks
- **Docker Compose** — Unified development environment
- **Scheduled Tasks** — Celery Beat for periodic operations
- **Scraper Scripts** — Scrapy-based content gathering

## Coding Standards

### Backend
- **PEP 8**: Python style guide
- **Type hints**: Modern Python typing
- **Django best practices**: Standard patterns
- **Celery tasks**: Defined in `tasks.py`
- **Ownership boundaries**: `core` (health/shared), `comics` (catalog/chapters), `users` (auth/profile), `scraping` (Scrapy/Selenium), `api` (routing)

### Frontend
- **Server Components by default**: Next.js App Router pattern
- **TypeScript strict**: Full type safety
- **API**: `/api/` endpoints on both stacks
- **Metadata-driven**: SEO-friendly pages

## Environment Variables

- Shared env vars across both stacks
- Never hardcode secrets or host values
- Redis URL required for Celery

## API Communication

- Backend serves REST API at `/api/` via DRF
- Frontend consumes backend API directly
- Shared environment variables across stacks

## License

Not specified.
