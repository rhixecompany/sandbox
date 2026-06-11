#!/usr/bin/env python3
"""
DEV INIT PIPELINE - CODE SAMPLES FOR EACH WORKFLOW PHASE

This module contains implementation code samples for the 6-phase
prompt conversion and enhancement pipeline.

Author: Alexa (Code Architect Profile)
Generated: 2026-05-27
"""

import json
import re
from pathlib import Path
from typing import Dict, List, Optional, Tuple
from dataclasses import dataclass
from enum import Enum

# ============================================================================
# PHASE 1: CONVERT PLAINTEXT → MARKDOWN
# ============================================================================

class ConversionPhase:
    """Phase 1: Convert plaintext .txt files to markdown format."""
    
    @staticmethod
    def parse_txt_file(file_path: str) -> Tuple[Dict, str]:
        """
        Parse a plaintext file and extract content structure.
        
        Args:
            file_path: Path to .txt file
            
        Returns:
            Tuple of (frontmatter_dict, markdown_content)
        """
        with open(file_path, 'r') as f:
            content = f.read()
        
        lines = content.split('\n')
        
        # Extract title from first non-empty line
        title = ""
        for line in lines:
            if line.strip() and not line.startswith('#'):
                title = line.strip().rstrip(':').strip()
                break
        
        # Generate trigger from title
        trigger = "/" + re.sub(r'[^a-z0-9-]', '', title.lower().replace(' ', '-'))
        
        # Extract tags based on content keywords
        tags = ConversionPhase._extract_tags(content)
        
        # Build frontmatter
        frontmatter = {
            'title': title,
            'trigger': trigger,
            'tags': tags,
            'generated': '2026-05-27'
        }
        
        return frontmatter, content
    
    @staticmethod
    def _extract_tags(content: str) -> List[str]:
        """Extract domain-specific tags from content."""
        tags = ['hermes', 'copilot']  # Always include base tags
        
        # Domain detection
        if 'bash' in content.lower() or 'shell' in content.lower():
            tags.append('bash')
        if 'git' in content.lower():
            tags.append('git')
        if 'script' in content.lower():
            tags.append('scripts')
        if 'automation' in content.lower():
            tags.append('automation')
        if 'planning' in content.lower():
            tags.append('planning')
        if 'documentation' in content.lower():
            tags.append('documentation')
        if 'migration' in content.lower():
            tags.append('migration')
        if 'security' in content.lower():
            tags.append('security')
        
        return tags
    
    @staticmethod
    def convert_to_markdown(frontmatter: Dict, content: str) -> str:
        """
        Convert plaintext content to markdown format.
        
        Args:
            frontmatter: Frontmatter dictionary
            content: Original plaintext content
            
        Returns:
            Formatted markdown string with frontmatter
        """
        # Build YAML frontmatter
        fm_lines = ['---']
        fm_lines.append(f"title: {frontmatter['title']}")
        fm_lines.append(f"trigger: {frontmatter['trigger']}")
        fm_lines.append(f"tags: {json.dumps(frontmatter['tags'])}")
        fm_lines.append('---')
        fm_lines.append('')
        
        # Process content
        markdown_lines = fm_lines.copy()
        
        for line in content.split('\n'):
            # Convert bold markers
            line = re.sub(r'\*\*(.*?)\*\*', r'**\1**', line)
            
            # Convert emphasis
            line = re.sub(r'_(.+?)_', r'*\1*', line)
            
            # Handle section headers (convert all caps + colon to markdown)
            if line.isupper() and line.endswith(':'):
                markdown_lines.append(f"## {line[:-1]}")
            else:
                markdown_lines.append(line)
        
        return '\n'.join(markdown_lines)
    
    @staticmethod
    def validate_yaml_frontmatter(yaml_str: str) -> Tuple[bool, List[str]]:
        """
        Validate YAML frontmatter structure.
        
        Returns:
            Tuple of (is_valid, error_list)
        """
        errors = []
        
        # Check for required fields
        required_fields = ['title', 'trigger', 'tags']
        for field in required_fields:
            if field + ':' not in yaml_str:
                errors.append(f"Missing required field: {field}")
        
        # Check trigger format
        if not re.search(r'trigger: /[\w-]+', yaml_str):
            errors.append("Trigger must start with / and contain only alphanumeric and hyphens")
        
        # Check tags format
        if 'tags:' not in yaml_str:
            errors.append("Tags must be present")
        
        return len(errors) == 0, errors


# ============================================================================
# PHASE 2: MAP CONTEXT
# ============================================================================

