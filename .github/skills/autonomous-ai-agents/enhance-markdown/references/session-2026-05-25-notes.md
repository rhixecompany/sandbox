Session: enhance-markdown — 6 Prompts
Date: 2026-05-25

Summary of live run (short):
- Resumed from existing artifacts and reconstructed missing Phase 1 artifacts.
- Ran Phase 3 catchup with append-only edits to `.github/prompts/*` files where necessary.
- Ran Phase 4 verification; wrote docs/enhance-markdown-6prompts-verify-context.md.

Operational notes (for future runs):
- Backup policy: always read C:\\Users\\Alexa\\AppData\\Local\\hermes\\.hermes_policies before making backups. If backup.enabled=false -> do not create scattered .bak files. Use backups/ when enabled.
- Phase 3 default edit mode: append-only unless user explicitly approves in-place edits or patch review.
- Validator script and daily cron exist under scripts/ and docs/; skill should reference them in the merge notes.

User preferences captured:
- Concise, action-first responses
- Prefer PowerShell for local commands; but automation may run under git-bash/MSYS
- Require explicit approval before git commits or destructive operations

Tool-limit fallback:
- When delegate_task fails with tools-array-too-long, fallback to execute_code using hermes_tools. Example code snippet is provided in references/tool-limit-workaround.md

References to artifacts created this session:
- docs/enhance-markdown-6prompts-context.md
- docs/enhance-markdown-6prompts-issues-context.md
- docs/enhance-markdown-6prompts-fix-issues-context.md
- docs/enhance-markdown-6prompts-verify-context.md
- thoughts/plans/enhance-markdown-6prompts-debug.md
- docs/enhance-markdown-6prompts-merge-notes.md

Verification summary:
- Fixed: 14 | Partial: 5 | Not fixed: 1
- Recommendation: merge now; follow-up PR to consolidate append-only notes into in-place edits for partial items.
