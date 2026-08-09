"""Small pure utilities that are easy to document and test."""

from __future__ import annotations


def clamp_score(value: int) -> int:
    """Clamp a score to the inclusive 0..100 range.

    >>> clamp_score(105)
    100
    >>> clamp_score(-4)
    0
    >>> clamp_score(72)
    72
    """
    return max(0, min(100, value))
