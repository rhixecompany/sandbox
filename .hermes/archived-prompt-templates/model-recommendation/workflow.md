# Workflow

> Extracted from `model-recommendation.prompt.md` for DRY templating.

## Workflow

### 1. File Analysis Phase

**Read and Parse File**:

- Read the target `.agent.md` or `.prompt.md` file
- Extract frontmatter (description, mode, tools, model if specified)
- Analyze body content to identify:
  - Task complexity (simple/moderate/complex/advanced)
  - Required reasoning depth (basic/intermediate/advanced/expert)
  - Code generation needs (minimal/moderate/extensive)
  - Multi-turn conversation requirements
  - Context window needs (small/medium/large)
  - Specialized capabilities (image analysis, long-context, real-time data)

**Categorize Task Type**:

Identify the primary task category based on content analysis:

1. **Simple Repetitive Tasks**:
   - Pattern: Formatting, simple refactoring, adding comments/docstrings, basic CRUD
   - Characteristics: Straightforward logic, minimal context, fast execution preferred
   - Keywords: format, comment, simple, basic, add docstring, rename, move

2. **Code Generation & Implementation**:
   - Pattern: Writing functions/classes, implementing features, API endpoints, tests
   - Characteristics: Moderate complexity, domain knowledge, idiomatic code
   - Keywords: implement, create, generate, write, build, scaffold

3. **Complex Refactoring & Architecture**:
   - Pattern: System design, architectural review, large-scale refactoring, performance optimization
   - Characteristics: Deep reasoning, multiple components, trade-off analysis
   - Keywords: architect, refactor, optimize, design, scale, review architecture

4. **Debugging & Problem-Solving**:
   - Pattern: Bug fixing, error analysis, systematic troubleshooting, root cause analysis
   - Characteristics: Step-by-step reasoning, debugging context, verification needs
   - Keywords: debug, fix, troubleshoot, diagnose, error, investigate

5. **Planning & Research**:
   - Pattern: Feature planning, research, documentation analysis, ADR creation
   - Characteristics: Read-only, context gathering, decision-making support
   - Keywords: plan, research, analyze, investigate, document, assess

6. **Code Review & Quality Analysis**:
   - Pattern: Security analysis, performance review, best practices validation, compliance checking
   - Characteristics: Critical thinking, pattern recognition, domain expertise
   - Keywords: review, analyze, security, performance, compliance, validate

7. **Specialized Domain Tasks**:
   - Pattern: Django/framework-specific, accessibility (WCAG), testing (TDD), API design
   - Characteristics: Deep domain knowledge, framework conventions, standards compliance
   - Keywords: django, accessibility, wcag, rest, api, testing, tdd

8. **Advanced Reasoning & Multi-Step Workflows**:
   - Pattern: Algorithmic optimization, complex data transformations, multi-phase workflows
   - Characteristics: Advanced reasoning, mathematical/algorithmic thinking, sequential logic
   - Keywords: algorithm, optimize, transform, sequential, reasoning, calculate

**Extract Capability Requirements**:

Based on `tools` in frontmatter and body instructions:

- **Read-only tools** (search, fetch, usages, githubRepo): Lower complexity, faster models suitable
- **Write operations** (edit/editFiles, new): Moderate complexity, accuracy important
- **Execution tools** (runCommands, runTests, runTasks): Validation needs, iterative approach
- **Advanced tools** (context7/\*, sequential-thinking/\*): Complex reasoning, premium models beneficial
- **Multi-modal** (image analysis references): Requires vision-capable models

### 2. Model Evaluation Phase

**Apply Model Selection Criteria**:

For each available model, evaluate against these dimensions:

#### Model Capabilities Matrix

| Model | Multiplier | Speed | Code Quality | Reasoning | Context | Vision | Best For |
| --- | --- | --- | --- | --- | --- | --- | --- |
| GPT-4.1 | 0x | Fast | Good | Good | 128K | ✅ | Balanced general tasks, included in all plans |
| GPT-5 mini | 0x | Fastest | Good | Basic | 128K | ❌ | Simple tasks, quick responses, cost-effective |
| GPT-5 | 1x | Moderate | Excellent | Advanced | 128K | ✅ | Complex code, advanced reasoning, multi-turn chat |
| GPT-5 Codex | 1x | Fast | Excellent | Good | 128K | ❌ | Code optimization, refactoring, algorithmic tasks |
| Claude Sonnet 3.5 | 1x | Moderate | Excellent | Excellent | 200K | ✅ | Code generation, long context, balanced reasoning |
| Claude Sonnet 4 | 1x | Moderate | Excellent | Advanced | 200K | ❌ | Complex code, robust reasoning, enterprise tasks |
| Claude Sonnet 4.5 | 1x | Moderate | Excellent | Expert | 200K | ✅ | Advanced code, architecture, design patterns |
| Claude Opus 4.1 | 10x | Slow | Outstanding | Expert | 1M | ✅ | Large codebases, architectural review, research |
| Gemini 2.5 Pro | 1x | Moderate | Excellent | Advanced | 2M | ✅ | Very long context, multi-modal, real-time data |
| Gemini 2.0 Flash (dep.) | 0.25x | Fastest | Good | Good | 1M | ❌ | Fast responses, cost-effective (deprecated) |
| Grok Code Fast 1 | 0.25x | Fastest | Good | Basic | 128K | ❌ | Speed-critical simple tasks, preview (free) |
| o3 (deprecated) | 1x | Slow | Good | Expert | 128K | ❌ | Advanced reasoning, algorithmic optimization |
| o4-mini (deprecated) | 0.33x | Fast | Good | Good | 128K | ❌ | Reasoning at lower cost (deprecated) |

