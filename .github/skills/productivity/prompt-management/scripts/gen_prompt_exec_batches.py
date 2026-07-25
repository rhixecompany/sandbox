#!/usr/bin/env python3
"""
Generate delegation batch definitions for executing SAFE prompts across a library.

Reads a manifest (docs/prompt-exec-manifest.json) produced by scanning prompts/:
  each entry: {file, name, unsafe_side_effect: bool, ...}
Emits docs/safe_batches.json: list of batches, each <= MAX tasks (default 3).

Each task context is self-contained: absolute prompt path, inline-body-authoritative note,
and a results/<name>.output.md target. Designed to feed delegate_task per batch.

Usage:
  python3 scripts/gen_prompt_exec_batches.py            # uses ./docs/ defaults
  python3 scripts/gen_prompt_exec_batches.py --batch 3 --base /abs/SandBox
"""
import json
import re
import argparse
from pathlib import Path

PROMPT = """Workspace: BASE
Read the prompt file `PROMPT_PATH` in full. Treat its inline body (Goal/Context/Phases/Rules/Steps) as the AUTHORITATIVE execution spec.
Facts about the repo:
- templates/_shared/* now exists at repo root (templates/_shared/).
- Per-prompt templates/<name>/*.md DO NOT exist in this repo; the inline body is the only spec. Do NOT fabricate missing template content.
- Produce a REAL, useful artifact per the prompt's stated Outputs/Goal. Do not write stubs or placeholders.
- Write your final artifact to RESULT_PATH with real content.
- If the prompt needs external services/credentials (Azure, GitHub, Docker) that are unavailable, instead write a concise dry-run analysis of what it WOULD do and why it is blocked — still a real artifact, clearly labeled.
- Report in <=8 lines: action taken, artifact path, any missing-template refs skipped.
Respond in English."""


def main():
    ap = argparse.ArgumentParser()
    ap.add_argument("--base", default=str(Path.home() / "Desktop/SandBox"))
    ap.add_argument("--manifest", default="docs/prompt-exec-manifest.json")
    ap.add_argument("--out", default="docs/safe_batches.json")
    ap.add_argument("--batch", type=int, default=3)
    args = ap.parse_args()

    base = Path(args.base)
    manifest = json.loads((base / args.manifest).read_text(encoding="utf"))
    safe = [m for m in manifest if not m.get("unsafe_side_effect")]

    batches, cur = [], []
    for m in safe:
        name = m["name"]
        ctx = (PROMPT
               .replace("BASE", str(base).replace("/", "\\"))
               .replace("PROMPT_PATH", str(base / "prompts" / m["file"]).replace("/", "\\"))
               .replace("RESULT_PATH", str(base / "results" / f"{name}.output.md").replace("/", "\\")))
        cur.append({"goal": f"Execute {name} prompt and produce a real artifact.",
                    "role": "leaf", "context": ctx})
        if len(cur) == args.batch:
            batches.append(cur); cur = []
    if cur:
        batches.append(cur)

    (base / args.out).write_text(json.dumps(batches, indent=2), encoding="utf")
    print(f"Wrote {base / args.out}: {len(safe)} safe -> {len(batches)} batches x<={args.batch}")


if __name__ == "__main__":
    main()
