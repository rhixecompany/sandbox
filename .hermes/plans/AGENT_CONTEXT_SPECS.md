# Agent Context Files + VS Code Configurator Specifications

## Acceptance Criteria

### Phase 1: Agent Context Files (18 locations)

| Location | Blueprint Type | Required Fields |
|----------|---------------|-----------------|
| SandBox root | Architecture, Folder, Stack | Purpose, Stack, Conventions, Commands |
| Bash/ | Architecture, Folder, Stack | Toolkit, Conventions, Commands |
| Resume_maker/ | Architecture, Folder, Stack | Entry, Commands, Notes |
| projects/Banking/ | Architecture, Folder, Stack | Stack, Commands, Notes |
| projects/comicwise/ | Architecture, Folder, Stack | Stack, Commands |
| projects/cookiecutter-django-tailwind/ | Architecture, Folder, Stack | Stack, Commands, Notes |
| projects/Django-Scrapy-Selenium/ | Architecture, Folder, Stack | Stack, Commands, Notes |
| projects/ecom/ | Architecture, Folder, Stack | Stack, Commands |
| projects/profile/ | Architecture, Folder, Stack | Stack, Commands |
| projects/Python-projects/ | Architecture, Folder, Stack | Conventions, Commands |
| projects/rhixe_scans/ | Architecture, Folder, Stack | Stack, Notes |
| projects/rhixecompany-comics/ | Architecture, Folder, Stack | Stack, Commands, Notes |
| projects/selenium_webdriver/ | Architecture, Folder, Stack | Stack, Notes |
| projects/university-libary-jsm/ | Architecture, Folder, Stack | Stack, Notes |
| projects/xamehi/ | Architecture, Folder, Stack | Notes |
| projects/xamehi.tv/ | Architecture, Folder, Stack | Notes |
| projects/youtube-downloader/ | Architecture, Folder, Stack | Stack, Notes |
| projects/docs/ | Architecture, Folder, Stack | Purpose, Structure |

### Phase 2: VS Code Configuration (17 .vscode folders)

| Check | Requirement |
|-------|-------------|
| JSON validity | All files parse without errors (python -c "import json; json.load(open(file))") |
| Formatter conflicts | One formatter per language per settings.json |
| Path variables | No hardcoded Windows paths; use ${workspaceFolder} |
| Extension recommendations | Match project stack; no github.copilot |
| JS comments | None in extensions.json, launch.json, tasks.json |
| Stack alignment | Each .vscode/ matches project's detected tech stack |

### Phase 2 Verification Commands

```bash
# Validate all JSON files
for f in $(find . -name "*.json" -path "*/.vscode/*"); do
  python3 -c "import json; json.load(open('$f'))" && echo "✓ $f"
done
```