@dataclass
class ContextMap:
    """Context mapping for a prompt file."""
    
    prompt_name: str
    trigger: str
    title: str
    dependencies: List[str]
    skills_required: List[str]
    external_tools: List[str]
    file_paths: Dict[str, List[str]]
    safety_sections: int
    critical_constraints: List[str]
    tags: List[str]

class ContextMapPhase:
    """Phase 2: Map context and extract dependencies."""
    
    @staticmethod
    def extract_context(content: str, frontmatter: Dict) -> ContextMap:
        """
        Extract context information from prompt content.
        
        Args:
            content: Markdown content
            frontmatter: YAML frontmatter dictionary
            
        Returns:
            ContextMap object
        """
        # Extract trigger and title
        trigger = frontmatter['trigger']
        title = frontmatter['title']
        prompt_name = trigger.lstrip('/')
        
        # Find skills required
        skills_match = re.search(
            r'Skills Required\n+((?:- .*\n)*)',
            content,
            re.IGNORECASE
        )
        skills = []
        if skills_match:
            skills = [
                s.strip().lstrip('-').strip()
                for s in skills_match.group(1).split('\n')
                if s.strip()
            ]
        
        # Find dependencies (prompt trigger references)
        dependencies = re.findall(r'/[\w-]+', content)
        dependencies = list(set(d for d in dependencies if d != trigger))
        
        # Find external tools
        external_tools = ContextMapPhase._extract_tools(content)
        
        # Find file paths
        file_paths = ContextMapPhase._extract_file_paths(content)
        
        # Count safety sections
        safety_sections = len(re.findall(
            r'## SAFETY|### CRITICAL|## RISK MANAGEMENT',
            content,
            re.IGNORECASE
        ))
        
        # Extract critical constraints
        critical_constraints = ContextMapPhase._extract_constraints(content)
        
        return ContextMap(
            prompt_name=prompt_name,
            trigger=trigger,
            title=title,
            dependencies=dependencies,
            skills_required=skills,
            external_tools=external_tools,
            file_paths=file_paths,
            safety_sections=safety_sections,
            critical_constraints=critical_constraints,
            tags=frontmatter.get('tags', [])
        )
    
    @staticmethod
    def _extract_tools(content: str) -> List[str]:
        """Extract external tool references from content."""
        tools = []
        
        tool_patterns = [
            r'`([a-z\-]+)\s+(?:command|cli|tool)',
            r'(?:using|with)\s+`([a-z\-]+)`',
            r'(?:install|setup)\s+`([a-z\-]+)`'
        ]
        
        for pattern in tool_patterns:
            matches = re.findall(pattern, content, re.IGNORECASE)
            tools.extend(matches)
        
        return list(set(tools))
    
    @staticmethod
    def _extract_file_paths(content: str) -> Dict[str, List[str]]:
        """Extract input/output file paths from content."""
        file_patterns = {
            'inputs': [
                r'(?:input|source|from):\s+`([^`]+)`',
                r'(?:read|load)\s+`([^`]+)`'
            ],
            'outputs': [
                r'(?:output|destination|to):\s+`([^`]+)`',
                r'(?:write|save)\s+(?:to\s+)?`([^`]+)`'
            ]
        }
        
        paths = {'inputs': [], 'outputs': []}
        
        for category, patterns in file_patterns.items():
            for pattern in patterns:
                matches = re.findall(pattern, content, re.IGNORECASE)
                paths[category].extend(matches)
        
        return {k: list(set(v)) for k, v in paths.items()}
    
    @staticmethod
    def _extract_constraints(content: str) -> List[str]:
        """Extract critical constraints from safety sections."""
        constraints = []
        
        # Find CRITICAL sections
        critical_pattern = r'(?:CRITICAL|MUST|REQUIRED):\s*(.+?)(?:\n|$)'
        constraints.extend(
            m.strip() for m in re.findall(critical_pattern, content, re.IGNORECASE)
        )
        
        return constraints
    
    @staticmethod
    def to_json(context_map: ContextMap) -> str:
        """Serialize context map to JSON."""
        return json.dumps({
            'prompt_name': context_map.prompt_name,
            'trigger': context_map.trigger,
            'title': context_map.title,
            'dependencies': context_map.dependencies,
            'skills_required': context_map.skills_required,
            'external_tools': context_map.external_tools,
            'file_paths': context_map.file_paths,
            'safety_sections': context_map.safety_sections,
            'critical_constraints': context_map.critical_constraints,
            'tags': context_map.tags
        }, indent=2)


# ============================================================================
# PHASE 3: SAFETY REVIEW
# ============================================================================

