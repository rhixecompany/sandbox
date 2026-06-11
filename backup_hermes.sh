#!/usr/bin/env bash
set -euo pipefail

TIMESTAMP="2026-06-11_173000"
BACKUP_ROOT="backup.hermes/${TIMESTAMP}"
HERMES_DATA="$HOME/AppData/Local/hermes"
HERMES_SKILLS="$HOME/AppData/Local/hermes/skills"

mkdir -p "${BACKUP_ROOT}/hooks"
mkdir -p "${BACKUP_ROOT}/plugins"
mkdir -p "${BACKUP_ROOT}/skills"

# Backup hooks
cp -r "${HERMES_DATA}/hooks/"* "${BACKUP_ROOT}/hooks/" 2>/dev/null || true

# Backup plugins directory
cp -r "${HERMES_DATA}/plugins/"* "${BACKUP_ROOT}/plugins/" 2>/dev/null || true

# Backup skills (installed skills)
cp -r "${HERMES_SKILLS}/"* "${BACKUP_ROOT}/skills/" 2>/dev/null || true

# Backup config.yaml
cp "${HERMES_DATA}/config.yaml" "${BACKUP_ROOT}/config.yaml"

# Create manifest
cat > "${BACKUP_ROOT}/manifest.json" <<MANIFEST_EOF
{
  "timestamp": "${TIMESTAMP}",
  "profile": "adminbot",
  "hermes_data": "${HERMES_DATA}",
  "hermes_skills": "${HERMES_SKILLS}",
  "hooks_count": $(find "${BACKUP_ROOT}/hooks" -mindepth 1 -maxdepth 1 -type d | wc -l),
  "plugins_count": $(find "${BACKUP_ROOT}/plugins" -mindepth 1 -maxdepth 1 -type d | wc -l),
  "skills_count": $(find "${BACKUP_ROOT}/skills" -mindepth 1 -maxdepth 1 -type d | wc -l),
  "config_yaml_backed_up": true
}
MANIFEST_EOF

echo "Backup complete: ${BACKUP_ROOT}"
cat "${BACKUP_ROOT}/manifest.json"
