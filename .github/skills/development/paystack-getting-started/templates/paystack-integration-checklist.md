# Paystack Integration Checklist

## Pre-Integration
- [ ] Paystack account created
- [ ] Business documents submitted (KYB)
- [ ] Account approved
- [ ] Sandbox API keys obtained
- [ ] Team members added with appropriate roles

## Sandbox Testing
- [ ] Test transaction successful
- [ ] Webhook endpoint receives events
- [ ] Webhook signature verification works
- [ ] Error handling tested (declined cards, network errors)
- [ ] Idempotency keys prevent duplicate charges
- [ ] Refund flow tested
- [ ] Transfer flow tested (if applicable)

## Production Readiness
- [ ] Production API keys configured
- [ ] Webhook URL updated to production
- [ ] Webhook events selected for production
- [ ] Monitoring/alerting configured
- [ ] Runbook for common issues documented
- [ ] Rollback plan if issues arise

## Go-Live
- [ ] First live transaction successful
- [ ] Settlement schedule confirmed
- [ ] Support contacts established
- [ ] Compliance documents current

## Post-Launch (Week 1)
- [ ] Transaction success rate > 99%
- [ ] Webhook delivery rate > 99%
- [ ] No unresolved customer complaints
- [ ] Settlement timing as expected