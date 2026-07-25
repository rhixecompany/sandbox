# Inventory Agents

## Overview

This skill wraps a script in `~/AppData/Local/hermes/scripts/` for PowerShell script inventorying AGENTS.md files.

## Script Purpose

The script PowerShell script inventorying AGENTS.md files within the Hermes ecosystem.

## Usage

```bash
# For Python scripts
python $LOCALAPPDATA/hermes/scripts/inventory_agents.py [options]

# For Node.js/CJS scripts  
node $LOCALAPPDATA/hermes/scripts/inventory_agents.cjs [options]

# For PowerShell scripts
pwsh -File $LOCALAPPDATA/hermes/scripts/inventory_agents.ps1 [options]

# For Bash scripts
bash $LOCALAPPDATA/hermes/scripts/inventory_agents.sh [options]
```

## Typical Output

The script produces reports, audit findings, or transformation results that can be reviewed for quality assurance.