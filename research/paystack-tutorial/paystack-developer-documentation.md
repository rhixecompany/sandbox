# Paystack Developer Documentation

> **Source:** https://paystack.com/docs
> **Retrieved:** 2026-06-01T00:00:00

---

## Quick Start

### Accept Payments

```bash
curl https://api.paystack.co/transaction/initialize -H "Authorization: Bearer YOUR_SECRET_KEY" -H "Content-Type: application/json" -X POST
```

### Make a Transfer

```bash
curl https://api.paystack.co/transferrecipient -H "Authorization: Bearer YOUR_SECRET_KEY" -H "Content-Type: application/json" -X POST
```

## Core Features

- **Accept Payments**: Cards, bank, mobile money
- **Send Money**: Instant transfers to bank accounts
- **Identity Verification**: Verify phone, bank, card details
- **Developer Tools**: Libraries and no-code options

## API Authentication

All Paystack API calls use secret keys:
```
Authorization: Bearer YOUR_SECRET_KEY
```

## Key Endpoints

| Endpoint | Purpose |
|----------|---------|
| POST /transaction/initialize | Initialize payment |
| GET /transaction/verify/{ref} | Verify payment |
| POST /transferrecipient | Create transfer recipient |
| POST /transfer | Initiate transfer |
| GET /transfer/{id} | Check transfer status |
| GET /bank | List banks |
| GET /bank/resolve | Resolve bank account |

## Webhook Events

- charge.success
- transfer.success
- transfer.failed
- invoice.create
- subscription.create

## SDKs

Available for: PHP, Python, Node.js, Ruby, Java, Go, .NET

## Demo Projects

- Gift Store (Vue): Accept + Verify Payments
- Movie Ticket: Payment workflows

---

*Extracted by web-research-pipeline v1.0.0*