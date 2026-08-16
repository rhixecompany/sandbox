# Credential Vault File Formats + Selector Recipes

Observed 2026-07-28 while hydrating `.env` from `~/Desktop/Github/*.txt` (25 files, 30 vars).
These shapes recur in plaintext credential vaults; classify each file before mapping.

## File Shapes

### 1. Single-line token (most common)
```
sk-proj-abc…xyz
```
→ whole file is the value. Selector: `None` (first non-empty line).

### 2. Label-prefixed variants (key rotation history)
```
OLD: sk-proj-old…aaa
NEW: sk-proj-new…bbb
new3: sk-proj-newest…ccc
```
→ selector `label:<prefix>`, match case-insensitively, split on FIRST colon only.
`personal_access_token:` works the same (underscores are fine; colons inside the
*value* are not separators — split once).

### 3. Multi-line with blank separators
```
sk-proj-key-one…111

sk-proj-key-two…222
```
→ selector `line:N` = Nth **non-empty** line (blank lines do not count).
This bit the extraction logic when a blank line sat between two keys.

### 4. Prefix-selectable lines (one file, two key types)
```
tskey-api-kvtPez…qFs5
tskey-auth-kPxKD…cDXi
```
→ selector `prefix:<token>` matches the line starting with the exact token
(`tskey-api-`, `tskey-auth-`, `hf_`, `ghp_`, `gsk_`, `sk-`, `tvly-`, `xai-`).

### 5. Pairs (access key id + secret)
```
LTAI_SANITIZED
SANITIZED_SECRET
```
→ `line:0` + `line:1`. In the field these were Alibaba `_ID` / `_SECRET`.

## Selector Implementation (hardened)

```python
def extract(lines, selector):
    if selector is None:                       # whole file
        return next((ln for ln in lines if ln.strip()), None)
    if selector.startswith("line:"):           # nth NON-EMPTY line
        idx = int(selector.split(":")[1])
        non_empty = [ln for ln in lines if ln.strip()]   # strip(), not truthiness
        return non_empty[idx] if idx < len(non_empty) else None
    if selector.startswith("prefix:"):
        pref = selector.split(":", 1)[1]
        return next((ln for ln in lines if ln.startswith(pref)), None)
    if selector.startswith("label:"):
        label = selector.split(":", 1)[1]
        for ln in lines:
            if ln.lower().startswith(label.lower()):
                return ln.split(":", 1)[1].strip() or None
        return None
```

The `if ln.strip()` in `None`/`line:` branches is load-bearing: `if ln` alone lets
whitespace-only lines through, silently shifting line indices. Fix BOTH branches
when you find it in one.

## Mapping Conventions

- Group output `.env` by provider with `# --- Provider ---` headers
- Suffix variants: `_OLD`, `_NEW3`, `_PAT`, `_RHIXECOMPANY` (owner), `_2` (second key)
- Normalize vault filename typos in the env var: `sithery` → `SMITHERY_API_KEY`,
  `travely` → `TAVILY_API_KEY`, `tailgate` → `TAILSCALE_*`, `xgrok` → `XAI_API_KEY`,
  `huncho` → `HONCHO_API_KEY`, `olama` → `OLLAMA_CLOUD_API_KEY`
- NEVER map billing/PII files (name, address, card) — those are not service keys

## Real-World Observations (2026-08-07)

### env_sync.py implementation notes
The user's active hydration script is at `~/AppData/Local/hermes/scripts/env_sync.py` (not the
generic `build_env_from_vault.py` template). It uses a `PLAN` dict mapping env var →
`(filename, extraction_hint)` where hints include `auto`, `idx0`/`idx1`, `longest`,
`prefix:<token>`, and custom prefixes like `sk-proj-7` / `sk-proj-3` for OpenAI
key rotation, `ghp_wX` / `ghp_oran` / `github_pat` for GitHub PAT variants.

**Fixed typo:** `SMITHERY_LEGACY_UUID` was mapped to `"sithery-api-key.txt"` (missing
`m`). Actual filename is `smithery-api-key.txt`. Corrected in script line 92.

### Empty / placeholder files
- `groq-cloud-api-key.txt` — 1 byte (newline only) → `EXTRACT-FAILED`
- `xgrok-api-key.txt` — 0 bytes → `EXTRACT-FAILED`
These are expected gaps; the script reports them cleanly without crashing.

### Duplicate-key handling (alibaba)
`alibaba-access-key.txt` contains two keys on separate lines. The script handles this
by:
1. First pass: `PLAN` entry with `idx0` → `ALIBABA_ACCESS_KEY_ID`
2. Explicit second pass (lines 137-141): `tokens_of()` again → `idx1` → `ALIBABA_ACCESS_KEY_SECRET`
This pattern works but is brittle if file grows beyond 2 lines — consider a proper
`line:1` selector in the `PLAN` for future maintainability.
