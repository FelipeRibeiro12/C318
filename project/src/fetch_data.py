import requests
import pandas as pd

def fetch_price_history_coin_gecko(coin_id, days=120):
    url = f'https://api.coingecko.com/api/v3/coins/{coin_id}/market_chart'
    params = {'vs_currency':'usd','days': days}

    r = requests.get(url, params=params)
    if r.status_code != 200:
        raise Exception(f"Erro ao buscar {coin_id}: {r.text}")

    data = r.json()

    df = pd.DataFrame({
        'timestamp': [p[0] for p in data['prices']],
        'price': [p[1] for p in data['prices']],
        'volume': [v[1] for v in data['total_volumes']],
        'market_cap': [m[1] for m in data['market_caps']]
    })

    df['timestamp'] = pd.to_datetime(df['timestamp'], unit='ms')
    df['coin'] = coin_id

    return df