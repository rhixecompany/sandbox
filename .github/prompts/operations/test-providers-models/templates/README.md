# Templates for test-providers-models

Templates share two operational invariants:

- Use the exact self-profile prompt from `../scripts/provider_status.py`.
- Run `hermes auth list` before probes and skip every model for a provider with
  rate-limit evidence; record `status: skipped` and
  `skip_reason: provider_rate_limited` without invoking `hermes chat`.
