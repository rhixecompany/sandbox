# projects/Banking — Architecture Blueprint

## Overview
- Detected stack: Next.js, React, Bun, TypeScript, Tailwind, ESLint, Prettier, Python
- Architectural pattern: JavaScript/Bun application with feature-oriented source layout
- Top-level components: src, scripts, docs

## Component Map
- `src, scripts, docs`
- Shared config: `.vscode/` when present
- Docs: `docs/` when present

## Top-Level Structure
```text
Banking/
├── .cursor/
│   ├── agents/
│   ├── hooks/
│   ├── plans/
│   ├── rules/
│   ├── skills/
│   ├── .markdownlint.json
│   ├── mcp.json
│   └── settings.json
├── .envs/
│   ├── local/
│   └── production/
├── .github/
│   ├── workflows/
│   ├── .markdownlint.json
│   ├── branch-compare-ignore
│   ├── copilot-instructions.md
│   ├── DOCKER_CI_CD_GUIDE.md
│   ├── GITHUB_ACTIONS_SETUP.md
│   └── pull_request_template.md
├── .husky/
│   ├── _/
│   └── pre-commit
├── .vercel/
│   ├── project.json
│   └── README.txt
├── bin/
│   ├── cleanup/
│   ├── deploy/
│   ├── docker/
│   ├── lib/
│   ├── server/
│   └── utils/
├── compose/
│   ├── dev/
│   ├── prod/
│   └── traefik/
├── database/
│   └── drizzle/
├── public/
│   ├── icons/
│   ├── robots.txt
│   ├── sitemap-0.xml
│   └── sitemap.xml
├── src/
│   ├── actions/
│   ├── app/
│   ├── assets/
│   ├── components/
│   ├── constants/
│   ├── dal/
│   ├── database/
│   ├── hooks/
│   ├── lib/
│   ├── stores/
│   └── types/
├── templates/
│   └── README.template.md
├── .all-contributorsrc
├── .codespellrc
├── .editorconfig
├── .env
├── .env.example
├── .env.local
├── .eslintignore
├── .gitattributes
├── .gitignore.patcher_note
├── .lintstagedrc.ts
├── .markdownlintrc.json
├── .npmrc
├── .prettierignore
├── .prettierrc.ts
├── AGENTS.md
├── API_REFERENCE.md
├── app-config.ts
├── ARCHITECTURE.md
├── AUDIT_Banking.md
├── bun.lock
├── bunfig.toml
├── CHANGELOG.md
├── code-exemplars.md
├── CODE_STYLE.md
├── components.json
├── CONTRIBUTING.md
├── copilot-instructions.md
├── cross-linking-report.md
├── DATABASE_SCHEMA.md
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
