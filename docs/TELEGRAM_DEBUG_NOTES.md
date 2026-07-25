# Debug Notes — Telegram DEBUG log issue

## Verified

- `hermes doctor --fix` passed.
- `hermes status` shows gateway `running`; `telegram` state is `connected`.
- Token/config files not modified; no secrets read/printed.

## Observed Issue

- `hermes logs --level DEBUG --since 24h` shows a repeated Telegram traceback:
  - `telegram.error.NetworkError: httpx.ConnectError: All connection attempts failed`
  - Origin: Hermes Telegram adapter bootstrap webhook cleanup path during reconnect.

## Root Cause Assessment

- This is a transient Telegram bootstrap/network error, not a fatal Hermes config failure.
- Current state indicates recovery/reconnect paths handled it; gateway remains connected.

## Notes

- Avoid changing Hermes internal plugin install files without upstream review.
- If recurring, review network/proxy/DNS or bot token/permission state.
- Re-run `hermes logs --level DEBUG --since 24h` after next reconnect to capture contextual warnings.
