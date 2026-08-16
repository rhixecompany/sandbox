# Session Detail: LSP Install Failure Analysis (2026-08-01)

## Symptom

`hermes lsp install <id>` for 9 servers all printed:
`<server>: install failed (see logs).` while `hermes lsp list` showed `[missing]`.

## Root Cause Trace

1. `agent/lsp/cli.py::_cmd_install` → `try_install(pkg, "auto")`.
2. `agent/lsp/install.py::_do_install`:
   - If pkg IS in `INSTALL_RECIPES` → runs recipe (npm/go/pip).
   - If pkg is NOT in `INSTALL_RECIPES` → `return shutil.which(pkg)` (PATH probe only).
3. `_recipe_pkg_for(server_id)` maps a few aliases (`vue-language-server`,
   `astro-language-server`, `dockerfile-ls`, `typescript`) but NOT the 9 missing ones.
4. Conclusion: "install failed" for non-recipe servers is a misnomer — it just
   means the toolchain binary isn't on PATH. `install-all` skips recipe-less
   servers entirely (it only iterates `INSTALL_RECIPES`).

## gopls Special Case

gopls HAS a recipe (`strategy: "go"`) but failed because Go was not on PATH.
Fix: `winget install --id GoLang.Go`, export PATH, then
`hermes lsp install gopls` → installed to `~/AppData/Local/hermes/lsp/bin/gopls.exe`.

## Toolchain Install Results (Windows, winget)

| Toolchain | Winget ID | Result |
|-----------|-----------|--------|
| Go 1.26.5 | `GoLang.Go` | OK → gopls installable |
| Temurin JDK 21.0.12 | `EclipseAdoptium.Temurin.21.JDK` | OK → unblocks jdtls/kotlin (still need server dist) |
| Julia 1.12.6 | `JuliaLang.Julia` | OK → installed to `%LOCALAPPDATA%\Programs\Julia-1.12.6\bin` |
| Dart SDK 3.12.2 | `Google.DartSDK` | OK |
| Erlang OTP 29.0.4 | `Erlang.ErlangOTP` | OK |

NOT practical: ocaml (choco only 4.0.1 from 2014), haskell (needs GHC bootstrap),
nixd (no native Windows Nix).

## Log-Noise Verification Recipe

The `Skill 'X' maps to slash command /X already claimed by 'X'` warnings (same
name both sides) in errors.log are a benign thread race. Proof:
`scan_skill_commands()` clears `_skill_commands = {}` at scan start, so a clean
single-threaded scan produces 0 warnings and the correct command count:

```bash
cd ~/AppData/Local/hermes/hermes-agent && ./venv/Scripts/python.exe -c \
  "from agent.skill_commands import scan_skill_commands; print(len(scan_skill_commands()))"
# → TOTAL commands: 562 (matches `hermes skills list` count), 0 warnings
```

Also verified: plugin manifests — 108 `plugin.yaml` files parsed with
`yaml.safe_load`, 0 broken (both `plugins/` tree + bundled install plugins tree).

## Other Diagnoses

- `mcp-stderr.log` 8.4MB: repeated `INFO Processing request of type PingRequest`
  every ~3 min = healthy MCP heartbeat, not an error.
- GUI `PermissionError: [WinError 5] .config_*.tmp -> config.yaml` = Windows
  file-lock race: gateway holds config.yaml open while GUI web_server
  `POST /api/model/set` does atomic replace. Durable fix is an upstream update;
  on Windows, prefer `hermes config set` for concurrent writes.
- `hermes update` refused: running Hermes python.exe processes hold .pyd locks.
  Exit with list of PIDs; close desktop/other terminals and re-run. Gateway
  launcher scripts were still refreshed and gateway restarted (exit 0 overall).
