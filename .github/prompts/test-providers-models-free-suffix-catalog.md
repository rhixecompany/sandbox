# Models with `:free` suffix — verified catalog (line 11 goal)
Source: docs/best-free-models.md + docs/free-model-selection.md + live hermes auth/config/state 2026-09-05
Verified providers (auth state captured by live `hermes auth list` / `hermes config show`):
- opencode-zen: OPENCODE_ZEN_API_KEY env valid; 1 manual key valid; 2 auth-failed 401; 1 manual 401
- openrouter: OPENROUTER_API_KEY env; rate-limited 429 (42m / 16h)
- deepseek: DEEPSEEK_API_KEY env valid; rate-limited 402 (docs say excluded / working via opencode-zen wrapper)
- gemini: GOOGLE_API_KEY env valid
- nous: device_code oauth (no :free model; excluded per docs)
- openai-codex: oauth rate-limited 429 (29d); no free model
- xai: 1 auth-failed 403; 1 env valid; no :free model
- copilot: no free models

Models:
- `opencode-zen/deepseek-v4-flash-free` | vision=True | reasoning=False | ctx=200000 | flags=vision
- `opencode-zen/nemotron-3-ultra-free` | vision=False | reasoning=True | ctx=1000000 | flags=reasoning
- `opencode-zen/nemotron-3-super-free` | vision=False | reasoning=True | ctx=1000000 | flags=reasoning
- `openrouter/nvidia/nemotron-3-nano-omni-30b-a3b-reasoning:free` | vision=True | reasoning=True | ctx=256000 | flags=vision,reasoning,PRIMARY
- `openrouter/nvidia/nemotron-3-ultra-550b-a55b:free` | vision=False | reasoning=True | ctx=1000000 | flags=reasoning
- `openrouter/nvidia/nemotron-3-super-120b-a12b:free` | vision=False | reasoning=True | ctx=1000000 | flags=reasoning
- `openrouter/google/gemma-4-31b-it:free` | vision=False | reasoning=False | ctx=262000 | flags=
- `openrouter/google/gemma-4-26b-a4b-it:free` | vision=False | reasoning=False | ctx=262000 | flags=
- `openrouter/openai/gpt-oss-20b:free` | vision=False | reasoning=False | ctx=131000 | flags=

Top 5 ranked (per docs ranking logic: vision→reasoning→ctx):
1. openrouter/nvidia/nemotron-3-nano-omni-30b-a3b-reasoning:free (vision+reasoning, 256K)
2. openrouter/nvidia/nemotron-3-ultra-550b-a55b:free (reasoning, 1M)
3. opencode-zen/deepseek-v4-flash-free (reasoning, 200K, PRIMARY)
4. openrouter/nvidia/nemotron-3-super-120b-a12b:free (reasoning, 1M)
5. openrouter/google/gemma-4-31b-it:free (262K, no reasoning)
