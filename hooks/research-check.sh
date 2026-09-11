#!/bin/bash
# Research folder integrity hook — verifies every research topic has its
# markdown sources, skill, script, and test. Exit 1 lists all gaps.
set -u

ROOT="$(cd "$(dirname "$0")/.." && pwd)"
FAIL=0

# topic dir -> script slug (dir name with '-' -> '_')
TOPICS="binance-api-tutorial busha-api-tutorial cryptocurrency-wallets-api-tutorial face-mask-video-call-tutorial flutterwave-tutorial hermes-agents-tutorial hermes-memory-files paypal-tutorial paystack-tutorial python-asyncio-tutorial"

check_topic() {
    local dir="$1" slug="$2"
    [ -d "$ROOT/research/$dir" ] || { echo "MISSING research/$dir"; FAIL=1; }
    [ -n "$(ls "$ROOT/research/$dir"/*.md 2>/dev/null)" ] || { echo "MISSING md files in research/$dir"; FAIL=1; }
    [ -f "$ROOT/skills/research-$dir/SKILL.md" ] || { echo "MISSING skills/research-$dir/SKILL.md"; FAIL=1; }
    [ -f "$ROOT/scripts/$slug.py" ] || { echo "MISSING scripts/$slug.py"; FAIL=1; }
    [ -f "$ROOT/scripts/tests/test_$slug.py" ] || { echo "MISSING scripts/tests/test_$slug.py"; FAIL=1; }
}

for t in $TOPICS; do
    check_topic "$t" "research_$(echo "$t" | tr '-' '_')"
done

# Root-level earnings research (2 md files, not a topic dir)
for f in uk-earning-sites-comparison.md uk-money-earning-sites-research-2026.md; do
    [ -f "$ROOT/research/$f" ] || { echo "MISSING research/$f"; FAIL=1; }
done
[ -f "$ROOT/skills/research-uk-earning-sites/SKILL.md" ] || { echo "MISSING skills/research-uk-earning-sites/SKILL.md"; FAIL=1; }
[ -f "$ROOT/scripts/research_uk_earning_sites.py" ] || { echo "MISSING scripts/research_uk_earning_sites.py"; FAIL=1; }
[ -f "$ROOT/scripts/tests/test_research_uk_earning_sites.py" ] || { echo "MISSING scripts/tests/test_research_uk_earning_sites.py"; FAIL=1; }

if [ "$FAIL" -eq 0 ]; then
    echo "OK: all research topics have md + skill + script + test"
    exit 0
fi
echo "FAIL: $FAIL gap(s) listed above" >&2
exit 1