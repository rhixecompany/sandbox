# Migration Instructions: {{ MIGRATION_NAME }}

## Configuration

| Variable | Value |
|----------|-------|
| Migration Type | {{ Framework Version | Architecture Refactoring | Technology Migration | Dependencies Update | Pattern Changes }} |
| Source Reference | {{ branch/commit/tag }} |
| Target Reference | {{ branch/commit/tag }} |
| Analysis Scope | {{ Entire project | Specific folder | Modified files only }} |
| Automation Level | {{ Conservative | Balanced | Aggressive }} |
| Generate Examples | {{ true/false }} |

## Detected Changes

| Category | Description |
|----------|-------------|
| Structural | {{ file moves, renames, deletes }} |
| API Changes | {{ before/after correspondence }} |
| New Patterns | {{ what to adopt }} |
| Obsolete Patterns | {{ what to avoid }} |

## Generated Instructions Output

- **File**: `.github/copilot-migration-instructions.md`
- **Status**: {{ pending / generated / validated }}

## Verification

- [ ] Source and target references exist
- [ ] Structural changes detected
- [ ] Code transformation patterns extracted
- [ ] Migration instructions file generated
- [ ] Instructions applied and verified on test code
- [ ] Edge cases documented