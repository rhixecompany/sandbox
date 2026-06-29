# xamehi — Dual-Backend + React

## Architecture
- **Type:** Legacy dual-backend app (Django + Express) + React frontend
- **Pattern:** Three separate services: Django DRF API, Express server, React 18 CRA frontend
- **Reference:** [Workflow Analysis](docs/Project_Architecture/Workflow_Analysis.md), [Exemplars](docs/Project_Architecture/exemplars.md)

Django + DRF (Python 3.10+) + Express (Node.js) + React 18 (CRA). Legacy application with two backend services and a React frontend, sharing a PostgreSQL database.

## Stack
- **Backend 1:** Django + DRF (Python 3.10+)
- **Backend 2:** Express (Node.js, Nodemon for dev)
- **Frontend:** React 18 (Create React App), Axios
- **Database:** PostgreSQL

## Commands
```bash
npm install
npm start               # React
npm run server          # Express (nodemon)
python manage.py migrate && python manage.py runserver
python manage.py createsuperuser
npm test                # React
python manage.py test   # Django
```

## Build
```bash
npm run build
python manage.py collectstatic
gunicorn xamehi.wsgi:application --bind 0.0.0.0:8000
NODE_ENV=production node index.js
```

## Conventions
- Ports: Express `:5000`, Django `:8000`, React `:3000`
- CORS configured across all services
- `.env` — never commit; Django `SECRET_KEY` in environment
- Production requires HTTPS and proper CORS setup
- React CRA-based — consider migration to Vite/Next.js

## Notes
- Legacy architecture with dual backends — consolidation opportunity
- Express handles supplementary API endpoints
- React 18 with CRA (no Server Components)
- Three separate build/deploy steps for production
