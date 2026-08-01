# OpenRouter Free Models Catalog (Web Research — 2026-07-27)

## Source: costgoat.com/pricing/openrouter-free-models, buldrr.com, teamday.ai, openrouter.ai/collections/free-models

## Free Models (18 as of Jul 2026)

| Model ID                                 | Provider | Context | Best For                                          | Notes                                                      |
| ---------------------------------------- | -------- | ------- | ------------------------------------------------- | ---------------------------------------------------------- |
| `nvidia/nemotron-3-ultra-550b-a55b:free` | NVIDIA   | 1M      | Long-horizon agents, deep research, orchestration | Most-used free model on OpenRouter                         |
| `nvidia/nemotron-3-super-120b-a12b:free` | NVIDIA   | 1M      | Multi-agent apps, cross-document reasoning        | 120B params, only 12B active (MoE)                         |
| `qwen/qwen3-coder:free`                  | Qwen     | 1M      | Code exploration, repository-scale context        | Strongest free coding model                                |
| `google/gemma-4-31b-it:free`             | Google   | 262K    | General multimodal instruction                    |                                                            |
| `google/gemma-4-26b-a4b-it:free`         | Google   | 262K    | General multimodal instruction                    | MoE: 26B total, 4B active                                  |
| `nvidia/nemotron-3-nano-30b-a3b:free`    | NVIDIA   | 256K    | Efficient specialized agents                      | Small MoE, low compute                                     |
| `cohere/north-mini-code:free`            | Cohere   | 256K    | Code generation, terminal & agentic coding        | Cohere's first agentic coding model                        |
| `poolside/laguna-m.1:free`               | Poolside | 262K    | Agentic coding, complex software engineering      | Flagship free coding model                                 |
| `poolside/laguna-xs-2.1:free`            | Poolside | 262K    | Fast, compact coding agent                        | Released Jul 2, 2026 (newest)                              |
| `openai/gpt-oss-120b:free`               | OpenAI   | 131K    | General reasoning + agentic tool use              | Open-weight, Apache 2.0                                    |
| `openrouter/free`                        | Router   | Varies  | Auto-routes among free models                     | Filters for capabilities (image, tools, structured output) |

## Key Observations

- Context windows: 131K → 1M tokens
- 1M context available on Nemotron Ultra/Super and Qwen3-Coder
- `openrouter/free` router auto-selects but not reproducible for production
- Catalog changes frequently — re-fetch before production use

## Web Sources

- https://costgoat.com/pricing/openrouter-free-models (18 models listed)
- https://buldrr.com/openrouter-free-api-keys-free-models-simple-guide
- https://www.teamday.ai/blog/best-free-ai-models-openrouter-2026
- https://openrouter.ai/collections/free-models (official)
- https://apidog.com/blog/free-ai-models (technical guide)

EOF
cat docs/research/openrouter-free-models.md
