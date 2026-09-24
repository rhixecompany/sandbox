# Verification contract for Hermes diagnostics

This file is the executable verification companion to `index.md`. It defines the report schema, canonical serialization, golden vectors, and the acceptance matrix. It is part of the proposed architecture and does not authorize running a repair command during the architecture phase.

## Contract versions

| Contract | Value |
|---|---|
| Report schema | `hermes-diagnostics-report.v1` |
| Diagnosis manifest | `hermes-diagnostics-manifest.v1` |
| Repair operation manifest | `hermes-repair.v1` |
| Collection allowlist | `collection_allowlist_v1` |
| Routing allowlist | `routing_allowlist_v1` |
| Repair allowlist | `repair_allowlist_v1` |
| Canonical JSON | `canonical_json_v1` |
| Checkpoint | `checkpoint-v1` |
| Hash | SHA 256, lowercase hexadecimal, 64 characters |

## Null and unavailable representation

A field has its declared JSON value when it is available. A field is `null` only when it is not applicable, unavailable, not collected, or redacted. Every null field has an entry in the root `field_states` object keyed by its RFC 6901 JSON Pointer. The entry has `state`, `reason_code`, and `source_refs`.

`state` is one of `not_applicable`, `unavailable`, `not_collected`, or `redacted`. `reason_code` is a stable uppercase code and `source_refs` is an array of source IDs. A missing optional object is not interpreted as an empty result. An empty array means the source was successfully collected and contained no values. This distinction is required for profile, routing, configuration, and command results.

## Canonical serialization and golden vectors

`canonical_json_v1` uses RFC 8785 JSON Canonicalization Scheme over UTF 8. Keys are sorted by the scheme, arrays preserve their declared order, strings use the scheme's escaping, and NaN and Infinity are rejected. Unicode values are normalized to NFC before hashing except `source_name`, which is hashed exactly as returned by Hermes. Timestamps use UTC RFC 3339 with exactly three fractional digits, for example `2026-09-23T19:00:00.000Z`. Hash paths use forward slashes, an uppercase Windows drive letter, no dot segments, and no trailing separator. Source display values are never rewritten merely to make them hashable.

The following bytes are exact UTF 8 bytes with no final newline:

```text
[{"argv":["hermes","doctor"],"mutates":false,"name":"hermes doctor","phase":"diagnosis","sequence":2}]
```

The expected SHA 256 is:

```text
7171886c677a8e97db3395ffc8cc45ff5cb58ed623edde0ffe2acf55c7c4d14e
```

The following repair plan bytes are also exact UTF 8 bytes with no final newline:

```text
{"affected_profile_ids":["default"],"allowlist_version":"repair_allowlist_v1","created_at":"2026-09-23T19:00:00.000Z","effect_digest":"0000000000000000000000000000000000000000000000000000000000000000","expected_post_state":{"config.mcp.servers.example.enabled":true},"manifest_hash":"1111111111111111111111111111111111111111111111111111111111111111","plan_id":"repair.run-001.3","pre_apply_snapshot_hash":"2222222222222222222222222222222222222222222222222222222222222222","schema_version":"hermes-repair.v1"}
```

The expected SHA 256 is:

```text
6e6dc95bc1abe01c2d4929ba0ff250e744248d2b40389adcd8ba1537fc3892bc
```

The implementation must test both vectors and must fail closed if its serializer produces another byte sequence.

## Formal JSON Schema

The implementation must validate every JSON report against this Draft 2020-12 schema before publishing it. A report that fails validation is a blocked run and is not presented as a passing diagnostic.

