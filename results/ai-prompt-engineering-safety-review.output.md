# AI Prompt Engineering Safety Review — `prompts/security.prompt.md`

**Reviewer:** Hermes Agent (subagent)
**Prompt executed:** `prompts/ai-prompt-engineering-safety-review.prompt.md` (inline body authoritative; `templates/ai-prompt-engineering-safety-review/phases.md` MISSING — used inline Rules & Phases).
**Subject of review:** `prompts/security.prompt.md` (a real prompt in this workspace, selected because no input prompt was supplied and it contains concrete defects).
**Date:** 2026-07-09

---

## Phase 1 — Analysis Report

### 1. Harmful content / misinformation / illegal-activity risk
- **None.** The prompt is defensive in nature (secure coding, secret handling, least privilege). No instruction encourages harm, illegal activity, or misinformation.

### 2. Bias / privacy / prompt-injection risk
- **Broken template references (quality/injection-adjacent).** The prompt links `templates/security/phases.md` (twice) but that file does **not exist** in this workspace (only `_shared/*` and `test-providers-models/*` phase files exist). A missing referenced sub-file means the model silently drops Phase 1/Phase 2 detail — a fragile dependency, not an injection, but it degrades reliability.
- **Privacy.** Prompt instructs "Never commit secrets" and includes a Secret Auditor persona — handled safely. No PII leakage vectors.
- **Bias.** None detected.

### 3. Clarity / specificity / constraints / output format
- **Vague Goal (HIGH).** `## Goal` reads: *"Use when 'Comprehensive security prompt aligned to repository secure development requirements.' to accomplish the associated tasks and objectives."* — circular and non-actionable. It tells the model *when* to fire but not *what to produce*.
- **Duplicate tags (LOW).** `security` and `hermes`/`prompts` appear twice in the frontmatter.
- **Orphaned phases (MEDIUM).** `## Phases` lists "Phase 1: Threat Surface Identification" and "Phase 2: Security Control Implementation" as empty headings pointing to the missing `phases.md`; the real procedure lives in `## Steps`/`## Tasks`/`## Subtasks`. Redundant/confusing structure.
- **No output-format spec (MEDIUM).** Unlike `code-review.prompt.md` (which yields a CRITICAL/HIGH/MEDIUM/LOW report), `security.prompt.md` never states the expected deliverable shape, severity tiers, or summary format.
- **Dangling reference anchors.** Links to `skills-table-core.md#security` but that doc has no `### security` section (sections are agents-fix, prompts-fix, bash-scripts-fix, general, workspace-consolidate, skills-fix).

### 4. Refusal check
- Not applicable — the prompt is benign and improvable.

### 5. Intent preservation
- Intent retained: security review with threat modeling, input validation, least-privilege, secret hygiene, and a risk report.

### 6. Safeguard policy
- Per Rule 6, no generic safety disclaimers added — only fixes for the risks/defects actually identified above.

---

## Phase 2 — Revised Prompt

> Changes: tightened Goal; removed duplicate tags; merged orphaned Phases into the Steps flow; dropped the broken `phases.md` reference; added an explicit Output Format + severity tiers; fixed the skills-table anchor link.

