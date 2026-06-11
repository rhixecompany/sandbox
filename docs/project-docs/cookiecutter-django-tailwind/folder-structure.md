# Folder Structure — cookiecutter-django-tailwind

```
cookiecutter-django-tailwind/
├── {{cookiecutter.project_slug}}/     # Generated project template
│   ├── .github/                       # CI workflows
│   ├── config/                        # Django settings
│   │   ├── settings/
│   │   │   ├── base.py                # Base settings
│   │   │   ├── local.py               # Dev settings
│   │   │   └── production.py          # Prod settings
│   │   ├── urls.py
│   │   └── wsgi.py
│   ├── apps/                          # Django applications
│   │   ├── users/                     # User management
│   │   └── ...                        # Additional apps
│   ├── static/                        # Static files
│   ├── templates/                     # Jinja2 templates
│   ├── requirements/                  # Requirements files
│   │   ├── base.txt
│   │   ├── local.txt
│   │   └── production.txt
│   ├── docker/                        # Docker config
│   ├── compose/                       # Docker Compose files
│   │   ├── local.yml
│   │   └── production.yml
│   ├── manage.py
│   ├── pyproject.toml
│   ├── package.json
│   └── tailwind.config.js
├── docs/                              # Documentation
├── hooks/                             # Cookiecutter hooks
├── cookiecutter.json                  # Cookiecutter config
├── pyproject.toml
└── AGENTS.md
```
