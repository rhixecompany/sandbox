# Generated Prompt

> Extracted from `generate-custom-instructions-from-codebase.prompt.md`.

## Generated Prompt

```
"Analyze code evolution between two project states to generate precise migration instructions for GitHub Copilot. These instructions will guide Copilot to automatically apply the same transformation patterns during future modifications. Follow this methodology:

### Phase 1: Comparative State Analysis

#### Structural Changes Detection
- Compare folder structure between ${SOURCE_REFERENCE} and ${TARGET_REFERENCE}
- Identify moved, renamed, or deleted files
- Analyze changes in configuration files
- Document new dependencies and removed ones

#### Code Transformation Analysis
${MIGRATION_TYPE == "Framework Version" ?
  "- Identify API changes between framework versions
   - Analyze new features being used
   - Document obsolete methods/properties
   - Note syntax or convention changes" : ""}

${MIGRATION_TYPE == "Architecture Refactoring" ?
  "- Analyze architectural pattern changes
   - Identify new abstractions introduced
   - Document responsibility reorganization
   - Note changes in data flows" : ""}

${MIGRATION_TYPE == "Technology Migration" ?
  "- Analyze replacement of one technology with another
   - Identify functional equivalences
   - Document API and syntax changes
   - Note new dependencies and configurations" : ""}

#### Transformation Pattern Extraction
- Identify repetitive transformations applied
- Analyze conversion rules from old to new format
- Document exceptions and special cases
- Create before/after correspondence matrix

### Phase 2: Migration Instructions Generation

Create a `.github/copilot-migration-instructions.md` file with this structure:

\`\`\`markdown
# GitHub Copilot Migration Instructions
