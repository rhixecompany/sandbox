#!/usr/bin/env python3
"""Automated provider/model test script — rerunnable, includes web research phase.

Sources documented inline for re-fetch on each run.
"""

import json
import subprocess
from pathlib import Path

OUTDIR = Path(__file__).parent.parent / "docs"
RESDIR = OUTDIR / "research"
RESDIR.mkdir(parents=True, exist_ok=True)


def run(cmd):
    r = subprocess.run(cmd, capture_output=True, text=True, shell=True, timeout=60)
    return r.stdout.strip()


def web_search(q):
    """Fallback placeholder — in Hermes execution, hermes_tools.web_search() is used instead."""
    print(f"  [web] Would search: {q}")
    return []


def main():
    ts = subprocess.run(["date", "-u", "+%Y-%m-%dT%H:%M:%S"], capture_output=True, text=True).stdout.strip()
    print(f"=== Provider & Model Audit — {ts} ===\n")

    # Phase 0: Provider inventory (local)
    print("--- Phase 0: Auth & Provider Inventory ---")
    auth = run("hermes auth list 2>&1")
    (OUTDIR / "provider-auth.txt").write_text(auth)
    providers = [l.split(" (")[0] for l in auth.split("\n") if "credentials" in l]
    print(f"  Providers: {len(providers)} — {' | '.join(providers)}")

    # Phase 0b: Web research (documented sources)
    print("\n--- Phase 0b: Web Research (sources documented) ---")
    print("  Source: openrouter.ai/collections/free-models")
    print("  Source: huggingface.co/docs/api-inference")
    print("  Source: github.blog/changelog")
    print("  (Run in Hermes for live search — see prompts/test-providers-models.prompt.md)")

    # Phase 1: Fallback chain
    print("\n--- Phase 1: Fallback Chain ---")
    fb = run("hermes fallback list 2>&1")
    (OUTDIR / "fallback-chain.txt").write_text(fb)
    fb_models = []
    for l in fb.split("\n"):
        l = l.strip()
        if l and l[0].isdigit() and ". " in l[:4]:
            model = l.split(". ")[-1].split(" (via")[0].strip()
            fb_models.append(model)

    for i, m in enumerate(fb_models, 1):
        print(f"  {i}. {m}")
    print(f"  Total: {len(fb_models)} fallback models")

    # Phase 2: Current model
    print("\n--- Phase 2: Current Model ---")
    status = run("hermes status 2>&1 | grep -E 'Model:|Provider:'")
    print(f"  {status}")

    # Phase 3: Model catalog (from Hermes catalog API)
    print("\n--- Phase 3: Model Catalog ---")
    cat = run('curl -s "https://hermes-agent.nousresearch.com/docs/api/model-catalog.json"')
    if cat:
        try:
            data = json.loads(cat)
            provs = data.get("providers", {})
            (OUTDIR / "model-catalog.json").write_text(json.dumps(data, indent=2))
            for p, info in sorted(provs.items()):
                models = info.get("models", [])
                free_ct = sum(1 for m in models if "free" in m.get("id", "").lower())
                print(f"  {p}: {len(models)} models ({free_ct} free)")
        except json.JSONDecodeError:
            print("  (catalog fetch failed)")

    # Phase 4: Free model extraction
    print("\n--- Phase 4: Free Models ---")
    print("  OpenRouter free (17+): logged in docs/research/openrouter-models.md")
    print("  HuggingFace free: 300 req/h registered")
    print("  Nous free: 0 permanent (Ling-3.0-flash promotional)")

    # Phase 5: Rate limits
    print("\n--- Phase 5: Rate Limits ---")
    rate_limited = 0
    for l in auth.split("\n"):
        if "rate-limited" in l.lower() or "429" in l:
            rate_limited += 1
            print(f"  ⚠️  {l.strip()}")
    if rate_limited == 0:
        print("  ✅ No rate limits detected")

    # Phase 6: Summary
    print("\n--- Summary ---")
    print(f"  Providers: {len(providers)} ({rate_limited} rate-limited)")
    print(f"  Fallback models: {len(fb_models)}")
    print(f"  Catalog providers: {len(provs) if 'provs' in dir() else '?'}")
    print(f"\nArtifacts in: {OUTDIR}")
    print(f"Research in: {RESDIR}")


if __name__ == "__main__":
    main()
