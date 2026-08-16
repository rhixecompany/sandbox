---
name: tooling-implementation
title: "Workspace Tooling Implementation (python-quality + tooling-lint + tooling-config)"
description: "Tooling stack: ruff, eslint, prettier, cspell workspace."
version: 1.1.0
author: Hermes Agent
license: MIT
tags: [tooling, ruff, pyright, eslint, prettier, cspell, markdownlint, pre-commit, git-cliff, mcp, workspace]
---

# Workspace Tooling Implementation

## Overview

Umbrella workflow for fully implementing and validating the three Hermes tooling MCP stacks across a workspace root and all subrepos:
`python-quality` (ruff/pyright), `tooling-lint` (eslint/prettier/cspell/markdownlint), `tooling-config` (gitignore/editorconfig/pre-commit/git-cliff).

## When to Use

- User asks to "implement fully" / "debug, fix, validate" the tooling stack on `./` and subrepos
- Setting up or repairing repo hygiene configs at scale (10+ repos)
- After MCP server or config changes, running the full check sweep
- Packaging a reproducible tooling workflow (plan + prompt + scripts)

## Workflow

### Phase 0 — Inventory (truth before action)
- Verify config matrix on disk: `find projects -maxdepth 2 -name <config>` per type; check root configs exist
- Confirm MCP servers present: git source in `.github/scripts/*_mcp_server.py`; RUNTIME copies (what config.yaml `mcp_servers` points at) live in `~/AppData/Local/hermes/scripts/`. Sync direction: repo → hermes/scripts; after editing a server, re-copy to hermes/scripts and kill python.exe so the gateway respawns the new path
- Record debt baseline from the verifier output

### Phase 1 — Init (scaffold missing configs)
- Use MCP init tools per repo type (only where the file is missing — never overwrite customized configs):
  - `python_quality.python_init_config` → `.ruff.toml` + `pyrightconfig.json`
  - `tooling_lint.eslint_init` / `prettier_init` / `cspell_init` → flat configs
  - `tooling_config.gitignore_init` / `editorconfig_init` / `precommit_init` / `changelog_init`
- Canonical `.ruff.toml`: target-version py311, line-length 120, select E/F/I/N/W/UP/B/SIM/ARG/RUF, ignore E501/N818, format double/space/lf; exclude node_modules, myvenv, .venv, .git, __pycache__, build/dist
- Root prettier must ignore `projects/` (submodules own their own formatting)
- Root ruff/cspell must exclude `hermes-profiles/` + generated dirs

### Phase 2 — Check (run every checker)
- `.github/scripts/tooling_full_check.py` (per-repo verifier; runtime copy at `~/AppData/Local/hermes/scripts/tooling_full_check.py`) or MCP `*_check` tools
- CLI fallbacks: `ruff check .`, `ruff format --check .`, `eslint .`, `npx prettier --check .`, `cspell lint "**/*"`, `markdownlint-cli2 --config .markdownlintrc.json "**/*.md"`, `pre-commit validate-config`

### Phase 3 — Fix (safe subset; report curated)
- FIX: `ruff check --fix` safe fixes; `prettier --write` (exclude curated dirs via .prettierignore); real undefined-name bugs (F821); config bugs (invalid UTF-8, wrong filenames)
- REPORT: non-fixable lint debt, pyright errors, markdownlint findings in curated prompt libraries, cspell domain terms

### Phase 4 — Validate & report
- Re-run verifier, record before/after counts
- Write artifact with per-phase findings + verification table
- Respawn patched MCP servers (kill python.exe processes; gateway respawns on next call)

## Pitfalls

