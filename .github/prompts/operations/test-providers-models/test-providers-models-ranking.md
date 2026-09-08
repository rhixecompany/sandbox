# Test Providers Models Ranking
Generated from Hermes insights and model capabilities testing.

## Model Ranking (Top 5)

|| Rank | Model | Provider | Vision | Reasoning | Context | Status |
|---|---|---|---|---|---|---|---|
| 1 | `nemotron-3-ultra-free` | OpenRouter | Yes | Yes | 2000 | Top-ranked |
| 2 | `nemotron-3-ultra-free` | OpenRouter | Yes | Yes | 2000 | Top-ranked |
| 3 | `nemotron-3-ultra-free` | OpenRouter | Yes | Yes | 2000 | Top-ranked |
| 4 | `nemotron-3-ultra-free` | OpenRouter | Yes | Yes | 2000 | Top-ranked |
| 5 | `nemotron-3-ultra-free` | OpenRouter | Yes | Yes | 2000 | Top-ranked |

## Fallback Chain

1. Primary: `nemotron-3-ultra-free` (OpenRouter)
2. Fallback 1: `nemotron-3-nano-omni-30b-a3b` (OpenRouter)
3. Fallback 2: `nemotron-3.5-lightning-free` (OpenCode Zen)
4. Fallback 3: `deepseek/v4-flash-free` (OpenRouter)
5. Fallback 4: `gemini-2.5-flash` (OpenRouter)

## Configuration Commands

\`\`\`bash
# Set primary model
hermes config set model.default nemotron-3-ultra-free

# Clear existing fallbacks
hermes fallback clear

# Add fallbacks in order
hermes fallback add openrouter/nvidia-nemotron-3-nano-omni-30b-a3b-reasoning:free
hermes fallback add opencode-zen/nemotron-3.5-lightning-free
hermes fallback add deepseek/deepseek-v4-flash-free
hermes fallback add openrouter/google-gemini-2.5-flash

# Verify
hermes config show
hermes fallback list
\`\`\`

## Testing Commands

\`\`\`bash
# Test primary model
hermes chat --model nemotron-3-ultra-free -q "What is 2+2?" --oneshot

# Test fallback models
hermes chat --model openrouter/nvidia-nemotron-3-nano-omni-30b-a3b-reasoning:free -q "What is 2+2?" --oneshot

# Verify fallback chain
hermes fallback list
\`\`\`

*Ranking based on: vision capability, reasoning capability, context window size, and Hermes configuration status*
