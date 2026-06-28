import pytest
from hypothesis import given, strategies as st

from count_k_nice_subarrays import number_of_subarrays


def _reference_number_of_subarrays(nums: list[int], k: int) -> int:
    total = 0
    for start in range(len(nums)):
        odd_count = 0
        for end in range(start, len(nums)):
            odd_count += nums[end] % 2
            if odd_count == k:
                total += 1
            elif odd_count > k:
                break
    return total


@pytest.mark.parametrize(
    "nums,k,expected",
    [
        ([1, 1, 2, 1, 1], 3, 2),
        ([2, 4, 6], 1, 0),
        ([2, 2, 2, 1, 2, 2, 1, 2, 2, 2], 2, 16),
        ([1], 1, 1),
        ([2], 1, 0),
        ([1, 1, 1], 1, 3),
        ([1, 1, 1], 3, 1),
        ([2, 2, 2, 2], 2, 0),
        ([1, 2, 1, 2, 1], 2, 4),
    ],
)
def test_number_of_subarrays_examples_and_edge_cases(nums, k, expected):
    assert number_of_subarrays(nums, k) == expected


@given(
    case=st.lists(
        st.integers(min_value=1, max_value=100_000),
        min_size=1,
        max_size=60,
    ).flatmap(lambda nums: st.tuples(st.just(nums), st.integers(min_value=1, max_value=len(nums))))
)
def test_number_of_subarrays_matches_reference(case):
    nums, k = case
    expected = _reference_number_of_subarrays(nums, k)
    assert number_of_subarrays(nums, k) == expected


@given(nums=st.lists(st.integers(min_value=2, max_value=100_000).filter(lambda x: x % 2 == 0), min_size=1, max_size=80))
def test_all_even_inputs_have_zero_nice_subarrays(nums):
    assert number_of_subarrays(nums, 1) == 0
