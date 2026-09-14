# Free-Model Latency Benchmark

> Generated: 2026-09-11 | Query: `Respond with current UTC time and 'PONG'` | Timeout: 120s | Models tested: 9

## Summary

| Metric | Value |
|---|---|
| Total runs | 9 |
| Successful | 7 |
| Failed (timeout) | 2 |
| Success rate | 78% |
| Avg latency (successful) | 68.70s |
| Min latency | 57.18s |
| Max latency | 93.63s |

## Results Table

| Provider | Model | Status | Latency (s) | Session ID |
|---|---|---|---|---|
| `openrouter` | `nvidia/nemotron-3-ultra-550b-a55b:free` | timeout | 120.07 | `` |
| `openrouter` | `thinkingmachines/inkling:free` | success | 70.45 | `20260911_045235_0cdb78` |
| `openrouter` | `deepseek/deepseek-v4-flash-0731` | success | 57.18 | `20260911_045345_b434a8` |
| `openrouter` | `nvidia/nemotron-3.5-lightning:free` | timeout | 120.03 | `` |
| `openrouter` | `google/gemma-4-31b-it:free` | success | 64.63 | `(exit 0)` |
| `nous` | `meituan/longcat-2.0:free` | success | 63.99 | `(exit 0)` |
| `opencode-zen` | `minimax/minimax-m3` | success | 93.63 | `(exit 0)` |
| `nous` | `upstage/solar-pro4:free` | success | 59.29 | `(exit 0)` |
| `openrouter` | `stepfun/step-3.7-flash:free` | success | 71.71 | `(exit 0)` |

## Ranked by Latency (Successful Only)

| Rank | Model | Latency (s) |
|---|---|---|
| 1 | `openrouter/deepseek/deepseek-v4-flash-0731` | 57.18 |
| 2 | `nous/upstage/solar-pro4:free` | 59.29 |
| 3 | `nous/meituan/longcat-2.0:free` | 63.99 |
| 4 | `openrouter/google/gemma-4-31b-it:free` | 64.63 |
| 5 | `openrouter/thinkingmachines/inkling:free` | 70.45 |
| 6 | `openrouter/stepfun/step-3.7-flash:free` | 71.71 |
| 7 | `opencode-zen/minimax/minimax-m3` | 93.63 |

## Recommendations for Free-Model Aux-Tasks

- **Fastest free model**: `openrouter/deepseek/deepseek-v4-flash-0731` (57.18s)
- **Recommended for aux-tasks**: route via `provider: openrouter`, model `deepseek/deepseek-v4-flash-0731`
- **Avoid for time-sensitive work**: nemotron models (2/2 timeouts in this benchmark)

## Providers Tested

| Provider | Free Models Available | Tested |
|---|---|---|
| openrouter | 19 | 6 |
| nous | 7 | 2 |
| opencode-zen | (pool-gated, 2 keys) | 1 |

## Verification

- Each successful run produced a real session (4 messages, 2-4 tool calls)
- Latency measured via `time.monotonic()` subprocess wrapper
- Status verified from `hermes chat` exit code + stdout length
