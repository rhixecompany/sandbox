# Recovery Procedures by Language

Commands to restore dependencies after cleanup operations.

## Node.js / npm

**Restore node_modules after deletion:**
```bash
cd ~/path/to/project
npm install
```

**Restore with specific lock file (npm 7+):**
```bash
npm ci  # Uses package-lock.json for exact versions
```

**Clear npm cache if rebuild fails:**
```bash
npm cache clean --force
npm install
```

**Check what will be installed:**
```bash
npm list  # Before install
npm list > deps-before.txt
npm install
npm list > deps-after.txt
diff deps-before.txt deps-after.txt
```

---

## Python / venv

**Restore virtual environment:**
```bash
cd ~/path/to/project
python -m venv venv

# Activate venv
source venv/Scripts/activate  # Linux/Mac
.\venv\Scripts\Activate.ps1   # PowerShell
venv\Scripts\activate.bat     # CMD

# Install dependencies
pip install -r requirements.txt
```

**If pip packages were cached:**
```bash
pip install --no-cache-dir -r requirements.txt  # Force fresh download
```

**Check what will be installed:**
```bash
pip freeze > installed-before.txt
pip install -r requirements.txt
pip freeze > installed-after.txt
diff installed-before.txt installed-after.txt
```

---

## .NET / dotnet

**Restore NuGet packages after deletion:**
```bash
cd ~/path/to/project
dotnet restore           # Restore packages
dotnet build             # Rebuild bin/obj
```

**Clean and rebuild from scratch:**
```bash
dotnet clean
dotnet build
```

**Check project dependencies:**
```bash
dotnet list package
```

---

## Java / Maven

**Restore Maven cache after deletion:**
```bash
cd ~/path/to/project
mvn clean install
```

**If build fails, clean and retry:**
```bash
mvn clean
mvn install
```

**Remove only specific artifact:**
```bash
mvn dependency:purge-local-repository
```

---

## Java / Gradle

**Restore Gradle cache after deletion:**
```bash
cd ~/path/to/project
gradle clean build
```

**Clear specific Gradle caches:**
```bash
gradle cleanBuildCache
gradle build
```

---

## Go / go modules

**Restore Go packages after deletion:**
```bash
cd ~/path/to/project
go mod download
go build ./...
```

**Clear Go cache if needed:**
```bash
go clean -cache
go mod download
```

---

## Ruby / Bundler

**Restore gems after deletion:**
```bash
cd ~/path/to/project
bundle install
```

**Restore from Gemfile.lock (exact versions):**
```bash
bundle install --frozen  # Requires Gemfile.lock
```

---

## Docker

**Rebuild Docker images after cache clear:**
```bash
# Remove all dangling images
docker system prune

# Rebuild specific image (triggers cache rebuild)
docker build -t myimage:latest .

# Rebuild without cache
docker build --no-cache -t myimage:latest .
```

---

## Caches (Auto-Regenerating, No Action Needed)

These caches regenerate automatically on next use — no recovery command needed:

| Cache | Regenerates On |
|-------|----------------|
| NPM cache | `npm install` |
| Bun cache | Any `bun` command |
| PNPM cache | `pnpm install` |
| Docker buildkit | Next `docker build` |
| Temp folder | Windows system operations |
| VS Code cache | VS Code restart |
| Git LFS cache | Next `git lfs` operation |
| DNS cache | Next network lookup |

---

## Pre/Post Verification Pattern

**Before cleanup:**
```bash
# Snapshot what's installed
npm list > before-deps.txt
pip freeze > before-pip.txt
dotnet list package > before-nuget.txt
ls -lah node_modules > before-node-size.txt
```

**After recovery:**
```bash
# Verify it matches
npm list > after-deps.txt
diff before-deps.txt after-deps.txt  # Should be identical

pip freeze > after-pip.txt
diff before-pip.txt after-pip.txt    # Should be identical

# Check size is similar
ls -lah node_modules > after-node-size.txt
```

---

## Bulk Recovery (Multi-Project)

For systems with multiple projects that all lost dependencies:

```bash
#!/bin/bash
projects=("Project1" "Project2" "Project3")

for proj in "${projects[@]}"; do
  echo "Restoring $proj..."
  cd ~/$proj
  
  if [ -f package.json ]; then
    echo "  → npm install"
    npm ci
  fi
  
  if [ -f requirements.txt ]; then
    echo "  → pip install"
    python -m venv venv
    source venv/Scripts/activate
    pip install -r requirements.txt
  fi
  
  if [ -f .sln ] || [ -f *.csproj ]; then
    echo "  → dotnet restore"
    dotnet restore
    dotnet build
  fi
  
  cd ..
done

echo "All projects recovered."
```
