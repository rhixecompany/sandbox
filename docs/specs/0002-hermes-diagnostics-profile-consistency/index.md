# 0002 · Hermes diagnostics, repair, and profile consistency

**Status**: Proposed
**Date**: 2026-09-23
**Feature link**: docs/scope/scope.md feature 9 (`Hermes diagnostics, repair, and profile consistency`)
**Build approach**: Tracer Bullet
**Workflow tier**: GA (`/check verify`, `/test`, fresh review, and `/document` required)

## Summary

Create a durable operational diagnostic path for the SandBox repository and Hermes Agent. The path records the requested repository check, Hermes health commands, Hermes log streams, profile inventory, profile aliases, routing, and non secret configuration references. It then supports evidence based repair through Hermes CLI commands, with a dry run and an explicit apply boundary.

This specification defines the decision and the future build. It does not run repair commands or change Hermes profile configuration in this run.

## Requirements

### Diagnostic coverage

* **AC-1**: The diagnostic manifest contains this exact command set in this order: `bun run check`, `hermes doctor`, `hermes doctor --fix`, `hermes status`, `hermes insights`, `hermes logs list`, `hermes logs errors`, `hermes logs desktop`, `hermes logs gateway`, `hermes logs gui`, and `hermes logs agent`. The manifest is versioned and immutable for a run. `hermes doctor --fix` is an apply phase item, not a diagnosis phase subprocess.
* **AC-2**: Each manifest item records the command name, exact arguments, phase, mutating flag, start time, finish time, duration, exit code, outcome, gate, and bounded standard output and standard error evidence. `exit_code` is null when the item has no spawned process, including `not_run`, `blocked`, `skipped`, `unavailable`, `timeout`, and `terminated` outcomes.
* **AC-3**: A failed command does not hide later command results. The run continues after a failure and records the failure as a finding.
* **AC-4**: The runner records platform limits and actual timeout or termination events. It never claims an unbounded background run when the host or delegation layer imposes a limit. The repository working directory and resolved Hermes home are recorded as run context.
* **AC-5**: Output is written as both structured JSON and a readable Markdown report below a date stamped directory in `$HERMES_HOME/plans/`.

### Profile consistency

* **AC-6**: Every profile returned by `hermes profile list` is checked. The inventory includes the profile name, alias, gateway state, model display value, profile directory, and relevant non secret configuration references, with each value linked to its source and normalization rule.
* **AC-7**: The comparison checks the live profile inventory against profile directories, aliases, routing, and non secret configuration references. Missing, extra, stale, duplicate, or conflicting entries are reported with a stable finding code, source, severity, and deterministic disposition.
* **AC-8**: The default profile is treated as the root profile when Hermes uses root identity and memory files. A profile directory is not created or deleted merely to make a table match. Default root paths and non default profile paths are explicit in the source contract.
* **AC-9**: Profile identity files, routing, and shared instructions remain DRY. The diagnostic reports drift without copying identity or secret values into evidence. It does not edit identity, memory, alias, routing, or profile files.

### Repair and approval boundaries

* **AC-10**: Repair planning distinguishes `automatic`, `manual`, `approval_required`, `out_of_scope`, `blocked`, and `not_run` findings.
* **AC-11**: Configuration changes use allowlisted Hermes CLI commands such as `hermes config set` when the command supports the approved field. Direct file edits are not automated by this feature. If the CLI path is unavailable, the finding is manual or out of scope and the runner does not write a file.
* **AC-12**: The repair path has a no write dry run phase and a separate explicit apply dispatcher. The apply phase requires a plan identifier, plan hash, approval record where required, and a fresh pre apply read back. The diagnosis dispatcher rejects every mutating manifest item before spawning it.
* **AC-13**: `hermes doctor --fix` is represented in the diagnosis report with `outcome: not_run`, `gate: approval_required`, and a null exit code. It can run only in the explicit apply dispatcher after its expected changes, allowlist, plan hash, approval, rollback record, and supported preview or diff are reviewed. Without a supported preview or diff that proves the effects are allowlisted, it is `blocked` and is not spawned.
* **AC-14**: Shared Telegram credential warnings use stable finding code `HERMES_SHARED_TELEGRAM_CREDENTIAL` and are approval gates. Approval records contain affected profile identifiers, scope, approver identity, decision, timestamp, expiry, plan identifier, and plan hash. The default decision is denied. The runner does not remove credential references, create credentials, rotate tokens, assign bots, or change routing automatically.
* **AC-15**: Credential values, API keys, tokens, passwords, `.env` contents, and sensitive command arguments are never copied into reports. Encountered values are represented as `[REDACTED]`. Sanitization is fail closed when the redactor cannot determine whether a value is safe.

