#!/usr/bin/env python3
"""Categorize flat skills by adding category to frontmatter metadata."""
import os, re, json, sys
from pathlib import Path

SKILLS_BASE = Path(r"C:\Users\Alexa\AppData\Local\hermes\skills")

# Category mapping: skill_name -> target_category
CATEGORY_MAP = {
    "1password": "productivity",
    "3-statement-model": "productivity",
    "accelerate": "mlops",
    "agentmail": "productivity",
    "antigravity-cli": "devops",
    "axolotl": "mlops",
    "baoyu-article-illustrator": "creative",
    "baoyu-comic": "creative",
    "bioinformatics": "mlops",
    "blackbox": "autonomous-ai-agents",
    "blender-mcp": "creative",
    "bun-nextjs": "software-development",
    "bun-shell": "software-development",
    "canvas": "productivity",
    "chroma": "data-science",
    "ci-cd-best-practices": "devops",
    "ci-cd-pipeline-builder": "devops",
    "claude-code": "autonomous-ai-agents",
    "clip": "mlops",
    "code-wiki": "development",
    "concept-diagrams": "creative",
    "creative-ideation": "planning",
    "darwinian-evolver": "development",
    "dcf-model": "productivity",
    "django-application": "software-development",
    "django-celery": "software-development",
    "domain-intel": "devops",
    "drawio-skill": "creative",
    "drug-discovery": "mlops",
    "duckduckgo-search": "research",
    "evm": "blockchain",
    "excel-author": "productivity",
    "faiss": "mlops",
    "fastmcp": "mcp",
    "fitness-nutrition": "productivity",
    "github-repo-management": "github",
    "gitnexus-explorer": "development",
    "guidance": "mlops",
    "here-now": "productivity",
    "hermes-agent": "devops",
    "honcho": "mlops",
    "huggingface-tokenizers": "mlops",
    "hyperframes": "creative",
    "hyperliquid": "blockchain",
    "instructor": "mlops",
    "kanban-video-orchestrator": "autonomous-ai-agents",
    "llava": "mlops",
    "mcporter": "mcp",
    "meme-generation": "creative",
    "memento-flashcards": "productivity",
    "nemo-curator": "mlops",
    "neuroskill-bci": "mlops",
    "one-three-one-rule": "planning",
    "openclaw-migration": "devops",
    "openhands": "autonomous-ai-agents",
    "osint-investigation": "research",
    "oss-forensics": "research",
    "outlines": "mlops",
    "page-agent": "software-development",
    "pinecone": "data-science",
    "pinggy-tunnel": "devops",
    "pptx-author": "productivity",
    "pytorch-fsdp": "mlops",
    "pytorch-lightning": "mlops",
    "qmd": "productivity",
    "searxng-search": "research",
    "sherlock": "research",
    "shop-app": "productivity",
    "shopify": "productivity",
    "siyuan": "note-taking",
    "solana": "blockchain",
    "stocks": "productivity",
    "telephony": "devops",
    "tensorrt-llm": "mlops",
    "torchtitan": "mlops",
    "unsloth": "mlops",
    "web-pentest": "security",
    "whisper": "mlops",
    "youtube-full": "media",
}

def get_frontmatter_boundaries(text):
    """Find frontmatter start/end indices. Returns (start, end) or None."""
    m = re.match(r"^---\n(.*?)\n---", text, re.DOTALL)
    if m:
        return (m.start(1), m.end(1))
    return None

def add_category_to_fm(fm_text, category):
    """Add metadata.hermes.category to YAML frontmatter text."""
    # Check if metadata.hermes already exists
    has_metadata_section = False
    lines = fm_text.split("\n")
    new_lines = []
    in_metadata_block = False
    metadata_depth = 0
    found_category = False
    in_hermes_block = False

    for line in lines:
        stripped = line.rstrip()
        # Check for existing category
        if re.match(r"^\s*category:\s*\S", stripped):
            found_category = True
        # Track metadata: block
        if re.match(r"^metadata:", stripped):
            has_metadata_section = True
            in_metadata_block = True
            metadata_depth = 1
        elif in_metadata_block and re.match(r"^  hermes:", stripped):
            in_hermes_block = True
            metadata_depth = 2
        elif in_metadata_block and in_hermes_block:
            # Check if we're still inside hermes block
            indent = len(stripped) - len(stripped.lstrip()) if stripped.strip() else 999
            if indent < 4 and stripped.strip():
                in_hermes_block = False
                # Insert category before this line
                new_lines.append("    category: " + category)
                in_metadata_block = False
        elif in_metadata_block and metadata_depth == 1 and stripped.strip():
            indent = len(stripped) - len(stripped.lstrip())
            if indent < 2:
                in_metadata_block = False
        new_lines.append(stripped)

    # Post-process: insert category if not found
    if not found_category:
        if in_hermes_block:
            # Inside hermes block, add category
            new_lines.append("    category: " + category)
        elif has_metadata_section:
            # Has metadata but no hermes, add hermes block before metadata end
            # Find metadata block end and insert
            result = []
            inserted = False
            for line in new_lines:
                result.append(line)
                if line.rstrip() == "metadata:" and not inserted:
                    result.append("  hermes:")
                    result.append("    category: " + category)
                    inserted = True
            new_lines = result
        else:
            # No metadata section at all, append at end
            new_lines.append("metadata:")
            new_lines.append("  hermes:")
            new_lines.append("    category: " + category)

    return "\n".join(new_lines)

def process_skill(skill_dir_name):
    """Process a flat skill directory."""
    skill_path = SKILLS_BASE / skill_dir_name
    md_path = skill_path / "SKILL.md"
    
    if not md_path.exists():
        return False, f"SKILL.md not found at {md_path}"
    
    text = md_path.read_text(encoding="utf-8", errors="ignore")
    fm_bounds = get_frontmatter_boundaries(text)
    if not fm_bounds:
        return False, f"No frontmatter in {skill_dir_name}"
    
    fm_start, fm_end = fm_bounds
    fm_text = text[fm_start:fm_end]
    
    # Check if already has category
    if re.search(r"^\s*category:\s*\S", fm_text, re.MULTILINE):
        return False, f"Already has category"
    
    category = CATEGORY_MAP.get(skill_dir_name)
    if not category:
        return False, f"No category mapping for {skill_dir_name}"
    
    new_fm = add_category_to_fm(fm_text, category)
    new_text = text[:fm_start] + new_fm + text[fm_end:]
    
    if new_text == text:
        return False, f"No changes needed"
    
    md_path.write_text(new_text, encoding="utf-8")
    return True, f"Added category: {category}"

# Main: discover flat skills and process them
flat_dirs = [d.name for d in SKILLS_BASE.iterdir() if d.is_dir() and "/" not in d.name]

patched = 0
skipped_categorized = 0
skipped_no_map = 0
errors = []

for d in sorted(flat_dirs):
    success, msg = process_skill(d)
    if success:
        print(f"✅ {d}: {msg}")
        patched += 1
    elif "Already has category" in msg:
        skipped_categorized += 1
    elif "No category mapping" in msg:
        skipped_no_map += 1
        print(f"⏭️ {d}: {msg}")
    else:
        errors.append(f"{d}: {msg}")
        print(f"❌ {d}: {msg}")

print(f"\n--- Summary ---")
print(f"Patched: {patched}")
print(f"Already categorized: {skipped_categorized}")
print(f"No category mapping: {skipped_no_map}")
print(f"Errors: {len(errors)}")
for e in errors:
    print(f"  ERROR: {e}")