class ConstraintLevel(Enum):
    """Severity levels for constraints."""
    CRITICAL = 1  # Credential, backup, approval
    HIGH = 2      # Deletion, git ops, production
    MEDIUM = 3    # Build, deploy, large changes
    LOW = 4       # Documentation, non-destructive

class SafetyReviewPhase:
    """Phase 3: Safety review and constraint documentation."""
    
    CRITICAL_PATTERNS = [
        (r'explicit.*approval', ConstraintLevel.CRITICAL),
        (r'sign[- ]off', ConstraintLevel.CRITICAL),
        (r'\d+-person.*review', ConstraintLevel.CRITICAL),
        (r'backup.*required', ConstraintLevel.CRITICAL),
        (r'credential', ConstraintLevel.CRITICAL),
        (r'password', ConstraintLevel.CRITICAL),
        (r'token.*secret', ConstraintLevel.CRITICAL),
        (r'data.*loss', ConstraintLevel.HIGH),
        (r'irreversible|permanent.*delete', ConstraintLevel.HIGH),
        (r'force.*push|rebase', ConstraintLevel.HIGH),
        (r'production', ConstraintLevel.HIGH),
        (r'git.*reset|git.*clean', ConstraintLevel.HIGH),
    ]
    
    @staticmethod
    def audit_constraints(content: str, context_map: ContextMap) -> Dict:
        """
        Audit all constraints in content.
        
        Args:
            content: Prompt markdown content
            context_map: Extracted context from Phase 2
            
        Returns:
            Audit report dictionary
        """
        audit = {
            'total_constraints': 0,
            'by_level': {},
            'critical_found': [],
            'constraints_preserved': True,
            'violations': [],
            'recommendations': []
        }
        
        # Count constraints by level
        for pattern, level in SafetyReviewPhase.CRITICAL_PATTERNS:
            matches = re.findall(pattern, content, re.IGNORECASE)
            if matches:
                level_name = level.name
                if level_name not in audit['by_level']:
                    audit['by_level'][level_name] = []
                
                audit['by_level'][level_name].extend(matches)
                audit['total_constraints'] += len(matches)
        
        # Verify constraints from context
        if context_map.critical_constraints:
            audit['critical_found'] = context_map.critical_constraints
        
        return audit
    
    @staticmethod
    def create_safety_report(audit: Dict, context_map: ContextMap) -> str:
        """Generate a markdown safety audit report."""
        report = "## SAFETY AUDIT REPORT\n\n"
        
        report += f"### Summary\n"
        report += f"- Total constraints found: {audit['total_constraints']}\n"
        report += f"- Safety sections: {context_map.safety_sections}\n"
        report += f"- Constraints preserved: {'✅ YES' if audit['constraints_preserved'] else '❌ NO'}\n\n"
        
        report += "### Constraints by Level\n"
        for level in ['CRITICAL', 'HIGH', 'MEDIUM', 'LOW']:
            if level in audit['by_level']:
                constraints = audit['by_level'][level]
                report += f"\n#### {level} ({len(constraints)} found)\n"
                for constraint in constraints[:5]:  # Show first 5
                    report += f"- {constraint}\n"
                if len(constraints) > 5:
                    report += f"- ... and {len(constraints) - 5} more\n"
        
        if audit['violations']:
            report += "\n### ⚠️ VIOLATIONS DETECTED\n"
            for violation in audit['violations']:
                report += f"- {violation}\n"
        
        report += "\n### Recommendations\n"
        if not audit['violations']:
            report += "- ✅ All constraints intact\n"
            report += "- ✅ Safe to proceed with enhancement\n"
        else:
            report += "- ❌ Fix constraint violations before proceeding\n"
        
        return report


# ============================================================================
# PHASE 4: BOOST/ENHANCE
# ============================================================================

