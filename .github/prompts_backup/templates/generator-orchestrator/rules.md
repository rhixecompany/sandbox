# Rules

## Core Orchestrator Rules

These rules govern all execution of the generator-orchestrator prompt.

### Stage Gate Rules

1. **Strict dependency ordering** — No stage may begin until its prerequisite stage's gate passes. Gate pass requires that all expected artifacts from the prerequisite stage exist and pass static lint validation.
2. **No parallel-skip** — All prompts in a parallel stage (Stage A) must complete before the gate opens. Partial completion is not sufficient.
3. **Degraded mode must be explicit** — If a generator fails or produces incomplete output, the orchestrator must record the failure, retry once with stricter constraints, then continue with an explicit warning. Silent degradation is forbidden.
4. **Stack detection must be unambiguous** — If technology-stack-blueprint-generator cannot determine a clear primary stack, it must record "ambiguous" and the orchestrator must use generic-safe defaults for dependent stages.

### Execution Mode Rules

1. **Mode = full (default)** — Execute all five stages (A → B → C → D → E). All conditional MCP generators fire based on detected stacks.
2. **Mode = quick** — Execute Stage A only. Generate minimal outputs (stack + folder structure). Skip B, C, D. Stage E produces a handoff with reduced validation.
3. **Mode = custom** — Accept explicit stage-selection flags:
   - `stages=A,B` — Execute only specified stages. Prerequisite stages are auto-injected before the requested ones.
   - `include-code-generation=true|false` — Controls whether Stage D fires.
   - `validation-level=strict|normal|skip` — Controls gate strictness.

### Validation Rules

1. **Static prompt lint** — Every generated artifact must be parseable as valid Markdown with no broken section fences.
2. **Dependency trace** — Each generated document may only reference artifacts from prior (completed) stages. Forward references are a gate failure.
3. **Cross-document consistency** — Across all generators, the detected stack, framework versions, and project name must be consistent. Mismatch = hard gate failure.
4. **Conditional-path determinism** — Given the same inputs + mode, the orchestrator must produce the same set of stages every time. No non-deterministic branching.

### Failure Policy

| Failure | Action | Gate Impact |
|| --------- | -------- | ------------- ||
| Generator produces no output | Retry once with stricter constraints | Blocked until retry |
| Retry also fails | Record degraded warning, use generic fallback | Gate passes with warning |
| Cross-doc inconsistency | Emit remediation checklist | Gate FAILS — hard handoff failure |
| Stack ambiguous | Use generic-safe defaults, continue | Gate passes with warning |
