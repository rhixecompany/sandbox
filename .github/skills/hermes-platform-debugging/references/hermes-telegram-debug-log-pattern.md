# Hermes Telegram DEBUG Log Pattern

## Trigger
- `hermes logs --level DEBUG --since 24h` shows sparse output with one repeating Telegram traceback.
- The visible error is transient-looking: `telegram.error.NetworkError` wrapping `httpx.ConnectError: All connection attempts failed`, often during bootstrap/webhook cleanup or reconnect.

## Decision Rule
- If `hermes status` shows Telegram `connected` / gateway `running`, do NOT patch `plugins/platforms/telegram/*` as the first action.
- Do additional evidence gathering first, then decide whether the failure is:
  1. current unreachable API/DNS
  2. transient bootstrap failure that already recovered
  3. reproducible code regression

## Verification Steps
1. Read `gateway_state.json` platform state.
2. Probe live API reachability to `api.telegram.org` from the current session.
3. Probe bootstrap dependencies if relevant, e.g. `dns.google/resolve`.
4. Inspect Hermes `.env` and `config.yaml` for Telegram-specific overrides that could explain repeated bootstrap failures: `TELEGRAM_PROXY`, `HERMES_TELEGRAM_DISABLE_FALLBACK_IPS`, `HERMES_TELEGRAM_*` timeout overrides, `TELEGRAM_WEBHOOK_URL`, `TELEGRAM_WEBHOOK_SECRET`.
5. Read surrounding adapter code to confirm best-effort handling exists before changing it.

## Capture Instead of Patch
When the conclusion is “transient recoverable failure, no current code regression,” record:
- exact traceback/file/line summary
- `hermes status` and `gateway_state.json` snapshot
- live reachability probe results
- repo/docs context preserved during investigation
- recommended next trigger for a real code edit

## Reproducibility Gate for Code Edits
Only edit installed Hermes provider code when:
- the failure is reproducible on demand, and
- the fix is minimal and scoped, and
- you can rerun the same verification and see the exact failure mode change.

Otherwise, prefer documentation/config checks/host-network checks over plugin edits.
