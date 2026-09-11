---
name: four-goal-execution
title: Four-Goal Execution Prompt (G1-G4)
description: "Executable prompt: research artifacts, skills dedupe/judge/fix, model benchmark, profile sync."
version: 1.0
author: Alexa
tags: [execution, skills, models, research, sync]
spec: .hermes/specs/2026-09-11-four-goal-execution-spec.md
plan: .hermes/plans/2026-09-11-four-goal-execution-master-plan.md
---

# GOAL: Execute 4 sequential goals per spec

You are approved on all destructive operations. Follow the spec strictly; verify each gate before advancing. You are in `~/Desktop/SandBox` on Windows 11 (bash/MSYS2); hermes home = `C:\Users\Alexa\AppData\Local\hermes`.

## Phase 1 — Research artifacts (G1)

1. Keep existing `node-dependency.md`, `python-packages.md`, `technology-stacks.md`.
2. For each of the 11 research topic dirs (binance-api-tutorial, busha-api-tutorial, cryptocurrency-wallets-api-tutorial, face-mask-video-call-tutorial, flutterwave-tutorial, hermes-agents-tutorial, hermes-memory-files, paypal-tutorial, paystack-tutorial, python-asyncio-tutorial, + root-level md topics):
   - Create `skills/<topic>-skill/SKILL.md` (valid frontmatter, ≤250 lines, references/ for detail).
   - Create `scripts/<topic>.py` (or working shell equivalent; no inline scripts).
   - Create test for the script; run it; debug/fix until exit 0.
3. Create `hooks/` entry wiring the `research/` folder.
4. Update `requirements.txt` = union(pip freeze, python-packages.md). Run `pip check`. Verify top packages import.
5. Gate: all 11 tests green + pip check clean.

## Phase 2 — Skills dedupe + judge + fix (G2)

1. `hermes skills list` > `initial-skills.txt`. Record count. Read the file; find near-exact duplicates (name collisions across categories, e.g. `brainstorming` exists twice).
2. For each duplicate: keep the canonical category-placed copy; merge unique content into it (enhance); delete the others. Save deletion log to `results/skills-deduped-2026-09-11.md`.
3. Run skill-judge on remaining skills; record scores.
4. systematic-debugging: fix all debts/bugs/issues/warnings; target score ≥90 per skill.
5. `hermes skills list` > `updated-skills.txt`. Verify count(initial) > count(updated).
6. Debug/fix/verify every skill in updated-skills.txt, ascending order of `hermes skills list-modified`.
7. Execute `hermes skills audit && hermes skills check && hermes skills update`; fix findings.
8. Gate: counts proven + audit/check clean (or residual documented).

## Phase 3 — Free-model benchmark (G3)

1. List free/non-premium models: opencode-zen provider first, then openrouter, nous (`hermes auth list` + test-providers-models workflow).
2. For each model run `hermes chat` probes: latency (timed), accuracy (factual probe), context (long input), capabilities (self-report probe), tools (function-call probe), vision (image probe where supported).
3. Record every outcome — success/timeout/error, exactly as observed. No fabricated completions.
4. Write `results/models-benchmark-2026-09-11.md` with status table + which queries completed successfully.
5. Gate: report shows observed-only results.

## Phase 4 — Profile asset sync (G4)

1. Inventory `~/AppData/Local/hermes/profiles/*` (15 subdirs; classify the odd `profiles/skills` dir first — do NOT proceed until classified).
2. In each profile subdir: delete `skills/`, `hooks/`, `plugins/`, `scripts/`, `config.yaml`, `.env`.
3. Copy the same set from `~/AppData/Local/hermes` into every profile subdir.
4. Verify: tree diff per profile vs root empty; each config.yaml parses as YAML.
5. Gate: parity verified for all 15 subdirs.

## Rules

- Strict sequential; "only then" gates are hard.
- Verify before claim: every gate ends with tool evidence.
- Report progress in scannable bullets; lead with results; no fluff.
- Never echo .env/config.yaml contents.
- When complete: state "Goal complete" with per-goal evidence summary.
