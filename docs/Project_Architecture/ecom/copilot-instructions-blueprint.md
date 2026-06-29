# GitHub Copilot Instructions — ecom

## Priority Guidelines

When generating code for this repository:

1. **Version Compatibility**: Always detect and respect the exact versions of languages, frameworks, and libraries used in this project
2. **Context Files**: Prioritize patterns and standards defined in the .github/copilot directory
3. **Codebase Patterns**: When context files don't provide specific guidance, scan the codebase for established patterns
4. **Architectural Consistency**: Maintain our **Monolithic (Django + React SPA)** architectural style and established boundaries
5. **Code Quality**: Prioritize **maintainability, security, and testability** in all generated code

## Technology Version Detection

Before generating code, scan the codebase to identify:

1. **Language Versions**: Detect the exact versions of programming languages in use
   - **Python** — check `runtime.txt` and `requirements.txt`
   - **JavaScript** — check `frontend/package.json`

2. **Framework Versions**: Identify the exact versions of all frameworks
   - **Django 3.1** — check `requirements.txt` (`django==3.1.14`)
   - **Django REST Framework 3.13** — check `requirements.txt`
   - **React 18** — check `frontend/package.json`
   - **Redux** with Thunk middleware
   - **React Bootstrap** — check frontend dependencies

3. **Library Versions**: Note the exact versions of key libraries and dependencies
   - **SimpleJWT** for authentication (`djangorestframework-simplejwt==5.2.0`)
   - **PayPal** integration (`react-paypal-button-v2`)
   - **SQLite** (dev), PostgreSQL (production with django-storages)
   - **AWS S3 / Google Cloud Storage** for media
   - **Gunicorn** for production WSGI
   - **django-cors-headers** for CORS
   - **django-filter** for API filtering

## Context Files

Prioritize the following files in .github/copilot directory (if they exist):

- **architecture.md**: System architecture guidelines
- **tech-stack.md**: Technology versions and framework details
- **folder-structure.md**: Project organization guidelines

## Codebase Scanning Instructions

When context files don't provide specific guidance:

1. Identify similar files to the one being modified or created
2. Analyze patterns for:
   - **Backend**: DRF ViewSets + Serializers with JWT authentication
   - **Frontend**: Redux pattern (constants/actions/reducers/components)
   - **Naming**: snake_case for Python, camelCase for JavaScript
   - **API**: RESTful endpoints at `/api/` with JWT auth
   - **State management**: Redux with Thunk for async API calls
3. Follow the most consistent patterns found in the codebase
4. When conflicting patterns exist, prioritize patterns in newer files or files with higher test coverage
5. Never introduce patterns not found in the existing codebase

## Code Quality Standards

- Write self-documenting code with clear naming
- Follow PEP 8 for Python, ESLint react-app presets for JavaScript
- Use Django REST Framework best practices
- Validate all API inputs via DRF serializers

## Documentation Requirements

- Match the level and style of comments found in existing code
- Document according to patterns observed in the codebase
- Follow existing patterns for documenting non-obvious behavior

## Testing Approach

- Match the exact structure and style of existing tests
- **Django tests**: `python manage.py test`
- **Frontend tests**: `cd frontend && npm test`
- Follow existing patterns for test organization

## Technology-Specific Guidelines

### Python/Django
- Use Django REST Framework ViewSets + Serializers for API
- JWT authentication via djangorestframework-simplejwt
- Models with proper `__str__`, `Meta`, and `get_absolute_url`
- Django admin customization with ModelAdmin classes

### React/Redux
- Redux pattern: constants → actions → reducers → components
- React functional components with hooks
- Axios for HTTP requests to Django backend
- React Bootstrap for UI components
- PayPal integration via react-paypal-button-v2

## Version Control Guidelines

- Follow Semantic Versioning patterns as applied in the codebase
- Match existing patterns for documenting breaking changes

## General Best Practices

- Follow naming conventions exactly as they appear in existing code
- Match code organization patterns from similar files
- Apply error handling consistent with existing patterns
- Never commit `SECRET_KEY` or database credentials
- Use environment variables for sensitive config
- CORS configured via django-cors-headers

## Project-Specific Guidance

- Scan the codebase thoroughly before generating any code
- Respect existing architectural boundaries without exception
- Full-stack ecommerce: Django REST backend + React/Redux frontend
- PayPal credentials in `.env` — never commit
- Separate settings for dev/staging/prod
- Backend on port 9000, frontend on port 3000 (proxied)
- Media files served via Django in development
