'''
Given an array of integers nums and an integer k. A continuous subarray is called nice if there are k odd numbers on it.

Return the number of nice sub-arrays.

 

Example 1:

Input: nums = [1,1,2,1,1], k = 3
Output: 2
Explanation: The only sub-arrays with 3 odd numbers are [1,1,2,1] and [1,2,1,1].
Example 2:

Input: nums = [2,4,6], k = 1
Output: 0
Explanation: There are no odd numbers in the array.
Example 3:

Input: nums = [2,2,2,1,2,2,1,2,2,2], k = 2
Output: 16
 

Constraints:

1 <= nums.length <= 50000
1 <= nums[i] <= 10^5
1 <= k <= nums.length
'''
from collections import defaultdict
from typing import List

def number_of_subarrays(nums: List[int], k: int) -> int:
    """Count subarrays containing exactly ``k`` odd numbers in O(n) time."""
    prefix_odd_counts = defaultdict(int)
    prefix_odd_counts[0] = 1
    total_subarrays = curr_odd_count = 0
    for i, num in enumerate(nums):
        curr_odd_count += num % 2
        # Any previous prefix with (curr_odd_count - k) odds forms a valid subarray.
        total_subarrays += prefix_odd_counts[curr_odd_count - k]
        prefix_odd_counts[curr_odd_count] += 1
    return total_subarrays