import pytest
from hypothesis import given, strategies as st

from rearrange_chars_to_make_target_string import max_number_of_balloons


def _reference_max_number_of_balloons(text: str, target: str) -> int:
    if not target:
        raise ValueError("target must be non-empty")

    text_counts: dict[str, int] = {}
    for ch in text:
        text_counts[ch] = text_counts.get(ch, 0) + 1

    target_counts: dict[str, int] = {}
    for ch in target:
        target_counts[ch] = target_counts.get(ch, 0) + 1

    return min((text_counts.get(ch, 0) // count for ch, count in target_counts.items()))


@pytest.mark.parametrize(
    "text,target,expected",
    [
        ("nlaebolko", "balloon", 1),
        ("loonbalxballpoon", "balloon", 2),
        ("leetcode", "balloon", 0),
        ("balon", "balloon", 0),
        ("balloonballoon", "balloon", 2),
        ("ilovecodingonleetcode", "code", 2),
        ("abcabc", "abc", 2),
        ("aaaa", "aa", 2),
        ("abc", "d", 0),
    ],
)
def test_max_number_of_balloons_examples(text, target, expected):
    assert max_number_of_balloons(text, target) == expected


@given(
    text=st.text(alphabet=st.characters(min_codepoint=97, max_codepoint=122), min_size=0, max_size=120),
    target=st.text(alphabet=st.characters(min_codepoint=97, max_codepoint=122), min_size=1, max_size=12),
)
def test_max_number_of_balloons_matches_reference(text, target):
    assert max_number_of_balloons(text, target) == _reference_max_number_of_balloons(text, target)


@given(
    text=st.text(alphabet=st.characters(min_codepoint=97, max_codepoint=122), min_size=0, max_size=120),
    target=st.text(alphabet=st.characters(min_codepoint=97, max_codepoint=122), min_size=1, max_size=12),
    extra=st.text(alphabet=st.characters(min_codepoint=97, max_codepoint=122), min_size=0, max_size=120),
)
def test_max_number_of_balloons_is_monotonic_with_extra_text(text, target, extra):
    base = max_number_of_balloons(text, target)
    extended = max_number_of_balloons(text + extra, target)
    assert extended >= base


def test_max_number_of_balloons_raises_on_empty_target():
    with pytest.raises(ValueError, match="target must be non-empty"):
        max_number_of_balloons("balloon", "")