# xamehi — Folder Structure

> **Stack:** Django + Express + React 18  
> **Type:** Triple-Service Web Application  
> **Status:** Legacy / Active

## Directory Tree

```
xamehi/
├── .github/workflows/
├── .vscode/
├── docs/
├── public/                      # Express static / Create React App public
├── src/components/              # React 18 components (Create React App)
├── xamehi/                      # Django project package
├── manage.py                    # Django management
├── package.json                 # Node/Express dependencies
└── ...
```

## Key Patterns

- **Three-service architecture:** Django (API/admin), Express (server), React 18 (frontend)
- **Django** via `xamehi/` directory + `manage.py`
- **React** via `src/components/` (Create React App convention)
- **Express** serves from `public/`
- **Minimal structure** — appears to be a legacy or early-stage project
