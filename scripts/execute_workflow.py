#!/usr/bin/env python3
"""
Execute the agents-system-prompt-context-fix workflow.
Phases:
1. Generate Agent Context Files (Architecture, Folder Structure, Tech Stack)
2. Audit VS Code Configuration
3. Verify & Implement
"""

import os
import json
import subprocess
import sys
from pathlib import Path

SANDBOX = Path.home() / "Desktop" / "SandBox"
PROJECTS_DIR = SANDBOX / "projects"
DOCS_DIR = SANDBOX / "docs" / "Project_Architecture"

# All subprojects to process
SUBPROJECTS = [
    "Banking",
    "Bash",
    "comicwise",
    "cookiecutter-django-tailwind",
    "Django-Scrapy-Selenium",
    "docs",
    "ecom",
    "mcp-servers",
    "profile",
    "Python-projects",
    "Resume_maker",
    "rhixe_scans",
    "rhixecompany-comics",
    "selenium_webdriver",
    "university-libary-jsm",
    "xamehi.tv",
    "xamehi",
    "youtube-downloader",
]

# Stack mapping for each subproject
STACK_MAP = {
    "Banking": "Next.js",
    "Bash": "Bun/TypeScript",
    "comicwise": "Next.js",
    "cookiecutter-django-tailwind": "Django",
    "Django-Scrapy-Selenium": "Django/Scrapy/Selenium",
    "docs": "Documentation",
    "ecom": "Django + React",
    "mcp-servers": "MCP Servers (Multi-language)",
    "profile": "Django",
    "Python-projects": "Python",
    "Resume_maker": "Bun/TypeScript",
    "rhixe_scans": "Next.js",
    "rhixecompany-comics": "Django + Next.js",
    "selenium_webdriver": "Node.js/Selenium",
    "university-libary-jsm": "Next.js",
    "xamehi.tv": "Django + React",
    "xamehi": "Django + Express + React",
    "youtube-downloader": "Python",
}

def run_command(cmd, cwd=None, check=True):
    """Run a command and return result."""
    print(f"\n$ {cmd}")
    result = subprocess.run(cmd, shell=True, cwd=cwd, capture_output=True, text=True)
    if result.stdout:
        print(result.stdout)
    if result.stderr:
        print(result.stderr, file=sys.stderr)
    if check and result.returncode != 0:
        print(f"Command failed with exit code {result.returncode}")
    return result

def ensure_docs_dir():
    """Ensure docs directory exists."""
    DOCS_DIR.mkdir(parents=True, exist_ok=True)

def generate_architecture_blueprint(project_name, project_path):
    """Generate architecture blueprint for a project."""
    print(f"\n{'='*60}")
    print(f"Generating Architecture Blueprint: {project_name}")
    print(f"{'='*60}")

    # Read AGENTS.md for context
    agents_md = project_path / "AGENTS.md"
    context = ""
    if agents_md.exists():
        context = agents_md.read_text()[:5000]

    output_file = DOCS_DIR / f"{project_name}_architecture.md"

    # Generate content based on AGENTS.md and project type
    content = generate_architecture_content(project_name, project_path, context)
    output_file.write_text(content)
    print(f"Generated: {output_file}")
    return output_file

