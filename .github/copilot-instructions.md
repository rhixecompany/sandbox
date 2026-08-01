# Copilot Instructions

Project-wide guidance for GitHub Copilot in the SandBox monorepo.

> **Source of Truth:** This workspace is governed by `AGENTS.md` (canonical). All other instruction files (CLAUDE.md, .cursorrules, .hermes.md) are thin stubs that defer to AGENTS.md. If a rule here differs from AGENTS.md, AGENTS.md wins.

> **Quick Links:** This file covers practical setup and subproject reference. For exhaustive guidance on patterns, conventions, and MCP server details, see `AGENTS.md`:
>
> - § 2 (Technology Stack) — language versions, framework details, Python dual-install
> - § 4 (Subproject Directory) — complete project inventory with entry points
> - § 5 (Code Patterns & Conventions) — TypeScript, Python, Bash, PowerShell patterns
> - § 9 (MCP Server Precedence) — when to use MCP vs native CLI

---

## 1. Priority Guidelines

When generating code for this repository:

1. **Version Compatibility** — Always detect and respect the exact versions of languages, frameworks, and libraries used in each subproject.
2. **AGENTS.md First** — Read the project-level `AGENTS.md` and subproject `projects/<name>/AGENTS.md` before writing code.
3. **Codebase Patterns First** — When instruction files don't provide specific guidance, scan the codebase for established patterns.
4. **Architectural Consistency** — Maintain the monorepo's multi-project layered architecture and established boundaries.
5. **Code Quality** — Prioritize maintainability, type safety, and testability in all generated code.

---

## 2. Workspace Setup & Python Environment

### 2.1 Initial Setup (One-time)

This workspace requires Python 3.11 (in venv) for root-level scripts. System Python 3.13 is also available but separate.

**On Windows (PowerShell):**

```powershell
# Activate venv (creates if missing)
. venv\Scripts\Activate.ps1

# Install workspace dependencies
pip install -r requirements.txt
# Or use faster uv:
uv pip install -r requirements.txt

# Verify Python versions
python --version      # Should show 3.11.x (venv)
python3 --version     # Shows 3.13.14 (system, for reference)
```

**On Linux/macOS (Bash):**

```bash
# Activate venv
source venv/bin/activate

# Install workspace dependencies
pip install -r requirements.txt
# Or: uv pip install -r requirements.txt

# Verify Python versions
python --version      # Should show 3.11.x (venv)
python3 --version     # Shows 3.13.14 (system)
```

### 2.2 Python Version Clarification

- **`python` (3.11.15)** — Use this for workspace root automation scripts in `~/AppData/Local/hermes/scripts/`. Always run from activated venv.
- **`python3` (3.13.14)** — System Python. Use only for one-off commands if needed; prefer venv.
- **PEP 668** — Virtual environment is required; `pip install` to system Python is blocked.
- **`uv`** — Fast pip alternative. Available in venv; `uv pip install` is faster than `pip install`.

### 2.3 Root-Level Package Manager

The workspace root has a minimal `package.json` (Bun workspace marker). Don't use it directly.

---

## 3. Workspace Root Scripts

The `~/AppData/Local/hermes/scripts/` directory contains 100+ Python automation scripts for Hermes maintenance, audits, and tooling. All scripts follow the pattern below and should be run from the workspace root with the venv activated.

**Key Scripts:**

| Script                       | Purpose                                                         |
| ---------------------------- | --------------------------------------------------------------- |
| `health_check.py`            | Verify workspace health (venv, deps, config)                    |
| `build_registry.py`          | Build prompt/skill registry from workspace                      |
| `audit_prompts.py`           | Audit prompt library for issues (frontmatter, duplicates, etc.) |
| `validate_vscode_configs.py` | Validate VS Code workspace settings                             |
| `build_env.py`               | Build `.env` or environment config                              |
| `memory_repair.py`           | Repair Hermes memory artifacts                                  |

**Running a script:**

```bash
# Activate venv first
source venv/bin/activate  # Linux/macOS
# or: . venv\Scripts\Activate.ps1  # PowerShell

# Run any script
python ~/AppData/Local/hermes/scripts/health_check.py
python ~/AppData/Local/hermes/scripts/build_registry.py --output registry.json
python ~/AppData/Local/hermes/scripts/audit_prompts.py --report report.md

# All scripts support --help
python ~/AppData/Local/hermes/scripts/health_check.py --help
```

