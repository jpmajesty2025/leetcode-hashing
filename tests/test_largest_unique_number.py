import pytest
from hypothesis import given, strategies as st

from largest_unique_number import largestUniqueNumber


def _reference_largest_unique_number(nums: list[int]) -> int:
    counts: dict[int, int] = {}
    for num in nums:
        counts[num] = counts.get(num, 0) + 1

    best = -1
    for num, count in counts.items():
        if count == 1 and num > best:
            best = num
    return best


@pytest.mark.parametrize(
    "nums,expected",
    [
        ([5, 7, 3, 9, 4, 9, 8, 3, 1], 8),
        ([9, 9, 8, 8], -1),
        ([1], 1),
        ([0], 0),
        ([0, 0, 1], 1),
        ([2, 2, 3, 3, 4], 4),
        ([10, 9, 10, 8, 8], 9),
    ],
)
def test_largest_unique_number_examples(nums, expected):
    assert largestUniqueNumber(nums) == expected


@given(nums=st.lists(st.integers(min_value=0, max_value=1000), min_size=1, max_size=200))
def test_largest_unique_number_matches_reference(nums):
    assert largestUniqueNumber(nums) == _reference_largest_unique_number(nums)


@given(nums=st.lists(st.integers(min_value=0, max_value=1000), min_size=1, max_size=200))
def test_largest_unique_number_result_invariants(nums):
    result = largestUniqueNumber(nums)
    counts: dict[int, int] = {}
    for num in nums:
        counts[num] = counts.get(num, 0) + 1

    if result == -1:
        assert all(count != 1 for count in counts.values())
    else:
        assert counts[result] == 1
        assert all(num <= result for num, count in counts.items() if count == 1)