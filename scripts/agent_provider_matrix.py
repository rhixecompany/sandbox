#!/usr/bin/env python3
"""Run a Hermes request matrix across installed profiles and authorized providers.

The runner:
- reads `hermes auth list` and `hermes profile list`
- scans `packages/**/*` for capability context
- renders a reusable prompt template
- runs the request noninteractively via `hermes chat --query-file`
- writes JSON + Markdown result artifacts

The script is intentionally dependency-free (stdlib only) so it can run in
Hermes automation, local shells, and CI without a bootstrap step.
"""

from __future__ import annotations

import argparse
import json
import os
import re
import subprocess
import sys
import tempfile
import textwrap
import time
from dataclasses import asdict, dataclass
from datetime import datetime, timezone
from pathlib import Path
from typing import Any, Iterable

try:  # Python 3.11+
    import tomllib  # type: ignore[attr-defined]
except ModuleNotFoundError:  # pragma: no cover - fallback for older interpreters
    tomllib = None  # type: ignore[assignment]

ROOT = Path(__file__).resolve().parent.parent
DEFAULT_PROMPT_PATH = ROOT / "prompts" / "agent-provider-matrix.prompt.md"
DEFAULT_PACKAGES_ROOT = ROOT / "packages"
DEFAULT_RESULTS_ROOT = ROOT / ".hermes" / "plans" / "results" / "agent-provider-matrix"
DEFAULT_REQUEST = (
    "Summarize the package capability matrix and return a normalized JSON record "
    "with provider, context, max_output, capabilities, status, result, and notes."
)
DEFAULT_MAX_OUTPUT = 1200
DEFAULT_MAX_TURNS = 20
DEFAULT_RUN_BUDGET_SECONDS = 300

PROVIDER_HEADER_RE = re.compile(r"^(?P<provider>[A-Za-z0-9_-]+) \((?P<count>\d+) credentials\):$")
PROVIDER_CRED_RE = re.compile(
    r"^\s*#(?P<index>\d+)\s+(?P<name>\S+)\s+(?P<kind>\S+)\s+(?P<detail>.*?)(?P<active>\s*←)?$"
)
PROFILE_RE = re.compile(
    r"^\s*(?P<selected>◆)?\s*(?P<name>\S+)\s+(?P<model>\S+)\s+(?P<gateway>\S+)\s+(?P<alias>\S+)\s+(?P<distribution>.+?)\s*$"
)
IGNORED_PARTS = {".git", "node_modules", "dist", "build", "__pycache__", ".venv", ".hg", ".svn"}
TEXT_SUFFIXES = {".ts", ".tsx", ".js", ".jsx", ".py", ".md", ".toml", ".json", ".yml", ".yaml", ".txt"}


@dataclass(slots=True)
class ProviderCredential:
    index: int
    name: str
    kind: str
    detail: str
    active: bool


@dataclass(slots=True)
class ProviderInventory:
    name: str
    credential_count: int
    credentials: list[ProviderCredential]


@dataclass(slots=True)
class ProfileInventory:
    name: str
    model: str
    gateway: str
    alias: str
    distribution: str
    selected: bool


@dataclass(slots=True)
class PackageInventory:
    name: str
    path: str
    language: str
    toolchain: str
    manifest: str
    files: list[str]
    capabilities: list[str]
    summary: str


@dataclass(slots=True)
class MatrixResult:
    profile: str
    provider: str
    package_context: str
    max_output: int
    capabilities: list[str]
    model: str
    command: list[str]
    exit_code: int
    duration_ms: int
    status: str
    response_excerpt: str
    result_path: str
    notes: str
    assumptions: list[str]


