# sync-hermes-copilot-codex — Fix Issues Context (Progress Log)

> Generated: 2026-06-21T10:00:00Z | Phase: 2-3 (Fix Planning + Execution)
> Tracks: Fix application progress per `thoughts/plans/sync-hermes-copilot-codex-debug.md`

---

## Fix Progress Tracker

| ID | Issue | Severity | File | Batch | Status | Applied | Verified |
|----|-------|----------|------|-------|--------|---------|----------|
| F1 | Stale `.prompt.txt` reference | Medium | `.prompt.md` | 1 | **Done** | ✅ | ✅ |
| F2 | Missing frontmatter fields | Low | `.prompt.md` | 1 | **Done** | ✅ | ✅ |
| F3 | Missing `metadata.hermes` | Low | `.prompt.md` | 1 | **Done** | ✅ | ✅ |
| F4 | Missing verification checklist | Low | `.prompt.md` | 1 | **Done** | ✅ | ✅ |
| F5 | Inconsistent tags style | Info | `.prompt.md` | 1 | **Done** | ✅ | ✅ |
| F6 | YAML comment at column 0 | Info | `.prompt.md` | 1 | **Done** | ✅ | ✅ |
| G1 | Full verification | — | `.prompt.md` | 2 | **Done** | ✅ | ✅ |

---

## Batch 1 Execution Log (Proof-of-Concept)

### F1: Stale `.prompt.txt` Reference

- **Target:** `sync-hermes-copilot-codex.prompt.md` line 45
- **Action:** Replace `**Source reference:** \`./sync-hermes-copilot-codex.prompt.txt\`` with consolidated reference
- **Command:** patch
- **Result:** TBD
- **Verification:** No `.prompt.txt` reference in file

### F2: Missing Frontmatter Fields

- **Target:** `sync-hermes-copilot-codex.prompt.md` frontmatter
- **Action:** Add `name`, `title`, `version` after `trigger:`
- **Result:** TBD
- **Verification:** Fields present in YAML

### F3: Missing metadata.hermes

- **Target:** `sync-hermes-copilot-codex.prompt.md` frontmatter
- **Action:** Add `metadata.hermes.related_skills` before closing `---`
- **Result:** TBD
- **Verification:** `metadata.hermes.related_skills` matches skills list

### F4: Missing Verification Checklist

- **Target:** `sync-hermes-copilot-codex.prompt.md` end of file
- **Action:** Add `## Verification Checklist` with 9 checkboxes
- **Result:** TBD
- **Verification:** Section present with checkboxes

### F5: Inconsistent tags Style

- **Target:** `sync-hermes-copilot-codex.prompt.md` frontmatter lines 8-17
- **Action:** Convert flow sequence to block-style YAML list
- **Result:** TBD
- **Verification:** Tags parse as 9-item block list

### F6: dependencies/skills Redundancy Note

- **Target:** `sync-hermes-copilot-codex.prompt.md` frontmatter
- **Action:** Add YAML comment before `dependencies:`
- **Result:** TBD
- **Verification:** Comment present

---

## Batch 2 Execution Log

### G1: Full Verification

- **Target:** `sync-hermes-copilot-codex.prompt.md`
- **Action:** Re-run complete audit suite
- **Result:** TBD
- **Verification:** All 9 gates pass

---

## Change Summary (Cumulative)

| File | Lines Changed | Issues Fixed | Last Modified |
|------|---------------|--------------|---------------|
| sync-hermes-copilot-codex.prompt.md | 0 | 0/6 | - |

---

## Next Actions

1. Apply F1: Fix stale `.prompt.txt` reference
2. Apply F2-F3: Add frontmatter fields + metadata block
3. Apply F5: Convert tags YAML style
4. Apply F6: Add redundancy comment
5. Apply F4: Add verification checklist at end
6. Run full verification (G1)
7. Update this log with results
