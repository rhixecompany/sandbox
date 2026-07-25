# Check Handle

## Overview

This skill wraps a script in `~/AppData/Local/hermes/scripts/` for PowerShell script checking process handles for Hermes.

## Script Purpose

The script PowerShell script checking process handles for Hermes within the Hermes ecosystem.

## Usage

```bash
# For Python scripts
python $LOCALAPPDATA/hermes/scripts/check_handle.py [options]

# For Node.js/CJS scripts  
node $LOCALAPPDATA/hermes/scripts/check_handle.cjs [options]

# For PowerShell scripts
pwsh -File $LOCALAPPDATA/hermes/scripts/check_handle.ps1 [options]

# For Bash scripts
bash $LOCALAPPDATA/hermes/scripts/check_handle.sh [options]
```

## Typical Output

The script produces reports, audit findings, or transformation results that can be reviewed for quality assurance.