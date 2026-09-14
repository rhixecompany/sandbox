# Hermes config diff evidence

This artifact contains redacted, tool-generated comparison results. It records paths, types, counts, versions, hashes, and exit codes only; it does not contain secrets, tokens, passwords, or `.env` values.

## Inventory

| Candidate | Size (bytes) | YAML | Version | SHA-256 prefix |
|---|---:|---|---:|---|
| `$HERMES_HOME/config.yaml` | 101526 | valid | 44 | `f75aabf74007e3a9` |
| `$HERMES_HOME/config.yaml.bak` | 186900 | valid | 42 | `89e1f8a63fbb68f4` |
| `$HERMES_HOME/config.yaml.bak.sync.20260824_185038` | 117804 | valid | 37 | `a86650e0077552c9` |
| `$HERMES_HOME/backups/config/config.yaml.corrupt.20260905-060730.bak` | 147582 | invalid at line 2769 | — | `06bd3f52196275c8` |
| `$HERMES_HOME/backups/config/config.yaml.corrupt.20260907-175103.bak` | 90155 | invalid at line 1169 | — | `4aab5444ad6cce19` |

## Scalar-path comparison

| Comparison | Current-only paths | Backup-only paths | Changed shared values |
|---|---:|---:|---:|
| Current vs `config.yaml.bak` | 57 | 2 | 136 |
| Current vs `config.yaml.bak.sync.20260824_185038` | 730 | 243 | 185 |

## Decision

The active config is the highest-version parseable candidate (version 44). The older parseable backups contain stale or conflicting values, and the two snapshot backups are malformed. No safe, schema-supported, non-conflicting addition was identified; the deprecated-looking `model.api_mode` path was not copied from the older backup.

The active file was not rewritten with raw YAML. `hermes config migrate` was run through the CLI and exited 0; it made no content change (the active SHA-256 prefix remained `f75aabf74007e3a9`). `hermes config check` was then run and exited 0 with config version 44.

## CLI warnings preserved

The migration/check output reported that configured platform toolsets `chrome_profiles`, `opencode`, and `weather` are not in the currently discovered standard toolset list and suggested `hermes-cli`/`hermes-telegram`. This warning was not “fixed” by deleting configuration; the names may correspond to deferred or installed tools and require a separate capability decision.
