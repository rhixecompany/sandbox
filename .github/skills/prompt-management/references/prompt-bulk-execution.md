# Prompt Bulk Execution — Recipe & Pitfalls

Condensed from a 215-prompt library run (SandBox/prompts/). Use when executing an entire `prompts/` directory, not one prompt.

## Inventory first (always)
```
ls prompts/*.prompt.md | wc -l
```
215 prompts ≈ 29.7k lines. Do NOT blind-execute.

## 1. Reconcile template paths
Prompts reference `templates/` at repo root, but files often live in `prompts/templates/`.
```
cp -r prompts/templates/. templates/      # git-tracked, reversible
```
Re-scan after to measure remaining missing refs.

## 2. Missing per-prompt bodies
`templates/<name>/phases.md`, `workflow_steps.md`, `cost_optimization_brief.md` etc. are
usually ABSENT from the repo. The prompt's inline body (Goal/Context/Phases/Steps) is the
authoritative spec. Run from inline; never invent template content.

## 3. Classify by external side-effect
Regex anchor (case-insensitive) on body:
`azure|az-|aws|gcp|kubernetes|kubectl|terraform|docker|containerize|deploy|github action|
pull request|\bPR\b|create-github-issue|secret|credential|ssh|smtp|spring boot|aspnet|
cosmosdb|appstore`
- **Safe (local)**: generate/audit/blueprint/doc prompts → execute.
- **External**: GitHub/Azure/Docker/Spring → gate behind explicit user auth; else emit a
  dry-run "blocked: needs creds" artifact, clearly labeled.

## 4. Batch with delegate_task (cap = 3)
`delegate_task` rejects >3 tasks. Split into batches of ≤3 parallel leaf delegations.
Each subagent context must be self-contained:
- absolute path to the prompt file
- "inline body is authoritative; per-prompt templates/<name>/*.md absent; do not fabricate"
- explicit output path `results/<name>.output.md`
- classification + report format (≤8 lines: action, path, skipped refs)

## 5. Verify the batch plan before firing
Ad-hoc check: every batch ≤3 tasks, every task references a prompt file that exists on disk,
distinct prompts == safe-set from manifest. Use a `tempfile` verifier, clean up after.

## Dry-run / pilot
Launch 3–5 safe prompts first to confirm the read→execute→write pattern, THEN scale.

## Output convention
Write real artifacts to `results/<name>.output.md`. No stubs. Blocked external prompts still
get a real (labeled) artifact, not silence.
