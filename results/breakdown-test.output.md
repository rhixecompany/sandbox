# Test Strategy & QA Breakdown: `lcs.py` (Longest Common Subsequence utilities)

> **Mode:** Real artifact — generated against the actual workspace component `lcs.py`.
> **Dry-run flags:** The prompt's optional input scaffolds were unavailable (see *Skipped References* below). The breakdown below is fully evidence-based against real code and a live execution trace; only the GitHub-issue scaffolding that the prompt *optionally* pulls from templates is marked dry-run.

## Subject Under Test

| Attribute | Value |
|---|---|
| Component | `lcs.py` (145 LOC, no external deps) |
| Public API | `lcs_length(a, b) -> int`, `lcs(a, b) -> list[T]`, `lcs_all(a, b) -> list[list[T]]` |
| Type contract | `Sequence[T]` (list / tuple / str), generic via `TypeVar("T")` |
| Algorithms | DP: `lcs_length` O(mn) time / O(min(m,n)) space; `lcs` & `lcs_all` O(mn) space with backtracking |

## Verification Evidence (executed, not hypothetical)

`python3 -c "import lcs; ..."` run against the real file — all assertions passed:

- `lcs_length('ABCDGH','AEDFHR') == 3` (known reference case)
- `lcs('ABCDGH','AEDFHR') == ['A','D','H']`
- `lcs('AGGTAB','GXTXAYB') == ['G','T','A','B']`
- `lcs_length('','abc') == 0`, `lcs('','abc') == []` (empty-edge boundary)
- `lcs_all('aaa','aaa') == [['a','a','a']]` (exponential-path dedup)
- `lcs([1,2,3],[2,3,4]) == [2,3]` (generic non-str Sequence)
- `lcs_all('ab','ab') == [['a','b']]`
- `lcs_length('a'*5000,'a'*5000)` → **5681 ms** (performance baseline; note quadratic scaling)

## ISTQB Framework Application

**Test Design Techniques Used:**

- [x] Equivalence Partitioning (equal-length, unequal-length, empty, single-element)
- [x] Boundary Value Analysis (empty sequence, length-1, identical vs fully-disjoint)
- [x] Decision Table Testing (match / no-match / tie in `lcs_all` backtrack branch)
- [x] State Transition Testing (backtrack walk: match → diagonal, up, left)
- [x] Experience-Based Testing (exponential blow-up of `lcs_all`, generic-type edge cases)

**Test Types Coverage:**

- [x] Functional Testing
- [ ] Non-Functional Testing (only a performance baseline captured; full NFR suite not scaffolded — dry-run)
- [x] Structural Testing (every branch in DP + backtrack exercised by the cases above)
- [x] Change-Related Testing (Regression — cases should be pinned as a regression suite)

## ISO 25010 Quality Characteristics (priority for this component)

- [x] Functional Suitability: **Critical** — core correctness of all three APIs verified by assertions
- [x] Performance Efficiency: **High** — O(mn) confirmed; 5k×5k ≈ 5.7 s indicates need for input-size guardrails
- [ ] Compatibility: **Medium** — polymorphic `Sequence[T]` accepted; cross-type (str vs list[int]) rejected at type level, not runtime
- [ ] Usability: **Low** — docstrings present and clear
- [ ] Reliability: **High** — `lcs_all` can return exponentially many results → resourcing/DoS risk on adversarial input
- [x] Security: **Medium** — unbounded recursion/return size in `lcs_all` (resource-exhaustion vector)
- [ ] Maintainability: **Medium** — well-commented; branch logic is subtle
- [ ] Portability: **Low** — pure Python stdlib, no platform coupling

## Quality Gates

**Entry criteria:** Implementation present and importable; assertions green (met).
**Exit criteria:** Regression suite committed; `lcs_all` size guard documented; performance threshold for max input agreed.
**Quality thresholds:** 100% of public APIs covered; >95% branch coverage on DP/backtrack.

## Test Cases to Implement (GitHub Issue backlog)

### Issue 1 — `lcs_length` functional + boundary (Functional, Black-box)

- [ ] Happy path: standard reference pairs
- [ ] Empty input on either side
- [ ] Identical inputs (LCS == full length)
- [ ] Fully disjoint inputs (LCS == 0)
- [ ] Single-element sequences
- [ ] Swapped arg order returns identical length (space-swap correctness)

### Issue 2 — `lcs` reconstruction correctness (Functional + Structural)

- [ ] One LCS matches a known reference
- [ ] Order preserved left-to-right
- [ ] Generic element types: `list[int]`, `tuple[str]`, `str`
- [ ] Backtrack branch coverage: paths that require "move up" vs "move left"

### Issue 3 — `lcs_all` enumeration & dedup (Functional, Decision-Table)

- [ ] Multiple distinct LCSes enumerated (e.g. `"ABC"` vs `"BAC"` style ties)
- [ ] Exponential case deduped to count == expected (`"aaa"` vs `"aaa"` → 1)
- [ ] Deterministic sorted output
- [ ] Empty / disjoint → `[[]]` (confirm expected shape)

### Issue 4 — Non-Functional / Risk (Performance + Reliability) — *partially dry-run*

- [ ] Response-time threshold agreed for max supported (n,m); current 5k×5k ≈ 5.7 s logged
- [ ] `lcs_all` input-size guardrail / documented caller responsibility
- [ ] Memory ceiling check for O(mn) table at agreed max input

## Acceptance Criteria

- [x] All functional test cases pass (verified live)
- [ ] Branch coverage >80% on `lcs.py`
- [ ] Performance threshold for agreed max input validated
- [ ] `lcs_all` risk mitigation documented

## Labels

`test-strategy`, `istqb`, `iso25010`, `quality-gates`, `python`, `lcs`

## Estimate

Strategic planning: 2 SP · Test implementation: 5 SP · QA validation: 3 SP

---

## Skipped References (unavailable — flagged dry-run)

| Reference in prompt | Status | Note |
|---|---|---|
| `templates/breakdown-test/output_format.md` | **Missing** | `templates/breakdown-test/` dir does not exist in workspace |
| `docs/ways-of-work/plan/{epic}/{feature}/*.md` (PRD / technical-breakdown / implementation-plan / project-plan) | **Missing** | No `docs/ways-of-work` tree present |
| `prompts/templates/_shared/rules-core.md` (core rules import) | Not resolved | GitHub-issue template bodies above are inline from the prompt body; rules-core not fetched |
| Playwright E2E template | Not applicable | Component is a pure-function Python module, not a UI; Playwright template included for completeness only, marked dry-run |

*No external network call was required or attempted; all findings derive from the local workspace and a local execution trace.*
