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

## Audit & Repair Patterns (from 2026-06-16 session)

### JSON Validation
- **Trailing commas** in arrays/objects are the #1 syntax error in `launch.json` and `tasks.json`. Always validate with `python3 -c "import json; json.load(open('file'))"` after writing.
- **JS comments** (`//` and `/* */`) in `settings.json` are OK (JSONC), but NEVER in `launch.json`, `tasks.json`, or `extensions.json` (strict JSON).
- When cleaning comments from settings.json, preserve the semantic intent — move commented-out active settings to a `references/removed-settings.md` if they might be needed later.

### Dual-Stack Repos (Django + Next.js)
When AGENTS.md describes both a Python backend AND a JS/TS frontend:
- `settings.json`: Must have `[python]` + `[django-html]` blocks AND `[javascript]` + `[typescript]` + `[typescriptreact]` + `[css]` + `[scss]` blocks
- `launch.json`: Must have Django debugpy configs AND Next.js node-terminal configs
- `tasks.json`: Must have Django manage.py tasks AND frontend npm tasks (with `cd frontend &&` prefix)
- `extensions.json`: Must include both Python/Django extensions AND JS/TS/Next.js extensions
- `python.defaultInterpreterPath` should point to `backend/venv/Scripts/python.exe` (not root)

### Bun CLI Launch Config
For Bun CLI tools (not dev servers), use:
```json
{
  "type": "node",
  "runtimeExecutable": "bun",
  "program": "${workspaceFolder}/index.ts",
  "console": "integratedTerminal"
}
```
NOT `type: "node-terminal"` — that type ignores the `console` field and doesn't support `runtimeExecutable`.

### Path Variables in tasks.json
- ALWAYS use `${workspaceFolder}` instead of hardcoded absolute paths
- Example: `"command": "cd ${workspaceFolder}/Bash && bun run format"` instead of `"command": "cd C:\\Users\\Alexa\\Desktop\\SandBox\\Bash && bun run format"`

### Formatter Conflict Check
After writing any `settings.json`, verify no language has two formatters:
```python
formatters = {}
for key, val in settings.items():
    if key.startswith('[') and isinstance(val, dict) and 'editor.defaultFormatter' in val:
        lang = key.strip('[]')
        if lang in formatters:
            print(f'CONFLICT: {lang}')
        formatters[lang] = val['editor.defaultFormatter']
```

### Verification Gate (run after ALL .vscode writes)
```bash
find . -path '*/.vscode/*.json' -type f ! -path '*/node_modules/*' | while read f; do
  python3 -c "import json; json.load(open(r'$f'))" 2>/dev/null || echo "INVALID: $f"
done
```
