import pytest
from hypothesis import given, strategies as st

from check_adjacent_nums import find_numbers


def _reference_find_numbers(nums: list[int]) -> set[int]:
    nums_set = set(nums)
    return {
        num
        for num in nums_set
        if (num - 1 not in nums_set) and (num + 1 not in nums_set)
    }


@pytest.mark.parametrize(
    "nums,expected",
    [
        ([1, 3, 5], {1, 3, 5}),
        ([1, 2, 3], set()),
        ([1, 1, 3, 3, 5], {1, 3, 5}),
        ([0, 2, 4, 5], {0, 2}),
        ([-3, -1, 1, 2], {-3, -1}),
        ([], set()),
    ],
)
def test_find_numbers_examples(nums, expected):
    assert set(find_numbers(nums)) == expected


@given(nums=st.lists(st.integers(min_value=-1_000, max_value=1_000), max_size=200))
def test_find_numbers_matches_reference(nums):
    result = find_numbers(nums)
    result_set = set(result)
    input_set = set(nums)
    expected = _reference_find_numbers(nums)

    # Matches reference behavior.
    assert result_set == expected

    # Output is unique (no duplicates).
    assert len(result) == len(result_set)

    # Every result value exists in the input and is isolated from +/-1.
    for value in result_set:
        assert value in input_set
        assert value - 1 not in input_set
        assert value + 1 not in input_set
