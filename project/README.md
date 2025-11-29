# Projeto: Clusterização de Criptomoedas por Perfil de Risco

Este projeto tem como objetivo analisar criptomoedas usando dados reais da API
da CoinGecko e agrupá-las em perfis de risco (baixo, médio e alto) utilizando
técnicas de Machine Learning Não Supervisionado.

A motivação principal é auxiliar investidores a construir portfólios mais
equilibrados, identificando ativos com comportamentos semelhantes em termos de
retorno, volatilidade e outros indicadores de risco.

---

## 📌 Objetivos do Projeto

### 🎯 Objetivo de Negócio
Ajudar investidores a diversificar seus portfólios por meio da identificação de
grupos de criptomoedas com perfis de risco semelhantes.

### 🧠 Objetivo de Ciência de Dados
Desenvolver uma pipeline completa de:
- Coleta de dados reais via API CoinGecko  
- Feature engineering  
- Clusterização (K-Means e PCA)  
- Avaliação dos clusters (silhouette score)  
- Visualização gráfica  

---

## 🚀 Como Executar o Projeto

### 1️⃣ **Instale as dependências**
'''pip install -r requirements.txt'''

### 2️⃣ **Execute o pipeline completo**
'''python main.py'''


Isso irá:
- Baixar dados reais de várias criptomoedas  
- Gerar o dataset de features  
- Aplicar clusterização  
- Exportar o resultado final:  
  `data/outputs/crypto_clusters.csv`

---

## 📊 Métodos Utilizados

### 📈 Feature Engineering
As seguintes métricas são calculadas:
- **avg_return** → retorno médio diário  
- **volatility** → volatilidade dos retornos  
- **downside_std** → risco de quedas  
- **avg_volume** → volume médio negociado  
- **avg_marketcap** → valor de mercado médio  
- **log_mc** e **log_vol** → transformações log  

---

## 🤖 Técnicas de Machine Learning

### 🔹 K-Means (k = 3)
Usado para identificar 3 perfis de risco:
1. **Baixo risco**  
2. **Médio risco**  
3. **Alto risco**

### 🔹 PCA (2 componentes)
Redução de dimensionalidade para visualização dos clusters em 2D.

### 🔹 Silhouette Score
Métrica usada para avaliar a separação entre os clusters.

---

## 📁 Notebooks Incluídos

Cada notebook corresponde a uma etapa do pipeline:

### **01_coleta_dados.ipynb**
Baixa dados reais da API da CoinGecko.

### **02_analise_exploratoria.ipynb**
Gráficos, estatísticas, comportamento dos preços.

### **03_feature_engineering.ipynb**
Cálculo das features de risco.

### **04_modelagem_clusters.ipynb**
Clusterização com K-Means + visualização PCA.

### **05_relatorio_final.ipynb**
Versão formatada para entrega.

---

## 📌 Créditos

- Desenvolvido por: **Felipe Ribeiro**  
- Projeto para a disciplina **C318 - Tópicos Especiais II**


