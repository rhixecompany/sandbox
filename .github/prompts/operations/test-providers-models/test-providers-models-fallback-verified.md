
  Primary:   thinkingmachines/inkling:free  (via openrouter)

  Fallback chain (3 entries):
    1. thinkingmachines/inkling:free  (via openrouter)  [https://openrouter.ai/api/v1]
    2. poolside/laguna-s-2.1:free  (via openrouter)  [https://openrouter.ai/api/v1]
    3. nvidia/nemotron-3-super-120b-a12b:free  (via openrouter)  [https://openrouter.ai/api/v1]

  Tried in order when the primary fails (rate-limit, 5xx, connection errors).
  Docs: https://hermes-agent.nousresearch.com/docs/user-guide/features/fallback-providers

