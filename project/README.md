**Objetivo de Ciência de Dados:**
Desenvolver uma pipeline completa:

- Coleta de dados reais via API CoinGecko
- Engenharia de features
- Clusterização (K-Means e PCA)
- Avaliação dos clusters (Silhouette Score)
- Visualização gráfica dos resultados
- Geração de relatório final

---

## 🚀 Como Executar o Projeto

1. **Instale as dependências:**

   ```bash
   pip install -r requirements.txt
   ```

2. **Execute o pipeline completo:**

   ```bash
   python main.py
   ```

3. **Visualize os resultados:**
   - Os arquivos gerados estarão em `data/outputs/crypto_clusters.csv` e `data/outputs/crypto_clusters_renomeados.csv`.
   - Para visualizar os clusters em uma interface web, execute:
   ```bash
   streamlit run app/app.py
   ```

---

## 📊 Pipeline e Métodos Utilizados

### 1. Coleta de Dados

- API CoinGecko: preços históricos, volumes, market cap
- Notebook: `01_coleta_dados.ipynb`

### 2. Análise Exploratória (EDA)

- Estatísticas, gráficos, correlações, outliers
- Notebook: `02_analise_exploratoria.ipynb`

### 3. Feature Engineering

- Métricas calculadas: `avg_return`, `volatility`, `downside_std`, `avg_volume`, `avg_marketcap`, `abs_return`, `log_mc`, `log_volume`
- Notebook: `03_feature_engineering.ipynb`

### 4. Modelagem e Clusterização

- Algoritmo: K-Means (k=5)
- Redução de dimensionalidade: PCA (2 componentes)
- Avaliação: Silhouette Score
- Notebook: `04_modelagem_clusters.ipynb`

### 5. Relatório Final

- Visualização dos clusters
- Interpretação dos grupos
- Notebook: `05_relatorio_final.ipynb`

### 6. Dashboard Interativo

- Visualização dos clusters por Streamlit
- Arquivo: `app/app.py`

---

## 📦 Dependências Principais

- pandas
- numpy
- scikit-learn
- matplotlib
- seaborn
- requests
- streamlit

---

- Projeto para a disciplina **C318 - Tópicos Especiais II**
