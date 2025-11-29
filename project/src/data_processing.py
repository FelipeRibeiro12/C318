import pandas as pd
import numpy as np
from sklearn.preprocessing import StandardScaler

def load_features(path="../data/processed/crypto_features.csv"):
    return pd.read_csv(path, index_col="coin")


def apply_feature_weighting(df_features, peso_marketcap=3):
    """
    Aplica transformações + peso maior no market cap.
    Mantém todas as outras métricas equilibradas.
    """
    
    X = df_features[['avg_return','volatility','downside_std','avg_volume','avg_marketcap']].copy()

    # log transforms
    X['log_volume'] = np.log1p(X['avg_volume'])
    X['log_mc'] = np.log1p(X['avg_marketcap'])

    # features selecionadas
    X_model = X[['avg_return','volatility','downside_std','log_volume','log_mc']].copy()

    # ---- PESO NO MARKET CAP ----
    X_model['log_mc'] = X_model['log_mc'] * peso_marketcap
    print(f"[INFO] Peso aplicado ao market cap: {peso_marketcap}")

    # normalização
    scaler = StandardScaler()
    X_scaled = scaler.fit_transform(X_model)

    return X_scaled, X_model