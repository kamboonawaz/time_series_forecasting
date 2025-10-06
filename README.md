# Time Series Forecasting (Moving Average vs ARIMA)

Lightweight project comparing two simple forecasting approaches (Moving Average and ARIMA) on a synthetic monthly time series with trend + seasonality.

## Goals
- Compare smoothing vs statistical model
- Rolling-origin evaluation (walk-forward)
- Metrics: sMAPE, MAE
- Simple matplotlib visualization

## Quick Start
1. Install dependencies:
```
python -m pip install -r requirements.txt
```
2. Open `notebooks/project_notebook.ipynb` and run cells in order (generate data, train models, evaluate, visualize, retune).

Outputs (plots, metrics DataFrames) are displayed in the notebook; a `reports/` directory may contain generated images if created by plotting cells.

## Sample Output
Example rolling-origin evaluation (values illustrative; yours may vary slightly due to stochastic noise):

| model              | sMAPE | MAE   |
|--------------------|------:|------:|
| MovingAverage(w=3) | 5.13  | 28.12 |
| ARIMA(1,1,1)       | 4.30  | 23.88 |

After simple tuning:

| model                | sMAPE | MAE   |
|----------------------|------:|------:|
| MovingAverage(w=5)   | 4.95  | 26.70 |
| ARIMA(2,1,2)         | 3.90  | 21.55 |

Interpretation: ARIMA captures trend & seasonality better on this synthetic dataset, producing lower symmetric MAPE and MAE.

## Folder Structure
```
data/            # raw & processed time series (auto-created by notebook)
notebooks/       # main project notebook(s)
reports/         # optional artifacts (plots)
requirements.txt # pinned dependencies
README.md
```

Logic is implemented in a single notebook for simplicity.

## Reproducing Without the Notebook
If you need a script version, export the notebook:
```
jupyter nbconvert --to script notebooks/project_notebook.ipynb
```
This will produce a `.py` file you can refactor into modules.

## Future Enhancements
- Interactive widget (slider for window size / ARIMA order)
- Environment freeze cell (`pip freeze > requirements.lock`)
- Residual diagnostics (ACF/PACF) & stationarity test (ADF)
- Lag-feature ML model benchmark (e.g., gradient boosting)
- Automated execution in CI (nbclient)

## Notes
- Synthetic data allows quick, reproducible experimentation.
- Metrics may change slightly run-to-run due to generated noise (seeded to reduce variance).
