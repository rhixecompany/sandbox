# AGENTS.md

> **Refreshed by AGENTS workflow 2026-06-01**

## Project Overview

Xamehi — a full-stack web application with a dual-backend architecture combining Django (Python) with Express.js (Node.js) alongside a React frontend. Serves as a legacy RhixeCompany project.

**Tech Stack:**
- **Backend 1**: Python 3.10+, Django with Django REST Framework
- **Backend 2**: Node.js with Express.js, Nodemon dev server, CORS middleware
- **Frontend**: React 18 (Create React App), Axios HTTP client
- **Database**: PostgreSQL (via Django ORM)
- **Entry Points**: `index.js` (Express server), `manage.py` (Django CLI)

## Hermes and Copilot

- Use the nearest `AGENTS.md` for files under `projects/xamehi/`; this file is
  the local fallback.
- `projects/xamehi/.github/copilot-instructions.md` is the primary Copilot
  guidance file for this project.
- Root Hermes orchestration assets live in `../../.github/agents/hermes.agent.md`
  and `../../.github/prompts/`.
- Keep this file, the local Copilot instructions, and both backend docs aligned
  when the dual-stack workflows change.

## Setup Commands

```bash
# Install Node dependencies
npm install

# Install Python dependencies
pip install -r requirements.txt  # if present

# Copy environment variables
cp .env.example .env
# Edit .env with database config and secrets

# Run Django migrations
python manage.py migrate

# Start all services (in separate terminals)
# Terminal 1: Express backend
node index.js

# Terminal 2: Django backend
python manage.py runserver

# Terminal 3: React frontend
npm start
```

## Development Workflow

```bash
# React frontend with hot-reload
npm start

# Express backend with auto-restart
npm run server  # uses nodemon

# Django admin
python manage.py runserver

# Django management
python manage.py createsuperuser
```

## Testing Instructions

```bash
# React tests
npm test

# Django tests
python manage.py test
```

## Code Style

- **Python**: Django conventions, PEP 8, Django REST Framework patterns
- **JavaScript (React)**: ESLint with react-app presets, ES6 modules
- **JavaScript (Express)**: CommonJS (require), Express middleware pattern
- **API**: Axios for HTTP requests from frontend to Express/Django backends
- **CSS**: Standard CSS (index.css) — no CSS framework detected

## Build/Deployment

```bash
# React production build
npm run build

# Django production
python manage.py collectstatic
gunicorn xamehi.wsgi:application --bind 0.0.0.0:8000

# Express production
NODE_ENV=production node index.js
```

## Security

- Never commit `.env` files or credentials
- Django `SECRET_KEY` must be in environment variables, never in code
- Express CORS should be restricted in production (not wildcard)
- Django CSRF protection enabled by default
- Validate all API inputs on both backends
- Use HTTPS in production

## Troubleshooting

- **Port conflicts**: Express defaults to 5000, Django to 8000, React to 3000
- **CORS errors**: Check CORS configuration in Express and django-cors-headers in Django
- **Django migration issues**: `python manage.py migrate --run-syncdb`
- **Express not starting**: Check for errors in index.js, ensure Node.js 18+
- **Frontend can't reach backend**: Verify proxy or API URL configuration