def parse_args() -> argparse.Namespace:
    parser = argparse.ArgumentParser(description="Run a Hermes provider/profile matrix noninteractively.")
    parser.add_argument("--hermes-bin", default="hermes", help="Hermes CLI executable (default: hermes)")
    parser.add_argument("--request", default=DEFAULT_REQUEST, help="Request text to place into the prompt template")
    parser.add_argument("--request-file", type=Path, help="Read the request text from a file instead of --request")
    parser.add_argument("--prompt-template", type=Path, default=DEFAULT_PROMPT_PATH, help="Prompt template to render")
    parser.add_argument("--packages-root", type=Path, default=DEFAULT_PACKAGES_ROOT, help="Root directory containing packages")
    parser.add_argument("--results-root", type=Path, default=DEFAULT_RESULTS_ROOT, help="Directory to write results into")
    parser.add_argument("--provider", action="append", dest="providers", help="Restrict to one or more providers (repeat or comma-separate)")
    parser.add_argument("--profile", action="append", dest="profiles", help="Restrict to one or more profiles (repeat or comma-separate)")
    parser.add_argument("--max-output", type=int, default=DEFAULT_MAX_OUTPUT, help="Output budget in characters for response excerpts")
    parser.add_argument("--max-turns", type=int, default=DEFAULT_MAX_TURNS, help="Hermes max-turns limit for each live run")
    parser.add_argument("--run-budget", type=int, default=DEFAULT_RUN_BUDGET_SECONDS, help="Hermes run budget in seconds for each live run")
    parser.add_argument("--source", default="agent-provider-matrix", help="Hermes session source tag")
    parser.add_argument("--model", help="Optional explicit Hermes model override")
    parser.add_argument("--limit-cells", type=int, help="Stop after N matrix cells (useful for smoke tests)")
    parser.add_argument("--dry-run", action="store_true", help="Render commands and artifacts without calling Hermes")
    parser.add_argument("--quiet", action="store_true", help="Reduce console noise")
    return parser.parse_args()


def run_command(command: list[str], cwd: Path | None = None, timeout: int | None = None) -> dict[str, Any]:
    started = time.perf_counter()
    completed = subprocess.run(
        command,
        cwd=str(cwd) if cwd else None,
        capture_output=True,
        text=True,
        encoding="utf-8",
        errors="replace",
        timeout=timeout,
        check=False,
    )
    elapsed_ms = int((time.perf_counter() - started) * 1000)
    return {
        "returncode": completed.returncode,
        "stdout": completed.stdout,
        "stderr": completed.stderr,
        "elapsed_ms": elapsed_ms,
    }


def read_text(path: Path) -> str:
    return path.read_text(encoding="utf-8", errors="replace")


def write_text(path: Path, text: str) -> None:
    path.parent.mkdir(parents=True, exist_ok=True)
    path.write_text(text, encoding="utf-8")


def write_json(path: Path, payload: object) -> None:
    write_text(path, json.dumps(payload, indent=2, ensure_ascii=False) + "\n")


def split_csv_or_list(values: list[str] | None) -> set[str] | None:
    if not values:
        return None
    items: set[str] = set()
    for value in values:
        for item in value.split(","):
            cleaned = item.strip()
            if cleaned:
                items.add(cleaned)
    return items or None


def dedupe_keep_order(values: Iterable[str]) -> list[str]:
    seen: set[str] = set()
    ordered: list[str] = []
    for value in values:
        if value not in seen:
            seen.add(value)
            ordered.append(value)
    return ordered


def slugify(text: str) -> str:
    cleaned = re.sub(r"[^A-Za-z0-9._-]+", "-", text.strip())
    cleaned = re.sub(r"-+", "-", cleaned).strip("-._")
    return cleaned or "item"


def truncate(text: str, limit: int) -> str:
    if len(text) <= limit:
        return text
    if limit <= 3:
        return text[:limit]
    return text[: limit - 1] + "…"


def normalize_lines(text: str) -> list[str]:
    return [line.rstrip() for line in text.splitlines()]


