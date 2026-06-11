# AGENTS.md

> **Refreshed by AGENTS workflow 2026-06-01**

## Project Overview

Xamehi TV — a movie/television streaming website built with Django REST backend and React 17 frontend. Features movie reviews, ratings, carousels, pagination, search, and admin management.

**Tech Stack:**
- **Backend**: Python 3.x, Django, Django REST Framework, SimpleJWT auth
- **Frontend**: React 17, Redux, Material-UI 4, React Bootstrap 1, react-admin 4
- **Database**: PostgreSQL (production), SQLite (dev)
- **Payments**: PayPal (react-paypal-button-v2)
- **Media**: video-react player
- **Auth**: JWT with django-rest-framework-simplejwt, django-allauth
- **Deployment**: Gunicorn, WhiteNoise, Procfile

## Hermes and Copilot

- Use the nearest `AGENTS.md` for files under `projects/xamehi.tv/`; this file
  is the local fallback.
- `projects/xamehi.tv/.github/copilot-instructions.md` is the primary Copilot
  guidance file for this project.
- Root Hermes orchestration assets live in `../../.github/agents/hermes.agent.md`
  and `../../.github/prompts/`.
- Keep this file, the local Copilot instructions, and backend/frontend docs in
  sync when auth, media, or deployment workflows change.

## Setup Commands

```bash
# Backend
python -m venv myenv
source myenv/bin/activate  # On Windows: myenv\Scripts\activate
pip install -r requirements.txt
python manage.py migrate
python manage.py runserver

# Frontend (separate terminal)
cd frontend
npm install
npm start
```

Backend runs on http://127.0.0.1:8000, frontend on http://localhost:3000 (proxied to backend).

## Development Workflow

```bash
# Backend
python manage.py runserver
python manage.py createsuperuser

# Frontend
cd frontend && npm start

# Build frontend for production
cd frontend && npm run build
```

## Testing Instructions

```bash
# Django tests
python manage.py test

# Frontend tests
cd frontend && npm test
```

## Code Style

- **Python**: Django conventions, DRF ViewSets + Serializers, JWT permissions
- **JavaScript**: ESLint (react-app), Redux pattern (constants/actions/reducers)
- **React**: Class components and functional components (mixed), react-admin for admin panel
- **UI**: Material-UI 4 components + React Bootstrap
- **State**: Redux with Thunk middleware for async API calls
- **API**: Axios HTTP client proxied through React dev server

## Build/Deployment

```bash
# Collect static files
python manage.py collectstatic

# Production server
gunicorn player.wsgi:application --bind 0.0.0.0:8000

# Frontend build
cd frontend && npm run build
```

Deploy to Heroku (Procfile included), DigitalOcean, or any VPS with Gunicorn + Nginx.

## Security

- JWT authentication for API endpoints
- CORS configured via django-cors-headers
- Never commit SECRET_KEY or database credentials
- Use environment variables for all secrets
- CSRF protection enabled (Django default)
- Admin panel restricted to superusers

## Troubleshooting

- **Migration errors**: Delete `db.sqlite3` and re-run `python manage.py migrate`
- **Frontend not connecting to backend**: Check proxy in `frontend/package.json` (default: http://127.0.0.1:8000)
- **Material-UI styling issues**: Verify @material-ui/core version compatibility
- **Video player not working**: Check video-react configuration and source URLs
- **CORS issues**: Ensure CORS_ALLOWED_ORIGINS includes frontend URL
