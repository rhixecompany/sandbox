# projects/Django-Scrapy-Selenium — Folder Structure Blueprint

## Overview
- Namespace: `projects/Django-Scrapy-Selenium`
- Folder model: top-level components plus tooling/config directories.

## Directory Tree
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

## Placement Rules
- Keep code in the existing top-level component directories.
- Keep config files at the project root or `.vscode/`.
- Keep docs under `docs/` if the project already uses a docs folder.

## Naming Conventions
- Preserve the current folder naming style for this project.
- Do not normalize dots, hyphens, or underscores.

## Update Notes
- Refresh after any folder move, rename, or new top-level component.
