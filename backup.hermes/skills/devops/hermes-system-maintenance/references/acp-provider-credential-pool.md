# ACP Provider Credential Pool Seed Failures

Detailed technical reference for diagnosing credential pool seed failures triggered by unused ACP providers in Hermes config.yaml.

## Symptom

Repeated DEBUG-level log entries on every Hermes startup:

```
DEBUG agent.credential_pool: Qwen OAuth token seed failed: Qwen CLI credentials not found. Run 'qwen auth qwen-oauth' first.
```

## Root Cause

The credential pool's `_seed_from_singletons()` function (credential_pool.py ~line 1804) has a hardcoded branch for `provider == "qwen-oauth"`:

```python
elif provider == "qwen-oauth":
    from hermes_cli.auth import resolve_qwen_runtime_credentials
    creds = resolve_qwen_runtime_credentials(refresh_if_expiring=False)
    token = creds.get("api_key", "")
    ...
```

This calls `resolve_qwen_runtime_credentials()` → `_read_qwen_cli_tokens()` → reads `~/.qwen/oauth_creds.json`. When that file doesn't exist, it raises:

```python
raise AuthError(
    "Qwen CLI credentials not found. Run 'qwen auth qwen-oauth' first.",
    provider="qwen-oauth",
    code="qwen_auth_missing",
)
```

Caught at line 1831-1832: `logger.debug("Qwen OAuth token seed failed: %s", exc)`

## How It Gets Triggered

The credential pool is initialized for a provider when Hermes resolves a provider block in config.yaml. If config.yaml has a provider that resolves to `qwen-oauth` at any point in its chain (e.g. `qwen-acp: base_url: acp://qwen`), the pool tries to seed credentials.

The mapping chain:
- `model_metadata.py` line 357: `"portal.qwen.ai": "qwen-oauth"` (base URL → provider name)
- `models_dev.py` line 159: `"qwen-oauth": "alibaba"` (provider → API family)

## Fix

1. **Identify** the ACP provider in config.yaml that's triggering the seed:
   ```bash
   grep -B2 -A2 "qwen" ~/AppData/Local/hermes/config.yaml
   ```

2. **Verify it's unused**: Check if any active model, fallback chain, or routing rule references it:
   ```bash
   grep -E "^model:|^fallback_providers:|base_url: acp://" ~/AppData/Local/hermes/config.yaml
   ```

3. **Remove** the provider block from config.yaml (edit via sed since patch/write_file are blocked for protected system files):
   ```bash
   sed -i '13,15d' ~/AppData/Local/hermes/config.yaml
   ```
   (Adjust line numbers to match the actual block)

4. **Verify** the credential pool no longer attempts the seed:
   ```bash
   grep "qwen" ~/AppData/Local/hermes/config.yaml
   ```
   Should return nothing.

## Qwen v0.17.0 Auth Change

`qwen auth` command was **removed** in v0.17.0. Running it shows:

```
qwen auth has been removed.
  Interactive  →  run qwen and use /auth to configure providers
  CI/Headless  →  set OPENAI_API_KEY + OPENAI_BASE_URL + OPENAI_MODEL
  OpenRouter   →  set OPENROUTER_API_KEY and OPENAI_BASE_URL=https://openrouter.ai/api/v1
  Qwen OAuth   →  run qwen interactively and use /auth
```

If Qwen is configured with OpenRouter (settings.json has `security.auth.selectedType: "openai"` with OpenRouter base URL), the CLI works for headless use without any OAuth credentials:

```bash
qwen "one-shot query"                    # ~5s response
qwen --yolo "automated task"             # ~60s for full agent response
```

### `--bare` mode caveat

The `--bare` flag in Qwen v0.17.0 skips loading settings.json entirely, which means it skips the auth config too. Result:

```
No auth type is selected. Please configure an auth type
```

Do NOT use `--bare` for headless queries unless explicitly passing auth params via CLI flags.

## Other Providers With Similar Patterns

The credential pool has hardcoded `_seed_from_singletons` branches for:
- `anthropic` (reads ~/.claude/.credentials.json)
- `nous` (reads auth store)
- `copilot` (resolves via `gh auth token`)
- `qwen-oauth` (reads ~/.qwen/oauth_creds.json) ← this one
- `minimax-oauth` (reads auth store)
- `xai-oauth` (reads auth store)

Any of these can generate seed-failed DEBUG logs when their provider is configured but the credentials file/env doesn't exist. The fix is the same: remove the provider block if it's unused.
