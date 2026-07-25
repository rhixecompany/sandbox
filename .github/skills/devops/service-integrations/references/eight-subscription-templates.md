# 8 Webhook Subscription Templates

These are the actual subscriptions created with their prompts. Use as starting
templates — adapt event names, prompt logic, and delivery targets per service.

---

## 1. GitHub PR Review

```bash
hermes webhook subscribe github-pr-review \
  --events "pull_request" \
  --prompt "$(cat << 'EOF'
GitHub PR #{pull_request.number} {action} by {pull_request.user.login}

Title: {pull_request.title}
Branch: {pull_request.head.ref} -> {pull_request.base.ref}
Description:
{pull_request.body}

Review this PR. Check for:
- Logic errors, edge cases, security issues
- Code quality, test coverage, documentation
- Breaking changes, migration needs

Post your review as a PR review comment via the GitHub API.
EOF
)" \
  --description "Auto-review every PR with code review skill" \
  --skills "github-code-review"
```

## 2. Stripe Payments

```bash
hermes webhook subscribe stripe-payments \
  --events "payment_intent.succeeded,payment_intent.payment_failed,charge.dispute.created" \
  --prompt "$(cat << 'EOF'
Stripe payment event: {type}

Status: {data.object.status}
Amount: {data.object.amount} {data.object.currency}
Captured: {data.object.amount_captured}
Customer: {data.object.receipt_email}
Description: {data.object.description}

Determine action:
- If amount > 100000 (1000 USD) OR dispute created -> FLAG FOR FRAUD REVIEW
- If new customer (first payment) -> DRAFT welcome email
- If payment_failed -> log and notify
- Otherwise -> ACKNOWLEDGE
EOF
)" \
  --description "Stripe payment events - draft welcome or flag fraud"
```

## 3. Helius On-Chain

```bash
hermes webhook subscribe helius-onchain \
  --events "transaction,nft,account" \
  --prompt "$(cat << 'EOF'
Helius on-chain event: {type}

Signature: {signature}
Account: {account}
Type: {eventType}
Data: {data}

Analyze this Solana on-chain event and compose a Telegram alert:
- What happened? Summarize in 1-2 lines
- Is it high-value or suspicious? Flag if so
- Include the Solscan link for the signature
EOF
)" \
  --description "Helius on-chain events -> Telegram alerts"
```

## 4. Beehiv Subscribers

```bash
hermes webhook subscribe beehive-subscribers \
  --events "subscriber.created,subscriber.unsubscribed" \
  --prompt "$(cat << 'EOF'
Beehiv subscriber event: {type}

Email: {data.email}
Name: {data.name}
Tags: {data.tags}
Source: {data.referrer}
List: {data.list}
Action: {action}

1. Enrich this lead: what segment do they belong to?
2. Route them: CRM pipeline, Slack channel, or acknowledge?
3. If unsubscribed -> log and remove from active lists.
EOF
)" \
  --description "Beehiv subscriber events - enrich and route"
```

## 5. Sentry Errors

```bash
hermes webhook subscribe sentry-errors \
  --events "event.alert" \
  --prompt "$(cat << 'EOF'
Sentry error alert

Project: {project}
Message: {message}
Level: {level}
URL: {url}
Environment: {environment}
Tags: {tags}
Event ID: {event}

1. Triage this error:
   - Determine severity (critical/high/medium/low)
   - Identify affected component and root cause
   - Is this a new error or a regression?
2. If critical or high severity -> PAGE ONCALL with error summary
3. Draft a remediation plan with steps
EOF
)" \
  --description "Sentry errors - agent triages and pages oncall"
```

## 6. Cal.com Bookings

```bash
hermes webhook subscribe cal-booking \
  --events "BOOKING_CREATED" \
  --prompt "$(cat << 'EOF'
Cal.com booking event: {triggerEvent}

Attendee: {attendee.name} ({attendee.email})
Organizer: {organizer.name}
Event: {eventType.title}
When: {startTime} - {endTime}
Timezone: {attendee.timeZone}
Location: {location}
Notes: {eventType.description}

Generate a pre-meeting briefing:
1. Who is the attendee? Company, role, context
2. What is this meeting about? Purpose, agenda
3. Key talking points and preparation items
4. Any action items before the meeting
EOF
)" \
  --description "Cal.com meeting booked - pre-meeting briefing"
```

## 7. TypeForm Submissions

```bash
hermes webhook subscribe typeform-submit \
  --events "form_response" \
  --prompt "$(cat << 'EOF'
TypeForm submission: {form_response.form_id}

Form: {form_response.form_name}
Submitted: {submitted_at}
Answers:
{form_response.answers}

Route this submission:
1. Add to CRM: extract contact info and form data
2. Draft Slack message: summary of who submitted what
3. Determine follow-up needed (high/medium/low priority)
EOF
)" \
  --description "TypeForm submit - CRM entry + Slack draft"
```

## 8. Home Assistant Sensor

```bash
hermes webhook subscribe homeassist-sensor \
  --events "state_changed" \
  --prompt "$(cat << 'EOF'
Home Assistant event: {event_type}

Entity: {data.entity_id}
Old state: {data.old_state.state}
New state: {data.new_state.state}
Domain: {data.domain}
Last changed: {data.new_state.last_changed}

A sensor tripped. Investigate:
1. What changed and why?
2. Is this expected behavior or an anomaly?
3. Check related entities for context
4. Recommend action: alert user, ignore, or auto-remediate?
EOF
)" \
  --description "Home Assistant sensor trip - agent investigates"
```

## Testing Commands

```bash
# Test each route with representative payload
hermes webhook test github-pr-review
hermes webhook test stripe-payments --payload '{"type": "payment_intent.succeeded", "data": {"object": {"amount": 50000, "currency": "usd", "receipt_email": "test@example.com"}}}'
hermes webhook test sentry-errors --payload '{"project": "my-app", "message": "NullPointerException", "level": "error"}'
hermes webhook test cal-booking --payload '{"triggerEvent": "BOOKING_CREATED", "attendee": {"name": "Jane", "email": "jane@example.com"}}'
hermes webhook test homeassist-sensor --payload '{"event_type": "state_changed", "data": {"entity_id": "sensor.temperature", "old_state": {"state": "22"}, "new_state": {"state": "45"}, "domain": "sensor"}}'
```
