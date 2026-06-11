# Prompts Markdown Safety And Quality Review

Generated: 2026-05-25
Scope: `Prompts/*.prompts.md`

## Findings Summary

- High severity: 0
- Medium severity: 0
- Low severity: 2

## Findings

1. Low: Typo in backup rule wording in `Prompts/commands-fix.prompts.md` (`backsup` -> `backups`).
2. Low: Dependency naming drift in `Prompts/commands-fix.prompts.md` (`dispatching-parallel-agents` did not match plaintext source intent for commands workflow).

## Safety Checks Applied

- Harmful or illegal content risk: none detected.
- Prompt-injection risk: low; prompts are procedural and file-scoped.
- Privacy risk: low; no secrets, tokens, or credentials requested.
- Clarity risk: low after fixes; phase outputs are explicit.

## Improvements Applied

- Corrected typo in backup rule for clearer operational instruction.
- Aligned command workflow dependency naming with source intent to reduce execution ambiguity.
- Updated repo migration prompt flow to include explicit merge prompt generation and execution verification.

## Residual Risks

1. External skill/tool availability is assumed and not runtime-validated inside these prompts.
2. Some prompts are broad by design and can still produce large-scope changes unless constrained by caller input.

## Revised Safety Checklist

- [x] Explicit phase ordering retained.
- [x] Output artifacts are path-specific.
- [x] No instruction to expose secrets.
- [x] No unsafe or disallowed behavior introduced.
