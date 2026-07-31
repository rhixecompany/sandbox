#!/usr/bin/env python3
"""Comprehensive prompt enhancement v3. Appends missing sections safely to end of body. DRY via shared templates."""
import yaml, re, sys
from pathlib import Path
from collections import defaultdict

P = Path(r"C:\Users\Alexa\Desktop\SandBox\.github\prompts")
S = P / "templates" / "_shared"

def sect(heading, content):
    return f"## {heading}\n\n{content}\n"

S_PERSONAS = sect("Personas",
    "See [`templates/_shared/personas.md`](templates/_shared/personas.md) for shared persona templates.\n\n"
    "| Persona | When to Use |\n"
    "| ------- | ----------- |\n"
    "| **Developer** | Implementation, debugging, refactoring |\n"
    "| **Reviewer** | Code review, quality assurance |\n"
    "| **User** | General purpose, operations |")

S_PERSONALITY = sect("Personality",
    "See [`templates/_shared/personality.md`](templates/_shared/personality.md) for shared personality guidelines.\n\n"
    "- **Tone**: Direct, practical, actionable\n"
    "- **Style**: Structured with clear steps and verification\n"
    "- **Avoid**: Ambiguity, assumptions, scope creep\n"
    "- **Encourage**: Evidence-based decisions, minimal changes")

S_CONTEXT_TMPL = sect("Context", "{text}")

S_RULES = sect("Rules",
    "See core rules: [`templates/_shared/rules-core.md`](templates/_shared/rules-core.md)\n\n"
    "### Domain Rules\n\n{rules}\n\n"
    "### Standing Rules\n\n"
    "1. **Map before touch** — Understand before making changes.\n"
    "2. **Smallest safe change** — Minimal change that achieves the goal.\n"
    "3. **Verify before claim** — Test before reporting complete.\n"
    "4. **Report blockers** — State clearly when something fails.")

S_PHASES = sect("Phases",
    "### Phase 1: Intake\n"
    "- Read the request and identify scope.\n"
    "- Locate relevant files, diffs, references.\n\n"
    "### Phase 2: Execute\n"
    "- Perform work with smallest safe change set.\n"
    "- Keep steps explicit and reproducible.\n\n"
    "### Phase 3: Verify\n"
    "- Check result against goal, rules, inputs.\n"
    "- Confirm output is usable and complete.\n\n"
    "### Phase 4: Hand Off\n"
    "- Return final artifact or findings clearly.\n"
    "- Stop once the requested result is delivered.")

S_WORKFLOW_TMPL = sect("Workflow",
    "See [`templates/_shared/section-skeleton.md`](templates/_shared/section-skeleton.md) for workflow structure.\n\n"
    "{text}")

S_CHECKLIST = sect("Verification Checklist",
    "| # | Gate | Criterion |\n"
    "|---|------|-----------|\n"
    "| 1 | Scope | Change matches the original request |\n"
    "| 2 | Quality | Meets project standards |\n"
    "| 3 | Tests | Tests pass (if applicable) |\n"
    "| 4 | Regression | No unintended side effects |\n"
    "| 5 | Docs | Changes documented if needed |")

S_BEST = sect("Best Practices",
    "See [`templates/_shared/best-practices.md`](templates/_shared/best-practices.md) for cross-cutting best practices.\n\n"
    "1. **DRY** — Reference shared templates instead of duplicating content.\n"
    "2. **Structured output** — Use clear sections with consistent heading levels.\n"
    "3. **Verification gates** — Always verify before claiming completion.\n"
    "4. **Minimal changes** — Fix root cause, not symptoms.")

S_DEPS = sect("Dependencies",
    "See [`templates/_shared/deps-core.md`](templates/_shared/deps-core.md) for shared dependency patterns.")

S_SUBGOALS = sect("Subgoals",
    "1. **Prepare** — Understand requirements and prerequisites.\n"
    "2. **Execute** — Follow structured workflow with incremental progress.\n"
    "3. **Verify** — Confirm output meets requirements and standards.\n"
    "4. **Document** — Record results, decisions, and lessons learned.")