### Logs and verification

* **AC-16**: Log results are categorized by domain, including MCP, hook, provider, auth, configuration, subagent, tool, chat, session, plugin, rate limit, network, and unknown.
* **AC-17**: Log excerpts are bounded and reviewed for sensitive data before they are written to the report. The report records a source identifier, line and byte bounds, truncation state, and redaction count without exposing raw secrets.
* **AC-18**: After an approved repair, the diagnostic sequence and profile consistency comparison run again. The report links findings before and after the repair without claiming that an unresolved warning disappeared.
* **AC-19**: A GA verification run includes repository checks, focused tests for the runner and comparison logic, a fresh review, and documentation updates.
* **AC-20**: The report uses formal outcome, gate, repair disposition, profile state, and approval decision enums. Summary aggregation maps every enum value without treating approval, not run, unavailable, timeout, or termination as pass.

### Immutable manifest and dispatch boundary

The root manifest constant is `manifest_version: hermes-diagnostics.v1`. Its canonical sequence is:

```json
[
  {"argv":["bun","run","check"],"mutates":false,"name":"bun run check","phase":"diagnosis","sequence":1},
  {"argv":["hermes","doctor"],"mutates":false,"name":"hermes doctor","phase":"diagnosis","sequence":2},
  {"argv":["hermes","doctor","--fix"],"mutates":true,"name":"hermes doctor --fix","phase":"apply","sequence":3},
  {"argv":["hermes","status"],"mutates":false,"name":"hermes status","phase":"diagnosis","sequence":4},
  {"argv":["hermes","insights"],"mutates":false,"name":"hermes insights","phase":"diagnosis","sequence":5},
  {"argv":["hermes","logs","list"],"mutates":false,"name":"hermes logs list","phase":"diagnosis","sequence":6},
  {"argv":["hermes","logs","errors"],"mutates":false,"name":"hermes logs errors","phase":"diagnosis","sequence":7},
  {"argv":["hermes","logs","desktop"],"mutates":false,"name":"hermes logs desktop","phase":"diagnosis","sequence":8},
  {"argv":["hermes","logs","gateway"],"mutates":false,"name":"hermes logs gateway","phase":"diagnosis","sequence":9},
  {"argv":["hermes","logs","gui"],"mutates":false,"name":"hermes logs gui","phase":"diagnosis","sequence":10},
  {"argv":["hermes","logs","agent"],"mutates":false,"name":"hermes logs agent","phase":"diagnosis","sequence":11}
]
```

The runner computes `manifest_hash` as SHA 256 over the UTF 8 bytes of the canonical JSON representation above, with object keys sorted lexicographically, arrays preserved in sequence order, no insignificant whitespace, and no values added from the environment. `name` is a required manifest field and must equal the argv values joined by one ASCII space. The root report and every checkpoint store `manifest_version` and `manifest_hash`. Resume rejects any mismatch.

Canonicalization is `canonical_json_v1`: RFC 8785 JSON Canonicalization Scheme over UTF 8, with no NaN or Infinity, integers represented without leading zeroes, strings escaped by the scheme, Unicode strings normalized to NFC before hashing except that `source_name` is hashed exactly as returned, timestamps rendered as UTC RFC 3339 with exactly three fractional digits, and hash paths rendered with forward slashes, an uppercase Windows drive letter, no dot segments, and no trailing separator. Source path and source identifier display values are not rewritten merely to make them hashable. Golden manifest and plan vectors are part of `verify.md`.

The implementation has two dispatchers. `diagnosis_dispatcher` accepts only manifest items with `phase: diagnosis` and `mutates: false`; it rejects phase or mutating mismatches before spawning a process. It records sequence 3 as `outcome: not_run`, `gate: approval_required`, and `exit_code: null`. `apply_dispatcher` is a separate entry point that accepts only a validated repair plan and the sequence 3 item. It never runs from the diagnosis loop. A test must prove that the diagnosis dispatcher cannot spawn `hermes doctor --fix`, even if the manifest is reordered or a caller passes an apply item.

