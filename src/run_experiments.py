import argparse
import json
from pathlib import Path
import yaml
import pandas as pd
from metrics import smape, mae
from models import make_model, ProphetModel


def rolling_origin_eval(df: pd.DataFrame, horizon: int, initial_train: int, model_specs):
    results = []
    y = df['y'].reset_index(drop=True)
    ds = df['ds']
    for spec in model_specs:
        model_name = spec['name']
        preds_all = []
        trues_all = []
        # Rolling window increments one horizon at a time
        for start in range(initial_train, len(y) - horizon + 1, horizon):
            train_y = y[:start]
            future_true = y[start:start + horizon]
            if model_name == 'prophet':
                # Prophet expects DataFrame with ds,y
                model = make_model(spec).fit(df.iloc[:start][['ds','y']])
            else:
                model = make_model(spec).fit(train_y)
            preds = model.predict(horizon)
            preds_all.extend(list(preds))
            trues_all.extend(list(future_true.values))
        s = smape(trues_all, preds_all)
        m = mae(trues_all, preds_all)
        results.append({
            'model': model_name,
            'smape': s,
            'mae': m
        })
    return results


def main(config_path: str):
    with open(config_path, 'r') as f:
        cfg = yaml.safe_load(f)
    horizon = cfg['horizon']
    initial_train = cfg['initial_train_periods']
    model_specs = cfg['models']
    df = pd.read_csv('data/processed/series.csv')
    df['ds'] = pd.to_datetime(df['ds'])

    results = rolling_origin_eval(df, horizon, initial_train, model_specs)

    reports = Path('reports')
    reports.mkdir(exist_ok=True)
    out_file = reports / 'metrics.json'
    out_file.write_text(json.dumps(results, indent=2))
    print('Results:')
    for r in results:
        print(r)

if __name__ == '__main__':
    ap = argparse.ArgumentParser()
    ap.add_argument('--config', required=True)
    args = ap.parse_args()
    main(args.config)
