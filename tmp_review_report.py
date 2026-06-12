from pathlib import Path
import json
import tempfile

root = Path("Bash")
out_path = Path("docs/bash-scripts-fix-prompt-review-report.md")
rows = []
for pattern in ["**/*.sh", "**/*.ps1", "**/*.bat", "**/*.ts"]:
    for p in root.glob(pattern):
        rel = str(p.relative_to(root))
        if "archive" in rel.lower() or "retired" in rel.lower():
            continue
        try:
            text = p.read_text(encoding="utf-8", errors="ignore")
        except Exception:
            text = ""
        lines = text.splitlines()
        nonzero = [ln for ln in lines if ln.strip()]
        issues = []
        if any(s in text for s in ["TODO:", "FIXME:", "HACK:"]):
            issues.append("todo_fixme_hack")
        if any(s in text.lower() for s in ["dead code", "deprecated", "no longer used", "legacy"]):
            issues.append("dead_code_marker")
        if any(s in text.lower() for s in ["backup", "do not delete", "do not create backup"]):
            issues.append("backup_related_text")
        if any(s in text for s in ["read -p", "read -r ", "Read-Host", "/P ", "set /p"]):
            issues.append("interactive_prompt")
        if not text.strip():
            issues.append("empty_file")
        if p.suffix.lower() == ".ts" and "export " not in text and "import " not in text:
            issues.append("ts_module_missing_exports")
        rows.append((rel, p.suffix.lstrip("."), len(nonzero), issues))

rows.sort(key=lambda item: item[0].lower())
out = [f"| File | Ext | Lines | Issues |"]
out += ["| --- | --- | --- | --- |"]
for rel, ext, line_count, issues in rows:
    marker = ", ".join(sorted(set(issues))) if issues else "—"
    # escape pipes themselves
    safe_rel = rel.replace("|", "/")
    out.append(f"| {safe_rel} | {ext} | {line_count} | {marker} |")

out_path.write_text("\n".join(out) + "\n", encoding="utf-8")
print(f"Wrote {out_path} with {len(rows)} files.")