The apply operation manifest is separate from the diagnosis manifest. Its version is `hermes-repair.v1`. The only non doctor operation allowed by `repair_allowlist_v1` is `config_set_mcp_server_enabled`, with exact argv `['hermes', 'config', 'set', 'mcp.servers.<name>.enabled', '<boolean>']`; `<name>` must be a safe, exact server identifier and `<boolean>` must be the literal `true` or `false`. The operation hash includes the exact post validation argv and the allowlist version. The doctor preview probe invokes `['hermes', 'doctor', '--fix', '--dry-run']` only when `hermes doctor --help` advertises `--dry-run`; if the flag is absent or the output is not a machine readable effect diff, the doctor operation is blocked and not spawned.

Diagnosis reports are append only. The initial sequence 3 command object remains `not_run` with its approval gate. An apply attempt creates an `attempt_id`, `parent_run_id`, `before_report_id`, `after_report_id`, operation name, operation argv hash, plan ID, plan hash, approval ID, effect digest, start and finish times, outcome, gate, and sanitized evidence. A blocked or executed attempt is never written over the initial command object. A successful apply starts a new diagnosis report with a new `run_id`, links it through `parent_run_id` and `after_report_id`, and preserves both reports.

The apply dispatcher acquires one OS exclusive repair lock, rechecks the plan hash, approval envelope, and pre apply snapshot while holding the lock, performs one mutation, reads back the allowlisted state, writes the attempt record, and releases the lock. A lock failure, snapshot mismatch, or effect digest mismatch produces a blocked attempt with no mutation. This is the required time of check and time of use boundary.

### Source contract and normalization

Every report field has one named source or deterministic derivation. Unavailable sources produce an explicit `unavailable` state and a finding, never an inferred value.

| Value | Canonical source | Normalization and failure rule |
|---|---|---|
| Command manifest | Versioned manifest owned by the runner | Preserve order and exact argv. A manifest change requires a schema version change |
| Command result | Subprocess start and finish events | Capture actual exit code, timeout, termination, and bounded sanitized streams |
| Repository working directory | Process working directory resolved at run start | Record the absolute path actually used. Do not substitute the path from documentation |
| Hermes home | Resolved Hermes runtime home used by the CLI | Record the absolute path and existence metadata only. Never copy `.env` or secret values |
| Live profile inventory | `hermes profile list` | Treat the live list as inventory authority. Preserve names exactly after parsing; derive a separate comparison key without changing the source identifier |
| Profile description and model display | `hermes profile show <name>` when supported, otherwise the live list | Record the source command and mark unavailable if the command is unsupported or fails |
| Profile directory | Hermes home profile layout from `hermes-profiles` | `default` maps to the Hermes home root. Every other name maps to `profiles/<name>`. Resolve paths safely and report unexpected paths |
| Profile identity and memory files | Existence, size, and hash metadata for documented `SOUL.md`, `USER.md`, and `MEMORY.md` paths | Read metadata only for comparison. Content is not evidence and is never copied into reports |
| Alias inventory | Alias values in `hermes profile list`, supplemented only by read only wrapper directory metadata | Do not invoke `hermes profile alias <name>` because that command creates a wrapper. A missing alias source produces `unavailable`, not an empty alias set. Duplicate aliases are a conflict |
| Routing | Allowlisted non secret routing fields from `hermes config show` or an explicit profile list field, when supported | Do not read the YAML file directly. A missing field is `not_collected`, not an inferred default |
| Non secret configuration | `hermes config check` plus an allowlisted projection from `hermes config show` with values redacted | Never parse or store `.env` contents. Configuration keys without safe projections are excluded and reported |
| Log evidence | The requested `hermes logs ...` command output and documented log source identifier | Store bounded line and byte ranges, hashes, category, and redacted excerpts only |
| Severity and disposition | Deterministic finding rules in the runner | Codes and precedence are versioned. Unknown cases become `unknown` and `manual` |
| Summary counts | Aggregation over normalized command, profile, log, and repair objects | Counts are derived, not typed by an operator. Null or unavailable values are not counted as pass |
| Redaction totals | Sanitizer events over argv, environment, stdout, stderr, findings, and config projections | Count every replacement and fail closed on uncertain matches |
| Limits | Host process budget, runner timeout, delegation limit, and termination event | Record configured and observed values, including whether a limit was reached |

