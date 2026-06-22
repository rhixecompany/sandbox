# Knowledge Base

> Extracted from `model-recommendation.prompt.md` for DRY templating.

## Knowledge Base

### Model Multiplier Cost Reference

| Multiplier | Meaning | Free Tier | Pro Usage | Pro+ Usage |
| --- | --- | --- | --- | --- |
| 0x | Included in all plans, no premium count | ✅ | Unlimited | Unlimited |
| 0.25x | 4 requests = 1 premium request | ❌ | 4000 uses | 20000 uses |
| 0.33x | 3 requests = 1 premium request | ❌ | 3000 uses | 15000 uses |
| 1x | 1 request = 1 premium request | ❌ | 1000 uses | 5000 uses |
| 1.25x | 1 request = 1.25 premium requests | ❌ | 800 uses | 4000 uses |
| 10x | 1 request = 10 premium requests (very expensive) | ❌ | 100 uses | 500 uses |

### Model Changelog & Deprecations (October 2025)

**Deprecated Models** (Effective 2025-10-23):

- ❌ o3 (1x) → Replace with GPT-5 or Claude Sonnet 4.5 for reasoning
- ❌ o4-mini (0.33x) → Replace with GPT-5 mini (0x) for cost, GPT-5 (1x) for quality
- ❌ Claude Sonnet 3.7 (1x) → Replace with Claude Sonnet 4 or 4.5
- ❌ Claude Sonnet 3.7 Thinking (1.25x) → Replace with Claude Sonnet 4.5
- ❌ Gemini 2.0 Flash (0.25x) → Replace with Grok Code Fast 1 (0.25x) or GPT-5 mini (0x)

**Preview Models** (Subject to Change):

- 🧪 Claude Sonnet 4.5 (1x) - Preview status, may have API changes
- 🧪 Grok Code Fast 1 (0.25x) - Preview, free during preview period

**Stable Production Models**:

- ✅ GPT-4.1, GPT-5, GPT-5 mini, GPT-5 Codex (OpenAI)
- ✅ Claude Sonnet 3.5, Claude Sonnet 4, Claude Opus 4.1 (Anthropic)
- ✅ Gemini 2.5 Pro (Google)

### Auto Model Selection Behavior (Sept 2025+)

**Included in Auto Selection**:

- GPT-4.1 (0x)
- GPT-5 mini (0x)
- GPT-5 (1x)
- Claude Sonnet 3.5 (1x)
- Claude Sonnet 4.5 (1x)

**Excluded from Auto Selection**:

- Models with multiplier > 1 (Claude Opus 4.1, deprecated o3)
- Models blocked by admin policies
- Models unavailable in subscription plan (1x models in Free tier)

**When Auto Selects**:

- Copilot analyzes prompt complexity, context size, task type
- Chooses from eligible pool based on availability and rate limits
- Applies 10% multiplier discount on auto-selected models
- Shows selected model on hover over response in Chat view
