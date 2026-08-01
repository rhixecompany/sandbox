# VS Code Config Audit Report

**Generated:** 2026-07-24  
**Scope:** User config + workspace `.vscode/`  
**Auditor:** vscode-config-audit skill

---

## Summary

| Category | Issues | Severity |
|----------|--------|----------|
| ESLint | 0 ✅ | — |
| Paths | 0 ✅ | — |
| Extensions | 5 ⚠️ | Low |
| Formatters | 0 ✅ | — |
| Tasks | 2 ⚠️ | Medium |
| Launch | 3 ⚠️ | Low |

**Total: 10 issues found (0 critical, 2 medium, 8 low)**

---

## 1. ESLint — ✅ Clean

`dbaeumer.vscode-eslint` is in `extensions.json` and `settings.json` references `source.fixAll.eslint`. No issues.

## 2. Paths — ✅ Clean

All paths in `settings.json` use `${workspaceFolder}` variable. No hardcoded `C:\Users\...` paths.

## 3. Extensions — ⚠️ 5 Missing Recommendations

| Missing Extension | Purpose | Stack Evidence |
|---|---|---|
| `redhat.vscode-yaml` | YAML editing (GitHub Actions, MCP configs) | `.github/workflows/*.yml`, `.markdownlintrc.json` |
| `streetsidesoftware.code-spell-checker` | Spellcheck | `cspell` MCP server + `cspell.json` configured |
| `timonwong.shellcheck` | Shell script lint | `scripts/*.sh`, `hooks/*.sh` |
| `ms-azuretools.vscode-docker` | Docker support | `Dockerfile`, `docker-compose.yml` |
| `bierner.markdown-mermaid` | Mermaid diagram preview | `*.md` files with mermaid blocks |
| `eamodio.gitlens` | Git history/blame | Multi-repo workspace |

## 4. Formatters — ✅ Clean

Single formatter per language. `editor.formatOnSave: true` globally.  
`ms-python.python` for Python, `esbenp.prettier-vscode` for JS/TS/CSS/SCSS, `vscode.html-language-features` for HTML, `foxundermoon.shell-format` for shell.

## 5. Tasks — ⚠️ 2 Issues

| Task | Issue | Fix |
|------|-------|-----|
| `Python: Test All` | Missing `problemMatcher` for pytest output | Add `$python.pytest` |
| `Python: Lint` | Missing `problemMatcher` for ruff output | Add `$ruff` or `$eslint-stylish` |
| Both | Missing `options.cwd` (runs from last active dir) | Add `"options": {"cwd": "${workspaceFolder}"}` |

## 6. Launch — ⚠️ 3 Issues

| Config | Issue | Fix |
|--------|-------|-----|
| `Python: Current File` | Missing `justMyCode: true` | Add `"justMyCode": true` |
| `Python: Current File` | Missing `python` path override | Uses default interpreter; add explicit `"python": "${workspaceFolder}/myvenv/Scripts/python.exe"` |
| All 4 | No `cwd` set | Add `"cwd": "${workspaceFolder}"` |

---

## Recommended Actions

1. Add missing extensions to `extensions.json`
2. Add `problemMatcher` and `cwd` to `tasks.json`
3. Add `justMyCode` and `cwd` to `launch.json`
4. No changes needed for `settings.json`, `mcp.json`

---
