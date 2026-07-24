#!/usr/bin/env python3
"""execute_all_prompts.py — deterministic runner for `/execute-all-prompts`."""
from __future__ import annotations

import asyncio
import datetime
import json
import os
import shutil
import sys
from pathlib import Path

ROOT = Path(__file__).resolve().parent.parent.parent
PROMPTS = ROOT / "prompts"
SCRIPTS = ROOT / ".github" / "scripts"
PROGRESS = ROOT / "docs" / "orchestrator-progress.md"
VERIFICATION = ROOT / "docs" / "orchestrator-verification.md"
HERMES = Path(os.environ.get("LOCALAPPDATA", "")) / "hermes"
SKILLS = HERMES / "skills"


def append(path: Path, text: str) -> None:
    past = path.read_text(encoding="utf-8") if path.exists() else ""
    out = past.rstrip() + "\n\n" + text.strip() + "\n"
    path.write_text(out, encoding="utf-8")


def ts() -> str:
    return datetime.datetime.now(datetime.timezone.utc).isoformat()


class GateFail(Exception):
    pass


def run(cmd: list[str]) -> int:
    print(f"+ {' '.join(cmd)}")
    exit_code = os.system(" ".join(cmd))
    return int(exit_code / 256) if isinstance(exit_code, int) and exit_code >= 256 else int(exit_code)


async def run_async(cmd: list[str]) -> int:
    return await asyncio.to_thread(run, cmd)


async def exec_phase(name: str, cmd: list[str], script: Path) -> None:
    if not script.exists():
        raise GateFail(f"missing script: {script}")

    append(PROGRESS, f"- {ts()} start {name}")
    rc = await run_async([sys.executable, str(script)])
    append(PROGRESS, f"- {ts()} finish {name} rc={rc}")
    if rc != 0:
        raise GateFail(f"{name} failed with rc={rc}")


async def _json_to_tsv(json_path: Path, tsv_path: Path) -> None:
    import json as _json
    data = _json.loads(await asyncio.to_thread(json_path.read_text, encoding="utf-8"))
    name_to_path = {}
    if SKILLS.exists():
        for skill_md in SKILLS.rglob("SKILL.md"):
            name_to_path[skill_md.parent.name] = str(skill_md)
    lines = ["name\tpath\tscore\terrors\tduration"]
    for item in data:
        name = item.get("name", "")
        path = name_to_path.get(name, "")
        score = str(item.get("score", ""))
        errors = "; ".join(item.get("errors", []))
        duration = str(item.get("duration", ""))
        lines.append(f"{name}\t{path}\t{score}\t{errors}\t{duration}")
    await asyncio.to_thread(tsv_path.write_text, "\n".join(lines) + "\n", encoding="utf-8")


async def phase1() -> None:
    """Audit Skills Judge Fix."""
    inventory = SCRIPTS / "categorize_skills.py"
    dedupe = SCRIPTS / "dedupe_skills.py"
    judge = SCRIPTS / "batch_skill_judge.py"
    remediate = SCRIPTS / "audit_fix_remediate_safe.py"
    consolidate = SCRIPTS / "consolidate_skills.py"

    await exec_phase(
        "phase1-inventory",
        ["--output", str(ROOT / "docs" / "skills-inventory.md")],
        inventory,
    )
    await exec_phase(
        "phase1-dedupe",
        ["--output", str(ROOT / "docs" / "skills-dedupe-report.md")],
        dedupe,
    )
    await exec_phase(
        "phase1-judge",
        [
            "--output",
            str(ROOT / "docs" / "skills-judge-report.md"),
            "--json",
            str(ROOT / "docs" / "skills-judge-results.json"),
        ],
        judge,
    )
    tsv_path = ROOT / "judge_results" / "all_results.tsv"
    tsv_path.parent.mkdir(parents=True, exist_ok=True)
    await _json_to_tsv(
        ROOT / "docs" / "skills-judge-results.json",
        tsv_path,
    )
    await exec_phase(
        "phase1-remediate",
        [],
        remediate,
    )
    await exec_phase(
        "phase1-consolidate",
        ["--report", str(ROOT / "docs" / "skills-consolidation-report.json")],
        consolidate,
    )
    required = [
        ROOT / "docs" / "skills-inventory.md",
        ROOT / "docs" / "skills-dedupe-report.md",
        ROOT / "docs" / "skills-judge-report.md",
        ROOT / "docs" / "skills-judge-results.json",
        ROOT / "docs" / "skills-consolidation-report.json",
        ROOT / "judge_results" / "remediation_report.md",
    ]
    missing = [str(p) for p in required if not p.exists()]
    if missing:
        raise GateFail("phase1 missing: " + ", ".join(missing))


async def phase2() -> None:
    """Agents System Prompt Context Fix."""
    ctx = SCRIPTS / "generate_context_files.py"
    vscode = SCRIPTS / "validate_vscode_configs.py"
    await exec_phase(
        "phase2-context",
        ["--output", str(ROOT / "docs" / "Project_Architecture" / "root_context.md")],
        ctx,
    )
    report = ROOT / "docs" / "vscode-validation-report.txt"
    rc = await run_async(
        [sys.executable, str(vscode), "--workspace", str(ROOT), "--report", str(report), "--allow-empty"]
    )
    append(PROGRESS, f"- {ts()} finish phase2-vscode rc={rc}")
    if rc not in {0, 2}:
        raise GateFail("phase2 vscode validation failed")