def parse_auth_list(text: str) -> list[ProviderInventory]:
    providers: list[ProviderInventory] = []
    current_name: str | None = None
    current_count = 0
    current_credentials: list[ProviderCredential] = []

    def flush() -> None:
        nonlocal current_name, current_count, current_credentials
        if current_name is not None:
            providers.append(
                ProviderInventory(
                    name=current_name,
                    credential_count=current_count,
                    credentials=current_credentials,
                )
            )
        current_name = None
        current_count = 0
        current_credentials = []

    for raw_line in normalize_lines(text):
        line = raw_line.strip("\n")
        if not line.strip():
            continue
        header = PROVIDER_HEADER_RE.match(line)
        if header:
            flush()
            current_name = header.group("provider")
            current_count = int(header.group("count"))
            continue
        if current_name is None:
            continue
        cred = PROVIDER_CRED_RE.match(line)
        if cred:
            detail = cred.group("detail").strip()
            # Remove the active marker if it was captured inside detail whitespace.
            detail = detail[:-1].rstrip() if detail.endswith("←") else detail
            current_credentials.append(
                ProviderCredential(
                    index=int(cred.group("index")),
                    name=cred.group("name"),
                    kind=cred.group("kind"),
                    detail=detail,
                    active=bool(cred.group("active")),
                )
            )
    flush()
    return providers


def parse_profile_list(text: str) -> list[ProfileInventory]:
    profiles: list[ProfileInventory] = []
    for raw_line in normalize_lines(text):
        line = raw_line.rstrip()
        if not line.strip():
            continue
        if line.lstrip().startswith(("Profile", "─")):
            continue
        match = PROFILE_RE.match(line)
        if not match:
            continue
        profiles.append(
            ProfileInventory(
                name=match.group("name"),
                model=match.group("model"),
                gateway=match.group("gateway"),
                alias=match.group("alias"),
                distribution=match.group("distribution").strip(),
                selected=bool(match.group("selected")),
            )
        )
    return profiles


def detect_language(manifest_path: Path) -> tuple[str, str, dict[str, Any]]:
    if manifest_path.name == "package.json":
        manifest = json.loads(read_text(manifest_path))
        name = str(manifest.get("name") or manifest_path.parent.name)
        return "typescript", name, manifest
    if manifest_path.name == "pyproject.toml":
        if tomllib is None:  # pragma: no cover - older interpreter fallback
            raise RuntimeError("Python 3.11+ tomllib is required for pyproject parsing")
        manifest = tomllib.loads(read_text(manifest_path))
        project = manifest.get("project", {}) if isinstance(manifest, dict) else {}
        tool_poetry = manifest.get("tool", {}).get("poetry", {}) if isinstance(manifest, dict) else {}
        name = str(project.get("name") or tool_poetry.get("name") or manifest_path.parent.name)
        return "python", name, manifest
    raise ValueError(f"Unsupported manifest: {manifest_path}")


def collect_package_files(root: Path) -> list[Path]:
    collected: list[Path] = []
    for candidate in root.rglob("*"):
        if not candidate.is_file():
            continue
        if any(part in IGNORED_PARTS for part in candidate.parts):
            continue
        if candidate.suffix.lower() not in TEXT_SUFFIXES and candidate.name not in {"package.json", "pyproject.toml"}:
            continue
        rel = candidate.relative_to(root)
        collected.append(rel)
    return sorted(collected, key=lambda path: path.as_posix())


def read_package_text(root: Path, files: list[Path]) -> str:
    chunks: list[str] = []
    for rel in files:
        abs_path = root / rel
        try:
            text = read_text(abs_path)
        except OSError:
            continue
        chunks.append(f"--- {rel.as_posix()} ---\n{text}\n")
    return "\n".join(chunks)


