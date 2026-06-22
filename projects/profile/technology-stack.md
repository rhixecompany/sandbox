# Technology Stack — profile

## Overview
Django-based blog/profile website with CKEditor rich text editing and Google Cloud Storage.

## Backend
| Technology | Version | Purpose |
|------------|---------|---------|
| Python | 3.10 | Runtime |
| Django | 3.x | Web framework |
| Django REST Framework | — | REST API (optional) |
| django-ckeditor | — | Rich text editor |
| django-crispy-forms | — | Form rendering |
| django-filter | — | Query filtering |
| psycopg2-binary | — | PostgreSQL adapter |

## Storage & Database
| Technology | Purpose |
|------------|---------|
| PostgreSQL | Production database |
| Google Cloud Storage | Media file storage |
| Amazon S3 | Alternative storage |

## Deployment
| Tool | Purpose |
|------|---------|
| Gunicorn | WSGI server |
| WhiteNoise | Static file serving |
| django-storages | Cloud storage backend |

## Models
- Profile (user profile data)
- Post (blog content with CKEditor)
- Tag (content categorization)
- PostComment (user comments)
