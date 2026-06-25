# RhixeCompany Comics — Dual-Stack Platform

**Naming**: `snake_case` for Python/Django files; `PascalCase` for Django classes/models; `PascalCase` for React components; `camelCase` for TypeScript hooks/utils; `kebab-case` for Next.js routes and directories; `snake_case` for database tables.

**Patterns**: Dual-stack architecture with Django REST backend + Next.js 16 frontend; API at `/api/` on both stacks; Celery + Redis for async task processing; Celery Beat for scheduled tasks; Django ORM for data access; Next.js Server Components by default; shared environment variables across stacks.

**Structure**: `backend/` (Django 4.x + DRF); `frontend/` (Next.js 16 App Router); Celery tasks in `tasks.py` within each Django app; shared `.env` at project root; Docker Compose for orchestration.

**Python/Django**: Python 3.10+; Django 4.x + DRF; PEP 8 with type hints; Django best practices (models, views, serializers, admin); Celery tasks for async processing.

**TypeScript/Next.js**: Next.js 16 App Router; TypeScript strict mode; Server Components by default; `npm` for package management; React 18+.

**Database**: PostgreSQL (shared across stacks); Django ORM for backend; optional Prisma for frontend direct access (avoid unless needed).

**Async Tasks**: Celery with Redis broker; Celery Beat for scheduled/cron tasks; tasks defined in `tasks.py` per Django app; long-running tasks return progress via Celery result backend.

**Testing**: `python manage.py test` (Django); `npm test` (Next.js); separate test databases.

**Security**: No `.env` secrets in VCS; CORS configured between frontend and backend; Django DRF authentication for API; rate limiting on Celery tasks; sanitize all user inputs.

**Env**: `DATABASE_URL`, `SECRET_KEY`, `CELERY_BROKER_URL` (Redis), `NEXT_PUBLIC_API_URL`, CORS origins.

**Commands**: `cd backend && pip install -r requirements.txt && python manage.py migrate && python manage.py runserver` (backend); `cd frontend && npm install && npm run dev` (frontend); `celery -A config worker -l info` (worker); `python manage.py test` (backend test); `npm test` (frontend test); `docker compose up -d` (full stack).
