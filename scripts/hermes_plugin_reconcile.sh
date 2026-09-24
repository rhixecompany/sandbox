#!/usr/bin/env bash
# Hermes plugin inventory, reconciliation, and verification for Bash.

set -u

SCRIPT_VERSION="1.0.0"
SCHEMA_VERSION="hermes-plugin-reconciliation.v1"
EXIT_OK=0
EXIT_USAGE=2
EXIT_INVENTORY=3
EXIT_BLOCKED=4
EXIT_ACTION=5
EXIT_VERIFY=6
EXIT_INTERNAL=7

HERMES_BIN="${HERMES_BIN:-hermes}"
PYTHON_BIN="${PYTHON_BIN:-python}"
REPORT_DIR="${REPORT_DIR:-${TMPDIR:-.}/hermes-plugin-reconciliation}"
MODE=""
CONFIRM_UNINSTALL=0
RUN_DIR=""
LOCK_DIR=""
LOCK_HELD=0
RUN_RC=0
INVENTORY_RC=0
BLOCKED_COUNT=0
ACTION_FAILURE_COUNT=0
VERIFY_FAILURE_COUNT=0

SCRIPT_PATH="$(cd -- "$(dirname -- "${BASH_SOURCE[0]}")" && pwd -P)/$(basename -- "${BASH_SOURCE[0]}")"

usage() {
  cat <<'USAGE'
Usage:
  bash scripts/hermes_plugin_reconcile.sh --inventory
  bash scripts/hermes_plugin_reconcile.sh --dry-run
  bash scripts/hermes_plugin_reconcile.sh --apply --confirm-uninstall
  bash scripts/hermes_plugin_reconcile.sh --verify
  bash scripts/hermes_plugin_reconcile.sh --self-test

Modes:
  --inventory              Read the live plugin list and print counts. No mutation.
  --dry-run                Audit every plugin and write a redacted action report.
  --apply                  Recompute the audit, then apply safe planned actions.
  --confirm-uninstall      Required with --apply. Confirms removal of non bundled plugins.
  --verify                 Reread the last report targets and verify live postconditions.
  --self-test              Run offline mock tests. Never calls the real Hermes binary.
  --help                   Show this help.

Environment:
  HERMES_BIN               Hermes executable path. Default: hermes.
  PYTHON_BIN               Python executable used for JSON parsing. Default: python.
  REPORT_DIR               Report directory. Default: TMPDIR/hermes-plugin-reconciliation.
  PLUGIN_RECONCILE_ASSUME_YES=1
                           Explicitly confirms apply in automation.

The script never reads .env, credentials, tokens, passwords, or provider stores.
Dry run is the default safety boundary. Apply uses exact plugin keys and does not grant
built in tool override permissions.
USAGE
}

fail_usage() {
  printf 'Usage error: %s\n' "$1" >&2
  usage >&2
  return "$EXIT_USAGE"
}

redact_stream() {
  sed -E \
    -e 's/(Bearer[[:space:]]+)[^[:space:]]+/\1[REDACTED]/Ig' \
    -e 's/((api[_-]?key|token|secret|password|passwd|credential|private[_-]?key)[[:space:]]*[:=][[:space:]]*)[^[:space:],;]+/\1[REDACTED]/Ig' \
    -e 's/((api[_-]?key|token|secret|password|passwd|credential)[[:space:]]+is[[:space:]]+)[^[:space:],;]+/\1[REDACTED]/Ig' \
    -e 's/([?&](api[_-]?key|token|secret|password|credential)=)[^&[:space:]]+/\1[REDACTED]/Ig' \
    -e 's/(-----BEGIN [^-]+ PRIVATE KEY-----).*(-----END [^-]+ PRIVATE KEY-----)/\1 [REDACTED] \2/Ig'
}

run_capture() {
  local output_file="$1"
  shift
  : > "$output_file" || return "$EXIT_INTERNAL"
  set +e
  "$@" 2>&1 | redact_stream > "$output_file"
  RUN_RC="${PIPESTATUS[0]}"
  set -u
  return 0
}

trim_value() {
  local value="${1:-}"
  value="${value#"${value%%[![:space:]]*}"}"
  value="${value%"${value##*[![:space:]]}"}"
  printf '%s' "$value"
}

safe_field() {
  printf '%s' "${1:-}" | tr '\r\n\t' '   ' | cut -c1-4096
}

compact_file() {
  local file="$1"
  if [[ ! -f "$file" ]]; then
    printf ''
    return 0
  fi
  tr '\r\n\t' '   ' < "$file" | cut -c1-4096
}

extract_field() {
  local label="$1"
  local file="$2"
  local line value
  while IFS= read -r line || [[ -n "$line" ]]; do
    line="${line//$'\r'/}"
    case "$line" in
      "$label:"*)
        value="${line#"$label:"}"
        trim_value "$value"
        return 0
        ;;
    esac
  done < "$file"
  return 1
}

extract_doctor_path() {
  local file="$1"
  local line rest awaiting=0
  while IFS= read -r line || [[ -n "$line" ]]; do
    line="${line//$'\r'/}"
    if [[ "$line" == Plugin\ Doctor:* ]]; then
      rest="${line#Plugin Doctor:}"
      rest="$(trim_value "$rest")"
      if [[ "$rest" =~ ^/[A-Za-z0-9_./\\:-]+$ || "$rest" =~ ^[A-Za-z]:[\\/].* ]]; then
        printf '%s' "$rest"
        return 0
      fi
      awaiting=1
      continue
    fi
    if (( awaiting == 1 )); then
      rest="$(trim_value "$line")"
      if [[ "$rest" =~ ^/[A-Za-z0-9_./\\:-]+$ || "$rest" =~ ^[A-Za-z]:[\\/].* ]]; then
        printf '%s' "$rest"
        return 0
      fi
      if [[ "$rest" == ERROR:* || "$rest" == WARN:* || "$rest" == manifest:* ]]; then
        awaiting=0
      fi
    fi
  done < "$file"
  return 1
}

