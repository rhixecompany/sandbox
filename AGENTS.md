# SandBox — AGENTS.md

Guidance for AI coding agents (GitHub Copilot, Codex, Hermes, etc.) in this workspace. Follow this FIRST, then subproject-local `AGENTS.md`, then `.github/instructions/*.instructions.md`.

> Verified against real repo files 2026-07-09. No aspirational practices.

## 1. Workspace Big Picture

**Hermes agent development workspace + Copilot config library + multi-language project portfolio.** Not a single compiled app.

Four concerns coexist:
1. Workspace root — `AGENTS.md` (this), `.hermes.md`, `README.md`
2. Copilot asset library — `.github/agents/` (174), `.github/instructions/` (186), `.github/skills/`
3. Automation toolkit — `projects/Bash/` (Bun/TS orchestrator)
4. Subprojects — `projects/*` (autonomous per-language)

## 2. Directory Map

```
SandBox/
├── AGENTS.md / .hermes.md / README.md   # root config
├── .github/agents/          # 174 *.agent.md
├── .github/instructions/    # 186 *.instructions.md
├── .github/skills/          # curated Hermes skills subset
├── .github/scripts/         # Python + PS audit tooling
├── .github/workflows/       # 17 CI workflows
├── .hermes/                 # Hermes plans, hooks, scripts
├── docs/                    # Hermes docs, audits, catalogs
├── prompts/                 # 250+ *.prompt.md
├── projects/Bash/           # automation toolkit (Bun/TS)
├── projects/*/              # autonomous subprojects
├── research/                # tutorial drafts
└── venv/ + requirements.txt # Python 3.11
```

## 3. Toolchain & Commands

**Do NOT use pnpm.** Package manager: `bun@1.3.14+`

| Tool | Config | Notes |
|------|--------|-------|
| **Bun** 1.3.14+ | `package.json` | runtime + pkg mgr + test runner |
| **TypeScript** strict | `tsconfig.json` | `tsc --noEmit` in toolkit |
| **ESLint** 10 flat | `eslint.config.mts` | zero-warning gate |
| **Prettier** 3 | `.prettierrc.ts` | |
| **markdownlint-cli2** | `.markdownlintrc.json` | |
| **Vitest** 4 | | toolkit unit tests |
| **EditorConfig** | `.editorconfig` | tab, indent=2, crlf, utf-8 |

**Validation from `projects/Bash/`:**
```bash
bun install --frozen-lockfile
bun run format / format:check   # prettier
bun run typecheck               # tsc --noEmit
bun run lint:strict             # eslint --max-warnings=0
bun run test                    # vitest
bash tests/verify-dryrun.sh
```

