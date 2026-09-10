# Extension-to-Filetype Mapping — Code-Insiders

Generated: 2026-09-10
Source: code-insiders --list-extensions --show-versions

## Extension → File Type → Configuration

### Prettier (esbenp.prettier-vscode)
- Files: .js, .jsx, .ts, .tsx, .json, .jsonc, .css, .scss, .less, .md, .mdx, .yaml, .yml, .toml, .html, .vue, .svelte, .graphql, .sh, .bash, .zsh
- Config: editor.defaultFormatter for all listed languages

### Ruff (charliermarsh.ruff)
- Files: .py, .pyi, .pyw
- Config: editor.defaultFormatter for python, python.linting.*

### Black Formatter (ms-python.black-formatter)
- Files: .py, .pyi, .pyw
- Config: python.formatting.provider = "black"

### Even Better TOML (tamasfe.even-better-toml)
- Files: .toml, .tml, .ctoml
- Config: editor.defaultFormatter for toml

### Shell Format (foxundermoon.shell-format)
- Files: .sh, .bash, .zsh, .fish, .awk, .bashrc, .bash_profile
- Config: editor.defaultFormatter for shellscript

### ShellCheck (timonwong.shellcheck)
- Files: .sh, .bash, .zsh, .fish
- Config: shellcheck.*

### Pylance (ms-python.vscode-pylance)
- Files: .py, .pyi, .pyw
- Config: python.analysis.*

### Python (ms-python.python)
- Files: .py, .pyi, .pyw
- Config: python.defaultInterpreterPath

### Debugpy (ms-python.debugpy)
- Files: .py, .pyi, .pyw
- Config: debugpy settings

### Go (golang.go)
- Files: .go, .mod, .sum
- Config: editor.defaultFormatter for go, go.*

### Java (redhat.java)
- Files: .java, .jav
- Config: java.*

### C# (ms-dotnettools.csharp)
- Files: .cs, .csx, .cshtml
- Config: csharp.*

### C# Dev Kit (ms-dotnettools.csdevkit)
- Files: .cs, .csx, .cshtml
- Config: dotnet.*

### Rust Analyzer (rust-lang.rust-analyzer)
- Files: .rs, .rust
- Config: rust-analyzer.*

### XML (redhat.vscode-xml)
- Files: .xml, .xsd, .xslt, .wsdl, .svg
- Config: xml.*

### YAML (redhat.vscode-yaml)
- Files: .yaml, .yml, .yaml-templates, .json-templates
- Config: yaml.*

### TypeScript Next (ms-vscode.vscode-typescript-next)
- Files: .ts, .tsx, .js, .jsx
- Config: editor.defaultFormatter for typescript, typescript.*

### React TypeScript (infeng.vscode-react-typescript)
- Files: .tsx, .jsx
- Config: typescript.react.*

### React Snippets (burkeholland.simple-react-snippets)
- Files: .jsx, .tsx
- Config: (snippets only, no formatter)

### JS Snippets (xabikos.javascriptsnippets)
- Files: .js
- Config: (snippets only, no formatter)

### ES7 React Snippets (rodrigovallades.es7-react-js-snippets)
- Files: .jsx, .tsx
- Config: (snippets only, no formatter)

### TypeScript Importer (pmneo.tsimporter)
- Files: .ts, .tsx
- Config: (import ordering)

### TypeScript Native Preview (typescriptteam.native-preview)
- Files: .ts, .tsx
- Config: (preview settings)

### Next.js (willluke.nextjs)
- Files: .tsx, .jsx, .next, .js
- Config: next.*

### QuickType (quicktype.quicktype)
- Files: .json, .ts, .tsx
- Config: (quicktype integration)

### Prisma (prisma.prisma)
- Files: .prisma, .graphql, .gql
- Config: prisma.*

### GraphQL (via Prisma extension)
- Files: .graphql, .gql
- Config: (graphql language server)

### PostgreSQL (via ms-toolsai.jupyter)
- Files: .sql, .psql, .postgresql
- Config: (sql language server)

### SQLite Viewer (qwtel.sqlite-viewer)
- Files: .sqlite, .sqlite3, .db
- Config: (sqlite viewer)

### SQL Tools (mtxr.sqltools)
- Files: .sql
- Config: sql-tools.*

### Prettier SQL (inferrinizzard.prettier-sql-vscode)
- Files: .sql, .ddl, .dml
- Config: (sql formatting)

