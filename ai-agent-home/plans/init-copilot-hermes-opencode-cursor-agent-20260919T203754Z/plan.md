# Agent Initialization Plan

**Status:** COMPLETE  
**Run:** `init-copilot-hermes-opencode-cursor-agent-20260919T203754Z`  
**Updated:** 2026-09-19

## Checkpoints
| Checkpoint | Work                                                    | Gate                                                                 | Status   |
| ---------- | ------------------------------------------------------- | -------------------------------------------------------------------- | -------- |
| 1          | Inventory existing agent adapters and canonical context | Existing surfaces identified without reading protected secrets       | COMPLETE |
| 2          | Consolidate shared rules in `AGENTS.md`                 | Tool adapters can defer without conflicting copies                   | COMPLETE |
| 3          | Add clarification and durable artifact protocol         | All requested systems reference the lifecycle                        | COMPLETE |
| 4          | Create run spec, plan, and prompt                       | Three timestamped artifact directories exist                         | COMPLETE |
| 5          | Validate                                                | Markdownlint, whitespace, stale-reference, and existence checks pass | COMPLETE |
## Changed Surfaces

- `AGENTS.md`
- `.github/copilot-instructions.md`
- `.hermes.md`
- `.cursorrules`
- `.cursor/rules/sandbox.mdc`
- `ai-agent-home/specs/init-copilot-hermes-opencode-cursor-agent-20260919T203754Z/spec.md`
- `ai-agent-home/plans/init-copilot-hermes-opencode-cursor-agent-20260919T203754Z/plan.md`
- `ai-agent-home/prompts/init-copilot-hermes-opencode-cursor-agent-20260919T203754Z/init.prompt.md`

## Validation Commands

```text
bunx markdownlint-cli2 --config .markdownlint-cli2.jsonc AGENTS.md .hermes.md .cursorrules .cursor/rules/sandbox.mdc .github/copilot-instructions.md copilot-instructions.md CLAUDE.md ai-agent-home/**/*.md
git diff --check
```

## Assumptions

- The user was unavailable to answer the clarification form, so recommended defaults were applied.
- OpenCode's repository discovery path is documented rather than represented by an invented `.opencode/opencode.json`.
- Existing unrelated subproject modifications were not reverted or changed.
