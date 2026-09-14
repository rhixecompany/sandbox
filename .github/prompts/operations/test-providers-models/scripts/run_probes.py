#!/usr/bin/env python3
"""Run all probe-<n>-*.txt tasks, capture results into probe-live-template.md.

For each probe file, look up the (provider, model_id) from the catalog, then
invoke `hermes chat` synchronously with a per-probe timeout. Append a row to
templates/probe-live-template.md with the result.

Run:
    python scripts/run_probes.py [--probe N] [--budget 45] [--concurrency 4]

Outputs:
    templates/probe-live-template.md (one row per probed model)
    ./reports/test-providers-probe-results.json (full transcript)
"""

from __future__ import annotations

import argparse
import json
import re
import subprocess
import time
from concurrent.futures import ThreadPoolExecutor, as_completed
from datetime import UTC, datetime
from pathlib import Path
from typing import TypedDict

from provider_status import (
    SELF_PROFILE_PROMPT,
    auth_rate_limited_providers,
    is_rate_limit_error,
    provider_is_rate_limited,
    skipped_result,
)

REPO_ROOT = Path(__file__).resolve().parents[5]
PROBES_DIR = REPO_ROOT / ".github/prompts/operations/test-providers-models/probes"
CATALOG = REPO_ROOT / ".github/prompts/operations/test-providers-models/templates/free-model-catalog.md"
TEMPLATE = REPO_ROOT / ".github/prompts/operations/test-providers-models/templates/probe-live-template.md"
RESULTS_JSON = REPO_ROOT / "./reports/test-providers-probe-results.json"
HERMES_BIN = "hermes"

PROBE_QUESTION = SELF_PROFILE_PROMPT


class CatalogRow(TypedDict):
    index: int
    provider: str
    model_id: str


def load_catalog() -> list[CatalogRow]:
    """Parse the catalog table into a list of (provider, model_id) rows."""
    if not CATALOG.exists():
        return []
    rows: list[CatalogRow] = []
    for line in CATALOG.read_text(encoding="utf-8").splitlines():
        # | 1 | `openrouter` | `cohere/north-mini-code:free` | ...
        m = re.match(r"^\|\s*(\d+)\s*\|\s*`?([\w-]+)`?\s*\|\s*`?([^`]+)`?\s*\|", line)
        if m:
            rows.append({"index": int(m.group(1)), "provider": m.group(2), "model_id": m.group(3).strip()})
    return rows


def run_one(probe_path: Path, provider: str, model_id: str, budget: int, tmp_dir: Path) -> dict:
    """Run `hermes chat` for one probe and return a result dict.

    Uses file-based stdout/stderr capture instead of subprocess pipes to
    avoid Windows pipe-buffer deadlocks when 4+ hermes chat processes run
    in parallel.
    """
    started = time.time()
    stdout_file = tmp_dir / f"{probe_path.stem}.stdout.log"
    stderr_file = tmp_dir / f"{probe_path.stem}.stderr.log"
    cmd = [
        HERMES_BIN,
        "chat",
        "--provider",
        provider,
        "--model",
        model_id,
        "-q",
        PROBE_QUESTION,
        "--oneshot",
        "--yolo",
        "--run-budget",
        str(budget),
    ]
    try:
        with stdout_file.open("w", encoding="utf-8") as out_f, stderr_file.open("w", encoding="utf-8") as err_f:
            result = subprocess.run(cmd, stdout=out_f, stderr=err_f, timeout=budget + 20)
        elapsed = time.time() - started
        return {
            "file": probe_path.name,
            "provider": provider,
            "model": model_id,
            "exit": result.returncode,
            "elapsed_s": round(elapsed, 1),
            "stdout_tail": stdout_file.read_text(encoding="utf-8", errors="ignore")[-4000:],
            "stderr_tail": stderr_file.read_text(encoding="utf-8", errors="ignore")[-2000:],
            "started_at": datetime.now(UTC).isoformat(),
        }
    except subprocess.TimeoutExpired:
        return {
            "file": probe_path.name,
            "provider": provider,
            "model": model_id,
            "exit": -1,
            "elapsed_s": round(time.time() - started, 1),
            "error": "timeout",
            "started_at": datetime.now(UTC).isoformat(),
        }
    except Exception as exc:
        return {
            "file": probe_path.name,
            "provider": provider,
            "model": model_id,
            "exit": -1,
            "elapsed_s": round(time.time() - started, 1),
            "error": str(exc),
            "started_at": datetime.now(UTC).isoformat(),
        }


