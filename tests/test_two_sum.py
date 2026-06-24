import pytest
from hypothesis import given, strategies as st

from two_sum import two_sum


@pytest.mark.parametrize(
    "nums,target,expected_indices",
    [
        ([2, 7, 11, 15], 9, {0, 1}),
        ([3, 2, 4], 6, {1, 2}),
        ([3, 3], 6, {0, 1}),
        ([-3, 4, 3, 90], 0, {0, 2}),
        ([0, 4, 3, 0], 0, {0, 3}),
    ],
)
def test_two_sum_finds_valid_pair(nums, target, expected_indices):
    result = two_sum(nums, target)

    assert len(result) == 2
    assert result[0] != result[1]
    assert nums[result[0]] + nums[result[1]] == target
    assert set(result) == expected_indices


def test_two_sum_returns_fallback_when_no_solution():
    assert two_sum([1, 2, 3], 7) == [-1, -1]


@given(
    x=st.integers(min_value=-10_000, max_value=10_000),
    y=st.integers(min_value=-10_000, max_value=10_000),
    filler_count=st.integers(min_value=0, max_value=20),
)
def test_two_sum_property_generated_cases(x, y, filler_count):
    """Property-style test: generated inputs should always return a valid solution pair."""
    target = x + y

    # Build filler values that cannot form target with themselves, x, or y.
    sentinel = target + 1
    while (
        sentinel in (x, y)
        or sentinel + x == target
        or sentinel + y == target
        or sentinel + sentinel == target
    ):
        sentinel += 1

    nums = [x, y] + [sentinel] * filler_count
    result = two_sum(nums, target)

    assert len(result) == 2
    assert result[0] != result[1]
    assert 0 <= result[0] < len(nums)
    assert 0 <= result[1] < len(nums)
    assert nums[result[0]] + nums[result[1]] == target
    assert set(result) == {0, 1}
