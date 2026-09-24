# 0003 · Hermes plugin reconciliation and agent script

**Status**: Proposed
**Date**: 2026-09-23
**Feature link**: `docs/scope/scope.md` feature 12 (`Hermes plugin reconciliation and agent script`)
**Build approach**: Tracer Bullet
**Workflow tier**: GA (`/check verify`, `/test`, fresh review, and `/document` required)

## Summary

Create one portable Bash command for Hermes terminal and Git Bash. It inventories every installed Hermes plugin, resolves exact plugin keys, runs the installed plugin doctor and compatibility checks, classifies configured and runtime state, writes a redacted dry run report, and applies only the user confirmed policy.

The script treats `enabled` and `active` as different values. Hermes reports configured state. The script derives runtime state from doctor, dependency, compatibility, and credential gates. A credential gated plugin may be enabled but remains inactive until its external requirement is available. The script never reads `.env` or credential values.

## Requirements

### Inventory and identity

* **AC-1**: The inventory uses live `hermes plugins list --json` output and records every returned item. The pre change baseline is verified from the live command, not from a checked in fixture.
* **AC-2**: Each item records display name, version, list source, configured status, exact plugin key, key resolution result, and source command references. A missing or ambiguous key is recorded and is not mutated.
* **AC-3**: Duplicate display names are separate records. The image and video backends use their exact keys, such as `image_gen/deepinfra` and `video_gen/deepinfra`, rather than a display name alone. The implementation must never silently collapse duplicate records.

### Compatibility and state

* **AC-4**: The script runs `hermes plugins doctor --ci <exact-key>` for every resolvable item. This is the doctor and dependency gate because the installed command validates manifest parsing, imports, runtime contracts, and registration. The real exit code is recorded.
* **AC-5**: The script runs `hermes plugins compat --json <resolved-plugin-path>` when the doctor output provides a path. A global compatibility result is retained as a fallback when a per plugin path is unavailable. A removed import, unresolved target, doctor failure, or unavailable compatibility probe is never treated as a pass.
* **AC-6**: The script reports `configured_state` as `enabled` or `disabled`. Hermes `not enabled` is normalized to `disabled` with its original value preserved. It reports `runtime_state` as `active` only when the configured state is enabled, doctor and compatibility gates pass, and no credential gate blocks use. All other installed items are `inactive`.
* **AC-7**: Credential gating is derived only from non secret plugin metadata and doctor or show text, using bounded markers for required keys, tokens, secrets, credentials, login, or authentication. The script records `credential_gate: declared`, `none`, or `unknown`. It never probes, prints, hashes, or stores a credential value. An unknown gate is conservative and blocks activation.
* **AC-8**: The report distinguishes compatible, incompatible, blocked, unavailable, and credential gated. Missing optional external credentials do not make plugin code incompatible. They keep a plugin enabled and inactive when the user policy allows it.

### Reconciliation and safety

* **AC-9**: A dry run is the default and performs no enable, disable, remove, install, login, provider, profile, alias, routing, config, or credential mutation. It writes a proposed action for every item.
* **AC-10**: A compatible plugin that is disabled or not enabled is proposed for `hermes plugins enable <exact-key> --no-allow-tool-override`. A compatible non credential gated plugin is classified active after the post action doctor and verification pass.
* **AC-11**: A compatible credential gated plugin is proposed for enable when needed, but its runtime state remains inactive and the reason is recorded. Enabling never grants a built in tool override and never supplies a credential.
* **AC-12**: An incompatible non bundled plugin is proposed for disable when currently enabled, then removal by its exact removable plugin key. The disable result is recorded before the remove attempt. An incompatible bundled plugin is proposed for disable, while uninstall is recorded as unavailable because bundled code is owned by the Hermes distribution. The report never claims bundled removal occurred.
* **AC-13**: Apply mode recomputes the live plan, requires `--apply --confirm-uninstall` or an explicit `PLUGIN_RECONCILE_ASSUME_YES=1`, uses a single writer lock, continues after an individual action failure, and records every command exit code. The dry run is not trusted as an apply plan without recomputation.
* **AC-14**: Apply uses only `hermes plugins enable`, `hermes plugins disable`, and `hermes plugins remove` with exact keys. It does not edit Hermes YAML, plugin files, profile files, aliases, routing, `.env`, or credential stores.
* **AC-15**: After apply, the script rereads `hermes plugins list --json`, checks each requested postcondition with exact keys, reruns compatibility checks, and records unresolved failures. Removal is verified by absence or a verified not found result, not by a successful command alone.

