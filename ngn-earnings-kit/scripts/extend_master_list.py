#!/usr/bin/env python3
"""Merge NGN platform rows into platform_master_list.csv (idempotent union).

IMPORTANT: this script is UNION-SAFE — it reads the existing CSV, adds only
rows whose `name` is not already present, re-scores everything, sorts, and
writes back. It NEVER rebuilds from an embedded base, so re-runs can't
truncate previously added rows.
"""
import csv
import os

KIT = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
MASTER = os.path.join(KIT, "references", "platform_master_list.csv")

W = dict(ngn_ph=0.30, reliability=0.20, ng_access=0.15, entry=0.10,
         scalability=0.10, tax=0.10, t2n=0.05)
MIN_PH = 1500  # elimination threshold: pay < ₦1,500/hr effective


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


def row(name, category, ngn_ph, reliability, ng_access, entry, scalability, tax,
        t2n_days, status, note):
    return {
        "name": name, "category": category, "ngn_ph": ngn_ph, "reliability": reliability,
        "ng_access": ng_access, "entry": entry, "scalability": scalability, "tax": tax,
        "t2n_days": t2n_days, "total": "", "eliminated": "KEEP" if status != "BLOCKED" else "ELIMINATED",
        "reason": "" if status != "BLOCKED" else "geo-locked",
        "status": status, "note": note,
    }


# 10-tuples: name, category, ngn_ph, reliability, ng_access, entry, scalability, tax, t2n_days, status, note
NEW_ROWS = [
    # --- bank switching & fintech referrals ---
    ("Kuda Referral", "bank-switching", 1500, 7, 10, 6, 5, 5, 14, "verified", "NGN4-12k/ref official; T2 referee req"),
    ("OPay Referral", "bank-switching", 600, 5, 10, 7, 4, 5, 7, "verified", "NGN800/ref; up to NGN3,600/yr login"),
    ("PalmPay Welcome/Ref", "bank-switching", 900, 6, 10, 7, 4, 5, 7, "verified", "welcome <=NGN5,550 while promo + NGN250 pair"),
    ("Risevest Naira Vault Ref", "bank-switching", 500, 6, 10, 6, 5, 5, 90, "verified", "up to 4% upfront on referral investments"),
    ("PiggyVest Signup/Ref", "bank-switching", 400, 5, 10, 6, 4, 5, 10, "verified", "NGN1k+NGN1k; lock NGN2.1k to unlock"),
    ("Moniepoint Refer&Earn", "bank-switching", 800, 6, 10, 6, 5, 5, 30, "verified", "NGN4/transaction 12-mo tail"),
    ("Flutterwave Send Ref", "bank-switching", 300, 6, 9, 5, 4, 5, 14, "verified", "NGN5k+NGN5k but NGN200k min transfer"),
    ("Zenith Salary Acct", "bank-switching", 2000, 8, 9, 8, 6, 6, 5, "verified", "7.95% p.a. + salary advance"),
    # ---- cashback / receipts ----
    ("JumiaPay (Jumia One)", "cashback-receipts", 1000, 6, 10, 9, 3, 5, 1, "verified", "3%/20% vouchers; NGN1-1.5k/mo"),
    ("OPay Cashback", "cashback-receipts", 700, 6, 10, 9, 3, 5, 1, "verified", "up to 6% airtime"),
    ("PalmPay PalmPoints", "cashback-receipts", 800, 6, 10, 9, 3, 5, 1, "verified", "tiered 1-5% + 50% palmpts"),
    ("Moniepoint Rewards", "cashback-receipts", 400, 6, 10, 9, 3, 5, 1, "verified", "up to 2% recharge"),
    ("Kuda Coins/Premium", "cashback-receipts", 500, 7, 10, 7, 3, 5, 1, "verified", "Premium cashback; NGN50k avg bal"),
    ("Chipper Cash 2%", "cashback-receipts", 300, 4, 9, 8, 2, 5, 1, "verified", "2% airtime; account issues"),
    ("Branch 2% Bills", "cashback-receipts", 500, 4, 9, 8, 2, 5, 1, "unverified", "2% bill payment"),
    ("Fetch Rewards", "cashback-receipts", 0, 3, 1, 5, 1, 4, 999, "BLOCKED", "US/CA/UK only"),
    ("Ibotta / Receipt Hog", "cashback-receipts", 0, 3, 1, 5, 1, 4, 999, "BLOCKED", "US-only"),
    # ---- mystery shopping / field tasks ----
    ("SagaPoll Store Visits", "mystery-shopping", 15000, 6, 10, 8, 4, 5, 14, "verified", "5,000pts=NGN30k; store audit photo tasks"),
    ("Premise Field Tasks", "mystery-shopping", 2000, 5, 9, 8, 4, 5, 10, "verified", "NGN150-2k/task; NGN rails"),
    ("Appen Mystery Shopper", "mystery-shopping", 13500, 6, 8, 6, 5, 5, 30, "verified", "Freelance NG listings; USD $3-15/hr equiv"),
    ("NLP Nigeria (agency)", "mystery-shopping", 10000, 4, 9, 7, 3, 5, 30, "verified", "Pan-NG ops; cash per visit"),
    ("Streetbees", "mystery-shopping", 4500, 3, 5, 7, 2, 5, 21, "unverified", "Works unofficially; supply skews UK/US"),
    ("Roamler", "mystery-shopping", 0, 4, 1, 5, 2, 4, 999, "BLOCKED", "EU-only; NG defunct"),
    ("BeMyEye", "mystery-shopping", 0, 4, 1, 5, 2, 4, 999, "BLOCKED", "EU-only"),
    ("Field Agent", "mystery-shopping", 0, 4, 1, 5, 2, 4, 999, "BLOCKED", "NG not served; SA only in Africa"),
    # ---- passive apps ----
    ("Pawns.app / IPRoyal", "passive-apps", 750, 6, 9, 8, 3, 5, 30, "verified", "NGM2-8k/mo passive + surveys; BTC/Visa GC payout in NG"),
    ("Honeygain", "passive-apps", 900, 7, 8, 7, 3, 5, 120, "verified", "NGM2-5k/mo; Min $20 = 4-8 months to first payout"),
    ("EarnApp (Bright Data)", "passive-apps", 600, 7, 9, 8, 3, 5, 30, "verified", "NGM1.5-4.5k/mo; min ~$2.5 fastest bandwidth payout"),
    ("Cointiply / FreeBitco.in", "passive-apps", 300, 5, 8, 9, 2, 5, 14, "verified", "NGM150-1.5k/mo faucets; legit dust"),
    ("Pi Network", "passive-apps", 500, 3, 8, 8, 1, 5, 365, "verified", "Speculative; not income"),
    ("PacketStream", "passive-apps", 200, 4, 5, 7, 2, 5, 60, "unverified", "NG demand near zero"),
    ("TraffMonetizer", "passive-apps", 150, 4, 5, 7, 2, 5, 60, "unverified", "legit dust"),
    ("DistributedMint", "passive-apps", 0, 2, 4, 5, 1, 4, 999, "BLOCKED", "no verifiable info; site unreachable"),
    ("Spilr", "passive-apps", 0, 2, 4, 5, 1, 4, 999, "BLOCKED", "RED FLAG - no real app"),
    ("Cloud mining apps", "passive-apps", 0, 1, 4, 4, 1, 3, 999, "BLOCKED", "HIGH RISK - scam class, you lose deposits"),
    ("Telegram tap-to-earn", "passive-apps", 0, 2, 5, 6, 1, 4, 999, "BLOCKED", "Near-zero after TGE"),
    # ---- freelance / gig ----
    ("Upwork", "freelance-gigs", 45000, 7, 9, 6, 8, 6, 21, "verified", "NG avg $163/job; escrow; Cleva/Payoneer rails"),
    ("Fiverr", "freelance-gigs", 15000, 6, 8, 7, 7, 6, 30, "verified", "Documentation gigs; 20% seller fee"),
    ("Freelancer.com", "freelance-gigs", 12000, 5, 8, 7, 5, 5, 21, "verified", "Race-to-bottom; Payoneer"),
    ("PeoplePerHour", "freelance-gigs", 10500, 5, 6, 6, 5, 5, 30, "verified", "EU/UK-focused; Payoneer route"),
    ("Contra", "freelance-gigs", 15000, 5, 7, 7, 5, 5, 14, "unverified", "Zero-commission; USDC rails"),
    ("Toptal", "freelance-gigs", 90000, 6, 6, 3, 7, 6, 60, "verified", "High ceiling, elite gate"),
    ("Jobberman", "freelance-gigs", 12000, 6, 10, 8, 4, 6, 21, "verified", "NG job board; salary roles"),
    ("MyJobMag", "freelance-gigs", 12000, 6, 10, 8, 4, 6, 21, "verified", "NG job board"),
]


