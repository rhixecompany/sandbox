# Local Instructions Discovery Process

> Extracted from `suggest-awesome-github-copilot-instructions.prompt.md`.

## Local Instructions Discovery Process

1. List all `*.instructions.md` files in the `instructions/` directory
2. For each discovered file, read front matter to extract `description` and `applyTo` patterns
3. Build comprehensive inventory of existing instructions with their applicable file patterns
4. Use this inventory to avoid suggesting duplicates
