# GitHub Copilot Instructions — profile

## Priority Guidelines

When generating code for this repository:

1. **Version Compatibility**: Always detect and respect the exact versions of languages, frameworks, and libraries used in this project
2. **Context Files**: Prioritize patterns and standards defined in the .github/copilot directory
3. **Codebase Patterns**: When context files don't provide specific guidance, scan the codebase for established patterns
4. **Architectural Consistency**: Maintain our **Monolithic (Django)** architectural style and established boundaries
5. **Code Quality**: Prioritize **maintainability, security, and testability** in all generated code

## Technology Version Detection

Before generating code, scan the codebase to identify:

1. **Language Versions**: Detect the exact versions of programming languages in use
   - **Python** — check `runtime.txt` and requirements
   - **Python 3.10+** or later

2. **Framework Versions**: Identify the exact versions of all frameworks
   - **Django 3.x** — check requirements for exact version
   - **Django REST Framework** — check installed apps
   - **django-ckeditor** for rich text editing

3. **Library Versions**: Note the exact versions of key libraries and dependencies
   - **django-crispy-forms** for form rendering
   - **django-filter** for filtering
   - **Google Cloud Storage** (`django-storages[google]`) for media
   - **Pillow** for image processing
   - **psycopg2-binary** for PostgreSQL
   - **Gunicorn** for production WSGI
   - **WhiteNoise** for static files

## Context Files

Prioritize the following files in .github/copilot directory (if they exist):

- **architecture.md**: System architecture guidelines
- **tech-stack.md**: Technology versions and framework details
- **folder-structure.md**: Project organization guidelines

## Codebase Scanning Instructions

When context files don't provide specific guidance:

1. Identify similar files to the one being modified or created
2. Analyze patterns for:
   - **Models**: Django model best practices with `__str__`, `Meta`, `get_absolute_url`
   - **Admin**: Custom ModelAdmin classes with list_display, search_fields, list_filter
   - **Templates**: Django template language with crispy forms
   - **URLs**: App-level url configs with namespacing
   - **Views**: Class-based views preferred over function-based
   - **Storage**: Google Cloud Storage for media files
3. Follow the most consistent patterns found in the codebase
4. When conflicting patterns exist, prioritize patterns in newer files
5. Never introduce patterns not found in the existing codebase

## Code Quality Standards

- Write self-documenting code with clear naming
- Follow PEP 8 and Django best practices
- Use type hints where possible
- Sanitize user input carefully with CKEditor to prevent XSS

## Documentation Requirements

- Match the level and style of comments found in existing code
- Document according to patterns observed in the codebase
- Follow existing patterns for documenting non-obvious behavior

## Testing Approach

- Match the exact structure and style of existing tests
- **Django tests**: `python manage.py test` or pytest
- Follow existing patterns for test organization

## Technology-Specific Guidelines

### Python/Django
- Follow Django standard conventions for models, views, and URLs
- Class-based views preferred over function-based where possible
- Customize admin with ModelAdmin classes
- Use django-environ for environment variable management
- CKEditor allows HTML — sanitize user input carefully

### Storage
- Google Cloud Storage configured via django-storages for media files
- WhiteNoise for static file serving in production

## Version Control Guidelines

- Follow Semantic Versioning patterns as applied in the codebase
- Match existing patterns for documenting breaking changes

## General Best Practices

- Follow naming conventions exactly as they appear in existing code
- Match code organization patterns from similar files
- Apply error handling consistent with existing patterns
- Never commit SECRET_KEY or any credentials
- Use django-environ for environment variable management
- Set DEBUG=False in production

## Project-Specific Guidance

- Scan the codebase thoroughly before generating any code
- Respect existing architectural boundaries without exception
- Django-based blog/profile website with rich content editing
- CKEditor for rich text, django-crispy-forms for form rendering
- Google Cloud Storage for media file storage
- Deployment via Gunicorn on Google Cloud Run, App Engine, or VPS
- Models: Profile, Post, Tag, PostComment (blog-style content)
