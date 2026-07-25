# rhixe_scans — Folder Structure Blueprint

> **Project:** rhixe_scans — Full-Stack Comic Reading Platform
> **Generated:** 2026-07-24
> **Source:** `projects/rhixe_scans/`

---

## 1. Top-Level Layout

```
rhixe_scans/
├── .devcontainer/              # VS Code Dev Container config
├── .envs/                      # Environment variable files (gitignored)
│   ├── .local/
│   │   ├── .django
│   │   └── .postgres
│   └── .production/
├── .github/                    # GitHub Actions workflows
├── .vscode/                    # VS Code workspace settings
├── backend/                    # Django backend (API + crawler)
├── compose/                    # Docker Compose auxiliary files
├── docs/                       # Project documentation
├── email/                      # React Email templates
├── node_modules/               # Node.js dependencies
├── public/                     # Next.js static assets
├── requirements/               # Python pip requirements
├── src/                        # Next.js frontend source
├── tests/                      # End-to-end / integration tests
│
├── .dockerignore
├── .editorconfig               # EditorConfig (indent=2, CRLF, utf-8)
├── .eslintignore
├── .gitignore
├── .pre-commit-config.yaml     # Pre-commit hooks config
├── .prettierignore
├── .prettierrc.yaml            # Prettier formatting rules
├── .python-version             # Python 3.12
├── .readthedocs.yml            # ReadTheDocs build config
├── AGENTS.md                   # Agent instructions
├── API_REFERENCE.md            # API documentation
├── ARCHITECTURE.md             # Architecture overview
├── CHANGELOG.md                # Release changelog
├── CONTRIBUTING.md             # Contribution guidelines
├── CONTRIBUTORS.txt            # Contributor credits
├── DATABASE_SCHEMA.md          # Database schema documentation
├── DEPLOYMENT_GUIDE.md         # Deployment instructions
├── DEVELOPMENT_GUIDE.md        # Development setup guide
├── LICENSE                     # License file
├── README.md                   # Project README
├── REPOSITORY_SUMMARY.md       # Repository overview
├── RESEARCH_REPORT.md          # Research findings
├── SECURITY.md                 # Security policy
├── SETUP_GUIDE.md              # Setup instructions
├── TESTING_GUIDE.md            # Testing guide
├── THE_STORY_OF_THIS_REPO.md   # Project history
│
├── docker-compose.docs.yml     # Docker Compose for docs
├── docker-compose.local.yml    # Docker Compose for local dev
├── docker-compose.production.yml  # Docker Compose for production
├── bun.lock                    # Bun lockfile
├── components.json             # shadcn/ui components registry
├── eslint.config.mjs           # ESLint flat config
├── jest.config.ts              # Jest test configuration
├── jest.setup.ts               # Jest setup file
├── justfile                    # Just task runner recipes
├── merge_production_dotenvs_in_dotenv.py  # Env merging utility
├── next.config.ts              # Next.js configuration
├── package.json                # Node.js dependencies
├── postcss.config.mjs          # PostCSS configuration
├── Procfile                    # Heroku process declaration
├── pyproject.toml              # Python project (Django) config
├── requirements.txt            # Python dependencies
├── tailwind.config.ts          # Tailwind CSS configuration
└── tsconfig.json               # TypeScript configuration
```

---

## 2. Backend Structure (`backend/`)

