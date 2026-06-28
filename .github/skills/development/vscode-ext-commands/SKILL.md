---
author: Hermes Agent
description: Use when adding, updating, or refactoring commands in VS Code extension
  development. Covers command registration, naming conventions, visibility, and menu
  contributions.
license: MIT
metadata:
  hermes:
    tags:
    - imported
name: vscode-ext-commands
tags:
- vscode
- extension
- commands
- ide
title: VS Code Extension Commands
version: 1.0.0

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

- Creating new views or webviews (use vscode-extension-playbook)
- Localizing command strings (use vscode-ext-localization)
- Extension packaging or publishing

## Skills Required

| Skill | Purpose |
|-------|---------|
| `vscode-ext-localization` | Localize command titles |
| `vscode-extension-playbook` | Extension architecture |

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
- [ ] Command strings are localized (use vscode-ext-localization)
- [ ] Context menu commands have correct `group` placement

## Pitfalls

- **Missing title:** Every command MUST have a `title` or VS Code will show the raw command ID
- **Naming collisions:** Use `extensionId.commandName` pattern to avoid conflicts
- **Too many commands:** Group related commands under submenus instead of flat lists
- **Wrong group:** Commands in wrong `group` appear in unexpected positions
- **Missing enablement:** Commands that should be context-dependent need `when` clauses
