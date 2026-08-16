# Obsidian Integration

## Desktop Integration
The wiki directory works as an Obsidian vault out of the box:
- [[wikilinks]] render as clickable links
- Graph View visualizes the knowledge network
- YAML frontmatter powers Dataview queries

## Headless Sync (servers)
On machines without a display, use obsidian-headless:
```bash
# Requires Node.js 22+
npm install -g obsidian-headless
ob login --email <email> --password '<password>'
ob sync-create-remote --name "LLM Wiki"
cd ~/wiki
ob sync-setup --vault "<vault-id>"
ob sync
```

## Continuous Sync via systemd
Create service file and enable with systemctl.
