---
name: python-quality
title: "Python Code Quality: Pylance & Ruff"
description: "Comprehensive workflow for init, use, test, debug, and fix Python code quality issues using Ruff + Pyright/Pylance."
version: 1.0.0
author: "Hermes Agent"
tags: [python, linting, type-checking, ruff, pyright, pylance, mcp]
license: MIT
---
# Python Code Quality: Pylance & Ruff

## Overview

Automated reasoning and workflow tool for `python-quality`. Execute multi-step tasks with deterministic quality controls and structured outputs.

## When to Use

- Setting up Python linting/type-checking in a new or existing project
- Debugging and fixing Ruff lint errors (E, F, I, B, SIM, etc.)
- Debugging and fixing Pyright/Pylance type errors
- Running comprehensive quality checks before commits
- Auto-fixing common issues across a codebase

This skill integrates with the **`python-quality` MCP server** (tools: `python_lint`, `python_format`, `python_fix`, `python_typecheck`, `python_check_all`, `python_init_config`).

---

## Quick Reference

### MCP Tools Available

| Tool | Source | Purpose |
|------|--------|---------|
| `python_lint` | python-quality | Run ruff check on files/directories |
| `python_format` | python-quality | Check or apply ruff formatting |
| `python_fix` | python-quality | Auto-fix ruff violations |
| `python_typecheck` | python-quality | Run pyright type checking |
| `python_check_all` | python-quality | Unified lint + format + typecheck report |
| `python_init_config` | python-quality | Scaffold ruff.toml + pyrightconfig.json |

### Terminal CLI Equivalents

```bash
# Lint
ruff check path/to/file.py

# Check formatting
ruff format --check --diff path/to/

# Auto-fix
ruff check --fix path/to/

# Type check
pyright path/to/file.py

# Full pipeline
ruff check path/ && ruff format --check path/ && pyright path/
```

---

## 1. INIT — Set Up Quality Tooling

### 1.1 Configuration Files

Create `.ruff.toml` in project root:

```toml
target-version = "py311"
line-length = 120

[lint]
select = ["E", "F", "I", "N", "W", "UP", "B", "SIM", "ARG", "RUF"]
ignore = ["E501", "N818"]

[format]
quote-style = "double"
line-ending = "lf"
```

Create `pyrightconfig.json` in project root:

```json
{
  "include": ["."],
  "exclude": ["**/node_modules", "**/__pycache__", "**/.git", "**/myvenv"],
  "typeCheckingMode": "basic",
  "reportMissingImports": "warning",
  "reportMissingTypeStubs": "none",
  "pythonVersion": "3.11",
  "pythonPlatform": "Windows",
  "strictListInference": true,
  "strictDictionaryInference": true
}
```

**Alternative: use MCP tool** — call `python_init_config` from the python-quality MCP server to auto-scaffold both files.

### 1.2 Install Linters

```bash
# Ruff (linter + formatter)
pip install ruff

# Pyright (type checker)
npm install -g pyright
```

### 1.3 Verify Setup

```bash
ruff --version && pyright --version
```

---

## 2. USE — Run Quality Checks

### 2.1 Lint with Ruff

```bash
# Check a single file
ruff check src/module.py

# Check entire project
ruff check .

# Check with specific rule selection
ruff check . --select=E,F,B
```

**MCP equivalent:** Call `python_lint(path=".", project_root="C:/Users/Alexa/Desktop/SandBox")`

### 2.2 Check Formatting

```bash
# Check-only (dry run)
ruff format --check --diff src/

# Format in-place
ruff format src/
```

**MCP equivalent:** Call `python_format(path=".", project_root="...", check_only=True)`

### 2.3 Type Check with Pyright

```bash
# Basic check
pyright src/

# With higher verbosity
pyright src/ --level warning
```

**MCP equivalent:** Call `python_typecheck(path=".", project_root="...")`

### 2.4 Full Pipeline

**MCP equivalent:** Call `python_check_all(path=".", project_root="...")` — returns lint errors, format issues, and type errors in one report.

---

## 3. TEST — Verify Code Quality

### 3.1 Pre-Commit Gate

Before committing, run the full quality check:

```bash
#!/usr/bin/env bash
set -e
echo "=== Ruff Lint ===" && ruff check .
echo "=== Ruff Format ===" && ruff format --check .
echo "=== Pyright ===" && pyright .
echo "=== ALL PASSED ==="
```

**Expected results:**
- `ruff check .` — exit 0 (no errors)
- `ruff format --check .` — exit 0 (all formatted)
- `pyright .` — exit 0 (no type errors)

### 3.2 Incremental Check (Changed Files Only)

```bash
# Check only files changed vs main
changed=$(git diff --name-only --diff-filter=ACMRT main -- '*.py')
[ -n "$changed" ] && ruff check $changed && pyright $changed
```

---

## 4. DEBUG — Diagnose Issues

### 4.1 Understanding Ruff Error Codes

| Rule | Meaning | Common Fix |
|------|---------|------------|
| `F821` | Undefined name | Check imports, typo in variable name |
| `F841` | Unused variable | Remove variable or prefix with `_` |
| `E722` | Bare except | Change `except:` to `except Exception:` |
| `B023` | Loop var in closure | Pass var as function parameter |
| `E741` | Ambiguous name | Rename `l`, `O`, `I` to descriptive names |
| `SIM115` | Open without context | Use `with open(...) as f:` |
| `SIM102` | Collapsible if | Merge `if a: if b:` into `if a and b:` |

### 4.2 Understanding Pyright Error Codes

