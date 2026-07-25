# VS Code Extension Commands — Reference Overview

## Key Concepts

- **VS Code Commands** are the fundamental building block for extension functionality. Each command is defined in `package.json` under `contributes.commands` and registered in the extension's `activate()` function via `vscode.commands.registerCommand`. Commands can be invoked from the Command Palette, keybindings, menus, or programmatically.
- **Command Naming Convention** — Commands should follow the `extensionId.commandName` pattern using camelCase (e.g., `myExtension.doSomething`). This prevents naming collisions between extensions. Side-bar-only commands use the `#sideBar` suffix to hide them from the Command Palette.
- **Visibility & Enablement** — Commands support `when` clauses for context-dependent visibility (e.g., `editorLangId == typescript`, `view == myView`). Side bar commands need icons. Context menu commands use `group` properties for placement (e.g., `navigation`, `inline`, `1_modification`).
- **Registration Lifecycle** — Command disposables should be added to `context.subscriptions` in the `activate()` function. This ensures proper cleanup when the extension is deactivated. Commands can use `vscode.commands.executeCommand('setContext', ...)` to dynamically control enablement conditions.
- **Localization** — Command titles should be localized for multi-language extensions. The `vscode-ext-localization` skill covers this workflow. Without localization, the raw command `title` string is displayed as-is.