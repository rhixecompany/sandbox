# cookiecutter-django-tailwind - Folder Structure Blueprint

**Project Path:** `C:\Users\Alexa\Desktop\SandBox\projects\cookiecutter-django-tailwind`
**Generated:** 2026-07-10
**Stack:** Django

## Directory Tree

```
cookiecutter-django-tailwind/
├── .editorconfig
├── .github/
│   ├── changelog-template.md
│   ├── CONTRIBUTORS-template.md
│   ├── contributors.json
│   ├── copilot-instructions.md
│   ├── dependabot.yml
│   ├── FUNDING.yml
│   ├── ISSUE_TEMPLATE/
│   │   ├── bug.md
│   │   ├── feature.md
│   │   ├── paid-support.md
│   │   └── question.md
│   ├── PULL_REQUEST_TEMPLATE.md
│   └── workflows/
│       ├── ci.yml
│       ├── django-issue-checker.yml
│       ├── issue-manager.yml
│       ├── pre-commit-autoupdate.yml
│       ├── update-changelog.yml
│       └── update-contributors.yml
├── .vscode/
│   ├── extensions.json
│   ├── launch.json
│   ├── settings.json
│   └── tasks.json
├── AGENTS.md
├── CHANGELOG.md
├── CODE_OF_CONDUCT.md
├── CONTRIBUTING.md
├── CONTRIBUTORS.md
├── cookiecutter.json
├── docs/
│   ├── __init__.py
│   ├── _static/
│   ├── audit-report.md
│   ├── CODE_DOCS.md
│   ├── conf.py
│   ├── contributing.md
│   ├── cookiecutter-triage-context.md
│   ├── deployment-on-heroku.rst
│   ├── deployment-on-pythonanywhere.rst
│   ├── deployment-with-docker.rst
│   ├── developing-locally-docker.rst
│   ├── developing-locally.rst
│   ├── docker-postgres-backups.rst
│   ├── document.rst
│   ├── faq.rst
│   ├── generate-project-block.rst
│   ├── index.rst
│   ├── linters.rst
│   ├── mailgun.rst
│   ├── maintainer-guide.md
│   ├── make.bat
│   ├── Makefile
│   ├── project-generation-options.rst
│   ├── PROJECT_DOCS.docx
│   ├── PROJECT_DOCS.md
│   ├── requirements.txt
│   ├── settings.rst
│   ├── testing.rst
│   ├── troubleshooting.rst
│   └── websocket.rst
├── hooks/
│   ├── post_gen_project.py
│   └── pre_gen_project.py
├── LICENSE
├── pyproject.toml
├── README.md
├── requirements.txt
├── RESEARCH_REPORT.md
├── scripts/
│   ├── __init__.py
│   ├── create_django_issue.py
│   ├── update_changelog.py
│   └── update_contributors.py
├── setup.py
├── tests/
│   ├── __init__.py
│   ├── test_bare.sh
│   ├── test_cookiecutter_generation.py
│   ├── test_docker.sh
│   └── test_hooks.py
├── tox.ini
└── {{cookiecutter.project_slug}}/
    ├── .editorconfig
    ├── .github/
    │   ├── dependabot.yml
    │   └── workflows/
    │       └── ci.yml
    ├── compose/
    │   ├── local/
    │   │   ├── django/
    │   │   │   ├── celery/
    │   │   │   ├── Dockerfile
    │   │   │   └── start
    │   │   ├── docs/
    │   │   │   ├── Dockerfile
    │   │   │   └── start
    │   │   └── node/
    │   │       └── Dockerfile
    │   └── production/
    │       ├── aws/
    │       │   ├── Dockerfile
    │       │   └── maintenance/
    │       ├── django/
    │       │   ├── celery/
    │       │   ├── Dockerfile
    │       │   ├── entrypoint
    │       │   └── start
    │       ├── nginx/
    │       │   ├── default.conf
    │       │   └── Dockerfile
    │       ├── postgres/
    │       │   ├── Dockerfile
    │       │   └── maintenance/
    │       └── traefik/
    │           ├── Dockerfile
    │           └── traefik.yml
    ├── config/
    │   ├── __init__.py
    │   ├── api_router.py
    │   ├── asgi.py
    │   ├── celery_app.py
    │   ├── settings/
    │   │   ├── __init__.py
    │   │   ├── base.py
    │   │   ├── local.py
    │   │   ├── production.py
    │   │   └── test.py
    │   ├── urls.py
    │   ├── websocket.py
    │   └── wsgi.py
    ├── CONTRIBUTORS.txt
    ├── COPYING
    ├── docker-compose.docs.yml
    ├── docker-compose.local.yml
    ├── docker-compose.production.yml
    ├── docs/
    │   ├── __init__.py
    │   ├── conf.py
    │   ├── howto.rst
    │   ├── index.rst
    │   ├── make.bat
    │   ├── Makefile
    │   ├── pycharm/
    │   │   ├── configuration.rst
    │   │   └── images/
    │   │       ├── 1.png
    │   │       ├── 2.png
    │   │       ├── 3.png
    │   │       ├── 4.png
    │   │       ├── 7.png
    │   │       ├── 8.png
    │   │       ├── f1.png
    │   │       ├── f2.png
    │   │       ├── f3.png
    │   │       ├── f4.png
    │   │       ├── issue1.png
    │   │       └── issue2.png
    │   └── users.rst
    ├── gulpfile.js
    ├── LICENSE
    ├── locale/
    │   ├── en_US/
    │   │   └── LC_MESSAGES/
    │   │       └── django.po
    │   ├── fr_FR/
    │   │   └── LC_MESSAGES/
    │   │       └── django.po
    │   ├── pt_BR/
    │   │   └── LC_MESSAGES/
    │   │       └── django.po
    │   └── README.md
    ├── manage.py
    ├── merge_production_dotenvs_in_dotenv.py
    ├── package.json
    ├── postcss.config.cjs
    ├── Procfile
    ├── pyproject.toml
    ├── README.md
    ├── requirements/
    │   ├── base.txt
    │   ├── local.txt
    │   └── production.txt
    ├── requirements.txt
    ├── runtime.txt
    ├── tailwind.config.cjs
    ├── tests/
    │   ├── __init__.py
    │   └── test_merge_production_dotenvs_in_dotenv.py
    ├── tsconfig.json
    ├── utility/
    │   ├── install_os_dependencies.sh
    │   ├── install_python_dependencies.sh
    │   ├── requirements-bionic.apt
    │   ├── requirements-bookworm.apt
    │   ├── requirements-bullseye.apt
    │   ├── requirements-buster.apt
    │   ├── requirements-focal.apt
    │   ├── requirements-jammy.apt
    │   ├── requirements-jessie.apt
    │   ├── requirements-stretch.apt
    │   ├── requirements-trusty.apt
    │   └── requirements-xenial.apt
    ├── webpack/
    │   ├── common.config.js
    │   ├── dev.config.js
    │   └── prod.config.js
    └── {{cookiecutter.project_slug}}/
        ├── __init__.py
        ├── conftest.py
        ├── contrib/
        │   ├── __init__.py
        │   └── sites/
        │       ├── __init__.py
        │       └── migrations/
        ├── static/
        │   ├── fonts/
        │   ├── images/
        │   │   └── favicons/
        │   ├── js/
        │   │   ├── project.ts
        │   │   └── vendors.ts
        │   └── sass/
        │       ├── custom_tailwind_vars.scss
        │       └── project.scss
        ├── templates/
        │   ├── 403.html
        │   ├── 403_csrf.html
        │   ├── 404.html
        │   ├── 500.html
        │   ├── account/
        │   │   └── base_manage_password.html
        │   ├── allauth/
        │   │   ├── elements/
        │   │   └── layouts/
        │   ├── base.html
        │   ├── pages/
        │   │   ├── about.html
        │   │   └── home.html
        │   └── users/
        │       ├── user_detail.html
        │       └── user_form.html
        └── users/
            ├── __init__.py
            ├── adapters.py
            ├── admin.py
            ├── api/
            │   ├── __init__.py
            │   ├── serializers.py
            │   └── views.py
            ├── apps.py
            ├── context_processors.py
            ├── forms.py
            ├── managers.py
            ├── migrations/
            │   ├── 0001_initial.py
            │   └── __init__.py
            ├── models.py
            ├── tasks.py
            ├── tests/
            │   ├── __init__.py
            │   ├── factories.py
            │   ├── test_admin.py
            │   ├── test_drf_urls.py
            │   ├── test_drf_views.py
            │   ├── test_forms.py
            │   ├── test_managers.py
            │   ├── test_models.py
            │   ├── test_swagger.py
            │   ├── test_tasks.py
            │   ├── test_urls.py
            │   └── test_views.py
            ├── urls.py
            └── views.py
```

## Key Directories

| Directory               | Purpose          | Convention                 |
| ----------------------- | ---------------- | -------------------------- |
| `<app>/`                | Django apps      | lowercase, plural          |
| `config/` / `settings/` | Settings modules | base/local/production      |
| `templates/`            | HTML templates   | app-specific subdirs       |
| `static/`               | Static assets    | Collected by collectstatic |

## Naming Conventions

- **Directories:** kebab-case (multi-word) or lowercase
- **Files:** Match language convention (PascalCase for React, snake_case for Python)
- **Configs:** lowercase with extension (.json, .yaml, .toml)

## File Placement Patterns

- Tests: co-located (`__tests__/`) or mirrored `tests/` structure
- Types: `types/` or co-located with implementation
- Config: Root level for tool configs

---

_Generated by agents-system-prompt-context-fix-runner_
