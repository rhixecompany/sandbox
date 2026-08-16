---
name: meeting-insights-analyzer-edge-cases
description: "Edge Cases & Ambiguous Situations"
version: 1.0.0
author: Alexa
---
     1|# Edge Cases & Ambiguous Situations
     2|
     3|This file handles difficult analysis scenarios where standard guidance doesn't directly apply.
     4|
     5|## Missing Speaker Labels or Labels are Ambiguous
     6|
     7|### The Problem
     8|
     9|Transcript like:
    10|
    11|```
    12|00:00:14 Speaker 1: "I think we should move the launch forward."
    13|00:00:22 Speaker 2: "That timeline seems aggressive."
    14|```
    15|
    16|No context for who Speaker 1 and Speaker 2 are. You can't analyze your own patterns without knowing which speaker is you.
    17|
    18|### What to Do
    19|
    20|**Step 1: Ask the user for context**
    21|
    22|"I see the transcript has speaker labels but no names. Can you tell me:
    23|
    24|- Who was each speaker?
    25|- Who were you in this meeting?
    26|- Or: provide a labeled transcript?"
    27|
    28|**Step 2: If context is provided, analyze with clear limitations note**
    29|
    30|"Analysis Note: Speaker identification provided by user. If speaker labels were inaccurate, pattern conclusions may be wrong."
    31|
    32|**Step 3: If speaker context is unavailable**
    33|
    34|"Unable to analyze individual patterns without speaker identification. I can provide:
    35|
    36|- Team-level patterns (meeting energy, disagreement dynamics, question frequency)
    37|- Transcript structure analysis (how the group functioned)
    38|- But NOT personal communication patterns
    39|
    40|To enable personal analysis, please provide a transcript with clear speaker labels or names."
    41|
    42|## Contradictory Patterns: "You Interrupt Frequently AND Ask a Lot of Questions"
    43|
    44|### The Problem
    45|
    46|You find:
    47|
    48|- 12 interruptions in one meeting
    49|- 18 clarifying questions
    50|- Conclusion: "You're domineering yet curious" (seems contradictory)
    51|
    52|### Analysis Strategy
    53|
    54|**Step 1: Separate self-interruptions from other-interruptions**
    55|
    56|- Count interruptions of YOUR OWN speech (you start talking, don't finish, keep going)
    57|- Count interruptions of OTHERS' speech (you cut them off)
    58|
    59|Often, high interrupt count is mostly self-interruption (thinking out loud) with few actual interruptions of others.
    60|
    61|**Report**: "12 total interruptions: 8 were self-interruptions (incomplete thoughts you finished), 4 were interruptions of others' speech. Combined with 18 clarifying questions, pattern shows: you think out loud but when others speak, you're deeply curious and listen for detail."
    62|
    63|**Step 2: Analyze timing and context**
    64|
    65|When do interruptions occur?
    66|
    67|- During YOUR explanations → self-interruption (thinking out loud)
    68|- During others' explanations → dominating pattern
    69|
    70|When do questions occur?
    71|
    72|- When you want to understand → active listening
    73|- When you're challenging → aggressive questioning
    74|
    75|These may be different patterns in different contexts, not a contradiction.
    76|
    77|**Step 3: Report the contextual variation**
    78|
    79|"Paradox resolved: In explaining your ideas, you think out loud and interrupt yourself frequently. When others are explaining, you shift into deep listening mode with many clarifying questions. This is actually good facilitation — you're making space for thinking while also staying curious about others' contributions."
    80|
    81|## No Clear Patterns Emerge
    82|
    83|### The Problem
    84|
    85|You analyzed 4 meetings looking for conflict avoidance, speaking patterns, active listening, leadership style — and found... relatively stable, consistent communication.
    86|
    87|No dramatic hedging, no extreme speaking ratios, no obvious avoidance, no dominance.
    88|
    89|**Temptation**: Report "no significant findings" and stop.
    90|
    91|**Reality**: This IS a significant finding. It's a strength profile, not a failure to analyze.
    92|
    93|### What to Do
    94|
    95|**Step 1: Reframe the lack of extremes as stability**
    96|
    97|"No conflict avoidance patterns detected. This suggests either:
    98|
    99|1. You naturally communicate directly when addressing issues
   100|2. You navigate these meetings without tension (may indicate good relationship dynamics)
   101|3. Insufficient conflict moments in these meetings to trigger avoidance patterns
   102|
   103|Recommend: Reanalyze a meeting that you know involved disagreement."
   104|
   105|**Step 2: Shift to positive pattern identification**
   106|
   107|Instead of looking for things you DON'T do, look for what you DO do:
   108|
   109|- "Moments of active listening" (questions that build on others' ideas)
   110|- "Clear communication" (few hedging words, direct statements)
   111|- "Inclusive facilitation" (inviting quieter people in)
   112|- "Collaborative decision-making" (seeking input before deciding)
   113|
   114|**Report**: "Across 4 meetings, no conflict avoidance detected. Positive patterns observed:
   115|
   116|- Asks clarifying questions consistently (average 6 per meeting)
   117|- Invites input from team members by name
   118|- Follows disagreements with direct acknowledgment
   119|- Completes action items with clear owners"
   120|
   121|**Step 3: Offer growth edge**
   122|
   123|Even stability can have developmental areas:
   124|
   125|- "Could you be more willing to take bold stances instead of always seeking consensus?"
   126|- "Could you facilitate faster in crisis moments, or do you naturally prefer collaborative?
   127|- "Are there contexts where you COULD be more direct?"
   128|
   129|This acknowledges strength while pointing to growth.
   130|
   131|## Very Long Transcripts (10+ Hour Meetings, Marathon Sessions)
   132|
   133|### The Problem
   134|
   135|Analyzing a 12-hour working session or all-hands meeting where patterns may shift dramatically over time.
   136|
   137|### What to Do
   138|
   139|**Step 1: Segment by time or topic**
   140|
   141|"This is a 12-hour meeting. I'll segment by hour (or by topic) and analyze patterns separately to account for fatigue effects."
   142|
   143|**Step 2: Track fatigue and engagement changes**
   144|
   145|- Speaking ratio hour 1 vs. hour 12 (likely drops as fatigue sets in)
   146|- Filler words increase or decrease?
   147|- Question frequency changes?
   148|- Interruption patterns change?
   149|
   150|**Report**: "Early meeting (hours 1-3): You're highly engaged, ask detailed questions, facilitate collaboratively. Late meeting (hours 10-12): You become quieter, shorter contributions, defer more to others. This pattern suggests fatigue-driven disengagement."
   151|
   152|**Step 3: Provide composite pattern**
   153|
   154|- "Overall, you show [pattern]"
   155|- "With time-of-day effect: [early pattern] that shifts to [late pattern]"
   156|- "This is normal fatigue response, not personality change"
   157|
   158|## Minimal Data (Only 1-2 Meetings)
   159|
   160|### The Problem
   161|
   162|User says "I only have 2 meetings transcribed. Can you analyze my patterns?"
   163|
   164|Patterns require data across different contexts. One or two meetings is insufficient.
   165|
   166|### What to Do
   167|
   168|**Clearly state the limitation**:
   169|
   170|"Analysis with only 2 meetings has significant limits:
   171|
   172|- Can't distinguish stable patterns from temporary effects
   173|- Context-specific behaviors might look like personality traits
   174|- One stressful meeting might be anomaly, not pattern
   175|
   176|Recommendation: Collect at least 2 additional meetings (4+ total) for reliable pattern analysis."
   177|
   178|**But provide value anyway**:
   179|
   180|"From these 2 meetings, I can note specific observations:
   181|
   182|- Meeting 1: You [behavior] when [context]. This suggests [possible pattern], but needs validation across more meetings.
   183|- Meeting 2: You [different behavior]. Possible explanations: [context variation] or [situational adaptation].
   184|
   185|For confirmed patterns, please provide 2+ additional meetings."
   186|
   187|## Conflicting Evidence: Pattern in Some Meetings, Not Others
   188|
   189|### The Problem
   190|
   191|"You avoid conflict in meetings with your boss, but not in peer meetings" — the pattern is real, but it's contextual.
   192|
   193|Not a contradiction; it's situational adaptation.
   194|
   195|### What to Do
   196|
   197|**Validate the context specificity**:
   198|
   199|- Boss meetings (power imbalance) → More hedging
   200|- Peer meetings (equal power) → More directness
   201|- Team meetings (responsibility) → More collaborative
   202|
   203|**Report the context variation explicitly**:
   204|
   205|"Conflict avoidance is situational, not personality-based:
   206|
   207|- In 1:1s with your boss: You use hedging language (maybe, kind of)
   208|- In peer strategy meetings: You're direct and name issues clearly
   209|- In team meetings: You facilitate collaboratively, encourage disagreement
   210|
   211|This suggests you're sensitive to power dynamics and adapt your communication appropriately. It's not a flaw; it's awareness of relational context."
   212|
   213|**Frame positively**:
   214|
   215|"Rather than 'conflict avoidance,' reframe as 'contextual communication adaptation.' You calibrate your directness based on the relationship and power dynamic. This is skillful."
   216|
   217|## Analysis Reveals Patterns Contrary to User's Self-Belief
   218|
   219|### The Problem
   220|
   221|User says: "I dominate meetings."
   222|
   223|But analysis shows: Relatively balanced speaking time, asks many questions, frequently defers to others.
   224|
   225|### Approach with Care
   226|
   227|**Don't immediately challenge their self-perception**:
   228|
   229|Instead, present evidence factually:
   230|
   231|"You mentioned dominating meetings. Here's what I observed:
   232|
   233|- Speaking time: 35% of meeting (participant baseline, not dominant)
   234|- Questions asked: 14 (high engagement, not dominance)
   235|- Interruptions of others: 2 (low)
   236|- Moments you suggested ideas: 4
   237|- Moments you asked for others' input: 6
   238|
   239|Pattern suggests you're collaborative and curious, not dominating.
   240|
   241|Does this match what you expected to find? If not, possible explanations:
   242|
   243|- You feel like you're dominating emotionally (took big stance on an issue)
   244|- Memory is selective (remember the moments you spoke, not the silence)
   245|- You're comparing to a baseline that's unrealistic
   246|- You dominate in other meetings (these 4 might be atypical)
   247|
   248|Let's dig deeper: Which meetings feel like you dominated? Let's analyze those specifically."
   249|
   250|**Respect their reality while offering alternative frames**:
   251|
   252|They may have accurate self-knowledge you're missing, OR they may have internalized false belief. Data helps clarify which.
   253|
   254|## Next Steps
   255|
   256|When you encounter an edge case:
   257|
   258|1. **Name the specific problem** clearly
   259|2. **State what analysis becomes possible** (and what becomes impossible)
   260|3. **Offer fallback approach** (what CAN you analyze, even with limitation?)
   261|4. **Ask clarifying questions** to the user for additional data
   262|5. **Report with explicit caveats** about what this analysis doesn't cover
   263|
   264|Honest analysis acknowledges its own limitations.
   265|