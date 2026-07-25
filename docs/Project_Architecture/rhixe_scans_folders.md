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
│   │   │   ├── __init__.py
│   │   │   ├── artist_urls.py
│   │   │   ├── author_urls.py
│   │   │   ├── category_urls.py
│   │   │   ├── chapter_image_urls.py
│   │   │   ├── chapter_urls.py
│   │   │   ├── comic_image_urls.py
│   │   │   ├── comic_urls.py
│   │   │   ├── genre_urls.py
│   │   │   └── user_urls.py
│   │   └── views/                  # DRF ViewSets
│   │       ├── __init__.py
│   │       ├── artist_views.py
│   │       ├── author_views.py
│   │       ├── category_views.py
│   │       ├── chapter_image_views.py
│   │       ├── chapter_views.py
│   │       ├── comic_image_views.py
│   │       └── comic_views.py
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
│   │
│   ├── (auth)/                     # Auth route group
│   │   ├── sign-in/
│   │   │   └── page.tsx
│   │   ├── sign-up/
│   │   │   └── page.tsx
│   │   └── logout/
│   │       └── page.tsx
│   │
│   ├── (root)/                     # Public route group
│   │   ├── layout.tsx              # Public layout with header
│   │   └── page.tsx                # Home page
│   │
│   ├── dashboard/                  # User dashboard
│   │   └── page.tsx
│   │
│   ├── admin/                      # Admin panel
│   │   ├── layout.tsx
│   │   ├── page.tsx
│   │   └── main-nav.tsx
│   │
│   └── api/auth/[...nextauth]/     # NextAuth API route
│       └── route.ts
│
├── assets/                         # Static assets
│   └── styles/                     # Global CSS files
│
├── components/                     # React components
│   ├── admin/
│   │   └── admin-search.tsx
│   ├── auth/
│   │   ├── credentials-signin-form.tsx
│   │   ├── custom-sign-in.tsx
│   │   ├── login-form.tsx
│   │   ├── signup-form.tsx
│   │   └── sign-up-form.tsx
│   ├── shared/
│   │   ├── delete-dialog.tsx
│   │   ├── pagination.tsx
│   │   └── header/
│   │       ├── index.tsx
│   │       ├── header-menu.tsx
│   │       ├── header-nav.tsx
│   │       ├── menu.tsx
│   │       ├── mode-toggle.tsx
│   │       ├── search.tsx
│   │       ├── search-mobile.tsx
│   │       ├── sign-out.tsx
│   │       ├── user-button.tsx
│   │       └── user-menu-button.tsx
│   ├── ui/                         # shadcn/ui primitives (30+)
│   │   ├── accordion.tsx
│   │   ├── alert-dialog.tsx
│   │   ├── avatar.tsx
│   │   ├── badge.tsx
│   │   ├── breadcrumb.tsx
│   │   ├── button.tsx
│   │   ├── card.tsx
│   │   ├── carousel.tsx
│   │   ├── chart.tsx
│   │   ├── checkbox.tsx
│   │   ├── collapsible.tsx
│   │   ├── command.tsx
│   │   ├── dialog.tsx
│   │   ├── drawer.tsx
│   │   ├── dropdown-menu.tsx
│   │   ├── form.tsx
│   │   ├── input.tsx
│   │   ├── label.tsx
│   │   ├── pagination.tsx
│   │   ├── radio-group.tsx
│   │   ├── select.tsx
│   │   ├── separator.tsx
│   │   ├── sheet.tsx
│   │   ├── sidebar.tsx
│   │   ├── skeleton.tsx
│   │   ├── sonner.tsx
│   │   ├── table.tsx
│   │   ├── tabs.tsx
│   │   ├── textarea.tsx
│   │   ├── toast.tsx
│   │   ├── toaster.tsx
│   │   ├── toggle.tsx
│   │   ├── toggle-group.tsx
│   │   └── tooltip.tsx
│   ├── app-sidebar.tsx
│   ├── chart-area-interactive.tsx
│   ├── custom-sign-in.tsx
│   ├── data-table.tsx
│   ├── footer.tsx
│   ├── github-sign-in.tsx
│   ├── nav-documents.tsx
│   ├── nav-main.tsx
│   ├── nav-projects.tsx
│   ├── nav-secondary.tsx
│   ├── nav-user.tsx
│   ├── section-cards.tsx
│   ├── sign-out.tsx
│   ├── site-header.tsx
│   └── team-switcher.tsx
│
├── hooks/                          # Custom React hooks
│   ├── use-mobile.tsx
│   └── use-toast.ts
│
├── lib/                            # Utilities & business logic
│   ├── actions/                    # Next.js Server Actions
│   │   ├── bookmark.actions.ts
│   │   ├── chapter.actions.ts
│   │   ├── comic.actions.ts
│   │   └── user.actions.ts
│   ├── constants/
│   │   └── index.ts
│   ├── data/                       # Data access layer (server-side)
│   │   ├── artist.ts
│   │   ├── author.ts
│   │   ├── category.ts
│   │   ├── chapter.ts
│   │   ├── chapterimage.ts
│   │   ├── comic.ts
│   │   ├── comicimage.ts
│   │   ├── genre.ts
│   │   └── user.ts
│   ├── db.ts                       # Prisma client singleton
│   ├── executeAction.ts            # Server action wrapper
│   ├── prisma.ts                   # Prisma client export
│   ├── sample-data.ts              # Development sample data
│   ├── schema.ts                   # Zod validation schemas
│   ├── seed.ts                     # Database seeder
│   ├── utils.ts                    # General utilities (cn, etc.)
│   └── validators.ts               # Zod validators
│
├── db/                             # Prisma ORM
│   ├── schema.prisma               # Prisma schema (18 models)
│   └── migrations/                 # SQL migration files
│       └── 20250618170353_init/    # Initial migration
│
├── types/                          # TypeScript type definitions
│   ├── analytics.ts
│   ├── index.ts
│   └── next-auth.d.ts              # NextAuth type augmentation
│
├── auth.config.ts                  # NextAuth configuration
├── auth.ts                         # Auth utilities
└── middleware.ts                   # Next.js middleware (route protection)
```

---

## 4. Docker Infrastructure (`compose/`)

```
compose/
├── local/
│   ├── django/
│   │   └── Dockerfile              # Django local dev image
│   └── node/
│       └── Dockerfile              # Node/Next.js dev image
├── production/
│   ├── django/
│   │   └── Dockerfile              # Django production image
│   ├── postgres/
│   │   └── Dockerfile              # PostgreSQL with init scripts
│   ├── redis/
│   │   └── Dockerfile              # Redis cache image
│   ├── redis-slave/
│   │   └── Dockerfile              # Redis replica image
│   ├── traefik/
│   │   └── Dockerfile              # Traefik reverse proxy
│   ├── aws/
│   │   └── Dockerfile              # AWS CLI utilities
│   └── docs/
│       └── Dockerfile              # MkDocs documentation image
└── production/
    ├── django/
    │   └── Dockerfile
    ├── postgres/
    │   └── Dockerfile
    ├── redis/
    │   └── Dockerfile
    └── redis-slave/
        └── Dockerfile
