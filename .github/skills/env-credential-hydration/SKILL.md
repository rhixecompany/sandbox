---
name: env-credential-hydration
description: Use when building .env from a plaintext credential vault.
version: 1.0.0
author: Hermes Agent
license: MIT
tags: [security, credentials, dotenv, secrets, vault]
---

# Env Credential Hydration

## When To Use

- User asks to configure `.env` files from a folder of plaintext key files (e.g. `~/Desktop/Github/*.txt`, `~/.keys/`, a credential vault dir)
- Wiring provider/API tokens (OpenAI, GitHub, Groq, HuggingFace, Tavily, Neon, etc.) into a root or per-project `.env`
- Any task where reading secret files is unavoidable and the values must NOT be echoed into the conversation

## When NOT TO USE

- Creating new credentials (use 1password / provider dashboards)
- Scanning for leaked secrets in a repo (use secret-scanning)

## Core Principle: never put raw secret values in tool calls

The transcript is a record of every tool payload. A `write_file`/`patch`/`echo` that contains the literal key value embeds it permanently. The fix: **a script reads the vault at runtime and writes `.env` itself**; the script source contains zero secret values, and its stdout prints only masked forms.

```python
# Correct: build_env.py reads raw files at runtime; no key appears in the script
val = Path(vault).read_text().strip()      # secret stays in-process
OUT.write_text(f"SERVICE_API_KEY={val}\n") # secret lands only on disk
print(f"SERVICE_API_KEY = {mask(val)}")    # stdout shows sk-…abcd only
```

## Workflow

1. **Inventory the vault.** List every credential file; read each (the file tool auto-redacts known key prefixes — rely on the *shape* of each file: line count, label prefixes like `OLD:`/`NEW:`/`new3:`, multi-line entries).
2. **Map filename → env var(s).** One file can yield multiple vars (e.g. `tailgate-api-key.txt` holds both `tskey-api-…` and `tskey-auth-…` lines; labeled files hold old/new/pat variants).
3. **Classify file formats** (see `references/credential-file-formats.md`):
   - single-line token → whole file
   - `label: value` lines → extract after `label:`
   - multi-line with blanks → nth non-empty line
   - prefix-selectable lines (`tskey-api-` vs `tskey-auth-`)
4. **Write the `.env` grouped by provider** with comment headers, then verify (below).
5. **Exclude non-key files.** Billing/PII files (name, address, credit card) are NOT service keys — never copy them into `.env`. Say so explicitly.
6. **Confirm `.gitignore` covers `.env`** (`git check-ignore .env` must exit 0).

## Verification (all masked)

- **Mask format:** `v[:6] + "…" + v[-4:]` — enough to distinguish keys, never enough to use them.
- **Spot-check integrity:** compare masked env value vs masked source value for a sample of vars (guards against wrong-line extraction).
- **Structure checks:** every var present, no duplicates, no empty values, no PII substrings (anything from the excluded billing file).
- **Idempotency:** run twice, `.env` byte-identical. Compare as *text* (`read_text`) — comparing `read_bytes()` against `read_text().encode()` always fails on Windows (CRLF).
- **Script stdout masked:** regex `^\s{2}\S+ = ` lines must contain `…` (watch for `===` header lines that trip naive `"=" in line` checks).

## Ad-hoc Verification Harness Pattern

When a script has no test suite, verify with a throwaway temp script:

- Create under `%TEMP%` with `hermes-verify-` prefix (`tempfile.mkstemp(prefix="hermes-verify-", suffix=".py")`), run it, then delete it.
- Distinguish **test-harness bugs** from **code bugs**: if a check fails, first ask whether the assertion or fixture is wrong (wrong expected value, CRLF vs LF, naive regex) before touching the code.
- For a script you exec'd to load its functions, re-run it as a subprocess for E2E checks (module exec also triggers top-level side effects).

## Pitfalls

