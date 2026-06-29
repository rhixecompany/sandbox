# GitHub Copilot Instructions — rhixecompany-comics

## Priority Guidelines

When generating code for this repository:

1. **Version Compatibility**: Always detect and respect the exact versions of languages, frameworks, and libraries used in this project
2. **Context Files**: Prioritize patterns and standards defined in the .github/copilot directory
3. **Codebase Patterns**: When context files don't provide specific guidance, scan the codebase for established patterns
4. **Architectural Consistency**: Maintain our **Dual-stack (Django backend + Next.js frontend)** architectural style and established boundaries
5. **Code Quality**: Prioritize **maintainability, performance, and testability** in all generated code

## Technology Version Detection

Before generating code, scan the codebase to identify:

1. **Language Versions**: Detect the exact versions of programming languages in use
   - **Python** — check `runtime.txt` and `backend/requirements.txt`
   - **TypeScript** — check `frontend/package.json` and `tsconfig.json`

2. **Framework Versions**: Identify the exact versions of all frameworks
   - **Django 4.x** with Django REST Framework — check `backend/`
   - **Next.js 16** with App Router — check `frontend/`
   - **Celery** for async task processing
   - **Redis** as message broker and result backend

3. **Library Versions**: Note the exact versions of key libraries and dependencies
   - **PostgreSQL** (shared database between stacks)
   - **Django REST Framework** for backend API
   - **Tailwind CSS** for frontend styling
   - **Docker Compose** for infrastructure

## Context Files

Prioritize the following files in .github/copilot directory (if they exist):

- **architecture.md**: System architecture guidelines
- **tech-stack.md**: Technology versions and framework details
- **folder-structure.md**: Project organization guidelines
- **exemplars.md**: Exemplary code patterns to follow

## Codebase Scanning Instructions

When context files don't provide specific guidance:

1. Identify similar files to the one being modified or created
2. Analyze patterns for:
   - **Backend (Django)**: PEP 8, type hints, Django REST Framework ViewSets + Serializers
   - **Frontend (Next.js)**: Server Components by default, Client Components only when needed
   - **API endpoints**: `/api/` on both stacks
   - **Async tasks**: Celery tasks in `tasks.py` per Django app
   - **Shared state**: Environment variables shared across stacks via Docker Compose
   - **Database**: Shared PostgreSQL between both stacks
3. Follow the most consistent patterns found in the codebase
4. When conflicting patterns exist, prioritize patterns in newer files or files with higher test coverage
5. Never introduce patterns not found in the existing codebase

## Code Quality Standards

- Write self-documenting code with clear naming
- Follow PEP 8 for Python, TypeScript strict mode for frontend
- Use type hints in Python code
- Follow Django REST Framework best practices

## Documentation Requirements

- Follow the exact documentation format found in the codebase
- Match the style and completeness of existing comments
- Document parameters, returns, and exceptions in the same style

## Testing Approach

- Match the exact structure and style of existing tests
- **Django tests**: `python manage.py test`
- **Frontend tests**: `npm test`
- Follow existing patterns for test organization

## Technology-Specific Guidelines

### Python/Django (Backend)
- Django 4.x with Django REST Framework conventions
- ViewSets + Serializers for API endpoints
- Celery tasks in `tasks.py` per Django app
- PEP 8, type hints

### Next.js 16 (Frontend)
- App Router conventions
- Server Components by default
- API routes under `src/app/api/`

### Async Processing
- Celery + Redis for task queue
- Tasks defined in `tasks.py` per Django app
- Celery beat for scheduled scraping tasks

## Version Control Guidelines

- Follow Semantic Versioning patterns as applied in the codebase
- Match existing patterns for documenting breaking changes

## General Best Practices

- Follow naming conventions exactly as they appear in existing code
- Match code organization patterns from similar files
- Apply error handling consistent with existing patterns
- Never commit `.env` files — managed via Docker Compose
- Redis required for Celery broker and result backend

## Project-Specific Guidance

- Scan the codebase thoroughly before generating any code
- Respect existing architectural boundaries without exception
- Comic publishing platform with two independent stacks sharing a PostgreSQL database
- Scraping functionality consolidated from `projects/Django-Scrapy-Selenium`
- Celery beat for scheduled scraping tasks
- Two separate dev servers: Django (`:8000`), Next.js (`:3000`)
- Docker Compose for orchestration
