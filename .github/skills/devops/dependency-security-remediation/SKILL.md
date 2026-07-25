---
name: dependency-security-remediation
title: "Dependency Security Remediation"
description: "Audit, triage, and fix vulnerable Python dependencies in venvs. Cross-reference manifests vs runtimes, check agent constraints, upgrade safely with rollback."
version: 1.0.0
author: Alexa
license: MIT
tags: [security, venv, pip, remediation]
---

## Goal

Systematically fix CVE findings in Python dependencies: identify the real venv, cross-reference constraints, upgrade safely, verify with imports.

## When to Use

- A security audit (pip-audit / safety / GHSA report) lists vulnerable packages
- `pip install --upgrade` alone fails due to hard `==` pins from the agent
- User asks "fix these CVEs" or "remediate vulnerabilities" in a Python project
- Venv drift detected (requirements.txt says X, installed version is Y < X)

## Workflow

See `references/venv-cve-remediation.md` for the full workflow with commands, but high-level phases:

1. **Locate the real venv** — SandBox/venv may be an alias of %LOCALAPPDATA%/hermes/hermes-agent/venv
2. **Triple-check** — manifest (requirements.txt) vs venv (pip show) vs application pins (pip show hermes-agent | grep Requires)
3. **Check dependents** — who requires the vulnerable package? If no one, upgrade freely
4. **Check consumer constraints** — will the new version satisfy all importers? Hard `==` pins need --force-reinstall or deferral
5. **Rollback snapshot** — pip freeze before any change (no git on ~/.hermes)
6. **Upgrade** — use --force-reinstall --no-deps for hard-pinned packages, --upgrade-strategy only-if-needed for transitive
7. **Verify** — pip show versions + runtime import of each upgraded package + import of its consumers
8. **Report** — which CVEs closed, which deferred, and why

## Pitfalls

- **SandBox/venv is not the real venv.** The runtime agent often lives at %LOCALAPPDATA%/hermes/hermes-agent/venv. Check both before targeting.
- **Hard== pins block safe upgrades.** hermes-agent often pins exact versions. The resolver will warn (not fail) but the package may not actually replace — use --force-reinstall --no-deps.
- **Transitive deps have no manifest entry.** If the package isn't in requirements.txt, `pip install --upgrade` is correct but it won't survive a `pip install -r requirements.txt` rebuild. Pin it explicitly if the fix must stick.
- **Module import name ≠ package name.** PyNaCl installs as `pynacl` but imports as `nacl`. Verify with `pip show` + `python -c "import nacl"`, not by matching the audit report's name.

## References

- `references/venv-cve-remediation.md` — full 8-step workflow with commands, the batch-replacement pitfall (quoted-string hazard in python code blocks), and the ad-hoc verification pattern

## Related

- `systematic-debugging` — use Phase 1-4 for the root-cause investigation; this skill extends Phase 4 with venv-specific remediation steps
