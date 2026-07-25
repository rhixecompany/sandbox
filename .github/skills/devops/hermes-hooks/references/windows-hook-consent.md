# Windows Hook Consent Gotcha

## Verified remediation path

- After recreating hooks under `~/AppData/Local/hermes/hooks/`, re-register in `hooks:` using the same command form that was previously allowlisted.
- `hermes hooks doctor` can show `not allowlisted` even with `hooks_auto_accept: true`.
- `hermes --accept-hooks ...` does not auto-add entries for wrappers like `bash -c "..."; exact-match command strings still need to match an existing allowlist entry.
- Direct manual addition to `~/AppData/Local/hermes/shell-hooks-allowlist.json` is the fastest non-TTY path when the matching entries are known.
- Preferred working command form on Windows: `"C:/Program Files/Git/usr/bin/bash.exe" -c "<absolute script path>"`.
- After editing the allowlist, rerun `hermes hooks doctor` and `hermes hooks test <event>`.
- If `bash -c "..."` is used, verify `/bin/bash` is resolvable in that execution path; WSL-style `CreateProcessCommon: execvpe(/bin/bash)` failures mean the runtime did not find `bash.exe`, which can happen when Hermes invokes a plain `bash -c` wrapper on DISM/WSL/Junction-managed environments.
