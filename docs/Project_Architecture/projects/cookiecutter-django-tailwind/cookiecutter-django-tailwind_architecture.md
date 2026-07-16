# projects/cookiecutter-django-tailwind — Architecture Blueprint

## Overview
- Detected stack: Python
- Architectural pattern: Python service or utility project
- Top-level components: scripts, docs, tests

## Component Map
- `scripts, docs, tests`
- Shared config: `.vscode/` when present
- Docs: `docs/` when present

## Top-Level Structure
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

## Cross-Cutting Concerns
- Configuration: environment and workspace configs live alongside the project.
- Testing: test locations should follow the existing project layout.
- Tooling: keep formatter/linter/editor settings in `.vscode/`.

## Extension Points
- Add new features within the existing top-level component that matches the current layout.
- Keep new dependencies aligned with the detected stack.

## Update Notes
- Regenerate when component boundaries, package dependencies, or folder structure change.
