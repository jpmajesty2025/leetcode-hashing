import pytest
from hypothesis import given, strategies as st

from subarray_sum_eq_k import subarray_sum


def _reference_subarray_sum(nums: list[int], k: int) -> int:
    total = 0

    for start in range(len(nums)):
        running = 0
        for end in range(start, len(nums)):
            running += nums[end]
            if running == k:
                total += 1

    return total


@pytest.mark.parametrize(
    "nums, k, expected",
    [
        ([1, 1, 1], 2, 2),
        ([1, 2, 3], 3, 2),
        ([1], 0, 0),
        ([-1, -1, 1], 0, 1),
        ([0, 0, 0], 0, 6),
        ([3, 4, 7, 2, -3, 1, 4, 2], 7, 4),
    ],
)
def test_subarray_sum_examples(nums: list[int], k: int, expected: int) -> None:
    assert subarray_sum(nums, k) == expected


@given(
    nums=st.lists(st.integers(min_value=-20, max_value=20), min_size=1, max_size=40),
    k=st.integers(min_value=-200, max_value=200),
)
def test_subarray_sum_matches_reference(nums: list[int], k: int) -> None:
    assert subarray_sum(nums, k) == _reference_subarray_sum(nums, k)
