# Phase 0: Auth & Provider Inventory

> Template for `test-providers-models`. Follow the domain rules in `_shared/rules-core.md`.

## Inputs

- `hermes auth list` (live source of truth)
- `hermes config show` (current provider/model config)

## Outputs

- Provider inventory table (provider | auth status | notes)
- Credential status per provider
- List of authorized providers for probe clusters

## Verification Gate

- [ ] All 9 authorized providers captured (copilot, deepseek, gemini, huggingface, nous, ollama-cloud, openai-codex, openrouter, xai-oauth)
- [ ] At least one provider has rate-limit warning noted
- [ ] Credential source documented (key file / OAuth / device code)

## Reference

See `test-providers-models.prompt.md` — Context Block for full baseline state as of 2026-08-07.
