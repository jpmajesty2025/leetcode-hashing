'''
Given an integer array arr, count how many elements x there are, such that x + 1 is also in arr. If there are duplicates in arr, count them separately.

 

Example 1:

Input: arr = [1,2,3]
Output: 2
Explanation: 1 and 2 are counted cause 2 and 3 are in arr.
Example 2:

Input: arr = [1,1,3,3,5,5,7,7]
Output: 0
Explanation: No numbers are counted, cause there is no 2, 4, 6, or 8 in arr.

Input: arr = [1,1,1,2,2,3]
Output: 5
Explanation: Each of the three 1's matches a 2 and each of the two 2's matches a 3.
'''
from typing import List


def count_elements(arr: List[int]) -> int:
    """Count elements x such that x + 1 is also present in arr."""
    num_set = set(arr)
    return sum(1 for x in arr if x + 1 in num_set)