#!/usr/bin/env python3
"""G3 free-model benchmark runner.

For every (provider, model) pair, runs a battery of `hermes chat` probes with
per-query timeouts and records ONLY observed outcomes (success/timeout/error).
No fabricated completions. Output: results/models-benchmark-2026-09-11.md.

Probes: latency, accuracy, context, capabilities, tools, vision (flag-gated).
Usage: python scripts/model_benchmark_2026.py [--provider opencode-zen|openrouter|nous|all] [--limit N]
"""
from __future__ import annotations

import argparse
import json
import statistics
import subprocess
import sys
import time
from pathlib import Path

ROOT = Path(__file__).resolve().parent.parent
RESULTS = ROOT / "results"
TIMEOUT = 110  # s per query; hermes chat hangs -> broken pipe/timeout treated as failure

MANIFEST = {
    "opencode-zen": [
        "deepseek-v4-flash-free",
        "muse-spark-1.3-contributor-free",
        "muse-spark-1.2-contributor-free",
        "mimo-v2.5-free",
        "ling-3.0-flash-fin-free",
        "nemotron-3-ultra-free",
        "nemotron-3.5-lightning-free",
    ],
    "openrouter": [
        "cohere/north-mini-code:free",
        "dots-studio/dots-3-note-preview:free",
        "google/gemma-4-26b-a4b-it:free",
        "google/gemma-4-31b-it:free",
        "inclusionai/ling-3.0-flash-fin:free",
        "inclusionai/ling-3.0-flash-sante:free",
        "inclusionai/ling-3.0-flash-vl:free",
        "liquid/lfm-2.5-2.6b:free",
        "nex-agi/nex-n2.5-mini:free",
        "nex-agi/nex-n2.5-pro:free",
        "nvidia/nemotron-3-nano-omni-30b-a3b-reasoning:free",
        "nvidia/nemotron-3-super-120b-a12b:free",
        "nvidia/nemotron-3-ultra-550b-a55b:free",
        "nvidia/nemotron-3.5-lightning:free",
        "openai/gpt-oss-20b:free",
        "deepseek/deepseek-r1:free",
        "meta-llama/llama-3.3-70b-instruct:free",
        "poolside/laguna-s-2.1:free",
        "poolside/laguna-xs-2.1:free",
        "thinkingmachines/inkling:free",
        "thinkingmachines/inkling-small:free",
    ],
    "nous": [
        "inclusionai/ling-3.0-flash-sante:free",
        "inclusionai/ling-3.0-flash-fin:free",
        "poolside/laguna-s-2.1:free",
        "poolside/laguna-xs-2.1:free",
        "stepfun/step-3.7-flash:free",
        "upstage/solar-pro4:free",
        "meituan/longcat-2.0:free",
    ],
}

VISION_MODELS = {
    "deepseek-v4-flash-vision-exp",  # known vision-capable
    "google/gemma-4-31b-it:free",
    "inclusionai/ling-3.0-flash-vl:free",
    "nvidia/nemotron-3-nano-omni-30b-a3b-reasoning:free",
}

PROBES = {
    "latency": "Reply with exactly the single word PONG and nothing else. (Latency probe)",
    "accuracy": "What is 17 * 43? Reply with just the number. (Accuracy probe)",
    "context": ("Repeat the number 42 exactly four times separated by spaces, then stop. "
                "(Context window probe)"),
    "capabilities": "List your capabilities in one line: context window size, knowledge cutoff if known, tools. (Capabilities probe)",
    "tools": "Do you have function/tool calling support? Reply YES or NO only. (Tools probe)",
    "vision": "Describe the image you see in this prompt you were given. If you cannot see an image, reply NO_IMAGE. (Vision probe)",
}


def run_probe(provider: str, model: str, probe: str) -> dict:
    started = time.time()
    q = PROBES[probe]
    cmd = ["hermes", "-z", q, "-m", model, "--provider", provider, "--cli"]
    try:
        r = subprocess.run(cmd, capture_output=True, text=True, timeout=TIMEOUT)
        elapsed = round(time.time() - started, 2)
    except subprocess.TimeoutExpired:
        return {"probe": probe, "status": "TIMEOUT", "seconds": TIMEOUT, "output": "", "exit": -1}
    except OSError as e:
        return {"probe": probe, "status": "ERROR", "seconds": 0, "output": str(e), "exit": -2}
    out = (r.stdout or r.stderr or "").strip()[:300]
    status = "SUCCESS" if r.returncode == 0 and out else "ERROR" if r.returncode != 0 else "EMPTY"
    return {"probe": probe, "status": status, "seconds": round(elapsed, 2), "output": out, "exit": r.returncode}


def main() -> int:
    ap = argparse.ArgumentParser()
    ap.add_argument("--provider", default="all", choices=["all", *MANIFEST])
    ap.add_argument("--limit", type=int, default=0, help="max models per provider (0 = all)")
    args = ap.parse_args()

    RESULTS.mkdir(exist_ok=True)
    providers = list(MANIFEST) if args.provider == "all" else [args.provider]
    all_rows = []
    for prov in providers:
        models = MANIFEST[prov][: args.limit] if args.limit else MANIFEST[prov]
        for model in models:
            print(f"[{time.strftime('%H:%M:%S')}] {prov}/{model} ...", flush=True)
            row = {"provider": prov, "model": model}
            for probe in PROBES:
                if probe == "vision" and model not in VISION_MODELS:
                    continue
                row[probe] = run_probe(prov, model, probe)
            all_rows.append(row)
            # incremental checkpoint
            (RESULTS / "benchmark-checkpoint.json").write_text(
                json.dumps(all_rows, indent=1), encoding="utf-8")

    # --- report ---
    lines = ["# Free-Model Benchmark — 2026-09-11", "", "Query outcomes: SUCCESS / TIMEOUT / ERROR / EMPTY — observed only.", ""]
    for prov, models in MANIFEST.items():
        lines += [f"## {prov} ({len(models)} models)", "", "| Model | #Probes | SUCCESS | TIMEOUT/ERROR/EMPTY |", "|---|---|---|---|"]
        prov_rows = [r for r in all_rows if r["provider"] == prov]
        for r in prov_rows:
            probes = [k for k in PROBES if k in r]
            ok = sum(1 for k in probes if r[k]["status"] == "SUCCESS")
            bad = [f"{k}:{r[k]['status']}" for k in probes if r[k]["status"] != "SUCCESS"]
            lines.append(f"| {r['model']} | {len(probes)} | {ok} | {', '.join(bad) or 'all ok'} |")
        lines.append("")
    lines += ["## Completing queries (all probes SUCCESS)", ""]
    for r in all_rows:
        probes = [k for k in PROBES if k in r]
        if all(r[k]["status"] == "SUCCESS" for k in probes):
            lat = [r[k]["seconds"] for k in r if k != "model" and k != "provider" and r[k]["status"] == "SUCCESS"]
            lines.append(f"- {r['provider']}/{r['model']} ({'~' + str(round(statistics.mean(lat), 1)) + 's/probe' if lat else 'n/a'})")
    out = RESULTS / "models-benchmark-2026-09-11.md"
    out.write_text("\n".join(lines) + "\n", encoding="utf-8", newline="\n")
    (RESULTS / "models-benchmark-2026-09-11.json").write_text(json.dumps(all_rows, indent=1), encoding="utf-8")
    print(f"\nfinisher: {len(all_rows)} models benchmarked -> {out}")
    return 0


if __name__ == "__main__":
    sys.exit(main())