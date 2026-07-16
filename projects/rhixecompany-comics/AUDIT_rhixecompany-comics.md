# AUDIT — rhixecompany-comics

Read-only repo-management audit (Phases 0, 2, 3). Destructive phases HELD.

## Overview
Full-stack comic platform: Django REST `backend/` (DRF, Celery, Redis, Scrapy, Selenium, SimpleJWT, drf-spectacular) + Next.js 16 / React 19 / Tailwind 4 `frontend/`. Docker-compose orchestrated. Rich docs (architecture.md, technology-stack.md, folder-structure.md, project-workflow.md). Has `.env.example`, `.logs/`.

## Disk Usage
62M (excluding .git/node_modules/venv/caches/build). Largest of the five — frontend assets + backend.

## Entrypoint
- Backend: `backend/manage.py` (Django), `backend/config/`, `backend/apps/`, `docker-compose.yml`.
- Frontend: `frontend/package.json` → `next dev` / `next build` / `next start`.

## Gitignore Audit
`.gitignore` present (concise, hand-written).
Covered: node_modules (`frontend/node_modules/`), .env (`backend/.env`, `frontend/.env.local`), *.pyc, __pycache__/, .next/ (`frontend/.next/`), db.sqlite3, media/, staticfiles/, .DS_Store.
MISSING:
- **`dist/`** — not listed.
- **`build/`** — not listed.
- **`venv/` / `.venv/`** — only `backend/.venv/` covered; a root-level or differently-named venv would not be ignored. Flag: narrow venv rule.
- `node_modules/` covered only under `frontend/` — a root/other-location node_modules would leak.
- NOTE: committed `.logs/` directory exists and is not in .gitignore (logs tracked).

## Dependency Audit
- **Backend Python:** `backend/requirements.txt`, well-pinned with ranges (Django 5.0–5.2, DRF 3.15+, celery 5.3+, redis 5.0+, scrapy 2.11+, selenium 4.20+, psycopg2-binary, gunicorn 22+, Pillow 10.x, whitenoise, simplejwt, drf-spectacular). `pip` available; `pip-audit` NOT installed (scan not run).
- **Frontend Node:** `frontend/package.json` + `frontend/bun.lock` AND `frontend/package-lock.json` (two lockfiles present — bun.lock + npm lock → flag: mixed package managers, pick one). Next 16 / React 19 / Tailwind 4 (bleeding-edge). `bun` 1.3.14 available; `bun audit` NOT run (read-only).

## Branch State
`git branch`: `* development`, `production`. No `master`/`main`/stray branches. Current = development.

## Destructive Phases HELD
- Phase 1 (branch deletion / push): NOT run.
- Phase 4 (CI creation): NOT run.
- Deferred: add `dist/`, `build/`, broaden `venv/`; ignore `.logs/`; resolve dual lockfiles (bun vs npm).
