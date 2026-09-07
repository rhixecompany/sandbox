#!/usr/bin/env python3
"""Run all probe-<n>-*.txt tasks, capture results into probe-live-template.md.

For each probe file, look up the (provider, model_id) from the catalog, then
invoke `hermes chat` synchronously with a per-probe timeout. Append a row to
templates/probe-live-template.md with the result.

Run:
    python scripts/run_probes.py [--probe N] [--budget 45] [--concurrency 4]

Outputs:
    templates/probe-live-template.md (one row per probed model)
    .hermes/reports/test-providers-probe-results.json (full transcript)
"""
from __future__ import annotations

import argparse
import json
import re
import subprocess
import time
from concurrent.futures import ThreadPoolExecutor, as_completed
from datetime import datetime, timezone
from pathlib import Path

REPO_ROOT = Path(__file__).resolve().parents[5]
PROBES_DIR = REPO_ROOT / ".github/prompts/operations/test-providers-models/probes"
CATALOG = REPO_ROOT / ".github/prompts/operations/test-providers-models/templates/free-model-catalog.md"
TEMPLATE = REPO_ROOT / ".github/prompts/operations/test-providers-models/templates/probe-live-template.md"
RESULTS_JSON = REPO_ROOT / ".hermes/reports/test-providers-probe-results.json"
HERMES_BIN = "hermes"

PROBE_QUESTION = (
    "Answer in one paragraph: what is your knowledge cutoff date, what is "
    "your context length, do you support reasoning, and what is your max "
    "output tokens?"
)


