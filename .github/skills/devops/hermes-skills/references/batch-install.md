# Batch Skill Install Pattern

## Problem
You need to install many skills from the Hermes hub at once (e.g., all 94 official optional skills).

## Solution: Bash Loop with `--yes`

```bash
#!/bin/bash
SKILLS=(
  "official/security/1password"
  "official/finance/3-statement-model"
  "official/dogfood/adversarial-ux-test"
  # ... add all identifiers
)

OK=0
FAIL=0
FAIL_LIST=""

for skill in "${SKILLS[@]}"; do
  echo "=== [$((OK+FAIL+1))/${#SKILLS[@]}] Installing: $skill ==="
  if hermes skills install "$skill" --yes 2>&1; then
    OK=$((OK+1))
  else
    FAIL=$((FAIL+1))
    FAIL_LIST="$FAIL_LIST $skill"
    echo "FAILED: $skill"
  fi
  echo ""
done

echo "========================================="
echo "DONE: $OK installed, $FAIL failed"
if [ -n "$FAIL_LIST" ]; then
  echo "Failed skills:$FAIL_LIST"
fi
```

## Getting the Full Identifier List

The `hermes skills browse --source official` table truncates identifiers. To get full identifiers:

1. **Use `hermes skills inspect`** to verify a specific identifier:
   ```bash
   hermes skills inspect "official/security/1password"
   ```

2. **The pattern is:** `official/<category>/<skill-name>` where category matches the skill's domain (security, finance, mlops, creative, etc.)

3. **Python parsing script** to extract identifiers from browse output:
   ```python
   import subprocess, re
   all_skills = {}
   for page in [1, 2]:
       raw = subprocess.run(
           ["hermes", "skills", "browse", "--size", "50", "--page", str(page), "--source", "official"],
           capture_output=True, text=True, timeout=30
       ).stdout
       for line in raw.split('\n'):
           # Match identifier pattern like "official/security\1password"
           m = re.search(r'(official/\S+)', line)
           if m:
               identifier = m.group(1).strip()
               parts = identifier.replace('\\', '/').split('/')
               if len(parts) == 3:
                   all_skills[parts[2]] = identifier
   ```

## Timing

- Each install triggers a security scan: ~2-5 seconds per skill
- 94 skills ≈ 3-8 minutes total
- Run as background process for large batches

## Post-Install Verification

```bash
hermes skills list                    # Count total installed
hermes skills audit --deep            # Security re-scan all installed
```

See `references/audit-results.md` for understanding BLOCKED verdicts.
