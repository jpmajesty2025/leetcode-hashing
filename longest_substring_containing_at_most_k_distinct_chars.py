'''
You are given a string s and an integer k. Find the length of the longest substring that contains at most k distinct characters.

For example, given s = "eceba" and k = 2, return 3. The longest substring with at most 2 distinct characters is "ece".

This is a sliding window problem. We can use two pointers to maintain a window of characters and a dictionary to count the occurrences 
of each character in the current window. We will expand the window by moving the right pointer and shrink it by moving the left pointer 
when we have more than k distinct characters.
'''
from collections import defaultdict

def longest_substring_containing_at_most_k_distinct_chars(s:str, k:int) -> int:
    counts = defaultdict(int)
    left = ans = 0
    for right in range(len(s)):
        counts[s[right]] += 1
        while len(counts) > k:
            counts[s[left]] -= 1
            if counts[s[left]] == 0:
                del counts[s[left]]
            left += 1
        ans = max(ans, right - left + 1)
    return ans