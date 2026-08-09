from __future__ import annotations

from japan_life.engine import new_game
from japan_life.events import get_event
from japan_life.story import generate_scene


def test_story_works_without_api_key(monkeypatch) -> None:  # type: ignore[no-untyped-def]
    monkeypatch.delenv("OPENAI_API_KEY", raising=False)
    text, used_ai = generate_scene(new_game(), get_event(1), use_ai=True)
    assert text == get_event(1).scene
    assert used_ai is False
