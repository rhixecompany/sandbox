# Copilot Instructions

Project-wide guidance for Xamehi TV.

## Source of truth

- `projects/xamehi.tv/AGENTS.md`
- `README.md`
- `frontend/`
- Django backend files

## Commands

Run from the project root:

```bash
python -m venv myenv
source myenv/bin/activate
pip install -r requirements.txt
python manage.py migrate
python manage.py runserver
cd frontend && npm install
cd frontend && npm start
cd frontend && npm run build
python manage.py test
cd frontend && npm test
python manage.py collectstatic
gunicorn player.wsgi:application --bind 0.0.0.0:8000
```

## Architecture

- Django REST backend serves movie data, reviews, ratings, and admin flows.
- React frontend handles the user experience and proxies to backend services.
- PayPal and video-react are part of the user-facing feature set.

## Conventions

- Keep backend/frontend dependencies and port expectations aligned.
- Use Django serializers and JWT auth for API entry points.
- Prefer environment variables for secrets and third-party keys.
- Keep static/media handling compatible with WhiteNoise and deployment settings.