### Evidence and portability

* **AC-16**: JSON, CSV, and Markdown reports contain bounded, sanitized evidence. Standard output and standard error are redacted before persistence. Sensitive assignments, bearer values, private key bodies, connection strings, and `.env` style secret values become `[REDACTED]`. Raw command output never enters a report or checkpoint.
* **AC-17**: The report contains the live inventory count, configured state counts, runtime state counts, compatibility counts, action counts, command results, and a final verification section. Counts are calculated from records, not typed by an operator.
* **AC-18**: The script runs on Bash in Hermes terminal and Git Bash on Windows, and on ordinary POSIX Bash when `hermes` is available. `HERMES_BIN` and `REPORT_DIR` are supported for isolated tests. It uses no Bash feature newer than Bash 4.2 without a documented failure.
* **AC-19**: `bash -n scripts/hermes_plugin_reconcile.sh` and `bash scripts/hermes_plugin_reconcile.sh --self-test` pass without touching live Hermes state. The self test uses a mock Hermes command and proves duplicate key handling, credential inactive state, incompatible removal planning, redaction, failure continuation, and postcondition verification.
* **AC-20**: The script has stable non zero exit codes for invalid arguments, inventory failure, unresolved required identity, blocked apply, action failures, and verification failures. A non zero command inside the audit does not stop later records, but a failed final gate is visible to the caller.

## Scope and non goals

In scope:

* Live inventory of every installed plugin.
* Exact key resolution, including duplicate display names.
* Doctor, dependency, and compatibility evidence.
* Configured state and derived active or inactive state.
* Credential gate classification without reading credentials.
* Dry run planning, explicit apply, removal for compatible plugin sources, and final verification.
* A portable Bash script, an offline mock self test, a specification, and operator documentation in the script help and report.

Out of scope:

* Reading or changing `.env`, API keys, tokens, passwords, cookies, private keys, or credential stores.
* Provider login, credential setup, profile creation or deletion, alias or routing changes, Hermes configuration edits, or direct plugin file edits.
* Granting built in tool override permissions.
* Automatically reinstalling a removed plugin or restoring a prior version.
* Treating a bundled plugin as removable when the installed CLI does not support that operation.
* Calling a plugin to test a paid external service. Doctor and dependency checks remain local and contract based.

## Decision

Use a single Bash script with a Tracer Bullet path that completes one thin end to end flow first:

```text
live inventory → exact key map → doctor and compatibility probes → state map → redacted report → explicit actions → reread and verify
```

The script uses Hermes CLI commands as the only mutation boundary. Bash owns orchestration, continuation, locking, report placement, and portable command handling. Python from the installed Hermes environment is used only for JSON parsing and deterministic report aggregation, so the script does not depend on `jq` or repository packages.

The primary compatibility rule is doctor success plus compatibility success. The primary runtime rule is enabled plus compatible plus no credential gate. Unknown identity, unknown compatibility, unknown dependency, or uncertain redaction is conservative and blocks mutation. The user confirmed the reconciliation policy: enable compatible plugins, keep credential gated plugins enabled but inactive, and disable and uninstall incompatible removable plugins. The exact key, not the display label, is always passed to the CLI.

**Implementation skills**: `plugin-health-check`, `system-commandline-cli`, `bash-files`, `hermes-system-maintenance`, `verification-before-completion`, `systematic-debugging`, `writing-plans`.

## State model

| Configured state | Runtime state | Meaning |
|---|---|---|
| `enabled` | `active` | Doctor, dependency, and compatibility gates pass and no credential gate blocks use |
| `enabled` | `inactive` | Credential gated, unresolved, unavailable, incompatible, or blocked |
| `disabled` | `inactive` | Installed and not enabled |
| `not enabled` | `inactive` | Original Hermes value is preserved and normalized configured state is disabled |
| absent after removal | `unavailable` | Removal was verified by a new live inventory |

Compatibility is a gate, not a user preference. A plugin is compatible only when its exact key resolves, doctor exits zero, the compatibility scan exits zero, and no hard dependency or safety finding blocks loading. Credential gating changes runtime state, not compatibility.

## Exact key resolution

The source of truth is the live list followed by `hermes plugins show <display-name>`. The resolver stores the `Key:` field returned by Hermes. When the display name occurs more than once, each occurrence is resolved independently. Known backend families are mapped by their non secret descriptions to `image_gen/<name>` and `video_gen/<name>`, then each candidate is confirmed with `hermes plugins show <exact-key>`. If a candidate cannot be confirmed, the item is `unavailable` and no action is proposed.

