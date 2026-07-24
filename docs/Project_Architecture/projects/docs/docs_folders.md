# docs — Folder Structure Blueprint

## Overview
Documentation repository containing reference documents for the SandBox workspace.

## Directory Tree
```text
docs/
├── .github/
│   └── workflows/
│       └── todo-scan.yml        — Scans for TODO markers
├── docs/                        — (self-referential, additional docs)
├── AGENTS.md                    — Agent context file
├── README.md                    — Entry point & navigation
├── architecture.md              — Workspace architecture overview
├── folder-structure.md          — Directory structure reference
├── tech-stack.md                — Technology index
├── DEPENDENCY_AUDIT.md          — Cross-project dependency audit
├── RESEARCH_APPENDIX.md         — Research campaign supplement
├── DEBIAN_INSTALL.md            — Debian install notes (archived)
├── hermes-chat-export.json      — Chat history export
├── hermes-personalities.json    — Personality configs
└── pr-checklist.json            — PR checklist
```

## File Placement Patterns
- **Configuration:** `.github/`, root-level JSON/YAML
- **Documentation:** Root `.md` files organized by topic
- **Data/Exports:** JSON archives at root level

## Naming Conventions
- Markdown files: lowercase kebab-case (`tech-stack.md`)
- Config files: UPPER_SNAKE_CASE (`.yml`, `.json`)
- Agent files: UPPERCASE (`AGENTS.md`, `README.md`)
