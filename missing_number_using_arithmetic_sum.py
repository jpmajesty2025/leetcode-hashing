'''
Given an array nums containing n distinct numbers in the range [0, n], return the only number in the range that is missing from the array.
'''
from typing import List


def missing_number(nums: List[int]) -> int:
    """Return the missing value from the range [0, n] using arithmetic sum."""
    n = len(nums)
    expected_sum = n * (n + 1) // 2
    actual_sum = sum(nums)
    return expected_sum - actual_sum