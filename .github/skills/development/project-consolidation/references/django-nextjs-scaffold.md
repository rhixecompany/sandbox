# Django + Next.js Project Scaffolding

Template for scaffolding a new full-stack project with Django REST backend + Next.js App Router frontend, inheriting patterns from existing repos without merging history.

## Directory Structure

```
<project-name>/
├── GUIDE.md               # Agent guidance (stack, setup, workflow, style, security)
├── RESEARCH_REPORT.md     # Inherited tech signals, architecture decisions, risks
├── README.md              # Quick start, stack table, origins
├── .gitignore             # Python + Node.js + OS + IDE patterns
├── .editorconfig          # 2-space (JS/TS) / 4-space (Python)
├── backend/
│   ├── config/            # Django settings (base, local, production)
│   ├── apps/              # Django apps (comics, scraping, users, api)
│   └── requirements.txt   # Django 5.x, DRF, Celery, Scrapy, Selenium
├── frontend/
│   ├── src/
│   │   └── app/           # Next.js App Router (layout.tsx, page.tsx, globals.css)
│   ├── next.config.ts
│   ├── package.json       # Next.js 16, React 19, Tailwind 4, shadcn/ui
│   └── tsconfig.json
├── scripts/               # Dev ops scripts
└── docs/                  # Project documentation
```

## Architecture Template

| Layer | Technology | Notes |
|-------|-----------|-------|
| Backend | Django 5.x + DRF | REST API consumed by Next.js client |
| Frontend | Next.js 16 (App Router) | React Server Components, SSR/SSG |
| Styling | Tailwind CSS 4 + shadcn/ui | Radix UI primitives, CVA for variants |
| Async | Celery + Redis | Background scraping, image processing |
| Database | PostgreSQL | Full-text search on content |
| Scraping | Scrapy + Selenium | JS-heavy sources via Selenium, structured via Scrapy |

## Key Files to Create

### GUIDE.md (agent guidance)

Must contain:

- Project overview with explicit stack table
- "Origins" section listing inherited repos and what patterns were taken
- Setup commands for backend (venv + pip) and frontend (npm/pnpm)
- Dev workflow (runserver + dev server)
- Validation gates (ruff, typecheck, lint)
- Code style (Black 88 chars, Prettier)
- Security considerations
- PR guidance (separate backend/frontend/scraping PRs)
- Troubleshooting section

### RESEARCH_REPORT.md

Must contain:

- Project type classification
- Table of inherited tech signals from each source repo
- Architecture decision rationale
- Scraping layer design (Scrapy spiders + Selenium WebDriver)
- Recommended project structure
- Key risks (history divergence, scraping legality, image storage, auth)

### .gitignore

Must exclude:
- Python artifacts (`*.pyc`, `__pycache__`, `.venv`, `.env`, `db.sqlite3`, `media/`, `staticfiles/`)
- Node artifacts (`node_modules/`, `.next/`, `out/`)
- IDE artifacts (`.vscode/`, `.idea/`)
- OS artifacts (`.DS_Store`, `Thumbs.db`)
- Docker override (`docker-compose.override.yml`)
- Scraping outputs (`scrapy_output/`, `downloads/`)

## Next.js 16 App Router Scaffold

The frontend scaffold needs:

1. **package.json** — Next.js 16+, React 19+, Tailwind 4+, shadcn/ui deps, vitest
2. **tsconfig.json** — Strict mode, `bundler` module resolution, `@/*` → `./src/*`
3. **next.config.ts** — `images.remotePatterns` with catch-all `**` wildcard
4. **src/app/layout.tsx** — Root layout with Geist font, metadata export
5. **src/app/page.tsx** — Landing page stub with Tailwind classes
6. **src/app/globals.css** — Tailwind directives, CSS custom properties for theme

## Common Pitfalls

- **History divergence**: When inheriting from multiple repos, do NOT attempt `git merge --allow-unrelated-histories`. Document the lineage in RESEARCH_REPORT.md instead. Create a clean `git init` and first commit for the scaffold.
- **Version mismatches**: Django 5.x + DRF 3.15+ work together; Celery 5.3+ needs Redis 5+. Pin major versions in requirements.txt. For frontend, pin Next.js 16, React 19, Tailwind 4 as peer-dependent.
- **Scraping legality**: Always include a risk note about robots.txt, rate limits, and terms of service in RESEARCH_REPORT.md.
- **Image storage**: Comic/image-heavy apps need CDN or S3. Never commit source images to git. Add `media/`, `staticfiles/` to .gitignore early.
