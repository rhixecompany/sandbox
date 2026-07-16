# projects/selenium_webdriver — Architecture Blueprint

## Overview
- Detected stack: Bun, Prettier
- Architectural pattern: JavaScript/Bun application with feature-oriented source layout
- Top-level components: src, docs

## Component Map
- `src, docs`
- Shared config: `.vscode/` when present
- Docs: `docs/` when present

## Top-Level Structure
```text
selenium_webdriver/
├── .github/
│   ├── workflows/
│   └── copilot-instructions.md
├── src/
│   ├── scrape.js
│   ├── scrape2.js
│   ├── test.js
│   ├── test1.js
│   └── utils.js
├── .editorconfig
├── .env.example
├── .eslintignore
├── .prettierignore
├── .prettierrc
├── AGENTS.md
├── API_REFERENCE.md
├── ARCHITECTURE.md
├── AUDIT_selenium_webdriver.md
├── bun.lock
├── code-exemplars.md
├── CONTRIBUTING.md
├── copilot-instructions.md
├── cross-linking-report.md
├── DATABASE_SCHEMA.md
├── DEPLOYMENT_GUIDE.md
├── DEVELOPMENT_GUIDE.md
├── execution-summary.md
├── folder-structure.md
├── package.json
├── project-workflow.md
├── README.md
├── REPOSITORY_SUMMARY.md
├── RESEARCH_REPORT.md
├── SECURITY.md
├── SETUP_GUIDE.md
├── technology-stack.md
├── TESTING_GUIDE.md
├── THE_STORY_OF_THIS_REPO.md
├── validation-report.md
└── web-research-selenium-webdriver.md
```

## Cross-Cutting Concerns
- Configuration: environment and workspace configs live alongside the project.
- Testing: test locations should follow the existing project layout.
- Tooling: keep formatter/linter/editor settings in `.vscode/`.

## Extension Points
- Add new features within the existing top-level component that matches the current layout.
- Keep new dependencies aligned with the detected stack.

## Update Notes
- Regenerate when component boundaries, package dependencies, or folder structure change.
