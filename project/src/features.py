import pandas as pd
from datetime import timedelta
import numpy as np

def compute_features(price_history_df, lookback_days=30):
    last_date = price_history_df['timestamp'].max()
    cutoff = last_date - timedelta(days=lookback_days)

    df_recent = price_history_df[price_history_df['timestamp'] >= cutoff].copy()

    features = []

    for coin, g in df_recent.groupby('coin'):
        g = g.sort_values('timestamp')
        g['ret'] = g['price'].pct_change()

        avg_return = g['ret'].mean(skipna=True)
        volatility = g['ret'].std(skipna=True)
        downside_std = g[g['ret'] < 0]['ret'].std(skipna=True)
        avg_volume = g['volume'].mean()
        avg_marketcap = g['market_cap'].mean()

        features.append({
            'coin': coin,
            'avg_return': avg_return,
            'volatility': volatility,
            'downside_std': downside_std,
            'avg_volume': avg_volume,
            'avg_marketcap': avg_marketcap
        })

    df_feat = pd.DataFrame(features).set_index("coin")
    df_feat = df_feat.fillna(0)
    return df_feat