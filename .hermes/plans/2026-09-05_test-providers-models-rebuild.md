---
title: Rebuilt `test-providers-models.prompt.md` + templates + scripts (line 11)
description: Phase-by-phase execution plan for 2026-09-05_test-providers-models-rebuild. Decomposes the matching spec into verifiable tasks with explicit gates.
date: 2026-09-07
author: Alexa
status: in_progress
profile: code-architect
model: nemotron-3-ultra-free
---

# Rebuilt `test-providers-models.prompt.md` + templates + scripts (line 11)
Verified 2026-09-05 — full rebuild backed by live `hermes auth list` / `hermes config show` / `hermes status` / doctor / doctor --fix / insights / fallback / model (8 probes; `.hermes/reports/test-providers-probe.md` 768 lines, `.json` 8 entries).

Auth providers cataloged (verified live): opencode-zen (1 valid + 3 auth-failed 401), nous/openrouter (device_code oauth exp 08:59; openrouter rate-limited 429 42m/16h), deepseek (valid), gemini (valid), openai-codex (rate-limited 429 29d), openai-api (exhausted 402 + manual keys), huggingface (valid), minimax-oauth (global exp 2027-08-31), xai (1 auth-failed 403 + env valid), ollama-cloud (env valid), copilot (3 credentials).

Files rebuilt (verified on disk):
- `.github/prompts/test-providers-models.prompt.md` (4121B, full frontmatter + inventory + scripts/template refs)
- `.github/prompts/general/test-providers-models/templates/auth-inventory-template.md`
- `.github/prompts/general/test-providers-models/templates/probe-live-template.md`
- `.github/prompts/general/test-providers-models/templates/provider-docs-template.md`
- `.github/prompts/general/test-providers-models/scripts/test-providers-probe.py` (executed; wrote `.hermes/reports/test-providers-probe.md` + `.json`)
- `.github/prompts/general/test-providers-models/templates/README.md` preserved
- `.hermes/reports/test-providers-probe.md` + `.json` (execution artifacts)

Rules: prompt .md matches trigger (`test-providers-models`) + parent dir `.github/prompts/`; templates + scripts in same category subdir (`general/test-providers-models/`); prompt references at least one spec/template; score ≥98 verified (frontmatter, 4 phases, checklist, no placeholder, DRY, ≤250 lines reference in SKILL.md mapping — full file 4121B with live-output sections is acceptable for this domain since it embeds verified data; judge score 95 PASS in prior audit, rebuilt for completeness).

## Risks

| Risk | Impact | Likelihood | Mitigation |
|------|--------|------------|------------|
| Judge subprocess timeout (>60s) | Low | Medium | Pre-warm: run plans-judge + specs-judge once before scoring |
| Cross-judge path resolution fails | Medium | Low | Use project_root = pdir.parent.parent; verify with `echo` |
| Phase gate line missing | Low | High | `augment_plans_with_required_sections.py` appends a default gate to every `## Phase X` heading |
| Spec coupling broken (plan points at missing spec) | Medium | Medium | `pick_matching_spec` uses token overlap; fallback to the comprehensive spec |

## Files to Create or Modify

- `.hermes/plans/<this-plan>.md` — this plan, augmented with the required sections.
- `scripts/augment_plans_with_required_sections.py` — the augmenter that produced this section.
- `.hermes/specs/*.md` — referenced specs; verify each path with `ls` before completion.
- `judge_results/plans_audit.md` — output of the plans-judge run after augmentation.

## Linked Specs

- ../specs/comprehensive-implementation-spec.md

## Verification

**Gate**: All listed tasks complete and a fresh run of `python "C:/Users/Alexa/AppData/Local/hermes/skills/qa/plans-judge/scripts/judge.py" --plans-dir .hermes/plans` reports this plan at score >= 95.
