# Cookiecutter Django Tailwind — Database Schema

## Template Database Schema

The generated Django project comes with PostgreSQL as the primary database. Below is the schema structure created out of the box.

## Core Tables

### `users_user` (Custom User Model)

| Column | Type | Constraints | Description |
|--------|------|-------------|-------------|
| `id` | `integer` | `PK AUTOINCREMENT` | Unique ID |
| `password` | `varchar(128)` | `NOT NULL` | Hashed password |
| `last_login` | `timestamptz` | `NULLABLE` | Last login timestamp |
| `is_superuser` | `boolean` | `DEFAULT false` | Admin status |
| `username` | `varchar(150)` | `UNIQUE NOT NULL` | Username (or email) |
| `first_name` | `varchar(150)` | `NOT NULL` | First name |
| `last_name` | `varchar(150)` | `NOT NULL` | Last name |
| `email` | `varchar(254)` | `NOT NULL` | Email address |
| `is_staff` | `boolean` | `DEFAULT false` | Staff access |
| `is_active` | `boolean` | `DEFAULT true` | Active flag |
| `date_joined` | `timestamptz` | `DEFAULT NOW()` | Registration date |

### `users_user_groups` (M2M Junction)

| Column | Type | Constraints |
|--------|------|-------------|
| `user_id` | `integer` | `FK → users_user.id` |
| `group_id` | `integer` | `FK → auth_group.id` |

### `users_user_user_permissions` (M2M Junction)

| Column | Type | Constraints |
|--------|------|-------------|
| `user_id` | `integer` | `FK → users_user.id` |
| `permission_id` | `integer` | `FK → auth_permission.id` |

### `django_admin_log`

| Column | Type | Constraints | Description |
|--------|------|-------------|-------------|
| `id` | `integer` | `PK` | |
| `action_time` | `timestamptz` | `NOT NULL` | When action occurred |
| `object_id` | `text` | `NULLABLE` | Affected object |
| `object_repr` | `varchar(200)` | `NOT NULL` | String representation |
| `action_flag` | `smallint` | `NOT NULL` | Addition/Change/Deletion |
| `change_message` | `text` | `NOT NULL` | Detail of changes |
| `content_type_id` | `integer` | `FK → django_content_type.id` | |
| `user_id` | `integer` | `FK → users_user.id` | Who performed action |

### `django_session`

| Column | Type | Constraints |
|--------|------|-------------|
| `session_key` | `varchar(40)` | `PK` |
| `session_data` | `text` | `NOT NULL` |
| `expire_date` | `timestamptz` | `NOT NULL` |

### `account_emailaddress` (django-allauth)

| Column | Type | Constraints | Description |
|--------|------|-------------|-------------|
| `id` | `integer` | `PK` | |
| `email` | `varchar(254)` | `NOT NULL` | Email address |
| `verified` | `boolean` | `DEFAULT false` | Verification status |
| `primary` | `boolean` | `DEFAULT false` | Primary email |
| `user_id` | `integer` | `FK → users_user.id` | Owner |

### `socialaccount_socialaccount` (allauth social)

| Column | Type | Constraints |
|--------|------|-------------|
| `id` | `integer` | `PK` |
| `provider` | `varchar(30)` | `NOT NULL` |
| `uid` | `varchar(255)` | `NOT NULL` |
| `last_login` | `timestamptz` | `NOT NULL` |
| `date_joined` | `timestamptz` | `NOT NULL` |
| `user_id` | `integer` | `FK → users_user.id` |

## Django ORM Models

```python
# {{project_slug}}/users/models.py
from django.contrib.auth.models import AbstractUser

class User(AbstractUser):
    """Custom user model ready for extension."""
    pass
```

## Database Configuration

Generated `config/settings/base.py`:

```python
DATABASES = {
    "default": env.db("DATABASE_URL", default="postgres:///{{project_slug}}"),
}
```

Environment variables in `.envs/`:

```
# .envs/.local/.postgres
POSTGRES_HOST=localhost
POSTGRES_PORT=5432
POSTGRES_DB={{project_slug}}
POSTGRES_USER={{project_slug}}
POSTGRES_PASSWORD=*** 
## Usage

```bash
docker-compose -f docker-compose.local.yml up
```
