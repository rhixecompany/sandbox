# prompts-md — Context Catalog

Generated: 2026-06-12 Source files: Prompts/*.md

## Summary

Fresh audit of 9 prompt files under `Prompts/`. These files are authored as task descriptors for Hermes/Copilot workflows and declare prompt/skill/tool dependencies in YAML. Forward references are primarily prompt and skill dependencies; peer files do not appear to back-reference these source prompts by path, so reverse coverage is sparse.

Batch assignments:
- Batch 1 (proof-of-concept): agents-fix, bash-scripts-fix, dev-init, general, prompts-fix
- Batch 2: repo-management, repo, skills-fix, workspace-consolidate

## Forward References (this file -> others)

| Type | Reference | Path | Exists? |
| --- | --- | --- | --- |
| prompt | .github/prompts/context-map.prompt.md | .github/prompts/context-map.prompt.md | True |
| prompt | .github/prompts/update-implementation-plan.prompt.md | .github/prompts/update-implementation-plan.prompt.md | True |
| prompt | .github/prompts/convert-plaintext-to-md.prompt.md | .github/prompts/convert-plaintext-to-md.prompt.md | True |
| prompt | .github/prompts/boost-prompt.prompt.md | .github/prompts/boost-prompt.prompt.md | True |
| prompt | .github/prompts/ai-prompt-engineering-safety-review.prompt.md | .github/prompts/ai-prompt-engineering-safety-review.prompt.md | True |
| prompt | .github/prompts/prompt-builder.prompt.md | .github/prompts/prompt-builder.prompt.md | True |
| prompt | .github/prompts/skills-debug-prompt.prompt.md | .github/prompts/skills-debug-prompt.prompt.md | True |
| prompt | ../../Bash/docs/AGENTS.md | ../../Bash/docs/AGENTS.md | Unknown |
| dependency fragment | context-map — Map impacted files and dependencies before edits | none | False |
| dependency fragment | context-map — Map script directories and dependency impact before migration | none | False |
| dependency fragment | context-map — Map source, destination, and dependency impact before | none | False |
| dependency fragment | context-map — Map impacted files and dependencies before changes (loaded as prompt dependency) | none | False |
| dependency fragment | context-map — Build dependency and file context before | none | False |
| agent mention | `@v2`, `@v4`, `@v5` | symbolic | Unknown |
| agent mention | `domain` | symbolic | Unknown |

## Reverse References (others -> this file)

| Type | Source File | Reference | Context snippet |
| --- | --- | --- | --- |
| Tests or docs | multiple `docs/*-issues-context.md`, `docs/*-verify-context.md` artifacts already exist for prior prompts batches, but no direct `Prompts/*.md` reverse path was observed in this run. | N/A | N/A |

## Plans & Specs (plugin system)

No plan/spec namespace entries with prompts-md roots matched prior artifacts. Plugin `plans-and-specs` integration remains optional; companion markdown in `thoughts/plans/` is the fallback.

## Malformed dependency blocks detected

These bullets under `dependencies:` look like prose fragments, not valid paths or declared references:

- `context-map — Map impacted files and dependencies before edits`
- `context-map — Map script directories and dependency impact before migration`
- `context-map — Map source, destination, and dependency impact before`
- `context-map — Map impacted files and dependencies before changes (loaded as prompt dependency)`
- `context-map — Build dependency and file context before`

These should be normalized to valid references or moved into bodies/`skills:` bullets.