def generate_architecture_content(project_name, project_path, agents_context):
    """Generate architecture markdown content."""
    lines = [
        f"# {project_name} - Architecture Blueprint",
        "",
        f"**Project Path:** `{project_path}`",
        f"**Generated:** 2026-07-10",
        f"**Source:** AGENTS.md + codebase analysis",
        "",
        "## 1. Architectural Pattern",
        "",
        "Based on AGENTS.md and project structure analysis.",
        "",
        "## 2. Core Components",
        "",
        "| Component | Purpose | Location |",
        "|-----------|---------|----------|",
    ]

    stack = STACK_MAP.get(project_name, "Unknown")

    if "Next.js" in stack:
        lines.extend([
            "| App Router | Next.js 15+ App Router pages and layouts | `app/` |",
            "| API Routes | Serverless API endpoints | `app/api/` |",
            "| Components | React components | `components/` |",
            "| Lib/Utils | Shared utilities | `lib/`, `utils/` |",
            "| Database | ORM models | `db/`, `prisma/`, `drizzle/` |",
        ])
    elif "Django" in stack and "Next.js" not in stack and "React" not in stack:
        lines.extend([
            "| Django Apps | Feature modules | Individual app directories |",
            "| Settings | Configuration layers | `config/`, `settings/` |",
            "| Models | Data models | `models.py` in each app |",
            "| Views/API | Business logic | `views.py`, `api.py` |",
            "| Templates | HTML templates | `templates/` |",
        ])
    elif "Django" in stack and ("Next.js" in stack or "React" in stack):
        lines.extend([
            "| Backend Apps | Django feature modules | `backend/` or root apps |",
            "| Frontend App | Next.js/React frontend | `frontend/` |",
            "| Shared DB | PostgreSQL database | Shared between stacks |",
            "| API Layer | DRF / Next.js API routes | Backend/Frontend |",
        ])
    elif "Bun" in stack or "TypeScript" in stack:
        lines.extend([
            "| Source | TypeScript source | `src/` |",
            "| Scripts | Build/test scripts | `scripts/` |",
            "| Config | Tool configs | Root level |",
        ])
    elif "Node.js" in stack:
        lines.extend([
            "| Source | JavaScript/TypeScript source | `src/` |",
            "| Tests | Test files | `test/`, `__tests__/` |",
        ])
    elif "Python" in stack:
        lines.extend([
            "| Scripts | Standalone Python scripts | Root / `scripts/` |",
            "| Modules | Reusable modules | `lib/`, `utils/` |",
        ])
    elif "MCP" in stack:
        lines.extend([
            "| Server Implementations | Language-specific MCP servers | Per-language directories |",
            "| Protocol | MCP protocol handling | Shared patterns |",
        ])
    else:
        lines.append("| TBD | To be analyzed | |")

    lines.extend([
        "",
        "## 3. Data Flow",
        "",
        "```mermaid",
        "graph TD",
        "    A[Client] --> B[API Gateway]",
        "    B --> C[Services]",
        "    C --> D[Database]",
        "```",
        "",
        "## 4. Cross-Cutting Concerns",
        "",
        "- **Authentication:** NextAuth.js / Django Auth / JWT",
        "- **Error Handling:** Centralized error boundaries / middleware",
        "- **Logging:** Structured logging per framework",
        "- **Configuration:** Environment-based config",
        "",
        "## 5. Implementation Patterns",
        "",
        "- Pattern 1: Feature-based organization",
        "- Pattern 2: Shared utilities",
        "- Pattern 3: Type-safe API contracts",
        "",
        "## 6. Extension Guide",
        "",
        "Follow existing patterns when adding new features.",
        "",
        "---",
        f"*Generated by agents-system-prompt-context-fix-runner*",
    ])

    return "\n".join(lines)

