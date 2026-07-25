# Paystack Dashboard Guide

## Navigation

| Section | Purpose |
|---------|---------|
| **Dashboard** | Overview of transactions, revenue, customers |
| **Transactions** | View, filter, export all transactions |
| **Customers** | Customer management, view history |
| **Products** | Create/manage products for checkout |
| **Payment Pages** | No-code payment links |
| **Subscriptions** | Recurring billing management |
| **Transfers** | Payouts to bank accounts |
| **Reports** | Financial reports, settlements |
| **Settings** | API keys, webhooks, team, business info |

## API Keys

```
Settings → API Keys & Webhooks
- Test Secret Key: sk_test_xxx (sandbox only)
- Test Public Key: pk_test_xxx (sandbox only)
- Live Secret Key: sk_live_xxx (production)
- Live Public Key: pk_live_xxx (production)
```

## Webhooks

```
Settings → API Keys & Webhooks → Webhooks
- Add webhook URL
- Select events: charge.success, transfer.success, etc.
- Secret hash for verification
```

## Test Transactions

Use test cards:
- Success: 4084 0840 8408 4081
- Decline: 4000 0000 0000 0002
- 3D Secure: 4000 0000 0000 3055