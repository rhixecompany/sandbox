# projects/Django-Scrapy-Selenium — Architecture Blueprint

## Overview
- Detected stack: Node.js, TypeScript, Tailwind, ESLint, Prettier, Django, Python
- Architectural pattern: Full-stack dual-stack app (Django backend + JavaScript frontend/tooling)
- Top-level components: docs, tests

## Component Map
- `docs, tests`
- Shared config: `.vscode/` when present
- Docs: `docs/` when present

## Top-Level Structure
```text
Django-Scrapy-Selenium/
├── .devcontainer/
│   ├── bashrc.override.sh
│   └── devcontainer.json
├── .do/
│   └── app.yaml
├── .envs/
│   └── .local/
├── .github/
│   ├── workflows/
│   └── copilot-instructions.md
├── api/
│   ├── apps/
│   ├── contrib/
│   ├── home/
│   ├── src/
│   ├── static/
│   ├── templates/
│   ├── users/
│   ├── __init__.py
│   └── conftest.py
├── compose/
│   ├── local/
│   └── production/
├── config/
│   ├── settings/
│   ├── __init__.py
│   ├── celery_app.py
│   ├── urls.py
│   ├── utils.py
│   └── wsgi.py
├── crawler/
│   ├── management/
│   ├── middlewares/
│   ├── pipelines/
│   ├── spiders/
│   ├── __init__.py
│   ├── addon.py
│   ├── extensions.py
│   ├── items.py
│   ├── settings.py
│   ├── tasks.py
│   └── utils.py
├── fixtures/
│   └── db.json
├── locale/
│   ├── en/
│   ├── fr/
│   ├── ja/
│   ├── pt/
│   └── README.md
├── requirements/
│   ├── base.txt
│   ├── local.txt
│   └── production.txt
├── webpack/
│   ├── common.config.js
│   ├── dev.config.js
│   └── prod.config.js
├── .cursorrules
├── .editorconfig
├── .env.example
├── .gitattributes
├── .pre-commit-config.yaml
├── .readthedocs.yml
├── AGENTS.md
├── api.sqlite3
├── API_REFERENCE.md
├── ARCHITECTURE.md
├── AUDIT_Django-Scrapy-Selenium.md
├── CHANGELOG.md
├── chapters.json
├── code-exemplars.md
├── comics.json
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
├── execution-summary.md
├── folder-structure.md
├── geckodriver.exe
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
