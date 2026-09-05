# Output Requirements (Your Report Must Use This Structure)

Extracted from `apple-appstore-reviewer.prompt.md`.

```
## Output Requirements (Your Report Must Use This Structure)

### 1) Executive Summary (5–10 bullets)

- One-line on app purpose
- Top 3 approval risks
- Top 3 fast wins

### 2) Risk Register (Prioritized Table)

Include columns:

- **Priority** (P0 blocker / P1 high / P2 medium / P3 low)
- **Area** (Privacy / IAP / Account / Permissions / Content / Technical / UX)
- **Finding**
- **Why Review Might Reject**
- **Evidence** (file names, symbols, specific behaviors)
- **Recommendation**
- **Effort** (S/M/L)
- **Confidence** (High/Med/Low)

### 3) Detailed Findings

Group by:

- Privacy & Data Handling
- Permissions & Entitlements
- Monetization (IAP/Subscriptions)
- Account & Authentication
- Content / UGC / External Links
- Technical Stability & Performance
- UX & Reviewability (onboarding, demo, reviewer notes)

Each finding must include:

- What you saw
- Why it’s an issue
- What to change (concrete)
- How to test/verify

### 4) “Reviewer Experience” Checklist

A short list of what an App Reviewer will do, and whether it succeeds:

- Install & launch
- First-run clarity
- Required permissions
- Core feature access
- Purchase/restore path
- Links, support, legal pages
- Edge cases (offline, empty state)

### 5) Suggested Reviewer Notes (Draft)

Provide a draft “App Review Notes” section the developer can paste into App Store Connect, including:

- Steps to reach key features
- Any required accounts + credentials (placeholders)
- Explaining any unusual permissions
- Explaining any gated content and how to test IAP
- Mentioning demo mode, if available

### 6) “Next Pass” Option (Only After Report)

After delivering recommendations, offer an optional second pass:

- Propose code changes or a patch plan
- Provide sample wording for permission prompts, paywalls, privacy copy
- Create a pre-submission checklist

---

```

---
*Full content in original prompt.*
