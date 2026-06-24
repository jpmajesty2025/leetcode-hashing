import string

import pytest
from hypothesis import given, strategies as st

from first_letter_to_appear_twice import repeated_character


def _reference_first_repeated_character(s: str) -> str:
    seen_chars = set()
    for ch in s:
        if ch in seen_chars:
            return ch
        seen_chars.add(ch)
    raise ValueError("Input string must contain at least one repeated character.")


@st.composite
def strings_with_a_repeat(draw) -> str:
    chars = draw(
        st.lists(
            st.sampled_from(list(string.ascii_lowercase)),
            min_size=2,
            max_size=100,
        )
    )
    i = draw(st.integers(min_value=0, max_value=len(chars) - 2))
    j = draw(st.integers(min_value=i + 1, max_value=len(chars) - 1))
    chars[j] = chars[i]
    return "".join(chars)


@pytest.mark.parametrize(
    "s,expected",
    [
        ("abccbaacz", "c"),
        ("abcdd", "d"),
        ("aa", "a"),
        ("aba", "a"),
        ("abca", "a"),
    ],
)
def test_repeated_character_examples(s, expected):
    assert repeated_character(s) == expected


@given(s=strings_with_a_repeat())
def test_repeated_character_matches_reference_implementation(s):
    result = repeated_character(s)

    assert result == _reference_first_repeated_character(s)
    assert result in string.ascii_lowercase
    assert s.count(result) >= 2
