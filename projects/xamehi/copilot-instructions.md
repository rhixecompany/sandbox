# xamehi — Dual-Backend + React

**Naming**: `snake_case` for Python files/variables/functions; `PascalCase` for Django models/classes; `camelCase` for JavaScript/Node.js variables/functions; `PascalCase` for React components; `UPPER_SNAKE_CASE` for constants; `kebab-case` for files/directories.

**Patterns**: Dual-backend architecture (Django + Express) with single React 18 frontend; Django REST Framework for primary API; Express (Node.js + Nodemon) for secondary services; React 18 with CRA (Create React App); Axios for API calls; CORS configuration between services.

**Structure**: Django project root (`xamehi/`); Express server (`index.js`/`server.js`); React frontend (CRA — `src/`, `public/`); Django apps for domain modules; separate route handlers for Express; environment variables shared.

**Python/Django**: Python 3.10+; Django + DRF; PEP 8 conventions; Django ORM for database; PostgreSQL; `manage.py` for administration; Gunicorn for production; settings in Django directory.

**Node/Express**: Node.js with Express; Nodemon for development auto-restart; route handlers for API endpoints; middleware for auth/logging/error handling; runs on port 5000.

**React/Frontend**: React 18 (modern hooks + functional components); CRA configuration; Axios HTTP client; separate build step (`npm run build`); runs on port 3000 (dev proxy).

**API Ports**: Express on port 5000; Django on port 8000; React on port 3000 (dev with proxy); CORS configured for cross-service communication.

**Security**: No `.env` or `SECRET_KEY` in VCS; Django `SECRET_KEY` in environment; CORS restricted in production; HTTPS required; JWT or session-based auth.

**Env**: `SECRET_KEY` (Django), `DATABASE_URL`, `PORT` (Express), `REACT_APP_API_URL`, `NODE_ENV`.

**Commands**: `npm install && npm start` (React dev); `npm run server` (Express via nodemon); `python manage.py migrate && python manage.py runserver` (Django); `python manage.py createsuperuser` (admin); `npm test` (React tests); `python manage.py test` (Django tests); `npm run build && python manage.py collectstatic && gunicorn xamehi.wsgi:application --bind 0.0.0.0:8000 && NODE_ENV=production node index.js` (production).
