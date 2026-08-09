from __future__ import annotations

from pathlib import Path

import pandas as pd

from japan_life.engine import simulate_strategy
from japan_life.storage import load_history, save_history
from japan_life.validation import strategy_results


def test_save_and_load_history(tmp_path: Path) -> None:
    history = simulate_strategy("balanced").history
    output = save_history(history, tmp_path / "history.csv")
    loaded = load_history(output)
    assert len(loaded) == 13
    assert set(["month", "japanese", "adaptation"]).issubset(loaded.columns)


def test_strategy_results_has_three_strategies() -> None:
    frame = strategy_results()
    assert isinstance(frame, pd.DataFrame)
    assert set(frame["strategy"]) == {"study-focused", "work-focused", "balanced"}
    assert frame["adaptation"].between(0, 100).all()
