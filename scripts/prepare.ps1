$ErrorActionPreference = "Stop"

Write-Host "[1/6] Refreshing uv.lock..."
if (Test-Path "uv.lock") {
    Remove-Item "uv.lock"
}
uv lock

Write-Host "[2/6] Reproducing environment..."
uv sync

Write-Host "[3/6] Type checking..."
uv run mypy src/

Write-Host "[4/6] Running unit tests and doctest..."
uv run pytest
uv run python -m doctest src/japan_life/utils.py

Write-Host "[5/6] Generating demo output..."
uv run japan-life demo --strategy balanced --history examples/demo_history.csv --plot docs/demo_trajectory.png

Write-Host "[6/6] Generating validation data and vector figure..."
uv run japan-life validate --output docs/strategy_comparison.pdf --csv examples/strategy_results.csv

Write-Host "Done. uv.lock, demo files, tests, and validation outputs are ready."
