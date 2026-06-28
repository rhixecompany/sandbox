import os
import json

# Configuration
sandbox_root = r"C:/Users/Alexa/Desktop/SandBox"
projects_root = os.path.join(sandbox_root, "projects")
docs_dir = os.path.join(sandbox_root, "docs", "Project_Architecture")
os.makedirs(docs_dir, exist_ok=True)

targets = []

# Collect all targets
for d in os.listdir(projects_root):
    full_path = os.path.join(projects_root, d)
    if os.path.isdir(full_path):
        targets.append((d, full_path, f"projects/{d}"))

for d in ["Bash", "Resume_maker", "docs"]:
    full_path = os.path.join(sandbox_root, d)
    if os.path.isdir(full_path):
        targets.append((d, full_path, d))

# Analyze and generate
for name, path, rel_path in targets:
    stack = []
    has_django = False
    has_next = False
    
    # Check root package.json
    pkg_json = os.path.join(path, "package.json")
    if os.path.exists(pkg_json):
        try:
            with open(pkg_json) as f:
                pkg = json.load(f)
            deps = {**pkg.get("dependencies", {}), **pkg.get("devDependencies", {})}
            if "next" in deps:
                has_next = True
                stack.append("Next.js")
            if "react" in deps:
                stack.append("React")
            if "tailwindcss" in deps:
                stack.append("TailwindCSS")
            if "typescript" in deps:
                stack.append("TypeScript")
            if "bun" in deps or os.path.exists(os.path.join(path, "bun.lock")):
                stack.append("Bun")
        except:
            pass
    
    # Check for backend/frontend dual-stack
    backend_path = os.path.join(path, "backend")
    frontend_path = os.path.join(path, "frontend")
    
    if os.path.isdir(backend_path):
        # Check backend package.json
        be_pkg = os.path.join(backend_path, "package.json")
        if os.path.exists(be_pkg):
            try:
                with open(be_pkg) as f:
                    be_data = json.load(f)
                be_deps = {**be_data.get("dependencies", {}), **be_data.get("devDependencies", {})}
                if "django" in be_deps or os.path.exists(os.path.join(backend_path, "manage.py")):
                    has_django = True
            except:
                pass
        if os.path.exists(os.path.join(backend_path, "manage.py")):
            has_django = True
    
    if os.path.isdir(frontend_path):
        fe_pkg = os.path.join(frontend_path, "package.json")
        if os.path.exists(fe_pkg):
            try:
                with open(fe_pkg) as f:
                    fe_data = json.load(f)
                fe_deps = {**fe_data.get("dependencies", {}), **fe_data.get("devDependencies", {})}
                if "next" in fe_deps:
                    has_next = True
            except:
                pass
    
    # Determine final stack
    if has_django and has_next:
        stack = ["Dual-stack (Django + Next.js)"]
    elif has_django:
        stack = ["Django", "Python"]
    elif has_next:
        stack = ["Next.js", "React", "TypeScript"]
    
    # Check root-level Python files if no stack detected yet
    if not stack:
        req_txt = os.path.join(path, "requirements.txt")
        pyproject = os.path.join(path, "pyproject.toml")
        manage_py = os.path.join(path, "manage.py")
        
        if os.path.exists(manage_py):
            stack = ["Django", "Python"]
            has_django = True
        elif os.path.exists(req_txt) or os.path.exists(pyproject):
            stack = ["Python"]
        elif os.path.exists(pkg_json) and (os.path.exists(os.path.join(path, "bun.lock")) or "bun" in str(open(pkg_json).read())):
            stack = ["Bun", "TypeScript"]
        else:
            stack = ["Unknown"]
    
    # Generate architecture blueprint
    arch_path = os.path.join(docs_dir, f"{name.replace('-', '_')}_architecture.md")
    with open(arch_path, "w") as f:
        f.write(f"""# {name} Architecture Blueprint

## Overview
- **Project**: {name}
- **Path**: {rel_path}
- **Stack**: {', '.join(stack)}

## Layer Analysis
""")
        if "Next.js" in str(stack):
            f.write("- **Presentation**: Next.js/React frontend with App Router\n")
        elif "Django" in str(stack) and "Next.js" not in str(stack):
            f.write("- **Presentation**: Django templates + optional DRF API\n")
            f.write("- **Business Logic**: Django views, models, serializers\n")
            f.write("- **Data Layer**: Django ORM with PostgreSQL/SQLite\n")
        else:
            f.write("- **Stack**: Unknown — inspect code for architecture patterns\n")
        
        f.write(f"""
## Cross-Cutting Concerns
- **Auth**: {'NextAuth.js' if has_next else 'Django Auth' if has_django else 'N/A'}
- **Error Handling**: Stack-specific patterns
- **Logging**: Standard logging configuration
- **Configuration**: Environment variables via .env files

## Extension Points
- {'Django apps modular, Celery tasks' if has_django else 'TypeScript modules, component-based'}
""")
    
    # Generate folder structure blueprint
    folder_path = os.path.join(docs_dir, f"{name.replace('-', '_')}_folders.md")
    with open(folder_path, "w") as f:
        f.write(f"""# {name} Folder Structure

## Root: {rel_path}

### Key Directories
""")
        if has_django and has_next:
            f.write("- backend/ — Django/Python backend\n- frontend/ — Next.js frontend\n")
        elif has_next:
            f.write("- src/ — source code\n- public/ — static assets\n")
        elif has_django:
            f.write("- .vscode/ — VS Code configuration\n- src/ or app/ — Django apps\n")
        
        f.write("""- .vscode/ — VS Code configuration
- AGENTS.md — agent context
- .github/ — CI/workflow configs
""")
    
    # Generate tech stack blueprint
    tech_path = os.path.join(docs_dir, f"{name.replace('-', '_')}_techstack.md")
    with open(tech_path, "w") as f:
        f.write(f"""# {name} Technology Stack

## Core Technologies
| Technology | Version/Notes |
|------------|---------------|
""")
        for tech in stack[:3]:
            f.write(f"| {tech} | Detected from project files |\n")
        
        f.write(f"""
## Build & Test Commands
""")
        if has_next:
            f.write("```bash\nnpm run dev\nnpm run build\nnpm run lint\n```\n")
        if has_django:
            f.write("```bash\npython manage.py runserver\npython manage.py test\n```\n")
    
    print(f"✓ {name}: {', '.join(stack)}")

print(f"\nGenerated docs in: {docs_dir}")