# Hermes Achievements Plugin

Achievement and unlock tracking system for Hermes Agent. Tracks milestones, usage patterns, and capability unlocks across sessions.

## What This Plugin Does

- Tracks achievement unlocks (capability milestones, usage patterns)
- Maintains persistent state across sessions via `state.json`
- Stores scan snapshots and checkpoints for resume capability
- Provides gamification layer for agent capabilities

## State Files

| File | Purpose |
|------|---------|
| `state.json` | Current achievement state — unlocks, tiers, timestamps |
| `scan_snapshot.json` | Last full workspace scan result |
| `scan_checkpoint.json` | Incremental scan checkpoint for resume |

## Hermes Integration

This is a **bundled Hermes plugin** — it ships with Hermes and is not from the awesome-copilot collection. It is always active and requires no configuration.

## Source

Built-in Hermes plugin.

## License

MIT
