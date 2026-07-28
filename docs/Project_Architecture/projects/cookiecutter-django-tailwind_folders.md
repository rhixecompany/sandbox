# cookiecutter-django-tailwind — Folder Structure

> **Stack:** Django 5.x + Tailwind CSS  
> **Type:** Project Generator / Cookiecutter Template  
> **Status:** Active

## Directory Tree

```
cookiecutter-django-tailwind/
├── .github/
│   ├── ISSUE_TEMPLATE/
│   └── workflows/
├── .vscode/
├── docs/_static/              # Documentation static assets
├── hooks/                     # Cookiecutter pre/post-generation hooks
├── scripts/                   # Utility scripts
├── tests/                     # Tests for the template
├── cookiecutter.json          # Cookiecutter configuration
├── pyproject.toml             # Python project config
├── setup.py                   # Package setup
└── {{cookiecutter.project_slug}}/  # Cookiecut generated project template
    ├── .devcontainer/
    ├── .envs/.local/
    ├── .envs/.production/
    ├── .github/workflows/
    ├── compose/local/          # Local Docker Compose
    ├── compose/production/     # Production Docker Compose
    ├── config/settings/        # Django settings (local, production, test)
    ├── docs/                   # Generated project docs
    ├── locale/                 # i18n (en_US, fr_FR, pt_BR)
    ├── requirements/           # Split requirements (local, production, test)
    ├── tests/                  # Generated test suite
    ├── utility/                # Utility scripts
    ├── webpack/                # Webpack configuration
    └── {{cookiecutter.project_slug}}/  # Django project package
        ├── contrib/            # Django contrib apps
        ├── static/             # Static files
        ├── templates/          # Django templates
        └── users/              # User management app
```

## Key Patterns

- **Cookiecutter variables** (`{{cookiecutter.xxx}}`) for template substitution
- **Split config:** `config/settings/` by environment
- **Split Docker:** `compose/local/`, `compose/production/`
- **Split requirements:** `requirements/local.txt`, `requirements/production.txt`
- **i18n:** `locale/<locale_code>/LC_MESSAGES/` structure
- **Naming:** Snake_case for Python, kebab-case for directories
