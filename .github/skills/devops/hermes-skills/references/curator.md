# Autonomous Curator (v0.12.0+)

## Overview
The curator maintains the skill library automatically on a 7-day cycle.

## Lifecycle
```
create → edit → use → update → (consolidate) → delete
```

## Curator Actions
- **Grades skills** by usage, success rate, freshness
- **Consolidates** near-duplicates
- **Prunes** stale/unused skills
- **Logs decisions** to `~/.hermes/logs/curator/`

## Configuration
```yaml
# In config.yaml
curator:
  enabled: true
  interval_hours: 168        # 7 days
  min_idle_hours: 2
  stale_after_days: 30
  archive_after_days: 90
  prune_builtins: true
  backup:
    enabled: true
    keep: 5
```

## Integration with Other Features
| Feature | Interaction |
|---------|-------------|
| **Memory** | Skills can `memory add` facts; memory can reference skill names |
| **Tools** | `requires_toolsets` / `fallback_for_toolsets` for conditional loading |
| **MCP** | Skills can invoke MCP tools via `execute_code` |
| **Delegation** | Skills can spawn subagents with `delegate_task` |
| **Hooks** | Skills can register hooks in `config.yaml` |

## Manual Override
- Curator only affects skills not recently used/modified
- Edited, hub-installed, and custom skills are always preserved
- `--remove` only deletes **unmodified** bundled skills (byte-identical)