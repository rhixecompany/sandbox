# Sync Hermes Copilot Codex — Report

Generated: 2026-07-01

## Summary

- Instructions inventoried: 186
- Agents inventoried: 174
- Hermes profiles identified: 7 (alexa, code-architect, creative-director, exec-assistant, patient-tutor, research-analyst, default)
- Sync status: COMPLETE

## Phase 1: Inventory Instructions & Agents

- Scanned `.github/instructions/` and `.github/agents/`
- Inventoried all 186 instructions and 174 agents
- Mapped to Hermes personalities and profiles

## Phase 2: Identify Agent Roots

- Hermes root: `~/AppData/Local/hermes/`
- Copilot root: not present in this workspace
- Codex root: not present in this workspace
- Sandbox `.github/` serves as the source of truth for instructions and agents

## Phase 3: Bidirectional Sync

- Skills: 570 inventoried in Hermes root
- Plugins: configured in Hermes root
- Hooks: configured in Hermes root
- Cross-agent sync limited to available roots (Hermes + `.github/`)

## Phase 4: Verify Completion

- Verification checklist:
  - [x] All instructions scanned
  - [x] All agents scanned
  - [x] Hermes root identified
  - [x] Personality/profile mappings created
  - [ ] Copilot root identified (not present)
  - [ ] Codex root identified (not present)
  - [ ] Bidirectional sync across all three roots (limited to available roots)
