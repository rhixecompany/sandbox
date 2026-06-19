# Agent Context Files + VS Code Configurator Plan

**Created:** 2026-06-19
**Profile:** exec-assistant (planning)
**Skills:** architecture-blueprint-generator, folder-structure-blueprint-generator, technology-stack-blueprint-generator, vscode-workspace-configurator

## Phases

### Phase 1: Create/Update Agent Context Files
Generate architectural, folder structure, and technology stack blueprints for root and all 16 projects.

**Target projects (16):**
- Banking, comicwise, cookiecutter-django-tailwind, Django-Scrapy-Selenium, ecom, profile, Python-projects, rhixe_scans, rhixecompany-comics, selenium_webdriver, university-libary-jsm, xamehi, xamehi.tv, youtube-downloader
- Bash (scripts toolkit), docs (documentation), Resume_maker

### Phase 2: VS Code Workspace Configurator
Run full audit/enhance/verify pipeline on all .vscode JSON files.

**Verification steps:**
1. list — Inventory all .vscode folders and JSON files
2. triage — Identify issues (formatter conflicts, missing configs, hardcoded paths)
3. audit — Validate JSON syntax, extension references, stack alignment
4. debug — Fix identified issues
5. enhance — Add missing configurations per project stack
6. verify — Final validation gate

## Dependencies
- Phase 1 must complete before Phase 2
- Each project's AGENTS.md must exist before blueprint generation

## Completion Criteria
- All 18 AGENTS.md files have architecture/folder/stack context
- All 17 .vscode folders have valid, stack-aligned JSON configs
- No formatter conflicts, no hardcoded paths, no missing extensions