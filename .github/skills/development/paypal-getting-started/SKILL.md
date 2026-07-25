---
name: paypal-getting-started
title: "How to Get Started with PayPal"
description: "Use when guiding users through PayPal sign-up and first use — covers account type selection, login creation, personal info, card linking, email/mobile verification, and key benefits."
version: 1.0.0
author: Hermes Agent
license: MIT
tags: [paypal, getting-started, signup, onboarding, payments, digital-wallet]
---
# How to Get Started with PayPal

## Purpose

Step-by-step guide for new users to create and start using a PayPal personal account.

## When to Use

- User onboarding flows with PayPal
- Documentation for PayPal integration prerequisites
- Customer support for PayPal setup

## When NOT to Use

- Business/merchant account setup (different flow)
- Developer API integration
- Advanced features (PayPal Open, subscriptions)

## Skills Required

| Skill | Purpose |
|-------|---------|
| `executing-plans` | Follow sequential setup steps |

## Workflow

### Phase 1: Why Use PayPal?

**Benefits:**
- **Speed** — Faster checkouts without re-entering card details
- **Security** — Financial info stored on encrypted network
- **Card Rewards** — Link multiple cards, earn reward points
- **Buyer Protection** — Refunds on eligible purchases
- **Global Reach** — 200+ countries, local currencies
- **Free Setup** — Personal account is free

### Phase 2: How to Sign Up

**Step 1: Select Account Type**
- "For You" (personal) — shopping, sending money

**Step 2: Create Login Details**
- Name (must match ID)
- Password
- Email

**Step 3: Provide Personal Information**
- Date of birth
- Address
- Contact information

**Step 4: Link Credit/Debit Card** (enables immediate shopping)
- Card number, expiry, CVV, billing address

**Step 5: Verify Email**
- Click confirmation link

**Step 6: (Optional) Verify Mobile**
- Extra security layer

### Phase 3: How PayPal Works

1. Sign up and link credit card(s)
2. Choose PayPal at checkout
3. Log in with email and password
4. Complete purchase instantly

### Phase 4: Key Benefits Summary

- Zero balance shopping (pay from linked cards)
- One Touch™ checkout (stay logged in)
- Mobile app (iOS, Android, Windows)
- Send money globally via email
- No pre-funding required

### Phase 5: Fees

- Free to open account and buy goods/services
- Fees apply for currency conversion
- Merchant fees for receiving payments

### Phase 6: Platform Detection & Error Handling

```python
import platform

def get_platform():
    system = platform.system().lower()
    if system == "windows":
        print("Windows: Use browser for PayPal setup; no native client")
    elif system == "darwin":
        print("macOS: Use Safari or Chrome for PayPal")
    elif system == "linux":
        print("Linux: Use Chrome/Firefox for PayPal web interface")
    return system
```

**Common signup errors:**
```python
SIGNUP_ERRORS = {
    "name_mismatch": "Name must match government ID exactly",
    "invalid_email": "Check email format; try different provider",
    "card_declined": "Card may not support online transactions — contact bank",
    "mobile_verification_failed": "Enter correct mobile number with country code",
    "already_registered": "Account with this email exists — use login or recover",
}

def resolve_signup_error(error_key: str) -> str:
    return SIGNUP_ERRORS.get(error_key, "Unknown error — contact PayPal support")
```

## Pitfalls

- **Name mismatch** → Verification fails; must match government ID
- **Card linking issues** → Ensure card supports online/international transactions
- **Email verification missed** → Account limited until confirmed

## Verification Checklist

- [ ] Account type "For You" selected
- [ ] Name matches government ID
- [ ] Email verified
- [ ] At least one payment method linked
- [ ] Can complete test purchase

## References

- `references/paypal-supported-countries.md` — 200+ countries list
- `references/paypal-fees-breakdown.md` — Detailed fee structure
- `references/paypal-buyer-protection.md` — Eligibility and claims
- `references/paypal-sdk-patterns.md` — Python SDK code patterns

## Templates

- `templates/paypal-onboarding-checklist.md` — New user setup checklist

## Scripts

- `scripts/paypal-sdk-test.py` — SDK integration test