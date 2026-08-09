"""Core data models for Japan Life."""

from __future__ import annotations

from dataclasses import dataclass, field
from typing import Mapping

from .utils import clamp_score

STAT_NAMES = (
    "japanese",
    "academics",
    "money",
    "health",
    "relationships",
    "adaptation",
    "stress",
)


@dataclass(slots=True)
class LifeState:
    """Player state. Every numeric attribute is kept between 0 and 100."""

    month: int = 1
    japanese: int = 35
    academics: int = 50
    money: int = 60
    health: int = 75
    relationships: int = 15
    adaptation: int = 10
    stress: int = 35

    def clamp(self) -> None:
        """Clamp all numeric life attributes to the inclusive range 0..100."""
        for name in STAT_NAMES:
            value = getattr(self, name)
            setattr(self, name, clamp_score(value))

    def snapshot(self) -> dict[str, int]:
        """Return a serializable snapshot used for history and plots."""
        return {"month": self.month, **{name: getattr(self, name) for name in STAT_NAMES}}


@dataclass(frozen=True, slots=True)
class Choice:
    """A selectable action and its deterministic effect on the player."""

    label: str
    effect: Mapping[str, int]
    explanation: str


@dataclass(frozen=True, slots=True)
class Event:
    """One monthly study-abroad event."""

    month: int
    title: str
    location: str
    scene: str
    choices: tuple[Choice, Choice, Choice]


@dataclass(slots=True)
class GameResult:
    """Completed simulation result."""

    state: LifeState
    ending: str
    history: list[dict[str, int]] = field(default_factory=list)
