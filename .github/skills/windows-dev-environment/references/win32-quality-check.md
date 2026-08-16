---
name: workspace-win32-quality-check
author: Hermes Agent
title: "Windows Workspace Quality Check"
description: "Post-setup verification sequence for Python linting, VSCode config integrity, and markdown linting on Windows."
version: 1.0.0
tags: [windows, vscode, python, markdown, verification]
---
# Windows Workspace Quality Check

## Overview

Automated reasoning and workflow tool for `workspace-win32-quality-check`. Execute multi-step tasks with deterministic quality controls and structured outputs.

## When to Use
- After modifying VSCode JSON configs on Windows
- After editing markdownlint configuration
- After setting up or modifying Python quality tooling
- To verify no deprecation warnings or silent failures exist

## Verification Sequence

Run these checks in order after any config change.

### 1. VSCode JSON Integrity

Validate every `.vscode/*.json` file parses correctly:
```bash
python -c "
import json, os, sys
errors = 0
for f in os.listdir('.vscode'):
    path = os.path.join('.vscode', f)
    try:
        json.load(open(path))
    except json.JSONDecodeError as e:
        print(f'FAIL {path}: {e}')
        errors += 1
if errors == 0:
    print('All VSCode JSON valid')
else:
    sys.exit(errors)
"
```

Check for duplicate language-specific blocks (last one wins silently):
```bash
grep -n '^  "\[' .vscode/settings.json | sort | uniq -d
```

Verify no deprecated Python keys in settings.json:
```bash
python -c "
import json
s = json.load(open('.vscode/settings.json'))
deprecated = ['python.languageServer', 'python.linting.enabled', 'python.linting.ruffEnabled', 'python.formatting.provider']
for k in deprecated:
    if k in s:
        print(f'WARN: deprecated {k} present')
"
```

Check `python3` is not used (missing on Windows):
```bash
grep -rn '"python3"' .vscode/tasks.json && echo "WARN: python3 not available on Windows" || echo "OK: no python3 references"
```

### 2. Python Linting Setup

Verify ruff runs:
```bash
ruff --version
ruff check --select=E722,F821 path/to/a/python/file.py
```

Verify pyright runs:
```bash
pyright --version
pyright path/to/a/python/file.py
```

### 3. markdownlint Configuration

Verify the markdownlint config works without excessive file scanning:
```bash
bunx markdownlint-cli2 --config .markdownlintrc.json --no-globs "*.md"
```
If this times out or scans >100 files when only passing a few, the config likely has a `globs` entry. Check:
```bash
python -c "import json; cfg = json.load(open('.markdownlintrc.json')); print('globs:', cfg.get('globs', 'not set'))"
```
If `globs` is present (`["**/*.md"]`), remove it — the `--no-globs` CLI flag must be the sole file-list source.

### 4. VSCode Audit Depth (replaces audit_vscode_config.py)

Verify `tasks.json` has `options.cwd` and `problemMatcher` on each task:
```bash
python -c "
import json
t = json.load(open('.vscode/tasks.json'))
print('options.cwd:', t.get('options', {}).get('cwd'))
for task in t.get('tasks', []):
    has_pm = 'problemMatcher' in task
    print(f'  {task[\"label\"]}: problemMatcher={\"✓\" if has_pm else \"✗\"}')
"
```

Verify `launch.json` Python configs have `justMyCode`, `python` path, and `cwd`:
```bash
python -c "
import json
l = json.load(open('.vscode/launch.json'))
for cfg in l['configurations']:
    if cfg.get('type') == 'debugpy':
        print(f'{cfg[\"name\"]}: justMyCode={cfg.get(\"justMyCode\", \"✗\")}, python={\"✓\" if \"myvenv\" in cfg.get(\"python\", \"\") else \"✗\"}, cwd={\"✓\" if cfg.get(\"cwd\") else \"✗\"}')
"
```

Verify `extensions.json` covers the detected tech stack:
```bash
python -c "
import json
e = json.load(open('.vscode/extensions.json'))
recs = e.get('recommendations', [])
minimum = ['esbenp.prettier-vscode', 'dbaeumer.vscode-eslint', 'davidanson.vscode-markdownlint',
           'charliermarsh.ruff', 'redhat.vscode-yaml', 'eamodio.gitlens',
           'streetsidesoftware.code-spell-checker', 'timonwong.shellcheck',
           'ms-azuretools.vscode-docker', 'bierner.markdown-mermaid']
for ext in minimum:
    print(f'  {ext}: {\"✓\" if ext in recs else \"✗\"}')
"
```

### 5. New Tooling Verification

Verify all code-quality CLIs are available:
```bash
for tool in eslint prettier cspell pre-commit ruff pyright bunx; do
  which "$tool" &>/dev/null && echo "✓ $tool" || echo "✗ $tool NOT FOUND"
done
```

Verify spellcheck config exists:
```bash
ls cspell.json 2>/dev/null && python -c "import json; json.load(open('cspell.json')); print('✓ cspell.json valid')" || echo "✗ cspell.json missing"
```

Verify pre-commit config exists and can be listed:
```bash
ls .pre-commit-config.yaml 2>/dev/null || echo "✗ .pre-commit-config.yaml missing"
```

Verify changelog config exists:
```bash
ls cliff.toml 2>/dev/null || echo "✗ cliff.toml missing"
```

### 6. MCP Server Pre-Registration Workflow

BEFORE registering a new MCP server in `config.yaml`, always test it:
```bash
# Create batch wrapper (if needed)
cat > ~/.local/bin/test-server-mcp.bat
# Test server directly
hermes mcp test <server-name>
```
If the test fails, fix the server BEFORE registering. Common failures:
- **Connection closed**: Wrapper script can't find Python or server file — use absolute paths in the .bat wrapper
- **Timeout (30s+)**: Server hangs on initialize — increase `connect_timeout` in config or add `stderr` blocking in wrapper
- **WinError 2/193**: Wrong binary — use `.cmd` suffix on Windows

## Common Fixes

### markdownlint scans too many files
Remove `globs` from `.markdownlintrc.json`. Always use `--no-globs` on CLI.

### VSCode shows deprecated Python settings
Remove `python.languageServer`, `python.linting.enabled`, `python.linting.ruffEnabled`, `python.formatting.provider` from `settings.json`.

### MCP server reports Win32 error
Replace `pyright` with `pyright.cmd` in the MCP server's executable lookup.

## Pitfalls

### Patch tool corrupts markdown list markers
When re-patching a markdown file that has `- ` list items, the patch tool can corrupt them to `|- `. After every patch that touches markdown list items, immediately `read_file` to verify the list markers stayed as `- ` and weren't corrupted. If corruption occurs, use `write_file` to rewrite the affected section instead of a second patch.

### MCP servers registered before passing test
Always run `hermes mcp test <name>` BEFORE adding the server to `mcp_servers` in config.yaml. A server that fails the test will block MCP tool discovery for all servers at Hermes startup. Test first, register second.