class EnhancementPhase:
    """Phase 4: Boost and enhance prompt content."""
    
    @staticmethod
    def apply_enhancements(
        content: str,
        original_constraints: List[str]
    ) -> Tuple[str, Dict]:
        """
        Apply enhancements while preserving constraints.
        
        Args:
            content: Original markdown content
            original_constraints: List of critical constraints to preserve
            
        Returns:
            Tuple of (enhanced_content, changes_log)
        """
        changes = {
            'clarity_improvements': [],
            'completeness_enhancements': [],
            'structure_optimizations': [],
            'examples_added': [],
            'constraint_violations': []
        }
        
        enhanced = content
        
        # Pre-enhancement: Validate constraints exist
        constraints_before = EnhancementPhase._extract_constraint_text(content)
        
        # Apply enhancements (examples only)
        # In real implementation, would apply transformations from boost template
        
        # Post-enhancement: Validate constraints still present
        constraints_after = EnhancementPhase._extract_constraint_text(enhanced)
        
        if len(constraints_after) < len(constraints_before):
            changes['constraint_violations'].append(
                f"Constraint loss detected: {len(constraints_before) - len(constraints_after)} constraints removed"
            )
        
        return enhanced, changes
    
    @staticmethod
    def _extract_constraint_text(content: str) -> List[str]:
        """Extract all constraint-related text."""
        patterns = [
            r'(?:MUST|CRITICAL|REQUIRED|APPROVAL|BACKUP).*',
            r'(?:Do not|Never|Always).*(?:delete|modify|change)',
        ]
        
        constraints = []
        for pattern in patterns:
            constraints.extend(re.findall(pattern, content, re.IGNORECASE))
        
        return constraints
    
    @staticmethod
    def validate_enhancement(
        original: str,
        enhanced: str,
        original_audit: Dict
    ) -> Tuple[bool, List[str]]:
        """
        Validate that enhancements don't violate constraints.
        
        Returns:
            Tuple of (is_valid, error_messages)
        """
        errors = []
        
        # Check constraint count
        original_count = original_audit['total_constraints']
        enhanced_audit = SafetyReviewPhase.audit_constraints(enhanced, None)
        enhanced_count = enhanced_audit['total_constraints']
        
        if enhanced_count < original_count:
            errors.append(
                f"Constraint count decreased: {original_count} → {enhanced_count}"
            )
        
        # Check critical constraint pattern preservation
        for pattern, level in SafetyReviewPhase.CRITICAL_PATTERNS:
            if level == ConstraintLevel.CRITICAL:
                if re.search(pattern, original, re.IGNORECASE):
                    if not re.search(pattern, enhanced, re.IGNORECASE):
                        errors.append(f"Critical constraint pattern lost: {pattern}")
        
        return len(errors) == 0, errors


# ============================================================================
# PHASE 5: UPDATE IMPLEMENTATION PLANS
# ============================================================================

class PlanUpdatePhase:
    """Phase 5: Update implementation plans and cross-references."""
    
    @staticmethod
    def find_plan_references(content: str) -> Dict[str, List[str]]:
        """
        Find references to implementation plans and documentation.
        
        Returns:
            Dictionary mapping file types to references
        """
        references = {
            'prompts': [],
            'plans': [],
            'documentation': [],
            'external': []
        }
        
        # Find prompt trigger references
        prompt_refs = re.findall(r'/[\w-]+', content)
        references['prompts'] = list(set(prompt_refs))
        
        # Find plan references
        plan_refs = re.findall(r'plan/[\w\-\.]+\.md', content)
        references['plans'] = list(set(plan_refs))
        
        # Find doc references
        doc_refs = re.findall(r'docs/[\w\-\.]+\.md', content)
        references['documentation'] = list(set(doc_refs))
        
        # Find external URLs
        external_refs = re.findall(r'https?://[^\s\)]+', content)
        references['external'] = list(set(external_refs))
        
        return references
    
    @staticmethod
    def validate_references(references: Dict[str, List[str]]) -> Dict[str, List[str]]:
        """
        Validate that all references point to existing files.
        
        Returns:
            Dictionary with validation status for each reference
        """
        validation = {
            'valid': [],
            'missing': [],
            'unresolvable': []
        }
        
        for ref_type, refs in references.items():
            if ref_type == 'external':
                # External URLs - mark as unresolvable (can't check locally)
                validation['unresolvable'].extend(refs)
            else:
                # Check local file references
                for ref in refs:
                    path = Path(ref) if ref_type != 'prompts' else Path(f"{ref}.md")
                    
                    if path.exists():
                        validation['valid'].append(ref)
                    else:
                        validation['missing'].append(ref)
        
        return validation


# ============================================================================
# PHASE 6: FINAL VALIDATION AND ASSEMBLY
# ============================================================================

