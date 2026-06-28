---
author: Alexa
description: 'Use when auditing, creating, debugging, updating, and verifying .vscode/*.json
  configurations across a monorepo root and all sub-repositories. Ensure every sub-repo
  has a properly configured .vscode/ folder with settings.json, launch.json, tasks.json,
  extensions.json, and mpc.json tailored to its tech stack. Detects project type from
  package.json, requirements.txt, manage.py, and directory structure.

  '
license: MIT
name: vscode-workspace-configurator
title: VS Code Workspace Configurator
version: 1.0.0

---

# VS Code Workspace Configurator

## Purpose

Ensure every sub-repository in a monorepo workspace has a properly configured
`.vscode/` folder with JSON files tailored to the project's tech stack. This
skill automates detection, creation, and validation of all VS Code workspace
configurations.

## When to Use

- Setting up VS Code for a monorepo workspace
- Auditing existing `.vscode/` configurations for correctness
- Adding `.vscode/` directories to sub-repos that lack them
- Updating `.vscode/` configs after toolchain changes
- Ensuring consistency across all sub-repo VS Code configurations

## Tech Stack Detection

Inspect these files in order to determine the project's stack:

1. `package.json` — check `dependencies` + `devDependencies`:
   - `next` → Next.js
   - `react` → React
   - `express` → Express
   - `prisma` / `@prisma/client` → Prisma
   - `drizzle-orm` → Drizzle
   - `tailwindcss` → Tailwind
   - `typescript` → TypeScript
2. `requirements.txt` — check contents:
   - `django` → Django
   - `scrapy` → Scrapy
   - `flask` → Flask
   - `fastapi` → FastAPI
3. `manage.py` → Django
4. `pyproject.toml` → Python
5. Directory `backend/` exists → Multi-dir (full-stack)

## Workflow

### Phase 1: Inventory & Detect

1. Walk the workspace tree (skip `node_modules`, `.git`, `__pycache__`)
2. Identify all sub-repos with code (have a stack-detecting file)
3. For each repo, detect its tech stack
4. Check for existing `.vscode/` directories and their JSON files
5. Record gap analysis: which repos lack `.vscode/`, which have stale configs

### Phase 2: Create .vscode Directories

For each repo missing `.vscode/`:

1. Create `.vscode/` directory
2. Generate `settings.json` based on detected stack
3. Generate `launch.json` with stack-appropriate debug configs
4. Generate `tasks.json` with stack-appropriate build/test tasks
5. Generate `extensions.json` with stack-appropriate recommendations
6. For root workspace only: generate `mcp.json`

### Phase 3: Update Existing Configs

For repos that already have `.vscode/`:

1. Read each existing JSON file
2. Validate JSON syntax
3. Check formatter conflicts (multiple formatters for same language)
4. Verify all referenced extensions exist
5. Add missing language-specific formatter blocks
9. Remove dead config blocks for uninstalled extensions
10. Ensure `editor.formatOnSave` is consistent
11. Check for hardcoded secrets
12. **Check for `markdownlint.config` DRY violation** — if `.markdownlintrc.json` (or `.markdownlint.json`) exists at workspace root, remove inline `markdownlint.config` from `settings.json`. The file-based config is auto-discovered by the VS Code extension — maintaining both creates drift risk. When both exist, they produce a confusing partial override (inline config wins for rules it defines, file covers the rest). Remove the inline block entirely.
13. **Set `[markdown]` formatter explicitly** — if the project uses markdown, set `"[markdown]": { "editor.defaultFormatter": "esbenp.prettier-vscode" }`. The `yzhang.markdown-all-in-one` extension handles TOC/sections, not formatting. Without an explicit block, format-on-save falls through to the global default which may not be appropriate.

### Phase 3.5: Detect & Resolve Extension Conflicts

After updating configs, scan for extension-level conflicts:

1. **Check for redundant extensions** — identify extensions with overlapping functionality:
   - Multiple Git extensions (GitLens supersedes git-history, git-graph)
   - Multiple color-highlighting extensions
   - Multiple markdown formatters (markdown-all-in-one vs prettier proseWrap)
