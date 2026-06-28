import pytest
from hypothesis import given, strategies as st

from find_winners_i import find_winners as find_winners_v1
from find_winners_ii import find_winners as find_winners_v2


IMPLEMENTATIONS = [find_winners_v1, find_winners_v2]


def _reference_find_winners(matches: list[list[int]]) -> list[list[int]]:
    loss_counts: dict[int, int] = {}
    players: set[int] = set()

    for winner, loser in matches:
        players.add(winner)
        players.add(loser)
        loss_counts[loser] = loss_counts.get(loser, 0) + 1

    zero_losses = sorted(player for player in players if loss_counts.get(player, 0) == 0)
    one_loss = sorted(player for player in players if loss_counts.get(player, 0) == 1)
    return [zero_losses, one_loss]


@pytest.mark.parametrize(
    "matches,expected",
    [
        (
            [[1, 3], [2, 3], [3, 6], [5, 6], [5, 7], [4, 5], [4, 8], [4, 9], [10, 4], [10, 9]],
            [[1, 2, 10], [4, 5, 7, 8]],
        ),
        (
            [[2, 3], [1, 3], [5, 4], [6, 4]],
            [[1, 2, 5, 6], []],
        ),
        (
            [[1, 2]],
            [[1], [2]],
        ),
        (
            [[1, 2], [1, 3], [1, 4]],
            [[1], [2, 3, 4]],
        ),
        (
            [[1, 2], [3, 2], [4, 2]],
            [[1, 3, 4], []],
        ),
    ],
)
@pytest.mark.parametrize("implementation", IMPLEMENTATIONS)
def test_find_winners_examples_and_edge_cases(implementation, matches, expected):
    assert implementation(matches) == expected


def _unique_matches_strategy():
    pair = st.tuples(
        st.integers(min_value=1, max_value=200),
        st.integers(min_value=1, max_value=200),
    ).filter(lambda p: p[0] != p[1])

    return st.lists(pair, min_size=1, max_size=120).map(
        lambda pairs: [list(p) for p in sorted(set(pairs))]
    ).filter(lambda matches: len(matches) > 0)


@pytest.mark.parametrize("implementation", IMPLEMENTATIONS)
@given(matches=_unique_matches_strategy())
def test_find_winners_matches_reference(implementation, matches):
    assert implementation(matches) == _reference_find_winners(matches)


@given(matches=_unique_matches_strategy())
def test_versions_i_and_ii_are_equivalent(matches):
    assert find_winners_v1(matches) == find_winners_v2(matches)
