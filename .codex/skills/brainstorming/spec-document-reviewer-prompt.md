---
name: spec-document-reviewer-prompt
description: "# Spec Document Reviewer Prompt Template"
version: 1.0.0
author: Alexa
license: MIT
metadata:
  hermes:
    tags: []
    related_skills: []
---
     1|# Spec Document Reviewer Prompt Template
     2|
     3|Use this template when dispatching a spec document reviewer subagent.
     4|
     5|**Purpose:** Verify the spec is complete, consistent, and ready for implementation planning.
     6|
     7|**Dispatch after:** Spec document is written to docs/superpowers/specs/
     8|
     9|```
    10|Task tool (general-purpose):
    11|  description: "Review spec document"
    12|  prompt: |
    13|    You are a spec document reviewer. Verify this spec is complete and ready for planning.
    14|
    15|    **Spec to review:** [SPEC_FILE_PATH]
    16|
    17|    ## What to Check
    18|
    19|    | Category | What to Look For |
    20|    |----------|------------------|
    21|    | Completeness | TODOs, placeholders, "TBD", incomplete sections |
    22|    | Consistency | Internal contradictions, conflicting requirements |
    23|    | Clarity | Requirements ambiguous enough to cause someone to build the wrong thing |
    24|    | Scope | Focused enough for a single plan — not covering multiple independent subsystems |
    25|    | YAGNI | Unrequested features, over-engineering |
    26|
    27|    ## Calibration
    28|
    29|    **Only flag issues that would cause real problems during implementation planning.**
    30|    A missing section, a contradiction, or a requirement so ambiguous it could be
    31|    interpreted two different ways — those are issues. Minor wording improvements,
    32|    stylistic preferences, and "sections less detailed than others" are not.
    33|
    34|    Approve unless there are serious gaps that would lead to a flawed plan.
    35|
    36|    ## Output Format
    37|
    38|    ## Spec Review
    39|
    40|    **Status:** Approved | Issues Found
    41|
    42|    **Issues (if any):**
    43|    - [Section X]: [specific issue] - [why it matters for planning]
    44|
    45|    **Recommendations (advisory, do not block approval):**
    46|    - [suggestions for improvement]
    47|```
    48|
    49|**Reviewer returns:** Status, Issues (if any), Recommendations
    50|