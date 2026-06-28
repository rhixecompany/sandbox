# Approval Gate Pattern

> Governance pattern for locking destructive/irreversible plan steps behind explicit human approval. Captured from 2026-06-16 unified ecosystem master plan Section 9.

## The Problem

Multi-phase plans often include destructive actions:
- Skill deletion/archival (`skill_manage action='delete'`)
- Config edits (`~/.hermes/config.yaml`, profile configs)
- Hook registration/deregistration (`hermes hooks` commands)
- MCP server install/uninstall/transport changes
- Bulk plugin enable/disable
- File/directory deletion in workspace or Hermes data dirs

Without a recorded approval gate, these happen on "mental consent" — no audit trail, no rollback plan, no verification requirement.

## The Pattern: Explicit Approval Gate

Before ANY destructive step, enforce this workflow:

### 1. Create Approval Request File

**Path:** `.hermes/approvals/<timestamp>_<short-title>.md`

**Required Fields:**

| Field | Description | Example |
|-------|-------------|---------|
| Requestor | GitHub handle or local username | `Alexa` |
| Owner(s) | Humans responsible for execution | `Alexa` |
| Scope | Concise list of files/skills/hooks/plugins/MCP servers changed | `51 skill SKILL.md patches, 26 re-judges` |
| Justification | Short reason for change | `Skills audit: 49 blocked, 87 critical findings` |
| Rollback Plan | Exact commands to revert | `git checkout HEAD -- <skill-path>/SKILL.md` |
| Verification Steps | Commands to run post-change + expected outputs | `hermes skills audit && hermes skills update` |
| Approval | Explicit `+1` from each Owner | `+1 (Alexa, 2026-06-16)` |
| Valid Until | ISO date | `2026-07-16` |

### 2. Notify & Wait

- Notify Owners (email/Slack/PR) with link to approval file
- **Wait for recorded `+1`** — do not proceed on verbal/mental consent
- Collect approvals as comments or signed messages in the approval file

### 3. Execute with Traceability

- Include approval filename in commit message: `git commit -m "fix: remediate skills per .hermes/approvals/2026-06-16_skills-remediation-approval.md"`
- Execute the plan steps

### 4. Post-Change Verification

- Run all verification steps from approval file
- Append actual outputs to approval file
- Update status: `VERIFIED` or `FAILED`

### 5. Rollback on Failure

- Execute rollback plan exactly
- Document remediation in approval file
- Re-open approval if re-attempt needed

## Approval Request Template

```markdown
# Approval Request: <Title>

**Date:** YYYY-MM-DD
**Requestor:** <username>
**Owner(s):** <list>
**Status:** PENDING

## Scope
<concise list of changes>

## Justification
<short reason>

## Rollback Plan
```bash
# Exact revert commands
```

## Verification Steps
1. <command> → <expected output>
2. <command> → <expected output>

## Approval
**Owner:** _______________ **Date:** _______________ **Signature:** +1
**Valid until:** YYYY-MM-DD

## Post-Execution Notes
_To be filled after execution:_
- Commit SHA: _______________
- Verification outputs appended: [ ] Yes [ ] No
- Any failures/remediation: _______________
```

## When to Require Approval

Per master plan Section 9, approval is mandatory for any plan step that:

- Edits `~/.hermes/config.yaml` or profile-specific config files
- Registers/deregisters hooks via `hermes hooks` commands
- `skill_manage(action='delete')` or any skill write that removes content
- Installs/uninstalls MCP servers or changes their transport
- Deletes files/directories in `C:\Users\Alexa\AppData\Local\hermes\` or workspace root
- Bulk plugin enable/disable operations

## When Approval is NOT Required

- Read-only operations (verification, audit, status checks)
- Non-destructive edits (patch adding content, config additions)
- Creating new files/artifacts (approval requests themselves, reports)
- Phase 0 inventory verification

## Anti-Patterns

| Anti-Pattern | Risk | Fix |
|--------------|------|-----|
| "I'll approve in my head" | No audit trail, no accountability | File + recorded `+1` mandatory |
| Verbal approval in chat | Not in repo history, lost context | Write to approval file |
| No rollback plan | Irreversible damage on failure | Rollback commands required in approval |
| Skip verification | Silent failures | Verification steps required + append outputs |
| Approve after execution | Retroactive justification | Gate is BEFORE execution |

## Example: Skills Remediation Approval (2026-06-16)

**File:** `.hermes/approvals/2026-06-16_skills-remediation-approval.md`

- **Scope:** 51 skills patch + 26 re-judge (77 skills total)
- **Justification:** Audit shows 49 blocked, 87 critical findings
- **Rollback:** `git checkout HEAD -- <skill-path>/SKILL.md` per skill
- **Verification:** `hermes skills audit && hermes skills update` passes
- **Status:** PENDING Owner `+1`

## Integration with executing-plans

```
Phase 3: Review & Checkpoint
  → If next phase has destructive steps: CREATE APPROVAL GATE
  → Wait for recorded +1
  → Execute with traceability
  → Verify & append outputs
  → Rollback on failure
```