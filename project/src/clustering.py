import pandas as pd
from sklearn.preprocessing import StandardScaler
from sklearn.cluster import KMeans
from sklearn.decomposition import PCA
from sklearn.metrics import silhouette_score
import numpy as np

def cluster_cryptos(features, k=5, peso_marketcap=5):
    """
    Aplica: 
    - feature weighting no market cap
    - normalização
    - KMeans
    - PCA
    Retorna: df com clusters e silhouette score
    """

    # ================================
    # 1) Preparação das features
    # ================================
    X = features[['avg_return','volatility','downside_std','avg_volume','avg_marketcap']].copy()

    # Melhorias importantes
    X['abs_return'] = np.abs(X['avg_return'])   # nova feature
    X['log_volume'] = np.log1p(X['avg_volume'])
    X['log_volume'] = X['log_volume'] / X['log_volume'].max() # normalização extra
    X['log_mc'] = np.log1p(X['avg_marketcap'])

    X_model = X[['volatility','downside_std','abs_return','log_volume','log_mc']].copy()

    # Peso maior no marketcap
    X_model['log_mc'] = X_model['log_mc'] * peso_marketcap
    print(f"[INFO] Peso aplicado ao market cap: {peso_marketcap}")

    # ================================
    # 2) Normalização
    # ================================
    scaler = StandardScaler()
    X_scaled = scaler.fit_transform(X_model)

    # ================================
    # 3) KMeans
    # ================================
    kmeans = KMeans(n_clusters=k, random_state=42, n_init=10)
    labels = kmeans.fit_predict(X_scaled)

    df_out = features.copy()
    df_out["cluster"] = labels

    # ================================
    # 4) PCA
    # ================================
    pca = PCA(n_components=2)
    coords = pca.fit_transform(X_scaled)
    df_out["pc1"] = coords[:,0]
    df_out["pc2"] = coords[:,1]

    # ================================
    # 5) Silhouette
    # ================================
    score = silhouette_score(X_scaled, labels)
    print(f"[INFO] Silhouette Score: {score}")

    return df_out, score