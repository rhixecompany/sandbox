# projects/rhixe_scans — Folder Structure Blueprint

## Overview
- Namespace: `projects/rhixe_scans`
- Folder model: top-level components plus tooling/config directories.

## Directory Tree
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

## Placement Rules
- Keep code in the existing top-level component directories.
- Keep config files at the project root or `.vscode/`.
- Keep docs under `docs/` if the project already uses a docs folder.

## Naming Conventions
- Preserve the current folder naming style for this project.
- Do not normalize dots, hyphens, or underscores.

## Update Notes
- Refresh after any folder move, rename, or new top-level component.
