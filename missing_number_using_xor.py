'''
Given an array nums containing n distinct numbers in the range [0, n], return the only number in the range that is missing from the array.
'''
from typing import List


def missing_number(nums: List[int]) -> int:
    """Return the missing value from the range [0, n] using XOR cancellation."""
    missing = len(nums)
    for i, num in enumerate(nums):
        missing ^= i ^ num
    return missing
