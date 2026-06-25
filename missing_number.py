'''
Given an array nums containing n distinct numbers in the range [0, n], return the only number in the range that is missing from the array.
'''
from typing import List


def missing_number(nums: List[int]) -> int:
    num_set = set(nums)
    for num in range(len(nums) + 1):
        if num not in num_set:
            return num
    raise ValueError("Input must contain exactly one missing number in [0, n].")