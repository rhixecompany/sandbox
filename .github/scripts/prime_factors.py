"""Functions for computing prime factors using recursion."""

from __future__ import annotations

import asyncio


def prime_factors(n: int) -> list[int]:
    """Return the prime factors of a positive integer using recursion.

    Recursively finds the smallest divisor (>= 2) of *n*, appends it to the
    result, and recurses on the quotient.  The base case (n == 1) returns an
    empty list.

    Parameters
    ----------
    n : int
        A positive integer (n >= 1) to factorise.

    Returns
    -------
    list[int]
        The prime factors in ascending order.  Returns an empty list for
        n == 1 (the number with no prime factors).

    Raises
    ------
    ValueError
        If *n* is less than 1.

    Examples
    --------
    >>> prime_factors(12)
    [2, 2, 3]
    >>> prime_factors(17)
    [17]
    >>> prime_factors(1)
    []
    >>> prime_factors(84)
    [2, 2, 3, 7]
    """
    if n < 1:
        raise ValueError(f"n must be >= 1, got {n}")
    if n == 1:
        return []

    smallest: int = _smallest_factor(n)
    return [smallest] + prime_factors(n // smallest)


def _smallest_factor(n: int) -> int:
    """Return the smallest prime divisor of *n* (*n* >= 2)."""
    for i in range(2, int(n**0.5) + 1):
        if n % i == 0:
            return i
    return n


async def main() -> None:
    """Demonstrate prime_factors with a few examples."""
    examples = [1, 12, 17, 84, 97, 100]
    for n in examples:
        print(f"prime_factors({n}) = {prime_factors(n)}")


if __name__ == "__main__":
    asyncio.run(main())
