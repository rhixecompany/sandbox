# Phase 3: Provider-by-Provider Benchmarking

> Template for `test-providers-models`. Live capability probes delegated to subagents.

## Inputs

- Free model list from Phase 2
- Probe method: `hermes chat --provider <provider> --model <model> -q ...`

## Probe Method (delegate to subagents A, B, C as per prompt context block)

```bash
hermes chat --provider opencode-zen --model deepseek-v4-flash-free \
  -q "reply with only: vision=<yes|no> reasoning=<yes|no> ctx=<tokens>"
```

## Return Format

```
provider | model | working=<bool> | vision=<bool> | reasoning=<bool> | ctx=<int>
```

## Verification Gate

- [ ] At least 3 subagent clusters dispatched (A, B, C)
- [ ] Each working model has vision/reasoning/context documented
- [ ] Rate-limited providers report `working=false` with error (not fabricated)