**Script Patterns:**

All workspace scripts follow these conventions:

- Entry point: `if __name__ == "__main__": main()`
- CLI: `argparse` for command-line args
- Logging: timestamped console output, optional `--log` for file output
- Dry-run: many scripts support `--dry-run` flag
- Type hints: all functions have type hints
- Docstrings: module and function docstrings required

---

## 4. Technology Version Detection

Before generating code, scan the codebase to identify:

### 2.1 Language Versions

| Language       | Detected Version | Indicators                                                                 |
| -------------- | ---------------- | -------------------------------------------------------------------------- |
| **TypeScript** | ESNext (strict)  | `tsconfig.json` → `"target": "ESNext"`, `"strict": true`                   |
| **Python**     | 3.11             | `pyrightconfig.json` → `"pythonVersion": "3.11"`, `.ruff.toml` → `"py311"` |
| **Bash**       | POSIX + bashisms | Shebang `#!/usr/bin/env bash`, `set -euo pipefail`                         |
| **PowerShell** | 5.1+             | `.ps1` extensions, `PascalCase` naming                                     |

### 2.2 Runtime Versions

| Runtime     | Version  | Indicators                                                                   |
| ----------- | -------- | ---------------------------------------------------------------------------- |
| **Bun**     | >=1.3.14 | `package.json` → `"packageManager": "bun@1.3.14"`, `bunfig.toml`, `bun.lock` |
| **Node.js** | >=18     | `package.json` → `"engines": {"node": ">=18"}`                               |

### 2.3 Framework & Library Versions

Key dependencies across the workspace (see `projects/Bash/package.json` for exhaustive list):

- **zod** ^4.4.3 — schema validation (NOT zod v3)
- **vitest** ^4.1.7 — test runner (NOT jest unless a subproject uses it)
- **eslint** ^10.4.0 — flat config (`eslint.config.mts`), NOT legacy `.eslintrc`
- **prettier** ^3.8.3 — formatter
- **markdownlint-cli2** ^0.22.1 — markdown linting
- **cspell** ^10.0.0 — spell checking
- **husky** ^9.1.7 — git hooks
- **lint-staged** ^16.4.0 — staged file checks
- **ts-morph** ^28.0.0 — AST transformations
- **tsx** ^4.22.3 — TypeScript execution
- **Pyright** — basic type-checking mode
- **Ruff** 0.15.10 — Python linter (select E,F,I,N,W,UP,B,SIM,ARG,RUF)
- **pytest** 9.0.3 — Python test runner
- **pydantic** 2.13.4 — Python data validation

---

## 3. Context Files (Source of Truth Hierarchy)

| Priority | File                         | Purpose                                             |
| -------- | ---------------------------- | --------------------------------------------------- |
| 1        | `AGENTS.md` (workspace root) | Canonical workspace rules, toolchain, conventions   |
| 2        | `projects/<name>/AGENTS.md`  | Subproject-specific overrides                       |
| 3        | `CLAUDE.md`                  | Claude model-specific guidance (defer to AGENTS.md) |
| 4        | `.cursorrules`               | Cursor IDE rules (defer to AGENTS.md)               |
| 5        | `.hermes.md`                 | Hermes profile config                               |
| 6        | `CONTRIBUTING.md`            | Git workflow, PR guidelines, branch naming          |
| 7        | `.github/prompts/`           | Canonical MCP prompt library                        |

### Useful auxiliary files in `.github/copilot/` (if they exist):

- `architecture.md` — System architecture guidelines
- `tech-stack.md` — Technology versions and framework details
- `coding-standards.md` — Code style and formatting standards
- `folder-structure.md` — Project organization guidelines
- `exemplars.md` — Exemplary code patterns to follow

---

## 4. Codebase Architecture

### 4.1 Monorepo Structure

```
SandBox/
├── AGENTS.md / .hermes.md / README.md   # Root config
├── projects/Bash/                        # Primary TypeScript automation toolkit (6-phase orchestrator)
├── projects/Resume_maker/                # Bun/TypeScript PDF generator
├── projects/mcp-servers/                 # MCP server implementations (multi-language)
├── projects/Django-Scrapy-*/            # Python data/web projects
├── projects/[14+ others]/               # Multi-language subprojects
├── .github/prompts/                      # Canonical MCP prompt library
├── .github/workflows/                    # CI/CD (shared across projects)
├── scripts/                              # Pointer README only — canonical scripts live in ~/AppData/Local/hermes/scripts/
├── venv/ + requirements.txt              # Python 3.11 environment
└── docs/                                 # Hermes docs + references
```

