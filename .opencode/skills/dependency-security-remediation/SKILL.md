---
name: dependency-security-remediation
title: "Dependency Security Remediation"
description: "Audit, triage, and fix vulnerable Python dependencies in venvs. Cross-reference manifests vs runtimes, check agent constraints, upgrade safely with rollback."
version: 1.1.0
author: Alexa
license: MIT
tags: [security, venv, pip, remediation]
---
## Goal

Systematically fix CVE findings in Python dependencies: identify the real venv, cross-reference constraints, upgrade safely, verify with imports.

## Overview

Automated reasoning and workflow tool for `dependency-security-remediation`. Execute multi-step tasks with deterministic quality controls and structured outputs.

## When to Use

- A security audit (pip-audit / safety / GHSA report) lists vulnerable packages
- `pip install --upgrade` alone fails due to hard `==` pins from the agent
- User asks "fix these CVEs" or "remediate vulnerabilities" in a Python project
- Venv drift detected (requirements.txt says X, installed version is Y < X)

## Workflow

See `references/venv-cve-remediation.md` for the full Python-venv workflow. For cross-project scanning and non-Python deps, see `references/cross-project-audit-workflow.md`.

High-level phases:

1. **Locate the real venv** — SandBox/venv may be an alias of %LOCALAPPDATA%/hermes/hermes-agent/venv
2. **Scan all projects** — don't stop at root requirements.txt; check every `projects/*/req*.txt` for pinned vulnerable versions (see cross-project audit reference)
3. **Triple-check** — manifest (requirements.txt) vs venv (pip show) vs application pins (pip show hermes-agent | grep Requires)
4. **Check dependents** — who requires the vulnerable package? If no one, upgrade freely
5. **Check consumer constraints** — will the new version satisfy all importers? Hard `==` pins need --force-reinstall or deferral
6. **Pin MCP server versions** — if `@latest` appears in `config.yaml` MCP server args, pin via `hermes config set mcp_servers.<name>.args` (covered in cross-project audit reference)
7. **Rollback snapshot** — pip freeze before any change (no git on ~/.hermes)
8. **Upgrade** — use `uv pip install` for PEP 668 (uv-managed) environments; `pip install --force-reinstall --no-deps` for hard-pinned packages
9. **Verify** — pip show versions + runtime import of each upgraded package + import of its consumers + `pip-audit --strict --desc` for zero-finding confirmation
10. **Report** — which CVEs closed, which deferred, and why

## Pitfalls

- **SandBox/venv is not the real venv.** The runtime agent often lives at %LOCALAPPDATA%/hermes/hermes-agent/venv. Check both before targeting.
- **Hard== pins block safe upgrades.** hermes-agent often pins exact versions. The resolver will warn (not fail) but the package may not actually replace — use --force-reinstall --no-deps.
- **Transitive deps have no manifest entry.** If the package isn't in requirements.txt, `pip install --upgrade` is correct but it won't survive a `pip install -r requirements.txt` rebuild. Pin it explicitly if the fix must stick.
- **Module import name ≠ package name.** PyNaCl installs as `pynacl` but imports as `nacl`. Verify with `pip show` + `python -c "import nacl"`, not by matching the audit report's name.
- **Don't stop at root requirements.txt.** Vulnerable pinned versions often live in stale `projects/*/requirements.txt`. Always scan all projects with `grep -rn` before declaring done.
- **PEP 668 blocks `pip install`.** `uv`-managed environments reject direct `pip install` with "externally-managed-environment". Use `uv pip install` instead.
- **`@latest` in MCP server args is a CVE vector.** Security scanners flag it because the version is un-pinned. Fix via `hermes config set mcp_servers.<name>.args`.
- **`hermes config set` can hit PermissionError on Windows.** The atomic YAML replace may race with file locking. Retry after `sleep 2`.

## References

- `references/venv-cve-remediation.md` — full 8-step Python-venv workflow, batch-replacement quoted-string pitfall, ad-hoc verification pattern
- `references/cross-project-audit-workflow.md` — cross-project requirements.txt scanning, `uv pip install` for PEP 668 envs, MCP server `@latest` pinning via `hermes config set`, full pip-audit cycle
- `references/2026-08-07-python-vulnerability-remediation.md` — session record: 14 CVEs (aiohttp, cryptography, PyNaCl) remediated in SandBox venv via pip upgrade; hermes-agent pin conflict noted; verification via `hermes security audit`

## Related

- `systematic-debugging` — use Phase 1-4 for the root-cause investigation; this skill extends Phase 4 with venv-specific remediation steps

## Verification Checklist

- [ ] Prerequisites and environment are properly configured
- [ ] "Dependency Security Remediation" operations completed successfully
- [ ] Output meets expected quality and requirements
- [ ] Any errors during execution were resolved
- [ ] Changes are documented and committed if applicable

## Best Practices

1. **Prepare before executing**: Ensure all prerequisites and dependencies are in place
2. **Validate inputs**: Check configuration, parameters, and environment before running
3. **Handle errors gracefully**: Implement proper error handling and recovery
4. **Document results**: Keep records of what was done, what worked, and what didn't
5. **Clean up**: Remove temporary files, release resources after completion
