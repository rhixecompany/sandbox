---
name: comprehensive-hermes-maintenance-approval
title: Comprehensive Hermes Maintenance Approval Record
description: "Authorize the approved maintenance scope with secret, deletion, hook, and release boundaries."
version: 1.0.0
author: Alexa
license: MIT
tags: [approval, hermes, maintenance, safety]
status: approved
plan: .hermes/plans/comprehensive-hermes-maintenance-plan.md
spec: .hermes/specs/comprehensive-hermes-maintenance-spec.md
prompt: .github/prompts/comprehensive-hermes-maintenance.prompt.md
---

- Requestor: Alexa
- Owner: Alexa
- Approved: 2026-09-05 (initiating request)
- Approval basis: the owner explicitly authorized destructive operations, fixes, creations, updates, enhancement, commit, and push in the initiating request.
- Approval scope: `C:/Users/Alexa/Desktop/SandBox`, independently detected nested Git repositories, and `C:/Users/Alexa/AppData/Local/hermes`.
- Plan: `.hermes/plans/comprehensive-hermes-maintenance-plan.md`
- Spec: `.hermes/specs/comprehensive-hermes-maintenance-spec.md`
- Prompt: `.github/prompts/comprehensive-hermes-maintenance.prompt.md`

## Owner decision

`+1` — proceed with the comprehensive implementation under the approved scope.

## Safety boundaries retained

- Preserve Hermes, OpenCode, Copilot, and Codex.
- Preserve active, referenced, ambiguous, credential-sensitive, model, and MCP/toolkit resources unless an explicit dry-run allowlist proves they are unused.
- Never expose, copy, hash, stage, or commit `.env` values, tokens, private keys, or credential-bearing configuration.
- Synchronize only the managed Hermes `quick_commands` projection through `hermes config set`; do not replace `config.yaml` wholesale.
- Keep platform-specific MCP schemas and intentional profile differences.
- Use non-forced, fast-forward Git pushes only. Stop on authentication, permission, protected-branch, lock, or non-fast-forward errors.
- Never create backup files; use Git or recorded skill patches for rollback.

## Destructive actions covered

- Removal of exact, unreferenced, non-secret duplicate files after reference checks.
- Removal of explicitly allowlisted inactive Docker resources after dry-run and post-check.
- Removal of proven orphaned/duplicate/unconfigured agent assets, preserving the four required platforms.
- Approved live configuration projections and hook allowlist changes only when the relevant focused verification passes.
- Safe commits and pushes of verified, non-secret changes.

## Rollback

- Workspace: `git restore -- <path>` or `git revert <commit>`.
- Hermes quick commands: restore the captured mapping with `hermes config set quick_commands <mapping>`.
- Skill changes: reverse the exact `skill_manage` patch recorded in the phase report.
- Hooks: remove only newly approved allowlist entries if lifecycle tests regress.
- Docker: no recovery is assumed for deleted volumes/images; the allowlist gate is mandatory.

## Verification required before release

- Prompt/spec/plan frontmatter and cross-references parse.
- Environment/config reports contain paths and key names only.
- Every supported Hermes root script has exactly one tested wrapper audit command.
- Scripts-judge quick-command hard gate passes.
- Hermes hooks/plugins/desktop/agents/session/context/system-prompt diagnostics are classified with evidence.
- MCP configs parse, translations are synchronized, and live/runtime checks are recorded.
- Dedupe and Docker post-state matches the allowlist.
- Relevant tests and secret scan pass.
- Commit IDs and remote branch readback are captured.

## Phase log

- M0 baseline: complete before this approval record; evidence under `.hermes/reports/baseline/`.
- M1 plan/spec/prompt/approval: in progress at creation; verify after write.
- M2–M8: pending sequential gates.
