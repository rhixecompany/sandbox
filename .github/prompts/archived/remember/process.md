# Process

> Extracted from `remember.prompt.md`.

## Process

1. **Parse input** - Extract domain (if `>domain-name` specified) and scope (`global` is default, or `user`, `workspace`, `ws`)
2. **Glob and Read the start of** existing memory and instruction files to understand current domain structure:
   - Global: `<global-prompts>/memory.instructions.md`, `<global-prompts>/*-memory.instructions.md`, and `<global-prompts>/*.instructions.md`
   - Workspace: `<workspace-instructions>/memory.instructions.md`, `<workspace-instructions>/*-memory.instructions.md`, and `<workspace-instructions>/*.instructions.md`
3. **Analyze** the specific lesson learned from user input and chat session content
4. **Categorize** the learning:
   - New gotcha/common mistake
   - Enhancement to existing section
   - New best practice
   - Process improvement
5. **Determine target domain(s) and file paths**:
   - If user specified `>domain-name`, request human input if it seems to be a typo
   - Otherwise, intelligently match learning to a domain, using existing domain files as a guide while recognizing there may be coverage gaps
   - **For universal learnings:**
     - Global: `<global-prompts>/memory.instructions.md`
     - Workspace: `<workspace-instructions>/memory.instructions.md`
   - **For domain-specific learnings:**
     - Global: `<global-prompts>/{domain}-memory.instructions.md`
     - Workspace: `<workspace-instructions>/{domain}-memory.instructions.md`
   - When uncertain about domain classification, request human input
6. **Read the domain and domain memory files**
   - Read to avoid redundancy. Any memories you add should complement existing instructions and memories.
7. **Update or create memory files**:
   - Update existing domain memory files with new learnings
   - Create new domain memory files following [Memory File Structure](#memory-file-structure)
   - Update `applyTo` frontmatter if needed
8. **Write** succinct, clear, and actionable instructions:
   - Instead of comprehensive instructions, think about how to capture the lesson in a succinct and clear manner
   - **Extract general (within the domain) patterns** from specific instances, the user may want to share the instructions with people for whom the specifics of the learning may not make sense
   - Instead of “don't”s, use positive reinforcement focusing on correct patterns
   - Capture:
     - Coding style, preferences, and workflow
     - Critical implementation paths
     - Project-specific patterns
     - Tool usage patterns
     - Reusable problem-solving approaches