2. **Uninstall redundant extensions** using `code --uninstall-extension <id>`:
   - Always verify uninstalled: `code --list-extensions | grep <id>`
3. **Check for settings conflicts specific to markdown:**
   - If both `yzhang.markdown-all-in-one` and `prettier.proseWrap` are active, set `[markdown]` formatter explicitly to one of them
   - Add `"[markdown]": { "editor.defaultFormatter": "yzhang.markdown-all-in-one" }` for explicit ownership
4. **Validate settings.json for structural issues:**
   - Check for duplicate keys (same `[language]` block appearing twice)
   - After any patch tool edit, re-read and verify no duplication
   - Validate JSON syntax: `python3 -c "import json; json.load(open('<path>'))"`
5. **Check terminal profile matches user workflow:**
   - On Windows, if user works in Git Bash, set `terminal.integrated.defaultProfile.windows` to `"Git Bash"` (not `"PowerShell"`)

### Phase 4: Verify

1. Validate all JSON files parse correctly
2. Cross-reference extension recommendations against installed extensions
3. Verify no formatter conflicts exist
4. Confirm all repos have `.vscode/` with at least `settings.json`
5. Report any remaining issues

## Settings.json Templates

### Bun / TypeScript Workspace Root / Script Toolkit
```json
{
  "editor.defaultFormatter": "esbenp.prettier-vscode",
  "editor.formatOnSave": true,
  "editor.codeActionsOnSave": {
    "source.fixAll": "explicit",
    "source.organizeImports": "explicit"
  },
  "editor.inlineSuggest.enabled": true,
  "editor.codeLens": true,
  "editor.suggestSelection": "first",
  "errorLens.enabled": true,
  "files.associations": {
    "*.css": "tailwindcss",
    "*.scss": "tailwindcss"
  },
  "tailwindCSS.classFunctions": [
    "tw",
    "clsx",
    "tw\\.[a-z-]+"
  ],
  "tailwindCSS.emmetCompletions": true,
  "terminal.integrated.defaultProfile.windows": "Git Bash",
  "terminal.integrated.profiles.windows": {
    "Command Prompt": {
      "icon": "terminal-cmd",
      "path": "cmd.exe"
    },
    "Git Bash": {
      "icon": "terminal-bash",
      "source": "Git Bash"
    },
    "PowerShell": {
      "icon": "terminal-powershell",
      "source": "PowerShell"
    }
  },
  "workbench.editor.editorActionsLocation": "default",
  "[typescript]": {
    "editor.defaultFormatter": "esbenp.prettier-vscode"
  },
  "[javascript]": {
    "editor.defaultFormatter": "esbenp.prettier-vscode"
  },
  "[json]": {
    "editor.defaultFormatter": "vscode.json-language-features"
  },
  "[jsonc]": {
    "editor.defaultFormatter": "vscode.json-language-features"
  },
  "[shellscript]": {
    "editor.defaultFormatter": "foxundermoon.shell-format"
  }
}
```

### Next.js / React / TypeScript

```json
{
  "editor.defaultFormatter": "esbenp.prettier-vscode",
  "editor.formatOnSave": true,
  "editor.codeActionsOnSave": {
    "source.fixAll.eslint": "explicit",
    "source.organizeImports": "explicit"
  },
  "editor.inlineSuggest.enabled": true,
  "files.associations": { "*.css": "tailwindcss" },
  "tailwindCSS.emmetCompletions": true,
  "tailwindCSS.includeLanguages": {
    "css": "css",
    "scss": "scss",
    "javascript": "jsx",
    "typescript": "tsx"
  },
  "[javascript]": { "editor.defaultFormatter": "esbenp.prettier-vscode" },
  "[typescript]": { "editor.defaultFormatter": "esbenp.prettier-vscode" },
  "[typescriptreact]": { "editor.defaultFormatter": "esbenp.prettier-vscode" },
  "[json]": { "editor.defaultFormatter": "vscode.json-language-features" },
  "[jsonc]": { "editor.defaultFormatter": "vscode.json-language-features" },
  "[css]": { "editor.defaultFormatter": "esbenp.prettier-vscode" },
  "[scss]": { "editor.defaultFormatter": "esbenp.prettier-vscode" }
}
```

