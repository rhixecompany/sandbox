# Copilot Instructions

Project-wide guidance for Rhixecompany Comics.

## Source of truth

- `projects/rhixecompany-comics/AGENTS.md`
- `README.md`
- `backend/`
- `frontend/`

## Commands

Run from the project root:

```bash
cd backend && python -m venv .venv
cd backend && pip install -r requirements.txt
cd backend && python manage.py migrate
cd backend && python manage.py createsuperuser
cd backend && python manage.py runserver
cd frontend && bun install
cd frontend && bun run dev
docker compose up -d
cd backend && python manage.py test
cd frontend && bun run test
cd backend && ruff check .
cd frontend && bun run lint
cd backend && python manage.py check --deploy
cd frontend && bun run build
```

## Architecture

- Django backend and Next.js 16 frontend are separate surfaces in one product.
- Scrapy and Selenium are inherited scraping/automation layers.
- Docker Compose wires Django, PostgreSQL, Redis, Celery, and Next.js together.

## Conventions

- Keep backend/frontend/scraping changes separated when possible.
- Use Django ORM, migrations, and DRF conventions on the backend.
- Keep TypeScript and App Router code aligned with the inherited ComicWise patterns.
- Respect robots.txt and scraping rate limits.
