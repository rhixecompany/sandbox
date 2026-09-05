# Model Probe Template

**Provider**: {{PROVIDER}}
**Model**: {{MODEL}}
**Probe Date**: {{TIMESTAMP}}
**Probe Session**: {{SESSION_ID}}
**Probe Method**: {{PROBE_METHOD}}

## Probe Command

```bash
{{PROBE_COMMAND}}
```

## Raw Response

```
{{RAW_RESPONSE}}
```

## Parsed Capabilities

| Capability | Value | Source |
|---|---|---|
| Working | {{WORKING}} | probe |
| Vision | {{VISION}} | {{VISION_SOURCE}} |
| Reasoning | {{REASONING}} | {{REASONING_SOURCE}} |
| Context Window (tokens) | {{CONTEXT_WINDOW}} | {{CTX_SOURCE}} |
| Max Output (tokens) | {{MAX_OUTPUT}} | {{OUTPUT_SOURCE}} |
| Latency (ms) | {{LATENCY_MS}} | probe |
| Error | {{ERROR}} | probe |

## Detailed Analysis

### Vision Test
- **Test Method**: {{VISION_TEST_METHOD}}
- **Result**: {{VISION_RESULT}}
- **Notes**: {{VISION_NOTES}}

### Reasoning Test
- **Test Method**: {{REASONING_TEST_METHOD}}
- **Result**: {{REASONING_RESULT}}
- **Notes**: {{REASONING_NOTES}}

### Context Window Verification
- **Claimed (docs)**: {{CLAIMED_CTX}}
- **Verified (probe)**: {{VERIFIED_CTX}}
- **Method**: {{CTX_VERIFY_METHOD}}

## Probe Metadata

| Field | Value |
|---|---|
| Probe Duration (ms) | {{PROBE_DURATION_MS}} |
| HTTP Status | {{HTTP_STATUS}} |
| Response Tokens | {{RESPONSE_TOKENS}} |
| Prompt Tokens | {{PROMPT_TOKENS}} |
| Rate Limited | {{RATE_LIMITED}} |
| Auth Error | {{AUTH_ERROR}} |

## Ranking Score Calculation

```python
working = {{WORKING_INT}}
vision = {{VISION_INT}}
reasoning = {{REASONING_INT}}
ctx = min({{CONTEXT_WINDOW}}, 2_000_000) / 2_000_000
output = min({{MAX_OUTPUT}}, 100_000) / 100_000
latency_penalty = {{LATENCY_PENALTY}}

score = (working, vision, reasoning, ctx, output, -latency_penalty)
# = ({{WORKING_INT}}, {{VISION_INT}}, {{REASONING_INT}}, {{CTX_NORMALIZED}}, {{OUTPUT_NORMALIZED}}, {{NEG_LATENCY_PENALTY}})
```

## Verdict

- **Include in fallback chain**: {{INCLUDE_IN_CHAIN}}
- **Rank position**: {{RANK_POSITION}}
- **Notes**: {{VERDICT_NOTES}}

---

*Fill in during Phase 3 execution. Save as `probes/{{PROVIDER}}-{{MODEL_SLUG}}-probe.md`*