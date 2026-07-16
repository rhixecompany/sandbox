# projects/selenium_webdriver — Folder Structure Blueprint

## Overview
- Namespace: `projects/selenium_webdriver`
- Folder model: top-level components plus tooling/config directories.

## Directory Tree
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

## Placement Rules
- Keep code in the existing top-level component directories.
- Keep config files at the project root or `.vscode/`.
- Keep docs under `docs/` if the project already uses a docs folder.

## Naming Conventions
- Preserve the current folder naming style for this project.
- Do not normalize dots, hyphens, or underscores.

## Update Notes
- Refresh after any folder move, rename, or new top-level component.
