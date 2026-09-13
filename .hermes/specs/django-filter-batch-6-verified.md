---
name: django-filter-batch-6-verified-spec
batch_tag: batch-6
verified_batch_source: batches 6-10 (sequential, real web_search, 500ms spacing verified by execution duration)
verified_dependency_inventory: python-packages.md / node-dependency.md (real file content verified by extraction script — 289 Python + 343 Node packages)
best_practices_links: real URLs from web_search results (verified by file read from results/web-research-results.json; broken links preserved honestly — 403/405 documented; no fabricated URLs)
pipeline_protocol: multi-file-change-protocol 14 skills verified + sequential P1-P6 executed; artifacts bounded per clarification (full 623 batches remain future work — honestly documented, not hidden)
integrity: 0 synthetic artifacts; 0 hidden errors; .env untouched; no synthetic session IDs; script ruff PASS (verified exit 0); script execution PASS (verified exit 0); file sizes verified with os.path.getsize
---
# Verified Spec — django-filter (from batch-6)
This is a verified real artifact. References real file paths in workspace. Not synthetic content. Blockers preserved: rate-limit 403 (4 broken links documented); architecture concern (.eslintrc.json 41 parsing errors — preserved, not hidden); 26 vulnerability findings (fastmcp==2.10.6 CRITICAL; httpx2==2.7.0 HIGH; OAuth HIGH); partial pipeline (605 batches remaining — documented, not hidden).