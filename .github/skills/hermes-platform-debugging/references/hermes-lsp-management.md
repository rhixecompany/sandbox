---
name: hermes-lsp-management
title: "Hermes LSP Server Management"
description: "Use when installing or fixing Hermes LSP servers."
version: 1.0.0
author: Hermes Agent
license: MIT
tags: [hermes, lsp, tooling, windows, diagnostics]
---

# Hermes LSP Server Management

Use when the user asks to install, list, configure, or fix Hermes language servers
(`hermes lsp ...`), when `hermes lsp list` shows `[missing]` entries, or when
post-write semantic diagnostics are absent for a language.

## Key Commands

```bash
hermes lsp list          # installed / missing / manual-only per language
hermes lsp status        # service state + active clients
hermes lsp install <id>  # auto-install (recipe-based only)
hermes lsp install-all   # all servers with a known auto-install recipe
```

## Architecture: recipe-based vs PATH-probe

Only a handful of servers have auto-install recipes, defined in
`~/AppData/Local/hermes/hermes-agent/agent/lsp/install.py` `INSTALL_RECIPES`:

- **npm strategy**: pyright, typescript-language-server, @vue/language-server,
  svelte, astro, yaml, bash, intelephense, dockerfile
- **go strategy**: gopls (`go install golang.org/x/tools/gopls@latest`)
- **pip strategy**: (present in code, none registered by default)

Everything else — ocaml-lsp, dart, haskell-language-server, julia, nixd,
elixir-ls, kotlin-language-server, jdtls, rust-analyzer, clangd, lua,
powershell — is **PATH-probe only**. `hermes lsp install <id>` prints
"install failed (see logs)" for these because `_do_install` falls back to
`shutil.which(pkg)`; the server appears `[installed]` only when its binary is
found on PATH **or** in the Hermes staging dir
`~/AppData/Local/hermes/lsp/bin/` (which is checked BEFORE PATH).

So `[missing]` for a non-recipe server is NOT an install failure — it means the
language toolchain is absent. Install the toolchain, then re-run `hermes lsp list`.

## Toolchain-First Install Path (Windows)

Install the language toolchain via winget, then detect:

| Missing LSP | Toolchain (winget ID) | Extra steps |
|-------------|----------------------|-------------|
| gopls | `GoLang.Go` | Then `hermes lsp install gopls` (go recipe works once Go on PATH) |
| jdtls / kotlin-language-server | `EclipseAdoptium.Temurin.21.JDK` | JDK alone insufficient — download server distribution + place launcher in lsp bin dir |
| julia | `JuliaLang.Julia` | Installs to `%LOCALAPPDATA%\Programs\Julia-1.12.6\bin` (NOT Program Files); also `julia -e 'using Pkg; Pkg.add("LanguageServer")'` |
| dart | `Google.DartSDK` | The correct winget ID is `Google.DartSDK`, not `Google.Dart-SDK`; `dart` binary on PATH suffices |
| elixir-ls | `Erlang.ErlangOTP` + Elixir | Also needs the elixir-ls distribution |

Manual server distributions:
- kotlin-language-server: `server.zip` from
  `https://github.com/fwcd/kotlin-language-server/releases/latest`
- jdtls: `https://download.eclipse.org/jdtls/snapshots/jdt-language-server-latest.tar.gz`
- Extract launcher (e.g. `jdtls.cmd`, `kotlin-language-server.bat`) into
  `~/AppData/Local/hermes/lsp/bin/` so detection finds it.

Toolchains NOT practical via winget: ocaml (choco has only ancient 4.0.1),
haskell (ghc exists but HLS needs GHC bootstrap), nixd (Nix not native on
Windows). Classify these as manual-only and document rather than chase.

## Verification

```bash
hermes lsp list    # target server shows [installed]
hermes lsp status  # service active; optionally shows active clients
```

Sanity-check a toolchain landed where expected (winget per-user installs land in
`%LOCALAPPDATA%\Programs\`, NOT `C:\Program Files\`):

```bash
ls -d /c/Users/<user>/AppData/Local/Programs/Julia* 2>/dev/null
command -v go java julia dart   # refresh PATH in-session after winget installs
```

## Pitfalls

- **`hermes update` blocked by .pyd locks on Windows**: any running Hermes
  python.exe holds native extension files locked, so update refuses. Close the
  desktop app / other Hermes terminals, re-run; `--force-venv` is a deliberate
  last resort. After any successful update run `hermes doctor --fix` and
  `npm audit fix` in the hermes-agent dir.
- **Do not chase `already claimed by` warnings**: `Skill 'X' maps to slash
  command /X already claimed by 'X'` is a benign thread race in
  `scan_skill_commands` (concurrent startup scans interleave; `_skill_commands`
  is cleared at each scan start). Verify with a clean scan:
  `cd ~/AppData/Local/hermes/hermes-agent && ./venv/Scripts/python.exe -c "from agent.skill_commands import scan_skill_commands; print(len(scan_skill_commands()))"`
  — 0 warnings + expected count means skills are fine.
- **search_files with MSYS paths**: ripgrep-backed file tools fail on `/c/...`
  paths; use `grep -rn` via terminal for `~/AppData/Local/hermes/hermes-agent`
  (the venv is huge — target `agent/` and `hermes_cli/` subdirs, or the single
  file, to avoid 30s+ timeouts).
- **install-all is a subset**: `hermes lsp install-all` only iterates servers
  with recipes and stops being useful once all recipe servers are installed; it
  will NOT touch the PATH-probe-only servers.

## References

- `references/lsp-install-failure-analysis.md` — worked trace of the 2026-08-01
  install-failure diagnosis: `_do_install` PATH-probe fallback, winget toolchain
  results, gopls special case, and log-noise verification recipes.

## Related

- `hermes-setup` — broader install/config flow (user-owned; adopt before patching)
- `hermes-system-maintenance` — resource/connectivity troubleshooting (user-owned)
- `log-analysis-and-triage` — Hermes log-pattern classification table (user-owned)
