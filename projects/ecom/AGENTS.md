# Ecom — Django + React Ecommerce
## Architecture

- **Blueprint**: [ecom Architecture](../docs/Project_Architecture/ecom_architecture.md)
- **Folders**: [ecom Folder Structure](../docs/Project_Architecture/ecom_folders.md)
- **Tech Stack**: [ecom Technology Stack](../docs/Project_Architecture/ecom_techstack.md)
- **Stack Type**: Dual-stack (Django + React)


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
