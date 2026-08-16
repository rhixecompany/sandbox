# Concurrent Pre-Read Optimization

## Problem

Phase 3 dispatches subagents for web research. While they run (often 2-5 minutes
of wall time), the main thread is idle. This time can be productively used to
assess the current state of all existing reports — revealing edits needed before
the subagents return.

## Pattern

1. **Dispatch** Phase 3 subagents via `delegate_task(tasks=[...])`
2. **Immediately read** all existing `RESEARCH_REPORT.md` files (batch-read in
   parallel via `read_file`)
3. **For each report** assess:
   - Section count (`>= 9`?)
   - Size gate (`1KB-5KB`?)
   - Cross-reference completeness and symmetry
   - URL freshness (key links likely stale?)
4. **Note** which reports need: trimming, expanding, cross-ref updates, or URL
   re-verification
5. **When subagents return**, merge their findings directly into the
   pre-assessed gaps — don't run a fresh audit from scratch

## Benefits

- **Phase 4 (verification)** becomes a re-check of known issues instead of
  first-time discovery
- **Phase 2 (report writing)** runs faster because gaps are already identified
- **Catches propagated issues** early (deleted reports, asymmetric cross-refs,
  size violations) before any new content is written
- **Reduces round-trips** — the subagent result message and the pre-read data
  combine into a single Phase 2 execution plan

## Taxonomy of Pre-Read Findings

| Finding | Action |
|---------|--------|
| Report > 5KB | Flag for trimming during Phase 2 merge |
| Report missing a Related Projects reference | Add during Phase 5 cross-ref pass |
| Report has < 9 `##` sections | Expand during Phase 2 |
| Asymmetric cross-ref (A → B but not B → A) | Fix during Phase 5 |
| Key external URL likely stale | Re-verify via `web_extract` in Phase 2 |
| Report missing entirely (deleted between sessions) | Escalate to CREATE target |

## Example Output

```
14 reports found on disk
5 of 14 exceed 5KB cap — flag for trimming
All 14 have ≥9 sections ✓
Cross-references appear symmetric in both directions
No missing reports — all 14 accounted for
```

## When to Skip

- **Single-project research** — no concurrent work to overlap
- **CREATE-only pipeline** — no existing reports to pre-read
- **Reports were refreshed in a prior session** — pre-read would be redundant
