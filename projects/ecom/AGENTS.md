# Ecom — Django + React Ecommerce

Django REST Framework + React/Redux + PayPal.

## Stack
- Backend: DRF, Python 3.10+
- Frontend: React + Redux Toolkit
- Database: PostgreSQL
- Payments: PayPal
- Deploy: Docker Compose

## Commands
```bash
# Backend
cd backend
pip install -r requirements.txt
python manage.py migrate && python manage.py makemigrations
python manage.py runserver
python manage.py test

# Frontend
cd frontend
npm install
npm start
npm test
```

## Notes
- `.env` — never commit
- API at `/api/v1/`
- Tests: `tests/` (backend), `__tests__/` (frontend)
- Separate settings per env