credential_gate_for() {
  local text="${1:-}"
  if [[ "$text" =~ API[_-]?KEY || "$text" =~ TOKEN || "$text" =~ SECRET || "$text" =~ PASSWORD || "$text" =~ CREDENTIAL || "$text" =~ OAUTH || "$text" =~ LOGIN || "$text" =~ AUTHENTICATION ]]; then
    printf 'declared'
  else
    printf 'none'
  fi
}

prepare_run_dir() {
  local stamp candidate suffix=0
  mkdir -p "$REPORT_DIR" || {
    printf 'Cannot create report directory: %s\n' "$REPORT_DIR" >&2
    return "$EXIT_INTERNAL"
  }
  stamp="$(date -u +%Y%m%dT%H%M%SZ)"
  while :; do
    if (( suffix == 0 )); then
      candidate="$REPORT_DIR/run-$stamp"
    else
      candidate="$REPORT_DIR/run-$stamp-$suffix"
    fi
    if mkdir "$candidate" 2>/dev/null; then
      RUN_DIR="$candidate"
      break
    fi
    suffix=$((suffix + 1))
    if (( suffix > 100 )); then
      printf 'Cannot allocate a unique report directory under %s\n' "$REPORT_DIR" >&2
      return "$EXIT_INTERNAL"
    fi
  done
  mkdir -p "$RUN_DIR/evidence" || return "$EXIT_INTERNAL"
  : > "$RUN_DIR/records.tsv"
  : > "$RUN_DIR/actions.tsv"
  : > "$RUN_DIR/post.tsv"
  return 0
}

acquire_lock() {
  LOCK_DIR="$REPORT_DIR/.hermes-plugin-reconcile.lock"
  if ! mkdir "$LOCK_DIR" 2>/dev/null; then
    printf 'Apply blocked because a reconciliation lock already exists: %s\n' "$LOCK_DIR" >&2
    return "$EXIT_BLOCKED"
  fi
  LOCK_HELD=1
  return 0
}

release_lock() {
  if (( LOCK_HELD == 1 )); then
    rmdir "$LOCK_DIR" 2>/dev/null || true
    LOCK_HELD=0
  fi
}

cleanup() {
  release_lock
}

trap cleanup EXIT

python_emit_inventory() {
  local inventory_file="$1"
  local inventory_tsv="$2"
  "$PYTHON_BIN" - "$inventory_file" "$inventory_tsv" <<'PY'
import json
import sys
from collections import Counter

source_path, output_path = sys.argv[1:3]
with open(source_path, encoding="utf-8") as handle:
    data = json.load(handle)
if isinstance(data, dict):
    items = data.get("plugins", data.get("items", data.get("data", [])))
else:
    items = data
if not isinstance(items, list):
    raise SystemExit("plugin inventory is not a JSON array")
counts = Counter(str(item.get("name", "")) for item in items if isinstance(item, dict))
with open(output_path, "w", encoding="utf-8", newline="") as handle:
    for index, item in enumerate(items, start=1):
        if not isinstance(item, dict):
            raise SystemExit(f"inventory item {index} is not an object")
        name = str(item.get("name", ""))
        if not name:
            raise SystemExit(f"inventory item {index} has no name")
        status = str(item.get("status", ""))
        source = str(item.get("source", ""))
        version = str(item.get("version", ""))
        description = " ".join(str(item.get("description", "")).replace("\t", " ").split())
        occurrence = sum(1 for prior in items[:index] if isinstance(prior, dict) and str(prior.get("name", "")) == name)
        fields = [str(index), name, status, source, version, description, str(occurrence), str(counts[name])]
        handle.write("\t".join(fields) + "\n")
PY
}

