# Copilot Instructions

Project-wide guidance for GitHub Copilot in this workspace.

## Quick Reference

- **Monorepo:** 18+ subprojects in `projects/`, root-level shared config
- **Primary Tooling:** `projects/Bash/` (Bun 1.3.14+ + TypeScript strict)
- **Source of Truth:** `AGENTS.md` (canonical), then `CLAUDE.md`, `.cursorrules`, `.hermes.md`
- **Dispatch:** Read `AGENTS.md` first; use subproject `AGENTS.md` for `projects/*/`

## Build, Test, and Lint

All commands run from the **project root** (where `package.json` and `bun.lock` exist). For subprojects, `cd projects/<name>` first.

```bash
# Install
bun install --frozen-lockfile

# Format & Lint
bun run format                           # Prettier auto-format
bun run format:check                     # Check without modifying
bun run lint:strict                      # ESLint, zero warnings (gate)
bun run lint:fix                         # Auto-fix linting issues
bun run format:markdown:check            # Markdown lint check
bun run format:markdown:fix              # Markdown lint fix
bun run typecheck                        # TypeScript: tsc --noEmit

# Test
bun run test                             # Vitest (all tests)
bash tests/verify-dryrun.sh              # Shell script verification
bash test-all.sh                         # Comprehensive shell test suite

# Multi-step validation (before PR)
bun run format && bun run typecheck && bun run lint:strict && bun run test
```

**Single Test:** Vitest tests live in `**/*.test.ts`:
```bash
bun run test -- --grep "pattern"         # Run tests matching pattern
bun run test -- src/specific.test.ts     # Run specific test file
```

## Toolchain

| Tool | Config | Purpose |
|------|--------|---------|
| **Bun** 1.3.14+ | `bunfig.toml` (per-project) | Runtime + package manager |
| **TypeScript** strict | `tsconfig.json` | Compiler: `noImplicitAny`, `noUncheckedIndexedAccess`, etc. |
| **ESLint** flat config | `eslint.config.mts` | Zero-warning gate; `@types/bun`, TypeScript parser |
| **Prettier** 3 | `.prettierrc.ts` (per-project) | Formatter: 2-space indent, single-quote strings |
| **markdownlint-cli2** | `.markdownlintrc.json` | Markdown rules |
| **cspell** 10 | `cspell.json` | Spell check |
| **Pyright** | `pyrightconfig.json` | Python type-check (basic mode, v3.11) |
| **Ruff** | `.ruff.toml` | Python lint (E, F, I, N, W, UP, B) |
| **Git hooks** | `.husky/` + `.lintstagedrc.ts` | Pre-commit: lint-staged on changed files |

## High-Level Architecture

**SandBox Monorepo:** Workspace for multi-language automation, research, and toolkit projects.

```
SandBox/
├── projects/Bash/              ← Primary TypeScript tooling (6-phase orchestrator)
├── projects/Resume_maker/      ← Bun/TypeScript PDF generator
├── projects/Django-Scrapy-*/   ← Python data/web projects
├── projects/[16+ others]/      ← Multi-language subprojects
├── .github/prompts/            ← Canonical MCP prompt library
├── .github/workflows/          ← CI/CD (shared across projects)
├── docs/                       ← Hermes docs + references
├── venv/ + requirements.txt    ← Python 3.11 environment
└── [root config]              ← AGENTS.md, CLAUDE.md, tsconfig.json, etc.
```

**Key Patterns:**

1. **6-Phase Orchestration** (Bash project): Discovery → Clone → Triage → Debug → Remediation → Cross-Reference
2. **Multi-Wrapper Parity:** Every destructive script has `.sh`, `.ps1`, `.bat` equivalents with `--dry-run` support
3. **TypeScript Strict:** No `any`, no implicit returns; use `zod` v4 for validation
4. **Logs:** Timestamped to `logs/` directory; never commit `.env` or credentials

## Conventions

**Git & Commits:**
- **Branches:** `<type>/<project>/<kebab-case-description>` (e.g., `feat/bash/add-parallel-mode`)
- **Commit Messages:** Conventional commits: `feat:`, `fix:`, `docs:`, `refactor:`, `test:`, `chore:`, `perf:`
- **PR Target:** Always `development`; `master` is production

