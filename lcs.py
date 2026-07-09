"""Longest Common Subsequence (LCS) utilities.

LCS length via classic DP O(mn) time, O(min(m,n)) space.
Reconstruction uses full O(mn) table.
"""

# `Sequence` is an abstract, read-only collection type (list, tuple, str all qualify).
# Using it instead of `list` keeps these functions generic across any ordered, indexable type.
from collections.abc import Sequence

# `TypeVar` creates a "type variable" so the SAME element type flows from input to output.
# If `a` is a list[str], then `T` becomes str everywhere below and the returned result is also str-based.
from typing import TypeVar

# Declare a single unbounded type variable. The capital letter is a convention, not a requirement.
T = TypeVar("T")


def lcs_length(a: Sequence[T], b: Sequence[T]) -> int:
    """Return the length of the longest common subsequence between *a* and *b*.

    Uses DP with O(min(m,n)) space — no reconstruction possible from this
    call alone.
    """
    # Goal: minimize memory. We only ever need the previous row to compute the
    # next one, so we swap `a`/`b` to make `b` the SHORTER sequence. That bounds
    # the rolling row array to len(b)+1 cells instead of len(a)+1.
    # ensure b is the shorter sequence for O(min(m,n)) space
    if len(a) < len(b):
        a, b = b, a

    # `m` and `n` are the classic DP names for the two string/sequence lengths.
    m, n = len(a), len(b)
    # `prev` holds the DP values for the previous row (1-indexed columns, hence n+1).
    # Initializing with zeros represents the base case: an empty prefix of `a`
    # shares length-0 subsequence with any prefix of `b`.
    prev = [0] * (n + 1)

    # Outer loop walks the rows (each character of `a`); note we index `a[i]`.
    for i in range(m):
        # `cur` is the row we are building for the current `i`. It starts all zeros,
        # which is the correct base case for column 0 (empty prefix of `b`).
        cur = [0] * (n + 1)
        for j in range(n):
            if a[i] == b[j]:
                # Characters match: extend the subsequence found for the prefixes
                # before these characters by 1. `prev[j]` is dp[i][j].
                cur[j + 1] = prev[j] + 1
            else:
                # No match: carry forward the best length seen so far from either
                # dropping the current `a` character (`prev[j+1]`) or the current
                # `b` character (`cur[j]`).
                cur[j + 1] = max(prev[j + 1], cur[j])
        # Promote the row we just finished to "previous" for the next iteration.
        # Because we discard the older row, total space stays O(n).
        prev = cur

    # After the last row, `prev[n]` holds dp[m][n] = the LCS length for full sequences.
    return prev[n]


def lcs(a: Sequence[T], b: Sequence[T]) -> list[T]:
    """Return one longest common subsequence of *a* and *b*.

    Full DP table (O(mn) space) is built to allow backtracking.
    """
    m, n = len(a), len(b)
    # Unlike `lcs_length`, we keep the ENTIRE 2-D table so we can walk backward
    # from dp[m][n] to recover which characters belong to the subsequence.
    # `dp[i][j]` = LCS length of a[:i] and b[:j]. The extra +1 row/col is the
    # empty-prefix base case and lets us index naturally with i, j (1-based).
    dp = [[0] * (n + 1) for _ in range(m + 1)]

    # Build the table forward, exactly like the length variant but storing every row.
    for i in range(m):
        for j in range(n):
            if a[i] == b[j]:
                # Match: take the answer for the prefixes before both characters, +1.
                dp[i + 1][j + 1] = dp[i][j] + 1
            else:
                # No match: best of "skip a[i]" (dp[i][j+1]) or "skip b[j]" (dp[i+1][j]).
                dp[i + 1][j + 1] = max(dp[i][j + 1], dp[i + 1][j])

    # backtrack
    # Start at the bottom-right corner (full sequences) and walk to (0,0).
    i, j = m, n
    result: list[T] = []
    while i > 0 and j > 0:
        if a[i - 1] == b[j - 1]:
            # This character was a match on the path, so it belongs to the LCS.
            # Append it, then move diagonally up-left past both matched characters.
            result.append(a[i - 1])
            i -= 1
            j -= 1
        elif dp[i - 1][j] >= dp[i][j - 1]:
            # No match here and the better subproblem came from dropping `a[i]`,
            # so move up one row.
            i -= 1
        else:
            # Otherwise the better subproblem came from dropping `b[j]`; move left.
            j -= 1

    # We appended matches in reverse order (end of sequence first), so reverse
    # to restore the original left-to-right order.
    result.reverse()
    return result


def lcs_all(a: Sequence[T], b: Sequence[T]) -> list[list[T]]:
    """Return *all* longest common subsequences of *a* and *b*.

    May return exponentially many results — use sparingly.
    """
    m, n = len(a), len(b)
    # Same full table as `lcs`; we need it to explore every equally-optimal path.
    dp = [[0] * (n + 1) for _ in range(m + 1)]

    for i in range(m):
        for j in range(n):
            if a[i] == b[j]:
                dp[i + 1][j + 1] = dp[i][j] + 1
            else:
                dp[i + 1][j + 1] = max(dp[i][j + 1], dp[i + 1][j])

    # Inner helper that walks backward collecting EVERY maximal path. Because we
    # branch whenever two subproblems tie at the optimal value, this is exponential
    # in the worst case (e.g., "aaa" vs "aaa"). `set` deduplicates identical paths
    # reached through different orderings.
    def backtrack(i: int, j: int) -> set[tuple[T, ...]]:
        # Base case: reached an empty prefix on either side -> one empty subsequence.
        if i == 0 or j == 0:
            return {()}
        if a[i - 1] == b[j - 1]:
            # Extend every subsequence from the diagonal subproblem with this match.
            return {sub + (a[i - 1],) for sub in backtrack(i - 1, j - 1)}
        results: set[tuple[T, ...]] = set()
        # If moving up keeps us at the optimal value, explore that branch too.
        if dp[i - 1][j] == dp[i][j]:
            results |= backtrack(i - 1, j)
        # Same for moving left.
        if dp[i][j - 1] == dp[i][j]:
            results |= backtrack(i, j - 1)
        return results

    # Sort the unique tuples so the output is deterministic and easy to test.
    return [list(t) for t in sorted(backtrack(m, n))]
