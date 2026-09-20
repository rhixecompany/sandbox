---
name: init-copilot-hermes-opencode-cursor-agent
version: 1.0.0
status: complete
run: init-copilot-hermes-opencode-cursor-agent-20260919T203754Z
---

# Initialize Agent Context

## Goal

Enhance the repository's shared system prompt and context-file architecture for GitHub Copilot, Hermes, OpenCode, and Cursor Agent without duplicating rules or inventing unsupported configuration.

## Clarification Gate

Before implementation, when the user is available, ask up to three focused questions per turn. The questions must cover:

- What changed between the old and new request?
- What is in scope and out of scope?
- What work remains?
- What blockers or missing inputs exist?
- Which optional or recommended improvements should be included?
- Which actions require approval?

Continue until material ambiguity is resolved. If the user is unavailable, use recommended defaults and record the assumption.

## Execution

1. Read the nearest `AGENTS.md`, tool adapters, project manifests, and relevant tests.
2. Create or update the current run directories:
   - `ai-agent-home/specs/<unique-timestamped-run>/`
   - `ai-agent-home/plans/<unique-timestamped-run>/`
   - `ai-agent-home/prompts/<unique-timestamped-run>/`
3. Keep `AGENTS.md` canonical and adapters thin.
4. Treat `projects/*` as autonomous subprojects.
5. Protect `.env`, keys, certificates, credentials, and unrelated worktree changes.
6. Validate the exact requested behavior.
7. Update spec, plan, and prompt status to `COMPLETE` only after all gates pass.

## Completion Output

Report changed files, validation evidence, unresolved blockers, and the run artifact path. Never claim capabilities, profile state, or verification results that were not observed.