### 4.2 Key Architectural Patterns

1. **6-Phase Orchestration** (Bash project): Discovery → Clone → Triage → Debug → Remediation → Cross-Reference
2. **Multi-Wrapper Parity:** Every destructive script has `.sh`, `.ps1`, `.bat` equivalents with `--dry-run` support
3. **MCP-First Tooling:** Prefer MCP servers over native command-line tools (filesystem over cat, ast-grep over grep, etc.)
4. **Shared CI:** `.github/workflows/` detects changed projects and runs appropriate checks

---

## 5. Code Patterns & Conventions

### 5.1 TypeScript Patterns

```typescript
// Imports — use .js extension in import specifiers (Bun requirement)
import { parseArgs } from "./lib/cli.js";

// Interfaces before implementation
export interface CliArgs {
	flags: Set<string>;
	named: Record<string, string>;
	positional: string[];
}

// JSDoc on all exports
/** CLI argument parsing utilities */
export function parseArgs(argv: string[]): CliArgs {
	// ... implementation
}

// Error classes extend built-in Error
export class ScriptError extends Error {
	constructor(
		message: string,
		public readonly exitCode: number = 1,
	) {
		super(message);
		this.name = "ScriptError";
	}
}

// Dry-run pattern for destructive operations
export class DryRunExecutor {
	constructor(private opts: DryRunOptions) {}

	async writeFile(path: string, content: string): Promise<void> {
		// Log operation, check this.opts.dryRun before executing
	}
}

// Module structure: types → class → convenience functions
// Shebang: #!/usr/bin/env bun
```

**Key rules:**

- Shebang `#!/usr/bin/env bun` for executable TypeScript files
- Use `.js` extension in import specifiers (Bun resolves to `.ts`)
- Prefer `Bun.write()`, `Bun.file()`, `Bun.spawn()` over Node.js fs alternatives
- All destructive operations support `--dry-run`
- No `any` type — use strict typing with `noUncheckedIndexedAccess`
- Non-null assertion (`!`) used where access is guaranteed after checks

### 5.2 Python Patterns

```python
#!/usr/bin/env python3
"""Module docstring describing purpose.

Usage:
    python script.py [--option VALUE]
"""

import argparse
import json
import sys
from dataclasses import dataclass
from pathlib import Path


@dataclass
class SkillResult:
    name: str
    score: int
    passed: bool
    errors: list[str]
    duration: float


def parse_args(argv: list[str] | None = None) -> argparse.Namespace:
    """Parse command-line arguments."""
    parser = argparse.ArgumentParser(description="...")
    parser.add_argument("--threshold", type=int, default=60)
    return parser.parse_args(argv)


def main() -> None:
    args = parse_args()
    # ... implementation
    print("Result: OK")


if __name__ == "__main__":
    main()
```

**Key rules:**

- Shebang `#!/usr/bin/env python3`
- Module docstrings: `"""..."""` triple double quotes
- Functions: `def func_name() -> None:` with type hints
- Prefer `pathlib.Path` over `os.path`
- Use `@dataclass` for data containers
- PEP 8 style, 4-space indent, double quotes
- Ruff linting: select E,F,I,N,W,UP,B,SIM,ARG,RUF

### 5.3 Bash Patterns

```bash
#!/usr/bin/env bash
set -euo pipefail
IFS=$'\n\t'

ROOT="$(cd "$(dirname "${BASH_SOURCE[0]}")/.." && pwd)"
DRY_RUN_SUPPORT=true

# Dry-run guard
if [[ "${1:-}" == "--dry-run" ]]; then
    echo "[DRY-RUN] Would execute: ..."
    exit 0
fi

# ... implementation
```

**Key rules:**

- `#!/usr/bin/env bash` shebang
- `set -euo pipefail` for strict error handling
- `IFS=$'\n\t'` for safe word splitting
- kebab-case file names (e.g. `verify-dryrun.sh`)
- `DRY_RUN_SUPPORT=true` marker for all destructive scripts
- `--help` and `--dry-run` support required

### 5.4 PowerShell Patterns

```powershell
# PascalCase naming, 4-space indent
function Invoke-Cleanup {
    param(
        [switch]$DryRun,
        [string]$Path
    )
    if ($DryRun) {
        Write-Host "[DRY-RUN] Would clean $Path"
        return
    }
    # ... implementation
}
```