| Pitfall | Severity | Mitigation |
|---------|----------|------------|
| Generated `.ruff.toml` with byte 0x97 (cp1252 em-dash, invalid UTF-8) breaks ALL repos | High | Write one canonical file, copy to all repos; verify `file .ruff.toml` says ASCII/UTF-8 |
| MCP `subprocess.run(capture_output=True)` deadlocks with node CLIs under the gateway (pipe inheritance) | High | Capture via temp files + `CREATE_NO_WINDOW` + `stdin=DEVNULL`; augment PATH with `C:\nvm4w\nodejs` + `%APPDATA%\npm` |
| cspell v10: `check` is file-only; `--no-progress` removed | High | Use `cspell lint "**/*"` |
| Markdownlint config must be named `.markdownlintrc.json` (server hardcodes it) | High | Don't rely on `.jsonc` copy |
| eslint flat config without `ignores` walks submodules → fails on foreign TS configs | High | Add `ignores: ["node_modules/**", ".next/**", "dist/**", "projects/**"]` |
| bun `add -d` updates package.json but not node_modules | Med | Run `bun install` after; npm repos may need `--legacy-peer-deps` |
| Prettier reformats curated/analysis dirs (large diffs, format damage) | Med | Exclude curated dirs (e.g. `.github/prompts`) in `.prettierignore`; review counts |
| Skill descriptions over 60 chars rejected | Med | Keep `description:` ≤60 chars |
| Ruff `.ruff.toml` exclude globs brace-expand: `{{cookiecutter.project_slug}}/` does NOT match the Jinja dir → ruff exit 2 parsing template `pyproject.toml` | High | Use brace-free pattern `*cookiecutter*` |
| Prettier exit 2 = parse error, not formatting debt (Django `templates/*.html` with Jinja, invalid JSON reports) | High | Add offending paths to `.prettierignore` (`**/templates/`, `docs/reports/`) |
| Global eslint 10.x shadows repo-local 9.x → `eslint-config-next`/FlatCompat configs hard-fail | High | Run via `./node_modules/.bin/eslint`; verifiers should prefer repo-local `node_modules/.bin` |
| `npm config omit=dev` set globally → `npm install`/`ci` skip devDependencies silently | High | Use `npm ci --include=dev`; add `--ignore-scripts` when postinstall fails headless |
| FlatConfig rejects top-level `parserOptions`; typed linting needs `languageOptions.parserOptions` scoped to `**/*.{ts,tsx}` + a `**/*.config.{js,mjs,cjs}` override with `project: false` and typed rules off | High | Follow the scoped-block pattern; migrate legacy `.eslintignore` into `ignores:` and delete the file |
| `log_debug` used but not imported from `lib` (hook F821); pyright false-positive on sys.path-injected lib | Med | Add import; trust `ruff check --select F821` |
| `cspell.json` `words` empty → hundreds of unknown-word findings | Med | Seed from `cspell lint --no-progress .` unknown-word frequency; add workspace/domain terms (incl. intentional repo-name spellings) |

## Verification Checklist

- [ ] Every repo has its full applicable config set (validated on disk)
- [ ] `tooling_full_check.py` completes for every repo (no tooling-level failure)
- [ ] Per-repo report written with before/after counts
- [ ] All SKILL.md + prompt frontmatter parse via `yaml.safe_load`
- [ ] Curated/analysis debt is REPORTED with disposition, not blindly rewritten
- [ ] Plan marked `status: completed` with verification table

## Related Skills

| Skill | Purpose |
|-------|---------|
| `python-quality` | Ruff + pyright workflow |
| `tooling-lint` | ESLint/Prettier/CSpell/Markdownlint |
| `tooling-config` | gitignore/editorconfig/pre-commit/git-cliff |
| `executing-plans` | Execute the plan with checkpoints |
| `executing-prompt-workflows` | Execute the workflow prompt |
| `repo-planning` | Per-repo PLAN.md/SPEC.md generation before tooling work |

## Best Practices

1. **Prepare before executing**: Ensure all prerequisites and dependencies are in place
2. **Validate inputs**: Check configuration, parameters, and environment before running
3. **Handle errors gracefully**: Implement proper error handling and recovery
4. **Document results**: Keep records of what was done, what worked, and what didn't
5. **Clean up**: Remove temporary files, release resources after completion
