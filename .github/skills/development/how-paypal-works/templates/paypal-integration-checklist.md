# PayPal Integration Checklist

## Pre-Integration
- [ ] PayPal Developer account created
- [ ] REST API app created (Sandbox)
- [ ] Client ID and Secret obtained
- [ ] Webhook URL configured (ngrok for local dev)

## Sandbox Testing
- [ ] Create order succeeds
- [ ] Capture payment succeeds
- [ ] Refund works
- [ ] Webhook events received
- [ ] Error handling tested

## Production Readiness
- [ ] Live app created and approved
- [ ] Live Client ID and Secret configured
- [ ] Production webhook URL set
- [ ] Webhook events selected
- [ ] Monitoring/alerting configured
- [ ] Runbook for common issues

## Go-Live
- [ ] First live transaction successful
- [ ] Settlement timing confirmed
- [ ] Support contacts established

## Post-Launch (Week 1)
- [ ] Transaction success rate > 99%
- [ ] Webhook delivery rate > 99%
- [ ] No unresolved customer complaints
- [ ] Settlement timing as expected