# RhixeCompany Comics - Dual-Stack Comic Platform Context

Django + Next.js 16 comic platform with Celery for async tasks.

## Architecture
- **Backend**: Django 4.x + Django REST Framework
- **Frontend**: Next.js 16 (App Router)
- **Async**: Celery + Redis
- **Database**: PostgreSQL
- **Deployment**: Docker Compose

## Conventions
- **Backend**: PEP 8, type hints, Django best practices
- **Frontend**: TypeScript strict, Next.js App Router
- API at `/api/` (Django) and `/api/` (Next.js API routes)
- Celery tasks in `tasks.py`
- Shared types between Django/Next.js

## Commands
```bash
# Backend
cd backend
pip install -r requirements.txt
python manage.py runserver

# Celery Worker
celery -A config worker -l info

# Frontend
cd frontend
npm install
npm run dev

# Database
python manage.py migrate

# Tests
python manage.py test
npm test
```

## Important Notes
- Redis required for Celery
- Shared environment variables
- Celery beat for scheduled tasks