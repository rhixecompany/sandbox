import os
import json

sandbox_root = r"C:/Users/Alexa/Desktop/SandBox"

# All settings.json files to check
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

# Fix ESLint mismatch: remove source.fixAll.eslint from codeActionsOnSave
for rel_path in settings_files:
    full_path = os.path.join(sandbox_root, rel_path)
    if not os.path.exists(full_path):
        continue
    
    with open(full_path) as f:
        settings = json.load(f)
    
    # Check for eslint in codeActionsOnSave
    changed = False
    if "editor.codeActionsOnSave" in settings:
        if "source.fixAll.eslint" in settings["editor.codeActionsOnSave"]:
            del settings["editor.codeActionsOnSave"]["source.fixAll.eslint"]
            changed = True
    
    # Check for eslint in other locations (like source.addMissingImports might have eslint variant)
    if "codeActionsOnSave" in settings:
        if "source.fixAll.eslint" in settings["codeActionsOnSave"]:
            del settings["codeActionsOnSave"]["source.fixAll.eslint"]
            changed = True
    
    if changed:
        with open(full_path, "w") as f:
            json.dump(settings, f, indent=2)
        print(f"✓ Fixed {rel_path}")
    else:
        print(f"✓ OK {rel_path}")

print("\nDone checking ESLint configs")