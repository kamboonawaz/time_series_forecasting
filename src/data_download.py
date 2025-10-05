import pandas as pd
from pathlib import Path

RAW = Path('data/raw')
PROCESSED = Path('data/processed')

# We'll synthesize an "airline passengers" style monthly series with trend + seasonality.

def generate_series():
    import numpy as np
    rng = pd.date_range(start='2010-01-01', periods=120, freq='M')
    t = np.arange(len(rng))
    seasonal = 10 + 15 * np.sin(2 * np.pi * t / 12)
    trend = 100 + 2 * t
    noise = np.random.default_rng(42).normal(0, 8, size=len(rng))
    y = trend + seasonal + noise
    return pd.DataFrame({'ds': rng, 'y': y})

def main():
    RAW.mkdir(parents=True, exist_ok=True)
    PROCESSED.mkdir(parents=True, exist_ok=True)
    df = generate_series()
    df.to_csv(RAW / 'synthetic_series.csv', index=False)
    df.to_csv(PROCESSED / 'series.csv', index=False)
    print('Generated synthetic series:', df.shape)

if __name__ == '__main__':
    main()