The resolver preserves the display name exactly for reporting. It does not use a normalized name as a mutation target. It records a stable comparison label separately for duplicate detection. Duplicate records with the same exact key are a conflict and are skipped.

## Credential gate

The script never tests a credential value. It checks only bounded metadata returned by `hermes plugins show`, the plugin doctor, and the inventory description. A declared marker includes a required API key, token, secret, credential, login, OAuth, or authentication phrase. The report stores the marker class, not the source line when that line could include a value. If the text is uncertain, the state is `unknown` and activation is blocked. A credential gated plugin is not removed solely because the credential is unavailable.

## Action policy

| Result | Current state | Action | Final runtime state |
|---|---|---|---|
| compatible, no credential gate | disabled | enable with no tool override | active after verification |
| compatible, no credential gate | enabled | none | active after verification |
| compatible, credential gated | disabled | enable with no tool override | inactive, credential gated |
| compatible, credential gated | enabled | none | inactive, credential gated |
| incompatible, removable source | enabled | disable, then remove | unavailable after verification |
| incompatible, removable source | disabled | remove | unavailable after verification |
| incompatible, bundled source | enabled | disable, report uninstall unavailable | inactive, bundled incompatible |
| unresolved or unknown | any | no mutation, report blocker | inactive or unavailable |

A failed disable prevents the corresponding remove call. A failed enable prevents an active claim. The script continues with the next item and returns a failed final gate when any requested action or postcondition fails.

## Report contract

Each run writes `plugin-reconciliation.json`, `plugin-reconciliation.csv`, and `plugin-reconciliation.md` under `REPORT_DIR`. The report contains:

* `schema_version`, `started_at`, `finished_at`, `repository_cwd`, `hermes_home`, and script version.
* `inventory_source`, its exit code, and the original live count.
* One record per live list entry with display name, original status, normalized configured state, source, version, exact key, resolution state, doctor exit code, compatibility exit code, credential gate, compatibility result, runtime state, proposed action, action result, and postcondition.
* Aggregated counts derived from those records.
* Bounded redacted command evidence and redaction counts.
* The apply confirmation mode and lock result, with no secret values.

Evidence text is capped at 4096 bytes per command and compacted to one report line. The script reports truncation. A report is not considered safe if redaction fails.

## Build plan

### Milestone 1: Walking inventory

Create the script entry point, argument parser, live list capture, Python JSON parser, report directory handling, and `--inventory`. Verify count and state totals against live output.

### Milestone 2: Exact identity and gates

Add `show` based key resolution, duplicate backend mapping, doctor probes, compatibility probes, bounded redaction, and state derivation. Verify exact keys for duplicate names and continue after failed probes.

### Milestone 3: Dry run and self test

Add deterministic action planning, JSON, CSV, and Markdown reports, mock Hermes self tests, shell syntax checks, and tests for credential inactive behavior and incompatible removal planning. Verify dry run has zero mutation calls.

### Milestone 4: Explicit apply and verification

Add the lock, confirmation gate, enable, disable, and remove calls, then reread live inventory and verify postconditions. Verify bundled removal is never claimed and action failures remain visible.

### Milestone 5: Operator handoff

Document command examples in the script help, link the script from the scope and spec, run repository quality checks relevant to touched files, and preserve the real live report path and exit codes without storing secrets.

## Consequences

This design adds one operational script and its tests, but avoids a new Python package or provider dependency. A full audit can take longer than a list command because it runs one doctor and one compatibility probe per resolvable plugin. That cost is deliberate because a display name alone cannot prove the exact plugin identity.

The script may leave an incompatible bundled plugin installed because the installed CLI treats bundled code as distribution owned. It makes that limit explicit instead of deleting Hermes supplied code. Non bundled removal is irreversible from this workflow, so the plan records source and version metadata and never auto reinstalls.

`active` is a report state, not a new Hermes CLI state. Hermes still reports `enabled`, `disabled`, or `not enabled`. The report makes the distinction visible without pretending to control external credentials or paid service readiness.

## Follow up

* If Hermes exposes a machine readable credential declaration or a safe bundled uninstall operation, add it as a versioned gate before expanding the script.
* If the installed plugin command gains a batch doctor or dependency command, prefer it while preserving per key evidence.
* Revisit incompatible bundled plugins only through a separate Hermes distribution maintenance decision.

## Rationale

See `rationale.md` for live CLI evidence, option comparison, and source notes.
