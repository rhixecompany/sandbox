---
name: humanizer-patterns-reference
description: "Pattern Reference: 24 AI Writing Anti-Patterns"
version: 1.0.0
author: Alexa
---
     1|# Pattern Reference: 24 AI Writing Anti-Patterns
     2|
     3|**MANDATORY — Read this entire file when identifying which specific AI writing patterns are present in your text.**
     4|
     5|This file documents all 24 patterns with decision trees and examples. Use this as your diagnostic guide when humanizing text.
     6|
     7|---
     8|
     9|## CONTENT PATTERNS (Patterns 1–6)
    10|
    11|These patterns inflate importance, exaggerate notability, or use superficial analysis.
    12|
    13|### Pattern 1: Undue Emphasis on Significance, Legacy, and Broader Trends
    14|
    15|**Trigger words**: stands/serves as, is a testament/reminder, a vital/significant/crucial/pivotal/key role/moment, underscores/highlights its importance/significance, reflects broader, symbolizing its ongoing/enduring/lasting, contributing to the, setting the stage for, marking/shaping the, represents/marks a shift, key turning point, evolving landscape, focal point, indelible mark, deeply rooted
    16|
    17|**Problem**: LLM writing puffs up importance by adding statements about how arbitrary aspects represent or contribute to a broader topic.
    18|
    19|**Decision Tree**:
    20|
    21|1. Does the text claim something "marks a pivotal moment" or "shapes the landscape"?
    22|2. Is there a claim about "broader trends" or "lasting significance" that's unsupported?
    23|3. Are simple facts dressed up as historical importance?
    24|
    25|**Example**:
    26|
    27|```
    28|Before: The Statistical Institute of Catalonia was officially established in 1989,
    29|marking a pivotal moment in the evolution of regional statistics in Spain. This
    30|initiative was part of a broader movement across Spain to decentralize administrative
    31|functions and enhance regional governance.
    32|
    33|After: The Statistical Institute of Catalonia was established in 1989 to collect
    34|and publish regional statistics independently from Spain's national statistics office.
    35|```
    36|
    37|**Why it's AI**: Machine learning models assign high probability to sentences that connect isolated facts to grand narratives. Humans often just state facts.
    38|
    39|---
    40|
    41|### Pattern 2: Undue Emphasis on Notability and Media Coverage
    42|
    43|**Trigger words**: independent coverage, local/regional/national media outlets, written by a leading expert, active social media presence, featured in, covered by, widely recognized, prominently featured
    44|
    45|**Problem**: LLMs hit readers over the head with claims of notability, often listing sources without context.
    46|
    47|**Decision Tree**:
    48|
    49|1. Does the text list media outlets without explaining WHY they matter?
    50|2. Is notability asserted ("active social media presence") rather than supported?
    51|3. Are citations used to justify importance rather than inform?
    52|
    53|**Example**:
    54|
    55|```
    56|Before: Her views have been cited in The New York Times, BBC, Financial Times,
    57|and The Hindu. She maintains an active social media presence with over 500,000 followers.
    58|
    59|After: In a 2024 New York Times interview, she argued that AI regulation should
    60|focus on outcomes rather than methods.
    61|```
    62|
    63|**Why it's AI**: LLMs generate "notability statements" as filler. Humans cite specific claims, not just outlets.
    64|
    65|---
    66|
    67|### Pattern 3: Superficial Analyses with -ing Endings
    68|
    69|**Trigger words**: highlighting/underscoring/emphasizing..., ensuring..., reflecting/symbolizing..., contributing to..., cultivating/fostering..., encompassing..., showcasing..., revealing...
    70|
    71|**Problem**: AI chatbots tack present participle ("-ing") phrases onto sentences to add fake depth.
    72|
    73|**Decision Tree**:
    74|
    75|1. Are there multiple "-ing" phrases strung together in one sentence?
    76|2. Do the "-ing" phrases restate what was just said (fake analysis)?
    77|3. Could the sentence be clearer without the "-ing" phrases?
    78|
    79|**Example**:
    80|
    81|```
    82|Before: The temple's color palette of blue, green, and gold resonates with the
    83|region's natural beauty, symbolizing Texas bluebonnets, the Gulf of Mexico, and
    84|the diverse Texan landscapes, reflecting the community's deep connection to the land.
    85|
    86|After: The temple uses blue, green, and gold colors. The architect said these
    87|were chosen to reference local bluebonnets and the Gulf coast.
    88|```
    89|
    90|**Why it's AI**: LLMs overuse "-ing" forms to add apparent depth. This pattern correlates heavily with post-2023 text.
    91|
    92|---
    93|
    94|### Pattern 4: Promotional and Advertisement-like Language
    95|
    96|**Trigger words**: boasts a, vibrant, rich (figurative), profound, enhancing its, showcasing, exemplifies, commitment to, natural beauty, nestled, in the heart of, groundbreaking (figurative), renowned, breathtaking, must-visit, stunning, iconic, picturesque, charming, heritage
    97|
    98|**Problem**: LLMs have serious problems keeping a neutral tone, especially for "cultural heritage" topics. They default to promotional language.
    99|
   100|**Decision Tree**:
   101|
   102|1. Would a travel brochure use this language?
   103|2. Are adjectives doing the work that facts should do?
   104|3. Could this be rewritten with fewer modifiers and more specifics?
   105|
   106|**Example**:
   107|
   108|```
   109|Before: Nestled within the breathtaking region of Gonder in Ethiopia, Alamata
   110|Raya Kobo stands as a vibrant town with a rich cultural heritage and stunning
   111|natural beauty.
   112|
   113|After: Alamata Raya Kobo is a town in the Gonder region of Ethiopia, known for
   114|its weekly market and 18th-century church.
   115|```
   116|
   117|**Why it's AI**: Marketing language is statistically overrepresented in training data. LLMs default to it when uncertain about tone.
   118|
   119|---
   120|
   121|### Pattern 5: Vague Attributions and Weasel Words
   122|
   123|**Trigger words**: Industry reports, Observers have cited, Experts argue, Some critics argue, Several sources/publications (when few cited), It is believed, Research suggests, Generally considered, It is widely held that
   124|
   125|**Problem**: AI chatbots attribute opinions to vague authorities without specific sources.
   126|
   127|**Decision Tree**:
   128|
   129|1. Who exactly are the "experts"? Can you name one?
   130|2. Does "industry reports" point to actual reports?
   131|3. Would a reader find the specific source if they searched?
   132|
   133|**Example**:
   134|
   135|```
   136|Before: Due to its unique characteristics, the Haolai River is of interest to
   137|researchers and conservationists. Experts believe it plays a crucial role in the
   138|regional ecosystem.
   139|
   140|After: The Haolai River supports several endemic fish species, according to a
   141|2019 survey by the Chinese Academy of Sciences.
   142|```
   143|
   144|**Why it's AI**: Vague attribution allows the LLM to continue without fetching real data. Humans cite when they know; they're specific.
   145|
   146|---
   147|
   148|### Pattern 6: Outline-like "Challenges and Future Prospects" Sections
   149|
   150|**Trigger words**: Despite its... faces several challenges..., Despite these challenges, Challenges and Legacy, Future Outlook, It remains to be seen, Looking ahead, In the coming years, As the field evolves
   151|
   152|**Problem**: Many LLM-generated articles include formulaic "Challenges" sections that repeat the intro without adding information.
   153|
   154|**Decision Tree**:
   155|
   156|1. Is there a "Challenges" section that doesn't exist in the source?
   157|2. Does it repeat problems already mentioned?
   158|3. Are "future prospects" vague (e.g., "will continue to grow")?
   159|
   160|**Example**:
   161|
   162|```
   163|Before: Despite its industrial prosperity, Korattur faces challenges typical of
   164|urban areas, including traffic congestion and water scarcity. Despite these challenges,
   165|with its strategic location and ongoing initiatives, Korattur continues to thrive as
   166|an integral part of Chennai's growth.
   167|
   168|After: Traffic congestion increased after 2015 when three new IT parks opened.
   169|The municipal corporation began a stormwater drainage project in 2022 to address
   170|recurring floods.
   171|```
   172|
   173|**Why it's AI**: Outline structure is common in training data. LLMs fill sections mechanically rather than with new information.
   174|
   175|---
   176|
   177|## LANGUAGE AND GRAMMAR PATTERNS (Patterns 7–12)
   178|
   179|These patterns involve vocabulary, grammar, and sentence construction.
   180|
   181|### Pattern 7: Overused "AI Vocabulary" Words
   182|
   183|**High-frequency AI words**: Additionally, align with, crucial, delve, emphasizing, enduring, enhance, fostering, garner, highlight (verb), interplay, intricate/intricacies, key (adjective), landscape (abstract noun), pivotal, showcase, tapestry (abstract noun), testament, underscore (verb), valuable, vibrant
   184|
   185|**Problem**: These words appear far more frequently in post-2023 text and often co-occur, signaling AI authorship.
   186|
   187|**Decision Tree**:
   188|
   189|1. Count instances of words in the "High-frequency AI words" list
   190|2. Do 3+ appear in a single paragraph?
   191|3. Do they co-occur (e.g., "pivotal landscape" or "testament to the landscape")?
   192|
   193|**Example**:
   194|
   195|```
   196|Before: Additionally, a distinctive feature of Somali cuisine is the incorporation
   197|of camel meat. An enduring testament to Italian colonial influence is the widespread
   198|adoption of pasta in the local culinary landscape, showcasing how these dishes have
   199|integrated into the traditional diet.
   200|
   201|After: Somali cuisine also includes camel meat, which is considered a delicacy.
   202|Pasta dishes, introduced during Italian colonization, remain common, especially in
   203|the south.
   204|```
   205|
   206|**Why it's AI**: LLM training data overweights academic/professional text. These words are common in that genre and get overused statistically.
   207|
   208|---
   209|
   210|### Pattern 8: Avoidance of "is"/"are" (Copula Avoidance)
   211|
   212|**Trigger words**: serves as/stands as/marks/represents [a], boasts/features/offers [a], comprises, constitutes, demonstrates, functions as
   213|
   214|**Problem**: LLMs substitute elaborate constructions for simple copulas.
   215|
   216|**Decision Tree**:
   217|
   218|1. Does the sentence use "serves as" or "stands as" where "is" would work?
   219|2. Could "boasts" be replaced with "has"?
   220|3. Is the elaborate form making the sentence harder to parse?
   221|
   222|**Example**:
   223|
   224|```
   225|Before: Gallery 825 serves as LAAA's exhibition space for contemporary art.
   226|The gallery features four separate spaces and boasts over 3,000 square feet.
   227|
   228|After: Gallery 825 is LAAA's exhibition space for contemporary art. The gallery
   229|has four rooms totaling 3,000 square feet.
   230|```
   231|
   232|**Why it's AI**: Copula avoidance is a known LLM quirk. Models treat "is" as too simple and substitute longer forms.
   233|
   234|---
   235|
   236|### Pattern 9: Negative Parallelisms
   237|
   238|**Trigger words**: It's not just about..., it's...; Not only...but...; It's not merely..., it's...; Rather than...instead...
   239|
   240|**Problem**: Constructions like "Not only...but..." are overused by LLMs.
   241|
   242|**Decision Tree**:
   243|
   244|1. Count instances of "It's not just..." or "Not only...but..." in the text
   245|2. Are multiple negative parallelisms present?
   246|3. Could the same idea be stated more directly?
   247|
   248|**Example**:
   249|
   250|```
   251|Before: It's not just about the beat riding under the vocals; it's part of the
   252|aggression and atmosphere. It's not merely a song, it's a statement.
   253|
   254|After: The heavy beat adds to the aggressive tone.
   255|```
   256|
   257|**Why it's AI**: LLMs overuse this structure because it's statistically common in persuasive text. Humans prefer direct statements.
   258|
   259|---
   260|
   261|### Pattern 10: Rule of Three Overuse
   262|
   263|**Trigger words**: Comma lists of exactly 3 items; Three "-ing" forms; Three adjectives in a row; Phrases like "A, B, and C"
   264|
   265|**Problem**: LLMs force ideas into groups of three to appear comprehensive (and because it's over-represented in training data).
   266|
   267|**Decision Tree**:
   268|
   269|1. Are ideas grouped into exactly 3 items when 2 or 4 would be more natural?
   270|2. Are three adjectives modifying the same noun?
   271|3. Does the grouping serve a purpose or just feel formulaic?
   272|
   273|**Example**:
   274|
   275|```
   276|Before: The event features keynote sessions, panel discussions, and networking
   277|opportunities. Attendees can expect innovation, inspiration, and industry insights.
   278|
   279|After: The event includes talks and panels. There's also time for informal
   280|networking between sessions.
   281|```
   282|
   283|**Why it's AI**: Rule of three is over-represented in rhetoric and training data. Humans naturally use variable list sizes.
   284|
   285|---
   286|
   287|### Pattern 11: Elegant Variation (Synonym Cycling)
   288|
   289|**Trigger words**: Look for the same concept using different terms: protagonist/character/hero/figure; company/organization/firm; city/metropolis/urban center; river/waterway/water body
   290|
   291|**Problem**: AI has repetition-penalty code causing excessive synonym substitution.
   292|
   293|**Decision Tree**:
   294|
   295|1. Is the same concept referred to by 4+ different terms?
   296|2. Does varying the term add clarity or just avoid repetition?
   297|3. Would repeating the original term be clearer?
   298|
   299|**Example**:
   300|
   301|```
   302|Before: The protagonist faces many challenges. The main character must overcome
   303|obstacles. The central figure eventually triumphs. The hero returns home.
   304|
   305|After: The protagonist faces many challenges but eventually triumphs and returns home.
   306|```
   307|
   308|**Why it's AI**: Modern LLMs have repetition penalties built in, causing them to over-vary synonyms. Humans repeat key terms for clarity.
   309|
   310|---
   311|
   312|### Pattern 12: False Ranges
   313|
   314|**Trigger words**: from X to Y, spanning from, ranging from, stretching from (where X and Y aren't on a continuous scale)
   315|
   316|**Problem**: LLMs use "from X to Y" constructions where X and Y aren't actually on a meaningful scale.
   317|
   318|**Decision Tree**:
   319|
   320|1. Does the "from X to Y" construction describe a continuous range?
   321|2. Or is it just two loosely related concepts forced into parallel?
   322|3. Would listing them separately be clearer?
   323|
   324|**Example**:
   325|
   326|```
   327|Before: Our journey through the universe has taken us from the singularity of
   328|the Big Bang to the grand cosmic web, from the birth and death of stars to the
   329|enigmatic dance of dark matter.
   330|
   331|After: The book covers the Big Bang, star formation, and current theories about dark matter.
   332|```
   333|
   334|**Why it's AI**: LLMs overuse "from...to" because it's a productive pattern in training data. It often creates false equivalence.
   335|
   336|---
   337|
   338|## STYLE PATTERNS (Patterns 13–18)
   339|
   340|These patterns involve formatting, punctuation, and visual presentation.
   341|
   342|### Pattern 13: Em Dash Overuse
   343|
   344|**Trigger**: Count em dashes (—) in a paragraph. LLM text typically has 2–3+ per paragraph where human text has 0–1.
   345|
   346|**Problem**: LLMs use em dashes (—) more than humans, mimicking "punchy" sales writing.
   347|
   348|**Decision Tree**:
   349|
   350|1. Are there 2+ em dashes in a single paragraph?
   351|2. Could a comma, semicolon, or period replace the em dash?
   352|3. Does the em dash add emphasis or just break up the sentence?
   353|
   354|**Example**:
   355|
   356|```
   357|Before: The term is primarily promoted by Dutch institutions—not by the people
   358|themselves. You don't say "Netherlands, Europe" as an address—yet this mislabeling
   359|continues—even in official documents.
   360|
   361|After: The term is primarily promoted by Dutch institutions, not by the people
   362|themselves. You don't say "Netherlands, Europe" as an address, yet this mislabeling
   363|continues in official documents.
   364|```
   365|
   366|**Why it's AI**: Sales copy and persuasive writing (over-represented in training data) overuse em dashes. LLMs mimic this style.
   367|
   368|---
   369|
   370|### Pattern 14: Overuse of Boldface
   371|
   372|**Trigger**: Count bold phrases. 3+ bold phrases in a short section signals AI text.
   373|
   374|**Problem**: AI chatbots emphasize phrases in boldface mechanically without regard for readability.
   375|
   376|**Decision Tree**:
   377|
   378|1. Count bold phrases in a section
   379|2. Are they emphasizing key terms or just highlighting randomly?
   380|3. Would the text be clearer without the bold?
   381|
   382|**Example**:
   383|
   384|```
   385|Before: It blends **OKRs (Objectives and Key Results)**, **KPIs (Key Performance
   386|Indicators)**, and visual strategy tools such as the **Business Model Canvas (BMC)**
   387|and **Balanced Scorecard (BSC)**.
   388|
   389|After: It blends OKRs, KPIs, and visual strategy tools like the Business Model
   390|Canvas and Balanced Scorecard.
   391|```
   392|
   393|**Why it's AI**: Markdown formatting is common in chatbot outputs. LLMs use bold to indicate importance without stylistic judgment.
   394|
   395|---
   396|
   397|### Pattern 15: Inline-Header Vertical Lists
   398|
   399|**Trigger**: Look for lists where each item starts with a bold label followed by a colon and explanation.
   400|
   401|**Problem**: AI outputs lists where items start with bolded headers followed by colons, creating artificial structure.
   402|
   403|**Decision Tree**:
   404|
   405|1. Does each list item start with **Bold Label:**?
   406|2. Are the explanations just rephrasing the label?
   407|3. Would a simpler list or prose paragraph work better?
   408|
   409|**Example**:
   410|
   411|```
   412|Before:
   413|- **User Experience:** The user experience has been significantly improved with a new interface.
   414|- **Performance:** Performance has been enhanced through optimized algorithms.
   415|- **Security:** Security has been strengthened with end-to-end encryption.
   416|
   417|After: The update improves the interface, speeds up load times through optimized
   418|algorithms, and adds end-to-end encryption.
   419|```
   420|
   421|**Why it's AI**: This structure is common in chatbot outputs because it's easy to generate. Humans use varied list formats.
   422|
   423|---
   424|
   425|### Pattern 16: Title Case in Headings
   426|
   427|**Trigger**: Look for headings where every main word is capitalized.
   428|
   429|**Problem**: AI chatbots capitalize all main words in headings (Title Case), which is becoming less standard in professional writing.
   430|
   431|**Decision Tree**:
   432|
   433|1. Is every main word capitalized (Title Case)?
   434|2. Is the document's style guide unclear or flexible?
   435|3. Would sentence case (capitalize first word only) be more modern?
   436|
   437|**Example**:
   438|
   439|```
   440|Before: ## Strategic Negotiations And Global Partnerships
   441|
   442|After: ## Strategic negotiations and global partnerships
   443|```
   444|
   445|**Why it's AI**: LLMs default to Title Case because it's over-represented in training data (titles, headers). Modern style guides prefer sentence case.
   446|
   447|---
   448|
   449|### Pattern 17: Emojis
   450|
   451|**Trigger**: Presence of emojis in headings or bullet points.
   452|
   453|**Problem**: AI chatbots often decorate headings or bullet points with emojis mechanically.
   454|
   455|**Decision Tree**:
   456|
   457|1. Are emojis present in headings or formal sections?
   458|2. Do they add meaning or just visual noise?
   459|3. Would the text be clearer without them?
   460|
   461|**Example**:
   462|
   463|```
   464|Before: 🚀 **Launch Phase:** The product launches in Q3
   465|💡 **Key Insight:** Users prefer simplicity
   466|✅ **Next Steps:** Schedule follow-up meeting
   467|
   468|After: The product launches in Q3. User research showed a preference for
   469|simplicity. Next step: schedule a follow-up meeting.
   470|```
   471|
   472|**Why it's AI**: Emojis are overused in chatbot outputs for visual appeal. Professional writing uses them rarely.
   473|
   474|---
   475|
   476|### Pattern 18: Curly Quotation Marks
   477|
   478|**Trigger**: Presence of curly quotes ("...") instead of straight quotes ("...").
   479|
   480|**Problem**: ChatGPT uses curly quotes ("...") instead of straight quotes ("..."), which is non-standard for code and technical writing.
   481|
   482|**Decision Tree**:
   483|
   484|1. Are quotation marks curved/curly ("...") instead of straight ("")?
   485|2. Is this a technical document where straight quotes are required?
   486|3. Should all quotes be converted for consistency?
   487|
   488|**Example**:
   489|
   490|```
   491|Before: He said "the project is on track" but others disagreed.
   492|
   493|After: He said "the project is on track" but others disagreed.
   494|```
   495|
   496|**Why it's AI**: ChatGPT's formatting model generates curly quotes by default. Proper technical writing uses straight quotes.
   497|
   498|---
   499|
   500|## COMMUNICATION PATTERNS (Patterns 19–21)
   501|