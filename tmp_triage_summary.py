from pathlib import Path
from collections import Counter

root = Path("Bash")
buckets = Counter()
for pattern in ["**/*.sh", "**/*.ps1", "**/*.bat", "**/*.ts"]:
    for p in root.glob(pattern):
        rel = str(p.relative_to(root)).lower()
        if "archive" in rel or "retired" in rel or "migrations" in rel:
            buckets["dead|archive"] += 1
            continue
        name = p.name.lower()
        ext = p.suffix.lower()
        if name in {"upgrade.sh", "upgrade.ps1", "upgrade.bat", "orchestrator-unified.sh", "orchestrator-unified.ps1", "orchestrator-unified.bat"}:
            buckets["orchestrator|keep"] += 1
        elif "banking/install" in rel or "install/" in rel or "ecom/install" in rel or "rhixe_scans/install_" in rel or "scripts/phase-5-verify-install" in rel:
            buckets["logic|install-migration"] += 1
        elif "banking/scripts" in rel or "comicwise" in rel or "scripts/" in rel and ext in {".sh", ".ps1", ".bat"}:
            buckets["utility"] += 1
        elif ext == ".ts" and "src/" in rel:
            buckets["logic|typescript"] += 1
        else:
            buckets["utility"] += 1

for key, count in sorted(buckets.items()):
    print(f"{key}: {count}")
