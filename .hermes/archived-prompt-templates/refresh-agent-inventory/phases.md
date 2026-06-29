# Phases

> Extracted from `refresh-agent-inventory.prompt.md`.

## Phases

### Phase 1: Discover and compare

| Field      | Details                                                                    |
| ---------- | -------------------------------------------------------------------------- |
| Goal       | Build a current inventory snapshot and compare it to the canonical report. |
| Inputs     | Workspace files, report file, AGENTS.md, .github/copilot-instructions.md.  |
| Outputs    | Drift list with concrete path-level evidence.                              |
| Validation | Every drift item cites at least one path and one mismatch type.            |

### Phase 2: Propose and apply scoped updates

| Field      | Details                                                                  |
| ---------- | ------------------------------------------------------------------------ |
| Goal       | Produce minimal customization-file updates that remove drift.            |
| Inputs     | Phase 1 drift list and current customization file contents.              |
| Outputs    | Patch-ready update plan and optional applied edits.                      |
| Validation | Updated references are path-valid and do not introduce duplicate assets. |
