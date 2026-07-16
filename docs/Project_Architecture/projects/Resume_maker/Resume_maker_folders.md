# projects/Resume_maker — Folder Structure Blueprint

## Overview
- Namespace: `projects/Resume_maker`
- Folder model: top-level components plus tooling/config directories.

## Directory Tree
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

## Placement Rules
- Keep code in the existing top-level component directories.
- Keep config files at the project root or `.vscode/`.
- Keep docs under `docs/` if the project already uses a docs folder.

## Naming Conventions
- Preserve the current folder naming style for this project.
- Do not normalize dots, hyphens, or underscores.

## Update Notes
- Refresh after any folder move, rename, or new top-level component.
