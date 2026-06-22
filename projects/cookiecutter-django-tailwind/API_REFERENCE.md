# Cookiecutter Django Tailwind — API Reference

> **Note:** This template generates Django projects which may include Django REST Framework (optional). Below is the API structure of a generated project.

## Generated API Structure

### Django REST Framework (Optional)

If `use_drf=y` during generation, the project includes:

#### `GET /api/v1/users/`
- **Purpose:** List users (admin only)
- **Auth:** Token/Session
- **Returns:** Paginated user list

#### `GET /api/v1/users/{id}/`
- **Purpose:** Get user details
- **Auth:** Owner or admin
- **Returns:** UserSerializer

#### `GET /api/v1/auth/`
- **Purpose:** DRF browsable API root
- **Auth:** Session

### django-allauth (Always Included)

#### `POST /accounts/signup/`
- **Purpose:** Register new user
- **Method:** POST (form)
- **Validation:** Email/username, password

#### `POST /accounts/login/`
- **Purpose:** User login
- **Method:** POST (form)

#### `GET /accounts/logout/`
- **Purpose:** User logout

#### `POST /accounts/password/reset/`
- **Purpose:** Request password reset email

#### `POST /accounts/password/change/`
- **Purpose:** Change password (authenticated)

### Django Admin

#### `GET /admin/`
- **Purpose:** Django admin interface
- **Auth:** Staff/superuser only

### Celery (Optional)

If `use_celery=y`, Celery tasks are available:

```python
# {{project_slug}}/users/tasks.py
from config.celery_app import app

@app.task
def example_task():
    """Example Celery task"""
    pass
```

### API Router Structure

When DRF is enabled, the generated `config/api_router.py`:

```python
from rest_framework.routers import DefaultRouter
from api.views import UserViewSet

router = DefaultRouter()
router.register("users", UserViewSet)

urlpatterns = router.urls
```

## Template Variables (Cookiecutter API)

The template exposes these variables for customization:

| Variable | Type | Description |
|----------|------|-------------|
| `project_name` | string | Human-readable project name |
| `project_slug` | string | Python/Package safe name |
| `description` | string | One-line description |
| `author_name` | string | Project author |
| `domain_name` | string | Production domain |
| `version` | string | Semantic version |
| `open_source_license` | choice | License type |
| `use_drf` | bool | Include Django REST Framework |
| `use_celery` | bool | Include Celery + Redis |
| `use_sentry` | bool | Include Sentry error tracking |
| `use_heroku` | bool | Configure for Heroku |
| `ci_tool` | choice | CI provider (Github, Gitlab, Travis) |
| `postgresql_version` | choice | PostgreSQL version |

## Generated Commands

```bash
python manage.py runserver        # Development server
python manage.py test             # Run tests
python manage.py createsuperuser  # Create admin
python manage.py collectstatic    # Collect static files
python manage.py makemigrations   # Create migrations
python manage.py migrate          # Apply migrations
```
