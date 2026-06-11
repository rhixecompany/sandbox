# Quickstart Commands Reference

## Installation
```bash
# pip (simplest)
pip install hermes-agent
hermes postinstall

# Git installer (bleeding-edge)
curl -fsSL https://raw.githubusercontent.com/NousResearch/hermes-agent/main/scripts/install.sh | bash
source ~/.bashrc
```

## Provider Selection
```bash
hermes model                    # Interactive picker
hermes setup --portal          # Nous Portal (recommended)
```

## Verification
```bash
hermes chat                    # Test chat
hermes config show             # View current config
```

## Next Steps
```bash
hermes gateway setup           # Connect messenger
/hermes skills                 # Browse skills
/skill install                 # Install from hub
hermes memory setup            # Enable memory
hermes cron create "name" "schedule" "prompt"  # Schedule tasks
```

## Troubleshooting
```bash
hermes setup                   # Re-run setup
hermes model                   # Change provider
tail -f ~/.hermes/logs/hermes/*.log  # Check logs
rm -rf ~/.hermes && hermes setup     # Nuclear reset
```