> ⚠️ **Do NOT include** `django-html`, `plaintext`, `django-txt`, or Python-related keys in Next.js-only projects. Those belong in the Django/Python template only.

### Django / Python

```json
{
  "editor.defaultFormatter": "ms-python.python",
  "editor.formatOnSave": true,
  "editor.codeActionsOnSave": {
    "source.organizeImports": "explicit"
  },
  "editor.inlineSuggest.enabled": true,
  "python.languageServer": "Pylance",
  "python.analysis.typeCheckingMode": "basic",
  "python.analysis.autoImportCompletions": true,
  "python.defaultInterpreterPath": "${workspaceFolder}/venv/Scripts/python.exe",
  "python-envs.alwaysUseUv": true,
  "python-envs.autoActivate": true,
  "python-envs.venvFolders": [".venv", "env", "venv", ".env", "envs", "venvs"],
  "files.associations": {
    "**/*.{txt,in}": "django-txt",
    "**/requirements/**/*.{txt,in}": "pip-requirements"
  },
  "[python]": {
    "editor.defaultFormatter": "ms-python.python",
    "editor.formatOnSave": true
  },
  "[html]": { "editor.defaultFormatter": "vscode.html-language-features" },
  "[django-html]": { "editor.defaultFormatter": "vscode.html-language-features" },
  "[css]": { "editor.defaultFormatter": "vscode.css-language-features" },
  "[javascript]": { "editor.defaultFormatter": "esbenp.prettier-vscode" },
  "[typescript]": { "editor.defaultFormatter": "esbenp.prettier-vscode" },
  "[json]": { "editor.defaultFormatter": "vscode.json-language-features" },
  "[jsonc]": { "editor.defaultFormatter": "vscode.json-language-features" }
}
```

### Bun / TypeScript (Scripts)

```json
{
  "editor.defaultFormatter": "esbenp.prettier-vscode",
  "editor.formatOnSave": true,
  "editor.codeActionsOnSave": {
    "source.fixAll": "explicit",
    "source.organizeImports": "explicit"
  },
  "editor.inlineSuggest.enabled": true,
  "[typescript]": { "editor.defaultFormatter": "esbenp.prettier-vscode" },
  "[javascript]": { "editor.defaultFormatter": "esbenp.prettier-vscode" },
  "[json]": { "editor.defaultFormatter": "vscode.json-language-features" },
  "[jsonc]": { "editor.defaultFormatter": "vscode.json-language-features" },
  "[shellscript]": { "editor.defaultFormatter": "foxundermoon.shell-format" }
}
```

### Node.js (Selenium / Scripts)

```json
{
  "editor.defaultFormatter": "esbenp.prettier-vscode",
  "editor.formatOnSave": true,
  "editor.codeActionsOnSave": {
    "source.fixAll.eslint": "explicit",
    "source.organizeImports": "explicit"
  },
  "editor.inlineSuggest.enabled": true,
  "[javascript]": { "editor.defaultFormatter": "esbenp.prettier-vscode" },
  "[typescript]": { "editor.defaultFormatter": "esbenp.prettier-vscode" },
  "[json]": { "editor.defaultFormatter": "vscode.json-language-features" },
  "[jsonc]": { "editor.defaultFormatter": "vscode.json-language-features" }
}
```

## Launch.json Templates

### Next.js

```json
{
  "version": "0.2.0",
  "configurations": [
    {
      "command": "npm run dev",
      "name": "Next.js: Dev Server",
      "request": "launch",
      "type": "node-terminal"
    },
    {
      "command": "npm run build",
      "name": "Next.js: Build",
      "request": "launch",
      "type": "node-terminal"
    },
    {
      "command": "npm run lint",
      "name": "Next.js: Lint",
      "request": "launch",
      "type": "node-terminal"
    },
    {
      "command": "npx tsc --noEmit",
      "name": "TypeScript: Type Check",
      "request": "launch",
      "type": "node-terminal"
    }
  ]
}
```