python_report() {
  local records_file="$1"
  local actions_file="$2"
  local post_file="$3"
  local report_json="$4"
  local report_csv="$5"
  local report_md="$6"
  local mode="$7"
  local inventory_rc="$8"
  local final_rc="$9"
  "$PYTHON_BIN" - "$records_file" "$actions_file" "$post_file" "$report_json" "$report_csv" "$report_md" "$mode" "$inventory_rc" "$final_rc" "$SCHEMA_VERSION" "$SCRIPT_VERSION" "$RUN_DIR" <<'PY'
import csv
import json
import os
import sys
from collections import Counter
from datetime import datetime, timezone

(records_path, actions_path, post_path, json_path, csv_path, md_path,
 mode, inventory_rc, final_rc, schema_version, script_version, run_dir) = sys.argv[1:]

record_fields = [
    "sequence", "display_name", "original_status", "configured_state", "list_source",
    "show_source", "version", "exact_key", "resolution", "doctor_exit",
    "compat_exit", "credential_gate", "compatibility", "runtime_state",
    "expected_runtime_state", "action", "reason", "doctor_excerpt", "compat_excerpt",
]

def read_tsv(path, fields):
    rows = []
    if not os.path.exists(path):
        return rows
    with open(path, encoding="utf-8", newline="") as handle:
        for values in csv.reader(handle, delimiter="\t"):
            if not values or not any(values):
                continue
            values = values + [""] * (len(fields) - len(values))
            rows.append(dict(zip(fields, values[:len(fields)])))
    return rows

def integer(value):
    try:
        return int(value)
    except (TypeError, ValueError):
        return None

records = read_tsv(records_path, record_fields)
action_fields = ["sequence", "action", "action_result", "action_exit", "action_excerpt"]
actions = {row.get("sequence", ""): row for row in read_tsv(actions_path, action_fields)}
post_fields = ["sequence", "postcondition", "post_status", "post_exit", "post_excerpt"]
post = {row.get("sequence", ""): row for row in read_tsv(post_path, post_fields)}

normalized = []
for row in records:
    sequence = row.get("sequence", "")
    action = actions.get(sequence, {})
    post_row = post.get(sequence, {})
    item = {
        "sequence": integer(sequence),
        "display_name": row.get("display_name", ""),
        "original_status": row.get("original_status", ""),
        "configured_state": row.get("configured_state", ""),
        "list_source": row.get("list_source", ""),
        "show_source": row.get("show_source", ""),
        "version": row.get("version", ""),
        "exact_key": row.get("exact_key", ""),
        "resolution": row.get("resolution", ""),
        "doctor_exit": integer(row.get("doctor_exit", "")),
        "compat_exit": integer(row.get("compat_exit", "")),
        "credential_gate": row.get("credential_gate", ""),
        "compatibility": row.get("compatibility", ""),
        "runtime_state": row.get("runtime_state", ""),
        "expected_runtime_state": row.get("expected_runtime_state", ""),
        "proposed_action": row.get("action", ""),
        "reason": row.get("reason", ""),
        "doctor_excerpt": row.get("doctor_excerpt", ""),
        "compat_excerpt": row.get("compat_excerpt", ""),
        "action_result": action.get("action_result", "not_attempted"),
        "action_exit": integer(action.get("action_exit", "")),
        "action_excerpt": action.get("action_excerpt", ""),
        "postcondition": post_row.get("postcondition", "not_checked"),
        "post_status": post_row.get("post_status", ""),
        "post_exit": integer(post_row.get("post_exit", "")),
        "post_excerpt": post_row.get("post_excerpt", ""),
    }
    normalized.append(item)

counts = {
    "records": len(normalized),
    "original_status": dict(Counter(item["original_status"] for item in normalized)),
    "configured_state": dict(Counter(item["configured_state"] for item in normalized)),
    "compatibility": dict(Counter(item["compatibility"] for item in normalized)),
    "runtime_state": dict(Counter(item["runtime_state"] for item in normalized)),
    "proposed_action": dict(Counter(item["proposed_action"] for item in normalized)),
    "action_result": dict(Counter(item["action_result"] for item in normalized)),
    "postcondition": dict(Counter(item["postcondition"] for item in normalized)),
}
redaction_count = sum(
    text.count("[REDACTED]")
    for item in normalized
    for text in (item.get("doctor_excerpt", ""), item.get("compat_excerpt", ""), item.get("action_excerpt", ""), item.get("post_excerpt", ""))
)
now = datetime.now(timezone.utc).isoformat(timespec="milliseconds").replace("+00:00", "Z")
report = {
    "schema_version": schema_version,
    "script_version": script_version,
    "mode": mode,
    "started_at": now,
    "finished_at": now,
    "report_directory": run_dir.replace("\\", "/"),
    "inventory_exit": integer(inventory_rc),
    "final_exit": integer(final_rc),
    "records": normalized,
    "counts": counts,
    "redaction_count": redaction_count,
    "redaction_policy": "sanitized before persistence; uncertain values block the affected record",
    "mutation_policy": "Hermes plugin commands only; no tool override grant; no .env or credential access",
}
with open(json_path, "w", encoding="utf-8") as handle:
    json.dump(report, handle, ensure_ascii=False, indent=2)
    handle.write("\n")

csv_fields = list(normalized[0].keys()) if normalized else ["sequence"]
with open(csv_path, "w", encoding="utf-8", newline="") as handle:
    writer = csv.DictWriter(handle, fieldnames=csv_fields)
    writer.writeheader()
    writer.writerows(normalized)

with open(md_path, "w", encoding="utf-8") as handle:
    handle.write("# Hermes plugin reconciliation\n\n")
    handle.write(f"Mode: `{mode}`  \n")
    handle.write(f"Schema: `{schema_version}`  \n")
    handle.write(f"Inventory exit: `{inventory_rc}`  \n")
    handle.write(f"Final exit: `{final_rc}`  \n")
    handle.write(f"Records: `{len(normalized)}`  \n\n")
    handle.write("## Counts\n\n")
    for group, values in counts.items():
        handle.write(f"* {group}: {json.dumps(values, ensure_ascii=False, sort_keys=True)}\n")
    handle.write(f"* redactions: `{redaction_count}`\n\n")
    handle.write("## Records\n\n")
    handle.write("| Seq | Display name | Exact key | Configured | Compatibility | Credential | Runtime | Action | Result | Reason |\n")
    handle.write("|---:|---|---|---|---|---|---|---|---|---|\n")
    for item in normalized:
        cells = [
            str(item.get("sequence", "")), item.get("display_name", ""), item.get("exact_key", ""),
            item.get("configured_state", ""), item.get("compatibility", ""), item.get("credential_gate", ""),
            item.get("runtime_state", ""), item.get("proposed_action", ""), item.get("action_result", ""),
            item.get("reason", "").replace("|", "\\|")
        ]
        handle.write("| " + " | ".join(cells) + " |\n")
PY
}