def derive_capabilities(language: str, combined_text: str, manifest: dict[str, Any]) -> list[str]:
    lowered = combined_text.lower()
    capabilities: list[str] = []

    def add(label: str, condition: bool) -> None:
        if condition:
            capabilities.append(label)

    if language == "typescript":
        add("TypeScript wrapper", True)
        deps = manifest.get("dependencies", {}) if isinstance(manifest, dict) else {}
        dev_deps = manifest.get("devDependencies", {}) if isinstance(manifest, dict) else {}
        add("OpenRouter SDK client", "@openrouter/sdk" in deps or "@openrouter/sdk" in dev_deps or "openrouter" in lowered)
        add("chat completions", "sendchat" in lowered or "chat" in lowered)
        add("streaming", "stream" in lowered)
        add("custom headers", "headers" in lowered or "httpreferer" in lowered or "apptitle" in lowered)
        add("max_tokens", "max_tokens" in lowered or "maxtokens" in lowered)
        add("temperature control", "temperature" in lowered)
        add("typed client", "class" in lowered or "interface" in lowered or "type" in lowered)
    else:
        add("Python wrapper", True)
        dependencies: list[str] = []
        if isinstance(manifest, dict):
            project = manifest.get("project", {})
            if isinstance(project, dict):
                project_deps = project.get("dependencies", []) or []
                if isinstance(project_deps, list):
                    dependencies.extend(str(item) for item in project_deps)
                elif isinstance(project_deps, dict):
                    dependencies.extend(str(key) for key in project_deps.keys())
            tool_section = manifest.get("tool", {})
            if isinstance(tool_section, dict):
                tool_poetry = tool_section.get("poetry", {})
                if isinstance(tool_poetry, dict):
                    deps = tool_poetry.get("dependencies", []) or []
                    if isinstance(deps, list):
                        dependencies.extend(str(item) for item in deps)
                    elif isinstance(deps, dict):
                        dependencies.extend(str(key) for key in deps.keys())
        add("OpenRouter client", "openrouter" in lowered or any("openrouter" in dep.lower() for dep in dependencies))
        add("chat completions", "send_chat" in lowered or "chat" in lowered)
        add("streaming", "stream" in lowered)
        add("custom headers", "headers" in lowered or "httpreferer" in lowered or "apptitle" in lowered)
        add("max_tokens", "max_tokens" in lowered or "maxtokens" in lowered)
        add("temperature control", "temperature" in lowered)
        add("dataclasses", "dataclass" in lowered)

    return dedupe_keep_order(capabilities)


def summarize_package(root: Path, manifest_path: Path) -> PackageInventory:
    language, package_name, manifest = detect_language(manifest_path)
    files = collect_package_files(root)
    combined_text = read_package_text(root, files)
    capabilities = derive_capabilities(language, combined_text, manifest)

    toolchain = "bun" if language == "typescript" else "python"
    manifest_label = manifest_path.name
    file_names = [rel.as_posix() for rel in files]

    if language == "typescript":
        summary = (
            f"TypeScript/Bun OpenRouter wrapper with {', '.join(capabilities[:4]) if capabilities else 'basic client features'}"
        )
    else:
        summary = (
            f"Python OpenRouter wrapper with {', '.join(capabilities[:4]) if capabilities else 'basic client features'}"
        )

    return PackageInventory(
        name=package_name,
        path=root.as_posix(),
        language=language,
        toolchain=toolchain,
        manifest=manifest_label,
        files=file_names,
        capabilities=capabilities,
        summary=summary,
    )


def discover_packages(packages_root: Path) -> list[PackageInventory]:
    if not packages_root.exists():
        return []
    manifest_roots: dict[Path, Path] = {}
    for manifest_name in ("package.json", "pyproject.toml"):
        for manifest_path in packages_root.rglob(manifest_name):
            if any(part in IGNORED_PARTS for part in manifest_path.parts):
                continue
            manifest_roots[manifest_path.parent] = manifest_path
    packages: list[PackageInventory] = []
    for root in sorted(manifest_roots, key=lambda path: path.as_posix()):
        packages.append(summarize_package(root, manifest_roots[root]))
    return packages


