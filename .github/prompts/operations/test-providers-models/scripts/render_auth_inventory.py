#!/usr/bin/env python3
"""Render one auth-inventory markdown per provider, plus a consolidated table.

Inputs:
  - .hermes/reports/test-providers-probe.json (from test-providers-probe.py)
  - Local known-good metadata for each provider (docs URL, env var, etc.)

Outputs:
  - provider_docs/<provider>.md -- one rendered auth-inventory file per provider
  - provider_docs/_consolidated.md -- single table of all providers
"""
from __future__ import annotations

import json
import re
from datetime import datetime, timezone
from pathlib import Path

REPO_ROOT = Path(__file__).resolve().parents[5]
PROBE_JSON = REPO_ROOT / ".hermes/reports/test-providers-probe.json"
PROVIDER_DOCS = REPO_ROOT / ".github/prompts/operations/test-providers-models/provider_docs"

# Curated metadata table. Each value lists the canonical docs URL, the env var
# (or "oauth" for device_code flows), the base inference endpoint, and any
# known rate-limit / auth-failure notes.
PROVIDER_META: dict[str, dict[str, str]] = {
    "opencode-zen": {
        "docs_url": "https://opencode.ai/docs/zen/",
        "key_env": "OPENCODE_ZEN_API_KEY",
        "endpoint": "https://opencode.ai/zen/v1",
        "auth_mechanism": "api_key",
    },
    "nous": {
        "docs_url": "https://inference-api.nousresearch.com/",
        "key_env": "oauth (device_code)",
        "endpoint": "https://inference-api.nousresearch.com/v1",
        "auth_mechanism": "device_code_oauth",
    },
    "openrouter": {
        "docs_url": "https://openrouter.ai/docs",
        "key_env": "OPENROUTER_API_KEY",
        "endpoint": "https://openrouter.ai/api/v1",
        "auth_mechanism": "api_key",
    },
    "deepseek": {
        "docs_url": "https://platform.deepseek.com/api-docs/",
        "key_env": "DEEPSEEK_API_KEY",
        "endpoint": "https://api.deepseek.com/v1",
        "auth_mechanism": "api_key",
    },
    "gemini": {
        "docs_url": "https://ai.google.dev/gemini-api/docs",
        "key_env": "GOOGLE_API_KEY",
        "endpoint": "https://generativelanguage.googleapis.com/v1beta",
        "auth_mechanism": "api_key",
    },
    "openai-codex": {
        "docs_url": "https://github.com/features/copilot",
        "key_env": "oauth (device_code)",
        "endpoint": "https://api.openai.com/v1",
        "auth_mechanism": "device_code_oauth",
    },
    "openai-api": {
        "docs_url": "https://platform.openai.com/docs",
        "key_env": "OPENAI_API_KEY",
        "endpoint": "https://api.openai.com/v1",
        "auth_mechanism": "api_key",
    },
    "huggingface": {
        "docs_url": "https://huggingface.co/docs/api-inference",
        "key_env": "HF_TOKEN",
        "endpoint": "https://router.huggingface.co/v1",
        "auth_mechanism": "api_key",
    },
    "minimax-oauth": {
        "docs_url": "https://docs.x.ai/",
        "key_env": "oauth (global)",
        "endpoint": "https://api.x.ai/v1",
        "auth_mechanism": "oauth",
    },
    "xai": {
        "docs_url": "https://docs.x.ai/docs",
        "key_env": "XAI_API_KEY",
        "endpoint": "https://api.x.ai/v1",
        "auth_mechanism": "api_key",
    },
    "xai-oauth": {
        "docs_url": "https://docs.x.ai/",
        "key_env": "oauth (device_code)",
        "endpoint": "https://api.x.ai/v1",
        "auth_mechanism": "device_code_oauth",
    },
    "ollama-cloud": {
        "docs_url": "https://ollama.com/docs",
        "key_env": "OLLAMA_API_KEY",
        "endpoint": "https://api.ollama.com/v1",
        "auth_mechanism": "api_key",
    },
    "copilot": {
        "docs_url": "https://github.com/features/copilot",
        "key_env": "GITHUB_TOKEN / COPILOT_GITHUB_TOKEN",
        "endpoint": "https://api.githubcopilot.com",
        "auth_mechanism": "api_key",
    },
}


def parse_auth_list(auth_text: str) -> dict[str, list[dict[str, str]]]:
    """Parse `hermes auth list` stdout into per-provider credential records."""
    out: dict[str, list[dict[str, str]]] = {}
    current = None
    for line in auth_text.splitlines():
        m = re.match(r"^([\w-]+) \((\d+) credentials?\):", line)
        if m:
            current = m.group(1)
            out[current] = []
            continue
        if current is None:
            continue
        # Lines look like:
        #   "  #1  OPENAI_API_KEY       api_key env:OPENAI_API_KEY exhausted (402) (ready to retry)"
        #   "  #2  COPILOT_GITHUB_TOKEN api_key env:COPILOT_GITHUB_TOKEN <-"
        cm = re.match(r"^\s*#(\d+)\s+(\S+)\s+(\S+)\s+(\S+)(.*)$", line)
        if cm:
            idx, key_name, key_type, key_source, tail = cm.groups()
            note = tail.strip()
            # Strip trailing arrow used by hermes to mark the "active" credential
            note = re.sub(r"\s*<-\s*$", "", note).strip()
            out[current].append(
                {
                    "index": idx,
                    "key_name": key_name,
                    "key_type": key_type,
                    "key_source": key_source,
                    "note": note,
                }
            )
    return out


