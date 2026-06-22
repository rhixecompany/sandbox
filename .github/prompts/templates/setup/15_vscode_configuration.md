# 15. VSCode Configuration

> Extracted from `setup.prompt.md`.

## 15. VSCode Configuration

### Settings (`.vscode/settings.json`)

```json
{
  "editor.defaultFormatter": "esbenp.prettier-vscode",
  "editor.formatOnSave": true,
  "editor.tabSize": 2,
  "eslint.lintTask.enable": true,
  "eslint.useFlatConfig": true,
  "eslint.validate": ["javascript", "typescript", "typescriptreact"],
  "explorer.fileNesting.enabled": true,
  "explorer.fileNesting.patterns": {
    "*.ts": "${capture}.test.ts, ${capture}.spec.ts",
    "*.tsx": "${capture}.test.tsx, ${capture}.spec.tsx"
  }
}
```

### Extensions (`.vscode/extensions.json`)

```json
{
  "recommendations": [
    "dbaeumer.vscode-eslint",
    "esbenp.prettier-vscode",
    "bradlc.vscode-tailwindcss",
    "PulkitGangwar.nextjs-snippets",
    "vitest.explorer"
  ],
  "unwantedRecommendations": [
    "hookyqr.beautify",
    "dbaeumer.jshint",
    "eg2.tslint"
  ]
}
```

---
