# NGN Earnings Kit Index — Aug 2026 (eight categories, 83 scored platforms)

Seed index for any future *better-than-Outlier/Atapoll* Nigeria earnings build.
FX used: US$1 ≈ ₦1,500. All per-platform deep-dives live in `~/Desktop/SandBox/ngn-earnings-kit/platforms/<cat>/`.

## Scored master list (46 KEEP / 37 ELIMINATED of 83)
Scoring weights: effective NGN/h 30%, reliability 20%, NG-accessibility 15%, entry barrier 10%, scalability 10%, tax-efficiency 10%, time-to-first-NGN 5%. Elimination: pay < ₦1,500/hr effective OR geo-locked/scam-class.

Top 10 by score:
1. Mercor (ai-training) — ₦24k/hr floor, ceiling ₦150k; weekly Wise/bank; validated reliable, selective (feast-or-famine)
2. Upwork (freelance) — NG avg $163/job; escrow; Cleva/Grey USD-A rails + Payoneer
3. DataAnnotation.tech (ai-training) — ₦45k/hr WHEN approved; 2.6% acceptance (⚠️)
4. Invisible Technologies (ai-training) — ₦35k/hr, selective
5. Stellar AI (ai-training) — ₦37.5k/hr, selective
6. Braintrust (ai-training) — ₦60k/hr, network gate
7. Micro1 (ai-training) — ₦45k/hr
8. Testlio (user-testing) — ₦22.5k/hr, weekly Payoneer
9. uTest/Applause (user-testing) — ₦15k+/item, Payoneer ✓ NG, daily cycles
10. Respondent.io (UX/interviews) — ₦60k (rare), Tremendous→PayPal

## Per-category top picks (validated)
| Category | Pick | Why |
|----------|------|-----|
| AI training | Mercor | highest ceiling, weekly payout |
| Freelance | Upwork | escrow, USD→NGN via Cleva |
| User testing | uTest | Payoneer ✓, daily cycles |
| Surveys | TimeBucks / FreeCash | $3-min GPTs, PayPal NG ✓ |
| Field tasks | SagaPoll / Premise | NGN-native bank rails; store visits ~10× surveys |
| Bank referral | Kuda | ₦4–12k/ref, T2 referee (NOT a CASS-equivalent bonus — NG banks only lottery) |
| Cashback | JumiaPay | 3% + 20% first-month; total NG stack ₦2.5–6k/mo only |
| Passive | Pawns.app / EarnApp | NG-verified; BTC/Visa GC payout; min $2.5–$5 |

## Payout-rail reality for Nigeria (CRITICAL — corrects common assumptions)
- **Payoneer** ✅ workhorse: free receiving USD/EUR/GBP, withdraw to any NG bank in NGN (~2% all-in).
- **PayPal (NG)** ⚠️ **send-only for receiving in 2026 guides** — do NOT plan inbound freelance income on it. Community surveys still use PayPal for small USD GPT earnings (receive OK there, volume-capped).
- **Cleva / Grey / Raenest** ✅ USD virtual US account numbers in your name — land Upwork ACH ($0.99) and cash out NGN at interbank-ish rates. Modern alternative to Payoneer for freelance.
- **Wise** ⚠️ NG USD receiving details NOT offered; use for NGN holding/sending only.
- **Bank transfer (NGN)** ✅ NGN-native apps (SagaPoll bank; PalmPay/Kuda/OPay wallet).
- **Airtime rails** small (~₦900/hr effective on GeoPoll); crypto P2P fine but ID-checked.
- **Paystack/Flutterwave on a remote “AI job” = scam tell** (merchant tools, not personal rails).

## Real-payer caveats observed
- Honeygain: min payout **$20 → 4–8 months** on one device; Content-Delivery mode NOT available in NG.
- EarnApp: min ~$2.5 — fastest first bandwidth payout.
- TimeBucks: legit but complaint-heavy (NG Facebook groups); use small balances.
- Chipper Cash: 2025-26 account/login failures; small amounts only.
- Passive apps on metered mobile data = GUARANTEED NET LOSS (NG data ≈ $0.39/GB vs $0.10–0.20 earned/GB). WiFi only.
- Cloud-mining / tap-to-earn / “name-only” apps (Spilr, DistributedMint) = scam class — flag and eliminate.

## NG tax quick-notes (verify at filing)
- Nigeria Tax Act 2025 (in force 1 Jan 2026): first ₦800,000/yr tax-free for everyone incl. freelancers/self-employed.
- Bands above: 15% to ₦3M, 18% to ₦12M, 21% to ₦25M, 23% to ₦50M, 25% above.
- Self-assessment mandatory above threshold; TIN auto-issued; foreign platforms usually don't withhold — you report.
- Record income in NGN (CBN/I&E rate); expenses deductible (internet/data/equipment; rent relief 20% up to ₦500k).
- Full guide in kit: `references/tax_guidance_ngn_2026.md`.

## Rebuild recipe (idempotent generator rule)
- Keep the scored CSV as the source of truth; the extend/merge script **must** read existing rows and only ADD missing `name` keys, or re-runs truncate (observed 83 → 56).
- Verify: `py_compile`; run the merge twice; second run reports `added 0`, same KEEP/ELIMINATED counts; assert unique names.
- Gate: `rows==N`, `KEEP==K`, no `\ufffd`/garbage tokens, openpyxl workbook opens.