The allowlists are versioned. `collection_allowlist_v1` contains `profile.name`, `profile.alias`, `profile.gateway_state`, `profile.model_display`, `config.model.name`, `config.model.provider`, `config.fallback_providers[].name`, `config.fallback_providers[].model`, `config.mcp.servers[].name`, `config.mcp.servers[].enabled`, and `config.mcp.servers[].transport`. `routing_allowlist_v1` contains only `routing.profile` and `routing.alias` when those non secret keys are returned by the CLI. `repair_allowlist_v1` contains only `config.mcp.servers.<name>.enabled`, and only when the installed CLI supports `hermes config set` for that exact key. The allowlists are collection identifiers, not permission to mutate; routing and alias fields remain hard denied for repair.

Profile identifiers have three representations. `source_name` is the exact value returned by Hermes and is never rewritten. `comparison_key` is Unicode NFC followed by Unicode case folding and is used only to detect duplicate or case collision findings. `display_label` is a redacted presentation value. Path mapping rejects empty names, `.`, `..`, path separators, control characters, Windows reserved device names (`CON`, `PRN`, `AUX`, `NUL`, `COM1` through `COM9`, and `LPT1` through `LPT9`, case insensitive), names ending in a space or period, and names that resolve outside the expected profile directory. A case collision or Unicode normalization collision is `conflict`; an unsafe identifier receives `HERMES_UNSAFE_PROFILE_IDENTIFIER` and is marked `unavailable` without filesystem access or shell interpolation. No profile identifier is normalized into a different source name.

Profile comparison states are `present`, `missing`, `extra`, `stale`, `duplicate`, `conflict`, `unavailable`, and `not_collected`. Severity precedence is `critical`, `high`, `medium`, `low`, `info`, and `unknown`; a shared credential warning is at least `high` and remains approval required. The live inventory is not overwritten by directory discovery, and the default root exception is applied before extra directory checks.

The field derivation matrix is:

| Report field | Source or derivation | Null, unavailable, and safety rule |
|---|---|---|
| `schema_version` | Checked in report contract constant | Never null. A contract change increments it |
| `run_id` | UTC start clock plus collision suffix selected for the artifact directory | Never guessed. A failed clock or path allocation blocks the run |
| `started_at` and `finished_at` | Runtime clock at run start and finalization | `finished_at` is null until finalization. Both include timezone |
| `manifest_version` and `manifest_hash` | Immutable manifest constant and canonical hash | Never taken from caller input. Mismatch blocks resume and apply |
| `context.repository_cwd` | Resolved process working directory | Never replaced with a documented or expected path |
| `context.hermes_home` | Hermes runtime home resolved for the CLI | Record path metadata only. Failure is `unavailable` and blocks profile comparison |
| `context.host` and `context.process` | Standard runtime host and process metadata | Sanitize values. Omit unsupported values with an explicit unavailable marker |
| `context.delegation` | Delegation response or local runner configuration | Record configured and observed limit. Do not claim unlimited execution |
| `commands[].sequence`, `argv`, `phase`, `mutates` | Manifest object | Immutable. Unsafe caller additions are rejected |
| `commands[].started_at`, `finished_at`, `duration_ms` | Subprocess lifecycle events | Null for not spawned. Duration is derived only from real clock events |
| `commands[].exit_code` | Subprocess result | Null for no process, timeout without an exit code, termination, and unavailable |
| `commands[].outcome` and `gate` | Dispatcher result and result normalization | Use the formal enums below. Never convert a gate or blocked state to pass |
| `commands[].stdout_evidence` and `stderr_evidence` | Sanitized bounded process streams | Empty array when no stream exists, or null with a `field_states` entry when the stream is unavailable. Raw output is never persisted |
| `profiles[]` | `hermes profile list`, optional read only detail, and filesystem metadata | Missing source is unavailable. No profile is synthesized from a directory |
| `profiles[].source_refs` | Source registry entries created for every collected value | A missing source reference is a report contract error and blocks finalization |
| `findings[]` | Deterministic rules over normalized command, profile, log, and repair objects | Unknown rule cases use `unknown` severity and `manual` disposition |
| `sources[]` | Command, filesystem metadata, and CLI read events | Store source kind, command, time, and sanitized metadata only |
| `evidence[]` | Sanitized bounded streams and metadata evidence | Store only canonical sanitized objects. A raw or uncertain object blocks finalization |
| `repair_plan` | No write dry run planner | Always an object. Use `state: not_collected` and field state entries when no repair is proposed. Proposed state never implies applied state |
| `approval` | Supplied approval record or default object created by the runner | Missing, denied, expired, stale, scope mismatch, or hash mismatch is denied |
| `summary` | Deterministic aggregation over all normalized objects | Counts each outcome and gate separately. No unavailable state counts as pass |
| `redactions` | Sanitizer counters over every persisted field | Count only replacements before persistence; removed values are never retained |
| `limits` | Runner configuration, host process events, and delegation events | Missing limit data is unavailable, not unlimited |