```json
{
  "$schema": "https://json-schema.org/draft/2020-12/schema",
  "$id": "https://hermes-agent.nousresearch.com/schemas/hermes-diagnostics-report.v1.json",
  "title": "Hermes diagnostics report v1",
  "type": "object",
  "additionalProperties": false,
  "required": ["schema_version", "manifest_version", "manifest_hash", "report_id", "run_id", "started_at", "finished_at", "context", "field_states", "commands", "profiles", "findings", "sources", "evidence", "repair_plan", "approval", "attempts", "summary", "redactions", "limits"],
  "properties": {
    "schema_version": {"const": "hermes-diagnostics-report.v1"},
    "manifest_version": {"const": "hermes-diagnostics-manifest.v1"},
    "manifest_hash": {"$ref": "#/$defs/hash"},
    "report_id": {"type": "string", "minLength": 1, "pattern": "^[A-Za-z0-9._:-]+$"},
    "run_id": {"type": "string", "minLength": 1, "pattern": "^[A-Za-z0-9._:-]+$"},
    "started_at": {"$ref": "#/$defs/timestamp"},
    "finished_at": {"$ref": "#/$defs/timestamp"},
    "context": {"$ref": "#/$defs/context"},
    "field_states": {"type": "object", "additionalProperties": {"$ref": "#/$defs/fieldState"}},
    "commands": {"type": "array", "minItems": 11, "items": {"$ref": "#/$defs/command"}},
    "profiles": {"type": "array", "items": {"$ref": "#/$defs/profile"}},
    "findings": {"type": "array", "items": {"$ref": "#/$defs/finding"}},
    "sources": {"type": "array", "items": {"$ref": "#/$defs/source"}},
    "evidence": {"type": "array", "items": {"$ref": "#/$defs/evidence"}},
    "repair_plan": {"$ref": "#/$defs/repairPlan"},
    "approval": {"$ref": "#/$defs/approval"},
    "attempts": {"type": "array", "items": {"$ref": "#/$defs/attempt"}},
    "summary": {"$ref": "#/$defs/summary"},
    "redactions": {"type": "array", "items": {"$ref": "#/$defs/redaction"}},
    "limits": {"$ref": "#/$defs/limits"}
  },
  "$defs": {
    "hash": {"type": "string", "pattern": "^[0-9a-f]{64}$"},
    "timestamp": {"type": "string", "pattern": "^[0-9]{4}-[0-9]{2}-[0-9]{2}T[0-9]{2}:[0-9]{2}:[0-9]{2}\\.[0-9]{3}Z$"},
    "fieldState": {
      "type": "object",
      "additionalProperties": false,
      "required": ["state", "reason_code", "source_refs"],
      "properties": {
        "state": {"enum": ["not_applicable", "unavailable", "not_collected", "redacted"]},
        "reason_code": {"type": "string", "pattern": "^[A-Z][A-Z0-9_]+$"},
        "source_refs": {"type": "array", "items": {"type": "string"}}
      }
    },
    "context": {
      "type": "object",
      "additionalProperties": false,
      "required": ["repository_cwd", "hermes_home", "host", "process", "delegation"],
      "properties": {
        "repository_cwd": {"type": "string", "minLength": 1},
        "hermes_home": {"type": "string", "minLength": 1},
        "host": {"type": "object"},
        "process": {"type": "object"},
        "delegation": {"type": "object"}
      }
    },
    "command": {
      "type": "object",
      "additionalProperties": false,
      "required": ["sequence", "name", "argv", "phase", "mutates", "started_at", "finished_at", "duration_ms", "exit_code", "outcome", "gate", "termination_reason", "stdout_evidence", "stderr_evidence", "source_refs", "redaction_count"],
      "properties": {
        "sequence": {"type": "integer", "minimum": 1},
        "name": {"type": "string", "minLength": 1},
        "argv": {"type": "array", "minItems": 1, "items": {"type": "string"}},
        "phase": {"enum": ["diagnosis", "apply"]},
        "mutates": {"type": "boolean"},
        "started_at": {"type": ["string", "null"]},
        "finished_at": {"type": ["string", "null"]},
        "duration_ms": {"type": ["integer", "null"], "minimum": 0},
        "exit_code": {"type": ["integer", "null"]},
        "outcome": {"enum": ["pass", "warn", "fail", "not_run", "blocked", "skipped", "timeout", "terminated", "unavailable"]},
        "gate": {"enum": ["none", "approval_required", "hard_deny", "capability_unavailable", "stale_snapshot"]},
        "termination_reason": {"enum": ["none", "timeout", "operator_interrupt", "process_exit", "process_tree_cleanup_failed", "host_limit", "unknown"]},
        "stdout_evidence": {"type": ["array", "null"], "items": {"type": "string"}},
        "stderr_evidence": {"type": ["array", "null"], "items": {"type": "string"}},
        "source_refs": {"type": "array", "items": {"type": "string"}},
        "redaction_count": {"type": "integer", "minimum": 0}
      }
    },
    "profile": {
      "type": "object",
      "additionalProperties": false,
      "required": ["source_name", "comparison_key", "display_label", "alias", "gateway_state", "model_display", "directory_state", "identity_file_metadata", "routing_state", "config_state", "credential_warning", "source_refs", "findings"],
      "properties": {
        "source_name": {"type": "string", "minLength": 1},
        "comparison_key": {"type": "string", "minLength": 1},
        "display_label": {"type": "string", "minLength": 1},
        "alias": {},
        "gateway_state": {},
        "model_display": {},
        "directory_state": {},
        "identity_file_metadata": {},
        "routing_state": {},
        "config_state": {},
        "credential_warning": {},
        "source_refs": {"type": "array", "items": {"type": "string"}},
        "findings": {"type": "array", "items": {"type": "string"}}
      }
    },
    "finding": {
      "type": "object",
      "additionalProperties": false,
      "required": ["code", "category", "severity", "state", "source_refs", "evidence_refs", "disposition", "repair_action"],
      "properties": {
        "code": {"type": "string", "pattern": "^[A-Z][A-Z0-9_]+$"},
        "category": {"enum": ["command", "profile", "alias", "routing", "configuration", "credential", "log", "platform", "durability", "repair", "security"]},
        "severity": {"enum": ["critical", "high", "medium", "low", "info", "unknown"]},
        "state": {"enum": ["open", "resolved", "suppressed", "unavailable", "not_collected"]},
        "source_refs": {"type": "array", "items": {"type": "string"}},
        "evidence_refs": {"type": "array", "items": {"type": "string"}},
        "disposition": {"enum": ["none", "report_only", "plan_candidate", "hard_deny", "blocked", "applied"]},
        "repair_action": {"enum": ["none", "propose", "apply", "rollback", "not_supported"]}
      }
    },
    "source": {
      "type": "object",
      "additionalProperties": false,
      "required": ["source_id", "source_kind", "source_command", "captured_at", "metadata"],
      "properties": {
        "source_id": {"type": "string", "minLength": 1},
        "source_kind": {"enum": ["command", "filesystem_metadata", "config_projection", "profile_inventory", "profile_detail", "approval", "plan", "derived"]},
        "source_command": {"type": ["array", "null"], "items": {"type": "string"}},
        "captured_at": {"$ref": "#/$defs/timestamp"},
        "metadata": {"type": "object"}
      }
    },
    "evidence": {
      "type": "object",
      "additionalProperties": false,
      "required": ["source_id", "source_command", "captured_at", "line_start", "line_end", "byte_limit", "line_limit", "bytes_observed", "bytes_captured", "truncated", "sha256", "redaction_count", "excerpt"],
      "properties": {
        "source_id": {"type": "string"},
        "source_command": {"type": "array", "items": {"type": "string"}},
        "captured_at": {"$ref": "#/$defs/timestamp"},
        "line_start": {"type": "integer", "minimum": 1},
        "line_end": {"type": "integer", "minimum": 0},
        "byte_limit": {"const": 32768},
        "line_limit": {"const": 512},
        "bytes_observed": {"type": "integer", "minimum": 0},
        "bytes_captured": {"type": "integer", "minimum": 0, "maximum": 32768},
        "truncated": {"type": "boolean"},
        "sha256": {"$ref": "#/$defs/hash"},
        "redaction_count": {"type": "integer", "minimum": 0},
        "excerpt": {"type": "string"}
      }
    },
    "repairPlan": {
      "type": "object",
      "additionalProperties": false,
      "required": ["state", "schema_version", "plan_id", "plan_hash", "manifest_hash", "allowlist_version", "affected_profile_ids", "changes", "expected_post_state", "pre_apply_snapshot_hash", "created_at", "rollback"],
      "properties": {
        "state": {"enum": ["not_collected", "available", "blocked", "applied"]},
        "schema_version": {"const": "hermes-repair.v1"},
        "plan_id": {"type": ["string", "null"]},
        "plan_hash": {"oneOf": [{"$ref": "#/$defs/hash"}, {"type": "null"}]},
        "manifest_hash": {"$ref": "#/$defs/hash"},
        "allowlist_version": {"const": "repair_allowlist_v1"},
        "affected_profile_ids": {"type": "array", "items": {"type": "string"}},
        "changes": {"type": "array", "items": {"type": "object"}},
        "expected_post_state": {"type": "object"},
        "pre_apply_snapshot_hash": {"oneOf": [{"$ref": "#/$defs/hash"}, {"type": "null"}]},
        "created_at": {"$ref": "#/$defs/timestamp"},
        "rollback": {"type": "object"}
      }
    },
    "approval": {
      "type": "object",
      "additionalProperties": false,
      "required": ["approval_id", "decision", "approver", "scope", "affected_profile_ids", "approved_at", "expires_at", "plan_id", "plan_hash", "effect_digest", "reason"],
      "properties": {
        "approval_id": {"type": ["string", "null"]},
        "decision": {"enum": ["denied", "approved", "revoked", "expired", "stale"]},
        "approver": {"type": ["string", "null"]},
        "scope": {"type": "array", "items": {"type": "string"}},
        "affected_profile_ids": {"type": "array", "items": {"type": "string"}},
        "approved_at": {"type": ["string", "null"]},
        "expires_at": {"type": ["string", "null"]},
        "plan_id": {"type": ["string", "null"]},
        "plan_hash": {"type": ["string", "null"]},
        "effect_digest": {"type": ["string", "null"]},
        "reason": {"type": "string"}
      }
    },
    "attempt": {
      "type": "object",
      "additionalProperties": false,
      "required": ["attempt_id", "parent_run_id", "before_report_id", "after_report_id", "operation", "operation_argv_hash", "plan_id", "plan_hash", "approval_id", "effect_digest", "started_at", "finished_at", "outcome", "gate", "evidence_refs"],
      "properties": {
        "attempt_id": {"type": "string"},
        "parent_run_id": {"type": "string"},
        "before_report_id": {"type": "string"},
        "after_report_id": {"type": ["string", "null"]},
        "operation": {"type": "string"},
        "operation_argv_hash": {"$ref": "#/$defs/hash"},
        "plan_id": {"type": ["string", "null"]},
        "plan_hash": {"type": ["string", "null"]},
        "approval_id": {"type": ["string", "null"]},
        "effect_digest": {"type": ["string", "null"]},
        "started_at": {"$ref": "#/$defs/timestamp"},
        "finished_at": {"type": ["string", "null"]},
        "outcome": {"enum": ["pass", "warn", "fail", "blocked", "timeout", "terminated", "unavailable"]},
        "gate": {"enum": ["none", "approval_required", "hard_deny", "capability_unavailable", "stale_snapshot"]},
        "evidence_refs": {"type": "array", "items": {"type": "string"}}
      }
    },
    "summary": {
      "type": "object",
      "additionalProperties": false,
      "required": ["outcome_counts", "gate_counts", "repair_disposition_counts", "profile_state_counts", "pass_count"],
      "properties": {
        "outcome_counts": {"type": "object", "additionalProperties": {"type": "integer", "minimum": 0}},
        "gate_counts": {"type": "object", "additionalProperties": {"type": "integer", "minimum": 0}},
        "repair_disposition_counts": {"type": "object", "additionalProperties": {"type": "integer", "minimum": 0}},
        "profile_state_counts": {"type": "object", "additionalProperties": {"type": "integer", "minimum": 0}},
        "pass_count": {"type": "integer", "minimum": 0}
      }
    },
    "redaction": {
      "type": "object",
      "additionalProperties": false,
      "required": ["reason", "count"],
      "properties": {"reason": {"type": "string"}, "count": {"type": "integer", "minimum": 1}}
    },
    "limits": {
      "type": "object",
      "additionalProperties": false,
      "required": ["stdout_max_bytes", "stderr_max_bytes", "max_lines", "head_bytes", "tail_bytes", "head_lines", "tail_lines"],
      "properties": {
        "stdout_max_bytes": {"const": 32768},
        "stderr_max_bytes": {"const": 32768},
        "max_lines": {"const": 512},
        "head_bytes": {"const": 8192},
        "tail_bytes": {"const": 24576},
        "head_lines": {"const": 128},
        "tail_lines": {"const": 384}
      }
    }
  }
}
```

