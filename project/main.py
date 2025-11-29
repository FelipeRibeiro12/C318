from src.fetch_data import fetch_price_history_coin_gecko
from src.features import compute_features
from src.clustering import cluster_cryptos
import pandas as pd
import time

coin_list = [
    "bitcoin", "ethereum", "solana", "cardano"
]

all_data = []
for coin in coin_list:
    print(f"Baixando {coin}...")
    df = fetch_price_history_coin_gecko(coin, days=120)
    all_data.append(df)
    time.sleep(5)

price_history = pd.concat(all_data, ignore_index=True)
price_history.to_csv("data/raw/prices_raw.csv", index=False)

features = compute_features(price_history, 30)
features.to_csv("data/processed/crypto_features.csv")

n_clusters = 3
if len(features) > n_clusters:
    clusters, score = cluster_cryptos(features, n_clusters)
    clusters.to_csv("data/outputs/crypto_clusters.csv")
    print("Silhouette:", score)
    print("Arquivo final salvo em data/outputs/crypto_clusters.csv")
else:
    print(f"Erro: Número de moedas ({len(features)}) insuficiente para {n_clusters} clusters. Tente novamente após garantir que os dados foram coletados corretamente.")