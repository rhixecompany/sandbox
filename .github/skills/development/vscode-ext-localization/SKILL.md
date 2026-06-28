---
author: Hermes Agent
description: Use when localizing VS Code extension resources — settings, commands,
  menus, views, walkthroughs, and user-facing strings. Covers all three localization
  approaches.
license: MIT
metadata:
  hermes:
    tags:
    - imported
name: vscode-ext-localization
tags:
- vscode
- extension
- localization
- l10n
- i18n
title: VS Code Extension Localization
version: 1.0.0

---
# VS Code Extension Localization

## Overview

Localize VS Code extension resources following the three official localization approaches. This skill covers localizing configurations (settings, commands, menus), walkthrough content, and in-code user-facing strings.

## When to Use

- Adding localization support to a new extension
- Localizing new or existing commands, settings, menus, views, or walkthroughs
- Translating user-facing strings in extension source code
- Adding a new language to an existing localized extension
- Reviewing localization completeness

## When NOT TO USE

- Creating new commands (use vscode-ext-commands)
- Extension architecture decisions (use vscode-extension-playbook)
- Non-extension localization tasks

## Skills Required

| Skill | Purpose |
|-------|---------|
| `vscode-ext-commands` | Define commands before localizing |
| `vscode-extension-playbook` | Extension structure |

## Workflow

### Phase 1: Identify Localizable Resources

VS Code has three localization approaches:

| Resource Type | Localization Method | File Pattern |
|--------------|---------------------|--------------|
| Settings, Commands, Menus, Views, Walkthrough titles/descriptions | `package.nls.LANGID.json` | `package.nls.pt-br.json` |
| Walkthrough step content (Markdown) | Language-specific Markdown files | `walkthrough/step1.pt-br.md` |
| In-code user messages and strings | `bundle.l10n.LANGID.json` | `bundle.l10n.pt-br.json` |

### Phase 2: Localize package.json Resources

Create `package.nls.json` (default English) and `package.nls.LANGID.json` for each language:

```json
// package.nls.json (default)
{
  "extension.myCommand.title": "Do Something",
  "extension.mySetting.enabled.label": "Enable Feature",
  "extension.myView.title": "My View"
}

// package.nls.pt-br.json (Brazilian Portuguese)
{
  "extension.myCommand.title": "Fazer Algo",
  "extension.mySetting.enabled.label": "Habilitar Recurso",
  "extension.myView.title": "Minha Visualização"
}
```

Reference in package.json:
```json
{
  "contributes": {
    "commands": [{
      "command": "extension.myCommand",
      "title": "%extension.myCommand.title%"
    }],
    "configuration": {
      "properties": {
        "myExtension.enabled": {
          "type": "boolean",
          "default": true,
          "description": "%extension.mySetting.enabled.label%"
        }
      }
    }
  }
}
```

### Phase 3: Localize Walkthrough Content

Create language-specific Markdown files:

```
walkthrough/
├── getting-started.md          # Default (English)
├── getting-started.pt-br.json  # Brazilian Portuguese
├── getting-started.ja.md       # Japanese
└── getting-started.zh-cn.md    # Simplified Chinese
```

Each file contains the full translated content for that walkthrough step.

### Phase 4: Localize In-Code Strings

Use the `l10n` API in TypeScript/JavaScript:

```typescript
import * as l10n from '@vscode/l10n';

// Load language-specific bundle
const bundle = l10n.config({ locale: 'pt-br' });

// Use localized strings
vscode.window.showInformationMessage(
  l10n.t('Operation completed successfully!')
);
```

Create `bundle.l10n.json` files:

```json
// bundle.l10n.json (default)
{
  "operation completed successfully!": "Operation completed successfully!",
  "Error: {0}": "Error: {0}"
}

// bundle.l10n.pt-br.json
{
  "operation completed successfully!": "Operação concluída com sucesso!",
  "Error: {0}": "Erro: {0}"
}
```

### Phase 5: Verify Localization

1. All `%...%` references in package.json have entries in all language files
2. All walkthrough steps have translations for all supported languages
3. All user-facing strings in code use `l10n.t()` instead of hardcoded strings
4. Test with different VS Code language settings:
   ```json
   // settings.json
   "locale": "pt-br"
   ```

## Verification Checklist

- [ ] `package.nls.json` exists with all default strings
- [ ] `package.nls.LANGID.json` exists for each supported language
- [ ] All `%...%` references in package.json are covered in nls files
- [ ] Walkthrough content files exist for each language
- [ ] `bundle.l10n.json` exists with all default strings
- [ ] `bundle.l10n.LANGID.json` exists for each supported language
- [ ] All user-facing strings use `l10n.t()` API
- [ ] No hardcoded user-facing strings in source code

## Pitfalls

- **Missing translations:** Every key in the default file must have a translation in each language file
- **Hardcoded strings:** Any string shown to users must go through localization — grep for `showInformationMessage`, `showErrorMessage`, etc.
- **Wrong file naming:** Language codes must match VS Code's locale codes (e.g., `pt-br` not `pt_br`)
- **Missing walkthrough translations:** Walkthrough content is separate from package.nls files
- **Not testing with locale change:** Always test by changing VS Code's `locale` setting