write_inventory_summary() {
  local inventory_file="$1"
  "$PYTHON_BIN" - "$inventory_file" <<'PY'
import json
import sys
from collections import Counter

with open(sys.argv[1], encoding="utf-8") as handle:
    data = json.load(handle)
items = data.get("plugins", data.get("items", data.get("data", []))) if isinstance(data, dict) else data
if not isinstance(items, list):
    raise SystemExit("plugin inventory is not a JSON array")
status = Counter(str(item.get("status", "")) for item in items if isinstance(item, dict))
name = Counter(str(item.get("name", "")) for item in items if isinstance(item, dict))
print(f"records={len(items)}")
for key in sorted(status):
    print(f"status[{key}]={status[key]}")
print("duplicates=" + ",".join(f"{key}:{value}" for key, value in sorted(name.items()) if value > 1) or "duplicates=none")
PY
}

resolve_plugin_identity() {
  local sequence="$1"
  local name="$2"
  local description="$3"
  local duplicate_count="$4"
  local original_show="$RUN_DIR/evidence/${sequence}-show.txt"
  local candidate_show="$RUN_DIR/evidence/${sequence}-candidate-show.txt"
  local exact_key=""
  local show_source=""
  local show_rc
  local candidate=""
  local candidate_rc
  local candidate_key
  run_capture "$original_show" "$HERMES_BIN" plugins show "$name"
  show_rc="$RUN_RC"
  exact_key="$(extract_field Key "$original_show" 2>/dev/null || true)"
  show_source="$(extract_field Source "$original_show" 2>/dev/null || true)"

  if (( duplicate_count > 1 )); then
    local lower_description="${description,,}"
    if [[ "$lower_description" == *"video generation"* || "$lower_description" == *"video backend"* ]]; then
      candidate="video_gen/$name"
    elif [[ "$lower_description" == *"image generation"* || "$lower_description" == *"image backend"* ]]; then
      candidate="image_gen/$name"
    fi
    if [[ -n "$candidate" ]]; then
      run_capture "$candidate_show" "$HERMES_BIN" plugins show "$candidate"
      candidate_rc="$RUN_RC"
      candidate_key="$(extract_field Key "$candidate_show" 2>/dev/null || true)"
      if (( candidate_rc == 0 )) && [[ "$candidate_key" == "$candidate" ]]; then
        exact_key="$candidate"
        show_source="$(extract_field Source "$candidate_show" 2>/dev/null || true)"
        show_rc=0
      else
        exact_key=""
      fi
    else
      exact_key=""
    fi
  fi

  if (( show_rc != 0 )) || [[ -z "$exact_key" ]]; then
    printf 'unresolved\t%s\t%s\t%s\n' "$exact_key" "$show_source" "$show_rc"
  else
    printf 'resolved\t%s\t%s\t%s\n' "$exact_key" "$show_source" "$show_rc"
  fi
}

