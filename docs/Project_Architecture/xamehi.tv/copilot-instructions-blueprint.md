# GitHub Copilot Instructions — xamehi.tv

## Priority Guidelines

When generating code for this repository:

1. **Version Compatibility**: Always detect and respect the exact versions of languages, frameworks, and libraries used in this project
2. **Context Files**: Prioritize patterns and standards defined in the .github/copilot directory
3. **Codebase Patterns**: When context files don't provide specific guidance, scan the codebase for established patterns
4. **Architectural Consistency**: Maintain our **Monolithic (Django + React SPA)** architectural style and established boundaries
5. **Code Quality**: Prioritize **maintainability, security, and performance** in all generated code

## Technology Version Detection

Before generating code, scan the codebase to identify:

1. **Language Versions**: Detect the exact versions of programming languages in use
   - **Python** — check `runtime.txt` and `requirements.txt`
   - **JavaScript** — check `frontend/package.json`

2. **Framework Versions**: Identify the exact versions of all frameworks
   - **Django** with Django REST Framework — check requirements
   - **SimpleJWT** for authentication (`djangorestframework-simplejwt`)
   - **React 17** — check `frontend/package.json`
   - **Redux** with Thunk middleware
   - **Material-UI 4** — check `@material-ui/core` version
   - **react-admin 4** for admin panel
   - **video-react** for media player
   - **React Bootstrap 1** for UI components

3. **Library Versions**: Note the exact versions of key libraries and dependencies
   - **PayPal** (`react-paypal-button-v2`) for payments
   - **django-allauth** for social authentication
   - **Axios** for HTTP client
   - **Gunicorn** for production WSGI
   - **WhiteNoise** for static files
   - **django-cors-headers** for CORS

## Context Files

Prioritize the following files in .github/copilot directory (if they exist):

- **architecture.md**: System architecture guidelines
- **tech-stack.md**: Technology versions and framework details
- **folder-structure.md**: Project organization guidelines

## Codebase Scanning Instructions

When context files don't provide specific guidance:

1. Identify similar files to the one being modified or created
2. Analyze patterns for:
   - **Backend**: DRF ViewSets + Serializers with JWT permissions
   - **Frontend**: Redux pattern (constants/actions/reducers), Material-UI components
   - **API communication**: Axios proxied through React dev server
   - **State**: Redux with Thunk for async API calls
   - **Admin**: react-admin for admin panel
3. Follow the most consistent patterns found in the codebase
4. When conflicting patterns exist, prioritize patterns in newer files
5. Never introduce patterns not found in the existing codebase

## Code Quality Standards

- Write self-documenting code with clear naming
- Follow PEP 8 for Python, ESLint react-app presets for JavaScript
- Use Django REST Framework best practices with JWT permissions
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
- Django REST Framework ViewSets + Serializers for API
- JWT authentication via djangorestframework-simplejwt
- django-allauth for social authentication
- CORS configured via django-cors-headers

### React/Redux
- Redux pattern: constants → actions → reducers → components
- React class components and functional components (mixed)
- Material-UI 4 components + React Bootstrap
- video-react for media player
- Axios for HTTP, proxied through React dev server
- react-admin for admin panel

## Version Control Guidelines

- Follow Semantic Versioning patterns as applied in the codebase
- Match existing patterns for documenting breaking changes

## General Best Practices

- Follow naming conventions exactly as they appear in existing code
- Match code organization patterns from similar files
- Apply error handling consistent with existing patterns
- Never commit SECRET_KEY or database credentials
- Use environment variables for all secrets
- CSRF protection enabled (Django default)

## Project-Specific Guidance

- Scan the codebase thoroughly before generating any code
- Respect existing architectural boundaries without exception
- Movie/television streaming website with Django REST backend and React frontend
- Features: movie reviews, ratings, carousels, pagination, search, admin management
- PayPal for payment processing
- video-react for media playback
- Backend on port 8000, frontend on port 3000 (proxied to backend)
- Deploy to Heroku (Procfile included), DigitalOcean, or any VPS with Gunicorn + Nginx
