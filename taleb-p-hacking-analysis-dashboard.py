import streamlit as st
import numpy as np
import plotly.graph_objects as go
from sklearn.linear_model import LinearRegression

# Configuração da página
st.set_page_config(page_title="Simulador de P-Hacking", layout="wide")

st.title("📊 Simulador Interativo de P-Hacking e Meta-Distribuição de P-Values")
st.markdown("> Baseado no artigo de **Nassim Nicholas Taleb** sobre os efeitos da repetição de testes estatísticos.")

# ==========================
# Seção 1: P-Hacking
# ==========================
st.header("🔍 Seção 1: Simulação de P-Hacking (P-Value Mínimo)")

with st.sidebar:
    st.subheader("Controles de Simulação")
    m = st.slider("Número de Tentativas (m)", min_value=1, max_value=50, value=10)
    N = st.number_input("Número de Simulações (N)", min_value=100, max_value=50000, value=10000, step=1000)
    alpha = st.select_slider("Nível de Significância (α)", options=[0.01, 0.05, 0.10], value=0.05)

if st.button("Rodar Simulação de P-Hacking"):
    p_min_list = []
    for _ in range(N):
        p_values = np.random.uniform(0, 1, m)
        p_min = np.min(p_values)
        p_min_list.append(p_min)

    p_min_array = np.array(p_min_list)
    false_positives = np.sum(p_min_array < alpha)
    fpr = false_positives / N
    expected_p_min = np.mean(p_min_array)

    # Gráfico
    fig1 = go.Figure()
    fig1.add_trace(go.Histogram(x=p_min_array, nbinsx=50, name='P-min'))
    fig1.add_vline(x=alpha, line=dict(color='red', dash='dash'), name=f'α = {alpha}')
    fig1.update_layout(title="Distribuição do P-Value Mínimo",
                       xaxis_title="P-min", yaxis_title="Frequência")
    st.plotly_chart(fig1, use_container_width=True)

    # Métricas
    col1, col2 = st.columns(2)
    col1.metric("Taxa de Falsos Positivos (FPR)", f"{fpr:.2%}")
    col2.metric("P-value Mínimo Esperado", f"{expected_p_min:.4f}")

# ==========================
# Seção 2: Hacking de Regressão
# ==========================
st.header("📈 Seção 2: Simulação de Hacking de Regressão (R² Máximo)")

with st.sidebar:
    n = st.slider("Tamanho da Amostra (n)", min_value=10, max_value=100, value=30)
    m_reg = st.slider("Número de Regressões (m)", min_value=1, max_value=20, value=10)
    N_reg = st.number_input("Número de Simulações (N)", min_value=100, max_value=20000, value=5000, step=1000, key='reg')

if st.button("Rodar Simulação de Regressão"):
    r2_max_list = []
    for _ in range(N_reg):
        r2_list = []
        for __ in range(m_reg):
            X = np.random.randn(n, 1)
            y = np.random.randn(n)
            model = LinearRegression().fit(X, y)
            r2 = model.score(X, y)
            r2_list.append(r2)
        r2_max = max(r2_list)
        r2_max_list.append(r2_max)

    r2_max_array = np.array(r2_max_list)
    expected_r2_max = np.mean(r2_max_array)

    # Gráfico
    fig2 = go.Figure()
    fig2.add_trace(go.Histogram(x=r2_max_array, nbinsx=50, name='R²_max'))
    fig2.update_layout(title="Distribuição do R² Máximo",
                       xaxis_title="R²_max", yaxis_title="Frequência")
    st.plotly_chart(fig2, use_container_width=True)

    # Métricas
    col1, col2 = st.columns(2)
    col1.metric("R² Máximo Esperado", f"{expected_r2_max:.4f}")
    col2.metric("R² Esperado (1 tentativa)", "~0.00")

# ==========================
# Texto Explicativo
# ==========================
with st.expander("📘 Leia mais sobre os conceitos"):
    st.markdown("""
    ### O que é P-Hacking?
    P-hacking é a prática de realizar múltiplos testes estatísticos e selecionar apenas os resultados significativos, distorcendo a validade científica.

    ### Meta-Distribuição
    A meta-distribuição mostra como os p-values (ou R²) se comportam **sob múltiplas tentativas**, mesmo quando não há efeito real.

    ### Implicações
    Mesmo sem fraude, a simples repetição de testes pode levar a **falsas descobertas**, como demonstrado por Taleb.

    ### Referência
    Taleb, N. N. (2025). *Data Hacking Distribution and Multiple Trials*. American University in Beirut & Universa Investments.
    """)