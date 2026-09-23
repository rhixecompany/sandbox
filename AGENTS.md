# AGENTS.md — SandBox Agent Context

**Canonical workspace context**: this file. Tool-specific adapters must defer here rather than copy rules.
**Workspace**: `C:\Users\Alexa\Desktop\SandBox`. **Repo**: `rhixecompany/sandbox`. Polyglot monorepo — 17+ subprojects (`projects/*`), each autonomous.

Subagent identity: ops/adminbot. Plan: `./plans/multi-goal-execution-plan-2026-09-14.md`. Branch: `clean-development`.

## Verified Honcho Peer Card

| Field             | Verified Value                                 |
| ----------------- | ---------------------------------------------- |
| User              | Alexa                                          |
| Active profile(s) | adminbot + patient-tutor                       |
| Workspace         | `~/Desktop/SandBox`                            |
| Authorization     | FULL                                           |
| Model (primary)   | `deepseek/deepseek-v4-flash-0731` (openrouter) |
| Fallback          | `deepseek-v4-flash-free`                       |
| Workspace branch  | clean-development (ahead 4 behind 0)           |
| Repo              | rhixecompany/sandbox                           |

Preferences (DRY — reference, don't duplicate):

- Concise / direct / table-first / action-first — see `/user-communication-preferences` SKILL.md.
- DRY enforcement — see `.hermes.md` + `/multi-file-change-protocol` SKILL.md.
- Verification-first — see `/systematic-debugging` SKILL.md (4-phase).
- Never synthetic IDs / never expose `.env`.

## Session Evidence (Verified — Preserved)

| Evidence               | Value / Status                                                          |
| ---------------------- | ----------------------------------------------------------------------- |
| Skills verified        | 28 (plan 11673 B)                                                       |
| Vulnerability findings | 26 (preserved, not hidden)                                              |
| Parsing errors (arch)  | 41 (`DEBUG_FIX_EVIDENCE_2026-09-13.md`)                                 |
| `.eslintrc.json`       | 69 B verified                                                           |
| Rate limit 403         | Preserved                                                               |
| MSYS2 FAIL             | Preserved (environment blocker)                                         |
| adminbot MISSING       | Preserved                                                               |
| `.env` size (CWD)      | 5274 B (unchanged — protected)                                          |
| `.env` size (hermes)   | 30504 B (unchanged — protected)                                         |
| Profile routing        | 15 registered (live 2026-09-20); adminbot gap preserved                 |
| Subagent execution     | `deleg_d3d36082` COMPLETE (511.2s, 37 api_calls)                        |
| Skill judgment gates   | specs-judge ~97 / plans-judge ~96 / prompts-judge ~98 / skill-judge ~97 |

## Agent Commands (Exact — From Repo)

Run from workspace root (`C:/Users/Alexa/Desktop/SandBox`):

```bash
# Setup
bun install                 # root TypeScript dependencies
python -m venv venv
source venv/Scripts/activate   # Windows; or venv/bin/activate (Linux/macOS)
pip install -r requirements.txt

# Root quality gate (exact commands from package.json + .husky/pre-commit)
bun run lint                 # eslint . --no-error-on-unmatched-pattern
bun run lint:fix             # eslint . --fix
bun run format               # prettier --write .
bun run format:check         # prettier --check --ignore-unknown .
bun run markdownlint         # markdownlint-cli2 (uses .markdownlint-cli2.jsonc)
bun run spellcheck           # DISABLED in package.json (# cspell disabled)
bun run typecheck            # tsc --noEmit
bun run check                # full gate: lint + format:check + markdownlint + spellcheck

# Python checks
ruff check .                 # lint (line-length 120, select E/F/I/B/N/W/UP/B/SIM/ARG/RUF)
pyright                      # type check (pythonVersion 3.11, Windows platform)
pytest                       # test (testpaths = ["projects"], -q --tb=short)

# Per-subproject (each has its own AGENTS.md / package.json / CI)
# Example — Bash project:
cd projects/Bash
bun install
bun run lint:strict         # max-warnings=0
bun run test                 # vitest run
```

## Agent Integration Contract

All supported agents use the same source of truth:

| Agent                   | Adapter                                  | Required behavior                                                                                   |
| ----------------------- | ---------------------------------------- | --------------------------------------------------------------------------------------------------- |
| GitHub Copilot          | `.github/copilot-instructions.md`        | Read this file before repository-wide work; read the nearest subproject `AGENTS.md` before app work |
| Hermes                  | `.hermes.md`                             | Apply profile routing and Hermes-only overrides without duplicating workspace rules                 |
| OpenCode                | `AGENTS.md` discovery                    | Use this file from the repository root; do not invent a second root prompt or config schema         |
| Cursor Agent            | `.cursorrules` and `.cursor/rules/*.mdc` | Treat this file as canonical and use scoped rules when present                                      |
| — SandBox Agent Context |

**Canonical workspace context**: this file. Tool-specific adapters must defer here rather than copy rules.
**Workspace**: `C:\Users\Alexa\Desktop\SandBox`. **Repo**: `rhixecompany/sandbox`. Polyglot monorepo — 17+ subprojects (`projects/*`), each autonomous.

Subagent identity: ops/adminbot. Plan: `./plans/multi-goal-execution-plan-2026-09-14.md`. Branch: `clean-development`.

## Verified Honcho Peer Card

| Field             | Verified Value                                 |
| ----------------- | ---------------------------------------------- |
| User              | Alexa                                          |
| Active profile(s) | adminbot + patient-tutor                       |
| Workspace         | `~/Desktop/SandBox`                            |
| Authorization     | FULL                                           |
| Model (primary)   | `deepseek/deepseek-v4-flash-0731` (openrouter) |
| Fallback          | `deepseek-v4-flash-free`                       |
| Workspace branch  | clean-development (ahead 4 behind 0)           |
| Repo              | rhixecompany/sandbox                           |

Preferences (DRY — reference, don't duplicate):

- Concise / direct / table-first / action-first — see `/user-communication-preferences` SKILL.md.
- DRY enforcement — see `.hermes.md` + `/multi-file-change-protocol` SKILL.md.
- Verification-first — see `/systematic-debugging` SKILL.md (4-phase).
- Never synthetic IDs / never expose `.env`.

## Session Evidence (Verified — Preserved)

| Evidence               | Value / Status                                                          |
| ---------------------- | ----------------------------------------------------------------------- |
| Skills verified        | 28 (plan 11673 B)                                                       |
| Vulnerability findings | 26 (preserved, not hidden)                                              |
| Parsing errors (arch)  | 41 (`DEBUG_FIX_EVIDENCE_2026-09-13.md`)                                 |
| `.eslintrc.json`       | 69 B verified                                                           |
| Rate limit 403         | Preserved                                                               |
| MSYS2 FAIL             | Preserved (environment blocker)                                         |
| adminbot MISSING       | Preserved                                                               |
| `.env` size (CWD)      | 5274 B (unchanged — protected)                                          |
| `.env` size (hermes)   | 30504 B (unchanged — protected)                                         |
| Profile routing        | 15 registered (live 2026-09-20); adminbot gap preserved                 |
| Subagent execution     | `deleg_d3d36082` COMPLETE (511.2s, 37 api_calls)                        |
| Skill judgment gates   | specs-judge ~97 / plans-judge ~96 / prompts-judge ~98 / skill-judge ~97 |

## Agent Commands (Exact — From Repo)

Run from workspace root (`C:/Users/Alexa/Desktop/SandBox`):

```bash
# Setup
bun install                 # root TypeScript dependencies
python -m venv venv
source venv/Scripts/activate   # Windows; or venv/bin/activate (Linux/macOS)
pip install -r requirements.txt

# Root quality gate (exact commands from package.json + .husky/pre-commit)
bun run lint                 # eslint . --no-error-on-unmatched-pattern
bun run lint:fix             # eslint . --fix
bun run format               # prettier --write .
bun run format:check         # prettier --check --ignore-unknown .
bun run markdownlint         # markdownlint-cli2 (uses .markdownlint-cli2.jsonc)
bun run spellcheck           # DISABLED in package.json (# cspell disabled)
bun run typecheck            # tsc --noEmit
bun run check                # full gate: lint + format:check + markdownlint + spellcheck

# Python checks
ruff check .                 # lint (line-length 120, select E/F/I/B/N/W/UP/B/SIM/ARG/RUF)
pyright                      # type check (pythonVersion 3.11, Windows platform)
pytest                       # test (testpaths = ["projects"], -q --tb=short)

# Per-subproject (each has its own AGENTS.md / package.json / CI)
# Example — Bash project:
cd projects/Bash
bun install
bun run lint:strict         # max-warnings=0
bun run test                 # vitest run
```

## Agent Integration Contract

All supported agents use the same source of truth:

| Agent                                                                                                                                                   | Adapter                                  | Required behavior                                                                                   |
| ------------------------------------------------------------------------------------------------------------------------------------------------------- | ---------------------------------------- | --------------------------------------------------------------------------------------------------- |
| GitHub Copilot                                                                                                                                          | `.github/copilot-instructions.md`        | Read this file before repository-wide work; read the nearest subproject `AGENTS.md` before app work |
| Hermes                                                                                                                                                  | `.hermes.md`                             | Apply profile routing and Hermes-only overrides without duplicating workspace rules                 |
| OpenCode                                                                                                                                                | `AGENTS.md` discovery                    | Use this file from the repository root; do not invent a second root prompt or config schema         |
| Cursor Agent                                                                                                                                            | `.cursorrules` and `.cursor/rules/*.mdc` | Treat this file as canonical and use scoped rules when present                                      |
| workspace context**: this file. Tool-specific adapters must defer here rather than copy rules.                                                          |
| **Workspace**: `C:\Users\Alexa\Desktop\SandBox`. **Repo**: `rhixecompany/sandbox`. Polyglot monorepo — 17+ subprojects (`projects/*`), each autonomous. |

Subagent identity: ops/adminbot. Plan: `./plans/multi-goal-execution-plan-2026-09-14.md`. Branch: `clean-development`.

## Verified Honcho Peer Card

| Field             | Verified Value                                 |
| ----------------- | ---------------------------------------------- |
| User              | Alexa                                          |
| Active profile(s) | adminbot + patient-tutor                       |
| Workspace         | `~/Desktop/SandBox`                            |
| Authorization     | FULL                                           |
| Model (primary)   | `deepseek/deepseek-v4-flash-0731` (openrouter) |
| Fallback          | `deepseek-v4-flash-free`                       |
| Workspace branch  | clean-development (ahead 4 behind 0)           |
| Repo              | rhixecompany/sandbox                           |

Preferences (DRY — reference, don't duplicate):

- Concise / direct / table-first / action-first — see `/user-communication-preferences` SKILL.md.
- DRY enforcement — see `.hermes.md` + `/multi-file-change-protocol` SKILL.md.
- Verification-first — see `/systematic-debugging` SKILL.md (4-phase).
- Never synthetic IDs / never expose `.env`.

## Session Evidence (Verified — Preserved)

| Evidence               | Value / Status                                                          |
| ---------------------- | ----------------------------------------------------------------------- |
| Skills verified        | 28 (plan 11673 B)                                                       |
| Vulnerability findings | 26 (preserved, not hidden)                                              |
| Parsing errors (arch)  | 41 (`DEBUG_FIX_EVIDENCE_2026-09-13.md`)                                 |
| `.eslintrc.json`       | 69 B verified                                                           |
| Rate limit 403         | Preserved                                                               |
| MSYS2 FAIL             | Preserved (environment blocker)                                         |
| adminbot MISSING       | Preserved                                                               |
| `.env` size (CWD)      | 5274 B (unchanged — protected)                                          |
| `.env` size (hermes)   | 30504 B (unchanged — protected)                                         |
| Profile routing        | 15 registered (live 2026-09-20); adminbot gap preserved                 |
| Subagent execution     | `deleg_d3d36082` COMPLETE (511.2s, 37 api_calls)                        |
| Skill judgment gates   | specs-judge ~97 / plans-judge ~96 / prompts-judge ~98 / skill-judge ~97 |

## Agent Commands (Exact — From Repo)

Run from workspace root (`C:/Users/Alexa/Desktop/SandBox`):

```bash
# Setup
bun install                 # root TypeScript dependencies
python -m venv venv
source venv/Scripts/activate   # Windows; or venv/bin/activate (Linux/macOS)
pip install -r requirements.txt

# Root quality gate (exact commands from package.json + .husky/pre-commit)
bun run lint                 # eslint . --no-error-on-unmatched-pattern
bun run lint:fix             # eslint . --fix
bun run format               # prettier --write .
bun run format:check         # prettier --check --ignore-unknown .
bun run markdownlint         # markdownlint-cli2 (uses .markdownlint-cli2.jsonc)
bun run spellcheck           # DISABLED in package.json (# cspell disabled)
bun run typecheck            # tsc --noEmit
bun run check                # full gate: lint + format:check + markdownlint + spellcheck

# Python checks
ruff check .                 # lint (line-length 120, select E/F/I/B/N/W/UP/B/SIM/ARG/RUF)
pyright                      # type check (pythonVersion 3.11, Windows platform)
pytest                       # test (testpaths = ["projects"], -q --tb=short)

# Per-subproject (each has its own AGENTS.md / package.json / CI)
# Example — Bash project:
cd projects/Bash
bun install
bun run lint:strict         # max-warnings=0
bun run test                 # vitest run
```

## Agent Integration Contract

All supported agents use the same source of truth:

| Agent          | Adapter                                  | Required behavior                                                                                   |
| -------------- | ---------------------------------------- | --------------------------------------------------------------------------------------------------- |
| GitHub Copilot | `.github/copilot-instructions.md`        | Read this file before repository-wide work; read the nearest subproject `AGENTS.md` before app work |
| Hermes         | `.hermes.md`                             | Apply profile routing and Hermes-only overrides without duplicating workspace rules                 |
| OpenCode       | `AGENTS.md` discovery                    | Use this file from the repository root; do not invent a second root prompt or config schema         |
| Cursor Agent   | `.cursorrules` and `.cursor/rules/*.mdc` | Treat this file as canonical and use scoped rules when present                                      |
