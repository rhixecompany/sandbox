# 🏗 Technology Stack Blueprint - rhixecompany-comics

**Project Path:** `projects/rhixecompany-comics`
**Generated:** 2026-07-28
**Status:** Active — Full Comics Platform (Dual-Stack: Django + Next.js)

---

## Architecture Overview

**Pattern:** Two independent stacks sharing PostgreSQL database

```
rhixecompany-comics/
├── backend/    # Django 5 + DRF + Celery + Scrapy + Selenium
└── frontend/   # Next.js 16 App Router + Prisma + Tailwind
```

---

## Backend Stack (`backend/`)

| Category | Technology | Version | License |
|----------|-----------|---------|---------|
| **Framework** | Django | 5.0+ (5.2) | BSD |
| **API** | Django REST Framework | 3.15+ | MIT |
| **Language** | Python | 3.10+ | PSF |
| **ORM** | Django ORM | Built-in | BSD |
| **Scraping** | Scrapy + Selenium | ^2.11 / ^4.20 | BSD / Apache 2.0 |
| **Async Tasks** | Celery | ^5.3 | BSD |
| **Message Broker** | Redis | ^5.0 | BSD |
| **Database** | PostgreSQL | Latest | PostgreSQL |
| **Auth** | SimpleJWT | ^5.3 | MIT |
| **API Docs** | drf-spectacular | ^0.27 | MIT |
| **CORS** | django-cors-headers | ^4.3 | MIT |
| **Filters** | django-filter | ^24.1 | MIT |
| **Static Files** | WhiteNoise | ^6.6 | MIT |
| **Storage** | Pillow | ^10.0 | MIT |
| **WSGI** | Gunicorn | ^22.0 | MIT |
| **Env** | python-dotenv | ^1.0 | BSD |

### Backend Dependencies (`requirements.txt`)

```text
Django>=5.0,<5.2
djangorestframework>=3.15,<4.0
django-cors-headers>=4.3,<5.0
django-filter>=24.1,<25.0
celery>=5.3,<6.0
redis>=5.0,<6.0
scrapy>=2.11,<3.0
selenium>=4.20,<5.0
psycopg2-binary>=2.9,<3.0
gunicorn>=22.0,<23.0
python-dotenv>=1.0,<2.0
Pillow>=10.0,<11.0
whitenoise>=6.6,<7.0
djangorestframework-simplejwt>=5.3,<6.0
drf-spectacular>=0.27,<1.0
```

---

## Frontend Stack (`frontend/`)

| Category | Technology | Version | License |
|----------|-----------|---------|---------|
| **Framework** | Next.js | 16.x | MIT |
| **Language** | TypeScript (strict) | ^5 | Apache 2.0 |
| **UI Library** | React | 19.x | MIT |
| **Package Manager** | npm/pnpm | Latest | - |
| **ORM** | Prisma | Latest | Apache 2.0 |
| **Database** | PostgreSQL | Latest | PostgreSQL |
| **Auth** | NextAuth.js | Latest | ISC |
| **Styling** | Tailwind CSS | Latest | MIT |
| **UI Components** | Radix UI + shadcn/ui | Latest | MIT |
| **State** | Zustand + TanStack Query | Latest | MIT |

### Frontend Dependencies (`frontend/package.json`)

```json
{
  "dependencies": {
    "next": "16.x",
    "react": "19.x",
    "react-dom": "19.x",
    "typescript": "^5",
    "prisma": "latest",
    "@prisma/client": "latest",
    "next-auth": "latest",
    "tailwindcss": "latest",
    "@radix-ui/react-*": "latest",
    "zustand": "latest",
    "@tanstack/react-query": "latest",
    "zod": "latest"
  }
}
```

---

## Shared Infrastructure

| Component | Technology |
|-----------|------------|
| **Database** | PostgreSQL (shared) |
| **Cache/Broker** | Redis (Celery + sessions) |
| **Container** | Docker Compose |
| **Env Config** | Shared `.env` via Docker Compose |

---

## Backend Architecture

```
┌─────────────┐     ┌─────────────┐     ┌─────────────┐
│  Celery     │────▶│   Celery    │────▶│   Scrapy    │
│  Beat       │     │  Worker     │     │  Spiders    │
│ (Scheduler) │     └──────┬──────┘     └──────┬──────┘
└─────────────┘            │                   │
                           ▼                   ▼
                    ┌─────────────┐     ┌─────────────┐
                    │    Redis    │     │  Selenium   │
                    │  (Broker)   │     │  WebDriver  │
                    └─────────────┘     └─────────────┘
                           │                   │
                           ▼                   ▼
                    ┌─────────────┐     ┌─────────────┐
                    │ PostgreSQL  │     │  Beautiful  │
                    │  (Results)  │     │   Soup 4    │
                    └─────────────┘     └─────────────┘
```

