from __future__ import annotations

import pytest

from japan_life.engine import apply_choice, determine_ending, new_game, play_choices, simulate_strategy
from japan_life.events import get_event
from japan_life.models import Choice, LifeState


def test_new_game_defaults() -> None:
    state = new_game()
    assert state.month == 1
    assert state.japanese == 35
    assert state.health == 75


def test_apply_choice_updates_multiple_stats_without_mutating_original() -> None:
    state = new_game()
    choice = Choice("test", {"japanese": 5, "stress": -3}, "")
    updated = apply_choice(state, choice)
    assert updated.japanese == 40
    assert updated.stress == 32
    assert state.japanese == 35


@pytest.mark.parametrize(
    ("start", "delta", "expected"),
    [
        (98, 10, 100),
        (2, -10, 0),
        (50, 5, 55),
    ],
)
def test_apply_choice_clamps_scores(start: int, delta: int, expected: int) -> None:
    state = LifeState(japanese=start)
    updated = apply_choice(state, Choice("test", {"japanese": delta}, ""))
    assert updated.japanese == expected


def test_unknown_attribute_is_rejected() -> None:
    with pytest.raises(ValueError, match="unknown state attribute"):
        apply_choice(new_game(), Choice("bad", {"luck": 3}, ""))


@pytest.mark.parametrize("month", [1, 6, 12])
def test_get_event_matches_month(month: int) -> None:
    assert get_event(month).month == month


@pytest.mark.parametrize("month", [0, 13])
def test_get_event_rejects_invalid_month(month: int) -> None:
    with pytest.raises(ValueError):
        get_event(month)


def test_play_choices_requires_twelve_choices() -> None:
    with pytest.raises(ValueError, match="exactly 12"):
        play_choices([0, 1])


def test_play_choices_rejects_invalid_choice_index() -> None:
    with pytest.raises(ValueError, match="0, 1, or 2"):
        play_choices([0] * 11 + [3])


def test_balanced_strategy_produces_complete_history() -> None:
    result = simulate_strategy("balanced")
    assert len(result.history) == 13
    assert 0 <= result.state.adaptation <= 100
    assert result.ending


def test_unknown_strategy_is_rejected() -> None:
    with pytest.raises(ValueError, match="unknown strategy"):
        simulate_strategy("impossible")


@pytest.mark.parametrize(
    ("state", "ending"),
    [
        (LifeState(stress=80), "燃え尽き留学生"),
        (LifeState(money=20), "金欠サバイバー"),
        (LifeState(japanese=70, adaptation=80), "日本生活マスター"),
        (LifeState(japanese=65, academics=85), "優等生留学生"),
        (LifeState(japanese=60, relationships=75), "国際交流の達人"),
    ],
)
def test_ending_rules(state: LifeState, ending: str) -> None:
    assert determine_ending(state) == ending
