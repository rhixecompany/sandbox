# Code Exemplars — cookiecutter-django-tailwind

## 1. Django Settings Split

```python
# config/settings/base.py
INSTALLED_APPS = [
    "django.contrib.admin",
    "django.contrib.auth",
    # ... common apps
]

# config/settings/local.py
from .base import *  # noqa
DEBUG = True
INSTALLED_APPS += ["debug_toolbar"]

# config/settings/production.py
from .base import *  # noqa
DEBUG = False
SECURE_SSL_REDIRECT = True
```

## 2. Docker Compose Setup

```yaml
# compose/local.yml
services:
  django:
    build:
      context: .
      dockerfile: docker/local/django/Dockerfile
    ports:
      - "8000:8000"
    depends_on:
      - postgres
  postgres:
    image: postgres:16
    environment:
      POSTGRES_DB: my_project
```
