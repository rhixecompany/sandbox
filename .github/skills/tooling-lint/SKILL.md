---
name: tooling-lint
title: "JS/TS & Markdown Linting: ESLint, Prettier, CSpell, Markdownlint"
description: "Use to lint JS/TS/Markdown with ESLint, Prettier, CSpell."
version: 1.0.0
author: "Hermes Agent"
tags: [eslint, prettier, cspell, markdownlint, javascript, typescript, linting, mcp]
license: MIT
---
# JS/TS & Markdown Linting (tooling-lint)

## Overview

Standardized workflow for JavaScript/TypeScript/Markdown quality: linting (ESLint), formatting (Prettier), spellchecking (CSpell), and Markdown linting. Integrates with the **`tooling-lint` MCP server**.

## When to Use

- Setting up JS/TS linting, formatting, or spellcheck in a new/existing project
- Running ESLint/Prettier/CSpell/Markdownlint checks before commits
- Fixing ESLint rule violations or formatting drift
- Adding spellcheck dictionaries for domain terms

## Quick Reference

| Tool | MCP Tool | Purpose |
|------|----------|---------|
| ESLint | `eslint_check` / `eslint_init` | Lint JS/TS (flat config `eslint.config.mjs`) |
| Prettier | `prettier_check` / `prettier_init` | Format check/apply (`.prettierrc.json`) |
| CSpell | `cspell_check` / `cspell_init` | Spellcheck (`cspell.json`) |
| Markdownlint | `markdownlint_check` | Lint Markdown (**`.markdownlint-cli2.jsonc`** with `{ "config": {...} }` wrapper — CLI2 rejects `.markdownlintrc.json` as a config name) |
| Mypy | `mypy_check` | Typecheck Python (`--no-error-summary`), resolves from PATH, repo `node_modules/.bin`, or `.venv` |

### CLI Equivalents

```bash
eslint .                          # lint
npx prettier --check .            # format check
npx prettier --write .            # format apply
cspell "**/*.{js,ts,jsx,tsx,md}"  # spellcheck
markdownlint-cli2 "**/*.md"       # markdown lint (if installed)
```

## 1. INIT — Scaffold Configs

- `eslint_init(project_root=...)` → creates `eslint.config.mjs` (flat config, recommended JS/TS).
- `prettier_init(project_root=...)` → creates `.prettierrc.json` (2-space, double quotes, lf).
- `cspell_init(project_root=...)` → creates `cspell.json` (basic config).
- Markdownlint has **no init tool** — create `.markdownlint-cli2.jsonc` manually. CLI2 only accepts CLI2-style names (`.markdownlint-cli2.jsonc`); it REJECTS `.markdownlintrc.json` as a config name (exit 2 crash). markdownlint-cli2 v0.19 also auto-discovers legacy `.markdownlint.jsonc` with HIGHER priority — keep all markdownlint configs aligned:

```jsonc
{
  "config": {
    "MD001": false,          // heading level increments (prompts jump levels)
    "MD003": false,          // heading style (mixed ## and ### is fine)
    "MD007": { "indent": 4 },
    "MD013": false,          // line length (prompts/docs get long)
    "MD024": false,          // duplicate headings (allowed in sections)
    "MD025": false,          // multiple top-level headings (prompt sections)
    "MD026": false,          // trailing punctuation in headings ("?")
    "MD033": false,          // inline HTML (badges/tables)
    "MD036": false,          // emphasis used as heading
    "MD040": false,          // fenced code without language (plain-output blocks)
    "MD041": false,          // first-line heading (files start with frontmatter)
    "MD060": false           // table column style (new strict rule, noise)
  }
}
```

- Mypy: run `mypy_check(path=".", project_root=...)`. No init tool — mypy reads `mypy.ini`/`pyproject.toml`/`setup.cfg`; install via `uv pip install mypy` or rely on `.venv`.

Only run inits where the file is missing — never overwrite a customized config blindly.

## 2. USE — Run Checks

```bash
eslint .                          # lint all
npx prettier --check .            # format check
cspell "**/*"                     # spellcheck
markdownlint-cli2 "**/*.md"       # markdown lint
mypy .                            # python typecheck
```

MCP equivalent: `eslint_check(project_root=...)`, `prettier_check(project_root=...)`, `cspell_check(project_root=...)`, `markdownlint_check(project_root=...)`, `mypy_check(project_root=...)`.

## 3. FIX — Remediate

```bash
npx prettier --write .            # apply formatting
eslint . --fix                    # auto-fix lint issues
cspell --words-add <word> --words-file .cspell-words.txt  # add dictionary words
```

