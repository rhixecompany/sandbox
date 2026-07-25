---
author: Hermes Agent
description: Use when adding, updating, or refactoring commands in VS Code extension development. Covers command registration, naming conventions, visibility, and menu contributions.
license: MIT
metadata:
  hermes:
    tags: [imported, vscode, extension, commands, ide]
name: vscode-ext-commands
tags:
- imported
- vscode
- extension
- commands
- ide
- scripts
title: VS Code Extension Commands
version: 1.1.0
---

# VS Code Extension Commands

## Overview

Add and manage commands in VS Code extensions following official guidelines. This skill covers command registration, naming conventions, visibility patterns, and menu contributions.

## When to Use

- Adding new commands to a VS Code extension
- Refactoring existing command definitions
- Configuring command visibility (Command Palette, Side Bar, Context Menu)
- Setting up command enablement conditions
- Contributing commands to menus and views

## When NOT to Use

- **Creating views or webviews** — Use `vscode-extension-playbook` for view containers, tree views, and webview panels
- **Localizing command strings** — Use `vscode-ext-localization` for i18n/localization of command titles and descriptions
- **Extension packaging or publishing** — This skill covers command development only. Use `vsce` CLI or marketplace tooling for packaging/publishing
- **Language extension contributions** — Language features (grammars, semantic tokens, hover, completion) have their own contribution points separate from commands

## Workflow

### Phase 1: Define Command in package.json

Every command must have a `title` and should have a `category`:

```json
{
  "contributes": {
    "commands": [
      {
        "command": "extensionId.doSomething",
        "title": "Do Something",
        "category": "Extension Name",
        "icon": "$(play)"
      }
    ]
  }
}
```

### Phase 2: Register Command in Extension Code

```typescript
import * as vscode from 'vscode';

export function activate(context: vscode.ExtensionContext) {
  // Register the command
  const disposable = vscode.commands.registerCommand(
    'extensionId.doSomething',
    async (args) => {
      // Command implementation
      vscode.window.showInformationMessage('Something done!');
    }
  );

  context.subscriptions.push(disposable);
}
```

### Phase 3: Configure Visibility

**Regular commands** (Command Palette visible):
```json
{
  "command": "extensionId.command",
  "title": "Command Name",
  "category": "Extension Name"
}
```

**Side Bar commands** (not in Command Palette):
```json
{
  "command": "extensionId.command#sideBar",
  "title": "Command Name",
  "icon": "$(gear)",
  "enablement": "view == extensionId.view"
}
```

**Context menu commands:**
```json
{
  "view/title": [
    {
      "command": "extensionId.refresh",
      "when": "view == extensionId.view",
      "group": "navigation"
    }
  ],
  "view/item/context": [
    {
      "command": "extensionId.delete",
      "when": "view == extensionId.view && viewItem == deletable",
      "group": "inline"
    }
  ]
}
```

### Phase 4: Set Enablement Conditions

Control when commands are available:

```json
// In menu contributions
"when": "editorLangId == typescript"
"when": "view == myView && viewItem == fileItem"
"when": "config.myExtension.enableFeature"
"when": "resourceExtname == .json"

// In code
vscode.commands.executeCommand(
  'setContext',
  'myExtension.isFeatureAvailable',
  true
);
```

## Command Types

| Type | Naming | Visible In | Needs Icon |
|------|--------|------------|------------|
| Regular | `ext.commandName` | Command Palette | No (unless in Side Bar) |
| Side Bar | `ext.commandName#sideBar` | Side Bar only | Yes |
| Context Menu | `ext.commandName` | Right-click menu | Optional |
| View Title | `ext.commandName` | View header | Yes |

## Verification Checklist

- [ ] All commands have `title` field
- [ ] Commands used in Command Palette have `category`
- [ ] Side Bar commands have `icon` and `#sideBar` suffix
- [ ] Enablement conditions (`when`) configured appropriately
- [ ] Command handler registered in `activate()` function
- [ ] Command strings are localized (use `vscode-ext-localization`)
- [ ] Context menu commands have correct `group` placement

## Usage Examples

```bash
# Generate command scaffold
vscode-ext-commands --generate --name "doSomething" --category "MyExtension"

# Validate command definitions
vscode-ext-commands --validate package.json

# List all commands in extension
vscode-ext-commands --list
```

## Error Handling

- **Missing title:** Every command MUST have a `title` or VS Code will show the raw command ID in the Command Palette and error logs
- **Duplicate command IDs:** Warns, prevents duplicate registration
- **Invalid visibility config:** Warns with line numbers
- **Icon not found:** Falls back to default icon, warns

## Pitfalls

- **Missing `context.subscriptions.push()`:** Commands won't be disposed properly, causing memory leaks
- **Missing `category`:** Commands appear in "Other" category in Command Palette, harder to discover
- **Invalid `when` clause:** VS Code silently ignores commands with invalid conditions
- **Hardcoded strings in title:** Use localization references (`%key%`) for internationalization
- **Conflicting keybindings:** Check existing VS Code keybindings before assigning shortcuts

## Verification Checklist

- [ ] All commands have `title` field
- [ ] Commands used in Command Palette have `category`
- [ ] Side Bar commands have `icon` and `#sideBar` suffix
- [ ] Enablement conditions (`when`) configured appropriately
- [ ] Command handler registered in `activate()` function
- [ ] Command strings are localized (use `vscode-ext-localization`)
- [ ] Context menu commands have correct `group` placement

## Skills Required

| Skill | Purpose |
|-------|---------|
| `terminal` | CLI commands execution |
| `file` | Read/write files |

## Related Skills

- `vscode-ext-localization` — Localize command titles
- `vscode-extension-playbook` — Extension architecture
- `vscode-cli` — Control VS Code from terminal

## References

- VS Code Commands API: <https://code.visualstudio.com/api/references/contribution-points#contributes.commands>
- Command Palette: <https://code.visualstudio.com/docs/getstarted/userinterface#_command-palette>
- `references/vscode-command-patterns.md` — Common command patterns and anti-patterns