run_audit() {
  local mode="$1"
  local inventory_file="$RUN_DIR/inventory.json"
  local inventory_tsv="$RUN_DIR/inventory.tsv"
  local records_file="$RUN_DIR/records.tsv"
  local sequence name original_status list_source version description occurrence duplicate_count
  local resolution exact_key show_source show_rc
  local doctor_file compat_file doctor_rc compat_rc doctor_path
  local credential_gate compatibility runtime_state expected_runtime action reason
  local doctor_excerpt compat_excerpt source_effective
  local configured_state
  local identity_result

  run_capture "$inventory_file" "$HERMES_BIN" plugins list --json
  INVENTORY_RC="$RUN_RC"
  if (( INVENTORY_RC != 0 )); then
    printf 'Plugin inventory failed with exit %s. Evidence: %s\n' "$INVENTORY_RC" "$inventory_file" >&2
    return "$EXIT_INVENTORY"
  fi
  if ! python_emit_inventory "$inventory_file" "$inventory_tsv"; then
    printf 'Plugin inventory JSON could not be normalized. Evidence: %s\n' "$inventory_file" >&2
    return "$EXIT_INVENTORY"
  fi

  BLOCKED_COUNT=0
  : > "$records_file"
  while IFS=$'\t' read -r sequence name original_status list_source version description occurrence duplicate_count; do
    [[ -z "${sequence:-}" ]] && continue
    configured_state="enabled"
    [[ "$original_status" != "enabled" ]] && configured_state="disabled"

    identity_result="$(resolve_plugin_identity "$sequence" "$name" "$description" "$duplicate_count")"
    IFS=$'\t' read -r resolution exact_key show_source show_rc <<< "$identity_result"
    show_source="${show_source:-$list_source}"
    doctor_rc=2
    compat_rc=2
    doctor_path=""
    doctor_file="$RUN_DIR/evidence/${sequence}-doctor.txt"
    compat_file="$RUN_DIR/evidence/${sequence}-compat.txt"

    if [[ "$resolution" == "resolved" ]]; then
      run_capture "$doctor_file" "$HERMES_BIN" plugins doctor --ci "$exact_key"
      doctor_rc="$RUN_RC"
      doctor_path="$(extract_doctor_path "$doctor_file" 2>/dev/null || true)"
      if [[ -n "$doctor_path" ]]; then
        run_capture "$compat_file" "$HERMES_BIN" plugins compat --json "$doctor_path"
        compat_rc="$RUN_RC"
      else
        printf 'compatibility probe unavailable because doctor returned no plugin path\n' > "$compat_file"
      fi
    else
      printf 'exact plugin key could not be resolved\n' > "$doctor_file"
      printf 'compatibility probe skipped because exact plugin key could not be resolved\n' > "$compat_file"
      BLOCKED_COUNT=$((BLOCKED_COUNT + 1))
    fi

    doctor_excerpt="$(compact_file "$doctor_file")"
    compat_excerpt="$(compact_file "$compat_file")"
    credential_gate="$(credential_gate_for "$description $(compact_file "$RUN_DIR/evidence/${sequence}-show.txt")")"
    if [[ "$resolution" != "resolved" ]]; then
      compatibility="unavailable"
      runtime_state="inactive"
      expected_runtime="inactive"
      action="none"
      reason="exact_key_unresolved"
    elif (( doctor_rc != 0 )); then
      compatibility="incompatible"
      runtime_state="inactive"
      expected_runtime="unavailable"
      source_effective="$show_source"
      if [[ "$source_effective" == "bundled" ]]; then
        action="disable_bundled"
        reason="doctor_failed_bundled_uninstall_unavailable"
      elif [[ "$configured_state" == "enabled" ]]; then
        action="disable_remove"
        reason="doctor_failed"
      else
        action="remove"
        reason="doctor_failed"
      fi
    elif (( compat_rc == 1 )); then
      compatibility="incompatible"
      runtime_state="inactive"
      expected_runtime="unavailable"
      source_effective="$show_source"
      if [[ "$source_effective" == "bundled" ]]; then
        action="disable_bundled"
        reason="deprecated_import_bundled_uninstall_unavailable"
      elif [[ "$configured_state" == "enabled" ]]; then
        action="disable_remove"
        reason="deprecated_import"
      else
        action="remove"
        reason="deprecated_import"
      fi
    elif (( compat_rc != 0 )); then
      compatibility="blocked"
      runtime_state="inactive"
      expected_runtime="inactive"
      action="none"
      reason="compatibility_probe_unavailable"
      BLOCKED_COUNT=$((BLOCKED_COUNT + 1))
    else
      compatibility="compatible"
      if [[ "$credential_gate" == "declared" ]]; then
        expected_runtime="inactive"
        reason="credential_gated"
      else
        expected_runtime="active"
        reason="all_local_gates_passed"
      fi
      if [[ "$configured_state" == "enabled" ]]; then
        action="none"
        runtime_state="$expected_runtime"
      else
        action="enable"
        runtime_state="inactive"
      fi
    fi

    if [[ "$resolution" != "resolved" || "$compatibility" == "blocked" ]]; then
      expected_runtime="inactive"
    fi

    printf '%s\t%s\t%s\t%s\t%s\t%s\t%s\t%s\t%s\t%s\t%s\t%s\t%s\t%s\t%s\t%s\t%s\t%s\t%s\n' \
      "$(safe_field "$sequence")" "$(safe_field "$name")" "$(safe_field "$original_status")" \
      "$(safe_field "$configured_state")" "$(safe_field "$list_source")" "$(safe_field "$show_source")" \
      "$(safe_field "$version")" "$(safe_field "$exact_key")" "$(safe_field "$resolution")" \
      "$(safe_field "$doctor_rc")" "$(safe_field "$compat_rc")" "$(safe_field "$credential_gate")" \
      "$(safe_field "$compatibility")" "$(safe_field "$runtime_state")" "$(safe_field "$expected_runtime")" \
      "$(safe_field "$action")" "$(safe_field "$reason")" "$(safe_field "$doctor_excerpt")" "$(safe_field "$compat_excerpt")" >> "$records_file"
  done < "$inventory_tsv"

  return 0
}

apply_actions() {
  local records_file="$RUN_DIR/records.tsv"
  local actions_file="$RUN_DIR/actions.tsv"
  local sequence name original_status configured_state list_source show_source version exact_key resolution doctor_rc compat_rc credential_gate compatibility runtime_state expected_runtime action reason doctor_excerpt compat_excerpt
  local action_file action_rc action_result action_excerpt disable_rc remove_rc
  ACTION_FAILURE_COUNT=0
  : > "$actions_file"
  while IFS=$'\t' read -r sequence name original_status configured_state list_source show_source version exact_key resolution doctor_rc compat_rc credential_gate compatibility runtime_state expected_runtime action reason doctor_excerpt compat_excerpt; do
    [[ -z "${sequence:-}" ]] && continue
    action_result="not_attempted"
    action_rc=""
    action_excerpt=""
    if [[ "$action" == "none" || -z "$exact_key" ]]; then
      printf '%s\t%s\t%s\t%s\t%s\n' "$sequence" "$action" "$action_result" "$action_rc" "$action_excerpt" >> "$actions_file"
      continue
    fi

    action_file="$RUN_DIR/evidence/${sequence}-action.txt"
    case "$action" in
      enable)
        run_capture "$action_file" "$HERMES_BIN" plugins enable "$exact_key" --no-allow-tool-override
        action_rc="$RUN_RC"
        action_excerpt="$(compact_file "$action_file")"
        if (( action_rc == 0 )); then action_result="passed"; else action_result="failed"; ACTION_FAILURE_COUNT=$((ACTION_FAILURE_COUNT + 1)); fi
        ;;
      disable_bundled)
        run_capture "$action_file" "$HERMES_BIN" plugins disable "$exact_key"
        action_rc="$RUN_RC"
        action_excerpt="$(compact_file "$action_file")"
        if (( action_rc == 0 )); then action_result="passed_uninstall_unavailable"; else action_result="failed"; ACTION_FAILURE_COUNT=$((ACTION_FAILURE_COUNT + 1)); fi
        ;;
      disable_remove)
        run_capture "$action_file" "$HERMES_BIN" plugins disable "$exact_key"
        disable_rc="$RUN_RC"
        action_excerpt="disable: $(compact_file "$action_file")"
        if (( disable_rc == 0 )); then
          run_capture "$action_file" "$HERMES_BIN" plugins remove "$exact_key"
          remove_rc="$RUN_RC"
          action_excerpt="$action_excerpt; remove: $(compact_file "$action_file")"
          action_rc="$remove_rc"
          if (( remove_rc == 0 )); then action_result="passed"; else action_result="remove_failed"; ACTION_FAILURE_COUNT=$((ACTION_FAILURE_COUNT + 1)); fi
        else
          action_rc="$disable_rc"
          action_result="disable_failed_remove_skipped"
          ACTION_FAILURE_COUNT=$((ACTION_FAILURE_COUNT + 1))
        fi
        ;;
      remove)
        run_capture "$action_file" "$HERMES_BIN" plugins remove "$exact_key"
        action_rc="$RUN_RC"
        action_excerpt="$(compact_file "$action_file")"
        if (( action_rc == 0 )); then action_result="passed"; else action_result="failed"; ACTION_FAILURE_COUNT=$((ACTION_FAILURE_COUNT + 1)); fi
        ;;
      *)
        action_result="blocked_unknown_action"
        ACTION_FAILURE_COUNT=$((ACTION_FAILURE_COUNT + 1))
        ;;
    esac
    printf '%s\t%s\t%s\t%s\t%s\n' "$sequence" "$action" "$action_result" "$action_rc" "$(safe_field "$action_excerpt")" >> "$actions_file"
  done < "$records_file"
}

