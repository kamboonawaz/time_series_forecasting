from __future__ import annotations
import pandas as pd
import numpy as np
from statsmodels.tsa.arima.model import ARIMA

try:
    from prophet import Prophet
except ImportError:  # fail gracefully if prophet not installed
    Prophet = None

class MovingAverageModel:
    def __init__(self, window=3):
        self.window = window
        self.history = []
    def fit(self, y: pd.Series):
        self.history = list(y.values)
        return self
    def predict(self, horizon: int):
        preds = []
        hist = self.history.copy()
        for _ in range(horizon):
            preds.append(np.mean(hist[-self.window:]))
            hist.append(preds[-1])
        return np.array(preds)

class ARIMAModel:
    def __init__(self, order=(1,1,1)):
        self.order = order
        self.model = None
    def fit(self, y: pd.Series):
        self.model = ARIMA(y, order=self.order).fit()
        return self
    def predict(self, horizon: int):
        forecast = self.model.forecast(steps=horizon)
        return forecast.values

class ProphetModel:
    def __init__(self, yearly_seasonality=True, weekly_seasonality=False, daily_seasonality=False):
        self.yearly_seasonality = yearly_seasonality
        self.weekly_seasonality = weekly_seasonality
        self.daily_seasonality = daily_seasonality
        self.model = None
    def fit(self, df: pd.DataFrame):
        if Prophet is None:
            raise RuntimeError('prophet not installed')
        m = Prophet(
            yearly_seasonality=self.yearly_seasonality,
            weekly_seasonality=self.weekly_seasonality,
            daily_seasonality=self.daily_seasonality,
        )
        m.fit(df)
        self.model = m
        return self
    def predict(self, horizon: int):
        future = self.model.make_future_dataframe(periods=horizon, freq='M')
        fcst = self.model.predict(future)
        tail = fcst.tail(horizon)
        return tail['yhat'].values


def make_model(spec: dict):
    name = spec['name']
    if name == 'moving_average':
        return MovingAverageModel(window=spec.get('window', 3))
    if name == 'arima':
        order = tuple(spec.get('order', [1,1,1]))
        return ARIMAModel(order=order)
    if name == 'prophet':
        return ProphetModel(
            yearly_seasonality=spec.get('yearly_seasonality', True),
            weekly_seasonality=spec.get('weekly_seasonality', False),
            daily_seasonality=spec.get('daily_seasonality', False),
        )
    raise ValueError(f'Unknown model name {name}')
