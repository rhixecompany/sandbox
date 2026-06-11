# Prompt Conversion And Context-Map Alignment Plan

## Objective

Create a comprehensive plan that uses brainstorming and plans-and-specs to:

1. Convert and normalize prompt content from plaintext sources.
2. Ensure prompt templates use context-map before implementation work.
3. Verify all created or updated markdown artifacts.

## Scope

### Primary conversion target

- `.github/prompts/convert-plaintext-to-md.prompt.md`

### Plaintext source set

- `Prompts/agents-fix.prompts.txt`
- `Prompts/bash-scripts-fix.prompts.txt`
- `Prompts/commands-fix.prompts.txt`
- `Prompts/dev-init.prompts.txt`
- `Prompts/general.prompts.txt`
- `Prompts/repo.prompts.txt`
- `Prompts/skills-fix.prompts.txt`

### Context-map enforcement targets

- `.github/prompts/boost-prompt.prompt.md`
- `.github/prompts/ai-prompt-engineering-safety-review.prompt.md`
- `.github/prompts/update-implementation-plan.prompt.md`
- `.github/prompts/prompt-builder.prompt.md`
- `Prompts/*.md`

## Feature Specifications

### Feature 1: Plaintext to markdown normalization

Goal:

- Convert plaintext prompts into clear markdown structure with headings, sections, and deterministic ordering.

Acceptance criteria:

- Every converted markdown file has clear title, intent, skills, and phase or step flow.
- Original behavior and workflow intent are preserved.
- Conversion is idempotent: repeat run does not produce semantic drift.

### Feature 2: Context-map preflight integration

Goal:

- Require `.github/prompts/context-map.prompt.md` usage in prompt workflows before edits and implementation.

Acceptance criteria:

- Target prompt files include explicit `context-map` dependency or preflight step.
- Prompts state mapping of dependencies/tests/references before execution.
- No target prompt remains without context-map usage guidance.

### Feature 3: Verification and traceability

Goal:

- Verify all created or updated markdown files and record coverage.

Acceptance criteria:

- Verification includes file existence, context-map reference scan, and markdown sanity checks.
- Report lists all touched files and validation outcomes.

## Implementation Plan

### Phase 1: Discovery (brainstorming + plans-and-specs)

1. Inventory plaintext prompt files and markdown counterparts.
2. Identify workflow sections where context-map preflight should be mandatory.
3. Define minimal safe edits that preserve source intent.

### Phase 2: Conversion and enhancement

1. Normalize prompt markdown structure for converted content.
2. Add context-map dependency/preflight instructions to target prompts.
3. Keep edits scoped to prompt behavior, dependencies, and instructions.

### Phase 3: Verification

1. Run a repository scan for `context-map` usage across all target markdown files.
2. Validate target file list coverage.
3. Review diffs for intent preservation and consistency.

## Code Samples

### Sample A: Add context-map dependency in frontmatter

```md
dependencies:
  - command:/context-map
  - skill:plans-and-specs
```

### Sample B: Add context-map preflight rule

```md
## Rules

1. Run `/context-map` before editing files so dependency and test impact are mapped first.
2. Do not proceed with implementation until the context map is complete.
```

### Sample C: Verification command pattern

```powershell
rg -n "context-map|/context-map|command:/context-map" .github/prompts/*.prompt.md Prompts/*.md
```

## File Reference Matrix

| File | Action | Why |
| --- | --- | --- |
| `.github/prompts/convert-plaintext-to-md.prompt.md` | Update | Add context-map dependency and preflight guidance for conversion safety |
| `.github/prompts/boost-prompt.prompt.md` | Update | Require context-map before workspace exploration and prompt refinement |
| `.github/prompts/ai-prompt-engineering-safety-review.prompt.md` | Update | Require context-map for safe input/context inventory |
| `.github/prompts/update-implementation-plan.prompt.md` | Update | Require context-map before plan file updates |
| `.github/prompts/prompt-builder.prompt.md` | Update | Require context-map before reference-pattern and file operations |
| `Prompts/agents-fix.prompts.md` | Update | Add context-map preflight skill usage |
| `Prompts/bash-scripts-fix.prompts.md` | Update | Add context-map preflight for script inventory changes |
| `Prompts/commands-fix.prompts.md` | Update | Add context-map preflight before command normalization |
| `Prompts/dev-init.prompts.md` | Update | Explicitly include context-map in skills |
| `Prompts/general.prompts.md` | Update | Add context-map preflight in general workflow |
| `Prompts/repo.prompts.md` | Update | Add context-map preflight to migration planning |
| `Prompts/skills-fix.prompts.md` | Update | Add context-map preflight for skill audit impact |
| `Prompts/workspace-consolidate.prompts.md` | Update | Add context-map dependency and skill for consolidation safety |

## Validation Checklist

- [ ] All target markdown files include context-map usage.
- [ ] Converted/updated markdown keeps original intent.
- [ ] File references are valid and workspace-relative.
- [ ] Verification scan output confirms complete coverage.