verify_postconditions() {
  local post_inventory="$RUN_DIR/post-inventory.json"
  local records_file="$RUN_DIR/records.tsv"
  local actions_file="$RUN_DIR/actions.tsv"
  local post_file="$RUN_DIR/post.tsv"
  local sequence name original_status configured_state list_source show_source version exact_key resolution doctor_rc compat_rc credential_gate compatibility runtime_state expected_runtime action reason doctor_excerpt compat_excerpt
  local action_result action_rc action_excerpt show_file post_rc post_status post_condition post_excerpt
  VERIFY_FAILURE_COUNT=0
  : > "$post_file"
  run_capture "$post_inventory" "$HERMES_BIN" plugins list --json
  local post_inventory_rc="$RUN_RC"
  if (( post_inventory_rc != 0 )); then
    VERIFY_FAILURE_COUNT=$((VERIFY_FAILURE_COUNT + 1))
  fi

  while IFS=$'\t' read -r sequence name original_status configured_state list_source show_source version exact_key resolution doctor_rc compat_rc credential_gate compatibility runtime_state expected_runtime action reason doctor_excerpt compat_excerpt; do
    [[ -z "${sequence:-}" ]] && continue
    action_result="not_attempted"
    action_rc=""
    action_excerpt=""
    while IFS=$'\t' read -r action_sequence action action_result action_rc action_excerpt; do
      [[ "$action_sequence" == "$sequence" ]] && break
    done < "$actions_file"
    post_condition="not_checked"
    post_status=""
    post_rc=""
    post_excerpt=""
    case "$action" in
      enable|disable_bundled|disable_remove|remove)
        show_file="$RUN_DIR/evidence/${sequence}-post-show.txt"
        run_capture "$show_file" "$HERMES_BIN" plugins show "$exact_key"
        post_rc="$RUN_RC"
        post_status="$(extract_field Status "$show_file" 2>/dev/null || true)"
        post_excerpt="$(compact_file "$show_file")"
        if [[ "$action" == "remove" || "$action" == "disable_remove" ]]; then
          if (( post_rc != 0 )); then
            post_condition="passed_removed"
          else
            post_condition="failed_still_present"
            VERIFY_FAILURE_COUNT=$((VERIFY_FAILURE_COUNT + 1))
          fi
        elif [[ "$action" == "enable" ]]; then
          if (( post_rc == 0 )) && [[ "$post_status" == "enabled" ]]; then
            post_condition="passed_enabled"
          else
            post_condition="failed_not_enabled"
            VERIFY_FAILURE_COUNT=$((VERIFY_FAILURE_COUNT + 1))
          fi
        elif [[ "$action" == "disable_bundled" ]]; then
          if (( post_rc == 0 )) && [[ "$post_status" == "disabled" ]]; then
            post_condition="passed_disabled_bundled"
          else
            post_condition="failed_not_disabled"
            VERIFY_FAILURE_COUNT=$((VERIFY_FAILURE_COUNT + 1))
          fi
        fi
        ;;
    esac
    printf '%s\t%s\t%s\t%s\t%s\n' "$sequence" "$post_condition" "$post_status" "$post_rc" "$(safe_field "$post_excerpt")" >> "$post_file"
  done < "$records_file"
}

write_reports() {
  local final_rc="$1"
  local report_json="$RUN_DIR/plugin-reconciliation.json"
  local report_csv="$RUN_DIR/plugin-reconciliation.csv"
  local report_md="$RUN_DIR/plugin-reconciliation.md"
  if ! python_report "$RUN_DIR/records.tsv" "$RUN_DIR/actions.tsv" "$RUN_DIR/post.tsv" "$report_json" "$report_csv" "$report_md" "$MODE" "$INVENTORY_RC" "$final_rc"; then
    printf 'Report generation failed.\n' >&2
    return "$EXIT_INTERNAL"
  fi
  printf '%s\n' "$RUN_DIR" > "$REPORT_DIR/latest.txt"
  printf 'Report directory: %s\n' "$RUN_DIR"
  printf 'JSON report: %s\n' "$report_json"
  printf 'Markdown report: %s\n' "$report_md"
  return 0
}

