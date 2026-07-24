# Methodology

> Extracted from `repo-story-time.prompt.md`.

## Methodology

### Phase 1: Repository Exploration

**EXECUTE these commands immediately** to understand the repository structure and purpose:

1. Get repository overview by running: `Get-ChildItem -Recurse -Include "*.md","*.json","*.yaml","*.yml" | Select-Object -First 20 | Select-Object Name, DirectoryName`

2. Understand project structure by running: `Get-ChildItem -Recurse -Directory | Where-Object {$_.Name -notmatch "(node_modules|\.git|bin|obj)"} | Select-Object -First 30 | Format-Table Name, FullName`

After executing these commands, use semantic search to understand key concepts and technologies. Look for:

- Configuration files (package.json, pom.xml, requirements.txt, etc.)
- README files and documentation
- Main source directories
- Test directories
- Build/deployment configurations

### Phase 2: Technical Deep Dive

Create comprehensive technical inventory:

- **Purpose**: What problem does this repository solve?
- **Architecture**: How is the code organized?
- **Technologies**: What languages, frameworks, and tools are used?
- **Key Components**: What are the main modules/services/features?
- **Data Flow**: How does information move through the system?

### Phase 3: Commit History Analysis

**EXECUTE these git commands systematically** to understand repository evolution:

**Step 1: Basic Statistics** - Run these commands to get repository metrics:

- `git rev-list --all --count` (total commit count)
- `(git log --oneline --since="1 year ago").Count` (commits in last year)

**Step 2: Contributor Analysis** - Run this command:

- `git shortlog -sn --since="1 year ago" | Select-Object -First 20`

**Step 3: Activity Patterns** - Run this command:

- `git log --since="1 year ago" --format="%ai" | ForEach-Object { $_.Substring(0,7) } | Group-Object | Sort-Object Count -Descending | Select-Object -First 12`

**Step 4: Change Pattern Analysis** - Run these commands:

- `git log --since="1 year ago" --oneline --grep="feat|fix|update|add|remove" | Select-Object -First 50`
- `git log --since="1 year ago" --name-only --oneline | Where-Object { $_ -notmatch "^[a-f0-9]" } | Group-Object | Sort-Object Count -Descending | Select-Object -First 20`

**Step 5: Collaboration Patterns** - Run this command:

- `git log --since="1 year ago" --merges --oneline | Select-Object -First 20`

**Step 6: Seasonal Analysis** - Run this command:

- `git log --since="1 year ago" --format="%ai" | ForEach-Object { $_.Substring(5,2) } | Group-Object | Sort-Object Name`

**Important**: Execute each command and analyze the output before proceeding to the next step. **Important**: Use your best judgment to execute additional commands not listed above based on the output of previous commands or the repository's specific content.

### Phase 4: Pattern Recognition

Look for these narrative elements:

- **Characters**: Who are the main contributors? What are their specialties?
- **Seasons**: Are there patterns by month/quarter? Holiday effects?
- **Themes**: What types of changes dominate? (features, fixes, refactoring)
- **Conflicts**: Are there areas of frequent change or contention?
- **Evolution**: How has the repository grown and changed over time?
