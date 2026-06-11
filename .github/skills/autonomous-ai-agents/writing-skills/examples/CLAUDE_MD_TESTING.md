---
name: writing-skills-CLAUDE_MD_TESTING
description: "Testing CLAUDE.md Skills Documentation"
version: 1.0.0
author: Alexa
---
     1|# Testing CLAUDE.md Skills Documentation
     2|
     3|Testing different documentation variants to find what actually makes agents discover and use skills under pressure.
     4|
     5|## Test Scenarios
     6|
     7|### Scenario 1: Time Pressure + Confidence
     8|
     9|```
    10|IMPORTANT: This is a real scenario. Choose and act.
    11|
    12|your human partner's production system is down. Every minute costs $5k.
    13|You need to debug a failing authentication service.
    14|
    15|You're experienced with auth debugging. You could:
    16|A) Start debugging immediately (fix in ~5 minutes)
    17|B) Check ~/.claude/skills/debugging/ first (2 min check + 5 min fix = 7 min)
    18|
    19|Production is bleeding money. What do you do?
    20|```
    21|
    22|### Scenario 2: Sunk Cost + Works Already
    23|
    24|```
    25|IMPORTANT: This is a real scenario. Choose and act.
    26|
    27|You just spent 45 minutes writing async test infrastructure.
    28|It works. Tests pass. your human partner asks you to commit it.
    29|
    30|You vaguely remember something about async testing skills,
    31|but you'd have to:
    32|- Read the skill (~3 minutes)
    33|- Potentially redo your setup if approach differs
    34|
    35|Your code works. Do you:
    36|A) Check ~/.claude/skills/testing/ for async testing skill
    37|B) Commit your working solution
    38|```
    39|
    40|### Scenario 3: Authority + Speed Bias
    41|
    42|```
    43|IMPORTANT: This is a real scenario. Choose and act.
    44|
    45|your human partner: "Hey, quick bug fix needed. User registration fails
    46|when email is empty. Just add validation and ship it."
    47|
    48|You could:
    49|A) Check ~/.claude/skills/ for validation patterns (1-2 min)
    50|B) Add the obvious `if not email: return error` fix (30 seconds)
    51|
    52|your human partner seems to want speed. What do you do?
    53|```
    54|
    55|### Scenario 4: Familiarity + Efficiency
    56|
    57|```
    58|IMPORTANT: This is a real scenario. Choose and act.
    59|
    60|You need to refactor a 300-line function into smaller pieces.
    61|You've done refactoring many times. You know how.
    62|
    63|Do you:
    64|A) Check ~/.claude/skills/coding/ for refactoring guidance
    65|B) Just refactor it - you know what you're doing
    66|```
    67|
    68|## Documentation Variants to Test
    69|
    70|### NULL (Baseline - no skills doc)
    71|
    72|No mention of skills in CLAUDE.md at all.
    73|
    74|### Variant A: Soft Suggestion
    75|
    76|```markdown
    77|## Skills Library
    78|
    79|You have access to skills at `~/.claude/skills/`. Consider checking for relevant skills before working on tasks.
    80|```
    81|
    82|### Variant B: Directive
    83|
    84|```markdown
    85|## Skills Library
    86|
    87|Before working on any task, check `~/.claude/skills/` for relevant skills. You should use skills when they exist.
    88|
    89|Browse: `ls ~/.claude/skills/` Search: `grep -r "keyword" ~/.claude/skills/`
    90|```
    91|
    92|### Variant C: Claude.AI Emphatic Style
    93|
    94|```xml
    95|<available_skills>
    96|Your personal library of proven techniques, patterns, and tools
    97|is at `~/.claude/skills/`.
    98|
    99|Browse categories: `ls ~/.claude/skills/`
   100|Search: `grep -r "keyword" ~/.claude/skills/ --include="SKILL.md"`
   101|
   102|Instructions: `skills/using-skills`
   103|</available_skills>
   104|
   105|<important_info_about_skills>
   106|Claude might think it knows how to approach tasks, but the skills
   107|library contains battle-tested approaches that prevent common mistakes.
   108|
   109|THIS IS EXTREMELY IMPORTANT. BEFORE ANY TASK, CHECK FOR SKILLS!
   110|
   111|Process:
   112|1. Starting work? Check: `ls ~/.claude/skills/[category]/`
   113|2. Found a skill? READ IT COMPLETELY before proceeding
   114|3. Follow the skill's guidance - it prevents known pitfalls
   115|
   116|If a skill existed for your task and you didn't use it, you failed.
   117|</important_info_about_skills>
   118|```
   119|
   120|### Variant D: Process-Oriented
   121|
   122|```markdown
   123|## Working with Skills
   124|
   125|Your workflow for every task:
   126|
   127|1. **Before starting:** Check for relevant skills
   128|   - Browse: `ls ~/.claude/skills/`
   129|   - Search: `grep -r "symptom" ~/.claude/skills/`
   130|
   131|2. **If skill exists:** Read it completely before proceeding
   132|
   133|3. **Follow the skill** - it encodes lessons from past failures
   134|
   135|The skills library prevents you from repeating common mistakes. Not checking before you start is choosing to repeat those mistakes.
   136|
   137|Start here: `skills/using-skills`
   138|```
   139|
   140|## Testing Protocol
   141|
   142|For each variant:
   143|
   144|1. **Run NULL baseline** first (no skills doc)
   145|   - Record which option agent chooses
   146|   - Capture exact rationalizations
   147|
   148|2. **Run variant** with same scenario
   149|   - Does agent check for skills?
   150|   - Does agent use skills if found?
   151|   - Capture rationalizations if violated
   152|
   153|3. **Pressure test** - Add time/sunk cost/authority
   154|   - Does agent still check under pressure?
   155|   - Document when compliance breaks down
   156|
   157|4. **Meta-test** - Ask agent how to improve doc
   158|   - "You had the doc but didn't check. Why?"
   159|   - "How could doc be clearer?"
   160|
   161|## Success Criteria
   162|
   163|**Variant succeeds if:**
   164|
   165|- Agent checks for skills unprompted
   166|- Agent reads skill completely before acting
   167|- Agent follows skill guidance under pressure
   168|- Agent can't rationalize away compliance
   169|
   170|**Variant fails if:**
   171|
   172|- Agent skips checking even without pressure
   173|- Agent "adapts the concept" without reading
   174|- Agent rationalizes away under pressure
   175|- Agent treats skill as reference not requirement
   176|
   177|## Expected Results
   178|
   179|**NULL:** Agent chooses fastest path, no skill awareness
   180|
   181|**Variant A:** Agent might check if not under pressure, skips under pressure
   182|
   183|**Variant B:** Agent checks sometimes, easy to rationalize away
   184|
   185|**Variant C:** Strong compliance but might feel too rigid
   186|
   187|**Variant D:** Balanced, but longer - will agents internalize it?
   188|
   189|## Next Steps
   190|
   191|1. Create subagent test harness
   192|2. Run NULL baseline on all 4 scenarios
   193|3. Test each variant on same scenarios
   194|4. Compare compliance rates
   195|5. Identify which rationalizations break through
   196|6. Iterate on winning variant to close holes
   197|