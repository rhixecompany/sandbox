# Architecture Blueprint: profile

**Generated:** 2026-06-29  
**Generator:** architecture-blueprint-generator  

---

## 1. Architecture Detection and Analysis

### Technology Stack

| Category | Technology |
|---|---|
| **Framework** | Django 3.x, Django REST Framework |
| **Language** | Python 3.10 |
| **Database** | PostgreSQL (via psycopg2-binary) |
| **Content Editor** | django-ckeditor (WYSIWYG) |
| **Forms** | django-crispy-forms |
| **Filtering** | django-filter |
| **Cloud Storage** | Google Cloud Storage (django-storages), AWS S3 alternative |
| **Static Files** | WhiteNoise |
| **Deployment** | Gunicorn, Procfile |
| **Package Manager** | pip |

### Architectural Pattern Detected

**Pattern:** Traditional Django Monolith (MVC)  
The project follows Django's standard Model-View-Template pattern with class-based views, featuring:

- **Models**: Profile, Post, Tag, PostComment with relationships
- **Views**: Class-Based Views for most endpoints
- **Templates**: Django template language with crispy forms
- **Admin**: Customized ModelAdmin with list_display, search_fields, list_filter

---

## 2. Architectural Overview

### Architecture Layers

```
┌──────────────────────────────────────────────────────────────┐
│                    Presentation Layer                         │
│  ┌──────────────┐  ┌──────────────┐  ┌───────────────────┐  │
│  │ Django Admin │  │ Class-Based  │  │  Templates        │  │
│  │              │  │ Views        │  │  (crispy forms)   │  │
│  └──────────────┘  └──────────────┘  └───────────────────┘  │
└──────────────────────────────────────────────────────────────┘
                           │
                           ▼
┌──────────────────────────────────────────────────────────────┐
│                    Application Layer                          │
│  ┌──────────────┐  ┌──────────────┐  ┌───────────────────┐  │
│  │  Models      │  │  Forms       │  │  URL Configs      │  │
│  │  (Profile,   │  │  (crispy)    │  │  (Namespaced)     │  │
│  │   Post, Tag) │  │              │  │                   │  │
│  └──────────────┘  └──────────────┘  └───────────────────┘  │
└──────────────────────────────────────────────────────────────┘
                           │
                           ▼
┌──────────────────────────────────────────────────────────────┐
│                      Storage Layer                            │
│  ┌────────────────────────────────────────────────────────┐  │
│  │  Local (dev) → Google Cloud Storage / AWS S3 (prod)    │  │
│  │  WhiteNoise for static file serving                    │  │
│  └────────────────────────────────────────────────────────┘  │
└──────────────────────────────────────────────────────────────┘
```

---

## 3. Key Design Decisions

| Decision | Rationale |
|---|---|
| Django monolith | Simple deployment, well-understood by team |
| CKEditor WYSIWYG | Rich content creation without separate CMS |
| Cloud storage abstraction | Google Cloud Storage (primary) + AWS S3 (fallback) |
| Class-based views | Reusable view logic, Django best practice |

---

## 4. Database Schema

### Core Models

| Model | Fields | Relationships |
|---|---|---|
| Profile | user, bio, avatar | User → Profile (1:1) |
| Post | title, content (CKEditor), slug, status | Post → Tag (M:N) |
| Tag | name, slug | Tag → Post (M:N) |
| PostComment | body, author, post | Post → Comment (1:N) |

---

## 5. URL Structure

| Pattern | View |
|---|---|
| `/admin/` | Django Admin |
| `/blog/` | Post ListView |
| `/blog/<slug>/` | Post DetailView |
| `/profile/<username>/` | Profile DetailView |

---

## 6. Extensibility Points

1. **New content types**: Add Django models following existing patterns
2. **Additional storage backends**: Configure in settings via django-storages
3. **REST API**: Django REST Framework is available for API endpoints
4. **Social auth**: Add django-allauth following Django conventions

---

*End of architecture blueprint.*
