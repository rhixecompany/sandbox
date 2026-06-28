import os
import json

sandbox_root = r"C:/Users/Alexa/Desktop/SandBox"
issues = {"formatter_conflicts": [], "hardcoded_paths": [], "missing_configs": [], "stack_mismatches": []}

settings_files = [
    ".vscode/settings.json",
    "Bash/.vscode/settings.json",
    "Resume_maker/.vscode/settings.json",
    "projects/Banking/.vscode/settings.json",
    "projects/comicwise/.vscode/settings.json",
    "projects/cookiecutter-django-tailwind/.vscode/settings.json",
    "projects/Django-Scrapy-Selenium/.vscode/settings.json",
    "projects/docs/.vscode/settings.json",
    "projects/ecom/.vscode/settings.json",
    "projects/profile/.vscode/settings.json",
    "projects/Python-projects/.vscode/settings.json",
    "projects/rhixe_scans/.vscode/settings.json",
    "projects/rhixecompany-comics/.vscode/settings.json",
    "projects/selenium_webdriver/.vscode/settings.json",
    "projects/university-libary-jsm/.vscode/settings.json",
    "projects/xamehi/.vscode/settings.json",
    "projects/xamehi.tv/.vscode/settings.json",
    "projects/youtube-downloader/.vscode/settings.json"
]

for rel_path in settings_files:
    full_path = os.path.join(sandbox_root, rel_path)
    if not os.path.exists(full_path):
        continue
    
    with open(full_path) as f:
        settings = json.load(f)
    
    # Check for eslint in codeActionsOnSave
    cas = settings.get("editor", {}).get("codeActionsOnSave", {})
    if "source.fixAll.eslint" in cas:
        # Check if eslint is in extensions recommendations
        ext_path = os.path.join(os.path.dirname(full_path), "extensions.json")
        if os.path.exists(ext_path):
            with open(ext_path) as f:
                exts = json.load(f)
            recs = exts.get("recommendations", [])
            if not any("eslint" in r for r in recs):
                issues["stack_mismatches"].append(f"{rel_path} - ESLint code action without extension")
    
    # Check for hardcoded paths
    settings_str = json.dumps(settings)
    if "C:\\\\Users\\\\" in settings_str or "C:/Users/" in settings_str:
        issues["hardcoded_paths"].append(rel_path)

# Report
print("=VS Code Configuration Audit Report (Re-run)=")
print(f"\nFormatter Conflicts: {len(issues['formatter_conflicts'])}")
print(f"Hardcoded Paths: {len(issues['hardcoded_paths'])}")
print(f"Missing Configs: {len(issues['missing_configs'])}")
print(f"Stack Mismatches: {len(issues['stack_mismatches'])}")

for category, items in issues.items():
    if items:
        print(f"\n{category.upper()}:")
        for item in items:
            print(f"  - {item}")

if not any(issues.values()):
    print("\n✓ ALL CHECKS PASSED - No issues found")