### Django

```json
{
  "version": "0.2.0",
  "configurations": [
    {
      "name": "Django: Runserver",
      "type": "debugpy",
      "request": "launch",
      "program": "${workspaceFolder}/manage.py",
      "args": ["runserver"],
      "django": true,
      "justMyCode": true
    },
    {
      "name": "Django: Test",
      "type": "debugpy",
      "request": "launch",
      "program": "${workspaceFolder}/manage.py",
      "args": ["test", "--keepdb", "--verbosity=2"],
      "django": true,
      "justMyCode": true
    },
    {
      "name": "Python: Current File",
      "type": "debugpy",
      "request": "launch",
      "program": "${file}",
      "console": "integratedTerminal"
    }
  ]
}
```

### Bun / TypeScript Scripts

```json
{
  "version": "0.2.0",
  "configurations": [
    {
      "name": "Bun: Current File",
      "type": "node",
      "request": "launch",
      "runtimeExecutable": "bun",
      "program": "${file}",
      "console": "integratedTerminal"
    },
    {
      "name": "Bun: Run All Tests",
      "type": "node",
      "request": "launch",
      "runtimeExecutable": "bun",
      "runtimeArgs": ["test"],
      "console": "integratedTerminal"
    }
  ]
}
```

### Node.js

```json
{
  "version": "0.2.0",
  "configurations": [
    {
      "name": "Node.js: Current File",
      "type": "node",
      "request": "launch",
      "program": "${file}",
      "console": "integratedTerminal"
    },
    {
      "name": "npm start",
      "type": "node",
      "request": "launch",
      "runtimeExecutable": "npm",
      "runtimeArgs": ["start"],
      "console": "integratedTerminal"
    }
  ]
}
```

## Tasks.json Templates

### Bun / TypeScript

```json
{
  "version": "2.0.0",
  "tasks": [
    {
      "command": "bun run format",
      "label": "Bash: Format",
      "type": "shell",
      "group": "build",
      "presentation": { "reveal": "always", "panel": "shared" }
    },
    {
      "command": "bun run typecheck",
      "label": "Bash: Type Check",
      "type": "shell",
      "group": "build",
      "presentation": { "reveal": "always", "panel": "shared" }
    },
    {
      "command": "bun test",
      "label": "Bash: Test",
      "type": "shell",
      "group": "test",
      "presentation": { "reveal": "always", "panel": "shared" }
    }
  ]
}
```

## Extensions.json Templates

## Pitfalls

