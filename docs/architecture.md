# Architecture

This project compares lightweight forecasting approaches on a synthetic monthly series.

## Flow
1. `src/data_download.py` generates synthetic seasonal-trend series.
2. `src/run_experiments.py` performs rolling-origin evaluation across model specs defined in `configs/default.yaml`.
3. Metrics (sMAPE, MAE) saved to `reports/metrics.json`.
4. Optional plot created via `src/plot_forecasts.py`.

## Models
- Moving Average: naive smoothing baseline
- ARIMA: classical parametric model
- Prophet: additive model with trend + seasonality (optional)

## Rolling-Origin Evaluation
Advance the origin by one horizon each loop: train on data up to t, forecast next H steps, accumulate errors.

## Extensions
- Add SARIMAX for exogenous features
- Add LightGBM with lag features
- Add backtest visualization overlaying predictions per origin