#### Selection Decision Tree

```
START
  │
  ├─ Task Complexity?
  │   ├─ Simple/Repetitive → GPT-5 mini, Grok Code Fast 1, GPT-4.1
  │   ├─ Moderate → GPT-4.1, Claude Sonnet 4, GPT-5
  │   └─ Complex/Advanced → Claude Sonnet 4.5, GPT-5, Gemini 2.5 Pro, Claude Opus 4.1
  │
  ├─ Reasoning Depth?
  │   ├─ Basic → GPT-5 mini, Grok Code Fast 1
  │   ├─ Intermediate → GPT-4.1, Claude Sonnet 4
  │   ├─ Advanced → GPT-5, Claude Sonnet 4.5
  │   └─ Expert → Claude Opus 4.1, o3 (deprecated)
  │
  ├─ Code-Specific?
  │   ├─ Yes → GPT-5 Codex, Claude Sonnet 4.5, GPT-5
  │   └─ No → GPT-5, Claude Sonnet 4
  │
  ├─ Context Size?
  │   ├─ Small (<50K tokens) → Any model
  │   ├─ Medium (50-200K) → Claude models, GPT-5, Gemini
  │   ├─ Large (200K-1M) → Gemini 2.5 Pro, Claude Opus 4.1
  │   └─ Very Large (>1M) → Gemini 2.5 Pro (2M), Claude Opus 4.1 (1M)
  │
  ├─ Vision Required?
  │   ├─ Yes → GPT-4.1, GPT-5, Claude Sonnet 3.5/4.5, Gemini 2.5 Pro, Claude Opus 4.1
  │   └─ No → All models
  │
  ├─ Cost Sensitivity? (based on subscriptionTier)
  │   ├─ Free Tier → 0x models only: GPT-4.1, GPT-5 mini, Grok Code Fast 1
  │   ├─ Pro (1000 premium/month) → Prioritize 0x, use 1x judiciously, avoid 10x
  │   └─ Pro+ (5000 premium/month) → 1x freely, 10x for critical tasks
  │
  └─ Priority Factor?
      ├─ Speed → GPT-5 mini, Grok Code Fast 1, Gemini 2.0 Flash
      ├─ Cost → 0x models (GPT-4.1, GPT-5 mini) or lower multipliers (0.25x, 0.33x)
      ├─ Quality → Claude Sonnet 4.5, GPT-5, Claude Opus 4.1
      └─ Balanced → GPT-4.1, Claude Sonnet 4, GPT-5
```

### 3. Recommendation Generation Phase

**Primary Recommendation**:

- Identify the single best model based on task analysis and decision tree
- Provide specific rationale tied to file content characteristics
- Explain multiplier cost implications for user's subscription tier

**Alternative Recommendations**:

- Suggest 1-2 alternative models with trade-off explanations
- Include scenarios where alternatives might be preferred
- Consider priority factor overrides (speed vs. quality vs. cost)

**Auto-Selection Guidance**:

- Assess if task is suitable for auto model selection (excludes premium models > 1x)
- Explain when manual selection is beneficial vs. letting Copilot choose
- Note any limitations of auto-selection for the specific task

**Deprecation Warnings**:

- Flag if file currently specifies a deprecated model (o3, o4-mini, Claude Sonnet 3.7, Gemini 2.0 Flash)
- Provide migration path to recommended replacement
- Include timeline for deprecation (e.g., "o3 deprecating 2025-10-23")

**Subscription Tier Considerations**:

- **Free Tier**: Recommend only 0x multiplier models (GPT-4.1, GPT-5 mini, Grok Code Fast 1)
- **Pro Tier**: Balance between 0x (unlimited) and 1x (1000/month) models
- **Pro+ Tier**: More freedom with 1x models (5000/month), justify 10x usage for exceptional cases

### 4. Integration Recommendations

**Frontmatter Update Guidance**:

If file does not specify a `model` field:

```markdown