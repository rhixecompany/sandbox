# Tutorial: The Longest Common Subsequence (LCS) in Python

> **Source file:** `lcs.py` (refactored & commented into `results/lcs_tutorial.py`)
> **What you'll learn:** how dynamic programming (DP) finds the longest common
> subsequence, why one variant saves memory, and how to recover the actual
> answer by backtracking.

---

## 1. What is a "subsequence"?

A **subsequence** keeps items in order but allows gaps. Compare:

| term | example from `"ABCBDAB"` |
|------|--------------------------|
| substring (contiguous) | `"CBD"` |
| subsequence (in order, gaps OK) | `"BCBA"` — letters pulled from positions 2,3,5,7 |

The **Longest Common Subsequence** of two sequences is the longest sequence
that appears *in order* in **both**. For `"ABCBDAB"` and `"BDCABA"` the answer
has length **4**, and there are three of them: `"BCAB"`, `"BCBA"`, `"BDAB"`.

LCS shows up in diff tools, bioinformatics (gene alignment), and version control.

---

## 2. The idea: a 2-D DP table

Let `dp[i][j]` = length of the LCS of `a[:i]` and `b[:j]` (the first `i` chars
of `a` and first `j` chars of `b`). The empty prefixes give `dp[0][*] = dp[*][0] = 0`.

For each pair `(a[i-1], b[j-1])` we apply one rule:

```
if a[i-1] == b[j-1]:
    dp[i][j] = dp[i-1][j-1] + 1        # characters match -> extend
else:
    dp[i][j] = max(dp[i-1][j], dp[i][j-1])   # else skip one side
```

That single rule, filled left-to-right / top-to-bottom, is the whole algorithm.

---

## 3. Variation 1 — length only (`lcs_length`)

Goal: report the **length**, using as little memory as possible. Because row
`i` only depends on row `i-1`, we keep just **one rolling row** instead of the
whole table. Swapping the inputs so the shorter one is `b` caps that row at
`len(b)+1` cells → **O(min(m,n))** space.

```python
def lcs_length(a, b):
    if len(a) < len(b):
        a, b = b, a            # make b the shorter sequence
    m, n = len(a), len(b)
    prev = [0] * (n + 1)       # one rolling row
    for i in range(m):
        cur = [0] * (n + 1)
        for j in range(n):
            if a[i] == b[j]:
                cur[j + 1] = prev[j] + 1
            else:
                cur[j + 1] = max(prev[j + 1], cur[j])
        prev = cur             # discard the old row
    return prev[n]             # = dp[m][n]
```

**Complexity:** time O(m·n), space O(min(m, n)).

---

## 4. Variation 2 — recover one subsequence (`lcs`)

To get the *actual* answer (not just its length) we must remember the **full
table**, so we can walk backward from `dp[m][n]` to `(0,0)`:

- If the two current characters match, it was part of the LCS → keep it, move
  diagonally up-left.
- Otherwise follow the larger of the two neighbor cells (up or left).

```python
def lcs(a, b):
    m, n = len(a), len(b)
    dp = [[0] * (n + 1) for _ in range(m + 1)]
    for i in range(m):
        for j in range(n):
            if a[i] == b[j]:
                dp[i+1][j+1] = dp[i][j] + 1
            else:
                dp[i+1][j+1] = max(dp[i][j+1], dp[i+1][j])
    i, j = m, n
    result = []
    while i > 0 and j > 0:
        if a[i-1] == b[j-1]:
            result.append(a[i-1]); i -= 1; j -= 1
        elif dp[i-1][j] >= dp[i][j-1]:
            i -= 1
        else:
            j -= 1
    result.reverse()           # we collected matches end-first
    return result
```

**Complexity:** time O(m·n), space O(m·n) (the full table).

---

## 5. Variation 3 — all subsequences (`lcs_all`)

When two subproblems *tie* at the optimal value, **both branches can be part of
a valid LCS**. A recursive `backtrack` that branches on ties collects every
maximal path. We dedupe with a `set` and sort for deterministic output.

```python
def lcs_all(a, b):
    # ... build dp table exactly as in lcs() ...
    def backtrack(i, j):
        if i == 0 or j == 0:
            return {()}
        if a[i-1] == b[j-1]:
            return {sub + (a[i-1],) for sub in backtrack(i-1, j-1)}
        results = set()
        if dp[i-1][j] == dp[i][j]:
            results |= backtrack(i-1, j)
        if dp[i][j-1] == dp[i][j]:
            results |= backtrack(i, j-1)
        return results
    return [list(t) for t in sorted(backtrack(m, n))]
```

⚠️ **Warning:** the number of answers can be **exponential** (e.g. `"aaa"` vs
`"aaa"`). Use only on small inputs.

---

## 6. Run it

```bash
python results/lcs_tutorial.py
```

```
a = ABCBDAB
b = BDCABA
lcs_length -> 4
lcs        -> BCBA
lcs_all    -> ['BCAB', 'BCBA', 'BDAB']
```

---

## 7. Cheat sheet

| function | returns | space | notes |
|----------|---------|-------|-------|
| `lcs_length` | `int` (length) | O(min(m,n)) | fastest, lowest memory |
| `lcs` | `list` (one answer) | O(m·n) | backtracks from full table |
| `lcs_all` | `list[list]` (all) | O(m·n) + output | exponential worst-case |

**Key takeaways**
1. DP trades a 2-D table for an efficient O(m·n) solution.
2. You only need the previous row if you don't need the answer itself → save memory.
3. Keep the full table + backtrack to recover *which* characters form the LCS.
4. Branch on ties to enumerate *every* optimal answer — but watch out for blow-up.
