# Cross-Project CVE Remediation Workflow

When a security audit (pip-audit) flags CVEs, the vulnerable package often appears in multiple projects. Fix them all in one pass.

## Full Pipeline

### 1. Audit & Identify

```bash
pip-audit --strict --desc
```

For each flagged package, record:
- Package name & current version
- Fixed version (from the advisory description)
- Which CVEs are resolved by the upgrade

### 2. Find All Pinned Occurrences

Scan ALL requirements.txt files across the workspace:

```bash
grep -rn 'pkgname==' projects/*/requirements.txt
grep -rn 'pkgname==' requirements.txt
```

Also check `pyproject.toml` and `Pipfile` if present.

### 3. Patch Every Pinned Version

For each file with a pinned vulnerable version (`==X.Y.Z`), patch to the fixed version (`==A.B.C`) or a minimum constraint (`>=A.B.C`):

- Use `patch` (targeted edit) for each file
- Prefer `>=` over `==` where compatible to allow future patch upgrades
- For stale projects (unmaintained), pinning to the minimum safe version is fine

### 4. Check Unpinned Lines

Lines like just `Pillow` or `pillow` (no version specifier) will resolve to the latest — no action needed.

### 5. Upgrade the Live Environment

PEP 668 environments (managed by `uv`) block direct `pip install`:

```bash
# ✓ Works in uv-managed envs
uv pip install pkgname==A.B.C

# ✗ Fails with: externally-managed-environment
pip install pkgname==A.B.C
```

For pip-managed envs:

```bash
pip install --upgrade pkgname==A.B.C
```

### 6. Handle Hard Pins & Dependents

If the package has hard `==` pins from a consumer:

```bash
# Check who depends on it
pip show pkgname  # Requires field
# or
python -c "import importlib.metadata as m; [print(d.metadata['Name'], [r for r in (d.requires or []) if 'pkgname' in r.lower()]) for d in m.distributions()]"
```

If a consumer hard-pins, use `--force-reinstall --no-deps` to upgrade without cascading.

### 7. Pin MCP Server Versions (npx)

MCP servers invoked via `npx @pkg@latest` have no pinned version — `@latest` resolves
to whatever npm serves, and a security scan sees it as `==latest`.

Fix via `hermes config set`:

```bash
# Check current
grep '@latest' ~/AppData/Local/hermes/config.yaml

# Pin to known-safe version
hermes config set mcp_servers.<name>.args '["-y","@scope/pkg@X.Y.Z"]'

# Verify
pip-audit  # @latest no longer appears
```

Use the latest available version (check with `npm view @scope/pkg version`), not the
minimum fixed version, to stay current on future patches.

### 8. Install & Run pip-audit

```bash
# Install if missing
uv pip install pip-audit

# Full audit
pip-audit --strict --desc
```

### 9. Verify

```bash
# Version match
python -m pip show pkgname | grep Version

# Runtime import
python -c "import pkgname; print('OK')"

# No remaining vulns
pip-audit --strict
# → No known vulnerabilities found
```

## Example: pillow CVE Batch Fix

Given `pillow==12.2.0` flagged with 10 HIGH + 3 MODERATE CVEs (fixed in 12.3.0):

| File | Original | Fix |
|------|----------|-----|
| `requirements.txt` | `pillow==12.2.0` | `pillow==12.3.0` |
| `projects/ecom/requirements.txt` | `pillow==9.0.1` | `pillow>=12.3.0` |
| `projects/Python-projects/requirements.txt` | `pillow==11.1.0` | `pillow>=12.3.0` |
| `projects/profile/requirements.txt` | `Pillow` (unpinned) | no change needed |
| `projects/xamehi.tv/requirements.txt` | `pillow` (unpinned) | no change needed |

## Pitfalls

- **Don't stop at root requirements.txt.** Other projects may pin older vulnerable versions. Scan all `projects/*/requirements.txt`.
- **`uv pip install` vs `pip install`.** In `uv`-managed environments, `pip install` errors with "externally-managed-environment". Always check first.
- **`@latest` in MCP config is a CVE vector.** Security scanners flag it because there's no pinned version. Pin via `hermes config set`.
- **`hermes config set` can fail with PermissionError.** The atomic replace may hit Windows file locking. Retry after a short sleep (`sleep 2 && hermes config set ...`).
- **Verify with pip-audit, not just version check.** A version match in `pip show` is necessary but not sufficient — pip-audit checks the advisory database against the full dependency tree.
