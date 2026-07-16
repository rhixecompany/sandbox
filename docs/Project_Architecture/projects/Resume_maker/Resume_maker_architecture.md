# projects/Resume_maker — Architecture Blueprint

## Overview
- Detected stack: Bun, TypeScript, ESLint, Prettier
- Architectural pattern: Lightweight utility or scaffold project
- Top-level components: scripts, docs

## Component Map
- `scripts, docs`
- Shared config: `.vscode/` when present
- Docs: `docs/` when present

## Top-Level Structure
```text
Resume_maker/
├── .github/
│   └── copilot-instructions.md
├── application_materials/
│   ├── COVER_LETTER.md
│   └── JOB_RECOMMENDATIONS.md
├── output/
│   ├── alexander-resume.md
│   ├── alexander-resume.pdf
│   ├── basil-resume.md
│   ├── basil-resume.pdf
│   ├── cover-letter.md
│   ├── cover-letter.pdf
│   ├── interview-qa.md
│   ├── job-recommendations.md
│   ├── linkedin-about-draft.md
│   ├── linkedin-guide.md
│   ├── output_resume.md
│   ├── project-walkthrough.md
│   ├── resume.md
│   ├── resume.pdf
│   ├── search-keywords.md
│   ├── Senior_React_Developer_Resume.md
│   ├── smoke-resume.md
│   └── smoke-resume.pdf
├── updated_readmes/
│   ├── ecom_README.md
│   ├── rhixe_scans_README.md
│   ├── rhixecompany_README.md
│   ├── selenium_webdriver_README.md
│   ├── university-libary-jsm_README.md
│   └── xamehitv_README.md
├── .cspell.json
├── .markdownlint.json
├── .markdownlintrc.json
├── AGENTS.md
├── alexander-input.json
├── architecture.md
├── AUDIT_Resume_maker.md
├── basil-input.json
├── bun.lock
├── copilot-instructions.md
├── eslint.config.js
├── folder-structure.html
├── folder-structure.md
├── grok_summary_prompt.md
├── grok_summary_prompt.txt
├── index.ts
├── LICENSE
├── LICENSE.html
├── package.json
├── README.html
├── README.md
├── REPOSITORY_SUMMARY.md
├── RESEARCH_REPORT.md
├── sample-input.json
├── tech-stack.md
├── THE_STORY_OF_THIS_REPO.md
├── tsconfig.json
└── web-research-resume-maker.md
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