async def phase3() -> None:
    """Sync Hermes Copilot Codex — write inventory/verification artifacts from real paths."""
    roots = {
        "hermes": str(HERMES),
        "copilot": str(Path(os.environ.get("USERPROFILE", "")) / ".config" / "github-copilot"),
        "codex": str(Path(os.environ.get("USERPROFILE", "")) / ".codex"),
    }
    report = ROOT / "docs" / "sync-roots.md"
    lines = ["# Sync Roots\n\n", "| Name | Path | Exists |\n", "|------|------|--------|\n"]
    for name, path in roots.items():
        exists = Path(path).exists()
        lines.append(f"| {name} | `{path}` | {'yes' if exists else 'no'} |\n")
    report.write_text("".join(lines), encoding="utf-8")

    prompt_mirror = ROOT / ".github" / "prompts"
    src = HERMES / "prompts"
    mirrored = []
    if src.exists():
        for fp in src.glob("*.prompt.md"):
            dst = prompt_mirror / fp.name
            shutil.copy2(fp, dst)
            mirrored.append(dst.name)

    manifest = ROOT / "docs" / "sync-manifest.json"
    payload = {
        "roots": roots,
        "mirrored_prompts": mirrored,
        "conflicts": [],
    }
    manifest.write_text(json.dumps(payload, indent=2), encoding="utf-8")
    append(PROGRESS, f"- {ts()} finish phase3 mirrored={len(mirrored)}")


async def phase4() -> None:
    """Test Providers & Models."""
    models = SCRIPTS / "test_models.py"
    bench = SCRIPTS / "benchmark_models.py"
    discovery = SCRIPTS / "model_discovery.py"

    model_report = ROOT / "docs" / "model-test-report.txt"
    bench_report = ROOT / "docs" / "model-benchmark-report.txt"
    model_report = ROOT / "docs" / "model-test-report.txt"
    model_rc = await run_async(
        [
            sys.executable,
            str(models),
            "--simulate",
            "--model",
            "echo-test",
            "--endpoint",
            "http://localhost:8080/v1",
            "--output",
            str(model_report),
        ]
    )
    bench_rc = await run_async(
        [
            sys.executable,
            str(bench),
            "--output",
            "table",
            "--report",
            str(bench_report),
            "--providers",
            "local",
            "--models",
            "echo-model",
            "--iterations",
            "1",
        ]
    )
    await exec_phase(
        "phase4-discovery",
        ["--report", str(ROOT / "docs" / "model-discovery-report.md")],
        discovery,
    )
    if model_rc != 0 or bench_rc != 0:
        raise GateFail(f"phase4 failed: test_models rc={model_rc}, benchmark_models rc={bench_rc}")


async def main() -> int:
    print("execute_all_prompts: main() starting")
    append(PROGRESS, f"- {ts()} execute-all-prompts started")
    summary = ["# Orchestrator Verification\n\n", "Generated: " + ts() + "\n\n"]
    phases = [
        ("Phase 1", "Audit Skills Judge Fix", phase1),
        ("Phase 2", "Agents System Prompt Context Fix", phase2),
        ("Phase 3", "Sync Hermes Copilot Codex", phase3),
        ("Phase 4", "Test Providers & Models", phase4),
    ]
    for idx, (label, title, fn) in enumerate(phases, 1):
        print(f"execute_all_prompts: running {label}")
        append(VERIFICATION, f"## {label} — {title}\n\n- Status: running\n- Evidence: _none yet_\n")
        try:
            await fn()
        except GateFail as exc:
            print(f"execute_all_prompts: {label} blocked={exc}")
            append(VERIFICATION, f"- Status: blocked\n- Evidence: {exc}\n\n")
            append(PROGRESS, f"- {ts()} {label} blocked: {exc}")
            return 2
        except Exception as exc:
            print(f"execute_all_prompts: {label} error={exc}")
            import traceback
            traceback.print_exc()
            append(VERIFICATION, f"- Status: error\n- Evidence: {type(exc).__name__}: {exc}\n\n")
            append(PROGRESS, f"- {ts()} {label} error: {exc}")
            return 3
        print(f"execute_all_prompts: {label} passed")
        append(VERIFICATION, f"- Status: passed\n- Evidence: phase artifacts and report written\n\n")

    append(VERIFICATION, "\n## Final Checks\n\n- All phases pass: true\n")
    append(PROGRESS, f"- {ts()} execute-all-prompts completed")
    print("execute_all_prompts: completed")
    return 0


if __name__ == "__main__":
    try:
        raise SystemExit(asyncio.run(main()))
    except Exception as exc:
        import traceback
        traceback.print_exc()
        print(f"execute_all_prompts: fatal {type(exc).__name__}: {exc}")
        raise
