"""Reproducible validation used to compare three life strategies."""

from __future__ import annotations

from pathlib import Path

import matplotlib.pyplot as plt
import pandas as pd

from .engine import STRATEGIES, simulate_strategy

COMPARE_STATS = ["japanese", "academics", "money", "health", "relationships", "adaptation"]


def strategy_results() -> pd.DataFrame:
    """Return final scores for every built-in strategy."""
    rows: list[dict[str, int | str]] = []
    for name in STRATEGIES:
        result = simulate_strategy(name)
        row: dict[str, int | str] = {"strategy": name}
        row.update({stat: getattr(result.state, stat) for stat in COMPARE_STATS})
        rows.append(row)
    return pd.DataFrame(rows)


def create_validation_figure(output: str | Path) -> Path:
    """Create a grouped bar chart showing that choices create distinct outcomes."""
    frame = strategy_results().set_index("strategy")
    path = Path(output)
    path.parent.mkdir(parents=True, exist_ok=True)

    ax = frame[COMPARE_STATS].T.plot(kind="bar", figsize=(8.4, 4.8))
    ax.set_xlabel("Life dimension")
    ax.set_ylabel("Final score (0-100)")
    ax.set_title("Final outcomes under three decision strategies")
    ax.set_ylim(0, 105)
    ax.tick_params(axis="x", rotation=25)
    ax.legend(title="Strategy", fontsize=8)
    fig = ax.get_figure()
    fig.tight_layout()
    fig.savefig(path)
    plt.close(fig)
    return path