### 5.5 Shell Wrapper Convention

Every tool/script should provide multi-platform wrappers:

- `.sh` — Bash implementation
- `.ps1` — PowerShell implementation
- `.bat` — Batch/Cmd implementation

All three wrappers must support `--help` and `--dry-run`.

### 5.6 Logging Pattern

```typescript
// TypeScript — use timestamped logging
import { dim } from "./colors.js";

const log = {
	info: (msg: string) => console.log(`[${new Date().toISOString()}] ${msg}`),
	error: (msg: string) => console.error(`[${new Date().toISOString()}] ERROR: ${msg}`),
};
```

Log files go to `logs/action_YYYYMMDD_HHMMSS.log`. Never log secrets.

---

## 6. Testing Approach

### 6.1 TypeScript Tests (Vitest)

```typescript
// Tests in **/*.test.ts
import { describe, expect, it } from "vitest";
import { parseArgs } from "../lib/cli.js";

describe("parseArgs", () => {
	it("parses flags", () => {
		const result = parseArgs(["--verbose", "--dry-run"]);
		expect(result.flags.has("verbose")).toBe(true);
		expect(result.flags.has("dry-run")).toBe(true);
	});
});
```

**Commands:**

```bash
bun run test                        # All tests
bun run test -- --grep "pattern"    # Filter by name
bun run test -- src/file.test.ts    # Single file
```

### 6.2 Shell Tests

- `bash tests/verify-dryrun.sh` — Verify all scripts have dry-run support
- `bash test-all.sh` — Comprehensive shell test suite

### 6.3 Python Tests (pytest)

```bash
# From root venv
pytest projects/<name>/
```

---

## 7. Git & Version Control

### 7.1 Branch Naming

```
<type>/<project>/<kebab-case-description>
```

**Types:** `feat`, `fix`, `refactor`, `docs`, `test`, `chore`, `perf`\
**Project:** One of 18 sub-projects under `projects/`, or `root` for workspace-level changes.

### 7.2 Commit Messages

Conventional commits format:

```
<type>: <description>

feat: add HTML output option
fix: handle empty resume data gracefully
chore: upgrade zod to 4.4.3
```

### 7.3 PR Workflow

- **PR Target:** Always `development`
- **One concern per PR** — don't mix bug fixes with new features
- **Scope to the project** — changes outside the declared project get flagged
- **Keep it small** — aim for <300 lines changed
- **Rebase, don't merge** — linear history on `development`

### 7.4 Pre-commit Validation

```bash
bun run format && bun run typecheck && bun run lint:strict && bun run test
```

---

## 8. Code Quality Standards

### 8.1 TypeScript Quality Gates

- **Zero warnings** on `bun run lint:strict` (ESLint `--max-warnings=0`)
- **Strict mode** — `noImplicitAny`, `noUncheckedIndexedAccess`, `noImplicitOverride`
- **Formatted** with Prettier (2-space indent, single quotes)
- **Type-checked** with `tsc --noEmit`

### 8.2 Python Quality Gates

- **Ruff linting:** `ruff check .` — selects E,F,I,N,W,UP,B,SIM,ARG,RUF
- **Ruff formatting:** `ruff format .` — line-length 120, double quotes, spaces
- **Pyright type-check:** basic mode, Python 3.11

### 8.3 Markdown Quality Gates

- **markdownlint-cli2** — fenced code blocks (MD046), backtick style (MD048)
- **cspell** v10 — spell check all markdown files

### 8.4 Documentation Standards

- Write self-documenting code with clear naming
- Match the level and style of comments found in existing code
- JSDoc `/** ... */` for TypeScript exports
- Python `"""..."""` docstrings for modules and functions
- Use fenced code blocks with language tags for examples

---

## 9. MCP Servers

The workspace has **16 active MCP servers** configured in `.mcp.json`. Prefer MCP tools over native CLI commands:

