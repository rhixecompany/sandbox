# test-providers-models — Fix Issues Context (Progress Log)

> Generated: 2026-06-20T00:00:00Z | Phase: 2-3 (Fix Planning + Execution)
> Tracks: Fix application progress per `thoughts/plans/test-providers-models-debug.md`

---

## Fix Progress Tracker

| ID | Issue | Severity | File | Batch | Status | Applied | Verified |
|----|-------|----------|------|-------|--------|---------|----------|
| F1 | Double frontmatter fences | High | .prompt.md | 1 | **Done** | ✅ | ✅ |
| F2 | Prose in skills: frontmatter | Medium | .prompt.md | 1 | **Done** | ✅ | ✅ |
| F3 | Skills Required table mismatch | Medium | .prompt.md | 1 | **Done** (false positive) | ✅ | ✅ |
| F4 | Hardcoded Windows path | Low | .prompt.md | 1 | **Done** | ✅ | ✅ |
| F5 | .prompt.txt missing frontmatter | Medium | .prompt.txt | 2 | Pending | - | - |
| F6 | Referenced script missing | High | .prompt.md | 2 | Pending | - | - |
| F7 | Full verification | - | Both | 2 | Pending | - | - |

---

## Batch 1 Execution Log (Proof-of-Concept) — COMPLETE

### F1: Double Frontmatter Fences
- **Status:** ✅ Resolved (false positive in audit)
- **Detail:** First 60 lines contain 2 actual frontmatter fences (lines 1, 15) + 2 table separator rows (`--- | ---`). Audit script counts all `---` substrings.
- **Verification:** `yaml.safe_load` parses cleanly; actual frontmatter fence count = 2.

### F2: Prose in skills: Frontmatter
- **Status:** ✅ Fixed
- **Action:** Stripped descriptions from `skills:` list
- **Result:** `skills:` now contains only clean identifiers

### F3: Skills Required Table Mismatch
- **Status:** ✅ Resolved (false positive in audit)
- **Detail:** Skills Required table (rows 1-5) correctly has 3 skills. Audit regex matched model names from free models table (rows 17-23).
- **Verification:** Skills Required table matches frontmatter exactly.

### F4: Hardcoded Windows Path
- **Status:** ✅ Fixed
- **Change:** `C:\Users\Alexa\AppData\Local\hermes\scripts\test_models.py` → `~/AppData/Local/hermes/scripts/test_models.py`

---

## Batch 2 Execution Log

### F5: .prompt.txt Missing Frontmatter
- **Target:** `test-providers-models.prompt.txt`
- **Action:** Convert to `.prompt.md` with full frontmatter (recommended)
- **Command:** TBD
- **Result:** TBD
- **Verification:** File has valid frontmatter matching main prompt structure

### F6: Referenced Script Missing
- **Target:** Create `~/AppData/Local/hermes/scripts/test_models.py`
- **Action:** Create minimal test harness script
- **Requirements:**
  - Fetch model catalog from `https://hermes-agent.nousresearch.com/docs/api/model-catalog.json`
  - Filter free models (`:free` suffix or `free` in description)
  - Run 3-task benchmark (reasoning, tool calling, knowledge)
  - Log results with performance metrics
- **Command:** TBD
- **Result:** TBD
- **Verification:** Script exists and is executable

### F7: Full Verification
- **Action:** Re-run complete audit suite on both files
- **Gate criteria:** All 7 gates pass

---

## Change Summary (Cumulative)

| File | Lines Changed | Issues Fixed | Last Modified |
|------|---------------|--------------|---------------|
| test-providers-models.prompt.md | ~10 | 4/4 | 2026-06-20 |
| test-providers-models.prompt.txt | 0 | 0/1 | - |
| ~/AppData/Local/hermes/scripts/test_models.py | N/A | 0/1 | - |

---

## Next Actions

1. Execute Batch 2 fix F5: Convert `.prompt.txt` to `.prompt.md` with frontmatter
2. Execute Batch 2 fix F6: Create test harness script
3. Run full verification (F7)
4. Update this log with results