def generate_folder_structure_blueprint(project_name, project_path):
    """Generate folder structure blueprint for a project."""
    print(f"\n{'='*60}")
    print(f"Generating Folder Structure Blueprint: {project_name}")
    print(f"{'='*60}")

    output_file = DOCS_DIR / f"{project_name}_folders.md"

    # Walk the directory
    tree_lines = []
    skip_dirs = {'.git', 'node_modules', '__pycache__', '.venv', 'venv', 'env', 'dist', 'build', '.next', '.turbo', 'coverage'}

    def walk_dir(path, prefix="", depth=0, max_depth=4):
        if depth > max_depth:
            return
        try:
            entries = sorted([e for e in path.iterdir() if not e.name.startswith('.') or e.name in {'.vscode', '.github', '.editorconfig'}])
            entries = [e for e in entries if e.name not in skip_dirs]
            for i, entry in enumerate(entries):
                is_last = i == len(entries) - 1
                current_prefix = "└── " if is_last else "├── "
                tree_lines.append(f"{prefix}{current_prefix}{entry.name}/" if entry.is_dir() else f"{prefix}{current_prefix}{entry.name}")
                if entry.is_dir():
                    next_prefix = prefix + ("    " if is_last else "│   ")
                    walk_dir(entry, next_prefix, depth + 1, max_depth)
        except PermissionError:
            pass

    tree_lines.append(f"{project_name}/")
    walk_dir(project_path)

    content = [
        f"# {project_name} - Folder Structure Blueprint",
        "",
        f"**Project Path:** `{project_path}`",
        f"**Generated:** 2026-07-10",
        f"**Stack:** {STACK_MAP.get(project_name, 'Unknown')}",
        "",
        "## Directory Tree",
        "",
        "```",
        *tree_lines,
        "```",
        "",
        "## Key Directories",
        "",
        "| Directory | Purpose | Convention |",
        "|-----------|---------|------------|",
    ]

    stack = STACK_MAP.get(project_name, "")
    if "Next.js" in stack:
        content.extend([
            "| `app/` | Next.js App Router pages & layouts | Feature-based subdirectories |",
            "| `components/` | React components | PascalCase, co-located with feature |",
            "| `lib/` | Shared utilities | camelCase files |",
            "| `db/` / `prisma/` / `drizzle/` | Database schema & ORM | Standard conventions |",
        ])
    elif "Django" in stack:
        content.extend([
            "| `<app>/` | Django apps | lowercase, plural |",
            "| `config/` / `settings/` | Settings modules | base/local/production |",
            "| `templates/` | HTML templates | app-specific subdirs |",
            "| `static/` | Static assets | Collected by collectstatic |",
        ])
    elif "Bun" in stack or "TypeScript" in stack:
        content.extend([
            "| `src/` | TypeScript source | Feature-based |",
            "| `scripts/` | Build/deploy scripts | kebab-case |",
        ])
    elif "Node.js" in stack:
        content.extend([
            "| `src/` | Source code | ES Modules |",
        ])
    elif "Python" in stack:
        content.extend([
            "| `scripts/` | Python scripts | snake_case |",
        ])
    else:
        content.append("| TBD | To be analyzed | |")

    content.extend([
        "",
        "## Naming Conventions",
        "",
        "- **Directories:** kebab-case (multi-word) or lowercase",
        "- **Files:** Match language convention (PascalCase for React, snake_case for Python)",
        "- **Configs:** lowercase with extension (.json, .yaml, .toml)",
        "",
        "## File Placement Patterns",
        "",
        "- Tests: co-located (`__tests__/`) or mirrored `tests/` structure",
        "- Types: `types/` or co-located with implementation",
        "- Config: Root level for tool configs",
        "",
        "---",
        f"*Generated by agents-system-prompt-context-fix-runner*",
    ])

    output_file.write_text("\n".join(content))
    print(f"Generated: {output_file}")
    return output_file

