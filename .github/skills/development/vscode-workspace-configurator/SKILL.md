---
author: Alexa
description: Use when auditing, creating, debugging, updating, and verifying .vscode/*.json configurations across a monorepo root and all sub-repositories. Ensure every sub-repo has a properly configured .vscode/ folder with settings.json, launch.json, tasks.json, extensions.json, and mcp.json tailored to its tech stack. Detects project type from package.json, requirements.txt, manage.py, and directory structure.
license: MIT
metadata:
  hermes:
    tags: [imported, vscode, workspace, configuration, monorepo, json, settings]
name: vscode-workspace-configurator
tags:
- imported
- vscode
- workspace
- configuration
- monorepo
- json
- settings
- scripts
title: VS Code Workspace Configurator
version: 1.0.0
---

# VS Code Workspace Configurator

## Purpose

Ensure every sub-repository in a monorepo workspace has a properly configured `.vscode/` folder with JSON files tailored to the project's tech stack. This skill automates detection, creation, and validation of all VS Code workspace configurations.

## When to Use

- Setting up VS Code for a monorepo workspace
- Auditing existing `.vscode/` configurations for correctness
- Adding `.vscode/` directories to sub-repos that lack them
- Updating `.vscode/` configs after toolchain changes
- Ensuring consistency across all sub-repo VS Code configurations

## When NOT to Use

- Single-project repositories (use `vscode-cli` for basic config)
- Extension development (use `vscode-extension-playbook`)
- Extension command reference (use `vscode-ext-commands`)

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
5. Remove dead config blocks for uninstalled extensions
6. Ensure `editor.formatOnSave` is consistent
7. Check for hardcoded secrets
8. **Check for `markdownlint.config` DRY violation** — if `.markdownlintrc.json` (or `.markdownlint.json`) exists at workspace root, remove inline `markdownlint.config` from `settings.json`. The file-based config is auto-discovered by the VS Code extension — maintaining both creates drift risk. When both exist, they produce a confusing partial override (inline config wins for rules it defines, file covers the rest). Remove the inline block entirely.
9. **Set `[markdown]` formatter explicitly** — if the project uses markdown, set `"[markdown]": { "editor.defaultFormatter": "esbenp.prettier-vscode" }`. The `yzhang.markdown-all-in-one` extension handles TOC/sections/shortcuts, not formatting. Without an explicit block, format-on-save falls through to the global default which may not be appropriate.

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

## Verification Checklist

- [ ] All sub-repos identified and tech stacks detected
- [ ] Every repo has `.vscode/` with `settings.json`
- [ ] All JSON files parse correctly (`python3 -m json.tool <file>`)
- [ ] No formatter conflicts (single formatter per language)
- [ ] All referenced extensions are installed
- [ ] No dead config blocks for uninstalled extensions
- [ ] `markdownlint.config` DRY violation resolved
- [ ] `[markdown]` formatter explicitly set
- [ ] Extension conflicts resolved (redundant uninstalled)
- [ ] Settings.json structural issues fixed (no duplicate keys)
- [ ] Terminal profile matches user workflow
- [ ] Root workspace has `mcp.json`
- [ ] `extensions.json` recommendations match installed extensions

## Skills Required

| Skill | Purpose |
|-------|---------|
| `terminal` | CLI commands execution |
| `file` | Read/write JSON config files |
| `vscode-cli` | Control VS Code from terminal |
| `vscode-extension-playbook` | Extension inventory & mapping |

## Related Skills

- `vscode-cli` — VS Code CLI control
- `vscode-extension-playbook` — Extension inventory & mapping
- `vscode-ext-commands` — Extension command reference
- `vscode-ext-localization` — Extension localization

## Usage Examples

```bash
# Full monorepo audit
vscode-workspace-configurator --inventory
vscode-workspace-configurator --detect-stacks
vscode-workspace-configurator --create-missing
vscode-workspace-configurator --update-existing
vscode-workspace-configurator --verify

# Dry run
vscode-workspace-configurator --dry-run

# Specific repo
vscode-workspace-configurator --repo ./projects/backend
```

## Error Handling

- **JSON parse error:** Prints file path and line number, exits with code 1
- **Permission denied:** Exits with code 2, prints path
- **Stack detection failed:** Warns, uses default template
- **Dry-run mode:** Uses `--dry-run` flag, outputs plan without writing files

## Pitfalls

- **Stale configs in sub-repos:** Subproject `.vscode/` frequently reference extensions from different profiles — always scan full workspace
- **Dead config blocks:** Config for removed extensions silently bloat settings.json — remove them
- **Formatter conflicts:** Multiple formatters for same language cause silent override — validate single formatter per language
- **Global `editor.defaultFormatter` trap:** Never set `editor.defaultFormatter` to a language-specific extension (e.g. `yzhang.markdown-all-in-one`). This applies that formatter to ALL languages that lack an explicit `[lang]` block. Use `esbenp.prettier-vscode` as default or omit it entirely. See `references/cross-file-conflict-detection.md` for detection scripts.
- **User vs workspace setting conflicts:** Workspace settings completely REPLACE (not merge) user settings for the same key. After editing workspace settings, check for unintended overrides that disable user-level features like `source.addMissingImports` or `source.sort.json` in `editor.codeActionsOnSave`.
- **Hardcoded paths:** Avoid absolute paths in launch.json/tasks.json — use `${workspaceFolder}` variables
- **Secret leakage:** Never commit API keys, tokens, or passwords in `.vscode/*.json`
- **Windows `code` CLI:** On Windows, `code` is a shell script (`cmd` wrapper). Calling from Python `subprocess.run()` fails with `FileNotFoundError`. Use `terminal()` tool: `terminal("code --list-extensions --show-versions")`.

## References

- `references/cross-file-conflict-detection.md` — User vs workspace conflict detection, file type coverage analysis, extension recommendation scripts
- `references/vscode-settings-templates.md` — Full template library
- `references/tech-stack-detection.md` — Detection rules and patterns
- `references/extension-conflict-resolution.md` — Conflict resolution guide

## Templates

- `templates/settings-bun-ts.json`
- `templates/settings-nextjs-react-ts.json`
- `templates/settings-django-python.json`
- `templates/settings-node-scripts.json`
- `templates/launch-debug.json`
- `templates/tasks-build-test.json`
- `templates/extensions-recommendations.json`
- `templates/mcp-root.json`