# Project Folder Structure Blueprint

## Project: comicwise — Next.js Comic Streaming Platform

**Generated:** 2026-06-25  
**Project Type:** Next.js (App Router) + TypeScript + Drizzle ORM + React  
**Auto-detected:** Yes (Next.js — `next.config.ts`, `src/app/`, `package.json`, `playwright.config.mts`, `docker-compose.yml`)

---

## Directory Tree

```
comicwise/
├── .all-contributorsrc
├── .codespellrc
├── .cursorrules
├── .cwrc.json
├── .dockerignore
├── .editorconfig
├── .env.example / .env.local / .env.local.example / .env.test
├── .github/
├── .gitignore
├── .husky/
├── .prettierignore
├── .prettierrc.ts
├── .schemas/
├── .vscode/
├── AGENTS.md
├── API_REFERENCE.md
├── ARCHITECTURE.md
├── CHANGELOG.md
├── CODE_OF_CONDUCT.md
├── CONTRIBUTING.md
├── DATABASE_SCHEMA.md
├── DEPLOYMENT_GUIDE.md
├── DEVELOPMENT_GUIDE.md
├── Dockerfile
├── Project_Architecture_Blueprint_Expanded.md
├── Project_Architecture_Summary.md
├── README.md
├── RESEARCH_REPORT.md
├── SECURITY.md
├── SETUP_GUIDE.md
├── TESTING_GUIDE.md
├── appConfig.ts
├── bun.lock
├── cleanup.ps1 / cleanup.sh
├── code-exemplars.md
├── components.json
├── copilot-instructions.md
├── cross-linking-report.md
├── dev.ps1 / dev.sh
├── docker-compose.yml
├── docs/
│   └── Project_Architecture/
├── drizzle.config.ts
├── eslint.config.mts
├── execution-summary.md
├── folder-structure.md
├── install-vscode-extensions.ps1 / install-vscode-extensions.sh
├── lint-report.json
├── lint-strict.txt
├── next-env.d.ts
├── next-sitemap.config.ts
├── next.config.ts
├── node_modules/
├── package.json
├── playwright.config.mts
├── pnpm-workspace.yaml
├── postcss.config.mjs
├── project-analysis-report.md
├── project-workflow.md
├── public/
├── quality-gate-triage.json / quality-gate.json
├── quality-gate.ps1 / quality-gate.sh
├── report.*.json            # Performance/lint reports
├── seed-report-*.json
├── seed-urls-report.txt
├── setup-dev.ps1 / setup-dev.sh
├── src/
│   ├── actions/             # Server actions
│   │   └── admin/
│   ├── app/                 # Next.js App Router
│   │   ├── (auth)/
│   │   │   ├── sign-in/
│   │   │   └── sign-up/
│   │   ├── (root)/          # Main app routes
│   │   │   ├── analytics/
│   │   │   ├── authors/
│   │   │   ├── bookmarks/
│   │   │   ├── browse/
│   │   │   ├── comics/
│   │   │   ├── comments/
│   │   │   ├── feed/
│   │   │   ├── genres/
│   │   │   ├── notifications/
│   │   │   ├── profile/
│   │   │   ├── ratings/
│   │   │   ├── reading-progress/
│   │   │   ├── search/
│   │   │   └── settings/
│   │   ├── admin/           # Admin panel routes
│   │   │   ├── artists/
│   │   │   ├── audit-logs/
│   │   │   ├── authors/
│   │   │   ├── chapters/
│   │   │   ├── comics/
│   │   │   ├── genres/
│   │   │   ├── permissions/
│   │   │   ├── roles/
│   │   │   ├── types/
│   │   │   └── users/
│   │   └── api/             # API routes
│   │       ├── auth/
│   │       └── seed/
│   ├── assets/
│   │   └── svg/
│   ├── backuptests/         # E2E test backups
│   │   └── e2e/
│   └── components/          # React components
├── technology-stack.md
├── test-report.txt
├── test-ui-report.txt
├── triage-report.txt
├── tsconfig.json
├── validation-report.md
└── vitest.config.mts
```

---

## Naming Conventions

| Convention | Pattern | Examples |
| --- | --- | --- |
| **Route groups** | `(group-name)` | `(auth)`, `(root)` |
| **React components** | kebab-case | `reading-progress/`, `doughnut-chart/` |
| **App routes** | plural-nouns | `comics/`, `authors/`, `genres/`, `chapters/` |
| **Config** | dotted-prefix | `.env.example`, `.prettierrc.ts` |
| **Quality reports** | kebab-case | `lint-report.json`, `test-report.txt` |

---

## File Placement Patterns

- **App routes**: `src/app/(group)/route-name/` with nested pages
- **Server actions**: `src/actions/`
- **Admin panel**: `src/app/admin/` with resource subdirectories
- **API routes**: `src/app/api/<resource>/`
- **Components**: `src/components/`
- **Documentation**: `docs/`
- **Quality gates**: Root-level JSON and script files

---

## Project Type Indicators

| Indicator                   | Value                   |
| --------------------------- | ----------------------- |
| Has `next.config.ts`        | ✅ Next.js              |
| App Router `src/app/`       | ✅ Next.js App Router   |
| Has `playwright.config.mts` | ✅ Playwright E2E tests |
| Has `drizzle.config.ts`     | ✅ Drizzle ORM          |
| Has `docker-compose.yml`    | ✅ Docker Compose       |
| Has `Dockerfile`            | ✅ Docker build         |
| Has `pnpm-workspace.yaml`   | ✅ PNPM workspace       |
| Has quality gate scripts    | ✅ CI/CD quality gates  |

---

## Key Architecture Decisions

1. **Next.js App Router** with route groups for auth, main app, and admin.
2. **Drizzle ORM** for database with schema management.
3. **Comic domain model** — comics, chapters, authors, artists, genres, ratings, comments, bookmarks, reading progress.
4. **Admin panel** with full CRUD for all domain resources.
5. **PNPM workspace** for monorepo package management.
6. **Docker** deployment with custom Dockerfile.
7. **Quality gates** — Script-based quality checks before deployment.
8. **Comprehensive docs** — Architecture, API reference, DB schema, deployment, testing, security guides.
