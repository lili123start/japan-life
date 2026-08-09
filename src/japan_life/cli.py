"""Command-line interface for Japan Life."""

from __future__ import annotations

import argparse
from pathlib import Path

from .engine import STRATEGIES, apply_choice, determine_ending, new_game, simulate_strategy
from .events import get_event
from .models import LifeState
from .plotting import plot_history
from .storage import save_history
from .story import generate_scene
from .validation import create_validation_figure, strategy_results


def _state_line(state: LifeState) -> str:
    """Format the seven tracked life dimensions for terminal output."""
    return (
        f"日本語 {state.japanese:>3} | 学業 {state.academics:>3} | "
        f"お金 {state.money:>3} | 健康 {state.health:>3} | "
        f"人間関係 {state.relationships:>3} | 適応 {state.adaptation:>3} | "
        f"ストレス {state.stress:>3}"
    )


def play(*, use_ai: bool, level: str, history_path: Path, plot_path: Path) -> int:
    """Run the interactive 12-month story."""
    state = new_game()
    history = [state.snapshot()]
    print("\n=== JAPAN LIFE ===")
    print("あなたは、今日から日本で生活を始める留学生です。\n")

    for month in range(1, 13):
        state.month = month
        event = get_event(month)
        scene, ai_used = generate_scene(state, event, use_ai=use_ai, level=level)
        print(f"\n--- Month {month}: {event.title} ---")
        print(f"場所: {event.location}")
        print(scene)
        if use_ai and not ai_used:
            print("[AI narration unavailable - built-in story is being used.]")
        print("\n" + _state_line(state))
        for number, choice in enumerate(event.choices, start=1):
            print(f"  {number}. {choice.label}")

        while True:
            answer = input("選択 [1-3]: ").strip()
            if answer in {"1", "2", "3"}:
                choice_index = int(answer) - 1
                break
            print("1, 2, 3 のどれかを入力してください。")

        choice = event.choices[choice_index]
        state = apply_choice(state, choice)
        print(f"\n{choice.explanation}")
        print(_state_line(state))
        history.append(state.snapshot())

    ending = determine_ending(state)
    save_history(history, history_path)
    plot_history(history, plot_path)
    print("\n=== ONE YEAR IN JAPAN ===")
    print(_state_line(state))
    print(f"Ending: {ending}")
    print(f"History: {history_path}")
    print(f"Trajectory: {plot_path}")
    return 0


def demo(strategy: str, history_path: Path, plot_path: Path) -> int:
    """Run a non-interactive demo, useful for checking installation."""
    result = simulate_strategy(strategy)
    save_history(result.history, history_path)
    plot_history(result.history, plot_path)
    print(f"Strategy: {strategy}")
    print(f"Ending: {result.ending}")
    print(_state_line(result.state))
    print(f"History: {history_path}")
    print(f"Trajectory: {plot_path}")
    return 0


def validate(output: Path, csv_output: Path) -> int:
    """Create the reproducible strategy comparison used for validation."""
    frame = strategy_results()
    csv_output.parent.mkdir(parents=True, exist_ok=True)
    frame.to_csv(csv_output, index=False)
    create_validation_figure(output)
    print(frame.to_string(index=False))
    print(f"Validation figure: {output}")
    print(f"Validation data: {csv_output}")
    return 0


def build_parser() -> argparse.ArgumentParser:
    """Build the command-line parser."""
    parser = argparse.ArgumentParser(
        prog="japan-life",
        description="Interactive first-year-in-Japan simulator for international students.",
    )
    sub = parser.add_subparsers(dest="command")

    play_parser = sub.add_parser("play", help="play the 12-month interactive story")
    play_parser.add_argument("--ai", action="store_true", help="use OpenAI narration when OPENAI_API_KEY is set")
    play_parser.add_argument("--level", default="N3", choices=["N4", "N3", "N2", "N1"], help="Japanese narration level")
    play_parser.add_argument("--history", type=Path, default=Path("life_history.csv"))
    play_parser.add_argument("--plot", type=Path, default=Path("life_trajectory.pdf"))

    demo_parser = sub.add_parser("demo", help="run a reproducible non-interactive example")
    demo_parser.add_argument("--strategy", choices=list(STRATEGIES), default="balanced")
    demo_parser.add_argument("--history", type=Path, default=Path("examples/demo_history.csv"))
    demo_parser.add_argument("--plot", type=Path, default=Path("docs/demo_trajectory.png"))

    validation_parser = sub.add_parser("validate", help="compare three built-in decision strategies")
    validation_parser.add_argument("--output", type=Path, default=Path("docs/strategy_comparison.pdf"))
    validation_parser.add_argument("--csv", type=Path, default=Path("examples/strategy_results.csv"))
    return parser


def main() -> int:
    """Console entry point."""
    parser = build_parser()
    args = parser.parse_args()
    if args.command == "play":
        return play(use_ai=args.ai, level=args.level, history_path=args.history, plot_path=args.plot)
    if args.command == "demo":
        return demo(args.strategy, args.history, args.plot)
    if args.command == "validate":
        return validate(args.output, args.csv)
    parser.print_help()
    return 0
