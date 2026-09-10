# VS Code Stable Uninstall + Code-Insiders Full Configuration

## Overview
Uninstall stable VS Code, keep Code-Insiders, configure all settings for every installed extension mapped to file types, and verify full functionality.

## Prerequisites
- Confirmed: Code-Insiders at `C:\Users\Alexa\AppData\Local\Programs\Microsoft VS Code Insiders\`
- Confirmed: Stable VS Code at `C:\Users\Alexa\AppData\Local\Programs\Microsoft VS Code\`
- Confirmed: ~70 extensions installed in Code-Insiders
- Confirmed: User has approved destructive operations

## Extension Inventory (70+ installed)

### Language/Formatters
| Extension | File Types | Role |
|-----------|-----------|------|
| esbenp.prettier-vscode | js, ts, json, jsonc, md, yaml, css, scss, toml | Default formatter |
| charliermarsh.ruff | python | Linter + formatter |
| ms-python.black-formatter | python | Black formatter |
| tamasfe.even-better-toml | toml | TOML formatter |
| foxundermoon.shell-format | shellscript | Shell formatter |
| timonwong.shellcheck | shellscript | Shell linter |
| davechanru.vscode-django-templates | django-html, django-txt | Django templates |
| ms-toolsai.jupyter | jupyter, python | Jupyter notebook |

### Language Servers
| Extension | File Types | Role |
|-----------|-----------|------|
| ms-python.vscode-pylance | python | Python language server |
| ms-python.python | python | Python interpreter |
| golang.go | go | Go language server |
| redhat.java | java | Java language server |
| ms-dotnettools.csharp | csharp | C# language server |
| ms-dotnettools.csdevkit | csharp, cs, csx | C# dev kit |
| rust-lang.rust-analyzer | rust | Rust language server |
| redhat.vscode-xml | xml | XML language server |
| redhat.vscode-yaml | yaml | YAML language server |
| ms-vscode.vscode-typescript-next | typescript, tsx | TypeScript language server |
| dskwrk.vscode-generate-getter-setter | typescript, javascript | Getter/setter generator |
| infeng.vscode-react-typescript | tsx, jsx | React/TS support |
| pmneo.tsimporter | typescript | TS importer |
| typescriptteam.native-preview | typescript | TS native preview |
| willluke.nextjs | typescript, javascript | Next.js support |
| xabikos.javascriptsnippets | javascript | JS snippets |
| rodrigovallades.es7-react-js-snippets | javascript, jsx | ES7 React snippets |
| burkeholland.simple-react-snippets | javascript, jsx | React snippets |
| cardinal90.multi-cursor-case-preserve | all | Multi-cursor preservation |
| loiane.ts-extension-pack | typescript | TS extension pack |
| mengsicode.vscode-django-boilerplate | python, django | Django boilerplate |

### Tools/Debgug
| Extension | File Types | Role |
|-----------|-----------|------|
| ms-python.debugpy | python | Python debugger |
| vscjava.vscode-java-debug | java | Java debugger |
| vscjava.vscode-maven | java, xml, pom | Maven support |
| ms-vscode.cmake-tools | cmake, cmakeLists | CMake tools |
| ms-vscode.makefile-tools | makefile | Makefile support |
| ms-playwright.playwright | javascript, typescript | Playwright testing |
| vitest.explorer | typescript, javascript | Vitest test runner |
| ms-toolsai.jupyter-keymap | jupyter | Jupyter keybindings |
| ms-toolsai.jupyter-renderers | jupyter | Jupyter renderers |

### Git/DevOps
| Extension | File Types | Role |
|-----------|-----------|------|
| eamodio.gitlens | all | Git blame/annotations |
| mhutchie.git-graph | all | Git graph visualization |
| donjayamanne.githistory | all | Git history |
| github.vscode-github-actions | yaml, github-actions | GitHub Actions |
| github.vscode-pull-request-github | all | PR management |
| ms-azuretools.vscode-containers | docker, dockerfile | Containers |
| formulahendry.auto-rename-tag | html, xml, vue | Auto-rename tags |
| editorconfig.editorconfig | all | EditorConfig support |
| dbaeumer.vscode-eslint | javascript, typescript | ESLint |
| davidanson.vscode-markdownlint | markdown | Markdown linting |
| yzhang.markdown-all-in-one | markdown | Markdown all-in-one |
| bierner.markdown-mermaid | markdown | Mermaid diagrams |
| bierner.markdown-preview-github-styles | markdown | Markdown preview styles |

### UI/Theme/Productivity
| Extension | File Types | Role |
|-----------|-----------|------|
| pkief.material-icon-theme | all | Material icons |
| usernamehw.errorlens | all | Error lens |
| naumovs.color-highlight | css, scss, html, less | Color highlighting |
| mechatroner.rainbow-csv | csv | Rainbow CSV |
| pflannery.vscode-versionlens | all | Version lens |
| streetsidesoftware.code-spell-checker | all | Spell checker |
| aaron-bond.better-comments | all | Better comments |
| esbenp.prettier-vscode | all | Prettier |
| njpwerner.autodocstring | python | Auto docstrings |
| cweijan.vscode-redis-client | redis | Redis client |
| qwtel.sqlite-viewer | sqlite | SQLite viewer |
| mtxr.sqltools | sql | SQL tools |
| prisma.prisma | graphql, prisma | Prisma support |
| quicktype.quicktype | json, typescript | QuickType |
| poppywu124.hermes-chat | all | Hermes chat |
| sst-dev.opencode | all | OpenCode |
| oven.bun-vscode | javascript, typescript | Bun support |
| bradlc.vscode-tailwindcss | css, scss, html | Tailwind CSS |
| batisteo.vscode-django | python | Django support |
| bierner.color-info | css, scss, html | Color info |
| bierner.markdown-preview-github-styles | markdown | Preview styles |
| ms-vscode.powershell | powershell | PowerShell |
| psulek-solo.zodschema-generator | typescript | Zod schema |
| inferrinizzard.prettier-sql-vscode | sql | Prettier SQL |
| ritwickdey.liveserver | html, css, js | Live server |
| visualstudioexptteam.intellicode-api-usage-examples | typescript | IntelliCode examples |
| visualstudioexptteam.vscodeintellicode | typescript | IntelliCode |
| mikaelkristiansson87.react-theme-vscode | typescript, jsx | React theme |
| xabikos.javascriptsnippets | javascript | JS snippets |

## Phases

### Phase 1: Uninstall Stable VS Code
- Step 1: Run standard uninstaller if available
- Step 2: Force-delete remaining Program Files directory
- Step 3: Clean registry entries
- Step 4: Delete leftover config/data/storage folders
- Step 5: Verify clean removal

### Phase 2: Build Extension-to-Filetype Mapping
- Step 1: Parse all installed extensions
- Step 2: Categorize by file type support
- Step 3: Create canonical mapping document

### Phase 3: Configure SandBox .vscode/ Settings
- Step 1: Configure settings.json (language-specific formatters, all extensions)
- Step 2: Configure tasks.json (ensure all tasks reference correct extensions)
- Step 3: Configure launch.json (ensure debug configs work with Code-Insiders)
- Step 4: Configure extensions.json (update recommendations)
- Step 5: Configure mcp.json (verify all MCP servers)

### Phase 4: Configure Code-Insiders Roaming User/ Settings
- Step 1: Configure User settings.json (language-specific formatters)
- Step 2: Verify tasks.json (currently empty `{}`)
- Step 3: Configure launch.json if needed
- Step 4: Configure extensions.json

### Phase 5: Verify All Extensions
- Step 1: Run code-insiders --health-check
- Step 2: Attempt to activate each extension
- Step 3: Check for errors in console logs
- Step 4: Fix any misconfigurations
- Step 5: Re-verify until clean

### Phase 6: Final Validation
- Step 1: Verify stable VS Code is fully removed
- Step 2: Verify Code-Insiders runs correctly
- Step 3: Verify all settings.json entries are valid JSON
- Step 4: Verify all extensions load without errors
- Step 5: Run final health check
- Step 6: Commit and document

## Resource Allocation
- Phase 1: 1 subagent (destructive, needs approval gate)
- Phase 2: 1 subagent (research/documentation)
- Phase 3: 1 subagent (config writing)
- Phase 4: 1 subagent (config writing)
- Phase 5: 1 subagent (verification/fixing)
- Phase 6: 1 subagent (final validation)

## Verification Gates
- Phase 1 Gate: `C:\Users\Alexa\AppData\Local\Programs\Microsoft VS Code\` does not exist, registry clean
- Phase 2 Gate: Extension-to-filetype mapping document covers all 70+ extensions
- Phase 3 Gate: All SandBox .vscode/*.json files are valid JSON with correct language mappings
- Phase 4 Gate: Code-Insiders Roaming User/ settings.json has all language-specific settings
- Phase 5 Gate: No extension activation errors, all known file types have formatters configured
- Phase 6 Gate: Final health check passes, all JSON configs valid, stable VS Code fully removed