def main():
    # Read existing (union-preserving)
    rows = []
    headers = None
    if os.path.exists(MASTER):
        with open(MASTER, newline="", encoding="utf-8") as f:
            reader = csv.DictReader(f)
            headers = reader.fieldnames
            rows = list(reader)

    existing = {r["name"] for r in rows}
    added = 0
    for t in NEW_ROWS:
        name, cat, ph, rel, acc, ent, sca, tax, t2n, status, note = t
        if name in existing:
            continue
        rows.append(row(name, cat, ph, rel, acc, ent, sca, tax, t2n, status, note))
        existing.add(name)
        added += 1

    # Score / eliminate
    for r in rows:
        if r["eliminated"] == "ELIMINATED":
            r["total"] = 0.0
            continue
        ph = float(r["ngn_ph"])
        if ph < MIN_PH:
            r["eliminated"] = "ELIMINATED"
            r["reason"] = "pay < NGN1,500/hr effective"
            r["total"] = 0.0
            continue
        r["total"] = round(
            W["ngn_ph"] * min(ph / 3000.0, 10.0)
            + W["reliability"] * float(r["reliability"])
            + W["ng_access"] * float(r["ng_access"])
            + W["entry"] * float(r["entry"])
            + W["scalability"] * float(r["scalability"])
            + W["tax"] * float(r["tax"])
            + W["t2n"] * t2n_score(int(r["t2n_days"])), 2)

    rows.sort(key=lambda r: -(float(r["total"] or 0)))

    hdr = headers or ["name", "category", "ngn_ph", "reliability", "ng_access", "entry",
                      "scalability", "tax", "t2n_days", "total", "eliminated", "reason", "status", "note"]
    with open(MASTER, "w", newline="", encoding="utf-8") as f:
        w = csv.DictWriter(f, fieldnames=hdr)
        w.writeheader()
        for r in rows:
            w.writerow({k: r.get(k, "") for k in hdr})

    kept = sum(1 for r in rows if r["eliminated"] == "KEEP")
    print(f"master list now {len(rows)} rows | added {added} | KEEP {kept} | ELIMINATED {len(rows) - kept}")
    bycat = {}
    for r in rows:
        bycat[r["category"]] = bycat.get(r["category"], 0) + 1
    print("by category:", bycat)


if __name__ == "__main__":
    import sys
    import csv  # noqa: F401 (used in main)
    main()