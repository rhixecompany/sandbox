# Phase 3: Config Update & Verification

Goal: Apply the validated best-2 model selection to Hermes config only if current config differs; otherwise note unchanged.

## Config writes
```bash
hermes config set model.default <model>
hermes config set model.provider <provider>
hermes config set fallback_providers '[...]'
```

## Verification
- `hermes config check`
- Inspect ` ~/AppData/Local/hermes/config.yaml`
- Fix malformed JSON-string-list fallback artifacts with safe Python replacement if needed

## Deliverables
- Verified config state summary
- Final selection report `docs/free-model-selection.md`
