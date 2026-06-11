# Copilot Instructions — profile

## Django Conventions
- Django standard conventions, PEP 8
- Class-based views preferred over function-based
- App-level URL configs with namespacing
- Custom ModelAdmin for all models

## Models
- Define `__str__`, `Meta`, `get_absolute_url` on all models
- Use `prepopulated_fields` for slug generation

## Security
- Never commit SECRET_KEY
- CKEditor allows HTML — sanitize user input to prevent XSS
- Use django-environ for environment variables
- Always set DEBUG=False in production
