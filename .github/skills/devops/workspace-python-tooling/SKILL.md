---
author: Alexa
description: "Install, configure, validate, and verify Python editor/tooling in a workspace: ruff, Pylance/pyright, pyproject/.ruff.toml, and VS Code settings.json. Use when setting up lint/format/type-check for a repo, debugging broken config, or adding a repeatable validation step."
license: MIT
name: workspace-python-tooling
tags:
  - python
  - ruff
  - pylance
  - pyright
  - vscode
  - linting
  - type-checking
title: Workspace Python Tooling
version: 1.0.0
---

# Workspace Python Tooling

Install, configure, validate, and verify Python linting, formatting, and type checking in a workspace.

## When to Use

- Adding ruff and Pylance/pyright to a workspace or repo
- Repairing broken `.ruff.toml` / `pyproject.toml` lint config
- Aligning VS Code `settings.json` with the workspace interpreter and linters
- Running a focused lint/type-check pass before commit or CI review

## When NOT to Use

- Project-specific Python packaging workflows beyond tooling setup
- CI-only lint jobs without local editor configuration
- Python version pinning that belongs under a packaging/runtime setup workflow

## Setup Order

1. Inspect existing manifests/configs:
   - `requirements.txt`
   - `pyproject.toml`
   - `.ruff.toml`
   - `pyrightconfig.json`
   - `.vscode/settings.json`
2. Add/repair tool config files
3. Align `settings.json` interpreter + linter + language-server settings
4. Validate with narrow commands
5. Expand only after the narrow pass succeeds

## ruff

Preferred config locations: `.ruff.toml` or `pyproject.toml`

Verify installation:
- `ruff --version`

Run validation:
- `ruff check <path> --config .ruff.toml`
- `ruff format <path> --check --config .ruff.toml`

Recommended starting lint/format behavior:
```toml
[format]
line-ending = "lf"
quote-style = "double"

[lint]
select = ["E", "F", "I", "UP", "B", "SIM"]
ignore = ["E501"]

[lint.isort]
known-first-party = ["scripts", "projects"]
```

Pitfall:
- `target-version` in ruff uses supported variants like `py311`, `py312`, `py313`
- `python-version = "3.11"` is invalid and blocks both check and format commands
- If ruff config parsing fails, remove the invalid stanza rather than guess alternate keys
- **`COM812` (missing-trailing-comma) conflicts with the formatter.** Ruff warns: "The following rule may cause conflicts when used with the formatter: `COM812`. To avoid unexpected behavior, we recommend disabling this rule, either by removing it from the `lint.select` or `lint.extend-select` configuration, or adding it to the `lint.ignore` configuration." Add `"COM812"` to your `ignore` list.
- **`UP038` (non-pep604-isinstance) was removed in recent ruff versions.** If you see "The following rules have been removed and ignoring them has no effect: `UP038`", remove it from your `select` or `extend-select` list.

## Multi-Repo / Workspace Batch Runs

When running quality checks across a monorepo with independent sub-projects:

```bash
# Check each sub-repo (they inherit root .ruff.toml via ruff's parent-walk)
for sub in projects/*/; do
  pyfiles=$(find "$sub" -maxdepth 3 -name "*.py" -not -path "*/__pycache__/*" -not -path "*/.git/*" 2>/dev/null | wc -l)
  if [ "$pyfiles" -gt 0 ]; then
    echo "=== $sub ===" && ruff check "$sub" && ruff format --check "$sub"
  fi
done
```

**Sub-repos without their own `.ruff.toml`** silently inherit the parent/root config. This works but check that the root's `target-version` matches each sub-repo's Python version.

**cookiecutter / Jinja templates** in `pyproject.toml` crash ruff's TOML parser. Add `exclude = ["cookiecutter-*"]` at the top level of `.ruff.toml` (NOT under `[lint]`).

**Django projects** produce many `RUF012` (mutable-class-default) errors from model fields. These are expected — Django's field API requires mutable defaults. Either `# noqa: RUF012` inline, or add to `ignore` if noise is too high.

**Import-outside-top-level (PLC0415)** is common in Django `ready()` and Celery configs — it's an intentional lazy-import pattern, not a bug.

**Pyright on full-workspace** may time out on large monorepos. Start with a single script or folder, then broaden.

## Pylance / pyright

VS Code Python settings:
- `"python.languageServer": "Pylance"`
- `"python.analysis.typeCheckingMode": "basic"`

Standalone validation:
- Install: `npm install -g pyright`
- Run narrow check first: `pyright <file-or-small-folder> --pythonversion 3.11`
- Avoid full-monorepo root runs until exclude/include paths are tuned

`pyrightconfig.json` example:
```json
{
  "include": ["."],
  "exclude": [
    "**/node_modules",
    "**/__pycache__",
    "**/.venv",
    "**/venv",
    "**/.git",
    "research",
    "scripts"
  ],
  "pythonVersion": "3.11",
  "typeCheckingMode": "basic"
}
```

Pitfall:
- Full-workspace pyright may time out on large monorepos
- Start with a single script or folder, then broaden

## VS Code Settings Pattern

```json
{
  "python.defaultInterpreterPath": "${workspaceFolder}/myvenv/Scripts/python.exe",
  "python.languageServer": "Pylance",
  "python.analysis.typeCheckingMode": "basic",
  "python.linting.enabled": true,
  "python.linting.ruffEnabled": true,
  "python.formatting.provider": "none",
  "[python]": {
    "editor.defaultFormatter": "ms-python.python",
    "editor.formatOnSave": true
  }
}
```

Pitfall:
- Do not leave stale backend interpreter paths in workspace `settings.json`
- Keep `python.linting.ruffEnabled` and formatter settings consistent
- If both pylint and ruff are viable, prefer ruff unless the repo explicitly requires pylint

## Verification

Use a narrow pass first:
- ruff check/format on a single script or folder
- pyright on a single script or folder
- Confirm VS Code settings contain the expected Pylance + ruff keys

Avoid these anti-patterns:
- Broad repo-wide pyright before `exclude` paths are tuned
- Blindly changing config without reading existing manifest files
- Capturing transient environment install issues as durable skill rules

## Skills Required

| Skill | Purpose |
|-------|---------|
| `terminal` | Run ruff/pyright/setup commands |
| `file` | Read/write config and settings files |
| `vscode-workspace-configurator` | Context for workspace-wide VS Code config |