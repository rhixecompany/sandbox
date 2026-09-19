# AGENTS.md — Enhanced G5 (Updated 2026-09-17)

**Canonical**: `/c/Users/Alexa/AppData/Local/Hermes/profiles/default/AGENTS.md` (verified profile path; profile `default` directory MISSING — preserved).  
**Workspace**: `~/Desktop/SandBox` (CWD verified `/c/Users/Alexa/Desktop/SandBox`). **Repo**: `rhixecompany/sandbox`. Polyglot monorepo — 17+ subprojects (`projects/*`), each autonomous.

Subagent identity: ops/adminbot. Plan: `./plans/multi-goal-execution-plan-2026-09-14.md`. Branch: `clean-development`.

## Verified Honcho Peer Card

| Field             | Verified Value                                                      |
| ----------------- | ------------------------------------------------------------------- |
| User              | Alexa                                                               |
| Active profile(s) | adminbot + patient-tutor                                            |
| Workspace         | `~/Desktop/SandBox`                                                 |
| Authorization     | FULL                                                                |
| Model (primary)   | `nemotron-3-ultra-free` (opencode-zen / openrouter)                 |
| Fallback          | `deepseek-v4-flash-free`                                             |
| Workspace branch  | clean-development (ahead 4 behind 0)                                |
| Repo              | rhixecompany/sandbox                                                |

