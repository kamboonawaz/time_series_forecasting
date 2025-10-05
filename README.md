# Time Series Model Comparison

Compare Moving Average, ARIMA, and (optionally) Prophet on a synthetic monthly series dataset.

## Goals
- Unified interface for multiple forecasting models
- Rolling-origin evaluation (walk-forward)
- Metrics: sMAPE, MAE
- Simple plots of forecast vs actual

## Quick Start (once code added)
```
python -m pip install -r requirements.txt
python src/data_download.py
python src/run_experiments.py --config configs/default.yaml
```

Outputs (metrics JSON + plot) are produced inline (future: add a reports/ folder if needed).

## Folder Structure (Simplified)
```
configs/        # experiment configuration
data/           # raw & processed time series
src/            # code (data download, models, run_experiments, metrics, plotting)
run_all.py      # convenience end-to-end runner
requirements.txt
README.md
```

If you later want plots or metrics persisted, recreate a `reports/` folder.