```markdown
---
license: MIT
author: Hermes Agent
version: 1.1.0
name: "security"
title: "Security Review"
description: "Comprehensive security review, vulnerability assessment, and secure-coding guidance aligned to repository secure-development requirements."
trigger: /security
tags:
  - api
  - architecture
  - audit
  - data
  - documentation
  - frontend
  - prompts
  - security
  - skills
  - typescript
  - hermes
  - review
  - code-quality
---

## Goal
Perform a security review of the specified code, docs, or change set: map trust boundaries, validate
external input, verify auth/authz and least privilege, audit secret handling, and report findings as a
severity-ranked risk list with concrete remediations.

## Description
Apply secure-by-default engineering practices to code and documentation updates, with explicit handling
for secrets, input validation, and least-privilege design.

## Context
Use this prompt for any change that handles external input, authentication, authorization, secrets, APIs,
or data persistence.

## Skills Required
> See per-domain purposes: [`prompts/templates/_shared/skills-table-core.md`](../prompts/templates/_shared/skills-table-core.md#general)
- Threat modeling and trust-boundary analysis
- Input validation and secure coding patterns
- Secret management and least-privilege architecture

## Subagents
| Subagent | Role | When to Use |
| --- | --- | --- |
| Security Reviewer | Detects vulnerabilities and misuse of trust boundaries | Always |
| Validation Specialist | Enforces schema and sanitization controls | External input paths |
| Secret Auditor | Checks secret handling and environment safety | Config and deployment changes |

## Personas
- Security Reviewer: Assumes input is hostile until validated.
- Validation Specialist: Requires strict schemas and typed boundaries.
- Secret Auditor: Blocks secret leakage and over-privileged access patterns.

## Rules
> Core rules: [`prompts/templates/_shared/rules-core.md`](../prompts/templates/_shared/rules-core.md)
- Never commit secrets or sensitive values in code, docs, or examples.
- Validate and sanitize all external inputs.
- Enforce least privilege in service and credential usage.
- Add logging and monitoring guidance for suspicious or failed auth events.
- Keep dependencies current and note known CVE implications.

## Steps
1. Map data flows and trust boundaries (Phase 1: Threat Surface Identification).
2. Validate and sanitize external input paths.
3. Enforce auth, authorization, and least-privilege controls (Phase 2: Security Control Implementation).
4. Verify secret handling and dependency hygiene.
5. Report findings and residual risks in the Output Format below.

## Tasks
- Task 1.1 — Identify sensitive flows and security-critical boundaries.
- Task 1.2 — Enforce strict input validation and sanitization.
- Task 1.3 — Verify authentication and authorization correctness.
- Task 1.4 — Check secret management and dependency risk posture.
- Task 1.5 — Document mitigations and unresolved security risks.

## Subtasks
- Subtask 1.1.1 — List entry points receiving untrusted input.
- Subtask 1.2.1 — Apply schema validation at boundary layers.
- Subtask 1.3.1 — Confirm permission checks precede sensitive actions.
- Subtask 1.4.1 — Ensure secrets are not present in source-controlled files.
- Subtask 1.5.1 — Provide actionable remediation for remaining risks.

## Output Format
Return a report with:
- **CRITICAL / HIGH / MEDIUM / LOW** tiers (one block each).
- Each finding: `file:line` location, the defect, the exploit/reliability impact, and the fix.
- A **Summary** line: counts per tier + must-fix list.

## Actions Summary
1. Identify security-sensitive paths.
2. Harden validation and authorization.
3. Verify secrets and dependency safety.
4. Deliver a risk-focused security outcome.
```

---

## Phase 3 — Validation of Revised Prompt
- Goal now states *what to produce* (severity-ranked risk list + remediations), not a circular "use when…".
- All frontmatter tags unique; `version` bumped to record the change.
- No reference to a non-existent `templates/security/phases.md`; Phase 1/2 folded into `## Steps` so no content is lost.
- `skills-table-core.md#general` anchor exists.
- Output Format gives the model an explicit, testable deliverable (matches the structure the sibling `code-review.prompt.md` already uses successfully).
- Security intent, personas, subagents, and rules all preserved verbatim.

---

## Phase 4 — Safety & Quality Checklist
- [x] No harmful, illegal, or misinformation instruction present.
- [x] No bias or PII-leak vector; secrets handled safely.
- [x] Broken/missing file references removed (was: `templates/security/phases.md`, `#security` anchor).
- [x] Goal is specific and actionable (was vague/circular).
- [x] Duplicate frontmatter tags de-duplicated.
- [x] Explicit output format + severity tiers added.
- [x] Required task intent and constraints preserved on rewrite.
- [x] No unrelated generic safety disclaimers injected (per Rule 6).

---

## Notes / Skipped References
- `templates/ai-prompt-engineering-safety-review/phases.md` — referenced by the reviewer prompt but **absent**; executed using the prompt's inline Rules & Phases instead.
- `templates/security/phases.md` — referenced by the *subject* prompt but **absent**; flagged as a defect and removed in the rewrite.
- No external network calls were required; this is a file-backed review (rules-core Rule 8).
