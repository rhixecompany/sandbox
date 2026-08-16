# RESEARCH_REPORT Boundary Checks

Use when editing bounded sections of existing `RESEARCH_REPORT.md` files, especially "Related Projects" and "Resources".

## Verified Procedure

- Read a full surrounding section window before patching.
- If repeated patch runs miss because section text is only partially visible, switch approaches:
  - rerun with a larger `limit`/offset window, or
  - run a small local script that diffs the exact target block before any write.
- After edits, run a strict reverse-reference check instead of regex heuristics:
  - collect project names from `projects/*/RESEARCH_REPORT.md`, then
  - collect referenced project names from `^- \*\*(.+?)\*\*` lines, then
  - fail if `source not in reverse_refs[target]`.
- Do not patch unread sections blindly.

## Script Reference

- Workspace check script: use the inline script from `references/research-report-boundaries.md` procedure.