def build_package_context(packages: list[PackageInventory]) -> str:
    if not packages:
        return "No packages discovered under packages/."
    lines: list[str] = []
    for pkg in packages:
        lines.append(f"- {pkg.name} ({pkg.language}, {pkg.toolchain})")
        lines.append(f"  summary: {pkg.summary}")
        lines.append(f"  capabilities: {', '.join(pkg.capabilities) if pkg.capabilities else 'none detected'}")
        if pkg.files:
            preview = ", ".join(pkg.files[:8])
            if len(pkg.files) > 8:
                preview += f" … (+{len(pkg.files) - 8} more)"
            lines.append(f"  files: {preview}")
    return "\n".join(lines)


def build_capability_bullets(packages: list[PackageInventory]) -> str:
    unique = dedupe_keep_order(capability for package in packages for capability in package.capabilities)
    if not unique:
        return "- none detected"
    return "\n".join(f"- {cap}" for cap in unique)


def render_template(template: str, replacements: dict[str, str]) -> str:
    rendered = template
    for key, value in replacements.items():
        rendered = rendered.replace(f"{{{{{key}}}}}", value)
    return rendered


def build_command(
    hermes_bin: str,
    profile: ProfileInventory,
    provider: ProviderInventory,
    query_file: Path,
    source: str,
    max_turns: int,
    run_budget: int,
    model_override: str | None,
) -> list[str]:
    command = [
        hermes_bin,
        "-p",
        profile.name,
        "chat",
        "--query-file",
        str(query_file),
        "--provider",
        provider.name,
        "--quiet",
        "--pass-session-id",
        "--source",
        source,
        "--max-turns",
        str(max_turns),
        "--run-budget",
        str(run_budget),
    ]
    if model_override:
        command.extend(["-m", model_override])
    return command


def make_response_excerpt(stdout: str, stderr: str, max_output: int) -> str:
    text = stdout.strip() if stdout.strip() else stderr.strip()
    if not text:
        return ""
    return truncate(text, max_output)


def write_cell_artifacts(base_dir: Path, payload: dict[str, Any], request_text: str, stdout: str, stderr: str) -> Path:
    base_dir.mkdir(parents=True, exist_ok=True)
    write_text(base_dir / "request.md", request_text)
    write_text(base_dir / "stdout.txt", stdout)
    write_text(base_dir / "stderr.txt", stderr)
    result_path = base_dir / "result.json"
    write_json(result_path, payload)
    return result_path


def markdown_table(rows: list[list[str]]) -> str:
    if not rows:
        return ""
    widths = [max(len(row[i]) for row in rows) for i in range(len(rows[0]))]
    header = "| " + " | ".join(rows[0][i].ljust(widths[i]) for i in range(len(widths))) + " |"
    separator = "| " + " | ".join("-" * widths[i] for i in range(len(widths))) + " |"
    body = ["| " + " | ".join(row[i].ljust(widths[i]) for i in range(len(widths))) + " |" for row in rows[1:]]
    return "\n".join([header, separator, *body])


def make_summary_markdown(
    generated_at: str,
    providers: list[ProviderInventory],
    profiles: list[ProfileInventory],
    packages: list[PackageInventory],
    results: list[MatrixResult],
    run_dir: Path,
) -> str:
    rows = [["Profile", "Provider", "Status", "Duration ms", "Max output", "Model", "Result file"]]
    for result in results:
        rows.append(
            [
                result.profile,
                result.provider,
                result.status,
                str(result.duration_ms),
                str(result.max_output),
                result.model,
                Path(result.result_path).name,
            ]
        )

    package_section = []
    for pkg in packages:
        package_section.append(f"- {pkg.name} (`{pkg.language}`) — {pkg.summary}")

    provider_names = ", ".join(provider.name for provider in providers) if providers else "none"
    profile_names = ", ".join(profile.name for profile in profiles) if profiles else "none"

    return textwrap.dedent(
        f"""\
        # Agent / Provider Matrix Report

        Generated: {generated_at}
        Results root: `{run_dir.as_posix()}`

        ## Inventory

        - Providers: {len(providers)} ({provider_names})
        - Profiles: {len(profiles)} ({profile_names})
        - Packages: {len(packages)}

        ## Package Context

        {chr(10).join(package_section) if package_section else '- none discovered'}

        ## Results

        {markdown_table(rows) if len(rows) > 1 else '_No results generated._'}
        """
    ).strip() + "\n"


