# projects/comicwise — Folder Structure Blueprint

## Overview
- Namespace: `projects/comicwise`
- Folder model: top-level components plus tooling/config directories.

## Directory Tree
```text
comicwise/
├── .github/
│   ├── copilot/
│   ├── ISSUE_TEMPLATE/
│   ├── plugin/
│   ├── PULL_REQUEST_TEMPLATE/
│   ├── workflows/
│   ├── copilot-instructions.md
│   └── dependabot.yml
├── .husky/
│   ├── _/
│   └── pre-commit
├── .schemas/
│   ├── collection.schema.json
│   ├── cookbook.schema.json
│   ├── my.tools.yml
│   └── tools.schema.json
├── public/
│   ├── uploads/
│   ├── file.svg
│   ├── globe.svg
│   ├── next.svg
│   ├── placeholder-comic.jpg
│   ├── robots.txt
│   ├── shadcn.jpg
│   ├── sitemap-0.xml
│   ├── sitemap.xml
│   ├── vercel.svg
│   └── window.svg
├── src/
│   ├── actions/
│   ├── app/
│   ├── assets/
│   ├── backuptests/
│   ├── components/
│   ├── dal/
│   ├── data/
│   ├── database/
│   ├── hooks/
│   ├── lib/
│   ├── schemas/
│   ├── storages/
│   ├── stores/
│   ├── styles/
│   ├── types/
│   ├── auth-adapter.ts
│   ├── auth-config.ts
│   ├── auth-providers.ts
│   ├── auth.ts
│   └── proxy.ts
├── .all-contributorsrc
├── .codespellrc
├── .cursorrules
├── .cwrc.json
├── .editorconfig
├── .env.example
├── .env.local
├── .env.local.example
├── .env.test
├── .gitattributes
├── .prettierignore
├── .prettierrc.ts
├── AGENTS.md
├── API_REFERENCE.md
├── appConfig.ts
├── ARCHITECTURE.md
├── AUDIT_comicwise.md
├── bun.lock
├── CHANGELOG.md
├── cleanup.ps1
├── cleanup.sh
├── code-exemplars.md
├── CODE_OF_CONDUCT.md
├── components.json
├── CONTRIBUTING.md
├── copilot-instructions.md
├── cross-linking-report.md
├── DATABASE_SCHEMA.md
├── DEPLOYMENT_GUIDE.md
├── dev.ps1
├── dev.sh
├── DEVELOPMENT_GUIDE.md
├── docker-compose.yml
├── Dockerfile
├── drizzle.config.ts
```

## Placement Rules
- Keep code in the existing top-level component directories.
- Keep config files at the project root or `.vscode/`.
- Keep docs under `docs/` if the project already uses a docs folder.

## Naming Conventions
- Preserve the current folder naming style for this project.
- Do not normalize dots, hyphens, or underscores.

## Update Notes
- Refresh after any folder move, rename, or new top-level component.
