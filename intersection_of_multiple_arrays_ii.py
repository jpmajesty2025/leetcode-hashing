'''
Given a 2D array nums that contains n arrays of distinct integers, return a sorted array containing all the numbers that appear in all n arrays.

For example, given nums = [[3,1,2,4,5],[1,2,3,4],[3,4,5,6]], return [3, 4]. 3 and 4 are the only numbers that are in all arrays.
'''
from typing import List

def intersection_multiple_arrays(nums: List[List[int]]) -> List[int]:
    """Return sorted values that appear in every row of nums."""
    return sorted(set.intersection(*(set(num) for num in nums))) if nums else []