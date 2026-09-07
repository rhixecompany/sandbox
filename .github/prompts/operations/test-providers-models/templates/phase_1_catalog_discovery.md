# Phase 1: Model Catalog Discovery

> Template for `test-providers-models`. Extract available model IDs per provider.

## Inputs

- Provider model endpoint: `https://openrouter.ai/models` or `https://hermes-agent.nousresearch.com/docs/api/model-catalog.json`
- `hermes auth list` (provider names)

## Outputs

- Catalog entries per provider (model ID | description | tier/free flag)
- Cross-reference to `templates/phase_2_free_model_extraction.md`

## Verification Gate

- [ ] Catalog entries documented per provider
- [ ] At least 1 `.md` file in `templates/` references this phase
- [ ] No invented model IDs — all IDs from web research or `hermes auth`
