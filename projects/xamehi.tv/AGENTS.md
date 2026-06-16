# xamehi.tv — Django + React Streaming

Django REST + React 17 (Material-UI, Redux).

## Stack
- Django + DRF, SimpleJWT, django-allauth
- React 17, Redux, Material-UI 4
- PostgreSQL (prod); SQLite (dev)
- PayPal, video-react; deploy: Gunicorn + WhiteNoise

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

## Notes
- Backend `127.0.0.1:8000`, frontend `localhost:3000` proxied
- `.env` — never commit
- CORS via django-cors-headers
- CORS + proxy troubleshooting common
