# VS Code JSON Config Templates

## Tech Stack Detection

1. `package.json` — check deps for: next, react, express, prisma, drizzle-orm, tailwindcss, typescript
2. `requirements.txt` — check for: django, scrapy, flask, fastapi
3. `manage.py` — Django project
4. `pyproject.toml` — Python project
5. `backend/` directory → Multi-dir full-stack

## Stack-to-Config Mapping

| Stack | settings | launch | tasks | extensions |
|-------|----------|--------|-------|------------|
| Next.js/React/TS | Prettier + Tailwind + ESLint | Dev/Build/Lint/TypeCheck | Dev/Build/Lint/Check | Prettier, Tailwind, ESLint, React snippets |
| Django/Python | Pylance + Python envs | Runserver/Test/File | Runserver/Test/Migrations/Migrate | Python, Pylance, Django, djlint |
| Bun/TS Scripts | Prettier + shell-format | Bun file / Bun tests | Format/TypeCheck/Test | Prettier, Bun, shell-format |
| Node.js | Prettier + ESLint | Node file / npm start | Start/Test | Prettier, ESLint, npm-intellisense |
| Python (standalone) | Pylance | Django-style | Test/Lint | Python, Pylance, Ruff |

## Key Rules

- Root workspace gets `mcp.json`; sub-repos do NOT
- Git submodules need commits in submodule first, then parent update
- `extensions.json` and `launch.json` are strict JSON (no JS comments)
- `settings.json` is JSONC (VS Code tolerates comments)
- Multi-dir repos need BOTH Python and JS/TS formatter blocks
- Skills in plugin directories are nested: `skills/<name>/SKILL.md` not flat
