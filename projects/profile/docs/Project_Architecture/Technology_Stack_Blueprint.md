# Technology Stack Blueprint

## Project: profile — Django Blog/CMS

> **Generated:** 2026-06-25  
> **Generator:** technology-stack-blueprint-generator  
> **Analysis Depth:** Comprehensive

---

## Overview

A Django-based blog/CMS platform with Google Cloud Storage for media assets and CKEditor 5 for rich content editing. Class-based views are preferred for clean, reusable code.

**Project Type:** Content Management System / Blog  
**Stack Type:** Django

---

## Technology Stack

### Languages & Runtimes

| Technology | Version | Usage |
|---|---|---|
| Python | ^3.11 | Backend language |
| Django | ^4.x | Web framework |
| HTML (Django Templates) | — | Server-side rendering |
| CSS | — | Styling |
| JavaScript | — | Client-side (CKEditor) |

### Backend Dependencies

| Category | Technologies |
|---|---|
| **Web Framework** | Django 4.x |
| **Database** | PostgreSQL |
| **Media Storage** | Google Cloud Storage (GCS) |
| **Rich Text Editor** | CKEditor 5 |
| **Serving** | Gunicorn |
| **Deployment** | Docker, Google Cloud Platform |
| **Testing** | Django Test Framework |

---

## Licensing

| Component | License |
|---|---|
| profile app | (not specified) |

---

## Key Scripts

| Command | Description |
|---|---|
| `python manage.py runserver` | Development server |
| `python manage.py test` | Run tests |
| `python manage.py collectstatic` | Collect static files |
| `python manage.py makemigrations` | Create migrations |

---

## Coding Conventions

- **CBV preference**: Class-Based Views over function views
- **PEP 8**: Python style guide
- **Django best practices**: Standard Django patterns
- **Environment**: `.env` for secrets (never committed)
- **GCS static/media**: Static files served via Google Cloud Storage

---

## Architecture Diagram

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
