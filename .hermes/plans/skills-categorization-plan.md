# Skills Categorization Plan

**Goal:** Move 26 uncategorized local skills to correct category folders.

**Source:** `docs/local-skills.md` (196 skills, 26 without category)

## Uncategorized Skills & Target Categories

| Skill | Target Category | Rationale |
|-------|----------------|-----------|
| Chainlink | blockchain | Blockchain/oracle integration |
| distributed-llm-pretraining-torchtitan | mlops | Distributed LLM training |
| here.now | productivity | Static site publishing |
| hermes-breakdown | autonomous-ai-agents | Project breakdown/epic→feature |
| hermes-hooks | devops | Hook lifecycle management |
| hermes-mcp | mcp | MCP server lifecycle |
| hermes-skills | devops | Skills management |
| hermes-system-maintenance | devops | Operational troubleshooting |
| huggingface-accelerate | mlops | Distributed training API |
| ideation | planning | Creative idea generation |
| inference-sh-cli | devops | AI apps CLI (150+ apps) |
| lambda-labs-gpu-cloud | devops | GPU cloud instances |
| modal-serverless-gpu | devops | Serverless GPU platform |
| optimizing-attention-flash | mlops | Flash Attention optimization |
| peft-fine-tuning | mlops | LoRA/QLoRA fine-tuning |
| profile-maintenance | devops | Profile identity & state |
| qdrant-vector-search | mlops | Vector similarity search |
| qwen-code | autonomous-ai-agents | ACPX coding agent |
| simpo-training | mlops | Preference optimization |
| skill-creator | development | Authoring in-repo skills |
| skill-judge | qa | Skill quality evaluation |
| stable-diffusion-image-generation | mlops | Text-to-image generation |
| template | autonomous-ai-agents | Skill scaffolding template |
| using-git-worktrees | development | Git worktrees workflow |
| validate-memories | devops | USER.md/MEMORY.md validation |
| writing-skills | development | Skill authoring guidance |

## New Categories to Create
- `blockchain` (for Chainlink)

## Execution Steps
1. Create category directories under `C:\Users\Alexa\AppData\Local\hermes\skills\`
2. Move each skill directory to its target category
3. Verify all skills have categories

## Verification
- Run `hermes skills list --source local` and confirm 0 skills with empty category
- Count skills per category matches expected distribution