**Code Style:**
- **TypeScript:** 2-space indent, single quotes, strict mode, no `any`
- **PowerShell:** PascalCase, 4-space indent
- **Bash:** kebab-case file names, `.sh` extension
- **Python:** PEP 8, 4-space indent, double quotes
- **Line Endings:** CRLF (Windows host, per `.editorconfig`)

**Operations:**
- **Destructive operations** require `--help` and `--dry-run` flags
- **No backup files:** Use git for rollback (never `.bak`, `.old`)
- **Logs:** `logs/action_YYYYMMDD_HHMMSS.log`
- **Secrets:** Never hardcode in source; `.env` is `.gitignore`'d

## Key Files

| File | Purpose |
|------|---------|
| `AGENTS.md` | Canonical workspace rules, toolchain, conventions |
| `CLAUDE.md` | Claude model guidance (filesystem/ast-grep MCP preference) |
| `.cursorrules` | Cursor IDE rules (defers to `AGENTS.md`) |
| `.hermes.md` | Hermes profile config + MCP server list |
| `CONTRIBUTING.md` | Git workflow, PR guidelines, branch naming |
| `.editorconfig` | Editor settings: CRLF, indent=2, utf-8 |
| `eslint.config.mts` | ESLint flat config (no old `.eslintrc`) |
| `.prettierrc.ts` | Prettier per-project config |
| `.github/prompts/` | Canonical MCP prompt library (Hermes) |

## MCP Server Precedence

Before native tools, prefer MCP servers (defined in `.hermes.md`):

- **`filesystem`** → all file operations
- **`ast-grep`** → code search/replace (faster than grep)
- **`github`** → GitHub API (issues, PRs, workflows)
- **`memory`** → persistent session memory
- **`playwright`** → browser automation
- **`sequential-thinking`** → multi-step reasoning
- **`code-sandbox`** → Node.js jest execution
- **`python-quality`** → ruff + pyright (Python lint/type-check)
- **`tooling-lint`** → eslint, prettier, markdownlint, cspell

## Source of Truth Hierarchy

1. **Dispatch Layer:** Start with `AGENTS.md`
2. **Subproject Overrides:** `projects/<name>/AGENTS.md` (if exists)
3. **Model-Specific:** `CLAUDE.md` (Claude), `.cursorrules` (Cursor), `.hermes.md` (Hermes)
4. **Hermes Fallback:** Run `hermes profile list` for live config

## Common Tasks

**Start a new feature:**
```bash
git checkout development && git pull
git checkout -b feat/projectname/description
# Make changes, test
bun run typecheck && bun run lint:strict
git commit -m "feat: description"
git push origin feat/projectname/description
# Open PR: Base=development, Compare=your-branch
```

**Debug a failing test:**
```bash
bun run test -- --grep "test name"      # Run specific test
bun run test -- src/file.test.ts        # Run specific file
bash tests/verify-dryrun.sh             # Dry-run shell verifications
```

**Before submitting a PR:**
```bash
git diff --stat origin/development      # Review scope
bun run format && bun run typecheck && bun run lint:strict && bun run test
git log --oneline origin/development..  # Review commits
```


## Repo-specific notes

- Primary workspace is a monorepo; most development happens inside projects/<name>. The primary tooling project is `projects/Bash`.

To run installs and checks for the main tooling project:
```bash
cd projects/Bash
bun install --frozen-lockfile
bun run format && bun run typecheck && bun run lint:strict
bun run test -- --grep "pattern"   # run specific tests in this project
```

- Run checks for a single subproject by changing to its directory (e.g., `cd projects/Resume_maker`) then run the same `bun run` commands.
- Run a single test in any project with:
```bash
cd projects/<name>
bun run test -- --grep "pattern"      # or specify a test file path
```
- Use root-level `CONTRIBUTING.md` and `AGENTS.md` as the canonical workflow and agent rules; CLAUDE.md and `.cursorrules` contain assistant-specific overrides.


## MCP servers configured

This repository already declares MCP servers in `.hermes.md`. The following servers are present and can be used by Copilot sessions:

- filesystem — file operations (recommended)
- tooling-lint — eslint, prettier, markdownlint, cspell
- python-quality — ruff + pyright (Python lint/type-check)
- playwright — browser automation (for web frontend testing)

Use `hermes profile list` and `.hermes.md` to view or adjust MCP server settings.

