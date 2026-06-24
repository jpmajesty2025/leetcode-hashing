'''
A pangram is a sentence where every letter of the English alphabet appears at least once.

Given a string sentence containing only lowercase English letters, return true if sentence is a pangram, or false otherwise.
'''
def check_if_pangram(sentence: str) -> bool:
    """Return True if sentence is a pangram, or False otherwise."""
    if len(sentence) < 26:
        return False
    return len(set(sentence)) == 26