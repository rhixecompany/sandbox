<<<<<<< HEAD
# AGENTS.md

> **Refreshed by AGENTS workflow 2026-06-01**

## Project Overview

RhixeCompany Ecommerce — a full-stack ecommerce platform with shopping cart, product reviews, PayPal integration, and admin dashboard. Built with Django REST backend and React/Redux frontend.

**Tech Stack:**
- **Backend**: Python 3.10, Django 3.1, Django REST Framework (DRF), SimpleJWT auth
- **Frontend**: React 18, Redux (with Thunk), React Bootstrap, React Router v5
- **Database**: SQLite (dev), PostgreSQL (production via django-storages)
- **Storage**: AWS S3 / Google Cloud Storage
- **Payments**: PayPal (react-paypal-button-v2)
- **Deployment**: Gunicorn, WhiteNoise, Procfile (Heroku-ready)

## Setup Commands

```bash
# Backend
python -m venv env
source env/bin/activate  # On Windows: env\Scripts\activate
pip install -r requirements.txt
python manage.py migrate
python manage.py runserver

# Frontend (separate terminal)
cd frontend
npm install
npm start
```

The backend runs on http://127.0.0.1:9000 and frontend on http://localhost:3000 (proxied).

## Development Workflow

```bash
# Backend
python manage.py runserver
python manage.py createsuperuser  # Admin panel at /admin

# Frontend
cd frontend && npm start

# Seed product data
python manage.py runscript  # or use admin panel
```

## Testing Instructions

```bash
# Django tests
python manage.py test

# Frontend tests
cd frontend && npm test
```

## Code Style

- **Python**: Django conventions, PEP 8, autopep8 for formatting
- **JavaScript**: ESLint (react-app presets), React class/functional components mixed
- **Redux**: Action constants, action creators, reducers pattern (screens/components/actions/reducers/constants)
- **API**: DRF ViewSets + Serializers with JWT authentication
- **CSS**: Bootstrap 5 with react-bootstrap components

## Build/Deployment

```bash
# Backend production
python manage.py collectstatic
gunicorn ecom.wsgi:application --bind 0.0.0.0:9000

# Frontend production
cd frontend && npm run build
# Served via Django or deployed separately
```

Deployment options: Heroku (Procfile included), DigitalOcean, or any Linux VPS with Gunicorn + Nginx.

## Security

- JWT tokens for API authentication (djangorestframework-simplejwt)
- CORS configured via django-cors-headers
- Never commit `SECRET_KEY` or database credentials
- Use environment variables for sensitive config
- Django admin protected by authentication
- Input sanitization via DRF serializers

## Troubleshooting

- **Migration errors**: Delete `db.sqlite3` and re-run `python manage.py migrate`
- **Frontend API calls failing**: Check the proxy setting in `frontend/package.json` points to correct backend URL
- **PayPal not loading**: Ensure PayPal client ID is in environment variables
- **Static files broken**: Run `python manage.py collectstatic` and verify `STATIC_ROOT`
- **CORS errors**: Check `CORS_ALLOWED_ORIGINS` in Django settings
=======
# Ecom - Full-Stack Ecommerce Platform Context

Django REST Framework + React/Redux ecommerce with PayPal.

## Architecture
- **Backend**: Django REST Framework (Python)
- **Frontend**: React + Redux
- **Database**: PostgreSQL
- **Payments**: PayPal
- **Deployment**: Docker Compose

## Conventions
- **Backend**: PEP 8, type hints, Django best practices
- **Frontend**: Redux Toolkit, functional components
- API endpoints at `/api/v1/`
- Tests in `tests/` (backend) and `__tests__/` (frontend)

## Commands
```bash
# Backend
cd backend
pip install -r requirements.txt
python manage.py runserver

# Frontend
cd frontend
npm install
npm start

# Database
python manage.py migrate
python manage.py makemigrations

# Tests
python manage.py test
npm test
```

## Important Notes
- PayPal credentials in `.env` — never commit
- Separate settings for dev/staging/prod
- Media files served via Django in dev
>>>>>>> d330f24 (chore: initial local project setup for ecom)
