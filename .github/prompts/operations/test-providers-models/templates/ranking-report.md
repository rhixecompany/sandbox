---
name: ranking-report
description: Final ranking of probed free models by score (1-5) plus knowledge cutoff, context length, reasoning flag, max output, latency, and exit code.
variables:
  generated_at: "ISO timestamp the ranking was written"
  primary: "the model chosen as hermes config set model.default"
---

# Free-model ranking — {{ generated_at }}

> Primary model after this run: `{{ primary }}`
> Source: probe results from `probes/probe-*.txt` and `templates/probe-live-template.md`.

| Rank | Score | Provider | Model ID | Knowledge cutoff | Context length | Reasoning | Max output | Latency (s) | Exit |
|------|-------|----------|----------|------------------|----------------|-----------|------------|-------------|------|
| 1 |  |  |  |  |  |  |  |  |  |
| 2 |  |  |  |  |  |  |  |  |  |
| 3 |  |  |  |  |  |  |  |  |  |
| 4 |  |  |  |  |  |  |  |  |  |
| 5 |  |  |  |  |  |  |  |  |  |

## Score formula

`score = (1 if knowledge_cutoff >= 2024-01) + (1 if context_length >= 32000) + (1 if reasoning == yes) + (1 if max_output >= 4096) + (1 if exit == 0)`. Max = 5. Tiebreak by lowest latency.

## Configuration applied

```bash
hermes config set model.default <top1.provider>:<top1.model>
hermes config set model.provider <top1.provider>
hermes fallback clear
hermes fallback add <top2.provider>:<top2.model>
hermes fallback add <top3.provider>:<top3.model>
hermes fallback add <top4.provider>:<top4.model>
hermes fallback add <top5.provider>:<top5.model>
```

## Verification

- [ ] `hermes config show | grep -E 'model|fallback'` matches the table above.
- [ ] `hermes config check` exits 0.
- [ ] `hermes chat --provider <top1.provider> --model <top1.model> -q "ping" --oneshot` exits 0.
