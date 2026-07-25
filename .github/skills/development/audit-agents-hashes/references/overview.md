# Audit Agents Hashes

## Overview

This skill wraps a script in `~/AppData/Local/hermes/scripts/` for PowerShell script finding duplicate AGENTS.md files.

## Script Purpose

The script PowerShell script finding duplicate AGENTS.md files within the Hermes ecosystem.

## Usage

```bash
# For Python scripts
python $LOCALAPPDATA/hermes/scripts/audit_agents_hashes.py [options]

# For Node.js/CJS scripts  
node $LOCALAPPDATA/hermes/scripts/audit_agents_hashes.cjs [options]

# For PowerShell scripts
pwsh -File $LOCALAPPDATA/hermes/scripts/audit_agents_hashes.ps1 [options]

# For Bash scripts
bash $LOCALAPPDATA/hermes/scripts/audit_agents_hashes.sh [options]
```

## Typical Output

The script produces reports, audit findings, or transformation results that can be reviewed for quality assurance.