## Acceptance matrix

The matrix is the implementation gate. `Deferred` means the architecture pass defines the test but does not run it. Each test must report its exit status and the fixture or command used.

| ID | Acceptance criterion | Fixture or test path | Command | Expected result |
|---|---|---|---|---|
| AC-1 | Fixed eleven item manifest and order | `tests/hermes_diagnostic/test_manifest.py::test_manifest_order` | `python -m pytest tests/hermes_diagnostic/test_manifest.py -q` | Exit 0 and sequence 1 through 11 exact |
| AC-2 | Diagnosis dispatcher rejects all mutating or apply items | `tests/hermes_diagnostic/test_dispatcher.py::test_diagnosis_rejects_apply` | `python -m pytest tests/hermes_diagnostic/test_dispatcher.py -q` | Exit 0 and no subprocess spawn |
| AC-3 | Sequence 3 remains not run in diagnosis | `tests/hermes_diagnostic/test_dispatcher.py::test_doctor_fix_not_run` | Same targeted test command | Exit 0, outcome `not_run`, gate `approval_required`, exit code null |
| AC-4 | Manifest golden hash | `tests/hermes_diagnostic/test_hashes.py::test_manifest_vector` | `python -m pytest tests/hermes_diagnostic/test_hashes.py -q` | Exit 0 and expected hash `7171886c...c4d14e` |
| AC-5 | Repair plan golden hash | `tests/hermes_diagnostic/test_hashes.py::test_plan_vector` | Same targeted test command | Exit 0 and expected hash `f314c97e...9a16` |
| AC-6 | Source fields derive from the declared command or filesystem source | `tests/hermes_diagnostic/test_sources.py` | `python -m pytest tests/hermes_diagnostic/test_sources.py -q` | Exit 0 and no inferred empty values |
| AC-7 | Profile names preserve source values and reject unsafe names | `tests/hermes_diagnostic/test_profiles.py` | `python -m pytest tests/hermes_diagnostic/test_profiles.py -q` | Exit 0 for device names, trailing characters, Unicode collisions, and traversal |
| AC-8 | Capture limits and truncation are deterministic | `tests/hermes_diagnostic/test_capture.py` | `python -m pytest tests/hermes_diagnostic/test_capture.py -q` | Exit 0, 32768 byte and 512 line limits enforced |
| AC-9 | Redaction occurs before persistence and hashing | `tests/hermes_diagnostic/test_redaction.py` | `python -m pytest tests/hermes_diagnostic/test_redaction.py -q` | Exit 0 and no raw secret fixture value in files or hashes |
| AC-10 | Profile, routing, and configuration allowlists are versioned | `tests/hermes_diagnostic/test_allowlists.py` | `python -m pytest tests/hermes_diagnostic/test_allowlists.py -q` | Exit 0 and unlisted fields are unavailable or hard denied |
| AC-11 | `config set` exact argv is apply only | `tests/hermes_diagnostic/test_repair_operations.py` | `python -m pytest tests/hermes_diagnostic/test_repair_operations.py -q` | Exit 0 and only `mcp.servers.<name>.enabled` is eligible |
| AC-12 | Doctor preview requires advertised dry run and machine readable diff | `tests/hermes_diagnostic/test_preview.py` | `python -m pytest tests/hermes_diagnostic/test_preview.py -q` | Exit 0; unsupported preview blocks without spawn |
| AC-13 | Approval envelope rejects missing, duplicate, malformed, denied, expired, revoked, stale, scope mismatch, plan mismatch, and effect mismatch | `tests/hermes_diagnostic/test_approval.py` | `python -m pytest tests/hermes_diagnostic/test_approval.py -q` | Exit 0 with stable rejection codes and no mutation |
| AC-14 | Effect diff is allowlist checked and bound by digest | `tests/hermes_diagnostic/test_effect_digest.py` | `python -m pytest tests/hermes_diagnostic/test_effect_digest.py -q` | Exit 0 and changed digest blocks apply |
| AC-15 | Lock prevents TOCTOU and concurrent apply | `tests/hermes_diagnostic/test_locking.py` | `python -m pytest tests/hermes_diagnostic/test_locking.py -q` | Exit 0 and second writer is blocked |
| AC-16 | Checkpoints are atomic and corruption is rejected | `tests/hermes_diagnostic/test_checkpoint.py` | `python -m pytest tests/hermes_diagnostic/test_checkpoint.py -q` | Exit 0 for crash, partial marker, duplicate, and mismatch fixtures |
| AC-17 | Resume skips committed items and requires exact context | `tests/hermes_diagnostic/test_resume.py` | `python -m pytest tests/hermes_diagnostic/test_resume.py -q` | Exit 0 and mismatched context refuses resume |
| AC-18 | Apply attempts and post apply reports are append only | `tests/hermes_diagnostic/test_attempts.py` | `python -m pytest tests/hermes_diagnostic/test_attempts.py -q` | Exit 0 and initial `not_run` record remains unchanged |
| AC-19 | Summary counts and schema validation are exact | `tests/hermes_diagnostic/test_report_schema.py` | `python -m pytest tests/hermes_diagnostic/test_report_schema.py -q` | Exit 0 and invalid required fields fail closed |
| AC-20 | GA verification tail and documentation are complete | `tests/hermes_diagnostic/test_ga_gate.py` plus `docs/operations/hermes-diagnostics.md` | `python -m pytest tests/hermes_diagnostic -q` then repository check command | Exit 0, review evidence recorded, and scope status updated only after all prior criteria pass |

The implementation plan must link each AC row to a task ID. The task is not implementation ready if any row lacks a fixture, a test path, an expected result, or an explicit reason for being unavailable.