| Server                  | Capabilities                                    | When to Use                                                |
| ----------------------- | ----------------------------------------------- | ---------------------------------------------------------- |
| **filesystem**          | Read/write/search files, directory ops          | File CRUD, searching file contents, stat ops               |
| **ast-grep**            | AST-based code search and rewrite               | Finding patterns in code, refactoring across files         |
| **github**              | GitHub API (issues, PRs, repos, commits)        | GitHub operations (search code, create issues, manage PRs) |
| **playwright**          | Browser automation, screenshots, form filling   | Interactive web testing, browser automation, scraping      |
| **sequential-thinking** | Structured multi-step reasoning                 | Complex planning, decision trees, analysis                 |
| **fetch**               | HTTP requests, web page content extraction      | Fetching plain-text URLs, markdown conversion              |
| **code-sandbox**        | Isolated Node.js/Jest execution                 | Running JavaScript code safely                             |
| **mcp-docker**          | Container management + GitHub ops               | Docker/Docker Compose operations                           |
| **copilot-mcp**         | Copilot provider operations                     | Copilot CLI integration                                    |
| **memory**              | Persistent cross-session memory                 | Durable facts, context preservation                        |
| **python-quality**      | Ruff lint/format + Pyright typecheck            | Python code quality checks                                 |
| **tooling-lint**        | ESLint, Prettier, markdownlint, cspell          | JavaScript/TypeScript/Markdown linting and formatting      |
| **tooling-config**      | pre-commit, git-cliff, .gitignore/.editorconfig | Config file validation and generation                      |
| **linear**              | Linear.app project management                   | Issue tracking and project planning                        |
| **smithery**            | MCP registry and discovery                      | Finding and installing new MCP tools                       |
| **mindstudio**          | Third-party integrations (Gmail, Slack, Notion) | External service automation                                |

**MCP Configuration:** Defined in `.mcp.json` at workspace root. To update server list or config, edit `.mcp.json` directly.

**Avoid native CLI when MCP is available:**

| Task                   | Use                       | NOT                        |
| ---------------------- | ------------------------- | -------------------------- |
| File operations        | `filesystem` MCP          | `cat`, `head`, `echo >`    |
| Code search/replace    | `ast-grep` MCP            | `grep`, `sed`              |
| GitHub API             | `github` MCP              | `gh` CLI                   |
| Browser automation     | `playwright` MCP          | manual `curl`              |
| Multi-step reasoning   | `sequential-thinking` MCP | unstructured planning      |
| Python lint/type-check | `python-quality` MCP      | manual `ruff`/`pyright`    |
| JS lint/format/spell   | `tooling-lint` MCP        | manual `eslint`/`prettier` |
| Containers             | `mcp-docker` MCP          | `docker` CLI directly      |
| JavaScript execution   | `code-sandbox` MCP        | `node`/`bun` directly      |
| Web content            | `fetch` MCP               | `curl` for web pages       |

---

## 10. Prompt Library Conventions

Prompts live in `.github/prompts/` as `*.prompt.md` files with YAML frontmatter:

```yaml
---
name: prompt-name
title: Prompt Title
description: Brief description of what this prompt does.
version: 1.0.0
author: Hermes Agent
---
```

When updating a prompt, also update its cross-references. Avoid duplicating prompt content — keep one canonical copy and cross-link instead.

---

## 11. Common Tasks

### Start a new feature

```bash
git checkout development && git pull
git checkout -b feat/projectname/description
# Make changes, test
cd projects/projectname
bun run typecheck && bun run lint:strict
git commit -m "feat: description"
git push origin feat/projectname/description
```

### Run checks for a subproject

```bash
cd projects/<name>
bun install --frozen-lockfile
bun run format && bun run typecheck && bun run lint:strict
bun run test -- --grep "pattern"
```

### Debug a failing test

```bash
bun run test -- --grep "test name"      # Run specific test
bun run test -- src/file.test.ts        # Run specific file
```

### Before submitting a PR

```bash
git diff --stat origin/development      # Review scope
bun run format && bun run typecheck && bun run lint:strict && bun run test
git log --oneline origin/development..  # Review commits
```

### Add a new script with dry-run support

1. Create `.sh` implementation with `DRY_RUN_SUPPORT=true` marker
2. Create `.ps1` and `.bat` wrappers with identical CLI interface
3. All wrappers support `--help` and `--dry-run`
4. Add to the appropriate project's `scripts/` directory

---

## 12. Subproject Quick Reference

This workspace contains **18+ subprojects** under `projects/`. Each is autonomous with its own package manager, build system, and test suite. Use this table to quickly find the right commands for each project.

