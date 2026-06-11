#!/usr/bin/env bash
set -euo pipefail
QUARANTINE_DIR=.hermes/quarantine
mkdir -p "$QUARANTINE_DIR"
SKILL_DIR_BASE="$HOME/AppData/Local/hermes/skills"

if [ -d "$SKILL_DIR_BASE/unsloth" ]; then
  mv "$SKILL_DIR_BASE/unsloth" "$QUARANTINE_DIR/unsloth.disabled" || true
  echo "Moved unsloth to $QUARANTINE_DIR/unsloth.disabled"
  # hermes skills opt-out unsloth || true
fi
if [ -d "$SKILL_DIR_BASE/lambda-labs" ]; then
  mv "$SKILL_DIR_BASE/lambda-labs" "$QUARANTINE_DIR/lambda-labs.disabled" || true
  echo "Moved lambda-labs to $QUARANTINE_DIR/lambda-labs.disabled"
  # hermes skills opt-out lambda-labs || true
fi
if [ -d "$SKILL_DIR_BASE/web-pentest" ]; then
  mv "$SKILL_DIR_BASE/web-pentest" "$QUARANTINE_DIR/web-pentest.disabled" || true
  echo "Moved web-pentest to $QUARANTINE_DIR/web-pentest.disabled"
  # hermes skills opt-out web-pentest || true
fi
if [ -d "$SKILL_DIR_BASE/here-now" ]; then
  mv "$SKILL_DIR_BASE/here-now" "$QUARANTINE_DIR/here-now.disabled" || true
  echo "Moved here-now to $QUARANTINE_DIR/here-now.disabled"
  # hermes skills opt-out here-now || true
fi
if [ -d "$SKILL_DIR_BASE/openclaw-migration" ]; then
  mv "$SKILL_DIR_BASE/openclaw-migration" "$QUARANTINE_DIR/openclaw-migration.disabled" || true
  echo "Moved openclaw-migration to $QUARANTINE_DIR/openclaw-migration.disabled"
  # hermes skills opt-out openclaw-migration || true
fi
if [ -d "$SKILL_DIR_BASE/cli" ]; then
  mv "$SKILL_DIR_BASE/cli" "$QUARANTINE_DIR/cli.disabled" || true
  echo "Moved cli to $QUARANTINE_DIR/cli.disabled"
  # hermes skills opt-out cli || true
fi
if [ -d "$SKILL_DIR_BASE/fitness-nutrition" ]; then
  mv "$SKILL_DIR_BASE/fitness-nutrition" "$QUARANTINE_DIR/fitness-nutrition.disabled" || true
  echo "Moved fitness-nutrition to $QUARANTINE_DIR/fitness-nutrition.disabled"
  # hermes skills opt-out fitness-nutrition || true
fi
if [ -d "$SKILL_DIR_BASE/grok" ]; then
  mv "$SKILL_DIR_BASE/grok" "$QUARANTINE_DIR/grok.disabled" || true
  echo "Moved grok to $QUARANTINE_DIR/grok.disabled"
  # hermes skills opt-out grok || true
fi
if [ -d "$SKILL_DIR_BASE/oss-forensics" ]; then
  mv "$SKILL_DIR_BASE/oss-forensics" "$QUARANTINE_DIR/oss-forensics.disabled" || true
  echo "Moved oss-forensics to $QUARANTINE_DIR/oss-forensics.disabled"
  # hermes skills opt-out oss-forensics || true
fi
if [ -d "$SKILL_DIR_BASE/qmd" ]; then
  mv "$SKILL_DIR_BASE/qmd" "$QUARANTINE_DIR/qmd.disabled" || true
  echo "Moved qmd to $QUARANTINE_DIR/qmd.disabled"
  # hermes skills opt-out qmd || true
fi