- **`if ln` vs `if ln.strip()`:** filtering "non-empty" lines with `if ln` lets whitespace-only lines through. Use `if ln.strip()` everywhere you mean "has content". Fix the class, not one site — check both `None`-selector and `line:N`-selector branches.
- **read_file auto-redaction:** values come back as `«redacted:sk-…»`. This is fine for understanding structure but means you cannot eyeball full values — write the hydration script to read raw files itself.
- **Label case/format drift:** labels may be `OLD:`, `old:`, `new3:`, `personal_access_token:` — match case-insensitively, split on the FIRST colon only (values like `github_pat_…` may contain colons inside the value — split once).
- **CRLF output on Windows:** `Path.write_text` emits `\r\n`; verification must account for it.
- **Never commit `.env`:** confirm `.gitignore` line exists before finishing; keep the hydration script in `scripts/` (repo-friendly) but never the `.env` itself.
- **Wrong test endpoint ≠ dead key.** A `404`/`401`/`0` from an invented URL proves nothing. Cloud MCP providers expose gateways (`mcp.neon.tech/mcp`, `mcp.context7.com/mcp`, `mcp.honcho.dev/`, `mcp.smithery.ai/<namespace>`) while their REST hosts (`api.neon.tech`, `context7.com`) may not resolve on the user's network. Check the URL the agent actually uses in `config.yaml` before declaring a key dead. MCP gateways reject plain JSON-RPC with `406 Not Acceptable` unless the request sends `Accept: application/json, text/event-stream`.
- **Distinguish key-fail from provider-fail:** xAI `403 permission-denied` = valid key, billing/credit block (do NOT purge — top up instead); Hostinger Cloudflare `530/1016` = provider origin-DNS outage (unverifiable, keep existing); `tskey-auth-` Tailscale pre-auth keys return `401` against the API by design (they're for `tailscale up --auth-key`, not API calls). Only `401/403 invalid/expired` on a healthy endpoint means the key is dead.
- **Explicit extraction hints, never fallthrough.** Multi-label files (`OLD`/`NEW`/`new3`, `github_pat_` vs `ghp_or`) must map each label to an explicit prefix hint in `extract()`. The generic "first token ≥20 chars" fallback silently picks the WRONG token (a `github_pat_` when the var wanted `ghp_or`), and a sync built on that will overwrite a good deployed key. Verify extracted fingerprint == deployed fingerprint BEFORE `--apply`.
- **Alibaba access keys need a signed request** (RPC v1.0 HMAC-SHA1 `GetCallerIdentity` against `sts.aliyuncs.com`) — a bare GET cannot validate them.

## Validate-then-sync workflow (working keys only) — PREFERRED

User-preferred order when syncing the vault into agent `.env` files: **test
every key against its provider URL FIRST, then write only the keys that
passed** (trigger: "test each key ... only then update ... with each working
key"). Two reusable scripts (in `$LOCALAPPDATA/hermes/scripts/`):

1. `python vault_key_validate.py --json` — extracts every key from the vault,
   calls each provider's LIVE endpoint (REST or MCP gateway), prints masked
   status, writes `%TEMP%\hermes-vault-working-keys.json` (working keys only).
   Read-only — never touches agent files.
2. `python vault_key_sync.py` (dry-run) then `--apply` — idempotently writes
   ONLY the validated working keys into Hermes root `.env` and workspace
   `.env`, with timestamped `.bak` backups. A dry-run after apply must show
   "no changes needed" (idempotency check).

`env_sync.py` (below) is the legacy bulk path — it does NOT validate and will
copy dead/expired keys. Prefer validate-then-sync for rotation tasks.
Endpoint map, verified URLs, and extraction hints: `references/validate-then-sync.md`.

## Hermes credential sync variant (absorbed: `hermes-credential-sync`)

When the destination is Hermes itself (root `.env`, `hermes auth` credential
store, MCP server configs, and per-project `.env` files) rather than a plain
project `.env`, use the Hermes sync path: run
`python "$LOCALAPPDATA/hermes/scripts/env_sync.py"` (dry-run) then `--apply`,
and `add_mcp_servers.py` for MCP configs. Verify with `hermes auth list` —
every provider should show the `←` source marker.
Full workflow, trigger phrases, and verification: `references/hermes-credential-sync.md`.

## Support Files

- `references/credential-file-formats.md` — observed vault file shapes + selector recipes
- `references/hermes-credential-sync.md` — syncing a vault into Hermes `.env` / auth store / MCP configs
- `references/validate-then-sync.md` — live endpoint map, status-code triage, extraction rules for the validate-then-sync scripts
- `scripts/build_env_from_vault.py` — generic parameterized hydration script (edit the MAP at the top; no secrets baked in)

## Verification Checklist

- [ ] Prerequisites and environment are properly configured
- [ ] Env Credential Hydration operations completed successfully
- [ ] Output meets expected quality and requirements
- [ ] Any errors during execution were resolved
- [ ] Changes are documented and committed if applicable

## When to Use


- When you need to perform Env Credential Hydration operations or tasks
- When managing Env Credential Hydration infrastructure or configurations
- When automating or debugging Env Credential Hydration workflows
- **Triggers**: "env credential hydration" required for a project

## Best Practices

1. **Prepare before executing**: Ensure all prerequisites and dependencies are in place
2. **Validate inputs**: Check configuration, parameters, and environment before running
3. **Handle errors gracefully**: Implement proper error handling and recovery
4. **Document results**: Keep records of what was done, what worked, and what didn't
5. **Clean up**: Remove temporary files, release resources after completion
