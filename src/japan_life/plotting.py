"""Matplotlib visualizations."""

from __future__ import annotations

from pathlib import Path

import matplotlib.pyplot as plt
import pandas as pd

PLOT_STATS = ["japanese", "academics", "money", "health", "relationships", "adaptation"]


def plot_history(history: list[dict[str, int]], output: str | Path) -> Path:
    """Plot the player's first-year trajectory to PNG or vector PDF."""
    frame = pd.DataFrame(history)
    path = Path(output)
    path.parent.mkdir(parents=True, exist_ok=True)

    fig, ax = plt.subplots(figsize=(8.4, 4.8))
    for column in PLOT_STATS:
        ax.plot(frame["month"], frame[column], marker="o", linewidth=1.5, label=column.capitalize())
    ax.set_xlabel("Month")
    ax.set_ylabel("Score (0-100)")
    ax.set_title("First Year in Japan - Life Trajectory")
    ax.set_ylim(0, 105)
    ax.grid(alpha=0.25)
    ax.legend(ncol=3, fontsize=8)
    fig.tight_layout()
    fig.savefig(path)
    plt.close(fig)
    return path
