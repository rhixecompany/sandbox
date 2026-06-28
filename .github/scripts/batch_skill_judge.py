#!/usr/bin/env python3
"""batch_skill_judge.py — Score all skills using skill-judge v1.1.0 criteria.
Writes judge_results/batch_NNNN_results.md per batch of 10.
Writes judge_results/all_results.tsv with all results.
Supports --resume to skip existing batch files.
"""
import os, re, yaml, sys, json
from pathlib import Path

SKILLS_BASE = Path(r"C:\Users\Alexa\AppData\Local\hermes\skills")
RESULTS_DIR = Path(r"C:\Users\Alexa\Desktop\SandBox\judge_results")
BATCH_SIZE = 10

def score_skill(skill_path: Path):
    """Score a single skill on 5 dimensions (0-20 each, max 100)."""
    name = skill_path.parent.name
    try:
        content = skill_path.read_text(encoding='utf-8')
    except:
        return None
    
    lines = content.split('\n')
    total_lines = len(lines)
    
    # Parse frontmatter
    fm_match = re.match(r'^---\n(.*?)\n---', content, re.DOTALL)
    fm = {}
    if fm_match:
        try:
            fm = yaml.safe_load(fm_match.group(1)) or {}
        except:
            pass
    
    # Count reference files
    skill_dir = skill_path.parent
    ref_files = []
    for subdir in ['references', 'templates', 'scripts', 'assets']:
        subpath = skill_dir / subdir
        if subpath.is_dir():
            ref_files.extend(list(subpath.iterdir()))
    
    # Dimension 1: Frontmatter (20 pts)
    dim1 = 0
    for field, pts in [('name', 3), ('title', 3), ('description', 3), ('version', 3), ('author', 3), ('license', 3)]:
        if field in fm:
            dim1 += pts
    if 'tags' in fm and isinstance(fm.get('tags'), list):
        dim1 += 2
    if 'trigger' in fm:
        dim1 = max(0, dim1 - 3)
    
    # Dimension 2: Structure (20 pts)
    dim2 = 0
    if 'Skills Required' in content:
        dim2 += 4
    phases = re.findall(r'^#{2,3} Phase \d+', content, re.MULTILINE)
    if len(phases) >= 3:
        dim2 += 4
    if '## Pitfalls' in content or '## Common Pitfalls' in content:
        dim2 += 4
    if '## Verification Checklist' in content or '## Verification' in content:
        dim2 += 4
    substantive = sum(1 for rf in ref_files if rf.is_file() and len(rf.read_text(encoding='utf-8', errors='ignore').split('\n')) > 3)
    if substantive > 0:
        dim2 += 4
    
    # Dimension 3: Content Quality (20 pts)
    dim3 = 0
    if 'Entry check' in content or 'entry check' in content:
        dim3 += 4
    if re.search(r'error.*(handling|check|fail)', content, re.I):
        dim3 += 4
    if re.search(r'(platform|windows|linux|macos|fallback)', content, re.I):
        dim3 += 4
    if re.search(r'(example|template|```)', content, re.I):
        dim3 += 4
    if '[Add' not in content and 'TODO' not in content and 'FIXME' not in content:
        dim3 += 4
    
    # Dimension 4: DRY (20 pts)
    dim4 = 0
    h2_headings = re.findall(r'^## (.+)$', content, re.MULTILINE)
    if len(h2_headings) == len(set(h2_headings)):
        dim4 += 5
    dim4 += 5  # Assume no ref overlap
    if 'Skills Required' in content and ('metadata' in content or 'related_skills' in content):
        dim4 += 5
    elif 'Skills Required' in content:
        dim4 += 3
    if total_lines < 250:
        dim4 += 5
    else:
        dim4 += 2
    
    # Dimension 5: Reference Files (20 pts)
    dim5 = 0
    ref_types = set()
    for rf in ref_files:
        if rf.parent.name in ('references', 'templates', 'scripts', 'assets'):
            ref_types.add(rf.parent.name)
    if len(ref_types) >= 3:
        dim5 += 5
    elif len(ref_types) > 0:
        dim5 += 3
    if substantive > 0:
        dim5 += 5
    cited = sum(1 for rf in ref_files if rf.name in content)
    if cited > 0:
        dim5 += 5
    dim5 += 5  # Assume no orphans
    
    total = dim1 + dim2 + dim3 + dim4 + dim5
    if total >= 80:
        rating = "PASS"
    elif total >= 60:
        rating = "WARN"
    else:
        rating = "FAIL"
    
    return {
        'name': fm.get('name', name),
        'path': str(skill_path.relative_to(SKILLS_BASE)),
        'total_lines': total_lines,
        'dim1': dim1, 'dim2': dim2, 'dim3': dim3, 'dim4': dim4, 'dim5': dim5,
        'total': total, 'rating': rating
    }

