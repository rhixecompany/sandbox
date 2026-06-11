Enhance-markdown — 6 Prompts

Merge notes (auto-generated)

Generated: 2026-05-25

Summary:
- Phase 1/2/3/4 pipeline run against Prompts/*.md completed.
- Verification doc: docs/enhance-markdown-6prompts-verify-context.md (14/20 fixed; 5 partial; 1 not fixed).
- Fix progress log: docs/enhance-markdown-6prompts-fix-issues-context.md
- Companion plan: thoughts/plans/enhance-markdown-6prompts-debug.md

Files modified (append-only catchup edits):
- Several prompt files under .github/prompts/ (append-only notes added; see verify/fix logs for details).

Recommended PR
- Branch name: enhance/6prompts-doc-fixes
- Title: docs: enhance-markdown fixes for 6 Prompts (Phase 1-4)
- Description: short summary + link to docs/enhance-markdown-6prompts-verify-context.md and docs/enhance-markdown-6prompts-fix-issues-context.md
- Reviewers: documentation lead, owner of Prompts/ files
- Labels: docs, enhancement

Quality gate & checks (run locally before opening PR):
1) Run validator: python3 ~/.hermes/scripts/validate_memories.py (or C:\Users\Alexa\AppData\Local\hermes\scripts\validate_memories.py) — must pass.
2) Run repo lint/format per project conventions.
3) Verify docs/verify-context.md present and up-to-date: docs/enhance-markdown-6prompts-verify-context.md
4) Optional: run grep to ensure no scattered .bak files under C:\Users\Alexa\AppData\Local\hermes (policy enforced). Command: git-bash: search_files pattern "*.bak" under hermes path (or Windows explorer).

Follow-up tasks (minor items) — created as todo entries (IDs):
- FMT-001, FMT-002, FMT-003, FMT-004, FMT-005, FMT-008, FMT-009
Each todo includes a failing test command in its description. See Hermes todo list (session) and docs/enhance-markdown-6prompts-issues-context.md for details.

Merge decision: recommended to merge now. Remaining minor items can be addressed in a small follow-up PR that consolidates appended notes into in-place edits.

Commands to create branch and PR (local; do not run without review):
- git checkout -b enhance/6prompts-doc-fixes
- git add docs/ .github/prompts/ .github/workflows/ (only changed files)
- git commit -m "docs: enhance-markdown fixes for 6 Prompts (Phase 1-4)"
- git push origin enhance/6prompts-doc-fixes
- Open PR with title and description above; attach docs/enhance-markdown-6prompts-verify-context.md and docs/enhance-markdown-6prompts-fix-issues-context.md

If you want, I can prepare the patch (diff) for review or open the PR for you — I will need repository remote access and auth (confirm and provide credentials).
