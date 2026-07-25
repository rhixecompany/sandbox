#!/usr/bin/env python3
"""Batch-import .github/instructions/*.instructions.md into Hermes config.yaml personalities.

Modifies config.yaml in ONE pass (reads → merges → writes) to avoid 186 slow
`hermes config set` calls.  Also generates a quick-command source-able script.
"""

import os
import re
import sys
from pathlib import Path

import yaml

HERE = Path(__file__).resolve().parent
WORKSPACE = HERE.parent
HERMES_HOME = Path(os.environ.get("LOCALAPPDATA", os.environ.get("HOME", "~"))) / "hermes"
CONFIG_PATH = HERMES_HOME / "config.yaml"
INSTRUCTIONS_DIR = WORKSPACE / ".github" / "instructions"
ALIAS_SCRIPT = HERE / "instruction-quick-commands.sh"
MAX_SUMMARY_CHARS = 400

CATEGORIES = {
    "frontend": [
        "angular",
        "reactjs",
        "vuejs3",
        "svelte",
        "nextjs",
        "nextjs-2026",
        "nextjs-tailwind",
        "tailwind-v4-vite",
        "tanstack-start-shadcn-tailwind",
        "astro",
    ],
    "dotnet": [
        "aspnet-rest-apis",
        "blazor",
        "csharp",
        "csharp-ja",
        "csharp-ko",
        "csharp-mcp-server",
        "dotnet-architecture-good-practices",
        "dotnet-framework",
        "dotnet-maui",
        "dotnet-maui-9-to-dotnet-maui-10-upgrade",
        "dotnet-upgrade",
        "dotnet-wpf",
        "oqtane",
        "azure-functions-typescript",
        "azure-logic-apps-power-automate",
        "azure-verified-modules-bicep",
        "azure-verified-modules-terraform",
        "bicep-code-best-practices",
        "azure-devops-pipelines",
        "generate-modern-terraform-code-for-azure",
    ],
    "power-platform": [
        "pcf-alm",
        "pcf-api-reference",
        "pcf-best-practices",
        "pcf-canvas-apps",
        "pcf-code-components",
        "pcf-community-resources",
        "pcf-dependent-libraries",
        "pcf-events",
        "pcf-fluent-modern-theming",
        "pcf-limitations",
        "pcf-manifest-schema",
        "pcf-model-driven-apps",
        "pcf-overview",
        "pcf-power-pages",
        "pcf-react-platform-libraries",
        "pcf-sample-components",
        "pcf-tooling",
        "power-apps-canvas-yaml",
        "power-apps-code-apps",
        "power-platform-connector",
        "power-platform-mcp-development",
        "power-bi-custom-visuals-development",
        "power-bi-data-modeling-best-practices",
        "power-bi-dax-best-practices",
        "power-bi-devops-alm-best-practices",
        "power-bi-report-design-best-practices",
        "power-bi-security-rls-best-practices",
        "mcp-m365-copilot",
        "typespec-m365-copilot",
        "declarative-agents-microsoft365",
    ],
    "dataverse": [
        "dataverse-python",
        "dataverse-python-advanced-features",
        "dataverse-python-agentic-workflows",
        "dataverse-python-api-reference",
        "dataverse-python-authentication-security",
        "dataverse-python-best-practices",
        "dataverse-python-error-handling",
        "dataverse-python-file-operations",
        "dataverse-python-modules",
        "dataverse-python-pandas-integration",
        "dataverse-python-performance-optimization",
        "dataverse-python-real-world-usecases",
        "dataverse-python-sdk",
        "dataverse-python-testing-debugging",
    ],
    "python": ["python", "python-mcp-server", "langchain-python"],
    "typescript": ["typescript", "typescript-5-es2022", "typescript-mcp-server", "nodejs-javascript-vitest"],
    "java-jvm": [
        "java",
        "java-11-to-java-17-upgrade",
        "java-17-to-java-21-upgrade",
        "java-21-to-java-25-upgrade",
        "java-mcp-server",
        "kotlin-mcp-server",
        "quarkus",
        "quarkus-mcp-server-sse",
        "scala2",
        "springboot",
        "springboot-4-migration",
        "clojure",
        "convert-cassandra-to-spring-data-cosmos",
        "convert-jpa-to-spring-data-cosmos",
    ],
    "systems": ["rust", "rust-mcp-server", "go", "go-mcp-server", "swift-mcp-server", "cpp-language-service-tools"],
    "php-ruby": ["php-mcp-server", "php-symfony", "ruby-mcp-server", "ruby-on-rails", "wordpress"],
    "infra-devops": [
        "terraform",
        "terraform-azure",
        "terraform-sap-btp",
        "kubernetes-deployment-best-practices",
        "kubernetes-manifests",
        "containerization-docker-best-practices",
        "ansible",
    ],
    "ci-cd": ["github-actions-ci-cd-best-practices", "devops-core-principles"],
    "databases": ["database-best-practices", "mongo-dba", "ms-sql-dba", "sql-sp-generation"],
    "security": ["security", "security-and-owasp"],
    "quality": [
        "code-review",
        "code-review-generic",
        "performance",
        "performance-optimization",
        "testing",
        "gilfoyle-code-review",
        "self-explanatory-code-commenting",
        "object-calisthenics",
    ],
    "design-ux": [
        "a11y",
        "design-system",
        "html-css-style-color-guide",
        "markdown",
        "markdown-accessibility",
        "seed-system",
    ],
    "shell-tooling": ["shell", "powershell", "powershell-pester-5", "makefile", "cmake-vcpkg", "no-heredoc"],
    "prompt-engineering": [
        "agents",
        "agent-safety",
        "agent-skills",
        "ai-prompt-engineering-safety-best-practices",
        "prompt",
        "prompts-strict-template",
        "instructions",
        "context-engineering",
    ],
    "copilot": [
        "copilot-sdk-csharp",
        "copilot-sdk-go",
        "copilot-sdk-nodejs",
        "copilot-sdk-python",
        "copilot-thought-logging",
        "taming-copilot",
    ],
    "other": [
        "arch-linux",
        "centos-linux",
        "debian-linux",
        "fedora-linux",
        "apex",
        "codexer",
        "coldfusion-cfc",
        "coldfusion-cfm",
        "context7",
        "devbox-image-definition",
        "documentation",
        "genaiscript",
        "joyride-user-project",
        "joyride-workspace-automation",
        "localization",
        "lwc",
        "memory-bank",
        "monorepo-path-routing",
        "moodle",
        "nestjs",
        "playwright-dotnet",
        "playwright-python",
        "playwright-typescript",
        "r",
        "spec-driven-workflow-v1",
        "task-implementation",
        "tasksync",
        "update-code-from-shorthand",
        "update-docs-on-code-change",
        "vsixtoolkit",
        "dart-n-flutter",
    ],
}