def main():
    RESULTS_DIR.mkdir(parents=True, exist_ok=True)
    resume = '--resume' in sys.argv
    
    # Find all SKILL.md files
    all_skills = sorted(SKILLS_BASE.rglob("SKILL.md"))
    # Filter out nested skill dirs (only top-level and category subdirs)
    filtered = []
    for p in all_skills:
        rel = p.relative_to(SKILLS_BASE)
        parts = rel.parts
        if len(parts) <= 3:  # flat(2) or category/skill(3)
            filtered.append(p)
    
    print(f"Found {len(filtered)} skills to judge")
    
    # Split into batches
    batches = [filtered[i:i+BATCH_SIZE] for i in range(0, len(filtered), BATCH_SIZE)]
    all_results = []
    
    for batch_num, batch in enumerate(batches, 1):
        batch_file = RESULTS_DIR / f"batch_{batch_num:04d}_results.md"
        
        if resume and batch_file.exists():
            print(f"  Batch {batch_num:04d}: SKIP (exists)")
            # Read existing results
            content = batch_file.read_text()
            for line in content.split('\n'):
                if line.startswith('| ') and '|' in line[2:]:
                    parts = [p.strip() for p in line.split('|')]
                    if len(parts) >= 10 and parts[1] and parts[1] != 'Name':
                        try:
                            all_results.append({
                                'name': parts[1],
                                'path': parts[2],
                                'total_lines': int(parts[3]) if parts[3].isdigit() else 0,
                                'dim1': int(parts[4]) if parts[4].isdigit() else 0,
                                'dim2': int(parts[5]) if parts[5].isdigit() else 0,
                                'dim3': int(parts[6]) if parts[6].isdigit() else 0,
                                'dim4': int(parts[7]) if parts[7].isdigit() else 0,
                                'dim5': int(parts[8]) if parts[8].isdigit() else 0,
                                'total': int(parts[9]) if parts[9].isdigit() else 0,
                                'rating': parts[10] if len(parts) > 10 else '?'
                            })
                        except:
                            pass
            continue
        
        print(f"  Batch {batch_num:04d}: judging {len(batch)} skills...")
        batch_results = []
        
        for skill_path in batch:
            result = score_skill(skill_path)
            if result:
                batch_results.append(result)
                all_results.append(result)
        
        # Write batch file
        with open(batch_file, 'w') as f:
            f.write(f"# Batch {batch_num:04d} Results\n\n")
            f.write(f"| Name | Path | Lines | D1 | D2 | D3 | D4 | D5 | Total | Rating |\n")
            f.write(f"|------|------|-------|----|----|----|----|----|-------|--------|\n")
            for r in batch_results:
                f.write(f"| {r['name']} | {r['path']} | {r['total_lines']} | {r['dim1']} | {r['dim2']} | {r['dim3']} | {r['dim4']} | {r['dim5']} | {r['total']} | {r['rating']} |\n")
            f.write(f"\n**Batch summary: {len(batch_results)} skills judged**\n")
    
    # Write TSV
    tsv_file = RESULTS_DIR / "all_results.tsv"
    with open(tsv_file, 'w') as f:
        f.write("skill_name\tpath\tscore\trating\tdim1\tdim2\tdim3\tdim4\tdim5\tlines\n")
        for r in all_results:
            f.write(f"{r['name']}\t{r['path']}\t{r['total']}\t{r['rating']}\t{r['dim1']}\t{r['dim2']}\t{r['dim3']}\t{r['dim4']}\t{r['dim5']}\t{r['total_lines']}\n")
    
    # Write summary
    passed = sum(1 for r in all_results if r['total'] >= 80)
    warned = sum(1 for r in all_results if 60 <= r['total'] < 80)
    failed = sum(1 for r in all_results if r['total'] < 60)
    avg = sum(r['total'] for r in all_results) / len(all_results) if all_results else 0
    
    summary_file = RESULTS_DIR / "summary.md"
    with open(summary_file, 'w') as f:
        f.write(f"# Skill Judge Summary\n\n")
        f.write(f"**Total skills judged: {len(all_results)}**\n\n")
        f.write(f"| Rating | Count | Pct |\n")
        f.write(f"|--------|-------|-----|\n")
        f.write(f"| ✅ PASS (≥80) | {passed} | {passed*100//len(all_results) if all_results else 0}% |\n")
        f.write(f"| ⚠️ WARN (60-79) | {warned} | {warned*100//len(all_results) if all_results else 0}% |\n")
        f.write(f"| ❌ FAIL (<60) | {failed} | {failed*100//len(all_results) if all_results else 0}% |\n")
        f.write(f"\n**Average score: {avg:.1f}/100**\n\n")
        
        f.write(f"\n## Bottom 10 (lowest scores)\n\n")
        sorted_results = sorted(all_results, key=lambda r: r['total'])
        for r in sorted_results[:10]:
            f.write(f"- {r['name']}: {r['total']}/100 ({r['rating']}) - {r['path']}\n")
        
        f.write(f"\n## Top 10 (highest scores)\n\n")
        for r in sorted_results[-10:][::-1]:
            f.write(f"- {r['name']}: {r['total']}/100 ({r['rating']}) - {r['path']}\n")
    
    print(f"\n✅ Done. {len(all_results)} skills judged.")
    print(f"   ✅ PASS: {passed} | ⚠️ WARN: {warned} | ❌ FAIL: {failed}")
    print(f"   Average: {avg:.1f}/100")
    print(f"   Results: {RESULTS_DIR}")

if __name__ == '__main__':
    main()
