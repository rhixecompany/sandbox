import os

sandbox_root = r"C:/Users/Alexa/Desktop/SandBox"
projects_root = os.path.join(sandbox_root, "projects")

# Project stack mapping based on AGENTS.md analysis
project_stacks = {
    "Banking": {"stack": "Next.js", "commands": "npm run dev, npm run build, npm run lint"},
    "comicwise": {"stack": "Next.js", "commands": "npm run dev, npm run build"},
    "cookiecutter-django-tailwind": {"stack": "Django", "commands": "python manage.py runserver, pytest"},
    "Django-Scrapy-Selenium": {"stack": "Django", "commands": "python manage.py runserver, scrapy crawl"},
    "ecom": {"stack": "Dual-stack (Django + React)", "commands": "python manage.py runserver, npm start"},
    "profile": {"stack": "Unknown", "commands": "TBD"},
    "Python-projects": {"stack": "Python", "commands": "python script.py, ruff check"},
    "rhixe_scans": {"stack": "Next.js", "commands": "npm run dev, npx prisma migrate dev"},
    "rhixecompany-comics": {"stack": "Dual-stack (Django + Next.js)", "commands": "python manage.py runserver, npm run dev"},
    "selenium_webdriver": {"stack": "Node.js", "commands": "npm start, npm test"},
    "university-libary-jsm": {"stack": "Next.js", "commands": "npm run dev, npm run build"},
    "xamehi": {"stack": "Django", "commands": "python manage.py runserver"},
    "xamehi.tv": {"stack": "Django", "commands": "python manage.py runserver"},
    "youtube-downloader": {"stack": "Unknown", "commands": "TBD"},
    "Bash": {"stack": "Bun/TypeScript", "commands": "bun run, bun test"},
    "Resume_maker": {"stack": "Bun/TypeScript", "commands": "bun index.ts"},
    "docs": {"stack": "Documentation", "commands": "N/A"}
}

# Update AGENTS.md files
for name, info in project_stacks.items():
    if name in ["Bash", "Resume_maker", "docs"]:
        agents_path = os.path.join(sandbox_root, name, "AGENTS.md")
    else:
        agents_path = os.path.join(projects_root, name, "AGENTS.md")
    
    if not os.path.exists(agents_path):
        continue
    
    with open(agents_path) as f:
        content = f.read()
    
    # Check if Architecture section already exists
    if "## Architecture" not in content:
        # Add Architecture section after the main header
        arch_doc = f"../docs/Project_Architecture/{name.replace('-', '_')}_architecture.md"
        folders_doc = f"../docs/Project_Architecture/{name.replace('-', '_')}_folders.md"
        tech_doc = f"../docs/Project_Architecture/{name.replace('-', '_')}_techstack.md"
        
        arch_section = f"""
## Architecture

- **Blueprint**: [{name} Architecture]({arch_doc})
- **Folders**: [{name} Folder Structure]({folders_doc})
- **Tech Stack**: [{name} Technology Stack]({tech_doc})
- **Stack Type**: {info['stack']}
"""
        
        # Insert after first header
        lines = content.split("\n", 1)
        if len(lines) > 1:
            new_content = lines[0] + arch_section + "\n" + lines[1]
            with open(agents_path, "w") as f:
                f.write(new_content)
            print(f"✓ Updated {name} AGENTS.md")

print("\nDone updating AGENTS.md files with architecture references")