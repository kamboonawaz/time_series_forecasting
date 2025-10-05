# Time Series Model Comparison

Compare Moving Average, ARIMA, and Prophet (optional fallback to statsmodels SARIMAX) on a classic airline passengers style dataset.

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

Outputs in `reports/`.
