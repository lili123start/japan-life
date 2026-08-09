"""Narration layer with an optional OpenAI API enhancement."""

from __future__ import annotations

import os

from .models import Event, LifeState


def built_in_scene(event: Event) -> str:
    """Return the built-in Japanese scene so the game always works offline."""
    return event.scene


def generate_scene(
    state: LifeState,
    event: Event,
    *,
    use_ai: bool = False,
    level: str = "N3",
    model: str | None = None,
) -> tuple[str, bool]:
    """Generate a short Japanese scene; fall back safely if AI is unavailable.

    Returns ``(text, used_ai)``. The AI never changes numeric game rules.
    """
    if not use_ai or not os.getenv("OPENAI_API_KEY"):
        return built_in_scene(event), False

    try:
        from openai import OpenAI

        client = OpenAI()
        selected_model = model or os.getenv("OPENAI_MODEL") or "gpt-5-mini"
        status = (
            f"日本語={state.japanese}, 学業={state.academics}, お金={state.money}, "
            f"健康={state.health}, 人間関係={state.relationships}, "
            f"適応={state.adaptation}, ストレス={state.stress}"
        )
        choices = " / ".join(choice.label for choice in event.choices)
        instructions = (
            "あなたは日本語学習者向けのインタラクティブ物語作家です。"
            "留学生の現実的な日本生活を、自然で簡潔な日本語で描写してください。"
            "数値ルールや選択肢の意味は変更しないでください。"
            "出力は物語本文だけにし、100〜180字程度にしてください。"
        )
        prompt = (
            f"学習者レベル: JLPT {level}\n"
            f"時期: 来日{event.month}か月目\n"
            f"場所: {event.location}\n"
            f"イベント: {event.title}\n"
            f"元の場面: {event.scene}\n"
            f"現在の状態: {status}\n"
            f"この後の固定選択肢: {choices}\n"
            "上の情報に合う臨場感のある短い場面を作ってください。"
        )
        response = client.responses.create(
            model=selected_model,
            instructions=instructions,
            input=prompt,
        )
        text = response.output_text.strip()
        if text:
            return text, True
    except Exception:
        # The simulation must remain usable without network access or an API key.
        pass

    return built_in_scene(event), False