_NAME_TO_CAT = {}
for cat, names in CATEGORIES.items():
    for n in names:
        _NAME_TO_CAT[n] = cat


def extract_summary(text: str, max_chars: int = MAX_SUMMARY_CHARS) -> str:
    """Extract a compact summary from instructions content."""
    lines = text.splitlines()
    body_start = 0
    if lines and lines[0].strip().startswith("---"):
        for i in range(1, len(lines)):
            if lines[i].strip().startswith("---"):
                body_start = i + 1
                break
    body = "\n".join(lines[body_start:])
    summary = re.sub(r"\s+", " ", body[:max_chars]).strip()
    if len(body) > max_chars:
        summary += "..."
    return summary


def main():
    if not INSTRUCTIONS_DIR.is_dir():
        print(f"ERROR: {INSTRUCTIONS_DIR} not found", file=sys.stderr)
        sys.exit(1)

    files = sorted(INSTRUCTIONS_DIR.glob("*.instructions.md"))
    if not files:
        print(f"No .instructions.md files in {INSTRUCTIONS_DIR}", file=sys.stderr)
        sys.exit(1)

    print(f"Found {len(files)} instruction files")

    # Build the personalities dict
    personalities = {}
    for f in files:
        stem = f.stem.replace(".instructions", "")
        cat = _NAME_TO_CAT.get(stem, "other")
        text = f.read_text(encoding="utf-8")
        summary = extract_summary(text)
        key = f"{cat}_{stem}"
        personalities[key] = summary

    # Read existing config.yaml or start fresh
    config = {}
    if CONFIG_PATH.exists():
        try:
            raw = CONFIG_PATH.read_text(encoding="utf-8")
            if raw.strip():
                config = yaml.safe_load(raw) or {}
        except Exception as e:
            print(f"Warning: couldn't read {CONFIG_PATH}: {e}", file=sys.stderr)

    # Merge personalities into agent section
    if "agent" not in config or not isinstance(config["agent"], dict):
        config["agent"] = {}
    existing_personalities = config["agent"].get("personalities", {})
    if not isinstance(existing_personalities, dict):
        existing_personalities = {}

    # Merge: add new ones, keep existing ones that don't start with a category prefix
    for key, val in personalities.items():
        existing_personalities[key] = val

    config["agent"]["personalities"] = existing_personalities

    # Write back
    CONFIG_PATH.write_text(yaml.dump(config, default_style=None, allow_unicode=True, sort_keys=False), encoding="utf-8")
    print(f"Updated {CONFIG_PATH} with {len(personalities)} instruction-based personalities")
    print(f"Total personalities in config: {len(existing_personalities)}")

    # Generate quick-command aliases
    alias_lines = [
        "#!/usr/bin/env bash",
        "# Instruction Personality Quick Commands",
        "# Source: source scripts/instruction-quick-commands.sh",
        "#",
        f"# Generated from {len(files)} .instructions.md files in {len(CATEGORIES)} categories",
        "",
    ]

    seen_cats = set()
    for f in files:
        stem = f.stem.replace(".instructions", "")
        cat = _NAME_TO_CAT.get(stem, "other")
        if cat not in seen_cats:
            seen_cats.add(cat)
            cat_names = [n for n in CATEGORIES.get(cat, []) if (INSTRUCTIONS_DIR / f"{n}.instructions.md").exists()]
            n = len(cat_names)
            alias_lines.append(f"""
# Switch to {cat} instruction personality set ({n} files)
use-{cat}() {{
    hermes config set agent.personality {cat}
    echo "Now using '{cat}' knowledge base ({n} instruction files)"
}}""")

    # Listing function
    alias_lines.append(
        """
# List all instruction personalities
list-instructions() {
    echo "Available instruction personality categories:"
    for cat in """
        + " ".join(sorted(CATEGORIES.keys()))
        + """; do
        n=$(hermes config show 2>/dev/null | grep -c "agent.personalities.${cat}_" 2>/dev/null || echo 0)
        echo "  $cat ($n files)"
    done
}
# Aliases
for cat in """
        + " ".join(sorted(CATEGORIES.keys()))
        + """; do
    alias "$cat"="use-$cat"
done"""
    )

    ALIAS_SCRIPT.parent.mkdir(parents=True, exist_ok=True)
    ALIAS_SCRIPT.write_text("\n".join(alias_lines) + "\n", encoding="utf-8")
    print(f"Quick-command aliases → {ALIAS_SCRIPT}")

    # Print summary
    print(f"\n{'=' * 60}")
    print("CATEGORY BREAKDOWN:")
    print(f"{'=' * 60}")
    for cat, names in sorted(CATEGORIES.items()):
        present = [n for n in names if (INSTRUCTIONS_DIR / f"{n}.instructions.md").exists()]
        print(f"  {cat:25s} {len(present):3d} files → use-{cat}")


if __name__ == "__main__":
    main()
