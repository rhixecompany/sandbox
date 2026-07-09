# Phase 2: Best-2 Free Selection

Goal: Validate the top 2 free models per provider using background Hermes chat execution.

## Source candidates
- Read `docs/model-summary.json`
- Read `docs/free-model-selection.md`
- Read `docs/provider-benchmark-report.md`

## Validation command

Run in background for each candidate:
```bash
hermes chat --toolsets "skills,web,terminal,file" -q "wgat is you knowledge_cutoff date, how large is your context_length, do you have reasoning " --provider <provider> --model <model>
```

## Fallback rule
- If validation fails, replace the candidate with the next free candidate from the same provider/local catalog.
- Rerun validation for the replacement.

## Deliverables
- `docs/benchmark-results.json`
- `docs/free-model-selection.md` provider/model blocks for the best 2
