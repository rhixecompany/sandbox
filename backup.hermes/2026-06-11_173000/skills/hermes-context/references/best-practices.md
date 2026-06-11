# Context Files Best Practices

## AGENTS.md
1. **Keep focused** — token cost injected into every message
2. **Use subdirectory AGENTS.md** for monorepos — avoids bloating root context
3. **One AGENTS.md per logical component** — frontend, backend, shared, infra
4. **SOUL.md for personality only** — not project instructions

## Subdirectory Structure
```
my-project/
├── AGENTS.md           # Root: architecture, shared conventions
├── frontend/
│   └── AGENTS.md       # Frontend-specific: pnpm, Tailwind, components
├── backend/
│   └── AGENTS.md       # Backend-specific: poetry, uvicorn, OpenAPI
├── shared/
│   └── AGENTS.md       # Shared types, utilities
└── infra/
    └── AGENTS.md       # Deployment, Docker, CI/CD
```

## .cursorrules
- If you already use Cursor, no duplication needed
- Hermes auto-detects `.cursorrules` and `.cursor/rules/*.mdc`
- Only loaded if no higher-priority file exists

## Template for New Projects
```markdown
# Project Context
Brief description of the project.

## Architecture
- Framework: <framework>
- Language: <language>
- Database: <database>
- Deployment: <deployment>

## Conventions
- <convention 1>
- <convention 2>
- <convention 3>

## Important Notes
- <note 1>
- <note 2>

## Commands
```bash
# Dev server
<command>

# Tests
<command>

# Build
<command>
```
```

## Common Mistakes
- ❌ Putting project instructions in SOUL.md
- ❌ Duplicating root AGENTS.md content in subdirectories
- ❌ Overly verbose AGENTS.md (token cost)
- ❌ Missing security scan (file rejected silently)