import streamlit as st
import pandas as pd

# ---------------------------
# 1. Carregamento do dataset
# ---------------------------
def load_data():
    df = pd.read_csv("data/outputs/crypto_clusters_renomeados.csv", index_col="coin")
    return df

df = load_data()

# ---------------------------
# 2. Configuração da página
# ---------------------------
st.set_page_config(
    page_title="Cluster de Criptomoedas",
    page_icon="💹",
    layout="centered"
)

st.title("💹 Classificação de Criptomoedas por Perfil de Risco")
st.write("""
Insira o nome das criptomoedas que deseja consultar.  
O sistema retornará o **grupo de risco** calculado pelo modelo de clusterização.
""")

st.divider()

# ---------------------------
# 3. Entrada do usuário
# ---------------------------
all_coins = df.index.tolist()

st.subheader("Digite uma ou mais criptomoedas:")

user_input = st.text_input(
    "Exemplo: bitcoin, ethereum, cardano",
    placeholder="Digite aqui..."
)

st.info("Você pode inserir várias moedas separadas por vírgula.")

# ---------------------------
# 4. Processamento
# ---------------------------
def find_clusters(query, df):
    query = [q.strip().lower() for q in query]
    df_index_lower = {c.lower(): c for c in df.index}

    results = []
    not_found = []

    for coin in query:
        if coin in df_index_lower:
            real_name = df_index_lower[coin]
            results.append((real_name, df.loc[real_name, "cluster_label"]))
        else:
            not_found.append(coin)

    return results, not_found

# ---------------------------
# 5. Botão
# ---------------------------
if st.button("Consultar Grupos"):
    if not user_input:
        st.warning("Digite pelo menos uma criptomoeda!")
    else:
        coins = user_input.split(",")

        results, missing = find_clusters(coins, df)

        # Resultados encontrados
        if results:
            st.subheader("📊 Resultados encontrados:")
            for coin, cluster in results:
                st.success(f"**{coin}** → Cluster **{cluster}**")

        # Moedas não encontradas
        if missing:
            st.subheader("⚠️ Não encontradas:")
            for m in missing:
                st.error(f"Moeda '{m}' não está no dataset.")

st.divider()