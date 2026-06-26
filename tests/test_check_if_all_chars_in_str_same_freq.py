from collections import Counter

import pytest
from hypothesis import given, strategies as st

from check_if_all_chars_in_str_same_freq import are_occurrences_equal


def _reference_are_occurrences_equal(s: str) -> bool:
    if not s:
        return True

    counts = Counter(s)
    frequencies = list(counts.values())
    return all(freq == frequencies[0] for freq in frequencies)


@pytest.mark.parametrize(
    "s, expected",
    [
        ("abacbc", True),
        ("aaabb", False),
        ("a", True),
        ("abc", True),
        ("aabbccc", False),
        ("", True),
    ],
)
def test_are_occurrences_equal_examples(s: str, expected: bool) -> None:
    assert are_occurrences_equal(s) is expected


@given(st.text(alphabet=st.characters(whitelist_categories=("Ll",)), min_size=0, max_size=200))
def test_are_occurrences_equal_matches_reference(s: str) -> None:
    assert are_occurrences_equal(s) == _reference_are_occurrences_equal(s)