The formal enums are `outcome = pass | warn | fail | not_run | blocked | skipped | timeout | terminated | unavailable`, `gate = none | approval_required | hard_deny | capability_unavailable | stale_snapshot`, `disposition = none | report_only | plan_candidate | hard_deny | blocked | applied`, `repair_action = none | propose | apply | rollback | not_supported`, and `approval_decision = denied | approved | revoked | expired | stale`. The `profile_state` and `severity` enums are the values listed above. A timeout or termination may have a real exit code only when the operating system returned one; otherwise it is null and carries a termination reason.

### Evidence and redaction contract

Each evidence object contains `source_id`, `source_command`, `captured_at`, `line_start`, `line_end`, `byte_limit`, `line_limit`, `bytes_observed`, `bytes_captured`, `truncated`, `sha256`, `redaction_count`, and `excerpt`. `capture_limits_v1` is fixed at 32768 bytes and 512 lines per stdout or stderr stream, retaining the first 8192 bytes and 128 lines plus the last 24576 bytes and 384 lines with one truncation marker between them. The runner bounds process streams while they are in memory, sanitizes them before any report, checkpoint, hash, or temporary persistence, and never writes a raw capture. `line_start`, `line_end`, and `bytes_observed` describe the observed stream before redaction; `bytes_captured` and `sha256` are calculated from the canonical sanitized UTF 8 bytes that are persisted. It sanitizes command arguments, environment projections, standard output, standard error, finding evidence, and config projections. Patterns cover API keys, bearer tokens, passwords, cookies, private keys, bot tokens, connection strings, and `.env` style assignments. If sanitization fails or a value is uncertain, the field is replaced with `[REDACTED]`, the raw value is discarded, and the command is marked `blocked`. Checkpoints contain only sanitized normalized results.

### Approval and repair contract

The runner writes a dry run plan with `plan_id`, `plan_hash`, `manifest_hash`, `affected_profile_ids`, an allowlisted command and field list, proposed changes, expected post state, `pre_apply_snapshot_hash`, rollback record, and creation time. `plan_id` is derived from the run ID and the first stable repair sequence, for example `repair.<run_id>.<sequence>`, and is never supplied by an untrusted source. `plan_hash` is SHA 256 over canonical JSON with sorted object keys, preserved array order, UTF 8 encoding, and exactly these inputs: schema version, plan ID, manifest hash, affected profile identifiers, allowlisted changes, expected post state, pre apply snapshot hash, and creation time. The pre apply snapshot is the SHA 256 of the canonical sanitized allowlisted configuration and profile metadata projection read immediately before apply.

The apply entry point requires the caller to pass the plan identifier and hash plus exactly one approval record bound to the same plan. The approval input envelope has `approval_id`, `decision`, `approver`, `scope`, `affected_profile_ids`, `approved_at`, `expires_at`, `plan_id`, `plan_hash`, `effect_digest`, and `reason`. Missing approval defaults to `denied`. Duplicate or malformed envelopes are rejected as `HERMES_APPROVAL_MULTIPLE` or `HERMES_APPROVAL_MALFORMED`; denied, expired, revoked, stale, scope mismatched, plan hash mismatched, and effect digest mismatched inputs use `HERMES_APPROVAL_DENIED`, `HERMES_APPROVAL_EXPIRED`, `HERMES_APPROVAL_REVOKED`, `HERMES_APPROVAL_STALE`, `HERMES_APPROVAL_SCOPE_MISMATCH`, `HERMES_APPROVAL_PLAN_HASH_MISMATCH`, and `HERMES_APPROVAL_EFFECT_MISMATCH` respectively. Every rejection creates a blocked attempt with no subprocess. Approval is valid only when its affected profile identifiers exactly match the plan after canonical sorting, its scope includes every proposed field, its effect digest matches the reviewed sanitized diff, and its expiry is later than the apply start time.

