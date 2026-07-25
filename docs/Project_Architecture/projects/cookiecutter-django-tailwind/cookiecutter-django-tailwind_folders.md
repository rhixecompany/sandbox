# projects/cookiecutter-django-tailwind — Folder Structure Blueprint

## Overview

- Namespace: `projects/cookiecutter-django-tailwind`
- Folder model: top-level components plus tooling/config directories.

## Directory Tree

```text
cookiecutter-django-tailwind/
├── .github/
│   ├── ISSUE_TEMPLATE/
│   ├── workflows/
│   ├── changelog-template.md
│   ├── CONTRIBUTORS-template.md
│   ├── contributors.json
│   ├── copilot-instructions.md
│   ├── dependabot.yml
│   ├── FUNDING.yml
│   └── PULL_REQUEST_TEMPLATE.md
├── hooks/
│   ├── post_gen_project.py
│   └── pre_gen_project.py
├── {{cookiecutter.project_slug}}/
│   ├── .devcontainer/
│   ├── .envs/
│   ├── .github/
│   ├── compose/
│   ├── config/
│   ├── locale/
│   ├── requirements/
│   ├── utility/
│   ├── webpack/
│   ├── {{cookiecutter.project_slug}}/
│   ├── .drone.yml
│   ├── .editorconfig
│   ├── .gitattributes
│   ├── .gitlab-ci.yml
│   ├── .pre-commit-config.yaml
│   ├── .readthedocs.yml
│   ├── .travis.yml
│   ├── CONTRIBUTORS.txt
│   ├── COPYING
│   ├── docker-compose.docs.yml
│   ├── docker-compose.local.yml
│   ├── docker-compose.production.yml
│   ├── gulpfile.js
│   ├── LICENSE
│   ├── manage.py
│   ├── merge_production_dotenvs_in_dotenv.py
│   ├── package.json
│   ├── postcss.config.cjs
│   ├── Procfile
│   ├── pyproject.toml
│   ├── README.md
│   ├── requirements.txt
│   ├── runtime.txt
│   ├── tailwind.config.cjs
│   └── tsconfig.json
├── .editorconfig
├── .flake8
├── .gitattributes
├── .pre-commit-config.yaml
├── .pyup.yml
├── .readthedocs.yaml
├── AGENTS.md
├── AUDIT_cookiecutter-django-tailwind.md
├── CHANGELOG.md
├── CODE_OF_CONDUCT.md
├── CONTRIBUTING.md
├── CONTRIBUTORS.md
├── cookiecutter.json
├── LICENSE
├── pyproject.toml
├── README.md
├── REPOSITORY_SUMMARY.md
├── requirements.txt
├── RESEARCH_REPORT.md
├── setup.py
├── THE_STORY_OF_THIS_REPO.md
├── tox.ini
└── web-research-cookiecutter-django-tailwind.md
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
