# Profile — Django Blog/CMS

> **Stack:** Django 4.x + GCS + CKEditor | **Type:** Content Management System / Blog | **Status:** Active

A Django-based blog/CMS platform with Google Cloud Storage for media assets and CKEditor 5 for rich content editing. Class-based views are preferred for clean, reusable code.

---

## Technology Stack

| Category | Technology |
|---|---|
| **Web Framework** | Django 4.x |
| **Language** | Python ^3.11 |
| **Database** | PostgreSQL |
| **Media Storage** | Google Cloud Storage (GCS) |
| **Rich Text Editor** | CKEditor 5 |
| **Serving** | Gunicorn |
| **Deployment** | Docker, Google Cloud Platform |
| **Testing** | Django Test Framework |

## Architecture

```
┌─────────────────────────────────────────────────────┐
│              Profile Blog/CMS                        │
├─────────────────────────────────────────────────────┤
│  Django 4.x                                         │
│  ├── Class-Based Views                              │
│  ├── Admin Interface                                │
│  └── CKEditor 5 (rich text editing)                 │
├─────────────────────────────────────────────────────┤
│  Database                                           │
│  └── PostgreSQL                                     │
├─────────────────────────────────────────────────────┤
│  Media Storage                                      │
│  └── Google Cloud Storage                           │
├─────────────────────────────────────────────────────┤
│  Deployment                                         │
│  ├── Docker                                         │
│  └── Google Cloud Platform                          │
└─────────────────────────────────────────────────────┘
```

## Project Structure

```
profile/
├── ... (Django apps)
├── manage.py
├── requirements.txt
├── Dockerfile
├── docker-compose.yml
└── docs/Project_Architecture/
```

## Getting Started

```bash
# Prerequisites: Python 3.11+, PostgreSQL

# Install dependencies
pip install -r requirements.txt

# Database setup
python manage.py migrate
python manage.py makemigrations

# Collect static files
python manage.py collectstatic

# Start development server
python manage.py runserver

# Run tests
python manage.py test
```

## Key Features

- **Rich Content Editing** — CKEditor 5 integration for WYSIWYG editing
- **Media Management** — Google Cloud Storage for scalable media hosting
- **Class-Based Views** — Clean, reusable CBV architecture
- **Admin Interface** — Django's powerful admin panel
- **Docker Deployment** — Containerized deployment on GCP

## Coding Standards

- **CBV preference**: Class-Based Views over function views
- **PEP 8**: Python style guide
- **Django best practices**: Standard Django patterns
- **Models**: Define `__str__`, `Meta`, `get_absolute_url`; `prepopulated_fields` for slugs
- **Admin**: Custom `ModelAdmin` configurations

## Security

- No secrets in VCS (`.env` never committed)
- Django `SECRET_KEY` in environment variables
- `DEBUG=False` in production
- Sanitize CKEditor HTML to prevent XSS
- GCS credentials managed securely

## Deployment

### Docker + GCP

```bash
# Build and deploy
docker build -t profile-app .
docker push gcr.io/<project>/profile-app
gcloud run deploy profile-app --image gcr.io/<project>/profile-app
```

## License

Not specified.
