# Phases

> Extracted from `typescript.prompt.md`.

## Phases

### Phase 1: Type and Boundary Design

| Field | Details |
| --- | --- |
| Goal | Define robust type contracts and execution boundaries before coding. |
| Inputs | Feature requirements, existing interfaces, architecture constraints. |
| Outputs | Typed API contracts, component boundaries, error model plan. |
| Validation | Type contracts cover all expected inputs/outputs and failure paths. |

### Phase 2: Implementation with Strict Safety

| Field | Details |
| --- | --- |
| Goal | Implement type-safe behavior and consistent runtime validation. |
| Inputs | Type plan, validation schemas, DAL abstractions, config wrappers. |
| Outputs | Updated .ts/.tsx code with strict safety guarantees. |
| Validation | No unsafe type escapes in critical paths and validation is enforced. |

### Phase 3: Quality and Maintainability Review

| Field | Details |
| --- | --- |
| Goal | Ensure readability, maintainability, and architecture alignment. |
| Inputs | Updated code, diagnostics, and project quality rules. |
| Outputs | Final code with notes on trade-offs and technical debt. |
| Validation | Complex types are documented and architecture rules are respected. |
