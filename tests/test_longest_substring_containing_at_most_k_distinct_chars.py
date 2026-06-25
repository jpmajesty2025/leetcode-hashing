import string

import pytest
from hypothesis import given, strategies as st

from longest_substring_containing_at_most_k_distinct_chars import longest_substring_k_distinct


def _reference_longest_substring_k_distinct(s: str, k: int) -> int:
    if k <= 0 or not s:
        return 0

    best = 0
    for left in range(len(s)):
        seen: set[str] = set()
        for right in range(left, len(s)):
            seen.add(s[right])
            if len(seen) > k:
                break
            best = max(best, right - left + 1)
    return best


@pytest.mark.parametrize(
    "s,k,expected",
    [
        ("eceba", 2, 3),
        ("aa", 1, 2),
        ("", 2, 0),
        ("abc", 0, 0),
        ("abc", 5, 3),
        ("a", 1, 1),
        ("abaccc", 2, 4),
        ("abaccc", 1, 3),
    ],
)
def test_longest_substring_k_distinct_examples(s, k, expected):
    assert longest_substring_k_distinct(s, k) == expected


@given(
    s=st.text(alphabet=string.ascii_lowercase, min_size=0, max_size=60),
    k=st.integers(min_value=0, max_value=30),
)
def test_longest_substring_k_distinct_matches_reference(s, k):
    result = longest_substring_k_distinct(s, k)
    expected = _reference_longest_substring_k_distinct(s, k)

    assert result == expected
    assert 0 <= result <= len(s)