run_inventory_mode() {
  local temporary_dir inventory_file
  temporary_dir="$REPORT_DIR/inventory-$$"
  mkdir -p "$temporary_dir" || return "$EXIT_INTERNAL"
  inventory_file="$temporary_dir/inventory.json"
  run_capture "$inventory_file" "$HERMES_BIN" plugins list --json
  local rc="$RUN_RC"
  if (( rc != 0 )); then
    printf 'Inventory failed with exit %s.\n' "$rc" >&2
    return "$EXIT_INVENTORY"
  fi
  write_inventory_summary "$inventory_file"
  rm -rf "$temporary_dir"
  return 0
}

run_verify_mode() {
  local latest latest_json verify_dir inventory_file report_path
  if [[ ! -f "$REPORT_DIR/latest.txt" ]]; then
    printf 'No previous report found under %s\n' "$REPORT_DIR" >&2
    return "$EXIT_VERIFY"
  fi
  latest="$(tr -d '\r\n' < "$REPORT_DIR/latest.txt")"
  latest_json="$latest/plugin-reconciliation.json"
  if [[ ! -f "$latest_json" ]]; then
    printf 'Previous report is missing: %s\n' "$latest_json" >&2
    return "$EXIT_VERIFY"
  fi
  verify_dir="$REPORT_DIR/verify-$$"
  mkdir -p "$verify_dir/evidence" || return "$EXIT_INTERNAL"
  inventory_file="$verify_dir/inventory.json"
  run_capture "$inventory_file" "$HERMES_BIN" plugins list --json
  if (( RUN_RC != 0 )); then
    printf 'Verification inventory failed with exit %s\n' "$RUN_RC" >&2
    return "$EXIT_VERIFY"
  fi
  printf 'Live inventory summary:\n'
  write_inventory_summary "$inventory_file"
  report_path="$latest_json"
  "$PYTHON_BIN" - "$report_path" <<'PY'
import json
import sys
with open(sys.argv[1], encoding="utf-8") as handle:
    report = json.load(handle)
records = report.get("records", [])
checked = [item for item in records if item.get("proposed_action") not in ("", "none")]
print(f"report_records={len(records)}")
print(f"action_targets={len(checked)}")
print("Use --apply to recompute and apply a current plan; this mode only rereads inventory.")
PY
  rm -rf "$verify_dir"
  return 0
}

self_test() {
  local test_dir mock mock_log report_dir report_json
  test_dir="$(mktemp -d "${TMPDIR:-.}/hermes-plugin-self-test.XXXXXX")" || return "$EXIT_INTERNAL"
  mock="$test_dir/mock-hermes"
  mock_log="$test_dir/mutations.log"
  report_dir="$test_dir/report"
  cat > "$mock" <<'MOCK'
#!/usr/bin/env bash
set -u
log_file="${MOCK_LOG:?}"
if [[ "$1" != "plugins" ]]; then
  exit 2
fi
case "${2:-}" in
  list)
    cat <<'JSON'
[{"name":"good-disabled","status":"not enabled","source":"user","version":"1.0.0","description":"local test plugin"},{"name":"credential-plugin","status":"disabled","source":"user","version":"1.0.0","description":"Requires DEMO_API_KEY"},{"name":"bad-plugin","status":"enabled","source":"user","version":"1.0.0","description":"local test plugin"},{"name":"deepinfra","status":"enabled","source":"bundled","version":"1.0.0","description":"image generation backend"},{"name":"deepinfra","status":"enabled","source":"bundled","version":"1.0.0","description":"video generation backend"},{"name":"home-dashboard","status":"enabled","source":"git","version":"1.0.0","description":"local dashboard"}]
JSON
    ;;
  show)
    key="${3:-}"
    case "$key" in
      deepinfra|image_gen/deepinfra) name="deepinfra"; exact="image_gen/deepinfra"; source="bundled"; status="enabled" ;;
      video_gen/deepinfra) name="deepinfra"; exact="video_gen/deepinfra"; source="bundled"; status="enabled" ;;
      good-disabled) name="good-disabled"; exact="good-disabled"; source="user"; status="not enabled" ;;
      credential-plugin) name="credential-plugin"; exact="credential-plugin"; source="user"; status="disabled" ;;
      bad-plugin) name="bad-plugin"; exact="bad-plugin"; source="user"; status="enabled" ;;
      home-dashboard) name="home-dashboard"; exact="home-dashboard"; source="git"; status="enabled" ;;
      *) printf 'Plugin %s not found\n' "$key"; exit 1 ;;
    esac
    printf '%s v1.0.0\nStatus: %s\nSource: %s\nKey: %s\n' "$name" "$status" "$source" "$exact"
    ;;
  doctor)
    key="${4:-}"
    printf 'Plugin Doctor: /mock/plugins/%s\n' "$key"
    if [[ "$key" == "bad-plugin" ]]; then
      printf 'ERROR: TOKEN=fixture_value\n'
      exit 1
    fi
    printf 'OK: runtime discovery, manifest parsing, import, and registration passed\n'
    ;;
  compat)
    path="${4:-}"
    if [[ "$path" == *home-dashboard* ]]; then
      printf '{"plugins":{"home-dashboard":[{"file":"plugin.py","line":1,"old":"old.import","new":"new.import"}]}}\n'
      exit 1
    fi
    printf '{"plugins":{}}\n'
    ;;
  enable|disable|remove)
    printf '%s\n' "$*" >> "$log_file"
    ;;
  *)
    exit 2
    ;;
