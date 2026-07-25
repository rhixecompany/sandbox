# PayPal Getting Started Patterns

## SDK Setup

```python
import paypalrestsdk

paypalrestsdk.configure({
    "mode": "sandbox",  # or "live"
    "client_id": "your_client_id",
    "client_secret": "your_client_secret"
})
```

## Create Payment

```python
payment = paypalrestsdk.Payment({
    "intent": "sale",
    "payer": {"payment_method": "paypal"},
    "redirect_urls": {
        "return_url": "https://yoursite.com/success",
        "cancel_url": "https://yoursite.com/cancel"
    },
    "transactions": [{
        "amount": {"total": "10.00", "currency": "USD"},
        "description": "Test payment"
    }]
})

if payment.create():
    # Redirect user to payment.links[1].href
    pass
else:
    print(payment.error)
```

## Execute Payment

```python
payment = paypalrestsdk.Payment.find(payment_id)

if payment.execute({"payer_id": payer_id}):
    print("Payment executed successfully")
else:
    print(payment.error)
```

## Webhook Verification

```python
import hmac
import hashlib

def verify_webhook(payload, signature, webhook_id):
    # PayPal uses different verification
    pass  # Implement based on PayPal documentation
```