def extract_response_text(stdout: str) -> str:
    """Pull the model's user-visible response out of the hermes chat TUI output."""
    if not stdout:
        return ""
    # Look for the `╭─ ⚕ ... ╰─` block that contains the assistant's text.
    blocks = re.findall(r"╭─[^\n]*\n(.*?)\n╰─", stdout, re.DOTALL)
    if blocks:
        return blocks[-1].strip()
    if "Initializing agent" in stdout:
        return stdout.split("Initializing agent")[-1][-500:].strip()
    return stdout[-500:].strip()


def detect_failure(stdout: str, stderr: str, exit_code: int) -> dict:
    """Inspect stdout/stderr for known hermes failure markers and return a
    normalized failure description. Returns {} when no failure is detected.
    """
    text = f"{stdout or ''}\n{stderr or ''}\n{exit_code}"
    if is_rate_limit_error(stdout, stderr, exit_code):
        return {"failed": True, "reason": "rate_limited", "exit": exit_code}
    patterns: list[tuple[str, str]] = [
        (r"API call failed.*HTTP 400", "model_unavailable_400"),
        (r"HTTP 401", "auth_failed_401"),
        (r"HTTP 402", "exhausted_402"),
        (r"HTTP 403", "auth_failed_403"),
        (r"HTTP 404", "model_not_found_404"),
        (r"Non-retryable error", "non_retryable_error"),
        (r"Model is unavailable", "model_unavailable"),
        (r"Invalid API key", "invalid_api_key"),
    ]
    for pat, label in patterns:
        if re.search(pat, text, re.IGNORECASE):
            return {"failed": True, "reason": label, "exit": exit_code}
    return {}


def parse_model_claims(response: str) -> dict[str, str | int | None]:
    """Heuristically extract knowledge cutoff, context length, reasoning, max output."""
    text = response.lower()
    claims: dict[str, str | int | None] = {
        "knowledge_cutoff": None,
        "context_length": None,
        "reasoning": None,
        "max_output": None,
    }
    m = re.search(r"\b(20\d{2})-(\d{2})-(\d{2})\b", text)
    if m:
        claims["knowledge_cutoff"] = m.group(0)
    else:
        m = re.search(
            r"\b(january|february|march|april|may|june|july|august|september|october|november|december)\s+(20\d{2})\b",
            text,
        )
        if m:
            claims["knowledge_cutoff"] = f"{m.group(2)}-{m.group(1)[:3]}"
    m = re.search(r"\b(\d{1,3}(?:,\d{3})*|\d+)\s*k\s*(?:token|context)?", text)
    if m:
        try:
            n = int(m.group(1).replace(",", "")) * 1000
            if 1000 <= n <= 10_000_000:
                claims["context_length"] = n
        except ValueError:
            pass
    if re.search(r"\b(i do|i can)\s+support\s+reasoning\b", text) or ("yes" in text and "reason" in text):
        claims["reasoning"] = "yes"
    elif re.search(r"\b(i do not|i don't)\s+support\s+reasoning\b", text):
        claims["reasoning"] = "no"
    m = re.search(r"max(?:imum)?\s*output[^.]{0,40}?(\d{1,5}(?:,\d{3})*|\d+)\s*k?\b", text)
    if m:
        claims["max_output"] = m.group(1).replace(",", "")
    return claims


