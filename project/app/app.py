import streamlit as st
import pandas as pd

# ---------------------------
# 1. Carregamento do dataset
# ---------------------------
def load_data():
    df = pd.read_csv("../data/outputs/crypto_clusters.csv", index_col="coin")
    return df

df = load_data()

# ---------------------------
# 2. Configuração da página
# ---------------------------
st.set_page_config(
    page_title="Clusters de Criptomoedas",
    page_icon="💹",
    layout="wide"
)

st.title("💹 Classificação de Criptomoedas por Perfil de Risco")
st.write("""
Esta tabela mostra todas as criptomoedas do dataset, separadas por **grupo de risco** calculado pelo modelo de clusterização.
""")

st.divider()

# ---------------------------
# 3. Organizando por clusters
# ---------------------------
# Ordenar pelo cluster_label para ficar organizado
df_sorted = df.sort_values(by="cluster")

# Criar uma tabela resumida por cluster
st.subheader("📊 Tabela completa de criptomoedas por grupo")
st.dataframe(df_sorted[["cluster", "avg_return", "volatility", "avg_marketcap"]])

st.subheader("📂 Criptomoedas separadas por clusters")

for cluster_name, group in df_sorted.groupby("cluster"):
    st.markdown(f"### {cluster_name}")
    st.table(group[["cluster", "volatility"]])