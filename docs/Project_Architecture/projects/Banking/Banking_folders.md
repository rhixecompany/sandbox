# projects/Banking — Folder Structure Blueprint

## Overview
- Namespace: `projects/Banking`
- Folder model: top-level components plus tooling/config directories.

## Directory Tree
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

## Placement Rules
- Keep code in the existing top-level component directories.
- Keep config files at the project root or `.vscode/`.
- Keep docs under `docs/` if the project already uses a docs folder.

## Naming Conventions
- Preserve the current folder naming style for this project.
- Do not normalize dots, hyphens, or underscores.

## Update Notes
- Refresh after any folder move, rename, or new top-level component.
