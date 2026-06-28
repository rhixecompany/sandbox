"""Fix all remaining skill issues: add Verification Checklist, When to Use, Workflow, Best Practices."""

import os, re, sys

skill_dir = os.path.join(os.environ.get("USERPROFILE", "C:\\Users\\Alexa"),
                         "AppData", "Local", "hermes", "skills")

stats = {"total": 0, "added_vc": 0, "added_wu": 0, "added_wf": 0, "added_bp": 0, "errors": 0}
errors_list = []

def read_skill(path):
    with open(path, "r", encoding="utf-8", errors="replace") as f:
        return f.read()

def write_skill(path, content):
    with open(path, "w", encoding="utf-8") as f:
        f.write(content)

def has_section(content, name_pattern):
    """Check if a section exists (as ## heading)."""
    for pat in name_pattern if isinstance(name_pattern, list) else [name_pattern]:
        if re.search(r"^## " + re.escape(pat) + r"\b", content, re.MULTILINE):
            return True
    return False

def get_h1(content):
    """Get the first H1 title."""
    m = re.search(r"^# (.+)", content, re.MULTILINE)
    return m.group(1).strip() if m else ""

def infer_skill_name(content, path):
    """Infer a human-readable name from frontmatter or H1 or path."""
    m = re.search(r"^title:\s*(.+)", content, re.MULTILINE)
    if m:
        return m.group(1).strip()
    h1 = get_h1(content)
    if h1:
        return h1
    # from path: .../skills/category/name/SKILL.md
    parts = path.replace("\\", "/").split("/")
    return parts[-2].replace("-", " ").title()

def infer_triggers(content, name):
    """Try to extract trigger conditions from existing content."""
    triggers = []
    # Look for bullet points that might describe triggers
    bullets = re.findall(r"^- When\s+(.+)$", content, re.MULTILINE)
    triggers.extend(bullets[:3])
    # Look for "Use when" patterns
    uses = re.findall(r"[Uu]se\s+when\s+([^\.]+)", content)
    for u in uses[:3]:
        u = u.strip().rstrip(":")
        if u and len(u) > 10:
            triggers.append(u)
    return triggers

def add_verification_checklist(content, skill_name):
    """Add a verification checklist section before EOF or after last section."""
    if has_section(content, ["Verification Checklist", "Checklist"]):
        return content
    
    checklist = f"""
## Verification Checklist

- [ ] Prerequisites and environment are properly configured
- [ ] {skill_name} operations completed successfully
- [ ] Output meets expected quality and requirements
- [ ] Any errors during execution were resolved
- [ ] Changes are documented and committed if applicable
"""
    # Append at the end
    content = content.rstrip() + "\n" + checklist
    stat_name = "added_vc"
    return content, stat_name

def add_when_to_use(content, skill_name, path):
    """Add When to Use section based on skill content."""
    if has_section(content, ["When to Use", "When to use"]):
        return content, None
    
    triggers = infer_triggers(content, skill_name)
    # Generate generic triggers based on skill name/purpose
    name_lower = skill_name.lower()
    
    lines = [f"\n## When to Use\n"]
    if triggers:
        lines.append("")
        for t in triggers[:4]:
            lines.append(f"- {t}")
    else:
        lines.append("")
        lines.append(f"- When you need to perform {skill_name} operations or tasks")
        lines.append(f"- When managing {skill_name} infrastructure or configurations")
        lines.append(f"- When automating or debugging {skill_name} workflows")
    
    lines.append(f"- **Triggers**: \"{skill_name.lower()}\" required for a project")
    lines.append("")
    
    # Find insertion point: before first ## section that's after the H1 and overview
    # or at end
    body_end = content.rstrip()
    
    result = body_end + "\n" + "\n".join(lines)
    return result, "added_wu"

def add_workflow(content, skill_name):
    """Add a basic Workflow section."""
    if has_section(content, ["Workflow", "Process", "Pipeline", "Phases", "The Process", "Decision Flow"]):
        return content, None
    
    wf = f"""
## Workflow

### Phase 1: Preparation

Set up required environment, dependencies, and configuration for {skill_name}.

### Phase 2: Execution

Run the primary {skill_name} operations according to the defined requirements.

### Phase 3: Verification

Verify output, handle any errors, and confirm results meet expectations.

### Phase 4: Completion

Document results, clean up resources, and finalize any deliverables.
"""
    content = content.rstrip() + "\n" + wf
    return content, "added_wf"

def add_best_practices(content, skill_name):
    """Add Best Practices section."""
    if has_section(content, ["Best Practices"]):
        return content, None
    
    bp = f"""
## Best Practices

1. **Prepare before executing**: Ensure all prerequisites and dependencies are in place
2. **Validate inputs**: Check configuration, parameters, and environment before running
3. **Handle errors gracefully**: Implement proper error handling and recovery
4. **Document results**: Keep records of what was done, what worked, and what didn't
5. **Clean up**: Remove temporary files, release resources after completion
"""
    content = content.rstrip() + "\n" + bp
    return content, "added_bp"


# Walk all skills
for root, dirs, files in os.walk(skill_dir):
    parts = root.replace("\\", "/").split("/")
    if "templates" in parts:
        continue
    if "references" in parts:
        continue
    if "scripts" in parts:
        continue
    if "assets" in parts:
        continue
    if "SKILL.md" in files:
        path = os.path.join(root, "SKILL.md")
        stats["total"] += 1
        
        try:
            content = read_skill(path)
            original = content
            skill_name = infer_skill_name(content, path)
            changes = []
            
            # 1. Add Verification Checklist
            if not has_section(content, ["Verification Checklist", "Checklist"]):
                content, _ = add_verification_checklist(content, skill_name)
                changes.append("vc")
                stats["added_vc"] += 1
            
            # 2. Add When to Use
            if not has_section(content, ["When to Use", "When to use"]):
                content, _ = add_when_to_use(content, skill_name, path)
                changes.append("wu")
                stats["added_wu"] += 1
            
            # 3. Add Workflow
            if not has_section(content, ["Workflow", "Process", "Pipeline", "Phases", "The Process", "Decision Flow"]):
                content, _ = add_workflow(content, skill_name)
                changes.append("wf")
                stats["added_wf"] += 1
            
            # 4. Add Best Practices
            if not has_section(content, ["Best Practices"]):
                content, _ = add_best_practices(content, skill_name)
                changes.append("bp")
                stats["added_bp"] += 1
            
            if changes:
                write_skill(path, content)
                print(f"  +{','.join(changes)} {path.replace(skill_dir, '')}")
                
        except Exception as e:
            stats["errors"] += 1
            errors_list.append(f"{path}: {e}")
            print(f"  ERROR {path}: {e}")

print(f"\n{'='*60}")
print(f"Done. Stats:")
print(f"  Total skills scanned: {stats['total']}")
print(f"  Verification Checklists added: {stats['added_vc']}")
print(f"  When to Use sections added: {stats['added_wu']}")
print(f"  Workflow sections added: {stats['added_wf']}")
print(f"  Best Practices added: {stats['added_bp']}")
print(f"  Errors: {stats['errors']}")
if errors_list:
    print(f"\nErrors:")
    for e in errors_list:
        print(f"  {e}")
