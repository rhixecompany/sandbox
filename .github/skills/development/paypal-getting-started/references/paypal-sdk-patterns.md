# PayPal SDK Patterns

## Python SDK Setup

```python
import paypalrestsdk

paypalrestsdk.configure({
    "mode": "sandbox",  # or "live"
    "client_id": "YOUR_CLIENT_ID",
    "client_secret": "YOUR_CLIENT_SECRET"
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
        "description": "Product description"
    }]
})

if payment.create():
    for link in payment.links:
        if link.rel == "approval_url":
            print(f"Redirect to: {link.href}")
else:
    print(payment.error)
```

## Execute Payment After Approval

```python
payment = paypalrestsdk.Payment.find(payment_id)
if payment.execute({"payer_id": payer_id}):
    print("Payment executed")
else:
    print(payment.error)
```

## Error Handling

```python
try:
    payment = paypalrestsdk.Payment.find(payment_id)
    if payment.execute({"payer_id": payer_id}):
        print("Success")
    else:
        # Payment SDK error
        print(f"Error: {payment.error.get('message', 'Unknown error')}")
except Exception as e:
    # Network or SDK error
    print(f"SDK Error: {e}")
```