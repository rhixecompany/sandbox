# Phase 3: Provider-by-Provider Benchmarking

> Template for `test-providers-models`. Live capability probes delegated to subagents.

## Inputs

- Free model list from Phase 2
- Probe method: `hermes chat --provider <provider> --model <model> -q "hello whoami, who are u, what is ur providers,performance,uptime,apps,Modalities,Price,Context,Released" --oneshot`
- Eligibility: only providers that passed the Phase 0 rate-limit preflight.

## Probe Method (delegate to subagents A, B, C as per prompt context block)

```bash
hermes chat --provider opencode-zen --model deepseek-v4-flash-free \
  -q "hello whoami, who are u, what is ur providers,performance,uptime,apps,Modalities,Price,Context,Released" \
  --oneshot
```

## Return Format

```
provider | model | status=<success|failed|skipped> | skip_reason=<reason> | response=<verbatim>
```

## Verification Gate

- [ ] At least 3 subagent clusters dispatched (A, B, C)
- [ ] Each working model has vision/reasoning/context documented
- [ ] Rate-limited providers are skipped at provider scope; no remaining model for that provider is invoked
- [ ] Skipped rows report `status=skipped`, `skip_reason=provider_rate_limited`, and no fabricated response
