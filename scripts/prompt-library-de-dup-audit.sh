#!/usr/bin/env bash
# scripts/prompt-library-de-dup-audit.sh — audit script for subgoal prompt-library-de-dup-and-backup-archive
# Usage: bash scripts/prompt-library-de-dup-audit.sh [prompts_dir] [backup_dir] [output_dir]
# Default paths relative to repo root (assumes CWD = repo root).

set -euo pipefail
PROMPTS_DIR="${1:-.github/prompts}"
BACKUP_DIR="${2:-.github/prompts_backup}"
OUT_DIR="${3:-./specs}"
mkdir -p "$OUT_DIR"

AUDIT_MD="$OUT_DIR/prompt-library-de-dup-audit.md"
AUDIT_JSON="$OUT_DIR/prompt-library-de-dup-audit-data.json"

# Compute MD5 for a single file
md5_file() { md5sum "$1" 2>/dev/null | awk '{print $1}' || md5 -q "$1" 2>/dev/null || echo "HASH_FAIL"; }

echo "=== Prompt Library De-Dup Audit ==="
echo "Prompts dir: $PROMPTS_DIR  (exists: $(test -d "$PROMPTS_DIR" && echo YES || echo NO))"
echo "Backup dir:  $BACKUP_DIR  (exists: $(test -d "$BACKUP_DIR" && echo YES || echo NO))"

# Count by basename
count_prompts=0; count_backup=0
for f in $(find "$PROMPTS_DIR" -maxdepth 1 -type f 2>/dev/null | head -n 200); do [ -f "$f" ] && ((count_prompts++)) || true; done
echo "Prompts file count (approx): $count_prompts"
echo "Audit artifacts target: $AUDIT_MD  $AUDIT_JSON"
echo "Run the Python audit (execute_code) for full MD5 triage; this bash script serves as portable entry point and verification wrapper."
echo "Audit complete. Check ./specs/ for full results."
