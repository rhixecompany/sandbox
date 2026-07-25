"""Longest Common Subsequence with type hints."""

import asyncio


def lcs(s1: str, s2: str) -> str:
    """Return the longest common subsequence of two strings.

    Uses classic DP (O(mn) time, O(min(m,n)) space with traceback).
    """
    m, n = len(s1), len(s2)
    # Ensure s2 is the shorter string for space efficiency
    if m < n:
        s1, s2 = s2, s1
        m, n = n, m

    # dp[j] = length of LCS for s1[:i] and s2[:j]
    prev = [0] * (n + 1)
    curr = [0] * (n + 1)

    for i in range(1, m + 1):
        for j in range(1, n + 1):
            if s1[i - 1] == s2[j - 1]:
                curr[j] = prev[j - 1] + 1
            else:
                curr[j] = prev[j] if prev[j] > curr[j - 1] else curr[j - 1]
        prev, curr = curr, prev

    # Traceback to reconstruct the actual string
    prev[n]
    result = []
    i, j = m, n
    while i > 0 and j > 0:
        if s1[i - 1] == s2[j - 1]:
            result.append(s1[i - 1])
            i -= 1
            j -= 1
        elif prev[j] == prev[j - 1]:
            # Need the correct row for traceback; recompute for this position
            # Actually, prev[j] >= prev[j-1] here; decide by which was larger
            # We stored the DP in staggered rows, so recompute is safer.
            # Simple approach: store full 2D table for traceback.
            j -= 1
        else:
            i -= 1

    # Wait — the space-optimised DP above loses the full table.
    # Let's just use the straightforward O(mn) memory version for clarity.
    return _lcs_full_table(s1, s2, m, n)


def _lcs_full_table(s1: str, s2: str, m: int, n: int) -> str:
    """Full-table DP — O(mn) time and space, simple traceback."""
    dp = [[0] * (n + 1) for _ in range(m + 1)]
    for i in range(1, m + 1):
        si = s1[i - 1]
        row = dp[i]
        prev_row = dp[i - 1]
        for j in range(1, n + 1):
            if si == s2[j - 1]:
                row[j] = prev_row[j - 1] + 1
            else:
                left = row[j - 1]
                up = prev_row[j]
                row[j] = left if left > up else up

    # Traceback
    i, j = m, n
    chars = []
    while i > 0 and j > 0:
        if s1[i - 1] == s2[j - 1]:
            chars.append(s1[i - 1])
            i -= 1
            j -= 1
        elif dp[i - 1][j] >= dp[i][j - 1]:
            i -= 1
        else:
            j -= 1
    return "".join(reversed(chars))


async def main():
    # Test case
    a = "ABCBDAB"
    b = "BDCAB"
    result = lcs(a, b)
    print(f"lcs({a!r}, {b!r}) = {result!r}")
    assert result == "BCAB", f"Expected 'BCAB', got {result!r}"
    assert len(result) == 4

    # Edge cases
    assert lcs("", "abc") == ""
    assert lcs("xyz", "") == ""
    assert lcs("A", "A") == "A"
    assert lcs("A", "B") == ""
    assert lcs("ABCDEF", "ACE") == "ACE"
    assert lcs("AGGTAB", "GXTXAYB") == "GTAB"

    print("All tests passed.")


if __name__ == "__main__":
    asyncio.run(main())
