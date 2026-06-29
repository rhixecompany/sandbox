# xamehi.tv — Django + React Streaming

## Architecture
- **Type:** Django REST + React streaming platform
- **Pattern:** DRF backend + React 17 frontend (Material-UI, Redux)
- **Reference:** [Workflow Analysis](docs/Project_Architecture/Workflow_Analysis.md), [Exemplars](docs/Project_Architecture/exemplars.md)

Django REST Framework + React 17 (Material-UI, Redux). Video streaming platform with PayPal payments, JWT auth, and allauth social login.

## Stack
- **Backend:** Django + DRF, SimpleJWT, django-allauth
- **Frontend:** React 17, Redux, Material-UI 4
- **Database:** PostgreSQL (prod), SQLite (dev)
- **Payments:** PayPal
- **Media:** video-react
- **Infra:** Gunicorn + WhiteNoise

## Commands
```bash
# Backend
python -m venv myenv && source myenv/bin/activate
pip install -r requirements.txt
python manage.py migrate && python manage.py runserver

# Frontend
cd frontend && npm install && npm start

# Tests
python manage.py test
cd frontend && npm test
```

## Conventions
- Backend on `127.0.0.1:8000`, frontend on `localhost:3000` (proxied)
- CORS via django-cors-headers — CORS + proxy troubleshooting common
- `.env` — never commit
- JWT authentication via SimpleJWT
- Social login via django-allauth

## Notes
- React 17 (CRA-based), not latest — upgrade consideration
- PayPal integration for payments
- Material-UI 4 for component library
- video-react for video player component
