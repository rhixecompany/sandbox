# Architecture Blueprint: rhixecompany-comics

**Generated:** 2026-06-29  
**Generator:** architecture-blueprint-generator  

---

## 1. Architecture Detection and Analysis

### Technology Stack

| Category | Technology |
|---|---|
| **Backend** | Django 4.x, Django REST Framework |
| **Frontend** | Next.js 16 (App Router) |
| **Language (Backend)** | Python 3.10+ |
| **Language (Frontend)** | TypeScript (strict) |
| **Database** | PostgreSQL (shared between stacks) |
| **Async Tasks** | Celery + Redis |
| **Scraping** | Scrapy, Selenium (inherited from Django-Scrapy-Selenium) |
| **Styling** | Tailwind CSS |
| **Infrastructure** | Docker Compose |

### Architectural Pattern Detected

**Pattern:** Dual-Stack Architecture (Django API + Next.js Frontend)  
The project combines two independent stacks sharing a PostgreSQL database:

**Presentation Layer**: Next.js 16 App Router (server components by default)  
**API Layer**: Django + DRF (REST API)  
**Domain Layer**: Django apps for comics, users, core functionality  
**Scraping Layer**: Celery + Scrapy spiders + Selenium automation  
**Infrastructure Layer**: PostgreSQL, Redis, Docker Compose

---

## 2. Architectural Overview

### System Architecture

```
┌──────────────────────────────────────────────────────────────┐
│                      Client Browser                           │
│  ┌────────────────────────────────────────────────────────┐  │
│  │              Next.js 16 Frontend                        │  │
│  │  ┌──────────────┐  ┌──────────────┐  ┌──────────────┐ │  │
│  │  │ App Router   │  │ Server Comp. │  │ Tailwind CSS │ │  │
│  │  └──────────────┘  └──────────────┘  └──────────────┘ │  │
│  └────────────────────┬───────────────────────────────────┘  │
│                       │ REST API                              │
└───────────────────────┼───────────────────────────────────────┘
                        │
                        ▼
┌──────────────────────────────────────────────────────────────┐
│                   Django + DRF Backend                        │
│  ┌──────────┐  ┌──────────┐  ┌──────────┐  ┌─────────────┐  │
│  │ apps/    │  │ apps/    │  │ apps/    │  │ apps/       │  │
│  │ comics/  │  │ users/   │  │ core/    │  │ scraping/   │  │
│  └──────────┘  └──────────┘  └──────────┘  └─────────────┘  │
└──────────────────────────────────────────────────────────────┘
                        │
            ┌───────────┴───────────┐
            ▼                       ▼
┌──────────────────────┐  ┌──────────────────────────────┐
│   PostgreSQL         │  │   Celery + Redis             │
│   (Shared Database)  │  │   (Async Task Queue)         │
└──────────────────────┘  └──────────────────────────────┘
                                    │
                                    ▼
                          ┌──────────────────────┐
                          │   Scrapy/Selenium    │
                          │   (Web Scraping)     │
                          └──────────────────────┘
```

---

## 3. Key Architectural Decisions

| Decision | Rationale |
|---|---|
| Dual-stack (Django + Next.js) | Leverages Django's mature admin/ORM + Next.js modern frontend |
| Shared PostgreSQL database | Both stacks access the same data |
| Celery + Redis | Async scraping and task processing |
| Scraping consolidated from Django-Scrapy-Selenium | Reuses existing scraping patterns |

---

## 4. Data Flow

### Reading Flow
```
Browser → Next.js Frontend → Django API → Domain Apps → PostgreSQL
```

### Scraping Flow
```
Celery Beat → Celery Worker → Scrapy Spider → External Sources
                                                   ↓
                                           Django ORM → PostgreSQL
```

---

## 5. Application Organization

### Django Apps

| App | Purpose |
|---|---|
| `apps/comics/` | Comic catalog, chapters, reading state |
| `apps/users/` | User profiles, authentication |
| `apps/core/` | Cross-cutting utilities, health checks |
| `apps/scraping/` | Scrapy spiders, Selenium tasks |

---

## 6. Extensibility Points

1. **New Django apps**: Add under `backend/apps/` following existing patterns
2. **New frontend features**: Add pages under Next.js App Router
3. **Additional scraping targets**: New Scrapy spiders in scraping app
4. **API versioning**: Add `/api/v2/` for breaking changes

---

*End of architecture blueprint.*