class ValidationPhase:
    """Phase 6: Comprehensive validation of final prompts."""
    
    @staticmethod
    def validate_yaml(content: str) -> Tuple[bool, List[str]]:
        """Validate YAML frontmatter."""
        errors = []
        
        if not content.startswith('---'):
            errors.append("Missing YAML frontmatter start marker")
        
        # Check for required fields
        required = ['title:', 'trigger:', 'tags:']
        for field in required:
            if field not in content.split('---')[1]:
                errors.append(f"Missing required field: {field}")
        
        # Validate trigger format
        trigger_match = re.search(r'trigger: (/.+)', content)
        if trigger_match:
            trigger = trigger_match.group(1)
            if not re.match(r'^/[\w-]+$', trigger.strip()):
                errors.append(f"Invalid trigger format: {trigger}")
        
        return len(errors) == 0, errors
    
    @staticmethod
    def validate_markdown_syntax(content: str) -> Tuple[bool, List[str]]:
        """Validate markdown syntax."""
        errors = []
        
        # Check for unclosed code blocks
        code_blocks = re.findall(r'```[\s\S]*?```', content)
        if len(code_blocks) != len(re.findall(r'```', content)) // 2:
            errors.append("Unclosed code blocks detected")
        
        # Check for unmatched brackets
        if content.count('[') != content.count(']'):
            errors.append("Unmatched brackets in markdown")
        
        # Check for unmatched parentheses
        if content.count('(') != content.count(')'):
            errors.append("Unmatched parentheses in markdown")
        
        return len(errors) == 0, errors
    
    @staticmethod
    def calculate_quality_metrics(content: str) -> Dict:
        """Calculate quality metrics for prompt."""
        metrics = {
            'file_size_kb': len(content.encode()) / 1024,
            'line_count': len(content.split('\n')),
            'section_count': len(re.findall(r'^## ', content, re.MULTILINE)),
            'code_block_count': len(re.findall(r'```', content)) // 2,
            'link_count': len(re.findall(r'\[.+?\]\(.+?\)', content)),
            'has_examples': bool(re.search(r'example|sample', content, re.IGNORECASE)),
            'has_safety': bool(re.search(r'SAFETY|CRITICAL|RISK', content, re.IGNORECASE))
        }
        
        return metrics
    
    @staticmethod
    def generate_validation_report(
        filename: str,
        yaml_valid: Tuple[bool, List],
        markdown_valid: Tuple[bool, List],
        metrics: Dict
    ) -> str:
        """Generate comprehensive validation report."""
        report = f"# VALIDATION REPORT: {filename}\n\n"
        
        report += "## YAML Frontmatter\n"
        report += f"- Status: {'✅ PASS' if yaml_valid[0] else '❌ FAIL'}\n"
        if yaml_valid[1]:
            for error in yaml_valid[1]:
                report += f"  - Error: {error}\n"
        report += "\n"
        
        report += "## Markdown Syntax\n"
        report += f"- Status: {'✅ PASS' if markdown_valid[0] else '❌ FAIL'}\n"
        if markdown_valid[1]:
            for error in markdown_valid[1]:
                report += f"  - Error: {error}\n"
        report += "\n"
        
        report += "## Quality Metrics\n"
        for metric, value in metrics.items():
            report += f"- {metric}: {value}\n"
        
        return report


# ============================================================================
# USAGE EXAMPLE
# ============================================================================

if __name__ == "__main__":
    # Example: Process a single file through all phases
    
    txt_file = "Prompts/dev-init.prompts.txt"
    
    # Phase 1: Convert
    print("Phase 1: Converting to markdown...")
    frontmatter, content = ConversionPhase.parse_txt_file(txt_file)
    markdown = ConversionPhase.convert_to_markdown(frontmatter, content)
    
    # Phase 2: Map context
    print("Phase 2: Mapping context...")
    context_map = ContextMapPhase.extract_context(markdown, frontmatter)
    context_json = ContextMapPhase.to_json(context_map)
    
    # Phase 3: Safety review
    print("Phase 3: Reviewing safety...")
    audit = SafetyReviewPhase.audit_constraints(markdown, context_map)
    safety_report = SafetyReviewPhase.create_safety_report(audit, context_map)
    
    # Phase 4: Enhance (with constraint validation)
    print("Phase 4: Enhancing content...")
    enhanced, changes = EnhancementPhase.apply_enhancements(
        markdown,
        context_map.critical_constraints
    )
    valid, errors = EnhancementPhase.validate_enhancement(
        markdown, enhanced, audit
    )
    
    if not valid:
        print(f"❌ Enhancement validation failed: {errors}")
    
    # Phase 5: Update plans
    print("Phase 5: Updating plans...")
    references = PlanUpdatePhase.find_plan_references(enhanced)
    validation = PlanUpdatePhase.validate_references(references)
    
    # Phase 6: Final validation
    print("Phase 6: Final validation...")
    yaml_valid = ValidationPhase.validate_yaml(enhanced)
    md_valid = ValidationPhase.validate_markdown_syntax(enhanced)
    metrics = ValidationPhase.calculate_quality_metrics(enhanced)
    validation_report = ValidationPhase.generate_validation_report(
        "test.md", yaml_valid, md_valid, metrics
    )
    
    print("\n" + "="*60)
    print("PIPELINE COMPLETE")
    print("="*60)
    print(validation_report)