def finalize_result(index: int, probe_path: Path, provider: str, model: str, raw: dict) -> dict:
    """Normalize one subprocess result for reports and ranking."""
    result = dict(raw)
    result.update({"index": index, "file": probe_path.name, "provider": provider, "model": model})
    response = extract_response_text(result.get("stdout_tail", ""))
    result["response"] = response[:1500]
    result["failure"] = detect_failure(result.get("stdout_tail", ""), result.get("stderr_tail", ""), result["exit"])
    if result["failure"].get("failed"):
        result["exit"] = -2
    result["claims"] = parse_model_claims(response)
    if result["failure"].get("reason", "").startswith("rate_limited"):
        result["provider_rate_limited"] = True
    result["status"] = "failed" if result["failure"].get("failed") else "success"
    return result


def make_skipped_result(index: int, probe_path: Path, provider: str, model: str, reason: str) -> dict:
    """Record a model skipped without invoking `hermes chat`."""
    result = skipped_result(provider, model, reason)
    result.update(
        {
            "index": index,
            "file": probe_path.name,
            "elapsed_s": 0,
            "stdout_tail": "",
            "stderr_tail": "",
            "response": "",
            "failure": {"failed": True, "reason": reason, "exit": None},
            "claims": parse_model_claims(""),
        }
    )
    return result


def run_provider_group(
    provider: str,
    provider_tasks: list[tuple[int, Path, str]],
    budget: int,
    tmp_dir: Path,
) -> list[dict]:
    """Probe one provider sequentially and stop its remaining models on 429."""
    results: list[dict] = []
    for position, (index, probe_path, model) in enumerate(provider_tasks):
        result = finalize_result(
            index, probe_path, provider, model, run_one(probe_path, provider, model, budget, tmp_dir)
        )
        results.append(result)
        print(
            f"  {provider}:{model} status={result['status']} "
            f"exit={result.get('exit')} elapsed={result.get('elapsed_s', '?')}s"
            f"{' FAIL=' + result['failure'].get('reason', '?') if result['failure'].get('failed') else ''}"
        )
        if result["failure"].get("reason", "").startswith("rate_limited"):
            for skipped_index, skipped_path, skipped_model in provider_tasks[position + 1 :]:
                results.append(
                    make_skipped_result(
                        skipped_index,
                        skipped_path,
                        provider,
                        skipped_model,
                        "provider_rate_limited",
                    )
                )
            break
    return results


def render_live(rows: list[dict]) -> str:
    now = datetime.now(UTC).strftime("%Y-%m-%d %H:%M UTC")
    body = "| # | Provider | Model | Status | Exit | Elapsed (s) | Failure | Skip Reason | Knowledge Cutoff | Context | Reasoning | Max Output |\n"
    body += "|---|----------|-------|--------|------|-------------|---------|-------------|------------------|---------|-----------|------------|\n"
    for r in rows:
        idx = r.get("index", "?")
        prov = r.get("provider", "?")
        model = r.get("model", "?")
        status = r.get("status", "failed" if r.get("failure", {}).get("failed") else "success")
        exit_code = r.get("exit", -1)
        elapsed = r.get("elapsed_s", "?")
        failure = r.get("failure") or {}
        failure_label = failure.get("reason", "") if failure.get("failed") else ""
        skip_reason = r.get("skip_reason", "")
        claims = r.get("claims", {})
        kc = claims.get("knowledge_cutoff") or "?"
        ctx = claims.get("context_length") or "?"
        rsn = claims.get("reasoning") or "?"
        mxo = claims.get("max_output") or "?"
        body += f"| {idx} | `{prov}` | `{model}` | {status} | {exit_code if exit_code is not None else '—'} | {elapsed} | {failure_label} | {skip_reason} | {kc} | {ctx} | {rsn} | {mxo} |\n"
    return f"""---
name: probe-live
description: Live results from the most recent probe run, captured by `scripts/run_probes.py` on {now}.
---

# Probe results -- live -- {now}

> Source: `hermes chat --oneshot --yolo --run-budget 45` per `probes/probe-*.txt` task file.
> Prompt: `{PROBE_QUESTION}`
> `success` means the model returned a response; `failed` means a request error was observed; `skipped` means no `hermes chat` call was made.
> A provider-level rate-limit result skips every remaining model for that provider and marks those rows `provider_rate_limited`.
> Knowledge cutoff / context / reasoning / max output are heuristically extracted from the model's free-form response; "?" means the model did not state a value.

{body}
"""