| Project                           | Language/Stack       | Entry Point           | Test Command                      | Notes                                  |
| --------------------------------- | -------------------- | --------------------- | --------------------------------- | -------------------------------------- |
| **Bash/**                         | TS + Bash + PS1      | `src/` scripts        | `bun run test`                    | 6-phase orchestrator, vitest           |
| **Banking/**                      | Next.js 16 + Drizzle | `src/app/`            | `npm run test`                    | Fintech dashboard, npm (NOT bun)       |
| **comicwise/**                    | Next.js 15 + Prisma  | `src/app/`            | `npm run test`                    | Comic storefront, npm                  |
| **ecom/**                         | Django + React       | `backend/manage.py`   | `python manage.py test` (backend) | Dual-stack: Django :8000 + React :3000 |
| **Resume_maker/**                 | Bun/TS               | `index.ts`            | None (script only)                | PDF/MD generator from JSON             |
| **mcp-servers/**                  | Multi-language       | Per-language          | Per-language build                | TS, Python, Go, Java, Rust, etc.       |
| **Python-projects/**              | Python scripts       | Standalone `.py`      | `pytest`                          | 18 beginner-to-intermediate scripts    |
| **Django-Scrapy-Selenium/**       | Python               | Per-usage             | Per-usage                         | Scraping/automation toolkit            |
| **cookiecutter-django-tailwind/** | Django template      | Cookiecutter scaffold | Follow README                     | Project scaffold generator             |
| **rhixe_scans/**                  | Check README         | Check README          | Check README                      | Project-specific                       |
| **rhixecompany-comics/**          | Check README         | Check README          | Check README                      | Project-specific                       |
| **selenium_webdriver/**           | Python/Selenium      | Standalone            | Manual                            | Browser automation scripts             |
| **university-libary-jsm/**        | Check README         | Check README          | Check README                      | Library system                         |
| **xamehi/**                       | Check README         | Check README          | Check README                      | Media project                          |
| **xamehi.tv/**                    | Check README         | Check README          | Check README                      | Media project                          |
| **youtube-downloader/**           | Check README         | Check README          | Check README                      | YouTube tool                           |
| **profile/**                      | Check README         | Check README          | Check README                      | Profile config                         |
| **docs/**                         | Markdown             | N/A                   | N/A                               | Architecture & reference docs          |

### Quick Commands by Project Type

**TypeScript/Bun projects (Bash, Resume_maker):**

```bash
cd projects/Bash
bun install --frozen-lockfile
bun run typecheck && bun run lint:strict
bun run test -- --grep "pattern"
bun run test -- src/file.test.ts
```

**Next.js projects (Banking, comicwise) — use npm, NOT bun:**

```bash
cd projects/Banking
npm install
npm run dev           # Start dev server
npm run build         # Production build
npm run lint          # ESLint
npm run test          # Jest or Vitest
```

**Django/Python projects (ecom backend, Python-projects):**

```bash
cd projects/ecom/backend
pip install -r requirements.txt
python manage.py migrate
python manage.py runserver    # :8000
python manage.py test         # Run tests

# Or for standalone Python projects:
cd projects/Python-projects
pytest --grep "test_name"     # Run specific test
python script_name.py         # Run script directly
```

**Workspace root (primarily Bash/TS orchestration):**

```bash
cd /  # Workspace root
bun install --frozen-lockfile
bun run format && bun run typecheck && bun run lint:strict
bun run test
```

---

## 13. Project-Specific Guidance

### projects/Bash/ (Primary TypeScript Toolkit)

- **Runtime:** Bun 1.3.14+ | **Tests:** Vitest | **Lint:** ESLint flat config (zero-warnings gate)
- **Pattern:** Phase-based orchestration, dry-run everywhere, multi-wrapper parity
- **ORM/Validation:** zod v4, ts-morph for AST transformations

### projects/Resume_maker/ (TypeScript PDF Generator)

- **Runtime:** Bun 1.3.14+ | **Tests:** Vitest
- Generates PDF/TXT/vCard output from structured JSON input

### Python Projects (Django-Scrapy-Selenium, ecom, etc.)

- **Python: 3.11** | **Lint:** Ruff (select E,F,I,N,W,UP,B,SIM,ARG,RUF) | **Type-check:** Pyright basic
- **Format:** Ruff (double quotes, spaces, 120 chars)
- **Test:** pytest 9.0.3

### projects/mcp-servers/ (Multi-Language MCP Servers)

- Contains MCP server implementations in TypeScript, Python, Go, Java, Kotlin, C#, PHP, Ruby, Rust, Swift
- Each has its own `AGENTS.md` for project-specific patterns
