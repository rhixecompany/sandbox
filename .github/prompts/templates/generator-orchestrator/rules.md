# Rules

> Extracted from `generator-orchestrator.prompt.md`.

## Rules

### Inputs

Accept these unified inputs:

- `mode`: `full | quick | custom`
- `scope`: target folders or project boundaries
- `detail-level`: `standard | deep | implementation-ready`
- `validation-level`: `standard | strict`
- `include-code-generation`: `true | false`
- `include-documentation`: `true | false`
- `custom-stage-selection` (custom mode only): list of requested stages

### Deterministic Defaults

When inputs are missing, use:

- `mode=full`
- `scope=workspace-root`
- `detail-level=standard`
- `validation-level=strict`
- `include-code-generation=true`
- `include-documentation=true`
- `custom-stage-selection=[]`

### Outputs

Always produce:

- generated artifact manifest with stage attribution
- cross-linking report between generated docs
- validation report (pass, warn, fail with reasons)
- execution summary with retries, degraded paths, and blocked handoffs

### Orchestration Constraints

- Never run downstream prompts before prerequisite artifacts exist.
- Stage quality gate must pass before advancing.
- Retry policy for missing sections: one retry only with stricter constraints.
- If still invalid after retry, continue in degraded mode and record warning.
- Final consistency gate is mandatory for successful handoff.