The reviewed effect diff is an array of objects with `path`, `before`, `after`, `source_ref`, and `allowed`. Values are sanitized allowlisted values only. `effect_digest` is SHA 256 of its canonical sanitized JSON and is an input to `plan_hash` and the approval envelope.

The apply dispatcher accepts only allowlisted non secret fields and commands. It rejects profile creation, deletion, recreation, identity or memory edits, alias changes, routing changes, credential reference changes, Telegram bot assignment, provider login, arbitrary file writes, and direct file repair. `hermes doctor --fix` is accepted only when a supported no write preview or machine readable diff proves that every effect is in the allowlist. Otherwise it is `blocked` and remains unspawned. Apply is single writer, idempotent by plan hash, and refuses a stale pre apply snapshot. After each mutation it performs a CLI read back, records the sanitized result, and reruns the diagnostic and consistency stages. Rollback is a new recorded plan using the same CLI boundary, not an automatic secret or file copy. A manual emergency file edit is outside this runner and cannot bypass the hard deny policy.

### Durability and execution context

The runner creates a deterministic date stamped directory with a collision suffix when needed. It writes a sanitized checkpoint record containing `run_id`, `schema_version`, `manifest_version`, `manifest_hash`, `sequence`, `normalized_result_hash`, `repository_cwd`, `hermes_home`, `report_path`, `recorded_at`, and `commit_marker`. `normalized_result_hash` is SHA 256 of canonical sanitized JSON containing the sequence, name, phase, mutates flag, outcome, gate, exit code, termination reason, evidence hashes, finding codes, and repair disposition; volatile `recorded_at` and `commit_marker` are excluded. `commit_marker` is the ASCII string `checkpoint-v1:` followed by SHA 256 of the canonical sanitized checkpoint record with the marker field omitted. A checkpoint is committed by writing the sanitized record to a temporary sibling opened with exclusive creation, flushing and syncing the file, atomically replacing the checkpoint path, then writing the marker file with exclusive creation, flushing and syncing it, and finally syncing the parent directory. A record without a matching marker is corrupt and is never resumed. No raw stdout, stderr, argv, environment, or config value may enter the temporary sibling.

A resume operation requires an explicit `--resume <run_id>` selection. It reads the checkpoint sequence, rejects corrupt, partial, duplicate, or missing commit markers, verifies the exact manifest hash, schema version, repository working directory, Hermes home, and report path, and does not rerun committed items. An interrupted item is marked `terminated` or `timeout` and is rerun only when the operator starts a new explicit resume after the checkpoint validates. Apply writes an independent `apply-<attempt_id>.json` checkpoint using `hermes-repair.v1`, the operation hash, plan hash, approval ID, pre apply snapshot hash, and post read back hash; it never resumes from a diagnosis checkpoint. Apply resume requires revalidating the plan hash, approval, effect digest, and pre apply snapshot while holding the repair lock. Timeout and termination results include the host reason, elapsed time, and process tree cleanup result.

## Scope and non goals

In scope:

* A repeatable diagnostic runner and report contract.
* The requested command inventory and ordering.
* Profile, alias, routing, and non secret configuration comparison.
* Log triage and redaction boundaries.
* A dry run and explicit apply boundary for supported Hermes CLI repairs.
* Evidence, rollback, verification, and documentation.

Out of scope for this run:

* Running `hermes doctor --fix` or any repair command.
* Creating, deleting, or recreating profiles.
* Removing shared credentials or assigning Telegram bots.
* Reading or modifying `.env` files.
* Logging into external providers or changing provider credentials.
* Adding an unrequested `hermes security audit` command to the required command set. It may be proposed later as an optional extension.