def load_catalog() -> list[dict[str, str]]:
    """Parse the catalog table into a list of (provider, model_id) rows."""
    if not CATALOG.exists():
        return []
    rows: list[dict[str, str]] = []
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
        HERMES_BIN, "chat",
        "--provider", provider,
        "--model", model_id,
        "-q", PROBE_QUESTION,
        "--oneshot", "--yolo", "--run-budget", str(budget),
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
            "started_at": datetime.now(timezone.utc).isoformat(),
        }
    except subprocess.TimeoutExpired:
        return {
            "file": probe_path.name, "provider": provider, "model": model_id,
            "exit": -1, "elapsed_s": round(time.time() - started, 1),
            "error": "timeout", "started_at": datetime.now(timezone.utc).isoformat(),
        }
    except Exception as exc:
        return {
            "file": probe_path.name, "provider": provider, "model": model_id,
            "exit": -1, "elapsed_s": round(time.time() - started, 1),
            "error": str(exc), "started_at": datetime.now(timezone.utc).isoformat(),
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
    text = (stdout or "") + "\n" + (stderr or "")
    patterns: list[tuple[str, str]] = [
        (r"API call failed.*HTTP 400", "model_unavailable_400"),
        (r"HTTP 401", "auth_failed_401"),
        (r"HTTP 402", "exhausted_402"),
        (r"HTTP 403", "auth_failed_403"),
        (r"HTTP 404", "model_not_found_404"),
        (r"HTTP 429", "rate_limited_429"),
        (r"rate-limited", "rate_limited"),
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
        m = re.search(r"\b(january|february|march|april|may|june|july|august|september|october|november|december)\s+(20\d{2})\b", text)
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
    if re.search(r"\b(i do|i can)\s+support\s+reasoning\b", text) or "yes" in text and "reason" in text:
        claims["reasoning"] = "yes"
    elif re.search(r"\b(i do not|i don't)\s+support\s+reasoning\b", text):
        claims["reasoning"] = "no"
    m = re.search(r"max(?:imum)?\s*output[^.]{0,40}?(\d{1,5}(?:,\d{3})*|\d+)\s*k?\b", text)
    if m:
        claims["max_output"] = m.group(1).replace(",", "")
    return claims


def render_live(rows: list[dict]) -> str:
    now = datetime.now(timezone.utc).strftime("%Y-%m-%d %H:%M UTC")
    body = "| # | Provider | Model | Exit | Elapsed (s) | Failure | Knowledge Cutoff | Context | Reasoning | Max Output |\n"
    body += "|---|----------|-------|------|-------------|---------|------------------|---------|-----------|------------|\n"
    for r in rows:
        idx = r.get("index", "?")
        prov = r.get("provider", "?")
        model = r.get("model", "?")
        exit_code = r.get("exit", -1)
        elapsed = r.get("elapsed_s", "?")
        failure = r.get("failure") or {}
        failure_label = failure.get("reason", "") if failure.get("failed") else ""
        claims = r.get("claims", {})
        kc = claims.get("knowledge_cutoff") or "?"
        ctx = claims.get("context_length") or "?"
        rsn = claims.get("reasoning") or "?"
        mxo = claims.get("max_output") or "?"
        body += f"| {idx} | `{prov}` | `{model}` | {exit_code} | {elapsed} | {failure_label} | {kc} | {ctx} | {rsn} | {mxo} |\n"
    return f"""---
name: probe-live
description: Live results from the most recent probe run, captured by `scripts/run_probes.py` on {now}.
---

# Probe results -- live -- {now}

> Source: `hermes chat --oneshot --yolo --run-budget 45` per `probes/probe-*.txt` task file.
> Exit 0 = model returned a response; Exit -2 = a known hermes failure marker was detected (see Failure column).
> Knowledge cutoff / context / reasoning / max output are heuristically extracted from the model's free-form response; "?" means the model did not state a value.

{body}
"""


def main() -> int:
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("--probe", type=int, default=None, help="Run only the Nth probe (1-indexed)")
    parser.add_argument("--budget", type=int, default=45, help="Per-probe run budget in seconds")
    parser.add_argument("--concurrency", type=int, default=4, help="Number of concurrent probes")
    parser.add_argument("--tmp-dir", type=Path, default=REPO_ROOT / ".hermes/reports/probe-logs", help="Per-probe stdout/stderr capture dir")
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

    # Build a list of (probe_file, provider, model_id) joined by catalog index.
    tasks: list[tuple[Path, str, str]] = []
    for i, p in enumerate(probe_files, 1):
        row = next((r for r in catalog if r["index"] == i), None)
        if row is None:
            print(f"  SKIP: no catalog row for index {i}")
            continue
        tasks.append((p, row["provider"], row["model_id"]))

    results: list[dict] = []
    if args.concurrency > 1:
        with ThreadPoolExecutor(max_workers=args.concurrency) as ex:
            futures = {ex.submit(run_one, p, prov, mid, args.budget, args.tmp_dir): (i, p, prov, mid)
                       for i, (p, prov, mid) in enumerate(tasks, 1)}
            for fut in as_completed(futures):
                i, p, prov, mid = futures[fut]
                r = fut.result()
                r["index"] = i
                response = extract_response_text(r.get("stdout_tail", ""))
                r["response"] = response[:1500]
                r["failure"] = detect_failure(r.get("stdout_tail", ""), r.get("stderr_tail", ""), r["exit"])
                if r["failure"].get("failed"):
                    r["exit"] = -2
                r["claims"] = parse_model_claims(response)
                results.append(r)
                print(f"  [{i:02d}/{len(tasks)}] {prov}:{mid} exit={r['exit']} elapsed={r.get('elapsed_s','?')}s"
                      f"{' FAIL=' + r['failure'].get('reason','?') if r['failure'].get('failed') else ''}")
    else:
        for i, (p, prov, mid) in enumerate(tasks, 1):
            r = run_one(p, prov, mid, args.budget, args.tmp_dir)
            r["index"] = i
            response = extract_response_text(r.get("stdout_tail", ""))
            r["response"] = response[:1500]
            r["failure"] = detect_failure(r.get("stdout_tail", ""), r.get("stderr_tail", ""), r["exit"])
            if r["failure"].get("failed"):
                r["exit"] = -2
            r["claims"] = parse_model_claims(response)
            results.append(r)
            print(f"  [{i:02d}/{len(tasks)}] {prov}:{mid} exit={r['exit']} elapsed={r.get('elapsed_s','?')}s"
                  f"{' FAIL=' + r['failure'].get('reason','?') if r['failure'].get('failed') else ''}")

    results.sort(key=lambda r: r.get("index", 0))
    TEMPLATE.write_text(render_live(results), encoding="utf-8")
    print(f"  WROTE: {TEMPLATE} ({len(results)} rows)")
    RESULTS_JSON.parent.mkdir(parents=True, exist_ok=True)
    RESULTS_JSON.write_text(json.dumps(results, indent=2, ensure_ascii=False), encoding="utf-8")
    print(f"  WROTE: {RESULTS_JSON}")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
