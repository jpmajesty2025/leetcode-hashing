'''
Given a 2D array nums that contains n arrays of distinct integers, return a sorted array containing all the numbers that appear in all n arrays.

For example, given nums = [[3,1,2,4,5],[1,2,3,4],[3,4,5,6]], return [3, 4]. 3 and 4 are the only numbers that are in all arrays.
'''
from typing import List
from collections import defaultdict

def intersection_multiple_arrays(nums: List[List[int]]) -> List[int]:
    counts = defaultdict(int)
    for arr in nums:
        for x in arr:
            counts[x] += 1

    n = len(nums)
    ans = []
    for key in counts:
        if counts[key] == n:
            ans.append(key)
    
    return sorted(ans)