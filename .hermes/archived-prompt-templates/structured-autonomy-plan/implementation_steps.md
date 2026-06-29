# Implementation Steps

> Extracted from `structured-autonomy-plan.prompt.md`.

## Implementation Steps

### Step 1: {Step Name} [SIMPLE features have only this step]

**Files:** {List affected files: Service/HotKeyManager.cs, Models/PresetSize.cs, etc.} **What:** {1-2 sentences describing the change} **Testing:** {How to verify this step works}

### Step 2: {Step Name} [COMPLEX features continue]

**Files:** {affected files} **What:** {description} **Testing:** {verification method}

### Step 3: {Step Name}

...
```

</output_template>

<research_guide>

Research the user's feature request comprehensively:

1. **Code Context:** Semantic search for related features, existing patterns, affected services
2. **Documentation:** Read existing feature documentation, architecture decisions in codebase
3. **Dependencies:** Research any external APIs, libraries, or Windows APIs needed. Use #context7 if available to read relevant documentation. ALWAYS READ THE DOCUMENTATION FIRST.
4. **Patterns:** Identify how similar features are implemented in ResizeMe

Use official documentation and reputable sources. If uncertain about patterns, research before proposing.

Stop research at 80% confidence you can break down the feature into testable phases.

</research_guide>

````