### Celery Tasks

- **Scheduled scraping** (Celery Beat → daily/weekly)
- **Image processing** (compression, thumbnails)
- **Notification dispatch** (email, push)
- **Data aggregation** (stats, recommendations)

### Scrapy Spiders

- **Comic metadata** from publisher sites
- **Chapter lists** and image URLs
- **Rate limited** with polite delays
- **Middleware** for rotation, retries

---

## Frontend Architecture

**Next.js 16 App Router** with:

- Server Components by default
- Client Components for interactivity
- Server Actions for mutations
- Prisma for direct DB access (shared with backend)

---

## API Integration

| Layer | Endpoint | Purpose |
|-------|----------|---------|
| **Django REST** | `/api/v1/` | Backend API (scraping, admin, auth) |
| **Next.js API** | `/api/` | Frontend API (SSR, user-facing) |
| **Shared** | Direct Prisma | Frontend reads from shared DB |

---

## Project Structure

```
rhixecompany-comics/
├── backend/
│   ├── apps/
│   │   ├── comics/          # Comic models, views, scrapers
│   │   ├── chapters/        # Chapter management
│   │   ├── scraping/        # Scrapy spiders + Selenium
│   │   ├── tasks/           # Celery tasks
│   │   └── api/             # DRF viewsets
│   ├── config/
│   │   ├── settings/
│   │   │   ├── base.py
│   │   │   ├── local.py
│   │   │   └── production.py
│   │   ├── celery.py
│   │   └── urls.py
│   ├── requirements.txt
│   ├── manage.py
│   └── Dockerfile
├── frontend/
│   ├── src/
│   │   ├── app/            # App Router
│   │   ├── components/
│   │   ├── lib/
│   │   │   ├── prisma.ts   # Prisma client
│   │   │   └── auth.ts     # NextAuth config
│   │   └── hooks/
│   ├── prisma/
│   │   └── schema.prisma
│   ├── package.json
│   └── Dockerfile
├── docker-compose.yml
└── .env.example
```

---

## Database Schema (Shared)

```prisma
// frontend/prisma/schema.prisma (mirrors Django models)
model Comic {
  id          String   @id @default(cuid())
  title       String
  slug        String   @unique
  sourceUrl   String   @unique
  coverImage  String?
  description String?
  status      String
  author      String?
  publisher   String?
  genres      String[]
  createdAt   DateTime @default(now())
  updatedAt   DateTime @updatedAt
  chapters    Chapter[]
}

model Chapter {
  id        String   @id @default(cuid())
  comicId   String
  comic     Comic    @relation(fields: [comicId], references: [id], onDelete: Cascade)
  number    Float
  title     String?
  sourceUrl String   @unique
  images    String[]
  published Boolean  @default(false)
  createdAt DateTime @default(now())
  updatedAt DateTime @updatedAt
}
```

---

## Commands

### Backend

```bash
cd backend
pip install -r requirements.txt
python manage.py migrate
python manage.py runserver  # :8000

# Celery
celery -A config worker -l info
celery -A config beat -l info

# Scrapy
scrapy crawl comic_spider
scrapy crawl chapter_spider

# Quality
pytest
ruff check .
mypy .
```

### Frontend

```bash
cd frontend
bun install
bunx prisma generate
bunx prisma migrate dev
bun run dev  # :3000

# Quality
bun run lint
bun run type-check
bun run test
```

### Full Stack (Docker)

```bash
docker-compose up -d
# backend: 8000, frontend: 3000, db: 5432, redis: 6379
```

---

## CI/CD

**Workflow:** `.github/workflows/rhixecompany-comics-ci.yml`

1. **Backend**: Install → Ruff → MyPy → pytest → Docker build
2. **Frontend**: Install → TypeScript → ESLint → Prisma → Build → Docker build
3. **Integration**: Docker Compose up → smoke tests

---

## License Summary

| Component | License |
|-----------|---------|
| Django/DRF | BSD / MIT |
| Scrapy/Selenium | BSD / Apache 2.0 |
| Celery/Redis | BSD |
| Next.js/React | MIT |
| Prisma | Apache 2.0 |
| All tooling | MIT / BSD |

---

*Generated by Hermes Agent Technology Stack Blueprint Generator*
