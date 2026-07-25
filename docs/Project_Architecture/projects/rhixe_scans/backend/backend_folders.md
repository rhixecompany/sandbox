# projects/rhixe_scans/backend — Folder Structure Blueprint

## Overview

- Namespace: `projects/rhixe_scans/backend`
- Folder model: top-level components plus tooling/config directories.

## Directory Tree

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

## Placement Rules

- Keep code in the existing top-level component directories.
- Keep config files at the project root or `.vscode/`.
- Keep docs under `docs/` if the project already uses a docs folder.

## Naming Conventions

- Preserve the current folder naming style for this project.
- Do not normalize dots, hyphens, or underscores.

## Update Notes

- Refresh after any folder move, rename, or new top-level component.
