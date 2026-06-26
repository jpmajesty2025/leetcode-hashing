'''
Given a string s, determine if all characters have the same frequency.

For example, given s = "abacbc", return true, because all characters appear twice. Given s = "aaabb", 
return false. "a" appears 3 times, "b" appears 2 times. 3 != 2.
'''
from collections import Counter


def are_occurrences_equal(s: str) -> bool:
    if not s:
        return True

    counts = Counter(s)
    return len(set(counts.values())) == 1