S_SKILLS = sect("Skills Required",
    "See [`templates/_shared/skills-table-core.md`](templates/_shared/skills-table-core.md) for shared skills table.\n\n"
    "| Skill | Purpose |\n"
    "|-------|---------|\n"
    "| `using-superpowers` | Foundational skill workflow |\n"
    "{skills_rows}| `executing-plans` | Execute plans step by step |\n"
    "| `verification-before-completion` | Validate before claiming done |")

S_SKILLS_ROWS = {
    "fix-sync": "| `systematic-debugging` | Root cause analysis and fix |\n| `git-patch-management` | Patch creation and management |\n",
    "code": "| `test-driven-development` | TDD workflow enforcement |\n| `code-review` | Code quality assurance |\n| `systematic-debugging` | Debugging and root cause analysis |\n",
    "research": "| `web-research-pipeline` | Structured web research |\n| `content-research-writer` | Research synthesis |\n| `repo-research-pipeline` | Multi-project research dispatching |\n",
    "general": "| `plans-and-specs` | Planning and decomposition |\n| `writing-plans` | Implementation plan authoring |\n",
}

S_MCP = sect("MCP Servers & Tools",
    "The following MCP servers and tools are available for this task. Use them in preference to native equivalents per MCP-first tooling policy.\n\n"
    "{mcp_rows}"
    "| `filesystem` | File read/write operations |\n"
    "| `sequential-thinking` | Structured reasoning for complex problems |\n"
    "| `fetch` | Web page content extraction |\n"
    "| `playwright` | Browser automation for interactive pages |\n"
    "| `github` | GitHub API operations |\n")

S_MCP_ROWS = {
    "fix-sync": "| `ast-grep` | AST-based code search and replace |\n",
    "code": "| `code-sandbox` | Isolated code execution and testing |\n| `ast-grep` | AST-based code search and replace |\n",
    "research": "| `tavily` | Web search and content extraction |\n| `firecrawl` | Website crawling and bulk extraction |\n",
    "general": "| `code-sandbox` | Isolated code execution |\n| `tavily` | Web search and extraction |\n",
}

S_TASKS = sect("Tasks",
    "- [ ] Understand requirements and scope\n"
    "- [ ] Plan approach and identify resources\n"
    "- [ ] Execute work incrementally\n"
    "- [ ] Verify against acceptance criteria\n"
    "- [ ] Document results and decisions\n")

S_GOAL_TMPL = sect("Goal", "{text}")

DOMAIN_RULES = {
    "fix-sync": "- Fix root causes, not symptoms.\n- Check siblings for the same flaw.\n- Restore from git clean before retrying.",
    "code": "- Read existing code before writing new code.\n- Match project conventions and style.\n- Add tests for new functionality.",
    "research": "- Verify sources before citing.\n- Extract to structured markdown.\n- Note confidence levels for findings.",
    "general": "- Follow prompt literally.\n- Prefer evidence from workspace.\n- Keep responses structured and actionable.",
}

CONTEXTS = {
    "fix-sync": "Use when fixing, repairing, or synchronizing files or configs. Diagnose first, apply minimal changes, verify each fix.",
    "code": "Use when implementing, modifying, or debugging code. Read the codebase first, understand patterns, then apply changes with tests.",
    "research": "Use when researching topics or synthesizing findings. Start with broad discovery, then narrow to specific sources.",
    "general": "Use for the task described in the Goal section. Follow structured workflow and verify results.",
}

