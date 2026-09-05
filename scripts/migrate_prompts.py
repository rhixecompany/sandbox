#!/usr/bin/env python3
"""
Migration script to restructure prompts to category/trigger layout.

Current: .github/prompts/*.prompt.md
Target:  .github/prompts/<category>/<trigger>/<trigger>.prompt.md
         with co-located templates/ and scripts/
"""
import re
import shutil
from pathlib import Path

# Mapping of prompt names to categories
CATEGORY_MAP = {
    # Planning
    "create-implementation-plan": "planning",
    "breakdown-epic-arch": "planning",
    "breakdown-epic-pm": "planning",
    "breakdown-feature-implementation": "planning",
    "breakdown-feature-prd": "planning",
    "breakdown-plan": "planning",
    "breakdown-test": "planning",
    "plan-audit": "planning",
    "plan-batch-fix": "planning",
    "plan-execute": "planning",
    "plan-generate": "planning",
    "refactor-plan": "planning",
    "update-implementation-plan": "planning",
    
    # Development
    "add-educational-comments": "development",
    "agents-fix": "development",
    "agents-generator": "development",
    "agents-system-prompt-context-fix": "development",
    "bash-scripts-fix": "development",
    "csharp-async": "development",
    "csharp-docs": "development",
    "csharp-mcp-server-generator": "development",
    "csharp-mstest": "development",
    "csharp-nunit": "development",
    "csharp-tunit": "development",
    "csharp-xunit": "development",
    "database": "development",
    "debug-issue": "development",
    "debugger-prompt": "development",
    "dev": "development",
    "dev-imp": "development",
    "dev-init": "development",
    "development": "development",
    "dotnet-best-practices": "development",
    "dotnet-design-pattern-review": "development",
    "dotnet-upgrade": "development",
    "ef-core": "development",
    "execute-plan": "development",
    "features": "development",
    "java-add-graalvm-native-image-support": "development",
    "java-docs": "development",
    "java-junit": "development",
    "java-mcp-server-generator": "development",
    "java-refactoring-extract-method": "development",
    "java-refactoring-remove-parameter": "development",
    "java-springboot": "development",
    "javascript-typescript-jest": "development",
    "kotlin-mcp-server-generator": "development",
    "kotlin-springboot": "development",
    "mcp-create-adaptive-cards": "development",
    "mcp-create-declarative-agent": "development",
    "mcp-deploy-manage-agents": "development",
    "optimize-agentsMd": "development",
    "php-mcp-server-generator": "development",
    "python-mcp-server-generator": "development",
    "refactor-code": "development",
    "refactor-mardown-files": "development",
    "refactor-method-complexity-reduce": "development",
    "review-and-refactor": "development",
    "ruby-mcp-server-generator": "development",
    "rust-mcp-server-generator": "development",
    "swift-mcp-server-generator": "development",
    "task-implementation": "development",
    "typescript-mcp-server-generator": "development",
    "typescript": "development",
    "write-coding-standards-from-file": "development",
    "write-tests": "development",
    
    # QA
    "audit-skills-judge-fix": "qa",
    "playwright-automation-fill-in-form": "qa",
    "playwright-generate-e2e-test": "qa",
    "playwright-generate-test": "qa",
    "postgresql-code-review": "qa",
    "pytest-coverage": "qa",
    "scoutqa-test": "qa",
    "test-skill": "qa",
    
    # Architecture
    "architecture-blueprint-generator": "architecture",
    "code-exemplars-blueprint-generator": "architecture",
    "create-architectural-decision-record": "architecture",
    "folder-structure-blueprint-generator": "architecture",
    "project-workflow-analysis-blueprint-generator": "architecture",
    "readme-blueprint-generator": "architecture",
    "technology-stack-blueprint-generator": "architecture",
    
    # Creative
    "comicwise-development": "creative",
    "ai-prompt-engineering-safety-review": "creative",
    "comprehensive-prompt-enhancer": "creative",
    
    # Documentation
    "comment-code-generate-a-tutorial": "documentation",
    "conventional-commit": "documentation",
    "create-readme": "documentation",
    "create-tldr-page": "documentation",
    "documentation": "documentation",
    "documentation-writer": "documentation",
    "generate-docs": "documentation",
    "update-docs-on-code-change": "documentation",
    "update-markdown-file-index": "documentation",
    "update-oo-component-documentation": "documentation",
    "update-llms": "documentation",
    "create-llms": "documentation",
    "update-llms": "documentation",
    
    # GitHub
    "create-github-action-workflow-specification": "github",
    "create-github-issue-feature-from-specification": "github",
    "create-github-issues-feature-from-implementation-plan": "github",
    "create-github-issues-for-unmet-specification-requirements": "github",
    "create-github-pull-request-from-specification": "github",
    "git-flow-branch-creator": "github",
    "git-multi-repo-orchestration": "github",
    "my-issues": "github",
    "my-pull-requests": "github",
    "list-all-installed-vscode-extension": "github",
    
    # MCP
    "mcp-audit": "mcp",
    "oh-my-openagent-setup": "mcp",
    "ollama-wire": "mcp",
    "parallel-mcp-install": "mcp",
    "smithery-setup": "mcp",
    
    # CI/CD
    "containerize-aspnet-framework": "ci-cd",
    "containerize-aspnetcore": "ci-cd",
    "devops-rollout-plan": "ci-cd",
    "multi-stage-dockerfile": "ci-cd",
    "all-repo-docker-setup": "ci-cd",
    "setup-bun-bunx": "ci-cd",
    "setup-groq-cloud": "ci-cd",
    "setup-nextjs-frontend-stack": "ci-cd",
    "setup-enhanced": "ci-cd",
    "setup-component": "ci-cd",
    "setup": "ci-cd",
    "repo-init": "ci-cd",
    
    # Research
    "ngn-earnings-research": "research",
    "ngn-earnings-research-pipeline": "research",
    "uk-earnings-research": "research",
    "uk-earnings-research-pipeline": "research",
    "us-earnings-research": "research",
    "repo-research-pipeline": "research",
    "web-research-pipeline": "research",
    "model-recommendation": "research",
    "provider-docs-research-template": "research",
    
    # Testing
    "testing": "testing",
    
    # Monitoring
    "quality-gate-debugger": "monitoring",
    "postgresql-optimization": "monitoring",
    "power-bi-performance-troubleshooting": "monitoring",
    
    # Productivity
    "boost-prompt": "productivity",
    "convert-plaintext-to-md": "productivity",
    "enhance-prompts": "productivity",
    "prompt-builder": "productivity",
    "prompt-management": "productivity",
    "prompts-fix": "productivity",
    "prompts-strict-template": "productivity",
    "shuffle-json-data": "productivity",
    "remember": "productivity",
    "remember-interactive-programming": "productivity",
    "memory-merger": "productivity",
    "create-agentsmd": "productivity",
    "generate-custom-instructions-from-codebase": "productivity",
    "update-agents-md": "productivity",
    
    # Reference
    "exemplars": "reference",
    "capability-ranking-template": "reference",
    "provider-inventory-template": "reference",
    "verification-gates-template": "reference",
    "hermes-config-template": "reference",
    "model-probe-template": "reference",
    
    # Security
    "security": "security",
    "sql-code-review": "security",
    "sql-optimization": "security",
    
    # Tools
    "tooling-implementation": "tooling",
    "repo-tooling-implementation": "tooling",
    "editorconfig": "tooling",
    "tsconfig": "tooling",
    
    # Finance
    "az-cost-optimize": "finance",
    "how-paypal-works": "finance",
    "paypal-getting-started": "finance",
    "paystack-dev-docs": "finance",
    "paystack-getting-started": "finance",
    "flutterwave-transfers-api": "finance",
    "busha-api-quickstart": "finance",
    "busha-business-api": "finance",
    "busha-quick-start-guide": "finance",
    "crypto-wallet-api-guide": "finance",
    "crypto-wallet-quickstart": "finance",
    "cryptoapis-wallet-builder": "finance",
    
    # Database
    "cosmosdb-datamodeling": "database",
    "dataverse-python-advanced-patterns": "database",
    "dataverse-python-production-code": "database",
    "dataverse-python-quickstart": "database",
    "dataverse-python-usecase-builder": "database",
    
    # Debugging
    "hermes-doctor": "debugging",
    "hermes-doctor-systematic-debugging": "debugging",
    "hermes-diagnostic": "debugging",
    "instruction-triage": "debugging",
    "debug-issue": "debugging",
    
    # Migration
    "migrate-to-next16": "migration",
    
    # MLOps
    "ml-models": "mlops",
    
    # Operations
    "disk-space-cleanup": "operations",
    "service-integrations": "operations",
    "webhook-subscriptions": "operations",
    
    # Payments
    "paypal-how-it-works": "payments",
    "stripe-integration": "payments",
    
    # Brainstorming
    "brainstorming": "brainstorming",
    "creative-ideation": "brainstorming",
    
    # Hooks
    "hooks-pattern": "hooks",
    "hermes-hooks": "hooks",
    
    # Web
    "next-intl-add-language": "web",
    "nextjs-tailwind": "web",
    "openapi-to-application-code": "web",
    "typespec-api-operations": "web",
    "typespec-create-agent": "web",
    "typespec-create-api-plugin": "web",
    
    # MLops/audio
    "audiocraft-audio-generation": "mlops",
    "segment-anything-model": "mlops",
    
    # Special
    "Initial": "general",
    "pl": "general",
    "general": "general",
    "repo": "general",
    "repo.prompt": "general",
    "repo-management": "general",
    "repo-story-time": "general",
    "repo.prompt": "general",
    "session-agentsmd-full-workflow": "general",
    "run-session-agentsmd-workflow": "general",
    "sync-hermes-opencode": "general",
    "comprehensive-hermes-maintenance": "general",
    "execute-all-prompts": "general",
    "hermes-breakdown-epic-arch": "planning",
    "hermes-breakdown-epic-pm": "planning",
    "hermes-breakdown-feature-implementation": "planning",
    "hermes-breakdown-feature-prd": "planning",
    "hermes-breakdown-plan": "planning",
    "hermes-breakdown-test": "planning",
    "hermes-comprehensive-setup": "general",
    "hermes-config-inventory": "general",
    "generate-session-report": "general",
    "multi-agent-fanout": "general",
    "multi-agent-research-template": "research",
    "structured-autonomy-generate": "general",
    "structured-autonomy-implement": "general",
    "structured-autonomy-plan": "general",
    "create-specification": "planning",
    "update-specification": "planning",
    "create-specification": "planning",
    "create-technical-spike": "development",
    "first-ask": "general",
    "finalize-agent-prompt": "general",
    "seed-review-and-create": "general",
    "shared-templates": "general",
    "setup": "ci-cd",
    "what-context-needed": "general",
    "workspace-consolidate": "general",
    "zod-schema-generation": "development",
}


