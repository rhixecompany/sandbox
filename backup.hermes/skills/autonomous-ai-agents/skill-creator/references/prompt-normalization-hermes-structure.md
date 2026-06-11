# Prompt Normalization for Hermes-Friendly Structure

Use this reference when consolidating or refactoring prompt files migrated into a Hermes-managed repository.

## Canonical shape

Prefer a single, clean structure with these sections in order:

1. YAML frontmatter
2. Description
3. Context
4. Skills Required
5. Subagents
6. Personas
7. Rules
8. Phases
9. Steps
10. Optional summary / handoff notes

## What to preserve

- Original task intent and user-facing behavior
- Compatibility metadata needed by multiple runtimes
- Any project-specific constraints or safety rules
- Useful role/persona definitions when the prompt relies on subagents

## What to remove

- Duplicate embedded frontmatter blocks
- Legacy repeated section headers from old prompt formats
- Empty filler text, puffery, or repeated paraphrases of the description
- Conflicting instructions that say the same thing in multiple ways

## Normalization rules

- Use one frontmatter block only.
- Keep metadata minimal and parseable.
- Make section labels consistent across files.
- Prefer short imperative bullets over prose paragraphs.
- Keep each phase bounded to a clear goal, steps, and tasks.
- If a prompt is being replaced by a cleaner source, rewrite from the cleaner source instead of merging noisy historical text.

## Safety and workflow notes

- Use git status and a focused checkpoint commit if needed; do not create timestamped backup copies.
- If the source file is malformed, normalize from the most legible copy available.
- Keep the prompt compatible with Hermes, Copilot, and OpenCode when the repo expects cross-tool support.
- Avoid changing the actual task semantics while improving structure.

## Example trigger

A good trigger for using this reference is a migrated prompt set that has:

- repeated YAML-like blocks inside the body
- inconsistent headings across files
- a mixture of old and new prompt styles
- duplicate step lists that can be collapsed into one canonical flow
