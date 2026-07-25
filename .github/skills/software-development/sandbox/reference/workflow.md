---
name: sandbox-workflow
description: "Agentic Development Workflow"
version: 1.0.0
author: Alexa
---
     1|# Agentic Development Workflow
     2|
     3|## 6-Phase Workflow
     4|
     5|### Phase 1: Ticket
     6|
     7|Create ticket file in `thoughts/tickets/` with:
     8|
     9|- Problem statement
    10|- Requirements
    11|- Success criteria
    12|
    13|### Phase 2: Research (`/research`)
    14|
    15|- Reads ticket first
    16|- Spawns codebase-locator + thoughts-locator (parallel)
    17|- Spawns codebase-pattern-finder
    18|- Spawns codebase-analyzer + thoughts-analyzer (parallel)
    19|- Output: `thoughts/research/YYYY-MM-DD_topic.md`
    20|
    21|**Sequencing**: Locate → Find Patterns → Analyze. Never mix agent types in parallel.
    22|
    23|### Phase 3: Plan (`/plan`)
    24|
    25|- Analyzes ticket + research
    26|- Creates phased implementation plan
    27|- Output: `thoughts/plans/descriptive-name.md`
    28|
    29|### Phase 4: Execute (`/execute`)
    30|
    31|- Implements plan phases sequentially
    32|- Runs verification after each phase
    33|- Updates progress checkmarks `[ ]` → `[x]`
    34|
    35|### Phase 5: Commit (`/commit`)
    36|
    37|- Reviews all changes
    38|- Generates conventional commit message
    39|- No Co-authored-by attribution
    40|
    41|### Phase 6: Review (`/review`)
    42|
    43|- Compares implementation to plan
    44|- Identifies drift
    45|- Verifies success criteria
    46|- Output: `thoughts/reviews/YYYY-MM-DD_review.md`
    47|
    48|## Context Management
    49|
    50|- Start each phase with fresh context window
    51|- Agents compress context automatically
    52|- File references: `path/to/file.ext:line`
    53|
    54|## Best Practices
    55|
    56|- Review each phase output before proceeding
    57|- Be specific in tickets
    58|- Document deviations from plan
    59|- Use iterative refinement
    60|