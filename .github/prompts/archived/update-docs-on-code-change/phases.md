# Phases

> Extracted from `update-docs-on-code-change.prompt.md`.

## Phases

### Phase 1: Trigger and Scope Detection

| Field | Details |
| --- | --- |
| Goal | Determine whether documentation updates are required and which files are affected. |
| Inputs | Code diff, changed APIs, config updates, dependency updates, CLI changes. |
| Outputs | Doc-impact checklist with required file updates. |
| Validation | Every triggering code change has a corresponding documentation decision. |

### Phase 2: Documentation Synchronization

| Field | Details |
| --- | --- |
| Goal | Apply accurate updates to required documentation files and sections. |
| Inputs | Impact checklist, current docs, code behavior, version context. |
| Outputs | Updated README/docs/examples/changelog/migration content. |
| Validation | Documentation text, examples, and signatures match current code state. |

### Phase 3: Verification and Release Readiness

| Field | Details |
| --- | --- |
| Goal | Ensure documentation quality, consistency, and release readiness. |
| Inputs | Updated documentation set and validation outcomes. |
| Outputs | Final documentation status report and remaining debt notes. |
| Validation | No major stale sections, broken links, or missing critical docs remain. |
