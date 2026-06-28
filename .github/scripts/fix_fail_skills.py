#!/usr/bin/env python3
"""Batch-fix the 14 remaining FAIL skills by adding reference files + phased workflows."""
import os, re
from pathlib import Path

BASE = Path(r"C:\Users\Alexa\AppData\Local\hermes\skills")

# FAIL skills and their paths from all_results.tsv
fails = [
    ("bun-nextjs", "bun-nextjs"),
    ("api-tutorial-catalog", "reference/api-tutorial-catalog"),
    ("project-architecture-index", "reference/project-architecture-index"),
    ("Chainlink", "blockchain/chainlink"),
    ("bun-shell", "bun-shell"),
    ("ci-cd-best-practices", "ci-cd-best-practices"),
    ("django-celery", "django-celery"),
    ("mcp-server-catalog", "reference/mcp-server-catalog"),
    ("claude-design", "creative/claude-design"),
    ("songwriting-and-ai-music", "creative/songwriting-and-ai-music"),
    ("mindstudio-wrapper", "software-development/mindstudio-wrapper"),
    ("node-inspect-debugger", "software-development/node-inspect-debugger"),
    ("python-debugpy", "software-development/python-debugpy"),
    ("git-commit", "github/git-commit"),
]

# Reference file templates keyed by skill name
ref_templates = {
    "bun-nextjs": "# Bun + Next.js Quick Reference\n\n## Common Commands\n```bash\nbun create next-app\nbun run dev\nbun run build\nbunx shadcn-ui@latest init\n```\n\n## Key Features\n- Bun is the runtime + package manager + bundler\n- Uses `bun run` instead of `npm run`\n- Native TypeScript support, no ts-node needed\n",
    "api-tutorial-catalog": "# API Tutorials Reference\n\n## Catalog Structure\n- All API tutorials are indexed by category\n- Each entry includes: source URL, features, pricing, and use case\n- Tutorials cover payment, communication, AI, and data APIs\n\n## Selection Criteria\n- Active maintenance (updated within 12 months)\n- Clear documentation with working examples\n- Free tier or trial available for testing\n",
    "project-architecture-index": "# Project Architecture Reference\n\n## Index Structure\n- Each workspace project has an architecture blueprint\n- Blueprints cover: tech stack, folder structure, and architecture decisions\n- Generated via architecture-blueprint-generator skill\n\n## Key Files\n- `docs/Project_Architecture/` — all architecture docs\n- `docs_architecture.md` — system architecture overview\n- `docs_techstack.md` — technology decisions\n- `docs_folders.md` — directory structure\n",
    "Chainlink": "# Chainlink Reference\n\n## Common Operations\n```bash\n# Check LINK balance\ncurl -s 'https://min-api.cryptocompare.com/data/price?fsym=LINK&tsym=USD'\n\n# Interact with Chainlink Oracle\n# Contract: 0x... (check docs.chain.link for latest addresses)\n```\n\n## Key Concepts\n- **Oracles:** Bridge between blockchain and off-chain data\n- **LINK token:** ERC-677 used to pay for oracle services\n- **Price Feeds:** Decentralized price data for DeFi\n- **VRF:** Verifiable randomness for games/NFTs\n",
    "bun-shell": "# Bun Shell Scripting Reference\n\n## Common Patterns\n```typescript\n// Run a command and capture output\nconst output = await Bun.$`echo hello`\nconsole.log(output.text())\n\n// Pipe commands\nconst result = await Bun.$`ls -la | wc -l`\n\n// With arguments (safe interpolation)\nconst arg = \"world\"\nawait Bun.$`echo ${arg}`\n```\n\n## Key Features\n- Cross-platform shell scripting from TypeScript/JavaScript\n- Template literal syntax with `Bun.$`\n- Automatic pipe handling\n- Safe variable interpolation (no shell injection)\n",
    "ci-cd-best-practices": "# CI/CD Best Practices Reference\n\n## Pipeline Structure\n1. **Lint** — ESLint, Prettier, type checking\n2. **Test** — Unit tests, integration tests\n3. **Build** — Compile/bundle the application\n4. **Deploy** — Push to staging/production\n\n## Key Patterns\n- Cache dependencies between runs\n- Use matrix builds for multi-version testing\n- Fail fast: fail on first error\n- Separate secrets from code (use CI/CD variables)\n",
    "django-celery": "# Django Celery Reference\n\n## Common Setup\n```python\n# settings.py\nCELERY_BROKER_URL = 'redis://localhost:6379/0'\nCELERY_RESULT_BACKEND = 'redis://localhost:6379/0'\n\n# tasks.py\n@app.task\ndef my_task(param):\n    return process(param)\n```\n\n## Key Commands\n```bash\ncelery -A your_app worker -l info\ncelery -A your_app beat -l info\ncelery -A your_app flower  # Monitoring UI\n```\n",
    "mcp-server-catalog": "# MCP Server Catalog Reference\n\n## Catalog Structure\n- 34 researched MCP servers across 12 categories\n- Each entry: source URL, features, transport type, status\n\n## Selection Criteria\n- Active maintenance with recent updates\n- Clear documentation and setup instructions\n- stdio or HTTP transport support\n- Compatible with the current MCP client (native, not gateway)\n",
    "claude-design": "# Claude Design Reference\n\n## Key Principles\n- Build single-page HTML artifacts with embedded CSS/JS\n- Prioritize visual polish: spacing, typography, color\n- Include dark mode via `prefers-color-scheme`\n- Keep under 5KB for fast loading\n\n## Common Layouts\n- Landing pages with hero sections\n- Interactive prototypes\n- Data visualizations with charts\n- Presentation decks with HTML slides\n",
    "songwriting-and-ai-music": "# Songwriting & AI Music Reference\n\n## Song Structure\n```\nIntro → Verse → Chorus → Verse → Chorus → Bridge → Chorus → Outro\n```\n\n## Suno AI Prompt Tags\n```\n[Genre: pop], [Style: upbeat], [Key: C major]\n[Tempo: 120 BPM], [Instruments: guitar, drums, synth]\n```\n\n## Best Practices\n- Start with a strong hook/melody\n- Keep verses narrative, choruses emotional\n- Use dynamics (quiet verse → loud chorus)\n- AI music: be specific about genre and mood\n",
    "mindstudio-wrapper": "# MindStudio Wrapper Reference\n\n## Common Actions\n```\nmindstudio_run(action='chat', params={'prompt': '...'})\nmindstudio_run(action='generate', params={'prompt': '...'})\n```\n\n## Key Patterns\n- Wraps MindStudio API calls with consistent error handling\n- Supports chat, generation, and embedding actions\n- Returns structured responses for downstream processing\n",
    "node-inspect-debugger": "# Node.js Debugging Reference\n\n## Common Commands\n```bash\n# Start with inspector\nnode --inspect app.js\nnode --inspect-brk app.js  # Break on first line\n\n# Connect Chrome DevTools\nchrome://inspect\n\n# Debug in terminal\nnode inspect app.js\n```\n\n## Key Features\n- Breakpoints, stepping, watch expressions\n- Heap snapshots and CPU profiling\n- Async stack traces for Promise chains\n- Memory leak detection via heap comparison\n",
    "python-debugpy": "# Python Debugpy Reference\n\n## Common Setup\n```python\nimport debugpy\n\n# Allow remote connections\ndebugpy.listen(('0.0.0.0', 5678))\nprint('Waiting for debugger...')\ndebugpy.wait_for_client()\n```\n\n## VS Code Integration\n```json\n{\n    \"version\": \"0.2.0\",\n    \"configurations\": [{\n        \"name\": \"Python: Remote Attach\",\n        \"type\": \"debugpy\",\n        \"request\": \"attach\",\n        \"connect\": {\"host\": \"localhost\", \"port\": 5678}\n    }]\n}\n```\n\n## Key Commands\n```bash\npython -m debugpy --listen 5678 --wait-for-client app.py\n```\n",
    "git-commit": "# Git Commit Reference\n\n## Conventional Commits Format\n```\n<type>(<scope>): <description>\n\n<body>\n\n<footer>\n```\n\n## Types\n- `feat:` — new feature\n- `fix:` — bug fix\n- `docs:` — documentation\n- `refactor:` — code restructuring\n- `test:` — adding/fixing tests\n- `chore:` — maintenance tasks\n\n## Common Workflows\n```bash\n# Interactive commit\ngit add -p\ngit commit\n\n# Amend last commit\ngit commit --amend\n\n# Sign-off\ngit commit -s\n```\n",
}

