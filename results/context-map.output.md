# Context Map: `audit_prompts.py` — Prompt File Audit Script

**Generated:** 2026-07-09
**Target:** `.github/scripts/audit_prompts.py`
**Task:** Productionize / extend the prompt file audit pipeline

---

## Context Map

| File | Role | Notes |
|------|------|-------|
| `.github/scripts/audit_prompts.py` | **modify** | The primary audit script. Scans `Prompts/` and `.github/prompts/` for frontmatter, formatting, structural, and content issues. Writes JSON results to `docs/audit_results.json`. |
| `Prompts/templates/_shared/rules-core.md` | **dependency** | Referenced as a shared rule template by prompt files — not directly imported, but its conventions shape the frontmatter fields the audit checks. |
| `docs/audit_results.json` | **dependency (output)** | Output artifact consumed by downstream phases (e.g., `batch_remediate.py`). Changing the output schema breaks the pipeline. |
| `docs/01-MCP_BEST_PRACTICES_GUIDE.md` | **dependency** | Doc convention being audited; the script's extension checks (`*.prompt.md`) are informed by the naming conventions described here. |
| `.github/scripts/batch_remediate.py` | **dependency** | Direct consumer of `audit_results.json` — performs batch fixes based on audit results. Schema coupling. |
| `.github/scripts/batch_skill_judge.py` | **reference pattern** | Same architectural pattern: Phase-1 scan followed by Phase-2 remediation. Mirror its `SANDBOX` path setup, event-loop structure, and JSON-report format. |
| `.github/scripts/skills-audit.py` | **reference pattern** | Same pattern: walks a directory of markdown files, checks frontmatter validity, writes issues. Uses `os.walk` + regex; uses `USERPROFILE` env var instead of hardcoded path — pattern to adopt. |
| `.github/scripts/fix_prompts.py` | **reference pattern** | Fixes issues the audit finds — paired by convention. Same repo root handling, same CLI pattern. |
| `Prompts/templates/` | **dependency** | Template prompts that should also pass the audit — not currently scanned (gap). |
| *(No dedicated test files found)* | **test** | **No related tests identified** — no `test_audit_prompts.py`, no `tests/` directory, no pytest fixtures, and no CI step that validates the audit script's output. |

---

## Risk Assessment

1. **⚠️ No tests exist for `audit_prompts.py`.** The script has no unit or integration tests. Any change risks silent regressions in the audit's output format (which is consumed by `batch_remediate.py`).
2. **🔴 Hardcoded paths.** `SANDBOX = Path("C:/Users/Alexa/Desktop/SandBox")` prevents the script from running on other machines or in CI. Compare with `skills-audit.py` which uses `USERPROFILE`.
3. **🟡 Tight coupling to output schema.** `docs/audit_results.json` is consumed by `batch_remediate.py`. Changing field names, nesting, or severity levels in the audit breaks the remediator without any compilation-time check.
4. **🟡 `.github/prompts/` is empty.** The script scans this directory but it contains zero files — the loop still runs but is a no-op. Risk of dead code if this directory is never populated.
5. **🟢 Template directory not scanned.** `Prompts/templates/` contains `.md` files with frontmatter that are not audited — structural blind spot for template quality.

---

## Phase 1 — Scope Summary

- **Files to modify:** 1 primary (`.github/scripts/audit_prompts.py`)
- **Direct dependencies consumed:** 3 JSON/directory targets
- **Downstream consumers:** 1 (`.github/scripts/batch_remediate.py`)
- **Reference patterns:** 2 sibling scripts (`.github/scripts/batch_skill_judge.py`, `.github/scripts/skills-audit.py`)
- **Tests:** 0 identified

**Stop: review this map before proceeding to implementation.**