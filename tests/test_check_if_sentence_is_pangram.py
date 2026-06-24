import string

import pytest
from hypothesis import given, strategies as st

from check_if_sentence_is_pangram import check_if_pangram


@pytest.mark.parametrize(
    "sentence,expected",
    [
        ("thequickbrownfoxjumpsoverthelazydog", True),
        ("leetcode", False),
        ("abcdefghijklmnopqrstuvwxyz", True),
        ("abcdefghijklmnopqrstuvwxy", False),
        ("aaaaaaaaaaaaaaaaaaaaaaaaaa", False),
        ("", False),
    ],
)
def test_check_if_pangram_examples(sentence, expected):
    assert check_if_pangram(sentence) is expected


@given(sentence=st.text(alphabet=string.ascii_lowercase, min_size=0, max_size=200))
def test_check_if_pangram_matches_reference(sentence):
    expected = len(set(sentence)) == 26
    assert check_if_pangram(sentence) is expected


@given(
    letters=st.lists(
        st.sampled_from(list(string.ascii_lowercase)),
        min_size=26,
        max_size=100,
    )
)
def test_check_if_pangram_true_when_all_letters_present(letters):
    sentence = "".join(letters) + string.ascii_lowercase
    assert check_if_pangram(sentence) is True