The future repair implementation also has a hard deny policy for profile creation, deletion, recreation, identity or memory edits, alias changes, routing changes, credential reference changes, Telegram bot assignment, provider login, and arbitrary file writes. Only explicitly allowlisted non secret configuration fields may be candidates for an approved repair plan.

## Decision

Use one durable sequential diagnostic runner with a fixed command manifest and continue on failure. It writes one record per command, then writes a summary report. Profile consistency is a separate comparison stage that consumes the live profile inventory and non secret filesystem metadata. Repair is a second explicit stage with a dry run and an apply boundary.

The runner is sequential because command ordering makes failures easier to attribute, reduces concurrent writes to Hermes logs and configuration, and preserves the exact evidence trail. Parallel execution would shorten wall time but would make log attribution and repair sequencing less reliable. Stop on first failure would reduce noise but would hide independent failures and violate the requested full sweep.

**Implementation skills**: `hermes-diagnostic-repair`, `hermes-system-maintenance`, `log-analysis-and-triage`, `hermes-profiles`, `systematic-debugging`, `verification-before-completion`.

## Interfaces and data contract

The report has a JSON root object with these fields:

| Field | Meaning |
|---|---|
| `schema_version` | Stable report contract version |
| `manifest_version` | Immutable command manifest version |
| `manifest_hash` | SHA 256 of the canonical command manifest |
| `report_id` | Immutable report identifier, unique for the initial or post apply report |
| `run_id` | Real date and time identifier generated at run start |
| `started_at` | Run start time with timezone |
| `finished_at` | Run finish time with timezone |
| `context` | Resolved repository path, Hermes home, host, process, and delegation limits |
| `field_states` | Explicit state and reason for every null field |
| `commands` | Ordered command result objects, including phase and nullable exit code |
| `profiles` | Profile comparison result objects with canonical sources and states |
| `findings` | Normalized issues with stable code, category, severity, evidence, and disposition |
| `sources` | Sanitized source registry entries referenced by command, profile, finding, and evidence objects |
| `evidence` | Deduplicated sanitized evidence objects |
| `repair_plan` | Proposed actions with plan identifier, hash, allowlist, approval state, expected post state, and rollback record |
| `approval` | Default denied approval metadata bound to a repair plan, without secret values |
| `attempts` | Append only apply attempt records linked to before and after reports |
| `summary` | Counts for pass, warn, fail, skipped, blocked, approval required, not run, and unavailable results |
| `redactions` | Count and reason for redactions, never the removed value |
| `limits` | Host, process, delegation, and capture limits observed during the run |

Each item in `commands` has `sequence`, `name`, `argv`, `phase`, `mutates`, `started_at`, `finished_at`, `duration_ms`, `exit_code`, `outcome`, `gate`, `termination_reason`, `stdout_evidence`, `stderr_evidence`, `source_refs`, and `redaction_count`. The `outcome` enum is `pass`, `warn`, `fail`, `not_run`, `blocked`, `skipped`, `timeout`, `terminated`, or `unavailable`. `gate` is `none`, `approval_required`, `hard_deny`, `capability_unavailable`, or `stale_snapshot`. `termination_reason` is `none`, `timeout`, `operator_interrupt`, `process_exit`, `process_tree_cleanup_failed`, `host_limit`, or `unknown`; it is `none` for a completed command and `unknown` only when the host cannot provide a more precise reason.

Each profile item has `source_name`, `comparison_key`, `display_label`, `alias`, `gateway_state`, `model_display`, `directory_state`, `identity_file_metadata`, `routing_state`, `config_state`, `credential_warning`, `source_refs`, and `findings`. Each finding has `code`, `category`, `severity`, `state`, `source_refs`, `evidence_refs`, `disposition`, and `repair_action`. `state` is `open`, `resolved`, `suppressed`, `unavailable`, or `not_collected`; `disposition` is `none`, `report_only`, `plan_candidate`, `hard_deny`, `blocked`, or `applied`; `repair_action` is `none`, `propose`, `apply`, `rollback`, or `not_supported`. Each source registry entry has `source_id`, `source_kind`, `source_command`, `captured_at`, and sanitized metadata. `source_kind` is `command`, `filesystem_metadata`, `config_projection`, `profile_inventory`, `profile_detail`, `approval`, `plan`, or `derived`. The approval object has `approval_id`, `decision`, `approver`, `scope`, `affected_profile_ids`, `approved_at`, `expires_at`, `plan_id`, `plan_hash`, `effect_digest`, and `reason`; `decision` defaults to `denied`.

