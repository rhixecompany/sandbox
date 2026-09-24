# Rationale for Hermes plugin reconciliation

## Context

Feature 12 in `docs/scope/scope.md` asks for a complete Hermes plugin inventory, state reconciliation, and a Bash entry point that Cursor Agent and Agent can run from Hermes terminal or Git Bash. The user confirmed three policy decisions:

1. Enable plugins that pass doctor and dependency checks.
2. Keep credential gated plugins enabled but inactive.
3. Disable and uninstall incompatible plugins, using exact plugin keys when display names repeat.

The workflow must protect `.env` and credential values. The report must remain useful when an individual plugin fails validation.

## Live evidence

| Command or source | Observed result |
|---|---|
| `hermes plugins --help` | The installed CLI exposes `list`, `enable`, `disable`, `remove`, `doctor`, `compat`, `capabilities`, and `show`. |
| `hermes plugins list --help` | Machine readable inventory is available through `--json`. |
| `hermes plugins enable --help` | Enabling supports `--no-allow-tool-override`, which is selected so reconciliation does not grant built in tool replacement. |
| `hermes plugins doctor --help` | Doctor accepts a plugin path or installed plugin id and supports `--ci` for non zero validation failures. |
| `hermes plugins compat --help` | Compatibility scans an installed plugin directory and exits non zero when removed imports are found. |
| `hermes plugins list --json` | The live inventory contained 159 records. The observed list split was 88 enabled, 23 disabled, and 48 not enabled. |
| `hermes plugins show deepinfra` | The display name resolved to `image_gen/deepinfra`, proving that the list name is not sufficient as a doctor target. |
| `hermes plugins show video_gen/deepinfra` | The video duplicate resolved to `video_gen/deepinfra` and was separately inspectable. |
| `hermes plugins show fal` and `hermes plugins show video_gen/fal` | Image and video records resolved independently, with the video record disabled. |
| `hermes plugins show openrouter` and `hermes plugins show video_gen/openrouter` | Image and video records resolved independently. |
| `hermes plugins show xai` and `hermes plugins show video_gen/xai` | Image and video records resolved independently. |
| `hermes plugins doctor --ci image_gen/deepinfra` | Exit 0, with runtime discovery, manifest parsing, import, and registration passed. |
| `hermes plugins doctor --ci video_gen/fal` | Exit 0 even though the configured status was disabled, so disabled compatible records are candidates for enable. |
| `hermes plugins doctor --ci intelligent_memory` | Exit 1 with unknown hook errors, an example incompatible user plugin. |
| `hermes plugins doctor --ci weather` | Exit 0 with runtime discovery and 13 registered tools. |
| `hermes plugins compat --json` | Exit 1 and reported four removed imports for `home-dashboard`. This is an actionable compatibility finding. |

The live list contains duplicate display names for `deepinfra`, `fal`, `openrouter`, and `xai`. The descriptions identify image and video backends, and the exact key mapping was confirmed with `hermes plugins show` for each family. The script therefore stores both display label and exact key.

The live command also showed that a plugin can be listed with a catalog source while `hermes plugins show` reports a different installed source. The report keeps list source and show source separate and uses the installed show result for mutation safety. It does not silently rewrite the inventory.

## Options considered

### Enable everything listed as disabled

Rejected. A list status is not a compatibility result. The user asked for doctor and dependency checks, and the live doctor already found a failing plugin.

### Resolve plugins only by display name

Rejected. The duplicate backend records demonstrate that this could address the image plugin while silently missing the video plugin or target the wrong directory.

### Write a Python only tool

Rejected for this request. Python is useful for JSON parsing, but the requested operator entry point must run from Hermes terminal and Git Bash. A Bash wrapper with the installed Hermes Python runtime as a parsing helper is more portable for the requested agents.

### Use `jq` as a hard dependency

Rejected. The repository and user environment do not establish `jq` as available. The script uses Python from the Hermes installation for JSON parsing and report aggregation, with `HERMES_BIN` and `REPORT_DIR` injection for tests.

### Mutate while discovering

Rejected. A plugin action based on a partial inventory would make duplicate handling and rollback evidence unreliable. The script completes a dry run first, requires an explicit apply confirmation, and rereads state after actions.

### Remove bundled plugins

Rejected by safety boundary. Bundled plugins are part of the Hermes distribution. The script disables an incompatible bundled plugin and records uninstall as unavailable rather than claiming that distribution code was removed. Non bundled incompatible plugins remain subject to the confirmed disable then remove policy.

## Design derivation

The installed command contract drives the design:

* `hermes plugins list --json` supplies the complete live record set.
* `hermes plugins show` supplies the exact key and installed detail needed for identity resolution.
* `hermes plugins doctor --ci` supplies the local runtime and dependency gate.
* `hermes plugins compat --json` supplies the removed import gate.
* `hermes plugins enable --no-allow-tool-override` supplies the least privilege enable operation.
* `hermes plugins disable` and `hermes plugins remove` supply the confirmed incompatible action path.

The distinction between `active` and `enabled` is derived rather than claimed as a Hermes native status. A plugin is active only when its configured state is enabled, its validation gates pass, and no declared credential gate blocks it. A credential marker is metadata only. The workflow never reads a credential to decide whether it is present.

The action planner is conservative. It skips an unresolved key, unknown compatibility result, uncertain credential classification, or unsafe report redaction. It records the reason and continues to the next item. A failed action prevents an active or removed postcondition claim.

## References

* Hermes Agent documentation, `https://hermes-agent.nousresearch.com/docs`, authoritative product documentation source.
* Installed Hermes CLI help output listed in the live evidence table, source captured on 2026-09-23.
* `docs/scope/scope.md`, feature 12, repository scope source.
* `scripts/hermes_plugin_reconcile.sh`, implementation path defined by the specification after the build phase.
* `docs/specs/0003-hermes-plugin-reconciliation/verify.md`, verification contract for this decision.

No credential values, `.env` content, or provider login output is retained in this rationale.
