---
author: Hermes Agent
description: Localize VS Code extension commands, walkthroughs, configuration, and in-code strings for international users. Covers package.nls.json, walkthrough translations, bundle.l10n.json, and the @vscode/l10n API.
license: MIT
metadata:
  hermes:
    tags: [imported, vscode, extension, i18n, localization, l10n]
name: vscode-ext-localization
tags:
- imported
- vscode
- extension
- i18n
- localization
- l10n
- scripts
title: VS Code Extension Localization
version: 1.1.0
---

# VS Code Extension Localization

## Overview

Localize VS Code extension commands, walkthroughs, configuration, and in-code strings for international users. Covers package.nls.json, walkthrough translations, bundle.l10n.json, and the @vscode/l10n API.

## When to Use

- Adding translations to VS Code extension package metadata
- Localizing walkthrough/getting-started content
- Translating configuration schema descriptions
- Internationalizing in-code user-facing strings
- Preparing extension for VS Code Marketplace global audience

## When NOT to Use

- **Creating new commands** — Use `vscode-ext-commands` for command development
- **Building extension architecture** — Use `vscode-extension-playbook`
- **Packaging/publishing** — Use `vsce` CLI

## Workflow

### Phase 1: Localize package.json Strings (package.nls.json)

Create language-specific JSON files for all user-facing strings in package.json:

```bash
# Default (English)
package.nls.json
# Brazilian Portuguese
package.nls.pt-br.json
# Japanese
package.nls.ja.json
# Simplified Chinese
package.nls.zh-cn.json
```

```json
// package.nls.json (default)
{
  "extension.mySetting.enabled.label": "Enable Feature",
  "extension.mySetting.enabled.description": "Enables the experimental feature",
  "extension.commands.doSomething.title": "Do Something",
  "extension.commands.doSomething.category": "My Extension"
}

// package.nls.pt-br.json
{
  "extension.mySetting.enabled.label": "Ativar Recurso",
  "extension.mySetting.enabled.description": "Ativa o recurso experimental",
  "extension.commands.doSomething.title": "Fazer Algo",
  "extension.commands.doSomething.category": "Minha Extensão"
}
```

In package.json, reference using `%key%`:
```json
{
  "contributes": {
    "commands": [
      {
        "command": "myExt.doSomething",
        "title": "%extension.commands.doSomething.title%",
        "category": "%extension.commands.doSomething.category%"
      }
    ],
    "configuration": {
      "properties": {
        "myExt.enabled": {
          "type": "boolean",
          "default": true,
          "description": "%extension.mySetting.enabled.description%"
        }
      }
    }
  }
}
```

### Phase 2: Localize Walkthrough Content

Create language-specific Markdown files:

```
walkthrough/
├── getting-started.md          # Default (English)
├── getting-started.pt-br.md    # Brazilian Portuguese
├── getting-started.ja.md       # Japanese
├── getting-started.zh-cn.md    # Simplified Chinese
```

Each file contains the full translated content for that walkthrough step.

### Phase 3: Localize In-Code Strings (bundle.l10n.json)

Use the `@vscode/l10n` API in TypeScript/JavaScript:

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
  "Operation completed successfully!": "Operation completed successfully!",
  "Error: {0}": "Error: {0}"
}

// bundle.l10n.pt-br.json
{
  "Operation completed successfully!": "Operação concluída com sucesso!",
  "Error: {0}": "Erro: {0}"
}
```

### Phase 4: Verify Localization

1. All `%...%` references in package.json have entries in all language files
2. All walkthrough steps have translations for all supported languages
3. All user-facing strings in code use `l10n.t()` instead of hardcoded strings
4. Test with different VS Code language settings:
   ```json
   // settings.json
   "locale": "pt-br"
   ```

## Usage Examples

```bash
# Extract strings for localization
vscode-ext-localization --extract package.json --output package.nls.json

# Validate all translations exist
vscode-ext-localization --validate --languages pt-br,ja,zh-cn

# Check for hardcoded strings
vscode-ext-localization --check-hardcoded src/
```

## Error Handling

- **Missing translation key:** Warns with missing key and language
- **Duplicate keys in nls file:** Exits with code 1, prints duplicates
- **Invalid locale code:** Exits with code 1, lists valid VS Code locales
- **Walkthrough file missing:** Warns, lists missing language files

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

## Verification Checklist

- [ ] `package.nls.json` exists with all default strings
- [ ] `package.nls.LANGID.json` exists for each supported language
- [ ] All `%...%` references in package.json are covered in nls files
- [ ] Walkthrough content files exist for each language
- [ ] `bundle.l10n.json` exists with all default strings
- [ ] `bundle.l10n.LANGID.json` exists for each supported language
- [ ] All user-facing strings use `l10n.t()` API
- [ ] No hardcoded user-facing strings in source code

## Skills Required

| Skill | Purpose |
|-------|---------|
| `terminal` | CLI commands execution |
| `file` | Read/write files |

## Related Skills

- `vscode-ext-commands` — Command development (strings to localize)
- `vscode-extension-playbook` — Extension architecture
- `vscode-cli` — Control VS Code from terminal

## References

- VS Code Localization Guide: <https://code.visualstudio.com/api/references/extension-manifest#localization>
- l10n API: <https://code.visualstudio.com/api/extension-guides/localization>
- VS Code Locale Codes: <https://code.visualstudio.com/docs/getstarted/locales>
- `references/vscode-l10n-patterns.md` — Localization patterns and best practices