#!/usr/bin/env python3
"""
consolidate_skills.py — Identify overlapping skills for merge.
Compares descriptions, tags, and content to find candidates for consolidation.
Phase 3/6 of audit-skills-judge-fix pipeline.
"""
import os
import json
import re
from pathlib import Path
from collections import defaultdict

SKILLS_ROOT = Path(r"C:\Users\Alexa\AppData\Local\hermes\skills")
OUTPUT_FILE = Path(r"C:\Users\Alexa\Desktop\SandBox\docs\consolidation-report.md")

def parse_frontmatter(content):
    """Extract YAML frontmatter from SKILL.md content."""
    if not content.startswith('---'):
        return {}
    match = re.match(r'^---\s*\n(.*?)\n---', content, re.DOTALL)
    if not match:
        return {}
    fm = {}
    for line in match.group(1).split('\n'):
        if ':' in line and not line.startswith(' ') and not line.startswith('\t'):
            key, val = line.split(':', 1)
            fm[key.strip()] = val.strip().strip('"\'')
    return fm

def get_skill_info(skill_path):
    """Get skill metadata from SKILL.md."""
    try:
        content = (Path(skill_path) / "SKILL.md").read_text(encoding='utf-8', errors='ignore')
        fm = parse_frontmatter(content)
        lines = len(content.splitlines())
        
        # Count reference files
        refs = 0
        for ref_type in ['references', 'templates', 'scripts']:
            ref_dir = Path(skill_path) / ref_type
            if ref_dir.exists():
                refs += len(list(ref_dir.iterdir()))
        
        return {
            'name': os.path.basename(skill_path),
            'path': str(skill_path),
            'rel_path': os.path.relpath(skill_path, SKILLS_ROOT),
            'description': fm.get('description', ''),
            'tags': fm.get('tags', ''),
            'lines': lines,
            'refs': refs,
            'has_pitfalls': bool(re.search(r'##\s*Pitfalls', content, re.IGNORECASE)),
            'has_checklist': bool(re.search(r'##\s*Verification\s*Checklist', content, re.IGNORECASE)),
            'has_phases': len(re.findall(r'##\s*Phase\s*\d+', content)) >= 2,
        }
    except:
        return None

def find_overlaps(skills_info):
    """Find skills with overlapping purposes."""
    overlaps = []
    
    # Group by similar description keywords
    keyword_groups = defaultdict(list)
    for info in skills_info:
        if info and info['description']:
            # Extract key terms from description
            desc = info['description'].lower()
            # Common purpose keywords
            keywords = []
            for kw in ['browser', 'test', 'code', 'git', 'docker', 'mcp', 'api', 'doc', 'write', 'search', 'train', 'model', 'deploy', 'review', 'debug', 'format', 'lint', 'build', 'commit', 'branch', 'merge', 'clone', 'push', 'pull', 'issue', 'pr', 'pull request', 'ci', 'cd', 'pipeline', 'workflow', 'template', 'generate', 'create', 'update', 'delete', 'manage', 'configure', 'setup', 'install', 'run', 'execute', 'validate', 'verify', 'check', 'audit', 'monitor', 'track', 'log', 'report', 'analyze', 'transform', 'convert', 'extract', 'parse', 'render', 'display', 'show', 'list', 'find', 'search', 'get', 'fetch', 'download', 'upload', 'send', 'receive', 'read', 'write', 'edit', 'modify', 'change', 'add', 'remove', 'enable', 'disable', 'start', 'stop', 'restart', 'pause', 'resume', 'skip', 'cancel', 'retry', 'fail', 'error', 'warn', 'info', 'debug', 'trace']:
                if kw in desc:
                    keywords.append(kw)
            for kw in keywords[:3]:  # Top 3 keywords
                keyword_groups[kw].append(info)
    
    # Find groups with multiple skills
    seen_pairs = set()
    for kw, group in keyword_groups.items():
        if len(group) >= 2:
            for i in range(len(group)):
                for j in range(i + 1, len(group)):
                    pair = tuple(sorted([group[i]['name'], group[j]['name']]))
                    if pair not in seen_pairs:
                        seen_pairs.add(pair)
                        # Check if they're actually similar
                        if group[i]['lines'] < 150 or group[j]['lines'] < 150:
                            overlaps.append({
                                'skill_a': group[i],
                                'skill_b': group[j],
                                'keyword': kw,
                                'reason': f"Both relate to '{kw}'; one may be thin"
                            })
    
    return overlaps

def main():
    print("Analyzing skills for consolidation...")
    
    # Collect all skill info
    skills_info = []
    for root, dirs, files in os.walk(SKILLS_ROOT):
        dirs[:] = [d for d in dirs if not d.startswith('.')]
        if 'SKILL.md' in files:
            info = get_skill_info(root)
            if info:
                skills_info.append(info)
    
    print(f"Analyzed {len(skills_info)} skills")
    
    # Find overlaps
    overlaps = find_overlaps(skills_info)
    
    # Find thin skills (<100 lines, no phases, no checklist)
    thin_skills = [s for s in skills_info if s['lines'] < 100 and not s['has_phases']]
    
    # Find skills missing key structural elements
    missing_structure = [s for s in skills_info if not s['has_pitfalls'] or not s['has_checklist']]
    
    # Generate report
    report = []
    report.append("# Consolidation Report\n")
    report.append(f"**Total skills analyzed:** {len(skills_info)}\n")
    report.append(f"**Potential overlaps:** {len(overlaps)}\n")
    report.append(f"**Thin skills (<100 lines, no phases):** {len(thin_skills)}\n")
    report.append(f"**Skills missing structure:** {len(missing_structure)}\n\n")
    
    report.append("## Potential Overlaps (Merge Candidates)\n")
    report.append("| Skill A | Skill B | Keyword | Reason |\n")
    report.append("|---------|---------|---------|--------|\n")
    for o in overlaps[:50]:  # Limit to top 50
        report.append(f"| {o['skill_a']['name']} ({o['skill_a']['lines']}L) | {o['skill_b']['name']} ({o['skill_b']['lines']}L) | {o['keyword']} | {o['reason']} |\n")
    
    report.append("\n## Thin Skills (Potential Merge Targets)\n")
    report.append("| Skill | Lines | Refs | Has Phases | Has Checklist |\n")
    report.append("|-------|-------|------|------------|----------------|\n")
    for s in sorted(thin_skills, key=lambda x: x['lines']):
        report.append(f"| {s['name']} | {s['lines']} | {s['refs']} | {'✅' if s['has_phases'] else '❌'} | {'✅' if s['has_checklist'] else '❌'} |\n")
    
    report.append("\n## Recommended Consolidation Actions\n")
    report.append("1. **Merge thin skills** into fuller versions with similar purpose\n")
    report.append("2. **Use `skill_manage(action='delete', absorbed_into='<umbrella>')`** for archiving\n")
    report.append("3. **Copy reference files** from absorbed skills to umbrella's `references/` directory\n")
    report.append("4. **Update umbrella SKILL.md** with 'Recently Absorbed Skills' section\n")
    report.append("5. **Verify** with `read_file()` not `skill_view()` (stale cache)\n")
    
    report_text = ''.join(report)
    OUTPUT_FILE.write_text(report_text, encoding='utf-8')
    
    print(f"\nReport written to {OUTPUT_FILE}")
    print(f"Overlaps found: {len(overlaps)}")
    print(f"Thin skills: {len(thin_skills)}")
    print(f"Missing structure: {len(missing_structure)}")

if __name__ == '__main__':
    main()