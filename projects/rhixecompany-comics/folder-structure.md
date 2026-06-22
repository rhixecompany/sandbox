# Folder Structure — rhixecompany-comics

```text
rhixecompany-comics/
├── AGENTS.md
├── README.md
├── RESEARCH_REPORT.md
├── backend/
│   ├── .env.example
│   ├── manage.py
│   ├── requirements.txt
│   ├── apps/
│   │   ├── api/
│   │   │   ├── __init__.py
│   │   │   └── apps.py
│   │   ├── comics/
│   │   │   ├── __init__.py
│   │   │   └── apps.py
│   │   ├── core/
│   │   │   ├── __init__.py
│   │   │   ├── apps.py
│   │   │   ├── urls.py
│   │   │   └── views.py
│   │   ├── scraping/
│   │   │   ├── __init__.py
│   │   │   └── apps.py
│   │   └── users/
│   │       ├── __init__.py
│   │       └── apps.py
│   └── config/
│       ├── __init__.py
│       ├── asgi.py
│       ├── settings.py
│       ├── urls.py
│       └── wsgi.py
└── frontend/
    ├── next.config.ts
    ├── next-env.d.ts
    ├── package.json
    ├── tsconfig.json
    └── src/
        └── app/
            ├── globals.css
            ├── layout.tsx
            └── page.tsx
```

## Notes

- The backend is intentionally scaffolded around Django app boundaries that match the target architecture.
- The frontend currently provides a minimal landing page and shared metadata shell.
- Source repositories remain separate and are still available for deeper feature migration.
