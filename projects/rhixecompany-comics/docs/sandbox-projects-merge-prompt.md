# Merge Execution Prompt: rhixecompany-comics

> Run this to complete remaining consolidation tasks.

## Quick Start

```bash
# 1. Install backend deps
cd backend && python -m venv .venv && source .venv/bin/activate && pip install -r requirements.txt && cd ..

# 2. Install frontend deps
cd frontend && npm install && cd ..

# 3. Build & verify
cd frontend && npm run build && cd ..
cd backend && python manage.py check --deploy && cd ..

# 4. Initialize git remote (example)
git remote add origin https://github.com/rhixecompany/rhixecompany-comics.git
git push -u origin development
git push -u origin production

# 5. Set default branch in GitHub Settings to production
```

## Docker Stack

```bash
docker compose up -d          # Start all services
docker compose logs -f        # Follow logs
docker compose down           # Stop all
docker compose build --no-cache  # Rebuild
```

## CI Pipeline

The `.github/workflows/test.yml` runs on push to `development`/`production`:
- `backend-lint` — ruff check + format
- `backend-test` — Django test suite (Postgres service)
- `frontend-lint` — ESLint + TypeScript typecheck
- `frontend-test` — Vitest

## Verification Checklist

- [ ] `python manage.py check --deploy` passes
- [ ] `python manage.py test` passes
- [ ] `cd frontend && npm run typecheck` passes
- [ ] `cd frontend && npm run lint` passes
- [ ] `docker compose build` completes
- [ ] `production` branch at scaffold commit `32a7f8d`
- [ ] `development` branch at consolidation commit `42a77c5`
- [ ] Only `development` and `production` branches exist
- [ ] Remote origin configured
- [ ] No comicwise-specific workflows in `.github/workflows/`
