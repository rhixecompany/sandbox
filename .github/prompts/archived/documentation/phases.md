# Phases

> Extracted from `documentation.prompt.md`.

## Phases

### Phase 1: Documentation Impact Analysis

| Field | Details |
| --- | --- |
| Goal | Determine exactly which docs must change for the code updates. |
| Inputs | Changed files, public API surfaces, config changes, existing docs. |
| Outputs | Documentation update checklist with file-level scope. |
| Validation | Every behavior-affecting code change has a mapped documentation target. |

### Phase 2: Authoring and Synchronization

| Field | Details |
| --- | --- |
| Goal | Implement all required doc updates with precise technical accuracy. |
| Inputs | Existing docs, source code, architecture patterns, examples. |
| Outputs | Updated docs, examples, and references with consistent terminology. |
| Validation | Examples and API details match current code signatures and behavior. |

### Phase 3: Quality and Accessibility Review

| Field | Details |
| --- | --- |
| Goal | Ensure docs are complete, navigable, and maintainable. |
| Inputs | Updated documentation set and link/reference map. |
| Outputs | Final reviewed docs and follow-up notes for any deferred work. |
| Validation | No broken links, missing required sections, or stale examples remain. |