Review auto-fixes; prefer targeted edits over `--fix` for semantic rules.

## 4. Pitfalls

| Pitfall | Severity | Mitigation |
|---------|----------|------------|
| ESLint 10 flat config ignores — must be inside `eslint.config.mjs` | High | Add `ignores: ["node_modules/**", ".next/**", "dist/**", "projects/**"]` — without it ESLint walks submodules and fails on foreign TS configs |
| Running ESLint without `node_modules` installed fails | High | `npm install` / `bun install` first (bun `add -d` does NOT materialize node_modules — run `bun install` after) |
| CSpell v10: `check` is file-only, `--no-progress` removed | High | Use `cspell lint "**/*"` (globs); bare `cspell check .` errors "File not found" |
| MCP server hangs 60-120s on node CLIs (Windows) | High | `capture_output` deadlocks when the gateway spawns node children — `_run` must capture via temp files + `CREATE_NO_WINDOW` + `stdin=DEVNULL`, and prepend `C:\nvm4w\nodejs` + `%APPDATA%\npm` to PATH |
| CSpell false positives on domain terms (comic names, fintech jargon) | Medium | Add to `words` in `cspell.json` |
| Prettier reformats whole repo on first run (large diff) | Medium | Run `prettier --check` first; apply in focused commits |
| Markdownlint MD013/MD024 on long docs | Medium | Disable per-project in `.markdownlintrc.json` |
| Root prettier descends into submodules → server timeout | Medium | Add `projects/` to root `.prettierignore`; each submodule owns its own formatting |
| markdownlint-cli2 rejects `.markdownlintrc.json` as config name (exit 2) | High | Use `.markdownlint-cli2.jsonc` with `{ "config": {...} }`; CLI2 v0.19 auto-discovers legacy `.markdownlint.jsonc` first — keep all markdownlint configs identical |
| Markdownlint MD060 (table column style) floods on existing tables | Medium | New strict rule (0.39) — disable MD060 for prompt/docs-heavy repos |
| Mypy not on PATH (no global install) | Medium | `_find_tool` falls back to repo `node_modules/.bin` then `.venv/Scripts/mypy`; install with `uv pip install mypy` |
| Local tools not on global PATH | Medium | `_find_tool` checks `node_modules/.bin` in project root before failing — run `bun install`/`npm install` first |
| Windows: global eslint/prettier may need `.cmd` in subprocess | Low | Use npx or full path `eslint.cmd` |

## 5. Verification Checklist

- [ ] `eslint.config.mjs` exists (JS/TS projects) with ignores
- [ ] `.prettierrc.json` exists
- [ ] `cspell.json` exists
- [ ] `.markdownlint.jsonc` exists (markdown-heavy repos)
- [ ] `eslint_check` exits clean
- [ ] `prettier_check` exits clean (or formatting applied)
- [ ] `cspell_check` exits clean (or words added)
- [ ] `markdownlint_check` exits clean
- [ ] `mypy_check` exits clean (or documented ignores)

## Related Skills

| Skill | Purpose |
|-------|---------|
| `devops/tooling-implementation` | Umbrella: full tooling stack workspace-wide |
| `software-development/python-quality` | Python lint/format/typecheck workflow |
| `devops/tooling-config` | Repo hygiene: gitignore/editorconfig/pre-commit/changelog |
| `qa/polyglot-test-agent` | Test generation |

## Verification Checklist

- [ ] Prerequisites and environment are properly configured
- [ ] "JS/TS & Markdown Linting: ESLint, Prettier, CSpell, Markdownlint" operations completed successfully
- [ ] Output meets expected quality and requirements
- [ ] Any errors during execution were resolved
- [ ] Changes are documented and committed if applicable

## Workflow

### Phase 1: Preparation

Set up required environment, dependencies, and configuration for "JS/TS & Markdown Linting: ESLint, Prettier, CSpell, Markdownlint".

### Phase 2: Execution

Run the primary "JS/TS & Markdown Linting: ESLint, Prettier, CSpell, Markdownlint" operations according to the defined requirements.

### Phase 3: Verification

Verify output, handle any errors, and confirm results meet expectations.

### Phase 4: Completion

Document results, clean up resources, and finalize any deliverables.

## Best Practices

1. **Prepare before executing**: Ensure all prerequisites and dependencies are in place
2. **Validate inputs**: Check configuration, parameters, and environment before running
3. **Handle errors gracefully**: Implement proper error handling and recovery
4. **Document results**: Keep records of what was done, what worked, and what didn't
5. **Clean up**: Remove temporary files, release resources after completion
