# rhixecompany-comics

Consolidated comics platform combining a Django backend with a Next.js 16 frontend.

## What lives here

- `backend/` — Django + DRF + Celery scaffold
- `frontend/` — Next.js 16 App Router scaffold
- `docs/project-docs/rhixecompany-comics/` — generated project documentation
- `RESEARCH_REPORT.md` — architecture and inheritance notes

## Quick Start

```bash
cd backend
python -m venv .venv
. .venv/bin/activate  # or .venv/Scripts/activate on Windows
pip install -r requirements.txt
python manage.py runserver
```

```bash
cd frontend
npm install
npm run dev
```

## Validation

```bash
cd backend
python -m compileall .
python manage.py check
```

```bash
cd frontend
npm run typecheck
npm run build
```

## Documentation

- [Technology Stack](technology-stack.md)
- [Folder Structure](folder-structure.md)
- [Architecture](architecture.md)
- [Project Workflow](project-workflow.md)
- [Code Exemplars](code-exemplars.md)
- [Copilot Instructions](copilot-instructions.md)
- [Cross-Linking Report](cross-linking-report.md)
- [Validation Report](validation-report.md)
- [Execution Summary](execution-summary.md)
