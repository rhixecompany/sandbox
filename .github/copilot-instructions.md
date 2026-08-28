# Copilot Instructions — SandBox Monorepo

**Canonical reference:** See `../../AGENTS.md` (general agent guidance), `../../.hermes.md` (Hermes-specific), `../../CLAUDE.md` (Claude-specific).

For full documentation, see [`copilot-instructions.md`](../../copilot-instructions.md) at the repository root.

## Quick Reference

### Root Workspace Setup
```bash
cd C:/Users/Alexa/Desktop/SandBox
bun install
python -m venv venv && source venv/Scripts/activate && pip install -r requirements.txt
bun run check  # Validate all: lint + format + typecheck + markdown + spellcheck
```

### Subproject Work
Each subproject (`projects/Banking`, `projects/comicwise`, `projects/Bash`, etc.) is autonomous.

```bash
cd projects/<PROJECT>
bun install                # Install dependencies
bun run dev               # Start (Next.js/Node projects)
bun run test              # Run tests
bun run lint              # Lint code
bun run type-check        # TypeScript check
```

## Architecture at a Glance

- **Root workspace:** TypeScript/Python linting for workspace-level code only
- **Subprojects:** Autonomous — each has its own `AGENTS.md`, `package.json`, CI, and build system
- **Shared:** `.github/workflows/` (CI), `.github/prompts/` (190+ prompts), tool configs

**Key Pattern:** Subprojects are excluded from root linting. Always work within each project's own context.

## Conventions

| Aspect | Rule |
|--------|------|
| **Branch naming** | `<type>/<project>/<kebab-case>` (e.g., `feat/banking/add-webhook`) |
| **PR target** | `development` branch |
| **TS naming** | `kebab-case.ts` (scripts), `PascalCase.tsx` (components) |
| **Python naming** | `snake_case.py` |
| **TS style** | 2-space indent, single-quotes, `strict` mode, no `any` |
| **Python style** | 4-space indent, double-quotes, PEP 8 |
| **Line endings** | CRLF (Windows host) |

## Root-Level Commands

```bash
bun run lint              # ESLint
bun run lint:fix          # Auto-fix ESLint
bun run format            # Prettier
bun run format:check      # Check Prettier
bun run typecheck         # TypeScript
bun run markdownlint      # Markdown
bun run spellcheck        # cspell
bun run check             # All checks (recommended)
```

## Major Subprojects

| Project | Stack | Key Command |
|---------|-------|-------------|
| **Banking** | Next.js 16, Drizzle, Plaid | `bun run dev` |
| **comicwise** | Next.js 15, Prisma, Stripe | `bun run dev` |
| **Bash** | Bun/TypeScript automation | `bun run lint` |
| **ecom** | Django, React, Redux | `python manage.py runserver` |
| **mcp-servers** | Multi-language MCP | See project README |

---

See [`copilot-instructions.md`](../../copilot-instructions.md) for the complete guide.