- Do not hardcode absolute paths in `launch.json` — use `${workspaceFolder}`, `${file}`
- Do not create `.vscode/mcp.json` in sub-repos — only in root workspace
- Do not add `github.copilot` to recommendations — it requires interactive OAuth
- Do not use JS comments in `.json` files — VS Code tolerates them in `settings.json` (JSONC) but `extensions.json`, `launch.json`, `tasks.json` must be strict JSON
- Do not reference extensions that aren't installed in the active profile
- Do not create duplicate formatter configs for the same language
- Always validate JSON after writing — a single trailing comma breaks the file
- For multi-dir repos (e.g., `backend/` + `frontend/`), configure formatters for both Python and JS/TS
- Do not run `code --list-extensions` from Python `subprocess` on Windows — `code` is a shell script, not a native exe; use `terminal()` instead
- When sub-repos are git submodules, commit `.vscode/` changes inside each submodule first (`git -C "$sub" add .vscode/ && git -C "$sub" commit -m "..." --no-verify`), then update the parent repo
- **Dual-stack repos** (e.g., Django + Next.js): `.vscode/` must have formatters, launch configs, tasks, AND extensions for BOTH stacks — see `references/vscode-config-templates.md`
- **Bun CLI tools**: Use `type: "node"` + `runtimeExecutable: "bun"` in launch.json, NOT `type: "node-terminal"` which ignores `console` and `runtimeExecutable`
- **Trailing commas**: The #1 JSON syntax error in `launch.json`/`tasks.json` — always validate with `python3 -c "import json; json.load(open('file'))"` after writing
- **Hardcoded paths**: Never use absolute paths in `tasks.json` — use `${workspaceFolder}`
- **Template leakage**: The Next.js template historically included `tailwindCSS.includeLanguages` entries for `django-html`, `plaintext` — these MUST be removed for pure Next.js projects (they cause irrelevant IntelliSense and confusion)
- **Python formatter in JS-only projects**: Never include `[python]` formatter blocks (ruff, black, pylance) in projects without Python code (e.g., pure Next.js). Check AGENTS.md for `python` or `django` before adding.
- **CSS file association pattern**: Use `"*.css"` NOT `"**/.css"` — the leading `**/` matches nothing and is a typo
- **Extension/code-action mismatch**: If `settings.json` has `"source.fixAll.eslint": "explicit"`, eslint MUST be in `extensions.json` recommendations, NOT in `unwantedRecommendations`
- **Root mcp.json parameterization**: Use `${workspaceFolder}` for paths and `${env:VAR}` for environment variables — never hardcode Windows absolute paths like `C:\\Users\\...`
- **Inventory precision rule**: When writing repo lists or status summaries, copy names exactly from discovery results instead of inventing normalized variants. Invented placeholders become false assumptions in reports.
- **Resume workflow state from actual artifacts**: If prior work reports a completed audit, continue from execution; do not restart inventory unless verification shows a real state change or missing artifact.
- **Duplicate keys after patch**: The `patch` tool can create duplicate JSON keys when patching adjacent regions. After every `patch` on `settings.json`, re-read the file and check for duplicate `"[lang]"` blocks. Validate with `python3 -c "import json; json.load(open('file'))"` — a valid parse does NOT guarantee no duplicates, because JSON silently takes the last value for duplicate keys. Use `grep -c '^\\t\"\\['` to count language blocks and compare against expected.
- **markdownlint.config DRY violation:** When a `.markdownlintrc.json` exists at workspace root, the inline `markdownlint.config` in VS Code settings is duplicate config that WILL drift. The file-based config is auto-discovered by the VS Code markdownlint extension — remove the inline block from settings.json. This avoids confusing partial-override behavior where each config handles different rules.
- **Prettier proseWrap vs markdown formatter**: `prettier.proseWrap: \"always\"` formats markdown prose width, but if `yzhang.markdown-all-in-one` is the `[markdown]` formatter, Prettier's proseWrap is ignored for markdown (the language-specific formatter wins). Avoid setting both without explicit `[markdown]` formatter — the conflict is silent and users see inconsistent markdown formatting.

## Template Files

Pre-built JSON templates for each stack type are in `templates/`:
- `templates/settings-nextjs.json` — Next.js/React/TypeScript
- `templates/settings-django.json` — Django/Python
- `templates/settings-bun.json` — Bun/TypeScript scripts
- `templates/settings-python.json` — Pure Python
- `templates/settings-node.json` — Node.js

Copy and modify rather than writing from scratch. These are known-good baselines validated across 16 repos.

## Audit & Repair Patterns

See `references/vscode-config-templates.md` § "Audit & Repair Patterns" for:
- JSON validation (trailing commas, JS comments in strict JSON)
- Dual-stack repo configuration (Django + Next.js)
- Bun CLI launch config pattern
- Path variable usage in tasks.json
- Formatter conflict detection
- Verification gate script

See `references/audit-scripts.md` for:
- ESLint mismatch detection (monorepo-wide)
- JSON validation script (all .vscode files)
- Formatter conflict detection
- Audit script stale-data pitfall

## Verification Checklist

- [ ] All sub-repos have `.vscode/` directory
- [ ] All `.vscode/*.json` files are valid JSON (no parse errors)
- [ ] `settings.json` has language-specific formatter blocks matching the stack
- [ ] `launch.json` has stack-appropriate debug configurations
- [ ] `tasks.json` has build/test tasks matching the stack
- [ ] `extensions.json` recommends only relevant extensions
- [ ] No formatter conflicts (one formatter per language per file)
- [ ] No hardcoded secrets or absolute paths
- [ ] No JS comments in strict JSON files
- [ ] Root workspace has `mcp.json` with parameterized inputs