def main() -> int:
    args = parse_args()
    root = ROOT
    prompt_template_path = args.prompt_template if args.prompt_template.is_absolute() else (root / args.prompt_template)
    packages_root = args.packages_root if args.packages_root.is_absolute() else (root / args.packages_root)
    results_root = args.results_root if args.results_root.is_absolute() else (root / args.results_root)

    if not prompt_template_path.exists():
        print(f"Prompt template not found: {prompt_template_path}", file=sys.stderr)
        return 2

    if args.request_file:
        request_file = args.request_file if args.request_file.is_absolute() else (root / args.request_file)
        if not request_file.exists():
            print(f"Request file not found: {request_file}", file=sys.stderr)
            return 2
        request_text = read_text(request_file).strip()
    else:
        request_text = args.request.strip()
    if not request_text:
        print("Request text is empty.", file=sys.stderr)
        return 2

    auth_run = run_command([args.hermes_bin, "auth", "list"], cwd=root)
    if int(auth_run["returncode"]) != 0:
        print(str(auth_run["stderr"]).strip() or "hermes auth list failed", file=sys.stderr)
        return int(auth_run["returncode"])

    profile_run = run_command([args.hermes_bin, "profile", "list"], cwd=root)
    if int(profile_run["returncode"]) != 0:
        print(str(profile_run["stderr"]).strip() or "hermes profile list failed", file=sys.stderr)
        return int(profile_run["returncode"])

    providers = parse_auth_list(str(auth_run["stdout"]))
    profiles = parse_profile_list(str(profile_run["stdout"]))
    packages = discover_packages(packages_root)

    provider_filter = split_csv_or_list(args.providers)
    profile_filter = split_csv_or_list(args.profiles)
    if provider_filter:
        providers = [provider for provider in providers if provider.name in provider_filter]
    if profile_filter:
        profiles = [profile for profile in profiles if profile.name in profile_filter]

    generated_at = datetime.now(timezone.utc).isoformat(timespec="seconds")
    timestamp = datetime.now(timezone.utc).strftime("%Y%m%dT%H%M%SZ")
    run_dir = results_root / timestamp
    run_dir.mkdir(parents=True, exist_ok=True)

    package_context = build_package_context(packages)
    package_capabilities = build_capability_bullets(packages)
    prompt_template = read_text(prompt_template_path)

    inventory_payload = {
        "generated_at": generated_at,
        "root": root.as_posix(),
        "auth": [asdict(provider) for provider in providers],
        "profiles": [asdict(profile) for profile in profiles],
        "packages": [asdict(package) for package in packages],
    }
    write_json(run_dir / "inventory.json", inventory_payload)

    if args.quiet:
        print(f"[matrix] providers={len(providers)} profiles={len(profiles)} packages={len(packages)}")
        print(f"[matrix] results={run_dir.as_posix()}")

    matrix_results: list[MatrixResult] = []
    planned_cells = 0
    for profile in profiles:
        for provider in providers:
            planned_cells += 1
            if args.limit_cells is not None and planned_cells > args.limit_cells:
                break

            rendered_prompt = render_template(
                prompt_template,
                {
                    "REQUEST": request_text,
                    "PROFILE": profile.name,
                    "PROVIDER": provider.name,
                    "MAX_OUTPUT": str(args.max_output),
                    "PACKAGE_CONTEXT": package_context,
                    "PACKAGE_CAPABILITIES": package_capabilities,
                    "MODEL_HINT": profile.model,
                },
            )

            cell_dir = run_dir / slugify(profile.name) / slugify(provider.name)
            query_path = cell_dir / "request.md"
            write_text(query_path, rendered_prompt)

            assumptions = [
                "provider/model defaults are selected by Hermes unless an explicit override is supplied",
                "package capability extraction is heuristic and based on files under packages/**/*",
            ]

            if args.dry_run:
                command = build_command(
                    args.hermes_bin,
                    profile,
                    provider,
                    query_path,
                    args.source,
                    args.max_turns,
                    args.run_budget,
                    args.model,
                )
                stdout = ""
                stderr = ""
                exit_code = 0
                duration_ms = 0
                status = "dry-run"
                notes = "Dry run: command not executed."
            else:
                command = build_command(
                    args.hermes_bin,
                    profile,
                    provider,
                    query_path,
                    args.source,
                    args.max_turns,
                    args.run_budget,
                    args.model,
                )
                started = time.perf_counter()
                completed = subprocess.run(
                    command,
                    cwd=str(root),
                    capture_output=True,
                    text=True,
                    encoding="utf-8",
                    errors="replace",
                    check=False,
                )
                duration_ms = int((time.perf_counter() - started) * 1000)
                stdout = completed.stdout or ""
                stderr = completed.stderr or ""
                exit_code = completed.returncode
                status = "ok" if exit_code == 0 else "error"
                notes = stderr.strip()

            response_excerpt = make_response_excerpt(stdout, stderr, args.max_output)
            result_payload = {
                "generated_at": generated_at,
                "profile": profile.name,
                "provider": provider.name,
                "package_context": package_context,
                "max_output": args.max_output,
                "capabilities": dedupe_keep_order(capability for package in packages for capability in package.capabilities),
                "model": args.model or profile.model,
                "command": command,
                "exit_code": exit_code,
                "duration_ms": duration_ms,
                "status": status,
                "response_excerpt": response_excerpt,
                "notes": notes,
                "assumptions": assumptions,
                "inventory": {
                    "profiles": len(profiles),
                    "providers": len(providers),
                    "packages": len(packages),
                },
            }
            result_path = write_cell_artifacts(cell_dir, result_payload, rendered_prompt, stdout, stderr)
            result_record = MatrixResult(
                profile=profile.name,
                provider=provider.name,
                package_context=package_context,
                max_output=args.max_output,
                capabilities=dedupe_keep_order(capability for package in packages for capability in package.capabilities),
                model=args.model or profile.model,
                command=command,
                exit_code=exit_code,
                duration_ms=duration_ms,
                status=status,
                response_excerpt=response_excerpt,
                result_path=result_path.as_posix(),
                notes=notes,
                assumptions=assumptions,
            )
            matrix_results.append(result_record)

            if args.quiet:
                print(f"[matrix] {profile.name} × {provider.name} -> {status} ({duration_ms} ms)")

            if args.limit_cells is not None and len(matrix_results) >= args.limit_cells:
                break
        if args.limit_cells is not None and len(matrix_results) >= args.limit_cells:
            break

    summary_md = make_summary_markdown(generated_at, providers, profiles, packages, matrix_results, run_dir)
    write_text(run_dir / "summary.md", summary_md)
    write_json(
        run_dir / "summary.json",
        {
            "generated_at": generated_at,
            "root": root.as_posix(),
            "results_root": run_dir.as_posix(),
            "providers": [provider.name for provider in providers],
            "profiles": [profile.name for profile in profiles],
            "packages": [package.name for package in packages],
            "result_count": len(matrix_results),
            "results": [asdict(result) for result in matrix_results],
        },
    )

    if not args.quiet:
        print(summary_md)
    else:
        print(f"[matrix] wrote summary to {run_dir.as_posix()}")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
