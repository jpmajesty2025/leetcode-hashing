import pytest
from hypothesis import given, strategies as st

from counting_elements import count_elements


def _reference_count_elements(arr: list[int]) -> int:
    counts: dict[int, int] = {}
    for value in arr:
        counts[value] = counts.get(value, 0) + 1
    return sum(freq for value, freq in counts.items() if value + 1 in counts)


@pytest.mark.parametrize(
    "arr,expected",
    [
        ([1, 2, 3], 2),
        ([1, 1, 3, 3, 5, 5, 7, 7], 0),
        ([1, 1, 1, 2, 2, 3], 5),
        ([], 0),
        ([10], 0),
        ([0, 0, 1], 2),
        ([-2, -1, -1, 0], 3),
    ],
)
def test_count_elements_examples(arr, expected):
    assert count_elements(arr) == expected


@given(arr=st.lists(st.integers(min_value=-1_000, max_value=1_000), max_size=200))
def test_count_elements_matches_reference(arr):
    result = count_elements(arr)
    expected = _reference_count_elements(arr)

    assert result == expected
    assert 0 <= result <= len(arr)