```
backend/
├── config/                         # Django project configuration
│   ├── __init__.py
│   ├── celery_app.py               # Celery app definition
│   ├── urls.py                     # Root URL dispatcher
│   ├── wsgi.py                     # WSGI entry point
│   └── settings/                   # Environment-specific settings
│       ├── base.py                 # Shared settings (all environments)
│       ├── local.py                # Local development overrides
│       ├── production.py           # Production overrides
│       └── test.py                 # Test overrides
│
├── api/                            # Django applications
│   ├── __init__.py
│   ├── conftest.py                 # Pytest fixtures
│   │
│   ├── home/                       # Home app
│   │   ├── __init__.py
│   │   ├── admin.py
│   │   ├── apps.py
│   │   ├── context_processors.py
│   │   ├── models.py
│   │   ├── tests.py
│   │   ├── urls.py
│   │   └── views.py
│   │
│   ├── libary/                     # Core domain (library/catalog)
│   │   ├── __init__.py
│   │   ├── admin.py                # Django Admin configs (Unfold themed)
│   │   ├── apps.py
│   │   ├── constants.py            # ComicStatus, ImageStatus enums
│   │   ├── data_helper.py          # Data processing helpers
│   │   ├── decorators.py           # View decorators
│   │   ├── filters.py              # Django-filter definitions
│   │   ├── forms.py                # Django forms for admin
│   │   ├── forms_helpers.py        # Form utility functions
│   │   ├── managers.py             # Custom model managers
│   │   ├── models.py               # Domain models (Comic, Chapter, etc.)
│   │   ├── pagination.py           # DRF pagination classes
│   │   ├── serializers.py          # DRF serializers
│   │   ├── signals.py              # Django signals
│   │   ├── signals_helpers.py      # Signal utility functions
│   │   ├── tables.py               # django-tables2 definitions
│   │   ├── tests.py                # Unit tests
│   │   ├── migrations/             # Database migrations
│   │   ├── templatetags/           # Custom template tags
│   │   ├── urls/                   # Per-resource URL configs
│   │   └── views/                  # DRF ViewSets
│   │
│   ├── users/                      # User management app
│   │   ├── __init__.py
│   │   ├── adapters.py             # allauth adapters
│   │   ├── admin.py
│   │   ├── apps.py
│   │   ├── forms.py
│   │   ├── models.py               # Custom User model
│   │   ├── tests.py
│   │   ├── urls.py
│   │   └── views.py
│   │
│   └── contrib/                    # Django contrib extensions
│       └── sites/
│           ├── __init__.py
│           └── migrations/         # Site framework migrations
│
├── crawler/                        # Content ingestion (Scrapy-based)
│   ├── __init__.py
│   ├── main.py                     # Spider entry point
│   ├── items.py                    # Scrapy Item definitions
│   ├── models.py                   # Crawl data models
│   ├── settings.py                 # Scrapy settings
│   └── tasks.py                    # Celery task wrappers
│
├── downloader/                     # Image download subsystem
│   ├── __init__.py
│   └── main.py                     # Download orchestration
│
├── staticfiles/                    # Collected static assets
├── locale/                         # Internationalization files
├── media/                          # User-uploaded media
├── manage.py                       # Django management CLI
└── superbase.py                    # Base management utility
```

---

## 3. Frontend Structure (`src/`)

```
src/
├── app/                            # Next.js App Router
│   ├── layout.tsx                  # Root layout with providers
│   ├── loading.tsx                 # Global loading state
│   ├── not-found.tsx               # Custom 404 page
│   ├── (auth)/                     # Auth route group
│   │   ├── sign-in/page.tsx
│   │   ├── sign-up/page.tsx
│   │   └── logout/page.tsx
│   ├── (root)/                     # Public route group
│   │   ├── layout.tsx
│   │   └── page.tsx
│   ├── dashboard/page.tsx          # User dashboard
│   ├── admin/                      # Admin panel
│   │   ├── layout.tsx
│   │   ├── page.tsx
│   │   └── main-nav.tsx
│   └── api/auth/[...nextauth]/     # NextAuth API route
│
├── assets/styles/                  # Global CSS files
├── components/                     # React components
│   ├── admin/
│   │   └── admin-search.tsx
│   ├── auth/                       # Auth forms (5 components)
│   ├── shared/                     # Header, pagination, dialogs
│   │   └── header/                 # Header sub-components (9 files)
│   └── ui/                         # shadcn/ui primitives (30+)
├── hooks/                          # Custom React hooks
│   ├── use-mobile.tsx
│   └── use-toast.ts
├── lib/                            # Utilities & business logic
│   ├── actions/                    # Server Actions (4 files)
│   ├── data/                       # Data access layer (9 files)
│   ├── constants/
│   ├── db.ts / prisma.ts           # Prisma client
│   ├── schema.ts / validators.ts   # Zod schemas
│   ├── seed.ts / sample-data.ts    # Seeding
│   └── utils.ts                    # cn() utility
├── db/                             # Prisma ORM
│   ├── schema.prisma               # 18 models
│   └── migrations/                 # Migration files
├── types/                          # TypeScript definitions
│   ├── analytics.ts
│   ├── index.ts
│   └── next-auth.d.ts              # NextAuth type augmentation
├── auth.config.ts                  # NextAuth configuration
├── auth.ts                         # Auth utilities
└── middleware.ts                   # Route protection middleware
```

---

## 4. Docker Infrastructure (`compose/`)

```
compose/
├── local/
│   ├── django/Dockerfile
│   └── node/Dockerfile
└── production/
    ├── django/Dockerfile
    ├── postgres/Dockerfile
    ├── redis/Dockerfile
    ├── redis-slave/Dockerfile
    ├── traefik/Dockerfile
    ├── aws/Dockerfile
    └── docs/Dockerfile
```

---

## 5. Directory Size Estimates

| Directory | Role | Est. Files |
| --- | --- | --- |
| `backend/api/libary/` | Core domain models, views, serializers | ~35 |
| `backend/api/users/` | User management | ~10 |
| `backend/crawler/` | Scrapy content ingestion | ~6 |
| `backend/config/` | Django settings | ~6 |
| `src/app/` | App Router pages | ~12 |
| `src/components/` | React components | ~50 |
| `src/lib/` | Utilities, actions, data access | ~20 |
| `src/db/` | Prisma schema + migrations | ~20 |
| `compose/` | Docker images | ~10 |
