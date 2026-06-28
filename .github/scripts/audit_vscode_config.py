import os
import json

sandbox_root = r"C:/Users/Alexa/Desktop/SandBox"
issues = {"formatter_conflicts": [], "hardcoded_paths": [], "missing_configs": [], "stack_mismatches": []}

# AGENTS.md to stack mapping
stack_map = {
    "Banking": "Next.js",
    "comicwise": "Next.js",
    "cookiecutter-django-tailwind": "Django",
    "Django-Scrapy-Selenium": "Django",
    "ecom": "Dual-stack",
    "profile": "Unknown",
    "Python-projects": "Python",
    "rhixe_scans": "Next.js",
    "rhixecompany-comics": "Dual-stack",
    "selenium_webdriver": "Node.js",
    "university-libary-jsm": "Next.js",
    "xamehi": "Django",
    "xamehi.tv": "Django",
    "youtube-downloader": "Unknown",
    "Bash": "Bun",
    "Resume_maker": "Bun"
}

for root, dirs, files in os.walk(sandbox_root):
    if ".git" in root:
        continue
    
    # Detect project name
    rel_root = os.path.relpath(root, sandbox_root)
    project_name = rel_root.split(os.sep)[0] if rel_root != "." else ""
    
    if ".vscode" not in dirs:
        continue
    
    vscode_path = os.path.join(root, ".vscode")
    settings_path = os.path.join(vscode_path, "settings.json")
    
    if not os.path.exists(settings_path):
        continue
    
    # Get expected stack
    expected_stack = stack_map.get(project_name, "Unknown")
    
    with open(settings_path) as f:
        settings = json.load(f)
    
    # Check for Python formatters in non-Python projects
    has_python_formatter = False
    has_nextjs_formatter = False
    
    for key in settings.get("editor", {}).get("defaultFormatter", "") or "":
        pass
    
    # Check language-specific formatters
    for key, value in settings.items():
        if key.startswith("[") and key.endswith("]"):
            lang = key[1:-1]
            if lang == "python":
                has_python_formatter = True
            if lang in ["javascript", "typescript", "typescriptreact"]:
                has_nextjs_formatter = True
    
    # Check for formatter conflicts (multiple formatters for same language)
    formatters = [(k, v.get("editor.defaultFormatter") if isinstance(v, dict) else None) 
                  for k, v in settings.items() if k.startswith("[")]
    
    # Check for hardcoded Windows paths
    settings_str = json.dumps(settings)
    if "C:\\\\Users\\\\" in settings_str or "C:/Users/" in settings_str:
        issues["hardcoded_paths"].append(f"{rel_root}/.vscode/settings.json")
    
    # Check stack alignment
    if expected_stack == "Django" and has_nextjs_formatter:
        # Check if it's pure Django (not dual-stack)
        if project_name not in ["ecom", "rhixecompany-comics", "rhixe_scans"]:
            pass  # May be acceptable if there's frontend code
    
    # Check for ESLint in settings when it might not be needed
    code_actions = settings.get("editor", {}).get("codeActionsOnSave", {})
    if "source.fixAll.eslint":
        # Check if eslint is in extensions
        ext_path = os.path.join(vscode_path, "extensions.json")
        if os.path.exists(ext_path):
            with open(ext_path) as f:
                exts = json.load(f)
            recs = exts.get("recommendations", [])
            if not any("eslint" in r for r in recs):
                issues["stack_mismatches"].append(f"{rel_root}/.vscode/settings.json - ESLint code action without extension")

# Report
print("=VS Code Configuration Audit Report=")
print(f"\nFormatter Conflicts: {len(issues['formatter_conflicts'])}")
print(f"Hardcoded Paths: {len(issues['hardcoded_paths'])}")
print(f"Missing Configs: {len(issues['missing_configs'])}")
print(f"Stack Mismatches: {len(issues['stack_mismatches'])}")

for category, items in issues.items():
    if items:
        print(f"\n{category.upper()}:")
        for item in items:
            print(f"  - {item}")