# xamehi.tv — Django + React Streaming

**Naming**: `snake_case` for Python files/variables/functions; `PascalCase` for Django models/classes; `PascalCase` for React components; `camelCase` for JS variables/functions; `UPPER_SNAKE_CASE` for constants/settings; `kebab-case` for files/directories.

**Patterns**: Django REST Framework with SimpleJWT auth; React 17 class components + hooks; Redux for state management; Material-UI 4 for component library; video-react for media player; PayPal payment integration; CORS configured via django-cors-headers; backend `127.0.0.1:8000` proxied to frontend `localhost:3000`.

**Structure**: Django project with DRF API; `frontend/` directory with React app; separate requirements for Python; `package.json` for frontend; settings split by environment.

**Python/Django**: Python 3.10+; Django + DRF; SimpleJWT for token auth; django-allauth for social auth; PostgreSQL (production); SQLite (development); Gunicorn + WhiteNoise for production serving.

**React/Frontend**: React 17 (class components + hooks); Redux for global state; Material-UI 4 (MUI) for UI components; video-react for video playback; PayPal Smart Buttons for payments; Axios for API calls.

**API**: Django REST Framework; SimpleJWT authentication (access + refresh tokens); CORS via django-cors-headers; PayPal order creation/capture endpoints; video streaming endpoints.

**Security**: No `.env` in VCS; DRF serializer validation; SimpleJWT token expiry; CORS restricted in production; PayPal credentials server-side only; HTTPS required in production.

**Env**: `SECRET_KEY`, `DATABASE_URL`, `JWT_SECRET`, `PAYPAL_CLIENT_ID`, `PAYPAL_CLIENT_SECRET`, `CORS_ORIGINS`.

**Commands**: `python -m venv myenv && source myenv/bin/activate && pip install -r requirements.txt && python manage.py migrate && python manage.py runserver` (backend); `cd frontend && npm install && npm start` (frontend); `python manage.py test` (backend tests); `cd frontend && npm test` (frontend tests).
