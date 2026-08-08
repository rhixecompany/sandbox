#!/usr/bin/env python3
"""Extend platform_master_list.csv with batch-2 categories (bank, cashback) and re-score."""
import csv, os

KIT = r"C:\Users\Alexa\Desktop\SandBox\ngn-earnings-kit"
MASTER = os.path.join(KIT, "references", "platform_master_list.csv")

W = dict(ngn_ph=0.30, reliability=0.20, ng_access=0.15, entry=0.10,
         scalability=0.10, tax=0.10, t2n=0.05)


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


# 10-tuple: name, category, ngn_ph, reliability, ng_access, entry, scalability, tax, t2n_days, note, status
new_rows = [
    ("Kuda Referral", "bank-switching", 1500, 7, 10, 6, 5, 5, 14, "NGN4-12k/ref official; T2 referee req", "verified"),
    ("OPay Referral", "bank-switching", 600, 5, 10, 7, 4, 5, 7, "NGN800/ref; up to NGN3,600/yr login", "verified"),
    ("PalmPay Welcome/Ref", "bank-switching", 900, 6, 10, 7, 4, 5, 7, "welcome <=NGN5,550 while promo + NGN250 pair", "verified"),
    ("Risevest Naira Vault Ref", "bank-switching", 500, 6, 10, 6, 5, 5, 90, "up to 4% upfront on referral investments", "verified"),
    ("PiggyVest Signup/Ref", "bank-switching", 400, 5, 10, 6, 4, 5, 10, "NGN1k+NGN1k; lock NGN2.1k to unlock", "verified"),
    ("Moniepoint Refer&Earn", "bank-switching", 800, 6, 10, 6, 5, 5, 30, "NGN4/transaction 12-mo tail", "verified"),
    ("Flutterwave Send Ref", "bank-switching", 300, 6, 9, 5, 4, 5, 14, "NGN5k+NGN5k but NGN200k min transfer", "verified"),
    ("Zenith Salary Acct", "bank-switching", 2000, 8, 9, 8, 6, 6, 5, "7.95% p.a. + salary advance", "verified"),
    ("JumiaPay (Jumia One)", "cashback-receipts", 1000, 6, 10, 9, 3, 5, 1, "3%/20% vouchers; NGN1-1.5k/mo", "verified"),
    ("OPay Cashback", "cashback-receipts", 700, 6, 10, 9, 3, 5, 1, "up to 6% airtime", "verified"),
    ("PalmPay PalmPoints", "cashback-receipts", 800, 6, 10, 9, 3, 5, 1, "tiered 1-5% + 50% palmpts", "verified"),
    ("Moniepoint Rewards", "cashback-receipts", 400, 6, 10, 9, 3, 5, 1, "up to 2% recharge", "verified"),
    ("Kuda Coins/Premium", "cashback-receipts", 500, 7, 10, 7, 3, 5, 1, "Premium cashback; NGN50k avg bal", "verified"),
    ("Chipper Cash 2%", "cashback-receipts", 300, 4, 9, 8, 2, 5, 1, "2% airtime; account issues", "verified"),
    ("Branch 2% Bills", "cashback-receipts", 500, 4, 9, 8, 2, 5, 1, "2% bill payment", "unverified"),
    ("Fetch Rewards", "cashback-receipts", 0, 3, 1, 5, 1, 4, 999, "US/CA/UK only", "BLOCKED"),
    ("Ibotta / Receipt Hog", "cashback-receipts", 0, 3, 1, 5, 1, 4, 999, "US-only", "BLOCKED"),
]

# read existing
rows = []
with open(MASTER, newline="", encoding="utf-8") as f:
    reader = csv.DictReader(f)
    fieldnames = reader.fieldnames
    existing_names = {r["name"] for r in rows}
    for r in reader:
        rows.append(r)

existing_names = {r["name"] for r in rows}

for name, cat, ph, rel, acc, ent, sca, tax, t2n, note, status in new_rows:
    if name in existing_names:
        continue
    rows.append({
        "name": name, "category": cat, "ngn_ph": ph, "reliability": rel,
        "ng_access": acc, "entry": ent, "scalability": sca, "tax": tax,
        "t2n_days": t2n, "total": "", "eliminated": "KEEP" if status != "BLOCKED" else "ELIMINATED",
        "reason": "" if status != "BLOCKED" else "geo-locked",
        "status": status, "note": note,
    })

for r in rows:
    if r["eliminated"] == "ELIMINATED":
        r["total"] = 0.0
        continue
    ph = float(r["ngn_ph"])
    if ph < 1500:
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

with open(MASTER, "w", newline="", encoding="utf-8") as f:
    w = csv.DictWriter(f, fieldnames=fieldnames)
    w.writeheader()
    for r in rows:
        w.writerow(r)

kept = sum(1 for r in rows if r["eliminated"] == "KEEP")
print(f"master list now {len(rows)} rows | KEEP {kept} | ELIMINATED {len(rows) - kept}")
bycat = {}
for r in rows:
    bycat[r["category"]] = bycat.get(r["category"], 0) + 1
print("by category:", bycat)