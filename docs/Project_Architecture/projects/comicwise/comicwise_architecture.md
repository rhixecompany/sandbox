# projects/comicwise — Architecture Blueprint

## Overview
- Detected stack: Next.js, React, Bun, TypeScript, Tailwind, ESLint, Prettier
- Architectural pattern: JavaScript/Bun application with feature-oriented source layout
- Top-level components: src, docs

## Component Map
- `src, docs`
- Shared config: `.vscode/` when present
- Docs: `docs/` when present

## Top-Level Structure
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

## Cross-Cutting Concerns
- Configuration: environment and workspace configs live alongside the project.
- Testing: test locations should follow the existing project layout.
- Tooling: keep formatter/linter/editor settings in `.vscode/`.

## Extension Points
- Add new features within the existing top-level component that matches the current layout.
- Keep new dependencies aligned with the detected stack.

## Update Notes
- Regenerate when component boundaries, package dependencies, or folder structure change.
