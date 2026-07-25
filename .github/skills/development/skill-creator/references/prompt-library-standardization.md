# Prompt Library Standardization

## Session Learnings

- Treat the prompt library as class-level umbrellas, not a pile of one-off session prompts.
- For broad prompt refactors, keep the original prompt body under a clearly labeled `Legacy Prompt Details` section after the new normalized wrapper.
- Prefer a consistent wrapper shape for migrated prompt files:
  - Goal
  - Context
  - Inputs
  - Outputs
  - Rules
  - Phases
- Normalize awkward generic context lines so they read naturally and are reusable across prompts.
- Add a cross-reference section to legacy docs (`Prompts/*.md`) so older prompt files point at the newer `.github/prompts` library.

## Safe Workflow

1. Check git status and capture a focused checkpoint if needed before batch edits.
2. Normalize a small sample first.
3. Verify the sample before scaling to the rest of the set.
4. Preserve original content unless the refactor is explicitly meant to replace it.
5. Re-read a few representative files after the batch to confirm consistency.

## Notes

- This pattern is for prompt-library cleanup and migration work, not for creating narrow throwaway skill files.
- If a prompt body is still useful, preserve it rather than deleting it during normalization.