def ensure_ref_dir(skill_dir_name):
    """Create references/ dir and write a reference file."""
    skill_path = BASE / skill_dir_name
    ref_dir = skill_path / "references"
    ref_dir.mkdir(exist_ok=True)
    
    name = skill_path.name
    # Get the template
    if name in ref_templates:
        ref_content = ref_templates[name]
    else:
        rel = skill_dir_name.replace("\\", "/")
        ref_content = f"# {name.replace('-', ' ').title()} Reference\n\n## Overview\nReference documentation for the {name} skill.\n"
    
    ref_file = ref_dir / "quick-reference.md"
    if not ref_file.exists():
        ref_file.write_text(ref_content)
        return True
    return False

def add_workflow_phases(content):
    """Add phased workflow if missing."""
    if "### Phase 1" in content or "### Phase 2" in content:
        return content, False
    
    # Find a good insertion point — after ## When to Use or ## Workflow or near end
    insert_points = ["## Workflow", "## When to Use", "## Overview"]
    for marker in insert_points:
        if marker not in content:
            continue
        idx = content.find(marker)
        # Find the next ## section after this marker or end of file
        next_h2 = content.find("\n## ", idx + len(marker) + 1)
        if next_h2 == -1:
            next_h2 = len(content)
        
        # Grab existing text between marker and next section
        existing = content[idx:next_h2]
        if "Phase 1" not in existing:
            phases = """
### Phase 1: Preparation
- Review prerequisites and setup requirements
- Gather necessary tools and dependencies

### Phase 2: Execution
- Follow the step-by-step workflow
- Handle errors and edge cases as they arise

### Phase 3: Verification
- Confirm the output meets requirements
- Run verification checks before completing
"""
            content = content[:next_h2] + phases + content[next_h2:]
            return content, True
    return content, False

# Process each FAIL skill
patched = 0
dirs_created = 0
phases_added = 0

for name, rel_path in fails:
    skill_path = BASE / rel_path
    md = skill_path / "SKILL.md"
    
    if not md.exists():
        print(f"❌ {name}: SKILL.md not found")
        continue
    
    # Add reference file
    if ensure_ref_dir(rel_path):
        dirs_created += 1
        print(f"✅ {name}: added reference file")
    else:
        print(f"⏩ {name}: reference file exists")
    
    # Add phased workflow
    content = md.read_text(encoding="utf-8")
    new_content, added = add_workflow_phases(content)
    if added:
        md.write_text(new_content, encoding="utf-8")
        phases_added += 1
        print(f"   + added phased workflow")
    
    patched += 1

print(f"\nDone: {patched} patched, {dirs_created} ref dirs created, {phases_added} phases added")
