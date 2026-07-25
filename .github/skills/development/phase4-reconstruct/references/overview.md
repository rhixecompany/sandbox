# Phase4 Reconstruct

## Overview

This skill wraps a script in `~/AppData/Local/hermes/scripts/` for Node.js CJS script checking existence and size of target files.

## Script Purpose

The script Node.js CJS script checking existence and size of target files within the Hermes ecosystem.

## Usage

```bash
# For Python scripts
python $LOCALAPPDATA/hermes/scripts/phase4_reconstruct.py [options]

# For Node.js/CJS scripts  
node $LOCALAPPDATA/hermes/scripts/phase4_reconstruct.cjs [options]

# For PowerShell scripts
pwsh -File $LOCALAPPDATA/hermes/scripts/phase4_reconstruct.ps1 [options]

# For Bash scripts
bash $LOCALAPPDATA/hermes/scripts/phase4_reconstruct.sh [options]
```

## Typical Output

The script produces reports, audit findings, or transformation results that can be reviewed for quality assurance.