# cookiecutter-django-tailwind — Folder Structure

```
cookiecutter-django-tailwind/
├── {{cookiecutter.project_slug}}/   # Generated project template
├── docs/                             # Template documentation
├── hooks/                            # Pre/post-generation hooks
├── scripts/                          # Utility scripts
├── tests/                            # Template output validation
├── cookiecutter.json                 # Cookiecutter configuration
├── pyproject.toml                    # Python project config
├── requirements.txt                  # Dependencies
├── setup.py                          # Package setup
└── tox.ini                           # Tox testing config
```

## Key Directories

| Directory | Purpose |
|-----------|---------|
| `{{cookiecutter.project_slug}}/` | The generated Django project (all app code) |
| `hooks/` | Cookiecutter hooks for pre/post generation |
| `tests/` | Tests verifying template output correctness |
| `docs/` | Template documentation and guides |
