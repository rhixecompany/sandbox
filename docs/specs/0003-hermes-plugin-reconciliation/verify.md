# Verification contract for Hermes plugin reconciliation

This contract verifies the proposed plugin reconciliation behavior. It does not authorize a mutation by itself. Apply remains gated by the live dry run, explicit confirmation, and the script's recomputation of the action plan.

## Required commands

| Gate | Command | Pass condition |
|---|---|---|
| Shell syntax | `bash -n scripts/hermes_plugin_reconcile.sh` | Exit 0 |
| Help | `bash scripts/hermes_plugin_reconcile.sh --help` | Exit 0 and documents inventory, dry run, apply, verify, and self test |
| Offline behavior | `bash scripts/hermes_plugin_reconcile.sh --self-test` | Exit 0 and reports all mock assertions passed |
| Live inventory | `bash scripts/hermes_plugin_reconcile.sh --inventory` | Exit 0, or a recorded live CLI blocker with no mutation |
| Live dry run | `bash scripts/hermes_plugin_reconcile.sh --dry-run` | No enable, disable, remove, install, login, provider, config, profile, or credential operation is called |
| Apply | `bash scripts/hermes_plugin_reconcile.sh --apply --confirm-uninstall` | Only after the dry run is reviewed; every action has an exit code and postcondition |
| Postcondition | `bash scripts/hermes_plugin_reconcile.sh --verify` | Live state is reread and requested postconditions are checked |
| Repository quality | `bunx markdownlint-cli2 --config .markdownlint-cli2.jsonc docs/scope/scope.md docs/specs/0003-hermes-plugin-reconciliation/*.md` | Exit 0 |
| Whitespace | `git diff --check` | Exit 0 |

## Acceptance matrix

| ID | Fixture or live check | Expected result |
|---|---|---|
| AC-1 | Mock list with multiple statuses | Every input record appears in the report |
| AC-2 | Mock show output with a `Key:` line | Exact key is stored and used as the target |
| AC-3 | Image and video duplicates for `deepinfra`, `fal`, `openrouter`, and `xai` | Eight independent records are retained and addressed by exact keys |
| AC-4 | Doctor returns zero | Doctor gate passes |
| AC-5 | Compatibility returns one with a finding | Record is incompatible and not enabled |
| AC-6 | Enabled plus all gates pass | Runtime state is active |
| AC-7 | Credential marker appears in metadata | Plugin remains enabled or is enabled, but runtime state is inactive |
| AC-8 | Doctor returns non zero | Record is incompatible or blocked, never active |
| AC-9 | Dry run mock | Mutation call count is zero |
| AC-10 | Compatible disabled plugin | Enable action uses `--no-allow-tool-override` |
| AC-11 | Credential gated disabled plugin | Enable may be proposed, active state is not claimed |
| AC-12 | Incompatible removable plugin | Disable precedes remove, and remove is verified |
| AC-13 | Apply without confirmation | No destructive action is called and the run is blocked |
| AC-14 | Mock config and profile mutation commands | No such command is emitted |
| AC-15 | Post list omits removed plugin | Removal postcondition passes |
| AC-16 | Mock output containing secret shaped assignments | Persisted report contains `[REDACTED]` and not the value |
| AC-17 | Inventory and action aggregation | Counts equal programmatic record counts |
| AC-18 | Git Bash path and injected `HERMES_BIN` | Script runs without repository package dependencies |
| AC-19 | Self test and shell syntax | Both exit zero |
| AC-20 | One failed action followed by a passing action | Later item runs, final gate remains non zero |

## Live evidence checks

The baseline before apply must be captured from a new `hermes plugins list --json` call. The known baseline from the earlier live call was 159 records, 88 enabled, 23 disabled, and 48 not enabled. The final report must recalculate these values rather than copying them.

The duplicate key check must include:

```text
image_gen/deepinfra
video_gen/deepinfra
image_gen/fal
video_gen/fal
image_gen/openrouter
video_gen/openrouter
image_gen/xai
video_gen/xai
```

The compatibility report must not leave `home-dashboard` active while its removed imports remain. The doctor failure for `intelligent_memory` must remain visible as a real incompatible result unless the live plugin changes before the run.

## Report safety checks

* Report files contain no `.env` content.
* Report files contain no API key, token, password, cookie, private key body, connection string, or bearer value.
* Exact plugin keys, versions, source labels, exit codes, and reason codes remain visible.
* All evidence excerpts are bounded and sanitized before hashing or writing.
* An uncertain redaction result blocks the affected record.

## Apply boundary

The live apply gate requires all of the following:

1. The current live inventory was captured immediately before planning.
2. The dry run report is present and readable.
3. The caller supplied `--apply --confirm-uninstall`, or explicitly set `PLUGIN_RECONCILE_ASSUME_YES=1` in the process environment.
4. A single writer lock was acquired.
5. The action target is an exact key that was revalidated by `hermes plugins show`.
6. The action is one of the allowlisted plugin commands.
7. The postcondition inventory is reread after actions.

The workflow never restores removed plugins automatically. Recovery is an explicit new plan using the recorded non secret source and version metadata.