def main() -> int:
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("--probe", type=int, default=None, help="Run only the Nth probe (1-indexed)")
    parser.add_argument("--budget", type=int, default=45, help="Per-probe run budget in seconds")
    parser.add_argument("--concurrency", type=int, default=4, help="Number of providers probed concurrently")
    parser.add_argument(
        "--tmp-dir", type=Path, default=REPO_ROOT / "./reports/probe-logs", help="Per-probe stdout/stderr capture dir"
    )
    args = parser.parse_args()

    args.tmp_dir.mkdir(parents=True, exist_ok=True)
    # Clean up prior capture files so each run is fresh.
    for old in args.tmp_dir.glob("*.log"):
        old.unlink()

    catalog = load_catalog()
    if not catalog:
        print(f"ERROR: no catalog rows parsed from {CATALOG}; run build_free_model_catalog.py first")
        return 1

    probe_files = sorted(PROBES_DIR.glob("probe-*.txt"))
    if args.probe is not None:
        probe_files = [p for p in probe_files if p.name.startswith(f"probe-{args.probe:03d}-")]
    print(f"Probes to run: {len(probe_files)} (budget={args.budget}s, concurrency={args.concurrency})")

    rate_limited, inventory_error = auth_rate_limited_providers(HERMES_BIN)
    if inventory_error:
        print(f"WARNING: {inventory_error}; runtime rate-limit detection remains enabled")
    if rate_limited:
        print(f"Providers skipped by auth preflight: {', '.join(sorted(rate_limited))}")

    # Build (catalog index, probe file, provider, model) tasks.
    tasks: list[tuple[int, Path, str, str]] = []
    for p in probe_files:
        match = re.match(r"^probe-(\d+)-", p.name)
        index = int(match.group(1)) if match else None
        row = next((r for r in catalog if r["index"] == index), None)
        if row is None:
            print(f"  SKIP: no catalog row for {p.name}")
            continue
        tasks.append((row["index"], p, row["provider"], row["model_id"]))

    results: list[dict] = []
    grouped: dict[str, list[tuple[int, Path, str]]] = {}
    for index, probe_path, provider, model in tasks:
        if provider_is_rate_limited(provider, rate_limited):
            results.append(make_skipped_result(index, probe_path, provider, model, "provider_rate_limited"))
            continue
        grouped.setdefault(provider, []).append((index, probe_path, model))

    if grouped:
        max_workers = max(1, min(args.concurrency, len(grouped)))
        with ThreadPoolExecutor(max_workers=max_workers) as ex:
            futures = {
                ex.submit(run_provider_group, provider, provider_tasks, args.budget, args.tmp_dir): provider
                for provider, provider_tasks in grouped.items()
            }
            for fut in as_completed(futures):
                results.extend(fut.result())

    results.sort(key=lambda r: r.get("index", 0))
    TEMPLATE.write_text(render_live(results), encoding="utf-8")
    print(f"  WROTE: {TEMPLATE} ({len(results)} rows)")
    RESULTS_JSON.parent.mkdir(parents=True, exist_ok=True)
    RESULTS_JSON.write_text(json.dumps(results, indent=2, ensure_ascii=False), encoding="utf-8")
    print(f"  WROTE: {RESULTS_JSON}")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
