#!/usr/bin/env python3
"""Phase 2 — build scored platform_master_list.csv for ngn-earnings-kit."""
import csv, os

KIT = r"C:\Users\Alexa\Desktop\SandBox\ngn-earnings-kit"
OUT = os.path.join(KIT, "references", "platform_master_list.csv")

# Weights per ngn-earnings-research.prompt.md
#   Effective NGN/hour 30%, Reliability 20%, NG Accessibility 15%, Entry Barrier 10%,
#   Scalability 10%, Tax Efficiency 10%, Time-to-first-NGN 5%
W = dict(ngn_ph=0.30, reliability=0.20, ng_access=0.15, entry=0.10,
         scalability=0.10, tax=0.10, t2n=0.05)

# rows: (name, category, ngn_ph, reliability, ng_access, entry, scalability, tax, t2n_days, status, note)
rows = [
    # --- AI / data annotation ---
    ("Mercor", "ai-training", 24000, 8, 9, 8, 8, 7, 3, "verified", "Wise/bank weekly; top pick"),
    ("DataAnnotation.tech", "ai-training", 45000, 7, 6, 7, 6, 6, 10, "likely", "PayPal ~3-7d; steady"),
    ("Stellar AI", "ai-training", 37500, 6, 7, 7, 6, 6, 10, "community", "PayPal weekly; $25 base"),
    ("Micro1", "ai-training", 45000, 5, 7, 6, 6, 5, 14, "community", "AI trainer $20-60"),
    ("Braintrust", "ai-training", 60000, 6, 7, 5, 7, 5, 30, "likely", "net30 slow"),
    ("Invisible Technologies", "ai-training", 35000, 6, 8, 7, 5, 6, 14, "verified", "PayPal/Payoneer 2x/mo"),
    ("Mindrift (Toloka)", "ai-training", 12000, 5, 8, 8, 4, 6, 7, "community", "bi-weekly"),
    ("CrowdGen (Appen)", "ai-training", 10500, 5, 9, 8, 5, 5, 21, "verified", "monthly"),
    ("Remotasks/Outlier", "ai-training", 15000, 6, 9, 8, 6, 5, 7, "verified", "weekly baseline"),
    # --- surveys / microtasks ---
    ("SagaPoll", "surveys", 1800, 6, 10, 9, 4, 5, 21, "verified", "native NGN bank"),
    ("Premise", "surveys", 2500, 5, 9, 8, 4, 5, 14, "verified", "location tasks"),
    ("GeoPoll", "surveys", 900, 6, 10, 9, 3, 5, 7, "verified", "airtime not cash"),
    ("TGM Panel (NG)", "surveys", 3750, 5, 10, 7, 5, 5, 21, "verified", "good comp; PayPal gripes"),
    ("TimeBucks", "surveys", 6000, 7, 9, 8, 5, 6, 7, "verified", "$3 min; multi rails"),
    ("FreeCash", "surveys", 7500, 6, 8, 8, 6, 5, 3, "verified", "offer walls > surveys"),
    ("Microworkers", "surveys", 4500, 5, 8, 8, 3, 5, 14, "community", "$9 min"),
    ("Clickworker", "surveys", 10500, 6, 8, 7, 5, 6, 14, "verified", "weekly PayPal/Payoneer"),
    ("Surveoo", "surveys", 1500, 4, 7, 7, 3, 5, 21, "unverified", "NG redemption issues"),
    ("Ipsos iSay", "surveys", 3000, 5, 7, 7, 4, 5, 30, "unverified", "NG rate unverified"),
    ("Toluna", "surveys", 1500, 5, 9, 8, 3, 5, 30, "verified", "huge NG panel; slow"),
    # --- user testing ---
    ("uTest (Applause)", "user-testing", 15000, 8, 9, 8, 6, 6, 4, "verified", "best NG crowdtesting"),
    ("Respondent.io", "user-testing", 60000, 5, 6, 6, 5, 5, 9, "verified", "high value; low volume"),
    ("Userlytics", "user-testing", 15000, 7, 8, 7, 4, 6, 10, "verified", "PayPal gate"),
    ("Testlio", "user-testing", 22500, 7, 8, 6, 5, 6, 7, "verified", "hourly; weekly"),
    ("Test.io", "user-testing", 15000, 6, 9, 8, 5, 6, 14, "verified", "bug pace"),
    ("PlaytestCloud", "user-testing", 7500, 5, 6, 8, 3, 5, 21, "possible", "low NG volume"),
    ("IntelliZoom", "user-testing", 6000, 5, 7, 8, 3, 5, 14, "unverified", "filler"),
    ("Trymata", "user-testing", 9000, 5, 6, 7, 3, 5, 14, "unverified", ""),
    ("UserFeel", "user-testing", 6000, 5, 6, 7, 3, 5, 14, "unverified", ""),
    ("UserDirect", "user-testing", 4500, 5, 6, 7, 3, 5, 14, "unverified", ""),
    ("Betakitesting", "user-testing", 22500, 6, 6, 7, 4, 5, 21, "blog", "Tremendous rails"),
    ("PlaybookUX", "user-testing", 30000, 5, 6, 6, 3, 5, 21, "unverified", "invite-only"),
    # --- BLOCKED / geo-locked ---
    ("UserTesting", "user-testing", 0, 3, 1, 4, 4, 4, 999, "BLOCKED", "NOT supported NG"),
    ("UserInterviews", "user-testing", 0, 3, 1, 4, 4, 4, 999, "BLOCKED", "NOT supported NG"),
    ("Maze", "user-testing", 0, 3, 1, 3, 3, 4, 999, "BLOCKED", "tool not panel"),
    ("Swagbucks", "surveys", 0, 4, 1, 6, 4, 5, 999, "BLOCKED", "geo-locked"),
    ("Qmee", "surveys", 0, 4, 1, 6, 4, 5, 999, "BLOCKED", "geo-locked"),
    ("Prolific", "surveys", 0, 4, 1, 6, 4, 5, 999, "BLOCKED", "geo-locked"),
    ("MoBrog", "surveys", 0, 3, 1, 4, 2, 4, 999, "BLOCKED", "VPN fraud risk"),
]


