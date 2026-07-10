## Objective

Bidirectionally sync skills, plugins, and hooks across Hermes, GitHub Copilot, and OpenCode Codex with zero drift; create the needed Copilot personalities (from 186 instructions) and profiles (from 174 agents) as applicable.

## Source Plan

`plan/prompt-orchestration-comprehensive-plan.md` → Phase 3 (§4.4), sub-phases 3.1–3.4

## Deliverables

- S3 `docs/agents-cross-reference.md`
- Zero drift in plugins (4/4) and hooks (3/3)

## Sub-phases

- 3.1 Inventory instructions (`.github/instructions/`, 186) & agents (`.github/agents/`, 174)
- 3.2 Identify root folders (Hermes `~/AppData/Local/hermes/`, Copilot `~/.copilot/`, Codex `~/.codex/`)
- 3.3 Sync assets bidirectionally (rsync/cp with exclusion list)
- 3.4 Verify (zero-drift check)

## Success Criteria

Zero plugin/hook drift; 174+186 agents/instructions accounted for; all cross-references resolve.

## Safety Gate G3

Zero plugin/hook drift — list diffs → sync → re-check.

## Dependencies

Phase 2 complete. Blocks Phase 4.
