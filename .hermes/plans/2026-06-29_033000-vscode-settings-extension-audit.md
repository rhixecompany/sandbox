---
status: completed
status: completed
status: completed
---
# Plan: VS Code Extension Settings Audit & Update

**Date:** 2026-06-29
**Author:** Alexa (Hermes Agent)
**Status:** Plan (not yet executed)

---

## Goal

Update both the **default** (`~/AppData/Roaming/Code/User/settings.json`) and **workspace** (`~/Desktop/SandBox/.vscode/settings.json`) VS Code settings files to include best-practice configuration for all **42 installed extensions**, and attempt to discover and incorporate extension documentation for settings.

---

## Context / Current State

### Installed Extensions (42 total)
Already inventoried — 42 extensions across 9+ categories: Python (5), JS/TS/React (6), Git (4), Markdown (3), Shell/Config (3), CSS (2), Testing (2), Visual (5), REST/SQL (2), Misc (5).

### Default settings.json (`~/AppData/Roaming/Code/User/settings.json`)
- 265 lines, 7.5KB
- Language formatters fully defined for 11 languages
- Python (Pylance), prettier, markdownlint, better-comments, Tailwind, git, terminal profiles configured
- **Missing config** for: ruff, Playwright, rest-client, sqltools, gitlens, git-graph, githistory, errorlens, color-highlight, color-info, gutter-preview, rainbow-csv, npm-intellisense, versionlens, pretty-ts-errors, auto-rename-tag, prettier (partial), vscode-pull-request-github, vscode-github-actions, vscode-python-envs, hermes-chat, ChatGPT, shell-format, postcss, vitest, etc.

### Workspace settings.json (`~/Desktop/SandBox/.vscode/settings.json`)
- 88 lines, 2.3KB
- Subset of default settings with local overrides (terminal profile = Git Bash, uv-env enabled)
- **Missing** similarly — very minimal extension config

---

## Approach

Two-phase approach:
1. **Research** — Fetch docs/readme from each extension's marketplace page to discover available settings
2. **Update** — Apply best-practice settings file-by-file

Given 42 extensions, batch the research (firecrawl-scrape marketplace pages) and settings generation.

---

## Step-by-Step Plan

### Phase 1: Research Extension Settings (batch of ≤7 extensions per call)
For each extension ID, fetch its VS Code marketplace page to extract settings/config docs:
- URL pattern: `https://marketplace.visualstudio.com/items?itemName={publisher}.{name}`
- Extract: settings schema, recommended defaults, key configuration groups

**Extensions to research (grouped by category):**
1. **Python:** ms-python.python, ms-python.vscode-pylance, ms-python.debugpy, ms-python.vscode-python-envs, charliermarsh.ruff
2. **JS/TS:** dbaeumer.vscode-eslint, esbenp.prettier-vscode, dsznajder.es7-react-js-snippets, bradlc.vscode-tailwindcss, yoavbls.pretty-ts-errors, christian-kohler.npm-intellisense
3. **Git:** eamodio.gitlens, mhutchie.git-graph, donjayamanne.githistory, github.vscode-pull-request-github, github.vscode-github-actions
4. **Markdown:** davidanson.vscode-markdownlint, yzhang.markdown-all-in-one, bierner.markdown-preview-github-styles
5. **Shell/Config:** foxundermoon.shell-format, editorconfig.editorconfig, zainchen.json
6. **CSS:** csstools.postcss, bradlc.vscode-tailwindcss (already listed)
7. **Testing:** vitest.explorer, ms-playwright.playwright
8. **Visual:** aaron-bond.better-comments, usernamehw.errorlens, naumovs.color-highlight, bierner.color-info, kisstkondoros.vscode-gutter-preview
9. **REST/SQL:** humao.rest-client, mtxr.sqltools
10. **Misc:** ms-vscode.powershell, openai.chatgpt, poppywu124.hermes-chat, mechatroner.rainbow-csv, oven.bun-vscode, pflannery.vscode-versionlens, quicktype.quicktype, formulahendry.auto-rename-tag, batisteo.vscode-django, pkief.material-icon-theme

### Phase 2: Generate Settings Config
For each extension, produce a best-practice config block based on:
- Official marketplace / GitHub docs
- Common community best practices
- Project-specific needs (Python + JS/TS in SandBox)

### Phase 3: Update Default settings.json
Apply extension config blocks to `~/AppData/Roaming/Code/User/settings.json`:
- Organize by extension (alphabetical or by category)
- Add comments for each block
- Preserve all existing settings
- Verify syntax after update

### Phase 4: Update Workspace settings.json
Apply workspace-appropriate subset to `~/Desktop/SandBox/.vscode/settings.json`:
- Include settings that differ from default (terminal, uv, python-envs)
- Add extension configs that matter at project level
- Verify syntax after update

### Phase 5: Update extensions.json
Sync `.vscode/extensions.json` recommendations to match the 42 installed extensions:
- Add missing extensions to `recommendations`
- Move intentionally unneeded ones to `unwantedRecommendations`

### Phase 6: Verification
- Run `code --list-extensions` — confirm no drift
- Validate JSON syntax of both settings files (`python3 -m json.tool`)
- Confirm all 42 extensions have at least baseline config
- Report any extensions where docs were unavailable

---

## Files Likely to Change

| File | Action |
|------|--------|
| `~AppData/Roaming/Code/User/settings.json` | Update — add missing extension configs |
| `~/Desktop/SandBox/.vscode/settings.json` | Update — add project-relevant extension configs |
| `~/Desktop/SandBox/.vscode/extensions.json` | Update — sync recommendations |
| `~AppData/Roaming/Code/User/keybindings.json` | Read-only check (if exists) |

---

## Risks & Trade-offs

| Risk | Likelihood | Impact | Mitigation |
|------|-----------|--------|------------|
| Extension docs unavailable / generic | Medium | Low | Use well-known defaults; skip obscurely-documented settings |
| settings.json syntax error after edit | Low | High | Validate with `python3 -m json.tool` after every batch |
| Settings conflict between extensions | Low | Medium | Prefer extension-specific scoping (`[lang]` blocks) |
| Workspace override silently overrides default | Low | Low | Document which settings differ in workspace vs default |
| Rate limiting from marketplace | Low | Medium | Batch requests; use web_extract/firecrawl with spacing |

---

## Verification

- [ ] `python3 -m json.tool` passes on both settings files
- [ ] All 42 extensions have at least one setting configured
- [ ] No duplicate or conflicting config keys
- [ ] `.vscode/extensions.json` references all installed extensions
- [ ] VS Code loads without errors (can be verified with `code --status`)
