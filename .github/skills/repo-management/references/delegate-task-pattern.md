# delegate_task usage pattern

## Key constraint
`delegate_task` is a **top-level tool** — it is NOT importable from `hermes_tools` inside `execute_code()`. Attempting `from hermes_tools import delegate_task` will raise `ImportError`. Always call it as a direct tool invocation, not from within Python scripts.

## Batch mode
- Max **3 tasks per call** (delegation.max_concurrent_children).
- Each task gets an isolated subagent with its own terminal session.
- Subagents CANNOT call `delegate_task` themselves unless given `role: "orchestrator"`.

## When to prefer over execute_code
- `execute_code` scripts that take >60s may time out or require user consent.
- Batch processing (e.g., running web-research-pipeline per project) is better done via `delegate_task` tasks array.
- `delegate_task` runs the model per task — use for reasoning-heavy work; use `execute_code` only for mechanical data processing.

## Pattern
```
# Call delegate_task with tasks array (up to 3):
- task 1: { goal, context, toolsets }
- task 2: ...
- task 3: ...
```