def t2n_score(days):
    if days >= 999:
        return 1
    if days <= 3:
        return 10
    if days <= 7:
        return 8
    if days <= 14:
        return 6
    if days <= 21:
        return 4
    if days <= 30:
        return 3
    return 2


def rate_ph(ph):
    """Scale NGN/hr: 3,000/hr -> 1 ... 30,000/hr -> 10 (capped)."""
    return min(ph / 3000.0, 10.0)


results = []
for name, cat, ph, rel, acc, ent, sca, tax, t2n, status, note in rows:
    blocked = status == "BLOCKED"
    lowpay = (not blocked) and ph < 1500
    if blocked:
        eliminated, reason, total = "ELIMINATED", "NG unavailable", 0.0
    elif lowpay:
        eliminated, reason, total = "ELIMINATED", "pay < NGN1,500/hr effective", 0.0
    else:
        eliminated, reason = "KEEP", ""
        total = round(
            W["ngn_ph"] * rate_ph(ph)
            + W["reliability"] * rel
            + W["ng_access"] * acc
            + W["entry"] * ent
            + W["scalability"] * sca
            + W["tax"] * tax
            + W["t2n"] * t2n_score(t2n),
            2,
        )
    results.append(dict(name=name, category=cat, ngn_ph=ph, reliability=rel,
                        ng_access=acc, entry=ent, scalability=sca, tax=tax,
                        t2n_days=t2n, total=total, eliminated=eliminated,
                        reason=reason, status=status, note=note))

results.sort(key=lambda r: -r["total"])

with open(OUT, "w", newline="", encoding="utf-8") as f:
    w = csv.DictWriter(f, fieldnames=["name", "category", "ngn_ph", "reliability",
                                      "ng_access", "entry", "scalability", "tax",
                                      "t2n_days", "total", "eliminated", "reason",
                                      "status", "note"])
    w.writeheader()
    for r in results:
        w.writerow(r)

print(f"Wrote {len(results)} rows -> {OUT}")
print("\nTOP 15 KEPT:")
for r in results:
    if r["eliminated"] == "KEEP":
        print(f"  {r['name']:<24}{r['category']:<14}{r['ngn_ph']:>8,} NGN/h  total={r['total']:>5.2f}")
        if sum(1 for x in results if x['eliminated'] == 'KEEP' and x['total'] >= r['total']) > 15:
            break
print("\nELIMINATED:")
for r in results:
    if r["eliminated"] == "ELIMINATED":
        print(f"  {r['name']:<24}{r['reason']}")