### Docker (ms-azuretools.vscode-containers)
- Files: .dockerfile, Dockerfile, .containerfile, .devcontainer
- Config: docker.*

### CMake Tools (ms-vscode.cmake-tools)
- Files: CMakeLists.txt, .cmake, .cmakelists
- Config: cmake.*

### Makefile Tools (ms-vscode.makefile-tools)
- Files: Makefile, makefile, GNUmakefile
- Config: makefile.*

### Playwright (ms-playwright.playwright)
- Files: .spec.ts, .test.ts, .spec.js, .test.js, .spec.tsx
- Config: playwright.*

### Vitest Explorer (vitest.explorer)
- Files: .test.ts, .test.tsx, .test.js, .spec.ts, .spec.tsx
- Config: vitest.*

### Jupyter (ms-toolsai.jupyter)
- Files: .ipynb, .jupyter
- Config: jupyter.*

### Jupyter Keymap (ms-toolsai.jupyter-keymap)
- Files: .ipynb
- Config: jupyter-keymap.*

### Jupyter Renderers (ms-toolsai.jupyter-renderers)
- Files: .ipynb
- Config: jupyter-renderers.*

### GitHub Actions (github.vscode-github-actions)
- Files: .github/workflows/*.yml, .github/workflows/*.yaml
- Config: github-actions.*

### PR GitHub (github.vscode-pull-request-github)
- Files: .github/pull_request_templates/*.md
- Config: (PR integration)

### GitLens (eamodio.gitlens)
- Files: All (overlay)
- Config: gitlens.*

### Git Graph (mhutchie.git-graph)
- Files: All (overlay)
- Config: git-graph.*

### Git History (donjayamanne.githistory)
- Files: All (overlay)
- Config: githistory.*

### EditorConfig (editorconfig.editorconfig)
- Files: All
- Config: editorconfig.*

### ESLint (dbaeumer.vscode-eslint)
- Files: .js, .jsx, .ts, .tsx, .mjs, .cjs
- Config: eslint.*

### Markdownlint (davidanson.vscode-markdownlint)
- Files: .md, .mdx, .markdown
- Config: markdownlint.*

### Markdown All in One (yzhang.markdown-all-in-one)
- Files: .md, .mdx, .markdown
- Config: markdown.*

### Mermaid (bierner.markdown-mermaid)
- Files: .md, .mdx
- Config: markdown-mermaid.*

### Markdown Preview GitHub Styles (bierner.markdown-preview-github-styles)
- Files: .md, .mdx
- Config: markdown-preview-github-styles.*

### Material Icon Theme (pkief.material-icon-theme)
- Files: All (icons)
- Config: workbench.iconTheme

### Error Lens (usernamehw.errorlens)
- Files: All (overlay)
- Config: errorLens.*

### Color Highlight (naumovs.color-highlight)
- Files: .css, .scss, .less, .html, .svg
- Config: color-highlight.*

### Rainbow CSV (mechatroner.rainbow-csv)
- Files: .csv, .tsv
- Config: rainbow-csv.*

### Version Lens (pflannery.vscode-versionlens)
- Files: All (overlay)
- Config: versionlens.*

### Code Spell Checker (streetsidesoftware.code-spell-checker)
- Files: All (overlay)
- Config: cspell.*

### Better Comments (aaron-bond.better-comments)
- Files: All (overlay)
- Config: better-comments.*

### Auto Rename Tag (formulahendry.auto-rename-tag)
- Files: .html, .xml, .vue, .svelte, .jsx, .tsx
- Config: auto-rename-tag.*

### Django (batisteo.vscode-django)
- Files: .py (django templates), .html (django)
- Config: django.*

### Django Templates (davechanru.vscode-django-templates)
- Files: django-html, django-txt, djangojs
- Config: django-templates.*

### Django Boilerplate (mengsicode.vscode-django-boilerplate)
- Files: .py (django)
- Config: django-boilerplate.*

### Tailwind CSS (bradlc.vscode-tailwindcss)
- Files: .css, .scss, .html, .jsx, .tsx, .vue, .svelte
- Config: tailwindcss.*

### Color Info (bierner.color-info)
- Files: .css, .scss, .less, .html
- Config: color-info.*

### npm Intellisense (christian-kohler.npm-intellisense)
- Files: .json, .package.json
- Config: npm-intellisense.*

### Path Intellisense (christian-kohler.path-intellisense)
- Files: All (overlay)
- Config: path-intellisense.*

### Bun (oven.bun-vscode)
- Files: .js, .ts, .jsx, .tsx, .json
- Config: bun.*

### PowerShell (ms-vscode.powershell)
- Files: .ps1, .psm1, .psd1, .psrc, .ps1xml
- Config: powershell.*

### CMake Tools (ms-vscode.cmake-tools)
- Files: CMakeLists.txt, .cmake
- Config: cmake.*

### Live Server (ritwickdey.liveserver)
- Files: .html, .htm, .css, .js
- Config: liveServer.*

### Auto Docstring (njpwerner.autodocstring)
- Files: .py
- Config: autodocstring.*

### Redis Client (cweijan.vscode-redis-client)
- Files: .redis, .rdb
- Config: redis-client.*

### Zod Schema Generator (psulek-solo.zodschema-generator)
- Files: .ts, .tsx
- Config: zod-schema.*

### IntelliCode (visualstudioexptteam.vscodeintellicode)
- Files: .ts, .tsx, .js, .jsx
- Config: intellicode.*

### IntelliCode Examples (visualstudioexptteam.intellicode-api-usage-examples)
- Files: .ts, .tsx
- Config: intellicode-examples.*

### React Theme (mikaelkristiansson87.react-theme-vscode)
- Files: .tsx, .jsx, .ts, .js
- Config: react-theme.*

### TS Extension Pack (loiane.ts-extension-pack)
- Files: .ts, .tsx
- Config: ts-extension-pack.*

### Multi-Cursor Case Preserve (cardinal90.multi-cursor-case-preserve)
- Files: All
- Config: multi-cursor-case-preserve.*

### Simple React Snippets (burkeholland.simple-react-snippets)
- Files: .jsx, .tsx
- Config: (snippets only)

### Getter Setter (dskwrk.vscode-generate-getter-setter)
- Files: .ts, .tsx, .js, .jsx
- Config: generate-getter-setter.*

### Code-Insiders Chat Evaluations (ms-vscode.vscode-chat-customizations-evaluations)
- Files: All
- Config: (chat customizations)

### Hermes Chat (poppywu124.hermes-chat)
- Files: All
- Config: hermes-chat.*

### OpenCode (sst-dev.opencode)
- Files: All
- Config: opencode.*

### Gemini Integration
- Files: All
- Config: (gemini provider)

### Python Env (ms-python.vscode-python-envs)
- Files: .python-version, .python-env
- Config: python-envs.*

### DotNet Runtime (ms-dotnettools.vscode-dotnet-runtime)
- Files: .csproj, .sln, .dotnet
- Config: dotnet-runtime.*

### CMake Tools (ms-vscode.cmake-tools)
- Files: CMakeLists.txt, .cmake
- Config: cmake.*

### Make (ms-vscode.makefile-tools)
- Files: Makefile, makefile, GNUmakefile
- Config: makefile.*

### Kotlin (redhat.java - also covers kotlin)
- Files: .kt, .kts, .kotlin
- Config: java.*

### Maven (vscjava.vscode-maven)
- Files: pom.xml, .maven
- Config: maven.*

### Java Debug (vscjava.vscode-java-debug)
- Files: .java
- Config: java.debug.*

### Gradle (via redhat.java)
- Files: .gradle, .gradle.kts
- Config: java.gradle.*

### Dockerfile (via ms-azuretools.vscode-containers)
- Files: Dockerfile, .dockerfile, .containerfile
- Config: docker.dockerfile.*

### DevContainer (via ms-azuretools.vscode-containers)
- Files: .devcontainer/*
- Config: devcontainer.*

### GraphQL (via prisma.prisma)
- Files: .graphql, .gql
- Config: graphql.*

### JSON (built-in vscode.json-language-features)
- Files: .json, .jsonc
- Config: editor.defaultFormatter = "vscode.json-language-features"

### HTML (built-in vscode.html-language-features)
- Files: .html, .htm, .shtml
- Config: editor.defaultFormatter = "vscode.html-language-features"

### CSS (built-in vscode.css-language-features)
- Files: .css, .scss, .less, .sass
- Config: editor.defaultFormatter = "esbenp.prettier-vscode"

### Markdown (built-in vscode.markdown-language-features)
- Files: .md, .mdx, .markdown
- Config: editor.defaultFormatter = "esbenp.prettier-vscode"

### Python (built-in vscode.python)
- Files: .py, .pyi, .pyw
- Config: editor.defaultFormatter = "charliermarsh.ruff"
