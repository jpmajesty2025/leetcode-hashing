'''
Given a string text, you want to use the characters of text to form as many instances of the word "balloon" as possible.

You can use each character in text at most once. Return the maximum number of instances that can be formed.
'''
from collections import Counter


def max_number_of_balloons(text: str, target: str = "balloon") -> int:
    if not target:
        raise ValueError("target must be non-empty")

    text_counts = Counter(text)
    target_counts = Counter(target)
    return min((text_counts[ch] // target_counts[ch] for ch in target_counts))