WORKFLOWS = {
    "fix-sync": "1. **Diagnose** — Run diagnostics.\n2. **Plan** — Determine minimal changes.\n3. **Fix** — Apply changes incrementally.\n4. **Verify** — Confirm fix works.\n5. **Document** — Note what changed.",
    "code": "1. **Read** — Understand existing code.\n2. **Plan** — Design approach.\n3. **Implement** — Write code with tests.\n4. **Test** — Run all tests.\n5. **Review** — Check quality and edge cases.",
    "research": "1. **Discover** — Search broadly.\n2. **Extract** — Save findings.\n3. **Synthesize** — Connect insights.\n4. **Organize** — Index and cross-ref.\n5. **Present** — Deliver recommendations.",
    "general": "1. **Understand** — Read request, identify scope.\n2. **Plan** — Determine approach.\n3. **Execute** — Perform work step by step.\n4. **Verify** — Check against goal.\n5. **Deliver** — Present result.",
}

def categorize(name, desc, body):
    t = (name + " " + desc + " " + body).lower()
    if re.search(r"fix|repair|patch|sync|migrat|remediat|audit|cleanup", t): return "fix-sync"
    if re.search(r"code|program|implement|function|api|script|build", t): return "code"
    if re.search(r"research|investigat|search|find|analyz|review|document", t): return "research"
    return "general"

def parse_fm(text):
    m = re.match(r'^---\s*\n(.*?)\n(?:---|\.\.\.)', text, re.DOTALL)
    if not m: return None, text, None
    raw = m.group(1); body = text[m.end():].strip()
    try: return yaml.safe_load(raw), body, raw
    except yaml.YAMLError: return None, body, raw

def qy(v):
    if v is None: return ""
    s = str(v)
    if not s: return "''"
    if any(c in s for c in [': ', '#', '{', '}', '[', ']', ',', '&', '*', '!', '"', "'"]):
        if "'" in s: return '"' + s.replace('\\', '\\\\').replace('"', '\\"') + '"'
        return "'" + s + "'"
    if s.lower() in ['true','false','yes','no']: return "'" + s + "'"
    return s

def fmt_fm(fm):
    lines = ["---"]
    for k, v in fm.items():
        if isinstance(v, list):
            if not v: lines.append(f"{k}: []")
            else:
                lines.append(f"{k}:")
                for i in v: lines.append(f"  - {i}")
        elif isinstance(v, dict):
            if not v:
                lines.append(f"{k}: {{}}")
            else:
                lines.append(f"{k}:")
                for k2, v2 in v.items():
                    if isinstance(v2, list):
                        if not v2: lines.append(f"  {k2}: []")
                        else:
                            lines.append(f"  {k2}:")
                            for i2 in v2: lines.append(f"    - {i2}")
                    elif isinstance(v2, dict):
                        lines.append(f"  {k2}: {{}}")
                    else: lines.append(f"  {k2}: {qy(v2)}")
        else: lines.append(f"{k}: {qy(v)}")
    lines.append("---")
    return "\n".join(lines) + "\n"

def heading_exists(body, heading):
    """Check if a heading exists in body."""
    return bool(re.search(r'^##\s*' + re.escape(heading) + r'\s*$', body, re.MULTILINE | re.IGNORECASE))

def heading_exists_prefix(body, heading):
    """Check if a heading exists allowing parenthetical/suffix variants (e.g. '## Rules (from shared-rules-core)')."""
    return bool(re.search(r'^##\s*' + re.escape(heading) + r'(?:\s|\(|$)', body, re.MULTILINE | re.IGNORECASE))

