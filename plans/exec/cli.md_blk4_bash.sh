#!/bin/bash
# Auto-extracted from: cli.md
# Source block language: bash
hermes --continue                          # Resume the most recent CLI session
hermes -c                                  # Short form
hermes -c "my project"                     # Resume a named session (latest in lineage)
hermes --resume 20260225_143052_a1b2c3     # Resume a specific session by ID
hermes --resume "refactoring auth"         # Resume by title
hermes --resume latest                     # Resume the most recent session (same as -c)
hermes --resume latest --in ./my-project   # Latest session for ./my-project's workspace
hermes -r 20260225_143052_a1b2c3           # Short form
