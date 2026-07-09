"""Longest Common Subsequence (LCS) — beginner-friendly tutorial version.

The LONGEST COMMON SUBSEQUENCE of two sequences is the longest sequence of
items that appears (in the same *order*, but not necessarily *contiguous*) in
both. For example:

    "ABCBDAB"  and  "BDCABA"
                 ->  "BCBA", "BCAB", "BDAB"  (each length 4)

This module shows three variations of the classic dynamic-programming solution:
  1. lcs_length(...)  — just the length, uses minimal memory
  2. lcs(...)         — one longest subsequence, keeps a full table to backtrack
  3. lcs_all(...)     — every longest subsequence (can be very many!)

Run this file directly (`python lcs_tutorial.py`) for a small demo.
"""

from collections.abc import Sequence
from typing import TypeVar

# `Sequence` is any read-only, indexable collection (list, tuple, str...).
# `TypeVar` lets the *same* element type flow from inputs to outputs, so the
# returned subsequence keeps the type of the inputs (str in, str out).
T = TypeVar("T")


# ---------------------------------------------------------------------------
# 1) LENGTH ONLY  —  O(m*n) time, O(min(m, n)) space
# ---------------------------------------------------------------------------
def lcs_length(a: Sequence[T], b: Sequence[T]) -> int:
    """Return the *length* of the longest common subsequence of a and b.

    We only ever need the previous row to compute the next one, so we swap the
    two inputs to make `b` the SHORTER sequence. That bounds the rolling array
    to len(b)+1 cells instead of len(a)+1 — the only memory optimization here.
    """
    # Make `b` the shorter of the two so the rolling row stays small.
    if len(a) < len(b):
        a, b = b, a

    m, n = len(a), len(b)
    # `prev` = DP values for the previous row. n+1 columns (1-indexed),
    # initialized to 0 = base case "empty prefix shares length-0 subsequence".
    prev = [0] * (n + 1)

    # Each `i` is a character of `a`; we build one row at a time.
    for i in range(m):
        cur = [0] * (n + 1)          # current row, starts at the column-0 base case
        for j in range(n):
            if a[i] == b[j]:
                # Match: extend the best answer for the prefixes before both.
                cur[j + 1] = prev[j] + 1
            else:
                # No match: keep the best of skipping a[i] or skipping b[j].
                cur[j + 1] = max(prev[j + 1], cur[j])
        prev = cur                  # discard the old row -> space stays O(n)

    return prev[n]                  # = dp[m][n] = LCS length for full sequences


# ---------------------------------------------------------------------------
# 2) ONE SUBSEQUENCE  —  O(m*n) time, O(m*n) space (full table for backtrack)
# ---------------------------------------------------------------------------
def lcs(a: Sequence[T], b: Sequence[T]) -> list[T]:
    """Return *one* longest common subsequence of a and b.

    Unlike lcs_length, we keep the ENTIRE 2-D table so we can walk backward
    from dp[m][n] to recover which characters belong to the subsequence.
    """
    m, n = len(a), len(b)
    # dp[i][j] = LCS length of a[:i] and b[:j]. Extra +1 row/col = empty-prefix
    # base case and lets us index naturally with 1-based i, j.
    dp = [[0] * (n + 1) for _ in range(m + 1)]

    for i in range(m):
        for j in range(n):
            if a[i] == b[j]:
                dp[i + 1][j + 1] = dp[i][j] + 1
            else:
                dp[i + 1][j + 1] = max(dp[i][j + 1], dp[i + 1][j])

    # Backtrack from the bottom-right corner (full sequences) to (0, 0).
    i, j = m, n
    result: list[T] = []
    while i > 0 and j > 0:
        if a[i - 1] == b[j - 1]:
            # This character was a match on the optimal path -> keep it.
            result.append(a[i - 1])
            i -= 1
            j -= 1
        elif dp[i - 1][j] >= dp[i][j - 1]:
            i -= 1                      # better subproblem dropped a[i] -> go up
        else:
            j -= 1                      # better subproblem dropped b[j] -> go left

    result.reverse()                   # we collected matches end-first
    return result


# ---------------------------------------------------------------------------
# 3) ALL SUBSEQUENCES  —  O(m*n) time, but possibly exponential output
# ---------------------------------------------------------------------------
def lcs_all(a: Sequence[T], b: Sequence[T]) -> list[list[T]]:
    """Return *all* longest common subsequences of a and b.

    WARNING: can be exponentially many (e.g. "aaa" vs "aaa"). Use sparingly.
    """
    m, n = len(a), len(b)
    dp = [[0] * (n + 1) for _ in range(m + 1)]

    for i in range(m):
        for j in range(n):
            if a[i] == b[j]:
                dp[i + 1][j + 1] = dp[i][j] + 1
            else:
                dp[i + 1][j + 1] = max(dp[i][j + 1], dp[i + 1][j])

    # Walk backward collecting EVERY maximal path. We branch on ties, so this
    # is exponential in the worst case. `set` removes duplicate paths that are
    # reached through different orderings.
    def backtrack(i: int, j: int) -> set[tuple[T, ...]]:
        if i == 0 or j == 0:
            return {()}                        # empty prefix -> one empty subsequence
        if a[i - 1] == b[j - 1]:
            return {sub + (a[i - 1],) for sub in backtrack(i - 1, j - 1)}
        results: set[tuple[T, ...]] = set()
        if dp[i - 1][j] == dp[i][j]:           # tie going up? explore it
            results |= backtrack(i - 1, j)
        if dp[i][j - 1] == dp[i][j]:           # tie going left? explore it
            results |= backtrack(i, j - 1)
        return results

    # Sort the unique tuples so output is deterministic and easy to test.
    return [list(t) for t in sorted(backtrack(m, n))]


# ---------------------------------------------------------------------------
# Demo
# ---------------------------------------------------------------------------
if __name__ == "__main__":
    a = "ABCBDAB"
    b = "BDCABA"
    print("a =", a)
    print("b =", b)
    print("lcs_length ->", lcs_length(a, b))
    print("lcs        ->", "".join(lcs(a, b)))
    print("lcs_all    ->", ["".join(x) for x in lcs_all(a, b)])
