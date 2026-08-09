"""History conversion and persistence utilities."""

from __future__ import annotations

from pathlib import Path

import pandas as pd


def history_frame(history: list[dict[str, int]]) -> pd.DataFrame:
    """Convert game history into a tabular DataFrame."""
    return pd.DataFrame(history)


def save_history(history: list[dict[str, int]], path: str | Path) -> Path:
    """Save history to CSV and return the output path."""
    output = Path(path)
    output.parent.mkdir(parents=True, exist_ok=True)
    history_frame(history).to_csv(output, index=False)
    return output


def load_history(path: str | Path) -> pd.DataFrame:
    """Load a saved history CSV."""
    return pd.read_csv(Path(path))
