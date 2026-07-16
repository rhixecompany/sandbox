# projects/rhixe_scans/backend — Architecture Blueprint

## Overview
- Detected stack: Django
- Architectural pattern: Django backend service
- Top-level components: api, config, crawler, downloader

## Component Map
- `api, config, crawler, downloader`
- Shared config: `.vscode/` when present
- Docs: `docs/` when present

## Top-Level Structure
```text
backend/
├── api/
│   ├── contrib/
│   ├── home/
│   ├── libary/
│   ├── templates/
│   ├── users/
│   ├── __init__.py
│   └── conftest.py
├── config/
│   ├── settings/
│   ├── __init__.py
│   ├── celery_app.py
│   ├── urls.py
│   └── wsgi.py
├── crawler/
│   ├── handlers/
│   ├── management/
│   ├── middlewares/
│   ├── pipelines/
│   ├── spiders/
│   ├── __init__.py
│   ├── items.py
│   ├── main.py
│   ├── models.py
│   ├── settings.py
│   └── tasks.py
├── downloader/
│   ├── management/
│   ├── __init__.py
│   └── main.py
├── fixtures/
│   └── db.json
├── locale/
│   ├── en/
│   ├── fr/
│   ├── ja/
│   ├── pt/
│   └── README.md
├── artist.json
├── author.json
├── category.json
├── chapter.json
├── chapterimage.json
├── chaptersdata1.json
├── chaptersdata2.json
├── comic.json
├── comicimage.json
├── comicsdata1.json
├── comicsdata2.json
├── genre.json
├── logs.txt
├── manage.py
├── scrapy.cfg
└── superbase.py
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
