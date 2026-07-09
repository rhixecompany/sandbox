# Consolidation Report

Generated: July 1, 2026

## Overview

- **Total skills analyzed**: 455
- **Potential overlaps**: 6537 (keyword-based)
- **Thin skills (<100 lines, no phases)**: 25
- **Skills missing structure**: 157

## Remediation Impact

After running Phase 1.5 remediation on 50 FAIL skills:
- Thin skills reduced from 27 → 25
- Missing structure reduced from 182 → 157
- 25 skills received frontmatter/section patches

## Duplicate Resolution (from dedupe report)

61 skills exist in both flat (top-level) and categorized subdirectories. Recommended action:
- **Keep**: Category subdirectory version (e.g., `devops/1password/SKILL.md`)
- **Delete**: Flat version (e.g., `skills/1password/SKILL.md`)
- Use `rm -rf skills/<flat-skill-name>` for safe removal

## Candidate Umbrella Merges

### 1. Firecrawl Umbrella
**Merge into**: `firecrawl-scrape` or create new `firecrawl` umbrella

| Thin Skill | Lines | Absorb Into |
|------------|-------|-------------|
| firecrawl-agent | 73 | firecrawl-scrape |
| firecrawl-crawl | 74 | firecrawl-scrape |
| firecrawl-download | 85 | firecrawl-scrape |
| firecrawl-map | 66 | firecrawl-scrape |
| firecrawl-scrape | 85 | (umbrella) |
| firecrawl-search | (not thin) | firecrawl-scrape |

### 2. Package Manager Umbrella
| Thin Skill | Lines | Absorb Into |
|------------|-------|-------------|
| uv-package-manager | 78 | skills or hermes-setup |
| pnpm-package-manager | 59 | skills or hermes-setup |

### 3. DevOps / CLI Tools Umbrella
| Thin Skill | Lines | Absorb Into |
|------------|-------|-------------|
| boost-prompt | 49 | prompt-batch-fixer |
| no-git-delete | 53 | git-helper |
| git-patch-management | 55 | git-helper |
| github-copilot-cli | 81 | gh-cli |
| skills-tools-preflight-check | 50 | hermes-skills |

### 4. General Thin Skills
| Thin Skill | Lines | Suggested Umbrella |
|------------|-------|-------------------|
| joyride | 50 | autonomous-ai-agents |
| acpx-executor | 51 | devops |
| dispatching-parallel-agents | 53 | autonomous-ai-agents |
| tmux-terminal-multiplexer | 54 | devops |
| parallel-cli-web-research | 56 | research |
| simplify | 65 | productivity |
| sequential-orchestration | 68 | autonomous-ai-agents |
| unsloth | 84 | mlops |
| stocks | 95 | finance |
| canvas | 98 | productivity |

## Structure Issues

### Skills Missing Required Sections

| Missing Section | Count |
|----------------|-------|
| Missing "When to Use" | 109 |
| Missing Workflow | 329 |
| Missing Verification Checklist | 214 |
| Missing Best Practices | 500 |

After remediation, 157 skills still lack key structural elements.

## Recommended Actions

1. **Duplicate cleanup**: Remove 61 flat copies where categorized versions exist
2. **Execute umbrella merges**: Use `merge_skill.py` for top candidates
3. **Firecrawl consolidation**: Merge 6 thin firecrawl skills into 1 umbrella
4. **Package manager consolidation**: Merge uv/pnpm into devops umbrella
5. **Git tool consolidation**: Merge git-patch-management, no-git-delete into git-helper
6. **Re-judge** after consolidation to verify score improvements
