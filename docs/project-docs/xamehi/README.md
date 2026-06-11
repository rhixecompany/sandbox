# xamehi — Dual-Backend Web Application

A full-stack web application with dual-backend architecture: Django + Express.js + React frontend.

## Tech Stack
- **Backend 1**: Django (Python), DRF, PostgreSQL
- **Backend 2**: Express.js (Node.js)
- **Frontend**: React 18 (Create React App), Axios

## Quick Start
```bash
npm install
pip install -r requirements.txt
cp .env.example .env
python manage.py migrate
# Start 3 terminals:
node index.js           # Express :5000
python manage.py runserver  # Django :8000
npm start               # React :3000
```

## Documentation
- [Technology Stack](technology-stack.md)
- [Architecture](architecture.md)
- [Code Exemplars](code-exemplars.md)
