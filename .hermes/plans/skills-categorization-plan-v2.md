# Skills Categorization Plan (Rebuilt)

**Generated:** 2026-06-22
**Total skills:** 344 (334 mapped + 10 skipped for YAML repair)
**Uncategorized on disk:** 74 flat skills
**Uncategorized in frontmatter:** needs analysis

## Approach

Per skill-judge reference: `hermes skills list` reads Category from frontmatter `metadata.hermes.category`, NOT from directory structure. Physical moves are cosmetic. Strategy: add/update `category:` in frontmatter rather than moving directories.

## Skills Needing Category Assignment

| Skill | Target Category | Rationale |
|-------|----------------|-----------|
| 1password | productivity | Password management CLI |
| 3-statement-model | productivity | Excel financial modeling |
| accelerate | mlops | Distributed training API |
| agentmail | productivity | Email for agents |
| antigravity-cli | devops | Antigravity CLI operations |
| axolotl | mlops | LLM fine-tuning |
| baoyu-article-illustrator | creative | Article illustration |
| baoyu-comic | creative | Knowledge comics |
| bioinformatics | mlops | Bioinformatics tools |
| blackbox | autonomous-ai-agents | AI coding agent |
| blender-mcp | creative | Blender 3D control |
| bun-nextjs | software-development | Next.js + Bun |
| bun-shell | software-development | Bun shell scripting |
| canvas | productivity | Canvas LMS integration |
| chroma | data-science | Embedding database |
| ci-cd-best-practices | devops | CI/CD best practices |
| ci-cd-pipeline-builder | devops | Pipeline generation |
| claude-code | autonomous-ai-agents | Claude Code CLI agent |
| clip | mlops | Vision-language model |
| code-wiki | development | Wiki doc generation |
| concept-diagrams | creative | SVG diagram generation |
| creative-ideation | planning | Idea generation |
| darwinian-evolver | development | Prompt/code evolution |
| dcf-model | productivity | DCF valuation in Excel |
| django-application | software-development | Django applications |
| django-celery | software-development | Django + Celery |
| domain-intel | devops | Domain reconnaissance |
| drawio-skill | creative | Draw.io diagrams |
| drug-discovery | mlops | Pharmaceutical research |
| duckduckgo-search | research | Web search via DDG |
| evm | blockchain | EVM blockchain client |
| excel-author | productivity | Excel workbook authoring |
| faiss | mlops | Vector similarity search |
| fastmcp | mcp | MCP server building |
| fitness-nutrition | productivity | Workout/nutrition |
| github-repo-management | github | Repo management |
| gitnexus-explorer | development | Codebase indexing |
| guidance | mlops | LLM output control |
| here-now | productivity | Static site publishing |
| hermes-agent | devops | Hermes Agent config |
| honcho | mlops | Cross-session memory |
| huggingface-tokenizers | mlops | Tokenizers |
| hyperframes | creative | HTML video compositions |
| hyperliquid | blockchain | Hyperliquid market data |
| instructor | mlops | Structured LLM output |
| kanban-video-orchestrator | autonomous-ai-agents | Multi-agent video prod |
| llava | mlops | Vision-language model |
| mcporter | mcp | MCP server management |
| meme-generation | creative | Meme image generation |
| memento-flashcards | productivity | Spaced repetition |
| nemo-curator | mlops | GPU data curation |
| neuroskill-bci | mlops | BCI integration |
| one-three-one-rule | planning | Planning framework |
| openclaw-migration | devops | Claw migration |
| openhands | autonomous-ai-agents | OpenHands coding agent |
| osint-investigation | research | OSINT framework |
| oss-forensics | research | Supply chain forensics |
| outlines | mlops | Structured generation |
| page-agent | software-development | HTML page agent |
| pinecone | data-science | Vector database |
| pinggy-tunnel | devops | Localhost tunnels |
| pptx-author | productivity | PowerPoint building |
| pytorch-fsdp | mlops | FSDP training |
| pytorch-lightning | mlops | PyTorch framework |
| qmd | productivity | Knowledge base search |
| searxng-search | research | Meta search |
| sherlock | research | OSINT username search |
| shop-app | productivity | Shop.app integration |
| shopify | productivity | Shopify API |
| siyuan | note-taking | SiYuan Note API |
| solana | blockchain | Solana blockchain |
| stocks | productivity | Stock quotes |
| telephony | devops | Phone capabilities |
| tensorrt-llm | mlops | TensorRT optimization |
| torchtitan | mlops | Distributed LLM pretraining |
| unsloth | mlops | Fast LoRA fine-tuning |
| web-pentest | security | Web penetration testing |
| whisper | mlops | Speech recognition |
| youtube-full | media | YouTube full access |

## Execution

1. Patch each flat skill's frontmatter to add `category:` under `metadata.hermes`
2. Skip skills that already have `category:` in frontmatter
3. Do NOT physically move directories (cosmetic only)
4. Verify with `hermes skills list --source local`
