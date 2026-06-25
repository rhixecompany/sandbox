# RhixeCompany Comics — Dual-Stack Platform

## Architecture
- **Type:** Dual-stack web platform (Django backend + Next.js frontend)
- **Pattern:** Two independent stacks sharing a PostgreSQL database, with Celery for async tasks
- **Reference:** [Workflow Analysis](docs/Project_Architecture/Workflow_Analysis.md), [Exemplars](docs/Project_Architecture/exemplars.md)

Django 4.x + DRF (backend API) + Next.js 16 App Router (frontend) + Celery + Redis. Scraping and comics management platform with separate frontend and backend services.

## Stack
- **Backend:** Django 4.x + Django REST Framework, Python 3.10+
- **Frontend:** Next.js 16 App Router, TypeScript (strict)
- **Async:** Celery + Redis
- **Database:** PostgreSQL (shared)
- **Infra:** Docker Compose

## Commands
```bash
# Backend
cd backend
pip install -r requirements.txt
python manage.py migrate
python manage.py runserver
python manage.py test

# Celery
celery -A config worker -l info

# Frontend
cd frontend
npm install
npm run dev
npm test
```

## Conventions
- Backend: PEP 8, type hints, Django best practices
- Frontend: Server Components by default; Client Components only when needed
- API at `/api/` on both stacks
- Celery tasks in `tasks.py` per Django app
- Shared env vars across stacks via Docker Compose
- Redis required for Celery broker and result backend

## Notes
- Scraping functionality consolidated from `projects/Django-Scrapy-Selenium`
- Celery beat for scheduled scraping tasks
- `.env` — never commit; shared across both stacks
- Two separate dev servers: Django (`:8000`), Next.js (`:3000`)