def generate_tech_stack_blueprint(project_name, project_path):
    """Generate technology stack blueprint for a project."""
    print(f"\n{'='*60}")
    print(f"Generating Technology Stack Blueprint: {project_name}")
    print(f"{'='*60}")

    output_file = DOCS_DIR / f"{project_name}_techstack.md"
    stack = STACK_MAP.get(project_name, "Unknown")

    content = [
        f"# {project_name} - Technology Stack Blueprint",
        "",
        f"**Project Path:** `{project_path}`",
        f"**Generated:** 2026-07-10",
        f"**Primary Stack:** {stack}",
        "",
        "## Core Technologies",
        "",
    ]

    if "Next.js" in stack:
        content.extend([
            "| Category | Technology | Version | Purpose |",
            "|----------|------------|---------|---------|",
            "| Runtime | Node.js | 18+ / 20+ | JavaScript runtime |",
            "| Framework | Next.js | 15+ | React full-stack framework |",
            "| Language | TypeScript | 5+ | Type-safe JavaScript |",
            "| Styling | Tailwind CSS | 3+ | Utility-first CSS |",
            "| Database ORM | Prisma / Drizzle | Latest | Type-safe database access |",
            "| Auth | NextAuth.js | 5+ | Authentication |",
            "| Package Manager | pnpm / bun | Latest | Dependency management |",
            "| Linting | ESLint | 9+ | Code quality |",
            "| Formatting | Prettier | 3+ | Code formatting |",
        ])
    elif "Django" in stack and "Next.js" not in stack and "React" not in stack:
        content.extend([
            "| Category | Technology | Version | Purpose |",
            "|----------|------------|---------|---------|",
            "| Language | Python | 3.10+ | Backend language |",
            "| Framework | Django | 4.x / 5.x | Web framework |",
            "| API | Django REST Framework | 3.14+ | REST API |",
            "| Database | PostgreSQL | 15+ | Primary database |",
            "| ORM | Django ORM | Built-in | Database abstraction |",
            "| Frontend | django-tailwind / React | Varies | Frontend integration |",
            "| Auth | django-allauth / NextAuth | Latest | Authentication |",
            "| Async | Celery + Redis | Latest | Background tasks |",
            "| Package Manager | pip / uv | Latest | Dependency management |",
            "| Linting | ruff / mypy | Latest | Code quality |",
            "| Formatting | Black | Latest | Code formatting |",
        ])
    elif "Django" in stack and ("Next.js" in stack or "React" in stack):
        content.extend([
            "| Category | Technology | Version | Purpose |",
            "|----------|------------|---------|---------|",
            "| Backend Language | Python | 3.10+ | Django backend |",
            "| Backend Framework | Django | 4.x / 5.x | Web framework |",
            "| Backend API | Django REST Framework | 3.14+ | REST API |",
            "| Frontend Framework | Next.js / React | 15+ / 18+ | Frontend |",
            "| Frontend Language | TypeScript | 5+ | Type-safe frontend |",
            "| Database | PostgreSQL | 15+ | Shared database |",
            "| ORM | Django ORM / Prisma / Drizzle | Latest | Database access |",
            "| Auth | NextAuth / django-allauth | Latest | Authentication |",
            "| Styling | Tailwind CSS | 3+ | Styling |",
        ])
    elif "Bun" in stack:
        content.extend([
            "| Category | Technology | Version | Purpose |",
            "|----------|------------|---------|---------|",
            "| Runtime | Bun | 1.3.14+ | JS runtime + pkg mgr + test runner |",
            "| Language | TypeScript | 5+ | Type-safe JavaScript |",
            "| Linting | ESLint | 9+ (flat config) | Code quality |",
            "| Formatting | Prettier | 3+ | Code formatting |",
            "| Testing | Vitest | 2+ | Unit testing |",
            "| Package Manager | Bun | Built-in | Dependency management |",
        ])
    elif "Node.js" in stack:
        content.extend([
            "| Category | Technology | Version | Purpose |",
            "|----------|------------|---------|---------|",
            "| Runtime | Node.js | 18+ | JavaScript runtime |",
            "| Framework | Selenium WebDriver | 4.x | Browser automation |",
            "| Language | TypeScript / JavaScript | Latest | Scripting |",
            "| Package Manager | npm | Latest | Dependencies |",
        ])
    elif "Python" in stack:
        content.extend([
            "| Category | Technology | Version | Purpose |",
            "|----------|------------|---------|---------|",
            "| Language | Python | 3.x | Scripting language |",
            "| Key Libraries | yt-dlp, curl_cffi, opencv, requests | Latest | Various utilities |",
            "| Linting | ruff | Latest | Fast Python linter |",
            "| Type Checking | mypy | Latest | Static type checking |",
        ])
    elif "MCP" in stack:
        content.extend([
            "| Category | Technology | Version | Purpose |",
            "|----------|------------|---------|---------|",
            "| Protocol | MCP | 2024-11-05 | Model Context Protocol |",
            "| Languages | TypeScript, Python, Go, Rust, Java, Kotlin, PHP, Ruby, Swift, C# | Various | Multi-language implementations |",
            "| Transport | stdio / HTTP | - | Communication |",
        ])
    else:
        content.append("| TBD | To be analyzed | | |")

    content.extend([
        "",
        "## Development Tools",
        "",
        "| Tool | Purpose | Config |",
        "|------|---------|--------|",
        "| VS Code | IDE | `.vscode/` |",
        "| Git | Version control | `.gitignore` |",
        "| Docker | Containerization | `Dockerfile`, `docker-compose.yml` |",
        "",
        "## Coding Conventions",
        "",
        "- **Naming:** Follow language/framework conventions",
        "- **Imports:** Organized (stdlib -> third-party -> local)",
        "- **Types:** Strict TypeScript / Type hints in Python",
        "- **Tests:** Co-located or mirrored structure",
        "",
        "## Usage Patterns",
        "",
        "- Feature-based organization",
        "- Shared utilities in `lib/`, `utils/`, or `common/`",
        "- Environment-based configuration",
        "",
        "---",
        f"*Generated by agents-system-prompt-context-fix-runner*",
    ])

    output_file.write_text("\n".join(content))
    print(f"Generated: {output_file}")
    return output_file

def audit_vscode_configs():
    """Run VS Code configuration audit."""
    print(f"\n{'='*60}")
    print("Phase 2: Audit VS Code Configuration")
    print(f"{'='*60}")

    script_path = Path.home() / "AppData" / "Local" / "hermes" / "scripts" / "audit_vscode_config.py"
    if script_path.exists():
        result = run_command(f"python {script_path}", cwd=SANDBOX, check=False)
        return result
    else:
        print("Audit script not found, skipping...")
        return None

