# projects/rhixe_scans — Architecture Blueprint

## Overview
- Detected stack: Next.js, React, Bun, TypeScript, Tailwind, ESLint, Prettier, Python
- Architectural pattern: JavaScript/Bun application with feature-oriented source layout
- Top-level components: src, backend, docs, tests

## Component Map
- `src, backend, docs, tests`
- Shared config: `.vscode/` when present
- Docs: `docs/` when present

## Top-Level Structure
```text
rhixe_scans/
├── .devcontainer/
│   ├── bash_history
│   ├── bashrc.override.sh
│   └── devcontainer.json
├── .github/
│   ├── workflows/
│   ├── copilot-instructions.md
│   └── dependabot.yml
├── backend/
│   ├── api/
│   ├── config/
│   ├── crawler/
│   ├── downloader/
│   ├── fixtures/
│   ├── locale/
│   ├── artist.json
│   ├── author.json
│   ├── category.json
│   ├── chapter.json
│   ├── chapterimage.json
│   ├── chaptersdata1.json
│   ├── chaptersdata2.json
│   ├── comic.json
│   ├── comicimage.json
│   ├── comicsdata1.json
│   ├── comicsdata2.json
│   ├── genre.json
│   ├── logs.txt
│   ├── manage.py
│   ├── scrapy.cfg
│   └── superbase.py
├── bash/
│   ├── docker-clean.sh
│   ├── git-setup.sh
│   ├── install_chrome.sh
│   ├── install_firefox.sh
│   ├── prod-dev.sh
│   ├── prod.sh
│   └── setup.sh
├── compose/
│   └── production/
├── requirements/
│   ├── base.txt
│   ├── local.txt
│   └── production.txt
├── src/
│   ├── app/
│   ├── assets/
│   ├── components/
│   ├── db/
│   ├── hooks/
│   ├── lib/
│   ├── types/
│   ├── auth.config.ts
│   ├── auth.ts
│   └── middleware.ts
├── .editorconfig
├── .eslintignore
├── .gitattributes
├── .pre-commit-config.yaml
├── .prettierignore
├── .prettierrc.yaml
├── .python-version
├── .readthedocs.yml
├── AGENTS.md
├── API_REFERENCE.md
├── ARCHITECTURE.md
├── AUDIT_rhixe_scans.md
├── bun.lock
├── CHANGELOG.md
├── code-exemplars.md
├── components.json
├── CONTRIBUTING.md
├── CONTRIBUTORS.txt
├── copilot-instructions.md
├── cross-linking-report.md
├── DATABASE_SCHEMA.md
├── DEPLOYMENT_GUIDE.md
├── DEVELOPMENT_GUIDE.md
├── docker-compose.docs.yml
├── docker-compose.local.yml
├── docker-compose.production.yml
├── eslint.config.mjs
├── execution-summary.md
├── folder-structure.md
├── jest.config.ts
├── jest.setup.ts
├── justfile
├── LICENSE
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