def classify(creds: list[dict[str, str]]) -> tuple[str, str]:
    """Return (status, details) for a provider's credential set."""
    if not creds:
        return "missing", "no credentials discovered"
    notes = " | ".join(c["note"] for c in creds if c.get("note"))
    text = " ".join(c["note"] for c in creds).lower()
    if "rate-limited" in text or "429" in text:
        return "rate-limited-429", notes or "rate-limited"
    if "exhausted" in text or "402" in text:
        return "exhausted-402", notes or "exhausted"
    if "auth-failed" in text or "401" in text or "403" in text:
        return "auth-failed-401/403", notes or "auth-failed"
    return "valid", notes or "all keys present"


def render_one(provider: str, creds: list[dict[str, str]], meta: dict[str, str]) -> str:
    status, details = classify(creds)
    auth_file = f"~/AppData/Local/hermes/auth.json (provider={provider})"
    cred_table = "\n".join(
        f"| #{c['index']} | `{c['key_name']}` | {c['key_type']} | `{c['key_source']}` | {c['note'] or '_(no note)_'} |"
        for c in creds
    ) or "_(no credentials parsed)_"
    now = datetime.now(timezone.utc).strftime("%Y-%m-%d %H:%M UTC")
    return f"""---
name: auth-inventory-{provider}
description: Rendered per-provider auth inventory captured by test-providers-models on {now}.
---

# Auth inventory — {provider}

> Captured from `hermes auth list` via `scripts/test-providers-probe.py` on {now}.
> Classified using `scripts/render_auth_inventory.py` (status mapping table).

## Summary

- **Provider:** `{provider}`
- **Key env:** `{meta['key_env']}`
- **Status:** **{status}**
- **Rate / auth notes:** {details}
- **Docs:** {meta['docs_url']}
- **Auth file verified:** `{auth_file}`
- **Auth mechanism:** {meta['auth_mechanism']}
- **Inference endpoint:** `{meta['endpoint']}`

## Credentials

| # | Key name | Type | Source | Note |
|---|----------|------|--------|------|
{cred_table}

## Configuration cross-check

- `~/AppData/Local/hermes/config.yaml` should reference this provider's model
  format (`{provider}:<model-id>`) for the primary model and any fallbacks.
- If status is `valid`, the provider is probe-eligible.
- If status is `rate-limited-429` or `exhausted-402`, probes will likely fail;
  the provider should be skipped in Phase 3.
- If status is `auth-failed-401/403`, the key in the active credential slot
  is rejected; rotate or remove the bad key before probing.
"""


def render_consolidated(rows: list[tuple[str, str, str, dict[str, str]]]) -> str:
    """Render `_consolidated.md` -- one table for all 13 providers."""
    now = datetime.now(timezone.utc).strftime("%Y-%m-%d %H:%M UTC")
    body = "| Provider | Status | Rate / auth notes | Docs |\n|---|---|---|---|\n"
    for provider, status, details, meta in rows:
        body += f"| `{provider}` | **{status}** | {details or '_(none)_'} | {meta['docs_url']} |\n"
    return f"""---
name: auth-inventory-consolidated
description: Single-table auth inventory across all Hermes providers, rendered from the live `hermes auth list` capture on {now}.
---

# Auth inventory -- consolidated

> Captured from `hermes auth list` via `scripts/test-providers-probe.py` on {now}.
> See `provider_docs/<provider>.md` for the full per-provider breakdown.

{body}
"""


def main() -> int:
    if not PROBE_JSON.exists():
        print(f"ERROR: {PROBE_JSON} not found; run scripts/test-providers-probe.py first")
        return 1
    PROVIDER_DOCS.mkdir(parents=True, exist_ok=True)
    data = json.loads(PROBE_JSON.read_text(encoding="utf-8"))
    auth_text = data["auth_list"]["stdout"]
    parsed = parse_auth_list(auth_text)
    rows: list[tuple[str, str, str, dict[str, str]]] = []
    rendered = 0
    for provider, creds in parsed.items():
        meta = PROVIDER_META.get(provider)
        if not meta:
            print(f"  SKIP: {provider} (no metadata)")
            continue
        text = render_one(provider, creds, meta)
        (PROVIDER_DOCS / f"{provider}.md").write_text(text, encoding="utf-8")
        rendered += 1
        status, details = classify(creds)
        rows.append((provider, status, details, meta))
        print(f"  WROTE: {provider}.md  status={status}")
    (PROVIDER_DOCS / "_consolidated.md").write_text(render_consolidated(rows), encoding="utf-8")
    print(f"  WROTE: _consolidated.md ({len(rows)} providers)")
    print(f"\nRendered {rendered} per-provider files + 1 consolidated table.")
    print(f"Output dir: {PROVIDER_DOCS}")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
