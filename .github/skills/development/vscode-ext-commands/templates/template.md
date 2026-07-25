# Command: {{ COMMAND_ID }}

## Declaration

```json
{
  "contributes": {
    "commands": [
      {
        "command": "{{ extension.id }}.{{ commandName }}",
        "title": "{{ Display Title }}",
        "category": "{{ Extension Name }}",
        "icon": "$({{ iconName }})"
      }
    ]
  }
}
```

## Registration

```typescript
vscode.commands.registerCommand('{{ extension.id }}.{{ commandName }}', async (args) => {
  // {{ handle the command }}
})
```

## Visibility

- [ ] Command Palette: {{ yes/no }}
- [ ] Side Bar: {{ yes/no }}
- [ ] Context Menu: {{ yes/no }}
- [ ] View Title: {{ yes/no }}

## Enablement

```json
"when": "{{ whenClause }}"
```

## Localization

- [ ] Title localized (see vscode-ext-localization)
- [ ] Description localized (see vscode-ext-localization)

## Verification

- [ ] Command title shows correctly in the Command Palette
- [ ] Enablement conditions work as expected
- [ ] Icon displays correctly (if applicable)
- [ ] Command executes the expected behavior
- [ ] No naming collisions with other extensions