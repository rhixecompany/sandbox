# Profile — Django Blog/CMS

**Naming**: `snake_case` for Python files/variables/functions; `PascalCase` for Django models/classes; `UPPER_SNAKE_CASE` for settings/constants; `kebab-case` for directories.

**Patterns**: Class-Based Views (CBVs) preferred over function views; Django admin customization; CKEditor 5 for rich text editing; Google Cloud Storage for media files; environment-driven settings split.

**Structure**: Django project with standard app layout; `templates/` for HTML templates; `static/` for static assets; media files stored on GCS; settings via environment variables.

**Python**: Python 3.11+; Django 4.x; PEP 8 conventions; class-based views (CreateView, UpdateView, DetailView, ListView); Django ORM for database; PostgreSQL (production); SQLite (development).

**Media/Static**: Google Cloud Storage (GCS) for user-uploaded media; Gunicorn + WhiteNoise for static files; `collectstatic` for production deployment; GCS credentials required in `.env`.

**Rich Text**: CKEditor 5 for WYSIWYG editing in admin and frontend forms; custom widget configuration; safe HTML rendering.

**Security**: No `.env` or GCS credentials in VCS; Django CSRF/XSS/SQL injection protection built-in; media file access controlled via GCS signed URLs; `SECRET_KEY` via environment.

**Env**: `SECRET_KEY`, `DATABASE_URL`, `DEBUG`, `ALLOWED_HOSTS`, `GS_BUCKET_NAME`, `GOOGLE_APPLICATION_CREDENTIALS`.

**Commands**: `pip install -r requirements.txt` (setup); `python manage.py migrate && python manage.py makemigrations` (DB); `python manage.py collectstatic` (static); `python manage.py runserver` (dev); `python manage.py test` (test); Docker + GCP for production.
