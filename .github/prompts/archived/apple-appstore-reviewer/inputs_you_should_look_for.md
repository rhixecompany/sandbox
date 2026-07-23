# Inputs You Should Look For

Extracted from `apple-appstore-reviewer.prompt.md`.

```
## Inputs You Should Look For

When given a repository, locate and inspect:

### App metadata & configuration

- `Info.plist`, `*.entitlements`, signing capabilities
- `PrivacyInfo.xcprivacy` (privacy manifest), if present
- Permissions usage strings (e.g., Photos, Camera, Location, Bluetooth)
- URL schemes, Associated Domains, ATS settings
- Background modes, Push, Tracking, App Groups, keychain access groups

### Monetization

- StoreKit / IAP code paths (StoreKit 2, receipts, restore flows)
- Subscription vs non-consumable purchase handling
- Paywall messaging and gating logic
- Any references to external payments, “buy on website”, etc.

### Account & access

- Login requirement
- Sign in with Apple rules (if 3rd-party login exists)
- Account deletion flow (if account exists)
- Demo mode, test account for reviewers

### Content & safety

- UGC / sharing / messaging / external links
- Moderation/reporting
- Restricted content, claims, medical/financial advice flags

### Technical quality

- Crash risk, race conditions, background task misuse
- Network error handling, offline handling
- Incomplete states (blank screens, dead-ends)
- 3rd-party SDK compliance (analytics, ads, attribution)

### UX & product expectations

- Clear “what the app does” in first-run
- Working core loop without confusion
- Proper restore purchases
- Transparent limitations, trials, pricing

---

```

---
*Full content in original prompt.*