Summary aggregation stores `outcome_counts` keyed by every `outcome` enum, `gate_counts` keyed by every `gate` enum, `repair_disposition_counts` keyed by every repair disposition, and `profile_state_counts` keyed by every profile state. `pass_count` is exactly the count of `outcome: pass`. `timeout`, `terminated`, `unavailable`, `blocked`, `not_run`, `skipped`, and every non none gate remain visible in their own counts and never contribute to `pass_count`.

The Markdown report mirrors the JSON summary, lists command outcomes in order, lists profile drift without secrets, groups log findings by category, and ends with proposed repair actions, approval state, rollback, and unresolved blockers. The JSON report is authoritative; Markdown is a bounded presentation and never a source for resume or repair.

## Build plan

The Tracer Bullet build creates one thin end to end path before adding deeper remediation.

1. **Report contract and command manifest**
   Define the versioned report schema, field derivation matrix, versioned allowlists, exact command manifest, canonical manifest hash, phase and exit code handling, bounded output capture, redaction rules, checkpoint format, and date stamped artifact path.
2. **Sequential runner**
   Resolve and record the working directory and Hermes home, use the diagnosis dispatcher only for read only items, record `hermes doctor --fix` as `not_run` with an `approval_required` gate, continue after failures, flush sanitized checkpoints, and emit JSON plus Markdown.
3. **Profile comparison**
   Parse the live `hermes profile list` inventory, use documented `hermes profile show` when supported, use list values and read only wrapper metadata for aliases, map each profile to directory and identity metadata with unsafe identifier rejection, compare the versioned non secret configuration and routing projection, and emit stable drift findings.
4. **Repair boundary**
   Add no write dry run planning, canonical plan serialization and hashing, explicit apply dispatcher, Hermes CLI allowlist, default denied approval state, exact affected profile binding, supported preview requirement, rollback recording, post apply read back, idempotency, stale snapshot rejection, and protection for shared credentials and profile identity.
5. **Verification and documentation**
   Add focused tests for source derivation, manifest immutability, diagnosis dispatcher denial, redaction before persistence, checkpoints, resume, approval guards, plan hash binding, unsafe profile identifiers, outcome aggregation, and profile comparison. The complete AC-1 through AC-20 matrix, formal JSON Schema, and golden vectors are maintained in `verify.md` and map to controller tasks `HERMES-001` through `HERMES-005`. Run the GA verification tail, document operation and failure handling, and update the scope status only after evidence passes.

## Consequences

Positive consequences:

* A complete command result remains available even when one command fails.
* Profile drift and shared credential conflicts become visible without exposing credential values.
* Repair actions have a review point and a rollback note before changing Hermes state.
* The JSON contract can support later trend analysis and CI reporting.

Tradeoffs:

* Sequential execution takes longer than parallel execution.
* Bounded excerpts can omit context, so the report must preserve source paths and support a follow up read.
* The design requires a real profile inventory at each run. It cannot prove an external credential is valid without a provider operation.
* Direct file repair is not automated by this feature. If the CLI cannot perform a safe supported change, the runner records a manual or out of scope finding and stops before writing.

## Follow up

* Decide whether to add `hermes security audit` as an optional or required command after the first implementation is verified.
* Decide whether profile consistency should later become a scheduled health check.
* If shared Telegram credentials must be separated, handle bot ownership and credential setup as a separate approved operations task.
* Add a trend view only after the report contract remains stable across several real runs.

## Plan coupling

The deferred Hermes architecture tasks are tracked in `$HERMES_HOME/plans/architect-fallow-coderabbit-20260923-191428.md`, Phase 1 tasks `TASK-004` through `TASK-007`. The future implementation map in that controller uses `HERMES-001` through `HERMES-005` and maps the acceptance matrix in `verify.md` to implementation artifacts and tests. That controller plan links back to this `index.md`, `rationale.md`, and `verify.md` set and keeps Hermes implementation deferred while Fallow and CodeRabbit proceed through their own specifications and plans.

## Rationale

See `rationale.md` for current evidence, options considered, documentation sources, unavailable supporting files, and the reason for the selected architecture.
