"""Deterministic simulation engine."""

from __future__ import annotations

from collections.abc import Iterable

from .events import EVENTS, get_event
from .models import Choice, GameResult, LifeState


def new_game() -> LifeState:
    """Create the default newly-arrived international student.

    >>> new_game().japanese
    35
    >>> new_game().month
    1
    """
    return LifeState()


def apply_choice(state: LifeState, choice: Choice) -> LifeState:
    """Apply one deterministic choice to a state and return a new state."""
    updated = LifeState(**state.snapshot())
    for attribute, delta in choice.effect.items():
        if not hasattr(updated, attribute):
            raise ValueError(f"unknown state attribute: {attribute}")
        setattr(updated, attribute, getattr(updated, attribute) + delta)
    updated.clamp()
    return updated


def advance_month(state: LifeState) -> LifeState:
    """Advance to the next month without exceeding month 12."""
    updated = LifeState(**state.snapshot())
    updated.month = min(12, state.month + 1)
    return updated


def determine_ending(state: LifeState) -> str:
    """Determine one ending from the final state."""
    if state.stress >= 75 or state.health < 30:
        return "燃え尽き留学生"
    if state.money < 25:
        return "金欠サバイバー"
    if state.adaptation >= 70 and state.japanese >= 65:
        return "日本生活マスター"
    if state.academics >= 80 and state.japanese >= 60:
        return "優等生留学生"
    if state.relationships >= 70 and state.japanese >= 55:
        return "国際交流の達人"
    return "自分のペースを見つけた留学生"


def play_choices(choice_indices: Iterable[int]) -> GameResult:
    """Run a complete deterministic simulation from zero-based choice indices."""
    indices = list(choice_indices)
    if len(indices) != len(EVENTS):
        raise ValueError(f"exactly {len(EVENTS)} choices are required")

    state = new_game()
    history = [state.snapshot()]
    for month, choice_index in enumerate(indices, start=1):
        if choice_index not in (0, 1, 2):
            raise ValueError("choice index must be 0, 1, or 2")
        state.month = month
        event = get_event(month)
        state = apply_choice(state, event.choices[choice_index])
        history.append(state.snapshot())

    return GameResult(state=state, ending=determine_ending(state), history=history)


STRATEGIES: dict[str, tuple[int, ...]] = {
    # More academic/Japanese choices.
    "study-focused": (0, 1, 2, 1, 2, 1, 0, 2, 0, 0, 1, 2),
    # Choices that prioritize income and practical work experience.
    "work-focused": (2, 0, 0, 0, 1, 1, 1, 0, 1, 1, 0, 2),
    # Moderate choices that protect health and relationships while progressing.
    "balanced": (0, 1, 1, 1, 0, 1, 1, 0, 0, 0, 2, 1),
}


def simulate_strategy(name: str) -> GameResult:
    """Simulate one named built-in strategy."""
    try:
        choices = STRATEGIES[name]
    except KeyError as exc:
        raise ValueError(f"unknown strategy: {name}") from exc
    return play_choices(choices)
