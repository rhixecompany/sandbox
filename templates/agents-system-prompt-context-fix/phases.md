# Agents System Prompt Context Fix — Phases

> Full operational phases for `prompts/agents-system-prompt-context-fix.prompt.md`.

## Phase 1: Generate Agent Context Files
- Run `architecture-blueprint-generator`, `folder-structure-blueprint-generator`, `technology-stack-blueprint-generator`.
- Scope: project root and all subprojects.
- Gate: context docs generated for root and each subproject.

## Phase 2: Audit VS Code Configuration
- List JSON files under `.vscode` and subfolders.
- Triage, audit, debug, enhance, and verify each config.
- Gate: all VS Code JSON configs triaged and verified.

## Phase 3: Verify & Implement
- Verify plan/specs, implement fixes, verify completion.
- Gate: verification report written and issues closed.
