# VS Code Extension Mapping

Use `code --list-extensions --show-versions` to refresh this inventory before changing the mapping.

| Extension | Primary Hermes skill / workflow | Why it matters |
| --- | --- | --- |
| `aaron-bond.better-comments` | `systematic-debugging` | Comment markers for TODO/FIXME/HACK/NOTE; use to annotate investigation paths and risk flags. |
| `bierner.color-info` | `frontend-design` | Inspect color values in CSS/UI work. |
| `bierner.markdown-preview-github-styles` | `project-docs` | Preview markdown with GitHub styling before publishing docs. |
| `bradlc.vscode-tailwindcss` | `frontend-design` | Tailwind class completion and validation. |
| `christian-kohler.npm-intellisense` | `context7` | Package/import discovery; verify package usage from docs. |
| `csstools.postcss` | `frontend-design` | PostCSS-aware CSS authoring. |
| `davidanson.vscode-markdownlint` | `writing-clearly-and-concisely` | Enforce concise, valid markdown structure. |
| `donjayamanne.githistory` | `git-helper` | Browse file and commit history for investigations. |
| `dsznajder.es7-react-js-snippets` | `frontend-design` | React snippet authoring. |
| `editorconfig.editorconfig` | `simplify` | Normalize editor formatting across files. |
| `esbenp.prettier-vscode` | `simplify` | Format code and docs consistently. |
| `formulahendry.auto-rename-tag` | `frontend-design` | Keep paired markup tags in sync. |
| `github.vscode-github-actions` | `github-pr-workflow` | Review and edit GitHub Actions workflows. |
| `humao.rest-client` | `httpie` | Send and inspect HTTP requests directly in the editor. |
| `kisstkondoros.vscode-gutter-preview` | `frontend-design` | Preview images and assets inline while editing. |
| `mechatroner.rainbow-csv` | `xlsx` | Inspect CSV/TSV data with alignment and delimiters. |
| `mhutchie.git-graph` | `git-helper` | Visualize branch topology and commit history. |
| `ms-playwright.playwright` | `webapp-testing` | Run and debug browser tests from VS Code. |
| `ms-python.debugpy` | `systematic-debugging` | Python debugger integration. |
| `ms-python.python` | `jupyter-live-kernel` | Python language/runtime support. |
| `ms-python.vscode-pylance` | `systematic-debugging` | Static analysis and type feedback for Python. |
| `ms-python.vscode-python-envs` | `asdf` | Manage Python environments and interpreter selection. |
| `ms-vscode.powershell` | `windows-maintenance-operations` | PowerShell editing and debugging on Windows. |
| `ms-vscode.vscode-chat-customizations-evaluations` | `writing-skills` | Evaluate chat customizations and prompt behavior. |
| `mtxr.sqltools` | `systematic-debugging` | Inspect and run SQL queries while debugging data issues. |
| `naumovs.color-highlight` | `frontend-design` | Highlight color values inline. |
| `oven.bun-vscode` | `context7` | Bun runtime support — IntelliSense, debug, run. |
| `pflannery.vscode-versionlens` | `clonedeps` | Track dependency versions and available updates. |
| `pkief.material-icon-theme` | `frontend-design` | Improve file-type recognition in the editor. |
| `pulkitgangwar.nextjs-snippets` | `frontend-design` | Next.js snippet authoring. |
| `quicktype.quicktype` | `code-docs` | Generate types from JSON and schemas. |
| `usernamehw.errorlens` | `verification-before-completion` | Surface diagnostics inline before claiming work is done. |
| `vitest.explorer` | `test-driven-development` | Run and organize Vitest test execution. |
| `yoavbls.pretty-ts-errors` | `systematic-debugging` | Improve TypeScript error readability. |
| `yzhang.markdown-all-in-one` | `project-docs` | Markdown authoring shortcuts and structure tools. |
| `zainchen.json` | `code-docs` | JSON editing, formatting, and schema work. |

## Removed Extensions

| Extension | Reason | Replacement |
|-----------|--------|-------------|
| `gamunu.vscode-yarn` | Bun is the package manager | `oven.bun-vscode` |
| `wayou.vscode-todo-highlight` | Superseded by Better Comments | `aaron-bond.better-comments` |
| `jacobdufault.fuzzy-search` | v0.0.3, unmaintained, built-in Ctrl+P suffices | Built-in VS Code search |
| `pnp.polacode` | Low utility, no project use | VS Code built-in screenshot |
