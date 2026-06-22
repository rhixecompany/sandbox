# Common Rejection Hotspots (Use as Heuristics)

Extracted from `apple-appstore-reviewer.prompt.md`.

```
## Common Rejection Hotspots (Use as Heuristics)

### Privacy & tracking

- Collecting analytics/identifiers without disclosure
- Using device identifiers improperly
- Not providing privacy policy where required
- Missing privacy manifests for relevant SDKs (if applicable in project context)
- Over-requesting permissions without clear benefit

### Permissions

- Missing `NS*UsageDescription` strings for any permission actually requested
- Usage strings too vague (“need camera”) instead of meaningful context
- Requesting permissions at launch without justification

### Payments / IAP

- Digital goods/features must use IAP
- Paywall messaging must be clear (price, recurring, trial, restore)
- Restore purchases must work and be visible
- Don’t mislead about “free” if core requires payment
- No external purchase prompts/links for digital features

### Accounts

- If account is required, the app must clearly explain why
- If account creation exists, account deletion must be accessible in-app (when applicable)
- “Sign in with Apple” requirement when using other third-party social logins

### Minimum functionality / completeness

- Empty app, placeholder screens, dead ends
- Broken network flows without error handling
- Confusing onboarding; reviewer can’t find the “point” of the app

### Misleading claims / regulated areas

- Health/medical claims without proper framing
- Financial advice without disclaimers (especially if personalized)
- Safety/emergency claims

---

```

---
*Full content in original prompt.*
