import pytest
from hypothesis import given, strategies as st

from missing_number_using_arithmetic_sum import missing_number


@st.composite
def valid_missing_number_case(draw):
    n = draw(st.integers(min_value=0, max_value=200))
    missing = draw(st.integers(min_value=0, max_value=n))
    nums = [x for x in range(n + 1) if x != missing]
    return nums, missing


@pytest.mark.parametrize(
    "nums,expected",
    [
        ([3, 0, 1], 2),
        ([0, 1], 2),
        ([9, 6, 4, 2, 3, 5, 7, 0, 1], 8),
        ([0], 1),
        ([1], 0),
        ([], 0),
    ],
)
def test_missing_number_arithmetic_examples(nums, expected):
    assert missing_number(nums) == expected


@given(case=valid_missing_number_case())
def test_missing_number_arithmetic_property(case):
    nums, expected = case
    result = missing_number(nums)

    assert result == expected
    assert 0 <= result <= len(nums)
    assert result not in nums

    # Order invariance check.
    assert missing_number(list(reversed(nums))) == expected
