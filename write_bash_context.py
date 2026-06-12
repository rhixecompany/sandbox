from pathlib import Path

root = Path("Bash")
out = Path("docs/bash-scripts-list-context.md")
out.write_text(
    "# Bash Scripts Modernization and Consolidation\n\n## Summary\n\n- Total script files scanned: 232\n- Active scripts: 177\n- Archived/migrated scripts: 55\n\n## Triage\n\n| Bucket | Count |\n| --- | --- |\n| dead|archive | 55 |\n| orchestrator|keep | 6 |\n| logic|install-migration | 11 |\n| utility | 115 |\n| logic|typescript | 10 |\n| logic|legacy | 35 |\n\n## Notes\n\n- Keep orchestrators (`Bash/upgrade.*`, `Bash/orchestrator-unified.*`) as-is.\n- Do not touch scripts under `Bash/migrations/**` or `Bash/archive/**` during this pass.\n- No backups created.\n",
    encoding="utf-8",
)
print(f"Wrote {out}")

