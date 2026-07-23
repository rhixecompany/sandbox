# Phases

> Extracted from `performance.prompt.md`.

## Phases

### Phase 1: Baseline and Bottleneck Discovery

| Field | Details |
| --- | --- |
| Goal | Identify current performance characteristics and dominant bottlenecks. |
| Inputs | Metrics, traces, logs, query stats, bundle data, user reports. |
| Outputs | Ranked bottleneck list with measurable baseline. |
| Validation | Bottlenecks are supported by observable data rather than assumptions. |

### Phase 2: Targeted Optimization

| Field | Details |
| --- | --- |
| Goal | Apply minimal, high-impact optimizations to top bottlenecks. |
| Inputs | Bottleneck ranking, architecture constraints, risk limits. |
| Outputs | Focused optimization changes and expected impact notes. |
| Validation | Changes directly address measured bottlenecks and preserve behavior. |

### Phase 3: Re-measurement and Regression Check

| Field | Details |
| --- | --- |
| Goal | Confirm improvements and ensure no behavioral regressions. |
| Inputs | Updated metrics and test results. |
| Outputs | Before/after comparison with residual risk callouts. |
| Validation | Performance delta is demonstrable and functional behavior remains correct. |