esac
MOCK
  chmod +x "$mock" || {
    rm -rf "$test_dir"
    return "$EXIT_INTERNAL"
  }

  HERMES_BIN="$mock" REPORT_DIR="$report_dir" MOCK_LOG="$mock_log" "$SCRIPT_PATH" --dry-run
  local dry_rc=$?
  if (( dry_rc != 0 )); then
    printf 'self test dry run failed with exit %s\n' "$dry_rc" >&2
    rm -rf "$test_dir"
    return "$EXIT_INTERNAL"
  fi
  if [[ -s "$mock_log" ]]; then
    printf 'self test found mutation calls during dry run\n' >&2
    rm -rf "$test_dir"
    return "$EXIT_INTERNAL"
  fi
  report_dir="$(tr -d '\r\n' < "$report_dir/latest.txt")"
  report_json="$report_dir/plugin-reconciliation.json"
  if ! "$PYTHON_BIN" - "$report_json" <<'PY'
import json
import sys
with open(sys.argv[1], encoding="utf-8") as handle:
    report = json.load(handle)
records = report["records"]
assert len(records) == 6, len(records)
keys = {item["exact_key"] for item in records}
assert "image_gen/deepinfra" in keys
assert "video_gen/deepinfra" in keys
credential = next(item for item in records if item["display_name"] == "credential-plugin")
assert credential["credential_gate"] == "declared"
assert credential["proposed_action"] == "enable"
assert credential["expected_runtime_state"] == "inactive"
bad = next(item for item in records if item["display_name"] == "bad-plugin")
assert bad["proposed_action"] == "disable_remove"
assert bad["compatibility"] == "incompatible"
home = next(item for item in records if item["display_name"] == "home-dashboard")
assert home["proposed_action"] == "disable_remove"
assert all("fixture_value" not in str(item) for item in records)
assert any("[REDACTED]" in str(item) for item in records)
PY
  then
    printf 'self test report assertions failed\n' >&2
    rm -rf "$test_dir"
    return "$EXIT_INTERNAL"
  fi
  if HERMES_BIN="$mock" REPORT_DIR="$test_dir/no-confirm" MOCK_LOG="$mock_log" "$SCRIPT_PATH" --apply >/dev/null 2>&1; then
    printf 'self test accepted apply without confirmation\n' >&2
    rm -rf "$test_dir"
    return "$EXIT_INTERNAL"
  fi
  if [[ -s "$mock_log" ]]; then
    printf 'self test found mutation calls without confirmation\n' >&2
    rm -rf "$test_dir"
    return "$EXIT_INTERNAL"
  fi
  printf 'self test passed: inventory, duplicate keys, credential gating, redaction, failure continuation, dry run, and apply confirmation\n'
  rm -rf "$test_dir"
  return 0
}

main() {
  local arg
  if (( $# == 0 )); then
    usage
    return "$EXIT_USAGE"
  fi
  while (( $# > 0 )); do
    arg="$1"
    case "$arg" in
      --help|-h) usage; return 0 ;;
      --inventory) MODE="inventory" ;;
      --dry-run) MODE="dry-run" ;;
      --apply) MODE="apply" ;;
      --confirm-uninstall) CONFIRM_UNINSTALL=1 ;;
      --verify) MODE="verify" ;;
      --self-test) MODE="self-test" ;;
      *) fail_usage "unknown argument: $arg"; return "$EXIT_USAGE" ;;
    esac
    shift
  done

  if [[ -n "${PLUGIN_RECONCILE_ASSUME_YES:-}" && "${PLUGIN_RECONCILE_ASSUME_YES}" == "1" ]]; then
    CONFIRM_UNINSTALL=1
  fi
  if [[ "$MODE" == "self-test" ]]; then
    self_test
    return $?
  fi
  if [[ "$MODE" == "" ]]; then
    return "$EXIT_USAGE"
  fi
  if [[ "$MODE" == "apply" && "$CONFIRM_UNINSTALL" != "1" ]]; then
    printf 'Apply blocked. Recompute and review a dry run, then pass --confirm-uninstall.\n' >&2
    return "$EXIT_BLOCKED"
  fi
  if ! command -v "$PYTHON_BIN" >/dev/null 2>&1; then
    printf 'Python executable is unavailable: %s\n' "$PYTHON_BIN" >&2
    return "$EXIT_INTERNAL"
  fi
  if [[ "$MODE" == "inventory" ]]; then
    run_inventory_mode
    return $?
  fi
  if [[ "$MODE" == "verify" ]]; then
    run_verify_mode
    return $?
  fi

  if [[ "$MODE" == "apply" ]]; then
    if ! acquire_lock; then
      return "$EXIT_BLOCKED"
    fi
  fi
  if ! prepare_run_dir; then
    return "$EXIT_INTERNAL"
  fi
  if ! run_audit "$MODE"; then
    local audit_rc=$?
    write_reports "$audit_rc" || true
    return "$audit_rc"
  fi

  local final_rc=0
  if [[ "$MODE" == "apply" ]]; then
    apply_actions
    verify_postconditions
    if (( ACTION_FAILURE_COUNT > 0 )); then final_rc="$EXIT_ACTION"; fi
    if (( VERIFY_FAILURE_COUNT > 0 )); then final_rc="$EXIT_VERIFY"; fi
    if (( BLOCKED_COUNT > 0 && final_rc == 0 )); then final_rc="$EXIT_BLOCKED"; fi
  fi
  write_reports "$final_rc" || return "$EXIT_INTERNAL"
  return "$final_rc"
}

main "$@"
exit $?
