---
goal: Refactor provider probes to use the self-profile prompt and skip rate-limited providers
version: 1.0
date_created: 2026-09-14
last_updated: 2026-09-14T16:15:19Z
owner: Alexa
status: Completed
tags: [refactor, providers, rate-limits, documentation]
---

# Introduction

![Status: Completed](https://img.shields.io/badge/status-Completed-brightgreen)

Replace the stale provider capability probe with the exact self-profile prompt supplied by the user and make every operational probe skip providers whose auth inventory reports rate-limit errors.

## 1. Requirements & Constraints

- **REQ-001**: Use the exact prompt `hello whoami, who are u, what is ur providers,performance,uptime,apps,Modalities,Price,Context,Released` for provider/model probes.
- **REQ-002**: Skip an entire provider when `hermes auth list` reports a rate-limit marker, including `rate-limited` or HTTP/status `429`.
- **REQ-003**: Do not invoke, retry, rank, or select skipped providers during the current probe run; record an explicit skipped status where operational output supports it.
- **REQ-004**: Preserve historical probe transcripts, captured result artifacts, and unrelated working-tree changes.
- **REQ-005**: Document the skip rule and fallback behavior in the requested fallback-provider and CLI guides.
- **CON-001**: Do not read or modify `.env` or credentials.
- **CON-002**: Keep Python scripts compatible with the repository's supported Python versions and existing command-line entry points.
- **PAT-001**: Centralize rate-limit parsing and the canonical prompt to avoid drift between scripts.

## 2. Implementation Steps

### Implementation Phase 1 — Shared operational behavior

- **GOAL-001**: Add shared prompt and auth-status helpers.

| Task | Description | Completed | Date |
|------|-------------|-----------|------|
| TASK-001 | Add a shared Python helper containing the exact probe prompt and parser for rate-limited providers from `hermes auth list`. | ✅ | 2026-09-14 |
| TASK-002 | Refactor `test-providers-probe.py`, `run_probes.py`, and `test-model.py` to use the helper, preflight provider status, and emit explicit skipped results without invoking rate-limited providers. | ✅ | 2026-09-14 |
| TASK-003 | Update the canonical workflow prompt and phase/template instructions to require the self-profile prompt and rate-limit skip gate. | ✅ | 2026-09-14 |

### Implementation Phase 2 — Documentation

- **GOAL-002**: Align fallback and CLI documentation with the operational rule.

| Task | Description | Completed | Date |
|------|-------------|-----------|------|
| TASK-004 | Document rate-limit preflight, provider-level skip semantics, and the distinction between probe-time filtering and live fallback in `fallback-providers.md`. | ✅ | 2026-09-14 |
| TASK-005 | Document the self-profile probe command and rate-limit skip checklist in `cli.md`. | ✅ | 2026-09-14 |

### Implementation Phase 3 — Verification

- **GOAL-003**: Verify behavior and scope.

| Task | Description | Completed | Date |
|------|-------------|-----------|------|
| TASK-006 | Compile changed Python scripts and run focused helper tests with representative valid, rate-limited, and mixed auth-list fixtures. | ✅ | 2026-09-14 |
| TASK-007 | Check the diff, confirm the exact prompt appears in operational sources, confirm no probe command is created for rate-limited providers, validate Markdown structure, and confirm unrelated changes remain untouched. | ✅ | 2026-09-14 |

## 3. Alternatives

- **ALT-001**: Add only prose instructions to the prompt. Rejected because scripts would still invoke rate-limited providers.
- **ALT-002**: Filter only individual credentials. Rejected because the requirement is provider-level skipping and provider credentials can share a rate limit.
- **ALT-003**: Rewrite historical probe artifacts. Rejected because captured evidence must remain immutable and historical failures must not be rewritten.

## 4. Dependencies

- **DEP-001**: `hermes auth list` output is the live source for provider credential/rate-limit status.
- **DEP-002**: Python standard library only for the new helper; no dependency changes.
- **DEP-003**: Existing `fallback_providers` runtime behavior and docs remain the source of truth for live session failover.

## 5. Files

- **FILE-001**: `.github/prompts/operations/test-providers-models/scripts/provider_status.py` — new shared prompt/status helper.
- **FILE-002**: `.github/prompts/operations/test-providers-models/scripts/test-providers-probe.py` — prompt and preflight skip.
- **FILE-003**: `.github/prompts/operations/test-providers-models/scripts/run_probes.py` — prompt and provider skip.
- **FILE-004**: `.github/prompts/operations/test-providers-models/scripts/test-model.py` — prompt and provider skip.
- **FILE-005**: `.github/prompts/operations/test-providers-models/test-providers-models.prompt.md` — workflow requirements.
- **FILE-006**: `.github/prompts/operations/test-providers-models/templates/phase_0_auth_inventory.md` — inventory gate.
- **FILE-007**: `.github/prompts/operations/test-providers-models/templates/phase_2_free_extraction.md` — eligibility rule.
- **FILE-008**: `.github/prompts/operations/test-providers-models/templates/phase_3_provider_benchmark.md` — exact probe prompt and skip behavior.
- **FILE-009**: `.github/prompts/operations/test-providers-models/templates/phase_4_comparison_report.md` — exclude skipped providers from ranking.
- **FILE-010**: `.github/prompts/operations/test-providers-models/templates/phase_5_fallback_chain.md` — exclude rate-limited entries.
- **FILE-011**: `.github/prompts/operations/test-providers-models/templates/test-provider-model.md` — self-profile test contract.
- **FILE-012**: `.github/prompts/operations/test-providers-models/templates/multi-task-model-tests.md` — probe eligibility wording.
- **FILE-013**: `docs/hermes/user-guide/features/fallback-providers.md` — user-facing skip/fallback documentation.
- **FILE-014**: `docs/hermes/user-guide/cli.md` — CLI probe and skip documentation.
- **FILE-015**: `.github/prompts/operations/test-providers-models/scripts/apply_config.py` — exclude rate-limited/skipped providers from ranking and configuration.
- **FILE-016**: `.github/prompts/operations/test-providers-models/templates/probe-live-template.md` — document the updated probe result columns and skip status.

## 6. Testing

- **TEST-001**: `python -m py_compile` for all changed Python scripts.
- **TEST-002**: Direct parser assertions for rate-limited, HTTP 429, valid, and mixed-provider auth output.
- **TEST-003**: Dry operational preflight showing rate-limited providers become skipped without invoking `hermes chat`.
- **TEST-004**: Search/diff checks confirming the exact prompt and explicit skip status are present.
- **TEST-005**: Markdown heading/code-fence sanity checks for the two requested docs and changed templates.

## 7. Risks & Assumptions

- **RISK-001**: Provider status text may vary between Hermes versions; use case-insensitive markers for `rate-limited` and `429`, while avoiding unrelated 402/403 classifications.
- **RISK-002**: Parallel probe execution can already have started before a runtime 429 is observed; preflight filtering is the primary guarantee, and runtime failures are recorded as skipped for subsequent selection.
- **ASSUMPTION-001**: Historical generated artifacts under `probes/`, `plans/`, `provider_docs/`, and result files are evidence, not operational source files, and should not be rewritten.

## 8. Related Specifications / Further Reading

- `docs/hermes/user-guide/features/fallback-providers.md`
- `docs/hermes/user-guide/cli.md`
- `test-providers-models.prompt.md`

## 9. Verification Evidence

- `C:/Users/Alexa/myvenv/Scripts/python.exe -m py_compile` — exit `0` for all six changed Python scripts.
- `C:/Users/Alexa/myvenv/Scripts/ruff.exe check` — `All checks passed!` for all six changed Python scripts.
- Focused helper/preflight test — `FOCUSED_RATE_LIMIT_TESTS_PASS`; fixture parser identified `openai-codex` and `openrouter`, runtime `429` stopped the provider group, and preflight skipped `openrouter` without calling `run_one`.
- Prompt/document/Markdown structure check — `PROMPT_DOC_STRUCTURE_CHECK_PASS`; 32 operational sources and 24 Markdown files checked; historical probe/result artifacts were excluded by design.
- Live read-only auth preflight — exit `0`; provider set was reported without exposing credentials.
- `git diff HEAD --check` — exit `0` (Git emitted only existing CRLF-normalization warnings).
- No live model probes or configuration writes were executed; the no-invocation guarantee was verified with mocked subprocess/preflight paths.
- Fresh scoped re-verification: Ruff lint, Ruff format check, Python compilation, and `git diff --check` all exited `0` after formatting the six changed scripts.
- Fresh focused behavior harness: `FOCUSED_RATE_LIMIT_TESTS_PASS`; exact prompt consistency, provider preflight skipping, runtime 429 stop-after-first-model, direct-runner zero invocation for skipped providers, ranking exclusion, and ten prompt/doc Markdown sources passed.
