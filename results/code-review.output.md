# Code Review Findings — `projects/ecom` (Django REST + DRF)

**Prompt:** `prompts/code-review.prompt.md` (inline body authoritative; `templates/code-review/phases.md` missing — used inline Steps/Tasks).
**Scope:** Order/User/Product API views + serializers + settings. Highest-risk (auth, payments, data) reviewed first.
**Reviewed files:**

- `projects/ecom/base/views/order_views.py`
- `projects/ecom/base/views/user_views.py`
- `projects/ecom/base/views/product_views.py`
- `projects/ecom/base/serializers.py`, `base/models.py`, `ecom/settings.py`

---

## CRITICAL

### C1 — Order totals taken verbatim from client (payment fraud)

`order_views.py:28-34, 47-62` — `addOrderItems` builds `Order` from `data['totalPrice']`, `data['taxPrice']`, `data['shippingPrice']` and each `OrderItem.price` from `i['price']`. None are cross-checked against `Product.price` (`models.py:18`). An authenticated user can POST an order with `totalPrice: "0.01"` while referencing real products → pay nothing for real goods. Server must compute price/tax/shipping server-side from `product.price`.

### C2 — Privilege escalation via `updateUser`

`user_views.py:92-108` — decorated only `@permission_classes([IsAuthenticated])` but sets `user.is_staff = data['isAdmin']` on **any** user (`User.objects.get(id=pk)`). Any logged-in user can `PUT /api/users/<self>/` with `{"isAdmin": true}` and promote themselves to admin. Must require `IsAdminUser` and forbid self/role changes without admin scope.

### C3 — Unauthenticated arbitrary file upload (`uploadImage`)

`product_views.py:101-111` — `@api_view(['POST'])` has **no** `permission_classes`. `REST_FRAMEWORK` sets only `DEFAULT_AUTHENTICATION_CLASSES` (`settings.py:36-40`); with no `DEFAULT_PERMISSION_CLASSES`, DRF defaults to `AllowAny`. So anyone (no auth) can `POST` an image to **any** product. No file-type/size validation; `product.image = request.FILES.get('image')` also accepts `None`. Add `IsAdminUser` + validate content type/size.

---

## HIGH

### H1 — `updateOrderToPaid` trusts client, no payment proof, no ownership check

`order_views.py:103-112` — marks `isPaid=True` with no PayPal webhook/IPN verification and no `order.user == request.user` or `is_staff` check. Any authenticated user who knows an order `_id` can mark **any** order paid. Also `Order.objects.get(_id=pk)` is unguarded → `DoesNotExist` → HTTP 500.

### H2 — Inventory not validated; stock can go negative

`order_views.py:47-62` — `qty` comes from client unvalidated (`i['qty']`); `product.countInStock -= item.qty` with no check for `qty <= 0`, `qty > countInStock`, or `countInStock < 0`. Negative/oversized quantities corrupt inventory. Also a race: no `select_for_update` → lost updates under concurrency.

### H3 — Bare `except:` / missing PK guards hide errors → 500s

- `order_views.py:99-100` bare `except:` swallows all errors, returning "Order does not exist" even for programming/DB faults.
- `user_views.py:87` `getUserById`, `:95` `updateUser`, `:114` `deleteUser` call `.get(id=pk)` with no `try/except` → 500 on bad pk.
- `user_views.py:44` bare `except:` in `registerUser` returns "email already exists" for **any** exception (e.g. missing field), masking real failures.
Catch `ObjectDoesNotExist` specifically; return 404.

---

## MEDIUM

### M1 — Email/username collision in `updateUserProfile` (account-takeover vector)

`user_views.py:56-58` — sets `username = data['email']`, `email = data['email']` with no uniqueness check. A user can set their email to another account's email (collision / confusion). Validate uniqueness against `User` excluding self.

### M2 — `getProducts` crashes on non-numeric `page`

`product_views.py:23-36` — `paginator.page(page)` tolerates bad input, but later `page = int(page)` raises `ValueError` on a string like `"abc"` → 500. Validate/coerce `page` before `int()`.

### M3 — No DB transaction around `addOrderItems`

`order_views.py:28-62` — Order, ShippingAddress, then OrderItems are created outside `transaction.atomic()`. If an `OrderItem` create fails mid-loop, the Order/ShippingAddress persist as orphans. Wrap in `atomic()`.

### M4 — Insecure defaults

- `settings.py:16` `DEBUG = True` (should be env-gated; prod must be False).
- `settings.py:44` `ACCESS_TOKEN_LIFETIME = timedelta(days=30)` — 30-day access tokens widen theft window; use short-lived access + refresh.

### M5 — Wrong status on authorization denial

`order_views.py:97-98` returns `HTTP_400_BAD_REQUEST` for "Not authorized". Should be `401/403` to distinguish authn vs authz.

---

## LOW

### L1 — Comment typo

`order_views.py:46` "order items adn set" → "and".

### L2 — `createProductReview` uses direct `data['rating']`/`data['comment']`

`product_views.py:128-139` — direct subscript (KeyError 500 if missing) and no rating-range validation (e.g. 1–5).

---

## Summary

- 3 CRITICAL (client-set prices, self-serve admin escalation, public file upload), 3 HIGH (unverified payment, unvalidated stock, swallowed exceptions/500s), 5 MEDIUM, 2 LOW.
- Must-fix: C1, C2, C3, H1, H2. Optional: M1–M5, L1–L2.
- No tests exist for these flows (`base/tests.py` present but no order/payment/auth coverage verified); add deterministic tests for price calc, role enforcement, and upload auth before shipping.
