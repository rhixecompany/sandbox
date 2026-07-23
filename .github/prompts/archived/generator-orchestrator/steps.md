# Steps

> Extracted from `generator-orchestrator.prompt.md`.

## Steps

1. Build inventory and role classification for the 11 root generators.
2. Normalize inputs using deterministic defaults.
3. Resolve execution plan by mode:
    - `full`: run Stage A, B, C, optional D by conditions, then E.
    - `quick`: run Stage A and minimal Stage B (`architecture` only), then Stage E.
    - `custom`: run user-selected stages if prerequisites are satisfied; otherwise auto-insert missing prerequisite stages.
4. Execute Stage A (parallel):
    - `technology-stack-blueprint-generator.prompt.md`
    - `folder-structure-blueprint-generator.prompt.md`
5. Run Stage A quality gate:
    - stack summary exists and includes confidence or ambiguity marker
    - folder structure artifact exists and is parseable
6. Execute Stage B (gated):
    - `architecture-blueprint-generator.prompt.md` (requires Stage A)
    - `project-workflow-analysis-blueprint-generator.prompt.md` (requires Stage A)
    - `code-exemplars-blueprint-generator.prompt.md` (requires Stage A)
7. Run Stage B quality gate:
    - each artifact has required top-level sections
    - references point to existing files or generated artifacts only
8. Execute Stage C (gated):
    - `copilot-instructions-blueprint-generator.prompt.md` (requires Stage A and B)
    - `readme-blueprint-generator.prompt.md` (requires Stage A and B)
9. Run Stage C quality gate:
    - instruction and README outputs cross-link to architecture/workflow/stack artifacts
    - no contradictory tech or workflow claims across generated docs
10. Execute Stage D (conditional MCP generation):
     - run only if `include-code-generation=true`
     - route by detected stack and mode:
        - TypeScript or Node indicators -> `typescript-mcp-server-generator.prompt.md`
        - Python indicators -> `python-mcp-server-generator.prompt.md`
        - Swift indicators -> `swift-mcp-server-generator.prompt.md`
        - Copilot Studio or Power Platform indicators -> `mcp-copilot-studio-server-generator.prompt.md`
11. Run Stage D quality gate:
     - generated server artifacts include runnable entry points and dependency metadata
     - output schemas and transport choices are documented
12. Execute Stage E consolidation and consistency validation:
     - compile final artifact manifest
     - compute cross-document consistency checks
     - produce pass/fail handoff decision
