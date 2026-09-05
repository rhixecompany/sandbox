# Capability Ranking Template

**Ranking Date**: {{TIMESTAMP}}
**Session**: {{SESSION_ID}}
**Ranker**: {{RANKER}}

## All Probed Models Summary

| Rank | Provider | Model | Working | Vision | Reasoning | Context | Max Output | Latency (ms) | Score Tuple | Include |
|---|---|---|---|---|---|---|---|---|---|---|
| 1 | {{P1}} | {{M1}} | {{W1}} | {{V1}} | {{R1}} | {{C1}} | {{O1}} | {{L1}} | ({{S1}}) | {{I1}} |
| 2 | {{P2}} | {{M2}} | {{W2}} | {{V2}} | {{R2}} | {{C2}} | {{O2}} | {{L2}} | ({{S2}}) | {{I2}} |
| 3 | {{P3}} | {{M3}} | {{W3}} | {{V3}} | {{R3}} | {{C3}} | {{O3}} | {{L3}} | ({{S3}}) | {{I3}} |
| 4 | {{P4}} | {{M4}} | {{W4}} | {{V4}} | {{R4}} | {{C4}} | {{O4}} | {{L4}} | ({{S4}}) | {{I4}} |
| 5 | {{P5}} | {{M5}} | {{W5}} | {{V5}} | {{R5}} | {{C5}} | {{O5}} | {{L5}} | ({{S5}}) | {{I5}} |
| 6 | {{P6}} | {{M6}} | {{W6}} | {{V6}} | {{R6}} | {{C6}} | {{O6}} | {{L6}} | ({{S6}}) | {{I6}} |
| 7 | {{P7}} | {{M7}} | {{W7}} | {{V7}} | {{R7}} | {{C7}} | {{O7}} | {{L7}} | ({{S7}}) | {{I7}} |
| 8 | {{P8}} | {{M8}} | {{W8}} | {{V8}} | {{R8}} | {{C8}} | {{O8}} | {{L8}} | ({{S8}}) | {{I8}} |
| 9 | {{P9}} | {{M9}} | {{W9}} | {{V9}} | {{R9}} | {{C9}} | {{O9}} | {{L9}} | ({{S9}}) | {{I9}} |
| 10 | {{P10}} | {{M10}} | {{W10}} | {{V10}} | {{R10}} | {{C10}} | {{O10}} | {{L10}} | ({{S10}}) | {{I10}} |

## Excluded Models (Non-Working)

| Provider | Model | Error | Reason |
|---|---|---|---|
| {{EX_P1}} | {{EX_M1}} | {{EX_E1}} | {{EX_R1}} |
| {{EX_P2}} | {{EX_M2}} | {{EX_E2}} | {{EX_R2}} |
| {{EX_P3}} | {{EX_M3}} | {{EX_E3}} | {{EX_R3}} |

## Ranking Algorithm

```python
def sort_key(m):
    working = 1 if m.working else 0
    vision = 2 if m.vision else 0
    reason = 1 if m.reasoning else 0
    ctx = min(m.ctx, 2_000_000) / 2_000_000
    output = min(m.max_output, 100_000) / 100_000
    latency_penalty = 0 if m.latency_ms < 5000 else (1 if m.latency_ms < 15000 else 2)
    return (working, vision, reason, ctx, output, -latency_penalty)
```

## Selected Fallback Chain

### Primary Model

| Field | Value |
|---|---|
| Provider | {{PRIMARY_PROVIDER}} |
| Model | {{PRIMARY_MODEL}} |
| Score | {{PRIMARY_SCORE}} |

### Fallback Providers (Ordered)

```yaml
fallback_providers:
  - "{{FALLBACK_1_PROVIDER}}"  # default_model: {{FALLBACK_1_MODEL}}
  - "{{FALLBACK_2_PROVIDER}}"  # default_model: {{FALLBACK_2_MODEL}}
  - "{{FALLBACK_3_PROVIDER}}"  # default_model: {{FALLBACK_3_MODEL}}
  - "{{FALLBACK_4_PROVIDER}}"  # default_model: {{FALLBACK_4_MODEL}}
  - "{{FALLBACK_5_PROVIDER}}"  # default_model: {{FALLBACK_5_MODEL}}
```

### Provider Default Models

| Provider | Default Model | Verified Working |
|---|---|---|
| {{FALLBACK_1_PROVIDER}} | {{FALLBACK_1_MODEL}} | Yes |
| {{FALLBACK_2_PROVIDER}} | {{FALLBACK_2_MODEL}} | Yes |
| {{FALLBACK_3_PROVIDER}} | {{FALLBACK_3_MODEL}} | Yes |
| {{FALLBACK_4_PROVIDER}} | {{FALLBACK_4_MODEL}} | Yes |
| {{FALLBACK_5_PROVIDER}} | {{FALLBACK_5_MODEL}} | Yes |

## Tie-Breaker Decisions

| Tie | Models | Decision | Reason |
|---|---|---|---|
| {{TIE_1_MODELS}} | {{TIE_1_DECISION}} | {{TIE_1_REASON}} |
| {{TIE_2_MODELS}} | {{TIE_2_DECISION}} | {{TIE_2_REASON}} |

## Vision Gap Analysis

- **Models with vision**: {{VISION_MODELS_COUNT}}
- **Top vision model**: {{TOP_VISION_MODEL}}
- **Fallback if no vision**: {{NO_VISION_FALLBACK}}

## Notes

{{RANKING_NOTES}}

---

*Fill in during Phase 4 execution. Save as `ranking/capability-ranking-{{TIMESTAMP}}.md`*