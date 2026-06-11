references/session-2026-05-24-notes.md

Lessons from running the focused content pass and subagent orchestration on 2026-05-24.

1) Always provide full task text in delegate_task context
- Rationale: prevents subagents from having to read large plan files and avoids context window issues.
- Example: include the original plan snippet, test steps, and exact file paths in the context block.

2) Gate sequence: Spec -> Quality -> Integration
- Reaffirmed: Spec compliance must run before code quality review. Document this as a hard rule in the skill.

3) Handling repeated questions from implementer subagents
- If an implementer repeatedly asks the same clarification, escalate to a human decision file and pause the task.

4) Verification artifacts
- After each completed task, produce 3 artifacts:
  a) commit id (if committed locally)
  b) per-file verification checklist
  c) test run summary (pytest short log)

5) Automation pitfalls
- When automating multi-task runs, keep subagent spawn depth = 1 to avoid runaway delegation loops. If deeper nesting is needed, require an orchestrator role with explicit approval.

6) Default conventions
- Batch size for per-task commits: 1 task per commit is ideal for traceability. For mass edits (skill updates), keep batch size = 7.

