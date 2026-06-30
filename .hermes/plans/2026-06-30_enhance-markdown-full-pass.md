# /enhance-markdown full pass — Prompt Markdown Optimization

Goal: fully optimize all `.prompt.md` files under `./prompts` using an enhance-markdown workflow, with strict verification and cancellation if any prompt fails validation/results review.

## Execution Rules
- Sequential pass over each prompt; do not batch write in one bulk sweep.
- Preserve exact YAML frontmatter, heading text, and required section names.
- Enforce:
  - one blank line between sections,
  - blank line before and after lists,
  - tables fit readable line width,
  - consistent header punctuation/capitalization,
  - collapse obvious redundancy without changing meaning.
- After each prompt, run local structural checks:
  - frontmatter opens with `---` and closes with `---`
  - no duplicate `---` blocks
  - required sections present per prompt
- If a prompt cannot be improved cleanly, stop, report the exact path and reason, and await direction.

## Completion Criteria
- All `.prompt.md` files in `./prompts` are processed.
- `docs/enhance-markdown-results.md` exists with per-prompt status (改进/无变更/阻塞).
- No verified markdown errors remain.

## Output Artifacts
- `docs/enhance-markdown-results.md`