| Error | Meaning | Common Fix |
|-------|---------|------------|
| `reportCallIssue` | Wrong argument type | Fix type annotation or add type stub |
| `reportOptionalMemberAccess` | Possible None access | Add None check or `assert x is not None` |
| `reportMissingImport` | Cannot find import | Install package or add to `extraPaths` |
| `reportGeneralTypeIssues` | Type mismatch | Fix type annotation or cast |
| `reportAssignmentType` | Wrong type assigned | Fix type annotation |

### 4.3 Debug Workflow (Systematic)

1. **Read error messages** — note file, line, rule code
2. **Check recent changes** — `git diff` to see what changed
3. **Run targeted check** — `ruff check specific_file.py` (not whole project)
4. **Trace data flow** — for F821, trace the undefined name; for type errors, trace the call chain
5. **Form hypothesis** — state root cause before fixing
6. **Fix and verify** — one change at a time, re-run check

---

## 5. FIX — Remediate Issues

### 5.1 Auto-Fix (Ruff)

```bash
# Safe auto-fix (reformats imports, removes unused imports)
ruff check --fix .

# With unsafe fixes (may change semantics — use carefully)
ruff check --fix --unsafe-fixes .
```

**Always re-check after auto-fix:** `ruff check .` to verify remaining errors.

### 5.2 Common Fixes by Category

**Bare excepts → specific exception:**
```python
# Bad
except:
# Good
except Exception as e:
```

**Unused variables → prefix with `_` or remove:**
```python
# Bad
for i, item in enumerate(items):
    process(item)  # i unused
# Good (prefix)
for _, item in enumerate(items):
    process(item)
```

**Open without context → use `with`:**
```python
# Bad
f = open("file.txt")
data = f.read()
f.close()
# Good
with open("file.txt") as f:
    data = f.read()
```

**Loop variable in closure → pass as default argument:**
```python
# Bad
funcs = []
for x in range(3):
    funcs.append(lambda: x)
# Good
funcs = []
for x in range(3):
    funcs.append(lambda x=x: x)
```

### 5.3 Type Fix Workflow

1. Run `python_typecheck(path=".")` to see all type errors
2. Fix missing type stubs: `pip install types-requests types-PyYAML` etc.
3. Add `# type: ignore` only as last resort for known library issues
4. Use `typing.cast(Type, expr)` for complex type narrowing

### 5.4 Full Remediation Pipeline

```bash
# 1. Auto-fix what we can
ruff check --fix .
ruff format .

# 2. Check remaining
ruff check .  # review remaining manually
pyright .     # review type errors

# 3. For each remaining error:
#    - Read the error
#    - Locate the line
#    - Apply the appropriate fix from section 5.2
#    - Re-run the check
```

**MCP equivalent:** Call `python_fix(path=".", project_root="...")` then `python_check_all(path=".")` to verify.

---

## Pitfalls

| Pitfall | Severity | Mitigation |
|---------|----------|------------|
| Auto-fix changes semantics of unsafe fixes | High | Always review `--unsafe-fixes` output; prefer `--fix` only |
| Pyright missing type stubs causes 100s of false errors | High | Install `types-*` packages; set `reportMissingTypeStubs: "none"` |
| Ruff E722 fixers that match `except:` inside strings | Medium | Review auto-fix output; some regex-based fixers can corrupt strings |
| Running ruff on venv/site-packages | Medium | Add `exclude = ["myvenv", ".venv"]` to .ruff.toml |
| Pyright on Windows may have path separator issues | Low | Use forward slashes in pyrightconfig.json paths |
| Pyright `pyright` is a POSIX shell script on Windows — subprocess can't run it | High | Use `pyright.cmd` instead (set `command: pyright.cmd` in MCP server config or use `which pyright.cmd`) |
| Generated `.ruff.toml` can contain byte 0x97 (cp1252 em-dash, invalid UTF-8) → config fails to load in EVERY repo | High | Verify with `file .ruff.toml`; write one canonical file and copy to all repos |

---

## References

- [Ruff Documentation](https://docs.astral.sh/ruff/)
- [Pyright Documentation](https://microsoft.github.io/pyright/)
- [Hermes MCP Configuration](skill_view("mcp/hermes-mcp"))
- [Native MCP Client](skill_view("mcp/native-mcp"))
- [Systematic Debugging](skill_view("software-development/systematic-debugging"))

---

## Related Skills

| Skill | Purpose |
|-------|---------|
| `devops/tooling-implementation` | Umbrella: full tooling stack workspace-wide |
| `software-development/systematic-debugging` | 4-phase root cause debugging |
| `software-development/requesting-code-review` | Pre-commit review |
| `mcp/hermes-mcp` | MCP server lifecycle |
| `qa/skill-judge` | Skill quality evaluation |

## Verification Checklist

- [ ] `.ruff.toml` exists with appropriate rule selection
- [ ] `pyrightconfig.json` exists with project paths
- [ ] `ruff` is installed and runs without errors
- [ ] `pyright` is installed and runs without errors
- [ ] Python-quality MCP server is registered (`hermes mcp list | grep python-quality`)
- [ ] First-time lint: `ruff check .` — review and fix errors
- [ ] First-time format: `ruff format --check .` — format if needed
- [ ] First-time type check: `pyright .` — review and fix errors
- [ ] Pre-commit pipeline is documented or scripted

## Workflow

### Phase 1: Preparation

Set up required environment, dependencies, and configuration for "Python Code Quality: Pylance & Ruff".

### Phase 2: Execution

Run the primary "Python Code Quality: Pylance & Ruff" operations according to the defined requirements.

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
