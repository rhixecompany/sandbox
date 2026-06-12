import re
import os

# Use the actual working directory
base = os.path.dirname(os.path.abspath(__file__))

# Read installed skills
installed_path = os.path.join(base, 'installed_clean.txt')
with open(installed_path, 'r') as f:
    installed = set(line.strip().lower() for line in f if line.strip())

# Official skills from the browse output (96 unique skills from pages 1-10)
official_skills = {
    '1password', '3-statement-model', 'adversarial-ux-test', 'agentmail', 
    'antigravity-cli', 'axolotl', 'baoyu-article-illustrator', 'baoyu-comic',
    'baoyu-infographic', 'bioinformatics', 'blackbox', 'blender-mcp', 'canvas',
    'chroma', 'clip', 'code-wiki', 'comps-analysis', 'concept-diagrams',
    'darwinian-evolver', 'dcf-model', 'distributed-llm-pretraining', 'docker-management',
    'domain-intel', 'drug-discovery', 'dspy', 'duckduckgo-search', 'evm',
    'excel-author', 'faiss', 'fastmcp', 'fine-tuning-with-trl', 'fitness-nutrition',
    'gitnexus-explorer', 'godmode', 'grok', 'guidance', 'here-now', 'hermes-s6-container-supervision',
    'honcho', 'huggingface-accelerate', 'huggingface-tokenizers', 'hyperframes',
    'hyperliquid', 'ideation', 'inference-sh-cli', 'instructor', 'kanban-video-orchestrator',
    'lambda-labs-gpu-cloud', 'lbo-model', 'llava', 'mcporter', 'meme-generation',
    'memento-flashcards', 'merger-model', 'minecraft-modpack-server', 'modal-serverless-gpu',
    'nemo-curator', 'neuroskill-bci', 'obliteratus', 'one-three-one-rule', 'openclaw-migration',
    'openhands', 'optimizing-attention-flash', 'osint-investigation', 'oss-forensics', 'outlines',
    'page-agent', 'parallel-cli', 'peft-fine-tuning', 'pinecone', 'pinggy-tunnel',
    'pixel-art', 'pokemon-player', 'pptx-author', 'pytorch-fsdp', 'pytorch-lightning',
    'qdrant-vector-search', 'qmd', 'rest-graphql-debug', 'scrapling', 'searxng-search',
    'sherlock', 'shop-app', 'shopify', 'simpo-training', 'siyuan', 'slime-rl-training',
    'solana', 'sparse-autoencoder', 'stable-diffusion-image-generation', 'stocks',
    'subagent-driven-development', 'telephony', 'tensorrt-llm', 'unsloth', 'watchers',
    'web-pentest', 'whisper'
}

print(f"Official skills: {len(official_skills)}")

# Find not installed
not_installed = official_skills - installed
print(f"\nNot installed ({len(not_installed)}):")
for s in sorted(not_installed):
    print(f"  - {s}")

# Check which official skills ARE installed
installed_official = official_skills & installed
print(f"\nAlready installed official ({len(installed_official)}):")
for s in sorted(installed_official):
    print(f"  + {s}")

# Extra installed (local/builtin not in official list)
extra_installed = installed - official_skills
print(f"\nExtra installed (local/builtin): {len(extra_installed)}")
for s in sorted(extra_installed)[:50]:
    print(f"  + {s}")
if len(extra_installed) > 50:
    print(f"  ... and {len(extra_installed) - 50} more")

# Write not_installed to file for next step
not_installed_path = os.path.join(base, 'not_installed_official.txt')
with open(not_installed_path, 'w') as f:
    for s in sorted(not_installed):
        f.write(s + '\n')