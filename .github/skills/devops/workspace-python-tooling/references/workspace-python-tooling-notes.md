# Workspace Python Tooling References

## Validated Ruff TOML

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

Note: omit invalid `target-version` forms such as `python-version = "3.11"`. Use supported variants like `py311`, `py312`, or `py313` if needed.

## Validated Pyright Config

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

## Validated VS Code Settings Snippet

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

## Verified Commands

- `ruff --version`
- `ruff check .github/scripts/_agents_fix_discover.py --config .ruff.toml`
- `ruff format .github/scripts/_agents_fix_discover.py --check --config .ruff.toml`
- `pyright .github/scripts/_agents_fix_discover.py --pythonversion 3.11`

## Narrow Validation Tip

Run ruff/pyright on one script or small folder first. Broad monorepo root runs can exceed timeout budgets before tuning `exclude`/`include`.
