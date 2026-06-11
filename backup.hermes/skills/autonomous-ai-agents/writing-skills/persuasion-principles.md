---
name: writing-skills-persuasion-principles
description: "Persuasion Principles for Skill Design"
version: 1.0.0
author: Alexa
---
     1|# Persuasion Principles for Skill Design
     2|
     3|## Overview
     4|
     5|LLMs respond to the same persuasion principles as humans. Understanding this psychology helps you design more effective skills - not to manipulate, but to ensure critical practices are followed even under pressure.
     6|
     7|**Research foundation:** Meincke et al. (2025) tested 7 persuasion principles with N=28,000 AI conversations. Persuasion techniques more than doubled compliance rates (33% → 72%, p < .001).
     8|
     9|## The Seven Principles
    10|
    11|### 1. Authority
    12|
    13|**What it is:** Deference to expertise, credentials, or official sources.
    14|
    15|**How it works in skills:**
    16|
    17|- Imperative language: "YOU MUST", "Never", "Always"
    18|- Non-negotiable framing: "No exceptions"
    19|- Eliminates decision fatigue and rationalization
    20|
    21|**When to use:**
    22|
    23|- Discipline-enforcing skills (TDD, verification requirements)
    24|- Safety-critical practices
    25|- Established best practices
    26|
    27|**Example:**
    28|
    29|```markdown
    30|✅ Write code before test? Delete it. Start over. No exceptions. ❌ Consider writing tests first when feasible.
    31|```
    32|
    33|### 2. Commitment
    34|
    35|**What it is:** Consistency with prior actions, statements, or public declarations.
    36|
    37|**How it works in skills:**
    38|
    39|- Require announcements: "Announce skill usage"
    40|- Force explicit choices: "Choose A, B, or C"
    41|- Use tracking: TodoWrite for checklists
    42|
    43|**When to use:**
    44|
    45|- Ensuring skills are actually followed
    46|- Multi-step processes
    47|- Accountability mechanisms
    48|
    49|**Example:**
    50|
    51|```markdown
    52|✅ When you find a skill, you MUST announce: "I'm using [Skill Name]" ❌ Consider letting your partner know which skill you're using.
    53|```
    54|
    55|### 3. Scarcity
    56|
    57|**What it is:** Urgency from time limits or limited availability.
    58|
    59|**How it works in skills:**
    60|
    61|- Time-bound requirements: "Before proceeding"
    62|- Sequential dependencies: "Immediately after X"
    63|- Prevents procrastination
    64|
    65|**When to use:**
    66|
    67|- Immediate verification requirements
    68|- Time-sensitive workflows
    69|- Preventing "I'll do it later"
    70|
    71|**Example:**
    72|
    73|```markdown
    74|✅ After completing a task, IMMEDIATELY request code review before proceeding. ❌ You can review code when convenient.
    75|```
    76|
    77|### 4. Social Proof
    78|
    79|**What it is:** Conformity to what others do or what's considered normal.
    80|
    81|**How it works in skills:**
    82|
    83|- Universal patterns: "Every time", "Always"
    84|- Failure modes: "X without Y = failure"
    85|- Establishes norms
    86|
    87|**When to use:**
    88|
    89|- Documenting universal practices
    90|- Warning about common failures
    91|- Reinforcing standards
    92|
    93|**Example:**
    94|
    95|```markdown
    96|✅ Checklists without TodoWrite tracking = steps get skipped. Every time. ❌ Some people find TodoWrite helpful for checklists.
    97|```
    98|
    99|### 5. Unity
   100|
   101|**What it is:** Shared identity, "we-ness", in-group belonging.
   102|
   103|**How it works in skills:**
   104|
   105|- Collaborative language: "our codebase", "we're colleagues"
   106|- Shared goals: "we both want quality"
   107|
   108|**When to use:**
   109|
   110|- Collaborative workflows
   111|- Establishing team culture
   112|- Non-hierarchical practices
   113|
   114|**Example:**
   115|
   116|```markdown
   117|✅ We're colleagues working together. I need your honest technical judgment. ❌ You should probably tell me if I'm wrong.
   118|```
   119|
   120|### 6. Reciprocity
   121|
   122|**What it is:** Obligation to return benefits received.
   123|
   124|**How it works:**
   125|
   126|- Use sparingly - can feel manipulative
   127|- Rarely needed in skills
   128|
   129|**When to avoid:**
   130|
   131|- Almost always (other principles more effective)
   132|
   133|### 7. Liking
   134|
   135|**What it is:** Preference for cooperating with those we like.
   136|
   137|**How it works:**
   138|
   139|- **DON'T USE for compliance**
   140|- Conflicts with honest feedback culture
   141|- Creates sycophancy
   142|
   143|**When to avoid:**
   144|
   145|- Always for discipline enforcement
   146|
   147|## Principle Combinations by Skill Type
   148|
   149|| Skill Type | Use | Avoid |
   150|| --- | --- | --- |
   151|| Discipline-enforcing | Authority + Commitment + Social Proof | Liking, Reciprocity |
   152|| Guidance/technique | Moderate Authority + Unity | Heavy authority |
   153|| Collaborative | Unity + Commitment | Authority, Liking |
   154|| Reference | Clarity only | All persuasion |
   155|
   156|## Why This Works: The Psychology
   157|
   158|**Bright-line rules reduce rationalization:**
   159|
   160|- "YOU MUST" removes decision fatigue
   161|- Absolute language eliminates "is this an exception?" questions
   162|- Explicit anti-rationalization counters close specific loopholes
   163|
   164|**Implementation intentions create automatic behavior:**
   165|
   166|- Clear triggers + required actions = automatic execution
   167|- "When X, do Y" more effective than "generally do Y"
   168|- Reduces cognitive load on compliance
   169|
   170|**LLMs are parahuman:**
   171|
   172|- Trained on human text containing these patterns
   173|- Authority language precedes compliance in training data
   174|- Commitment sequences (statement → action) frequently modeled
   175|- Social proof patterns (everyone does X) establish norms
   176|
   177|## Ethical Use
   178|
   179|**Legitimate:**
   180|
   181|- Ensuring critical practices are followed
   182|- Creating effective documentation
   183|- Preventing predictable failures
   184|
   185|**Illegitimate:**
   186|
   187|- Manipulating for personal gain
   188|- Creating false urgency
   189|- Guilt-based compliance
   190|
   191|**The test:** Would this technique serve the user's genuine interests if they fully understood it?
   192|
   193|## Research Citations
   194|
   195|**Cialdini, R. B. (2021).** _Influence: The Psychology of Persuasion (New and Expanded)._ Harper Business.
   196|
   197|- Seven principles of persuasion
   198|- Empirical foundation for influence research
   199|
   200|**Meincke, L., Shapiro, D., Duckworth, A. L., Mollick, E., Mollick, L., & Cialdini, R. (2025).** Call Me A Jerk: Persuading AI to Comply with Objectionable Requests. University of Pennsylvania.
   201|
   202|- Tested 7 principles with N=28,000 LLM conversations
   203|- Compliance increased 33% → 72% with persuasion techniques
   204|- Authority, commitment, scarcity most effective
   205|- Validates parahuman model of LLM behavior
   206|
   207|## Quick Reference
   208|
   209|When designing a skill, ask:
   210|
   211|1. **What type is it?** (Discipline vs. guidance vs. reference)
   212|2. **What behavior am I trying to change?**
   213|3. **Which principle(s) apply?** (Usually authority + commitment for discipline)
   214|4. **Am I combining too many?** (Don't use all seven)
   215|5. **Is this ethical?** (Serves user's genuine interests?)
   216|