# Technology Stack Blueprint

## Project: rhixecompany-comics — Dual-Stack Platform

> **Generated:** 2026-06-25  
> **Generator:** technology-stack-blueprint-generator  
> **Analysis Depth:** Comprehensive

---

## Overview

A dual-stack comic platform combining a Django REST Framework backend (API, admin, async tasks) with a Next.js 16 frontend (modern App Router, TypeScript). Uses Celery + Redis for asynchronous task processing.

**Project Type:** Full-Stack Web Application (Dual-Stack)  
**Stack Type:** Dual-stack (Django + Next.js)

---

## Technology Stack

### Languages & Runtimes

| Technology | Version | Usage |
|---|---|---|
| Python | ^3.10+ | Backend language |
| TypeScript | ^5 (strict) | Frontend language |
| React | ^19.0.0 | UI framework |
| Node.js | — | JavaScript runtime |
| HTML/CSS | — | Templates & styling |

### Backend Stack (Django)

| Category | Technologies |
|---|---|
| **Web Framework** | Django 4.x |
| **API Framework** | Django REST Framework |
| **Async Tasks** | Celery + Redis |
| **Database** | PostgreSQL |
| **Serving** | Gunicorn |
| **Deployment** | Docker Compose |

### Frontend Stack (Next.js)

| Category | Dependencies |
|---|---|
| **Framework** | next ^16.0.0 |
| **UI** | react ^19.0.0, react-dom ^19.0.0 |
| **Styling** | tailwindcss ^4.0.0 |
| **Components** | @radix-ui/* (accordion, dialog, dropdown-menu, tabs, tooltip) |
| **Utilities** | clsx, tailwind-merge, class-variance-authority, lucide-react |
| **Dev Tools** | @types/node, vitest, prettier, typescript |

### Backend Convention Tools

| Tool | Purpose |
|---|---|
| pytest | Testing |
| Black | Code formatting |
| ruff | Linting |
| mypy | Type checking |
| pre-commit | Git hooks |

---

## Licensing

| Component | License |
|---|---|
| rhixecompany-comics | (not specified) |

---

## Project Structure

```
rhixecompany-comics/
├── backend/               # Django application
│   ├── config/            # Django settings
│   ├── api/               # DRF views/serializers
│   ├── requirements.txt
│   └── manage.py
├── frontend/              # Next.js application
│   ├── src/               # Components, pages
│   ├── package.json
│   └── next.config.js
├── scripts/
│   └── scraper/           # Scrapy scraper scripts
├── docker-compose.yml
└── AGENTS.md
```

---

## Key Scripts

| Command | Description |
|---|---|
| `python manage.py runserver` | Django dev server |
| `python manage.py test` | Run Django tests |
| `celery -A config worker -l info` | Celery worker |
| `npm run dev` (frontend) | Next.js dev server |
| `npm test` (frontend) | Frontend tests |

---

## Coding Conventions

### Backend
- **PEP 8**: Python style
- **Type hints**: Modern Python typing
- **Django best practices**: Standard patterns
- **Celery tasks**: Defined in `tasks.py`

### Frontend
- **Server Components by default**: Next.js App Router pattern
- **TypeScript strict**: Full type safety
- **API**: `/api/` endpoints on both stacks

---

## Architecture Diagram

```
┌──────────────────────────────────────────────────────────┐
│           rhixecompany-comics (Dual-Stack)               │
├──────────────────────────┬───────────────────────────────┤
│   Backend (Django 4.x)   │   Frontend (Next.js 16)       │
│                          │                               │
│   Django REST Framework  │   React 19 + TypeScript       │
│   Celery + Redis         │   Tailwind CSS 4              │
│   PostgreSQL             │   Radix UI primitives          │
│   Gunicorn               │   App Router / Server Comp.   │
│                          │                               │
│   API: /api/             │   API: /api/                  │
│   Tasks: tasks.py        │   Build: next build           │
├──────────────────────────┴───────────────────────────────┤
│  Shared Infrastructure                                    │
│  ├── PostgreSQL Database                                  │
│  ├── Redis (Celery broker)                               │
│  ├── Docker Compose                                      │
│  └── Shared environment variables                        │
└──────────────────────────────────────────────────────────┘
```

---

## Notes

- Redis required for Celery
- Shared env vars across stacks
- Celery beat for scheduled tasks
- Scraper scripts in `scripts/scraper/`