**Single-file lint** (don't run full project lint for one file):
```bash
bunx eslint --config eslint.config.mts <file.ts> --max-warnings=0
bunx markdownlint-cli2 --config .markdownlintrc.json "<file.md>"
```

Root `package.json` has no scripts. Run everything from `projects/Bash/`.

## 4. Conventions

- **Multi-wrapper parity**: every Bash script ships as `.sh` + `.ps1` + `.bat`
- **Dry-run**: destructive actions require `--dry-run` / `-DryRun`; upgrades/cleanups need confirmation
- **No backup files**: git for rollback; never create `.bak`/`.old`
- **TypeScript strict**: no `any`, `noUncheckedIndexedAccess` on; `zod` v4 for runtime, `ts-morph` for AST
- **Naming**: Bash=kebab-case/.sh, PowerShell=PascalCase/.ps1, Agents=kebab-case.agent.md, Python=PEP 8
- **CRLF** per `.editorconfig` (Windows host); CI enforces
- **Logs**: `logs/action_YYYYMMDD_HHMMSS.log`, no secrets

## 5. Editing Copilot Assets (`.github/`)

### 5.1 Agents (`*.agent.md`)
```yaml
---
description: "Concise purpose, single-quoted"
name: "Display Name"
tools: [read, edit, search]
model: "Claude Sonnet 4.5"
target: "vscode"
infer: true
---
```
File name = `kebab-case.agent.md`. `tools` aliases: `read`, `edit`, `search`, `execute`, `web`, `agent`, `github/*`, `playwright/*`. Omit = all.

### 5.2 Instructions (`*.instructions.md`)
```yaml
---
description: "When to apply"
applyTo: "**/*.agent.md"
---
```
Use fine-grained `applyTo` globs, never blanket `**`.

### 5.3 Before creating any asset
1. Read `reports/inventory/refresh-agent-inventory-summary-*.md` for current counts
2. Check `.github/scripts/` — run relevant audit after edits
3. Update cross-reference docs in `docs/`

## 6. Automation Toolkit — `projects/Bash/`

Bun/TS orchestrator with 6 phases: Discovery → Clone → Triage → Debug → Remediation → Cross-Reference.

| Script (via `bun run`) | Purpose |
|------------------------|---------|
| `format` / `format:check` | Prettier |
| `format:markdown:check` / `:fix` | markdownlint |
| `typecheck` | tsc --noEmit |
| `lint` / `lint:fix` / `lint:strict` | ESLint (flat, zero-warning) |
| `clean:cache` / `clean:deps` | cache/dep cleanup |
| `cross-ref` / `cross-ref:fix` | asset cross-reference |
| `commit:batches` | git batch commits |

**Orchestrator**: `powershell.exe -NoProfile -File scripts/orchestrator-unified.ps1 -Mode <mode>`

⚠️ CI path filter `Bash/**` is wrong — should be `projects/Bash/**` (known issue §13).

## 7. Subprojects

Each `projects/*/` is autonomous with its own AGENTS.md. Key ones:

| Project | Stack | Package Mgr |
|---------|-------|-------------|
| `Resume_maker/` | Bun/TS | bun |
| `Bash/` (toolkit) | Bun/TS | bun |
| `Banking/`, `comicwise/`, `ecom/` | Mixed | via Bash toolkit |
| `cookiecutter-django-tailwind/`, `Django-Scrapy-Selenium/` | Python | pip/uv |
| `mcp-servers/` | MCP servers | per-language |

**Use subproject's local instructions**, not Bash conventions. Don't run bun in Python projects.

## 8. CI / GitHub Workflows (17 total)

Key workflows: `bash-scripts-ci.yml`, `validate-agentic-workflows-pr.yml`, `check-line-endings.yml`, `check-plugin-structure.yml`. Add workflows with tight path filters.

## 9. Security
- No secrets/`.env` committed; `dotenv-safe` only for `.env.example`
- Least-privilege `tools` in agent frontmatter
- Destructive ops behind `--dry-run`/confirmation

## 10. Hermes Integration
- CLI: `%LOCALAPPDATA%/hermes/hermes-agent/venv/Scripts/hermes`
- Profiles: `adminbot` (active), `default`, `code-architect`, `creative-director`, etc. Switch with `hermes profile use <name>`
- Hooks: `session-logger`, `session-auto-commit`, `governance-audit`
- Skills: curated in `.github/skills/`, full registry at `%LOCALAPPDATA%/hermes/skills/`

## 11. Session Start
1. Read `SESSION_REPORT.md` first
2. Prefer MCP tools (filesystem, github, ast-grep, memory, playwright, fetch, code-sandbox, mcp-docker, sequential-thinking, cli)
3. Switch to correct Hermes profile for task
4. After `.github` edits, run relevant `.github/scripts/` audit

## 12. Common Recipes

**Add agent**: copy template → set frontmatter → lint (`bunx markdownlint-cli2`) → run `inventory-agents.ps1` → update cross-ref docs.

**Lint one file**: `bunx eslint --config eslint.config.mts <file> --max-warnings=0` and/or `bunx markdownlint-cli2 <file.md>`.

**Run toolkit**: `powershell.exe -NoProfile -File scripts/orchestrator-unified.ps1 -Mode cross-ref`

**Add Python script**: under `.github/scripts/`, use venv, make standalone.

## 13. Known Stale References (verified 2026-07-09)
1. `.github/copilot-instructions.md` references root `Bash/` — toolkit is at `projects/Bash/`
2. CI path filter `Bash/**` — should be `projects/Bash/**`
3. `README.md` references `PROJECT_RULES.md` — file doesn't exist
4. Prompt boilerplate "use pnpm" is wrong — toolchain is bun
5. Inventory counts in `copilot-instructions.md` stale (2026-05-30 snapshot vs current 174 agents/186 instructions)

## 14. Feedback
- Flag if §13 stale references should be auto-fixed
- Verify `.github/scripts/` paths before running
- Subproject AGENTS.md is authoritative for its subtree
