# Project Workflow — rhixecompany-comics

## Local Setup

### Backend

```bash
cd backend
python -m venv .venv
. .venv/bin/activate  # or .venv/Scripts/activate on Windows
pip install -r requirements.txt
cp .env.example .env
python manage.py migrate
python manage.py runserver
```

### Frontend

```bash
cd frontend
npm install
npm run dev
```

## Validation

### Backend

```bash
cd backend
python -m compileall .
python manage.py check
```

### Frontend

```bash
cd frontend
npm run typecheck
npm run build
```

## Development Notes

- Keep backend settings env-driven.
- Keep frontend metadata in the root layout.
- Prefer explicit health checks and small app boundaries.
- Use the source repositories as read-only references until a future feature migration lands.