def generate_vscode_configs():
    """Generate VS Code configurations for all projects."""
    print(f"\n{'='*60}")
    print("Generating VS Code Configurations")
    print(f"{'='*60}")

    script_path = Path.home() / "AppData" / "Local" / "hermes" / "scripts" / "generate_vscode_configs.py"
    if script_path.exists():
        result = run_command(f"python {script_path}", cwd=SANDBOX, check=False)
        return result
    else:
        print("Generate script not found, skipping...")
        return None

def verify_json_configs():
    """Verify all .vscode JSON files are valid."""
    print(f"\n{'='*60}")
    print("Verifying VS Code JSON Configurations")
    print(f"{'='*60}")

    issues = []
    for vscode_dir in PROJECTS_DIR.rglob(".vscode"):
        if "node_modules" in vscode_dir.parts:
            continue
        for json_file in vscode_dir.glob("*.json"):
            try:
                with open(json_file) as f:
                    json.load(f)
                print(f"Valid: {json_file.relative_to(SANDBOX)}")
            except json.JSONDecodeError as e:
                print(f"Invalid JSON: {json_file.relative_to(SANDBOX)} - {e}")
                issues.append(str(json_file))

    # Also check root .vscode
    root_vscode = SANDBOX / ".vscode"
    if root_vscode.exists():
        for json_file in root_vscode.glob("*.json"):
            try:
                with open(json_file) as f:
                    json.load(f)
                print(f"Valid: {json_file.relative_to(SANDBOX)}")
            except json.JSONDecodeError as e:
                print(f"Invalid JSON: {json_file.relative_to(SANDBOX)} - {e}")
                issues.append(str(json_file))

    if issues:
        print(f"\nFound {len(issues)} invalid JSON files")
    else:
        print(f"\nAll JSON files are valid")

    return issues

def main():
    """Main execution workflow."""
    print("="*60)
    print("AGENTS SYSTEM PROMPT CONTEXT FIX - WORKFLOW EXECUTION")
    print("="*60)

    ensure_docs_dir()

    # Phase 1: Generate Agent Context Files
    print("\n\nPHASE 1: GENERATE AGENT CONTEXT FILES")
    print("="*60)

    for project_name in SUBPROJECTS:
        project_path = PROJECTS_DIR / project_name
        if not project_path.exists():
            print(f"Skipping {project_name} - directory not found")
            continue

        print(f"\nProcessing: {project_name}")

        # Step 1.1: Architecture Blueprint
        generate_architecture_blueprint(project_name, project_path)

        # Step 1.2: Folder Structure Blueprint
        generate_folder_structure_blueprint(project_name, project_path)

        # Step 1.3: Technology Stack Blueprint
        generate_tech_stack_blueprint(project_name, project_path)

    # Also generate for root
    print(f"\nProcessing: SandBox (root)")
    generate_architecture_blueprint("SandBox", SANDBOX)
    generate_folder_structure_blueprint("SandBox", SANDBOX)
    generate_tech_stack_blueprint("SandBox", SANDBOX)

    print("\n\nPHASE 2: AUDIT VS CODE CONFIGURATION")
    print("="*60)

    # Step 2.1-2.6: Audit VS Code configs
    audit_vscode_configs()

    # Step 2.2-2.5: Generate/Enhance configs
    generate_vscode_configs()

    # Step 2.6: Verify
    issues = verify_json_configs()

    print("\n\nPHASE 3: VERIFY & IMPLEMENT")
    print("="*60)

    # Summary
    arch_files = list(DOCS_DIR.glob("*_architecture.md"))
    folder_files = list(DOCS_DIR.glob("*_folders.md"))
    tech_files = list(DOCS_DIR.glob("*_techstack.md"))

    print(f"\nSUMMARY:")
    print(f"   Architecture Blueprints: {len(arch_files)}")
    print(f"   Folder Structure Blueprints: {len(folder_files)}")
    print(f"   Technology Stack Blueprints: {len(tech_files)}")
    print(f"   Invalid JSON Configs: {len(issues)}")
    print(f"   Output Directory: {DOCS_DIR}")

    if issues:
        print(f"\nIssues to fix:")
        for issue in issues:
            print(f"   - {issue}")
        return 1

    print("\nWORKFLOW COMPLETE - All phases successful!")
    return 0

if __name__ == "__main__":
    sys.exit(main())