def enhance(pf, dry=True):
    changes = []
    text = pf.read_text(encoding="utf-8")
    fm, body, raw = parse_fm(text)
    if fm is None: return [("SKIP", "Cannot parse YAML")]
    
    name = fm.get("name", pf.stem)
    desc = fm.get("description", "")
    cat = categorize(name, desc, body)
    
    # Frontmatter enhancements
    if "dependencies" not in fm or fm["dependencies"] is None:
        fm["dependencies"] = []; changes.append(("FM", "dependencies"))
    if "metadata" not in fm:
        fm["metadata"] = {"hermes": {}}; changes.append(("FM", "metadata"))
    
    # Build list of sections to append
    appendix = []
    
    # 1. Goal section (if missing, extract from description)
    if not heading_exists(body, "Goal"):
        goal_text = desc if desc else "Complete the task described in this prompt."
        appendix.append(S_GOAL_TMPL.format(text=goal_text))
        changes.append(("SECT", "Goal"))
    
    # 2. Subgoals
    if not heading_exists(body, "Subgoals"):
        appendix.append(S_SUBGOALS)
        changes.append(("SECT", "Subgoals"))
    
    if not heading_exists(body, "Personas"):
        appendix.append(S_PERSONAS)
        changes.append(("SECT", "Personas"))
    if not heading_exists(body, "Personality"):
        appendix.append(S_PERSONALITY)
        changes.append(("SECT", "Personality"))
    if not heading_exists(body, "Context"):
        ctx = CONTEXTS.get(cat, CONTEXTS["general"])
        appendix.append(S_CONTEXT_TMPL.format(text=ctx))
        changes.append(("SECT", f"Context ({cat})"))
    if not heading_exists_prefix(body, "Rules"):
        rules = DOMAIN_RULES.get(cat, DOMAIN_RULES["general"])
        appendix.append(S_RULES.format(rules=rules))
        changes.append(("SECT", f"Rules ({cat})"))
    
    has_phases = heading_exists(body, "Phases")
    has_workflow = heading_exists(body, "Workflow")
    if not has_phases and not has_workflow:
        appendix.append(S_PHASES)
        changes.append(("SECT", "Phases"))
    
    if not heading_exists(body, "Best Practices"):
        appendix.append(S_BEST)
        changes.append(("SECT", "Best Practices"))
    if not heading_exists(body, "Verification Checklist"):
        appendix.append(S_CHECKLIST)
        changes.append(("SECT", "Checklist"))
    
    # Skills Required
    if not heading_exists(body, "Skills Required"):
        srows = S_SKILLS_ROWS.get(cat, S_SKILLS_ROWS["general"])
        appendix.append(S_SKILLS.format(skills_rows=srows))
        changes.append(("SECT", f"Skills Required ({cat})"))
    
    # MCP Servers & Tools
    if not heading_exists(body, "MCP Servers & Tools"):
        mrows = S_MCP_ROWS.get(cat, S_MCP_ROWS["general"])
        appendix.append(S_MCP.format(mcp_rows=mrows))
        changes.append(("SECT", f"MCP ({cat})"))
    
    # Tasks
    if not heading_exists(body, "Tasks"):
        appendix.append(S_TASKS)
        changes.append(("SECT", "Tasks"))
    
    if not heading_exists(body, "Dependencies"):
        appendix.append(S_DEPS)
        changes.append(("SECT", "Dependencies section"))
    
    if not appendix:
        return changes
    
    # Append everything at the end
    new_body = body.rstrip() + "\n\n" + "\n\n".join(appendix) + "\n"
    new_text = fmt_fm(fm) + new_body
    
    if new_text == text: return changes
    
    if not dry:
        pf.write_text(new_text, encoding="utf-8")
        changes.append(("OK", f"{len(new_text)}b"))
    
    return changes

def main():
    dry = "--apply" not in sys.argv
    files = sorted(P.glob("*.prompt.md"))
    print(f"=== Comprehensive Enhancement v3 ===\nMode: {'DRY' if dry else 'APPLY'}\nFiles: {len(files)}\n")
    
    stats = defaultdict(int); results = []
    for pf in files:
        ch = enhance(pf, dry)
        if ch:
            for t, d in ch: stats[t] += 1
            results.append((pf.stem, ch))
    
    print("Changes by type:")
    for t, c in sorted(stats.items(), key=lambda x: -x[1]): print(f"  {t}: {c}")
    print(f"\nFiles modified: {len(results)}")
    
    if results and dry:
        print("\n=== First 3 files with changes ===")
        for name, ch in results[:3]:
            print(f"\n  {name}:")
            for t, d in ch:
                print(f"    - [{t}] {d[:60]}")
    
    print(f"\n{'='*50}")
    print(f"{'DRY RUN. Run with --apply to execute.' if dry else 'APPLY COMPLETE.'}")

if __name__ == "__main__":
    main()
