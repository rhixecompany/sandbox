# Repo Management Workflow Snapshot

Use this note when a prompt drives multi-repo inventory, branch normalization, ignore-file auditing, or research-doc cross-referencing.

## Working Pattern
- Read the driving prompt file first.
- Verify live state with `git`, `gh`, auth, and current directory before planning.
- Choose the Hermes profile that matches the task class.
- Inventory repos from live branch and remote state.
- Record branch counts, default branch, and ignore-file coverage before making changes.
- Write or refresh the inventory snapshot doc before deeper edits.

## Verification
- Compare local branch count, remote branch count, and default branch.
- Treat branch normalization as complete only when the intended `production` / `development` shape is present on both sides.
- Keep research-doc cross-references aligned with the current repo list.
