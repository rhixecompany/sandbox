# Update Handling

> Extracted from `suggest-awesome-github-copilot-instructions.prompt.md`.

## Update Handling

When outdated instructions are identified:

1. Include them in the output table with ⚠️ status
2. Document specific differences in the "Suggestion Rationale" column
3. Provide recommendation to update with key changes noted
4. When user requests update, replace entire local file with remote version
5. Preserve file location in `.github/instructions/` directory

