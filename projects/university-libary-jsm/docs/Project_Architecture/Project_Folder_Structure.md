# Project Folder Structure Blueprint

## Project: university-libary-jsm — Library Management System

**Generated:** 2026-06-25  
**Project Type:** Next.js (App Router) + TypeScript + Drizzle ORM  
**Auto-detected:** Yes (Next.js — `app/`, `components.json`, `drizzle.config.ts`, `eslint.config.mjs`, `package.json`)

---

## Directory Tree

```
university-libary-jsm/
├── .github/
│   └── workflows/
├── .vscode/
├── AGENTS.md
├── API_REFERENCE.md
├── ARCHITECTURE.md
├── CONTRIBUTING.md
├── DATABASE_SCHEMA.md
├── DEPLOYMENT_GUIDE.md
├── DEVELOPMENT_GUIDE.md
├── README.md
├── RESEARCH_REPORT.md
├── SECURITY.md
├── SETUP_GUIDE.md
├── TESTING_GUIDE.md
├── app/                       # Next.js App Router (root-level pages)
│   ├── (auth)/
│   │   ├── sign-in/
│   │   └── sign-up/
│   ├── (root)/
│   │   ├── books/
│   │   ├── library/
│   │   └── my-profile/
│   ├── admin/
│   │   ├── account-requests/
│   │   ├── book-requests/
│   │   ├── books/
│   │   └── users/
│   └── api/
│       └── auth/
├── assets/
├── auth.ts
├── books.json                 # Seed data
├── bun.lock
├── code-exemplars.md
├── components/                # React components
├── components.json            # shadcn/ui components
├── constants/
├── copilot-instructions.md
├── cross-linking-report.md
├── database/                  # Database schema/migrations
├── docs/
│   └── Project_Architecture/
├── drizzle.config.ts
├── dummybooks.json
├── emails/                    # Email templates
├── eslint.config.mjs
├── execution-summary.md
├── folder-structure.md
├── package.json
├── project-workflow.md
├── technology-stack.md
└── validation-report.md
```

---

## Naming Conventions

| Convention | Pattern | Examples |
|---|---|---|
| **Route groups** | `(group-name)` | `(auth)`, `(root)` |
| **App routes** | kebab-case | `sign-in/`, `my-profile/`, `account-requests/` |
| **Admin routes** | plural-nouns | `books/`, `users/`, `book-requests/` |
| **Config files** | dotted-prefix | `.github/`, `.vscode/` |
| **Data files** | kebab-case.json | `books.json`, `dummybooks.json` |

---

## File Placement Patterns

- **App routes**: `app/` at root level (App Router)
- **Components**: `components/`
- **Database**: `database/` with Drizzle ORM
- **Assets**: `assets/`
- **Constants**: `constants/`
- **Email templates**: `emails/`
- **Seed data**: Root-level JSON files

---

## Project Type Indicators

| Indicator | Value |
|---|---|
| Has `app/` with App Router | ✅ Next.js App Router |
| Has `drizzle.config.ts` | ✅ Drizzle ORM |
| Has `components.json` | ✅ shadcn/ui |
| Has `database/` | ✅ Local database config |
| Has `emails/` | ✅ Email templates |
| Has `auth.ts` | ✅ Authentication config |

---

## Key Architecture Decisions

1. **Next.js App Router** with route groups for auth and main app.
2. **Library domain** — Books, users, book requests, account requests, profiles.
3. **Drizzle ORM** for database management.
4. **shadcn/ui** component library.
5. **Email templates** — `emails/` directory for transactional emails.
6. **Admin panel** — Full admin CRUD for books, users, and requests.
