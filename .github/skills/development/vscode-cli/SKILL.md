---
author: Hermes Agent
description: Use when controlling Visual Studio Code from the `code` command: launching, installing extensions, managing settings, debugging, and configuring the editor environment.
license: MIT
metadata:
  hermes:
    tags: [imported, vscode, cli, editor, debugging, extensions, configuration]
name: vscode-cli
tags:
- imported
- vscode
- cli
- editor
- debugging
- extensions
- configuration
- scripts
title: VS Code CLI
version: 1.0.0
---

# VS Code CLI

## Overview

Use this skill when you need to control Visual Studio Code from the `code` command: launching, installing extensions, managing settings, debugging, and configuring the editor environment.

## When to Use

- Launching VS Code with specific files, folders, or workspace
- Installing, uninstalling, or managing extensions
- Configuring user or workspace settings
- Debugging extension host or editor issues
- Managing VS Code profiles and data directories
- Running VS Code in CI/CD or headless modes

## When NOT to Use

- Writing VS Code extension code (use `vscode-extension-playbook`)
- Designing UI/UX for web components (use `frontend-design`)
- General terminal operations unrelated to VS Code

## Workflow

### Phase 1: Launch & Basic Operations

```bash
# Open a file or folder
code .
code path/to/file.ts

# Open with specific profile
code --profile "My Profile" .

# Open in new window
code --new-window .

# Open with specific user data dir (isolated instance)
code --user-data-dir /tmp/vscode-test
```

### Phase 2: Extension Management

```bash
# List installed extensions
code --list-extensions

# Show extension details
code --show-extensions

# Install extension
code --install-extension ms-python.python

# Uninstall extension
code --uninstall-extension ms-python.python

# Update all extensions
code --update-extensions

# Install from VSIX file
code --install-extension path/to/extension.vsix
```

### Phase 3: Settings & Configuration

```bash
# Open settings UI
code --preferences

# Open user settings JSON
code --settings

# Open workspace settings
code --workspace-settings

# Open keybindings
code --keybindings

# Open snippets
code --snippets
```

### Phase 4: Debugging & Diagnostics

```bash
# Print version and diagnostics
code --status

# Verbose logging
code --verbose

# Profile startup performance
code --prof-startup

# Inspect extensions
code --inspect-extensions 9229

# Disable all extensions (clean launch)
code --disable-extensions

# Disable specific extension
code --disable-extension ms-python.python
```

### Phase 5: Advanced Operations

```bash
# Create tunnel for remote access
code tunnel

# Serve web UI
code serve-web

# Run as agent host
code agent

# Diff two files
code --diff file1.ts file2.ts

# Merge tool
code --merge base.ts local.ts remote.ts output.ts

# Wait for files to close before returning
code --wait file.ts
```

## Verification Checklist

- [ ] `code --help` matches the installed version
- [ ] The correct subcommand help was checked
- [ ] The command used the right profile or user-data directory
- [ ] Extension or MCP changes were verified after execution
- [ ] No secrets were written into config files

## Skills Required

| Skill | Purpose |
|-------|---------|
| `terminal` | CLI commands execution |
| `file` | Read/write settings files |
| `vscode-ext-commands` | Extension command reference |

## Related Skills

- `vscode-ext-commands` — Extension command reference
- `vscode-ext-localization` — Extension localization
- `vscode-extension-playbook` — Extension development
- `vscode-workspace-configurator` — Workspace configuration

## Usage Examples

```bash
# Quick diff
code --diff src/old.ts src/new.ts

# Isolated test environment
code --user-data-dir /tmp/vscode-test --disable-extensions

# Extension development workflow
code --install-extension ./my-extension.vsix --force
code --inspect-extensions 9229

# CI/CD headless check
code --status --disable-extensions
```

## Error Handling

- **Command not found:** `code` must be on PATH or called by full path — Exits with code 127
- **Extension not found:** `--install-extension` fails with code 1 if extension ID invalid
- **Permission denied:** User data dir access fails — Exits with code 2
- **Already running:** Some operations require VS Code to not be running — Use `--new-window` or kill existing

## Pitfalls

- Do not assume old CLI flags still exist — check `code --help` first
- Do not hardcode MCP secrets in source-controlled config
- Do not use detached mode for stdio MCP servers
- Do not rely on disabled extensions staying disabled across all window types unless the CLI option is documented for that version
- Do not mix user-profile and workspace extension state when debugging reproducibility

## References

- VS Code CLI docs: <https://code.visualstudio.com/docs/editor/command-line>
- `references/vscode-cli-reference.md` — Complete flag reference
- `references/vscode-profiles.md` — Profile management guide