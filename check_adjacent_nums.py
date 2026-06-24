'''
Given an integer array nums, find all the numbers x in nums that satisfy the following: x + 1 is not in nums, and x - 1 is not in nums.

If a valid number x appears multiple times, you only need to include it in the answer once.
'''
from typing import List


def find_numbers(nums: List[int]) -> List[int]:
    """Return unique numbers x where neither x - 1 nor x + 1 exists in nums."""
    isolated_numbers: List[int] = []
    nums_set = set(nums)

    for num in nums_set:
        if (num + 1 not in nums_set) and (num - 1 not in nums_set):
            isolated_numbers.append(num)

    return isolated_numbers