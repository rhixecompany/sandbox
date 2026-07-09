#!/usr/bin/env python3
"""
Generate delegation batch definitions for executing SAFE prompts.

Reads docs/prompt-exec-manifest.json (produced by scan). For each safe prompt,
emits a self-contained subagent task spec that:
  - reads prompts/<name>.prompt.md
  - treats inline body as authoritative (per-prompt templates/<name>/*.md are absent)
  - executes against the real workspace and writes results/<name>.output.md

Output: docs/safe_batches.json  (list of batches; each batch <= 3 tasks)
Used by the orchestrator to call delegate_task per batch.
"""
import json
from pathlib import Path

BASE = Path.home() / "Desktop/SandBox"
MANIFEST = BASE / "docs" / "prompt-exec-manifest.json"
OUT = BASE / "docs" / "safe_batches.json"
BATCH = 3

PROMPT = """Workspace: C:\\Users\\Alexa\\Desktop\\SandBox
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
    manifest = json.loads(MANIFEST.read_text(encoding="utf"))
    safe = [m for m in manifest if not m["unsafe_side_effect"]]
    batches = []
    cur = []
    for m in safe:
        name = m["name"]
        task = {
            "goal": f"Execute {name} prompt and produce a real artifact.",
            "role": "leaf",
            "context": PROMPT
                .replace("PROMPT_PATH", f"C:\\Users\\Alexa\\Desktop\\SandBox\\prompts\\{m['file']}")
                .replace("RESULT_PATH", f"C:\\Users\\Alexa\\Desktop\\SandBox\\results\\{name}.output.md"),
        }
        cur.append(task)
        if len(cur) == BATCH:
            batches.append(cur)
            cur = []
    if cur:
        batches.append(cur)
    OUT.write_text(json.dumps(batches, indent=2), encoding="utf")
    print(f"Wrote {OUT}")
    print(f"Safe prompts: {len(safe)} -> {len(batches)} batches of <= {BATCH}")


if __name__ == "__main__":
    main()
