# USER.md Compaction Patterns

When root USER.md exceeds the 2000-byte limit, compact it before syncing to profiles. This reference captures the required schema shape and common compaction strategies.

## Required Schema (validate-memories enforces)

```
---
user: Alexa
---
# USER.md — <profile> profile

Pointer file. Canonical durable rules in MEMORY.md.

## Identity
- Name: Alexa | Workspace: ~/Desktop/SandBox | Profile: <name> | Role: <role>

## Environment Stack
- OS: Windows 11 (MSYS2/git-bash)
- Runtimes: Bun, Python 3.11/3.13 (uv), TypeScript strict
- Tooling: Ruff, Pyright, ESLint, Prettier, Markdownlint
- Execution: Hermes TUI, terminal/process tools

## Model
- <profile_model>

## Execution Preferences  ← MUST be exact heading text
- key:value pairs in bullet list
```

### Validator checks for these exact headings:
- `## Identity` (required)
- `## Model` (required)
- `## Execution Preferences` (required — NOT `## Preferences` or `## Execution`)

## Size limits
- **USER.md**: ≤ 2000 bytes (`wc -c`). Aim for ~900-1500 bytes for profile copies.
- **MEMORY.md**: ≤ 6000 chars (`python3 -c "len(open(path).read())"`).

## Compaction strategy (root USER.md → compact)

| Original content | What to keep in compact version |
|-----------------|--------------------------------|
| `## Communication` (3 bullets) | Fold into `## Execution Preferences` as `Communication: concise bullets, lead with result, skip fluff.` |
| `## Environment Stack` (4 bullets) | Condense to key info: OS, runtimes, tooling, execution method |
| `## Planning Style` (6 bullets) | Shorten to core patterns: milestone-based, arch review at step 0, decomposition pipeline |
| `## Prompting & Generation Preferences` (7 bullets) | Keep only distinctive preferences (MCP+skills pairing, zero-tolerance config errors) |
| `## Custom Skill Utilization` (6 bullets) | Keep only: structured SKILL.md format, local model for preprocessing |
| `## Automation Hooks` (5 bullets) | Keep only: ruff pre-commit, charliermarsh.ruff formatter |
| `## Execution Preferences` (8 bullets) | Keep all — this is the core behavior descriptor |
| `## Canonical Store` (3 items) | Keep concise pointers (MEMORY.md for rules, cookiecutter exclusion) |

## Profile-specific adaptations

| Field | Root | Profile copy |
|-------|------|-------------|
| Heading | `# USER.md — default profile` | `# USER.md — <name> profile` |
| Identity | `Profile: default` | `Profile: <name> \| Role: <role>` |
| Model | `deepseek-v4-flash-free (opencode-zen) [config default]\n- google/gemma-4-31b-it:free (openrouter) [fallback/current]` | Single model line matching `hermes profile list` output |
| Execution prefs | Full list (communication, code, skills, hooks, execution) | Matching subset (profiles inherit the same preferences) |

## Example: root vs alexa profile USER.md

**Root** (compact; 1508 bytes):
```yaml
---
user: Alexa
---
# USER.md — default profile

Pointer file. Canonical durable rules in MEMORY.md.

## Identity
- Name: Alexa | Workspace: ~/Desktop/SandBox | Profile: default

## Environment Stack
- OS: Windows 11 (MSYS2/git-bash)
- Runtimes: Bun, Python 3.11/3.13 (uv), TypeScript strict
- Tooling: Ruff, Pyright, ESLint, Prettier, Markdownlint
- Execution: Hermes TUI, terminal/process tools

## Model
- deepseek-v4-flash-free (opencode-zen) [config default]
- google/gemma-4-31b-it:free (openrouter) [fallback/current]

## Planning Style
- Milestone-based with exit criteria; short incremental plans.
- Architecture Review phase at step 0 of macro-plans.
- Present multi-stage plans as tables (Time, Tool, Failure Mode).
- Decompose: epic → feature → story → test data (hermes-breakdown).

## Execution Preferences
- **Communication**: concise bullets, lead with result, skip fluff.
- **Code**: TypeScript strict, JSDoc/docstring *why* not *what*, pragmatic.
- **Skills**: structured SKILL.md (YAML frontmatter + md body), local models for preprocessing.
- **Hooks**: ruff format+check --fix pre-commit; charliermarsh.ruff formatter.
- **Execution**: read→patch→verify, MCP-first, no backup files (git rollback), full exec no phase-gate pauses, clarify when ambiguous, delegate_task over sequential.

## Canonical Store
- User rules: MEMORY.md
- Cookie-cutter pyproject.toml has Jinja that breaks Ruff's TOML parser → exclude at .ruff.toml root level.
```

**alexa profile** (906 bytes):
```yaml
---
user: Alexa
---
# USER.md — alexa profile

Pointer file. Canonical durable rules in MEMORY.md.

## Identity
- Name: Alexa | Workspace: ~/Desktop/SandBox | Profile: alexa | Role: Operations

## Environment Stack
- OS: Windows 11 (MSYS2/git-bash)
- Runtimes: Bun, Python 3.11/3.13 (uv), TypeScript strict
- Tooling: Ruff, Pyright, ESLint, Prettier, Markdownlint
- Execution: Hermes TUI, terminal/process tools

## Model
- google/gemma-4-31b-it:free (openrouter)

## Execution Preferences
- Communication: concise bullets, lead with result.
- Code: TypeScript strict, JSDoc/docstring *why* not *what*, pragmatic.
- Skills: structured SKILL.md (YAML frontmatter + md body).
- Hooks: ruff format+check --fix pre-commit; charliermarsh.ruff formatter.
- Execution: read→patch→verify, MCP-first, no backup files, full exec, clarify when ambiguous, delegate_task over sequential.
```

Key differences:
- Profile gets single model line, not fallback chain
- Profile adds `| Role:` to Identity line
- Profile drops Planning Style and Canonical Store sections (those are root-specific)
- Model differs: profile uses its assigned model, root shows default + fallback