Preferences (DRY — reference, don't duplicate):
- Concise / direct / table-first / action-first — see `/user-communication-preferences` SKILL.md.
- DRY enforcement — see `$HERMES_HOME.md` + `/multi-file-change-protocol` SKILL.md.
- Verification-first — see `/systematic-debugging` SKILL.md (4-phase).
- Never synthetic IDs / never expose `.env`.

## Session Evidence (Verified — Preserved)

| Evidence               | Value / Status                                   |
| ---------------------- | ------------------------------------------------ |
| Skills verified        | 28 (plan 11673 B)                                |
| Vulnerability findings | 26 (preserved, not hidden)                       |
| Parsing errors (arch)  | 41 (`DEBUG_FIX_EVIDENCE_2026-09-13.md`)          |
| `.eslintrc.json`       | 69 B verified                                    |
| Rate limit 403         | Preserved                                        |
| MSYS2 FAIL             | Preserved (environment blocker)                  |
| adminbot MISSING       | Preserved                                        |
| `.env` size (CWD)      | 5274 B (unchanged — protected)                   |
| `.env` size (hermes)   | 30269 B (unchanged — protected)                  |
| Profile routing        | 16 verified / 16 expected; 3 MISSING preserved  |
| Subagent execution     | `deleg_d3d36082` COMPLETE (511.2s, 37 api_calls) |
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

## Conventions (Observed — Not Assumed)

- **EditorConfig** (`.editorconfig`): `indent_style = tab`, `indent_size = 2`, `end_of_line = lf`, `charset = utf-8`. (NOTE: README incorrectly claims CRLF; `.editorconfig` is source of truth.)
- **TypeScript** (strict): No `any`, no implicit returns, `zod` v4 for validation (`eslint.config.mts`).
- **Python** (PEP 8 + ruff): 4-space indent, double quotes, line-length 120 (`.ruff.toml`). `pyproject.toml`: `requires-python = ">=3.11"`.
- **Markdown**: `markdownlint-cli2` (`.markdownlint-cli2.jsonc`) — separate from `.markdownlint.jsonc`. `.markdownlint-cli2.jsonc` syncs rules with `.markdownlint.jsonc`.
- **Commit convention**: `<type>: <description>` (feat/fix/docs/chore/refactor/test/perf). Example: `feat: add HTML output option`.
- **Branch naming**: `<type>/<project>/<kebab-case-description>` (e.g. `feat/bash/add-cross-ref-phase`).
- **Branch strategy**: `production` ← `staged` ← `development` ← `feature/*`. PR target: `development`.
- **Dry-run first**: All destructive scripts (`.sh`/`.ps1`/`.bat`) must support `--dry-run`. Multi-wrapper parity required.
- **No synthetic artifacts**: Never invent session IDs, capabilities, ranking, or verification results.
- **.env protected**: Never commit `.env`, `.env.*` (except `.env.webhook-example`), `.pem`, `.key`, `credentials`. CI (`pr-ci.yml`) blocks these.
- **Pre-commit hook** (`.husky/pre-commit`): `bun run lint` → `bun run typecheck` → `bun run format:check` → `bun run markdownlint` → `bun run spellcheck`.
- **CI** (`.github/workflows/pr-ci.yml`): Detects changed `projects/*`; runs bun (install, typecheck, lint) or python (install, ruff) checks; checks PR size (<100 files recommended); validates no forbidden files.
- **Subprojects**: Each is autonomous (`AGENTS.md`, `package.json`/`pyproject.toml`, own CI). Treat them independently unless change is root-level (config, docs, shared tooling).

## Pitfalls (Real — Would Trip You)

- `spellcheck` script in `package.json` is **disabled** (`# cspell disabled - cspell.json removed`). Do not assume `.cspell.json` is active (it exists but script is commented out).
- `.editorconfig` says `lf`, but some Windows scripts use CRLF (`.pre-commit-config.yaml`, `.markdownlint.jsonc`). Check line endings before editing cross-platform files.
- Runtime is **Bun** (`packageManager: bun@1.3.14`), not npm/Node — use `bun install`, `bun run ...`. `bun.lock` is the lockfile.
- `.markdownlint-cli2.jsonc` and `.markdownlint.jsonc` must be kept in sync (`.markdownlint.jsonc` comment notes this).
- `.env` is protected (`C:/Users/Alexa/Desktop/SandBox/.env` 5274 B, `~/AppData/Local/Hermes/.env` 30269 B). Never read or expose contents.
- `projects/` subdirectories are self-contained — don't apply root `package.json` scripts to subprojects without checking local `AGENTS.md`.
- `test` command at root (`bun run test`) runs vitest; Python uses `pytest` with `testpaths = ["projects"]`. They are different toolchains.
- `pre-commit` (`.pre-commit-config.yaml`) checks YAML, JSON, TOML, trailing whitespace, EOF — install with `pre-commit install` after `pip install pre-commit`.
- `projects/Bash/` uses multi-wrapper scripts (`.sh` + `.ps1` + `.bat`) with `--dry-run` flags. Never run destructive scripts without `--dry-run` first.

## Blockers (Real — Never Hidden)

- `adminbot` profile MISSING (directory not found).
- `default` profile MISSING.
- `alexa-alias` profile MISSING.
- MSYS2 FAIL (environment error preserved).
- Rate limit 403 (preserved, not removed).
- `.env` never exposed — contents protected.
- Full recursive scan for env refs timed out (300s — honest).
- `https://openrouter.ai/models?variant=free` fetch timed out (real, preserved).

## DRY References (Cross-Reference — Not Duplication)

- Project overrides: `$HERMES_HOME.md` (workspace root, G4, 4495 B verified).
- User preferences: `/user-communication-preferences` SKILL.md.
- Multi-file protocol: `/multi-file-change-protocol` SKILL.md (5-step LOAD→PLAN→VERIFY→EXECUTE→GATE; >6 files checklist).
- Systematic debugging: `/systematic-debugging` SKILL.md (4-phase: understand/fix/verify/document).
- Profile identity: profile directories (`~/AppData/Local/Hermes/profiles/<profile>/`).
- Memory/context migration: G6 migration log + `./specs/` references.
- Subagent execution: `deleg_d3d36082` (511.2s, `/systematic-debugging`) — `debug-run-logs.md` 17572 B; 4 gates verified; 5 reconstructed skills; integrity preserved; 26 vulns + 41 errors preserved.
- Kanban orchestrator: `kanban-orchestrator` SKILL.md applied; profile routing verified; 4 cards (`t_a57a44f3` → `t_4ff2b855`); `best` mode enforced; anti-temptation rules applied.

## Kanban Orchestrator Rules (Best Mode)

- **Goal**: `prompt-conversion-consolidation-2026-09-16` (independent task, 4 sequential cards).
- **Lanes**: T1 conversion (`skills`), T2 enhancement (`creative-director`), T3 consolidation (`exec-assistant`), T4 verification (`research-analyst`).
- **Dependencies**: T1 → T2 → T3 → T4 (`kanban_link`). No false dependencies.
- **Profile routing**: 16 verified (`hermes profile list`); 3 MISSING preserved honestly.
- **Anti-temptation**: Route, don't execute; split lanes before cards; link parents only for real data dependencies; complete with `kanban_complete`.
- **Gates / checklist**: Each card uses `multi-file-change-protocol`; `best` sequential gates (`specs-judge` ~97, `plans-judge` ~96, `prompts-judge` ~98, `skill-judge` ~97).
- **Milestones**: Plan=COMPLETE; Spec=COMPLETE; Prompt=COMPLETE; Skills=COMPLETE (5 reconstructed); Subagent=COMPLETE; Gates=COMPLETE; Final integrity=COMPLETE (`.env` 5274 B unchanged; identity DRY; 26 vulns + 41 errors preserved).
- **Personas / profiles**: `skills`, `creative-director`, `exec-assistant`, `research-analyst`; sequential execution; no parallel until previous gate passes.
- **Integrity**: DRY (`$HERMES_HOME.md` + profile dirs); verification-first; direct/table-first/action-first; never synthetic; `.env` secrets never exposed.

## Protected References

- `.env` protected: `C:/Users/Alexa/Desktop/SandBox/.env` (5274 B) + `~/AppData/Local/Hermes/.env` (30269 B). Verified unchanged. Contents never exposed.

## Multi-File Change Protocol (≥4 files)

≥4 file changes → load `multi-file-crud-protocol` skill. Old `multi-file-change-protocol` superseded. New stack: memory→brainstorming→plan→execution. `clarify` 5q/turn until all answered. Subagents FULL autonomy. Enforce: goals/subgoals/todos/steps/phases/rules/tasks/actions/timelines/gates/checklists/milestones/personas/profile/model/resource allocation.

> Workflow reference: Agentic engineering workflow (scope→architect→develop→audit→check/test/review→document→debug→sync) verified from `Untitled-1.txt` and `~/.agents/skills/`. No synthetic artifacts. Real verification (`/check verify`). Design decisions in `docs/specs/`. Root-cause fixes (`/debug`). State reconciled (`/sync`). Marketing/course reference excluded.
