import pytest
from hypothesis import given, strategies as st

from max_contiguous_subarray_with_eq_0_and_1 import findMaxLength


def _reference_find_max_length(nums: list[int]) -> int:
    best = 0
    for start in range(len(nums)):
        zeros = 0
        ones = 0
        for end in range(start, len(nums)):
            if nums[end] == 0:
                zeros += 1
            else:
                ones += 1
            if zeros == ones:
                best = max(best, end - start + 1)
    return best


@pytest.mark.parametrize(
    "nums,expected",
    [
        ([0, 1], 2),
        ([0, 1, 0], 2),
        ([0, 1, 1, 1, 1, 1, 0, 0, 0], 6),
        ([0], 0),
        ([1], 0),
        ([0, 0], 0),
        ([1, 1], 0),
        ([0, 0, 1, 1], 4),
        ([1, 0, 1, 0, 1, 0], 6),
    ],
)
def test_find_max_length_examples_and_edges(nums, expected):
    assert findMaxLength(nums) == expected


@given(nums=st.lists(st.integers(min_value=0, max_value=1), min_size=1, max_size=80))
def test_find_max_length_matches_reference(nums):
    assert findMaxLength(nums) == _reference_find_max_length(nums)


@given(nums=st.lists(st.integers(min_value=0, max_value=1), min_size=1, max_size=200))
def test_find_max_length_result_invariants(nums):
    result = findMaxLength(nums)
    assert 0 <= result <= len(nums)
    assert result % 2 == 0