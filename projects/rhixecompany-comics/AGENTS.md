# RhixeCompany Comics — Dual-Stack Platform
## Architecture

- **Blueprint**: [rhixecompany-comics Architecture](../docs/Project_Architecture/rhixecompany_comics_architecture.md)
- **Folders**: [rhixecompany-comics Folder Structure](../docs/Project_Architecture/rhixecompany_comics_folders.md)
- **Tech Stack**: [rhixecompany-comics Technology Stack](../docs/Project_Architecture/rhixecompany_comics_techstack.md)
- **Stack Type**: Dual-stack (Django + Next.js)


Django + Next.js 16 + Celery.

## Stack
- Backend: Django 4.x + DRF
- Frontend: Next.js 16 App Router + TypeScript strict
- Async: Celery + Redis
- Database: PostgreSQL
- Deploy: Docker Compose

## Conventions
- Backend: PEP 8, type hints, Django best practices
- Frontend: Server Components by default
- API at `/api/` on both stacks
- Celery tasks in `tasks.py`

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

## Notes
- Redis required for Celery
- Shared env vars across stacks
- Celery beat for scheduled tasks