def extract_trigger(text: str) -> str:
    for line in text.splitlines():
        if line.startswith("trigger:"):
            val = line.split(":", 1)[1].strip().strip('"').strip("'")
            if val.startswith("/"):
                val = val[1:]
            return val
    return ""


def extract_category_from_path(p: Path) -> str:
    """Determine category from the prompt name."""
    stem = p.stem.replace(".prompt", "")
    return CATEGORY_MAP.get(stem, "general")


def migrate_prompts(dry_run: bool = True):
    prompts_dir = Path("C:/Users/Alexa/Desktop/SandBox/.github/prompts")
    prompts = sorted(prompts_dir.glob("*.prompt.md"))
    
    print(f"Found {len(prompts)} prompts to migrate")
    print(f"Dry run: {dry_run}")
    print()
    
    for pp in prompts:
        text = pp.read_text(encoding="utf-8")
        trigger = extract_trigger(text)
        if not trigger:
            trigger = pp.stem.replace(".prompt", "")
        
        category = extract_category_from_path(pp)
        
        # Target structure
        target_dir = prompts_dir / category / trigger
        target_prompt = target_dir / f"{trigger}.prompt.md"
        target_templates = target_dir / "templates"
        target_scripts = target_dir / "scripts"
        
        # Check if templates exist in old location
        old_templates = prompts_dir / "templates" / trigger
        
        print(f"Category: {category:20} Trigger: {trigger:50} -> {target_dir}")
        
        if not dry_run:
            # Create directories
            target_dir.mkdir(parents=True, exist_ok=True)
            target_templates.mkdir(parents=True, exist_ok=True)
            target_scripts.mkdir(parents=True, exist_ok=True)
            
            # Move prompt file
            shutil.move(str(pp), str(target_prompt))
            print(f"  Moved prompt to: {target_prompt}")
            
            # Move templates if they exist
            if old_templates.exists() and old_templates.is_dir():
                for tmpl in old_templates.glob("*.md"):
                    dest = target_templates / tmpl.name
                    shutil.move(str(tmpl), str(dest))
                    print(f"  Moved template: {tmpl.name}")
                # Remove empty old dir
                try:
                    old_templates.rmdir()
                except OSError:
                    pass
            
            # Update frontmatter in moved prompt
            new_text = target_prompt.read_text(encoding="utf-8")
            # Add category if not present
            if "category:" not in new_text:
                lines = new_text.splitlines()
                # Insert after trigger
                for i, line in enumerate(lines):
                    if line.startswith("trigger:"):
                        lines.insert(i + 1, f"category: {category}")
                        break
                target_prompt.write_text("\n".join(lines) + "\n", encoding="utf-8")
                print(f"  Added category: {category}")
            
            # Update template references in prompt
            new_text = target_prompt.read_text(encoding="utf-8")
            # Fix template paths: templates/old -> templates/ (now local)
            new_text = re.sub(r'templates/\.\./', 'templates/', new_text)
            new_text = re.sub(r'templates/[^/]+/', 'templates/', new_text)
            target_prompt.write_text(new_text, encoding="utf-8")
            
            # Create README in templates if empty
            if not list(target_templates.glob("*.md")):
                readme = target_templates / "README.md"
                readme.write_text(f"# Templates for {trigger}\n\nAdd template files here.\n", encoding="utf-8")
                print(f"  Created empty README.md in templates/")
    
    print("\nMigration complete!")


if __name__ == "__main__":
    import sys
    dry_run = "--execute" not in sys.argv
    migrate_prompts(dry_run=dry_run)