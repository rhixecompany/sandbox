# List Cli Tools

## Overview

This skill wraps a script in `~/AppData/Local/hermes/scripts/` for Bash script enumerating non-system executables.

## Script Purpose

The script Bash script enumerating non-system executables within the Hermes ecosystem.

## Usage

```bash
# For Python scripts
python $LOCALAPPDATA/hermes/scripts/list_cli_tools.py [options]

# For Node.js/CJS scripts  
node $LOCALAPPDATA/hermes/scripts/list_cli_tools.cjs [options]

# For PowerShell scripts
pwsh -File $LOCALAPPDATA/hermes/scripts/list_cli_tools.ps1 [options]

# For Bash scripts
bash $LOCALAPPDATA/hermes/scripts/list_cli_tools.sh [options]
```

## Typical Output

The script produces reports, audit findings, or transformation results that can be reviewed for quality assurance.