```

---

## 5. Documentation (`docs/`)

```
docs/
└── Project_Architecture/           # Architecture documentation
    ├── Workflow_Analysis.md
    └── exemplars.md
```

---

## 6. Python Dependencies (`requirements/`)

```
requirements/
├── base.txt                        # Core dependencies (Django, DRF, etc.)
├── local.txt                       # Local dev dependencies
├── production.txt                  # Production dependencies
└── test.txt                        # Test dependencies
```

---

## 7. Environment Configuration (`.envs/`)

```
.envs/
├── .local/
│   ├── .django                     # Django local env vars
│   └── .postgres                   # PostgreSQL local env vars
└── .production/
    ├── .django                     # Django production env vars
    └── .postgres                   # PostgreSQL production env vars
```

---

## 8. Directory Statistics

| Directory | Purpose | Estimated Files |
| --- | --- | --- |
| `backend/` | Django REST API + Crawler | ~80 Python files |
| `src/` | Next.js frontend | ~100 TSX/TS files |
| `compose/` | Docker images | ~10 Dockerfiles |
| `docs/` | Project documentation | ~4 files |
| `email/` | React email templates | ~5 files |
| `tests/` | E2E tests | ~10 files |
| `requirements/` | Python deps | ~4 files |
| `public/` | Static assets | ~10 files |
| `.envs/` | Environment config | ~4 files |
