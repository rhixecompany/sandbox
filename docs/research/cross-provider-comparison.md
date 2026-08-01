# Cross-Provider Comparison & Fallback Chain (2026-07-27)

## Comparison: Free Tier Capabilities

| Criteria            | OpenRouter            | Google AI Studio | Hugging Face          | Copilot Free | OpenAI API       |
| ------------------- | --------------------- | ---------------- | --------------------- | ------------ | ---------------- |
| **Free Models**     | 18                    | 3+               | 100s                  | 1-2          | 0 (credits only) |
| **Max Context**     | 1M                    | 1M+              | 1M+                   | 128K         | 128K-1M          |
| **Rate Limits**     | ~20 RPM               | High (web)       | ~30 RPM               | 50/mo        | Tier-based       |
| **Coding**          | Qwen3-Coder, Poolside | Gemini 2.5 Flash | Many (Kimi, DeepSeek) | GPT-4o       | GPT-4o           |
| **Reasoning**       | Nemotron Ultra        | Flash thinking   | GLM, Qwen             | o1-preview   | o1/o3            |
| **Multimodal**      | Gemma 4, GPT-OSS      | Native           | Some                  | GPT-4o       | Native           |
| **Tools/Functions** | Most models           | Yes              | Varies                | Yes          | Full             |
| **Reproducibility** | Low (router)          | High             | Medium                | High         | High             |
| **No CC Required**  | ✅                    | ✅               | ✅                    | ✅           | ❌               |

## Recommended Fallback Chain (Production)

### Primary: OpenRouter (openrouter/free or explicit models)

```
1. qwen/qwen3-coder:free          → coding, 1M context
2. nvidia/nemotron-3-ultra-550b:free → reasoning, 1M context
3. nvidia/nemotron-3-super-120b:free  → multi-agent, 1M context
4. google/gemma-4-31b-it:free        → multimodal, 262K
5. poolside/laguna-m.1:free           → coding, 262K
```

### Secondary: Google AI Studio (via browser)

- Direct web access, higher limits
- Use for: long context, multimodal, when OpenRouter rate limited

### Tertiary: Hugging Face Inference Providers

```
1. Kimi-K2.7-Code (together/novita)   → coding, 262K
2. GLM-5.2 (together/fireworks)       → reasoning, 262K-1M
3. DeepSeek-V4-Pro (fireworks)        → reasoning, 1M
```

- Choose provider by lowest latency/price on HF Inference Providers page

### Quaternary: GitHub Copilot Free

- 50 chat requests/month, 2000 completions
- Use for: quick GitHub-integrated tasks
- Models: GPT-4o, o1-preview

## Automation Scripts Needed

### 1. Provider Health Check

```python
# Check each provider's /models endpoint or /chat/completions with 1 token
# Return: healthy, rate_limited, auth_failed, timeout
```

### 2. Model Availability Probe

```python
# For each free model on OpenRouter, send test request
# Track: success rate, latency, token throughput
```

### 3. Fallback Executor

```python
# Try providers in order until success
# Log which provider/model succeeded
# Cache successful route for session
```

### 4. Context Window Selector

```python
# Given input size, select model with sufficient context
# Prefer largest context among healthy models
```

## Integration Points

- `test-providers-models` skill scripts → update with findings
- `hermes auth list` → source of truth for credentials
- `config.yaml` → fallback chain configuration
- MCP servers (openrouter, huggingface) → direct access

## Verification Checklist

- [ ] OpenRouter free models responding (<5s latency)
- [ ] Google AI Studio accessible in browser
- [ ] Hugging Face inference providers responding
- [ ] Copilot CLI functional (tested earlier)
- [ ] Fallback chain script runs without auth errors
- [ ] Comparison report saved to docs/research/

## Next Actions

1. Create health check script
2. Create fallback executor
3. Run benchmark on top 5 free models
4. Document results in orchestrator-verification.md

EOF
cat docs/research/cross-provider-comparison.md
