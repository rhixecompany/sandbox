"""Longest Common Subsequence (LCS) utilities.

LCS length via classic DP O(mn) time, O(min(m,n)) space.
Reconstruction uses full O(mn) table.
"""

from collections.abc import Sequence
from typing import TypeVar

T = TypeVar("T")


def lcs_length(a: Sequence[T], b: Sequence[T]) -> int:
    """Return the length of the longest common subsequence between *a* and *b*.

    Uses DP with O(min(m,n)) space — no reconstruction possible from this
    call alone.
    """
    # ensure b is the shorter sequence for O(min(m,n)) space
    if len(a) < len(b):
        a, b = b, a

    m, n = len(a), len(b)
    prev = [0] * (n + 1)

    for i in range(m):
        cur = [0] * (n + 1)
        for j in range(n):
            if a[i] == b[j]:
                cur[j + 1] = prev[j] + 1
            else:
                cur[j + 1] = max(prev[j + 1], cur[j])
        prev = cur

    return prev[n]


def lcs(a: Sequence[T], b: Sequence[T]) -> list[T]:
    """Return one longest common subsequence of *a* and *b*.

    Full DP table (O(mn) space) is built to allow backtracking.
    """
    m, n = len(a), len(b)
    dp = [[0] * (n + 1) for _ in range(m + 1)]

    for i in range(m):
        for j in range(n):
            if a[i] == b[j]:
                dp[i + 1][j + 1] = dp[i][j] + 1
            else:
                dp[i + 1][j + 1] = max(dp[i][j + 1], dp[i + 1][j])

    # backtrack
    i, j = m, n
    result: list[T] = []
    while i > 0 and j > 0:
        if a[i - 1] == b[j - 1]:
            result.append(a[i - 1])
            i -= 1
            j -= 1
        elif dp[i - 1][j] >= dp[i][j - 1]:
            i -= 1
        else:
            j -= 1

    result.reverse()
    return result


def lcs_all(a: Sequence[T], b: Sequence[T]) -> list[list[T]]:
    """Return *all* longest common subsequences of *a* and *b*.

    May return exponentially many results — use sparingly.
    """
    m, n = len(a), len(b)
    dp = [[0] * (n + 1) for _ in range(m + 1)]

    for i in range(m):
        for j in range(n):
            if a[i] == b[j]:
                dp[i + 1][j + 1] = dp[i][j] + 1
            else:
                dp[i + 1][j + 1] = max(dp[i][j + 1], dp[i + 1][j])

    def backtrack(i: int, j: int) -> set[tuple[T, ...]]:
        if i == 0 or j == 0:
            return {()}
        if a[i - 1] == b[j - 1]:
            return {sub + (a[i - 1],) for sub in backtrack(i - 1, j - 1)}
        results: set[tuple[T, ...]] = set()
        if dp[i - 1][j] == dp[i][j]:
            results |= backtrack(i - 1, j)
        if dp[i][j - 1] == dp[i][j]:
            results |= backtrack(i, j - 1)
        return results

    return [list(t) for t in sorted(backtrack(m, n))]
