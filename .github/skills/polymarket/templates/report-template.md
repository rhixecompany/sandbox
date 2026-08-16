# Polymarket Query Report

## Market Details
- **Market:** `{market_name}`
- **Question:** `{question}`
- **Outcome:** `{outcome}` / No
- **Expiration:** `{expiry}`

## Current Prices
| Outcome | Price (USDC) | Implied Probability | Volume |
|---------|-------------|-------------------|--------|
| Yes | {yes_price} | {yes_prob}% | {yes_volume} |
| No | {no_price} | {no_prob}% | {no_volume} |

## Order Book (Top 5)
### Yes Bids
| Price | Size | Total |
|-------|------|-------|
{yes_bids}

### No Bids
| Price | Size | Total |
|-------|------|-------|
{no_bids}

## Historical Volume
{history_chart}

## Analysis
{analysis}
