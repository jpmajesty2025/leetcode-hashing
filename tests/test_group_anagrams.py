from collections import Counter

import pytest
from hypothesis import given, strategies as st

from group_anagrams import group_anagrams as group_anagrams_sorted_key
from group_anagrams_ii import group_anagrams as group_anagrams_count_key


def _normalize_groups(groups: list[list[str]]) -> list[tuple[str, ...]]:
    """Return a deterministic, order-insensitive representation of grouped anagrams."""
    return sorted(tuple(sorted(group)) for group in groups)


def _reference_group_anagrams(strs: list[str]) -> list[list[str]]:
    buckets: dict[str, list[str]] = {}
    for s in strs:
        key = "".join(sorted(s))
        buckets.setdefault(key, []).append(s)
    return list(buckets.values())


@pytest.mark.parametrize(
    "strs,expected",
    [
        (["eat", "tea", "tan", "ate", "nat", "bat"], [["eat", "tea", "ate"], ["tan", "nat"], ["bat"]]),
        ([""], [[""]]),
        (["a"], [["a"]]),
        (["ab", "ba", "abc", "cba", "bca"], [["ab", "ba"], ["abc", "cba", "bca"]]),
        (["zzz", "zzz", "zzz"], [["zzz", "zzz", "zzz"]]),
    ],
)
def test_group_anagrams_examples(strs, expected):
    expected_norm = _normalize_groups(expected)

    result_sorted_key = group_anagrams_sorted_key(strs)
    result_count_key = group_anagrams_count_key(strs)

    assert _normalize_groups(result_sorted_key) == expected_norm
    assert _normalize_groups(result_count_key) == expected_norm


@pytest.mark.parametrize("impl", [group_anagrams_sorted_key, group_anagrams_count_key])
def test_group_anagrams_preserves_input_multiset(impl):
    strs = ["eat", "tea", "tan", "ate", "nat", "bat", "eat"]
    result = impl(strs)

    flattened = [s for group in result for s in group]
    assert Counter(flattened) == Counter(strs)


@given(
    strs=st.lists(
        st.text(alphabet=st.characters(min_codepoint=97, max_codepoint=122), min_size=0, max_size=20),
        min_size=1,
        max_size=80,
    )
)
def test_group_anagrams_both_implementations_match_reference(strs):
    expected = _normalize_groups(_reference_group_anagrams(strs))
    result_sorted_key = _normalize_groups(group_anagrams_sorted_key(strs))
    result_count_key = _normalize_groups(group_anagrams_count_key(strs))

    assert result_sorted_key == expected
    assert result_count_key == expected
    assert result_sorted_key == result_count_key


@given(
    strs=st.lists(
        st.text(alphabet=st.characters(min_codepoint=97, max_codepoint=122), min_size=0, max_size=20),
        min_size=1,
        max_size=80,
    )
)
def test_group_anagrams_group_invariants(strs):
    result = group_anagrams_count_key(strs)

    flattened = [s for group in result for s in group]
    assert Counter(flattened) == Counter(strs)

    for group in result:
        if not group:
            continue
        signature = "".join(sorted(group[0]))
        for word in group:
            assert "".join(sorted(word)) == signature
