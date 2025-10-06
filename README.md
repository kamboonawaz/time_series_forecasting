# Time Series Model Comparison

Notebook-only implementation comparing Moving Average, ARIMA, and (optionally) Prophet on a synthetic monthly series dataset.

## Goals
- Unified interface for multiple forecasting models
- Rolling-origin evaluation (walk-forward)
- Metrics: sMAPE, MAE
- Simple plots of forecast vs actual

## Quick Start (Notebook Only)
1. Install dependencies:
```
python -m pip install -r requirements.txt
```
2. Open: `notebooks/project_notebook.ipynb`
3. Run cells in order (they generate data, train models, evaluate, visualize, and optionally retune).

Outputs (plots, metrics DataFrames) are displayed in the notebook; a `reports/` directory may contain generated images if created by plotting cells.

## Folder Structure (Notebook-Only)
```
data/            # raw & processed time series (auto-created by notebook)
notebooks/       # main project notebook(s)
reports/         # optional artifacts (plots)
requirements.txt # pinned dependencies
README.md
```

All former Python scripts have been removed; logic now lives inside the notebook cells.

## Reproducing Without the Notebook
If you later need scripts again, export the notebook:
```
jupyter nbconvert --to script notebooks/project_notebook.ipynb
```
This will produce a `.py` file you can refactor into modules.

## Future Enhancements
- Add interactive widgets (sliders for window size / ARIMA order)
- Add environment freeze cell (pip freeze > requirements.lock)
- Integrate nbclient execution in CI for regression testing

## Notes
Prophet is optional. If unavailable, its results will show NaNs in the results table.
