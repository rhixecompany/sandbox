# Hermes Prompt Normalization Notes

Session-derived notes for normalizing prompts into a stricter Hermes-friendly structure.

## What worked well
- Use a consistent top-level structure: Goal, Context, Inputs, Outputs, Rules, Phases, Actions Summary.
- Keep sections short and direct; avoid long prefatory prose.
- Preserve the original task intent while removing duplicate or conflicting instructions.
- Make workflows explicit with phased steps and short task lists.
- Add a concise list of related prompts when porting useful prompts into companion markdown files.

## Prompt classes normalized in this session
- Hermes breakdown prompts:
  - epic PRD
  - epic architecture
  - feature PRD
  - feature implementation plan
  - test strategy / QA plan
  - project plan
- Next.js planning prompts:
  - page refactor / DRY cleanup / test hardening
  - repository-wide refactor and upgrade
  - markdown refactor and documentation normalization
  - component and test consolidation

## Practical heuristics
1. Start with a clean YAML frontmatter block when the prompt is shared across systems.
2. Make the workflow usable by an agent without requiring hidden context.
3. Use short declarative rules instead of long narrative paragraphs.
4. Include verification steps so the prompt is self-checking.
5. When a prompt family overlaps, prefer a broader class-level shape over a one-off rewrite.

## Common pitfalls
- Don't preserve legacy fluff or duplicated sections when converting older prompt drafts.
- Don't bury important constraints after long explanatory paragraphs.
- Don't mix multiple prompt styles in one file unless the prompt explicitly needs that.
- Don't forget to preserve the original output path or artifact names.
- Don't invent scope beyond the source artifacts.

## Porting checklist
- Confirm the prompt is worth keeping.
- Normalize headings and section order.
- Trim redundant prose.
- Add explicit phases and actions.
- Verify file paths and output targets.
- If useful, add a short "related prompts" list to companion `.md` docs in `Prompts/`.