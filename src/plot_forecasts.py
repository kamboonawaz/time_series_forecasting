import argparse
from pathlib import Path
import pandas as pd
import json
import matplotlib.pyplot as plt


def main():
    df = pd.read_csv('data/processed/series.csv')
    df['ds'] = pd.to_datetime(df['ds'])
    metrics_path = Path('reports/metrics.json')
    if not metrics_path.exists():
        print('No metrics.json found; run experiments first.')
        return
    metrics = json.loads(metrics_path.read_text())
    # For quick visualization we just plot the raw series; could extend to show last window forecast.
    plt.figure(figsize=(10,4))
    plt.plot(df['ds'], df['y'], label='Actual')
    plt.title('Synthetic Series')
    plt.xlabel('Date')
    plt.ylabel('Value')
    plt.grid(True, alpha=0.3)
    plt.tight_layout()
    out = Path('reports/series.png')
    plt.savefig(out)
    print('Saved plot to', out)

if __name__ == '__main__':
    parser = argparse.ArgumentParser()
    main()
