import pytest
from hypothesis import given, strategies as st

from intersection_of_multiple_arrays_iii import intersection_multiple_arrays


def _reference_intersection(nums: list[list[int]]) -> list[int]:
    if not nums:
        return []
    common = set(nums[0])
    for row in nums[1:]:
        common &= set(row)
    return sorted(common)


@pytest.mark.parametrize(
    "nums,expected",
    [
        ([[3, 1, 2, 4, 5], [1, 2, 3, 4], [3, 4, 5, 6]], [3, 4]),
        ([], []),
        ([[5, 1, 3]], [1, 3, 5]),
        ([[1, 2, 3], [4, 5, 6]], []),
        ([[2, 1], [1, 2], [2, 1]], [1, 2]),
        ([[-3, -1, 0], [-1, 0, 2], [0, -1, 5]], [-1, 0]),
    ],
)
def test_intersection_multiple_arrays_iii_examples(nums, expected):
    assert intersection_multiple_arrays(nums) == expected


@given(
    nums=st.lists(
        st.lists(
            st.integers(min_value=-200, max_value=200),
            unique=True,
            max_size=20,
        ),
        max_size=20,
    )
)
def test_intersection_multiple_arrays_iii_matches_reference(nums):
    result = intersection_multiple_arrays(nums)
    expected = _reference_intersection(nums)

    assert result == expected
    assert result == sorted(result)
    assert len(result) == len(set(result))
