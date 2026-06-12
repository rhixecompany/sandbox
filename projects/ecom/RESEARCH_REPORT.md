# RESEARCH_REPORT.md

## Project: ecom

**Type:** Ecommerce platform
**Tech Stack:** Django REST Framework, Django, React, Redux, PostgreSQL, PayPal, Docker Compose
**Status:** Active, pending frontend stack refresh

---

## Similar Projects

| Project | URL | Why Relevant |
|---------|-----|--------------|
| xamehi | `projects/xamehi` | Shared Django + React multi-service setup. |
| xamehi.tv | `projects/xamehi.tv` | Shared DRF + React shopping flow and admin management. |

---

## Key Findings

### DRF + React Checkout Flow
- DRF ViewSets with `SimpleRouter` work well for product and order flows; prefer nested routers for order items.
- Keep sensitive checkout completion in DRF ViewSets using PayPal server-side capture; client should not treat approval as completion.

### Redux State Shape
- Use Redux Toolkit slices for cart, catalog, and auth; avoid duplicating server-derived state in multiple slices.
- Consider React Query on top of Redux for cart freshness to reduce manual invalidation.

### PayPal Integration
- Prefer PayPal Orders + Capture API over direct charges so order state can be finalized server-side after shipping checks.
- Store PayPal `order_id` and `capture_id` as order metadata before success redirects.

### Admin Operations
- Django admin is strong here; expose simple readonly dashboards for orders and users instead of building admin UI in React.

---

## Cheatsheets & Quick Reference

| Topic | Resource | Type |
|-------|----------|------|
| DRF docs | https://www.django-rest-framework.org | Docs |
| PayPal Orders API | https://developer.paypal.com/docs/api/orders/v2/ | Docs |
| Redux Toolkit | https://redux-toolkit.js.org | Docs |
| Django admin docs | https://docs.djangoproject.com/en/stable/ref/contrib/admin/ | Docs |
| Docker Compose docs | https://docs.docker.com/compose/ | Docs |

---

## Best Practices
1. **Server-side PayPal capture** — avoid bank-state desync by completing capture in DRF after inventory/order validation.
2. **DRF nested endpoints** — use `drf-nested-routers` for order items so the frontend can mutate child resources safely.
3. **Media via Django in dev** — serve media through Django only when debugging; prefer S3 or WhiteNoise in production.
4. **Read model for carts** — compute cart totals on the server and return finalized totals to the client.
5. **Audit admin actions** — log order status changes with user, timestamp, and prior state.

---

## Common Pitfalls

| Pitfall | Impact | Avoidance |
|---------|--------|-----------|
| PayPal approval treated as payment | Phantom paid orders | Require DRF capture success before order paid status. |
| Frontend-only quantity math | Inventory race conditions | Validate stock on server before confirming line items. |
| Django media path leaks between envs | Mixed dev/prod uploads | Use environment-specific media roots. |
| Redundant cart state | Sync bugs | Treat DRF cart endpoint as source of truth. |

---

## Performance
1. Use `select_related()` and `prefetch_related()` for product categories and order items.
2. Cache category trees with Redis when catalog changes are infrequent.
3. Use Django database-backed sessions for cart durability across anonymous sessions.

---

## Security
1. Verify PayPal webhook signatures before applying capture events.
2. Use CSRF on all DRF session-authenticated mutations; disable unsafe browser exposure for write endpoints.
3. Validate uploaded product images and limit sizes to avoid DoS during media writes.
4. Record admin action log for order refunds and cancellations to preserve financial audit trail.

---

## Related Projects (in workspace)

- **xamehi** — shared Django + React multi-service layout and backend concerns
- **xamehi.tv** — shared DRF + React media/admin experience

---

## Resources

| Resource | URL | Description |
|----------|-----|-------------|
| DRF docs | https://www.django-rest-framework.org | Official documentation |
| Django admin docs | https://docs.djangoproject.com/en/stable/ref/contrib/admin/ | Admin reference |
| PayPal dev docs | https://developer.paypal.com/docs | Payments |
| Redux Toolkit | https://redux-toolkit.js.org | Frontend state |
| WhiteNoise docs | https://whitenoise.readthedocs.io | Static/media serving |
