# 📊 Simulador Interativo de P-Hacking e Meta-Distribuição de P-Values  
&gt; *"Não é fraude — é a matemática funcionando contra nossa intuição."*  
&gt; Baseado no artigo de **Nassim Nicholas Taleb**, *“Data Hacking Distribution and Multiple Trials”*

---

## 🔍 O que é este projeto?

Dashboard **open-source** que **simula em tempo real** dois dos principais vícios da ciência moderna:

| Tipo de Hacking | O que acontece na prática | O que o dashboard mostra |
|-----------------|---------------------------|--------------------------|
| **P-Hacking** | Pesquisador testa 20 hipóteses e publica apenas a que deu *p &lt; 0,05* | Distribuição exata do **p-value mínimo** quando você faz *m* testes sob H₀ |
| **Hacking de Regressão** | Pesquisador testa 20 regressões e apresenta a que deu **R² mais alto** | Distribuição do **R² máximo** quando *X* e *Y* são **independentes** |

O objetivo é **tornar palpável** o que Taleb chama de *“pay-off from search”*: mesmo sem fraudar dados, a mera **repetição de testes** gera **falsas descobertas** com probabilidade previsível — e muito alta.

---

## 🚀 Link rápido

| Ambiente | URL |
|----------|-----|
| **Oficial (Streamlit Cloud)** | [`https://taleb-p-hacking-analysis-dashboard.streamlit.app/`](https://taleb-p-hacking-analysis-dashboard.streamlit.app/) |
| **Execução local** | `streamlit run app.py` |

---

## 📦 Instalação local (opcional)

```bash
git clone taleb-p-hacking-analysis-dashboard.git
cd p-hacking-simulador
python -m venv venv
source venv/bin/activate  # Windows: venv\Scripts\activate
pip install -r requirements.txt
streamlit run app.py
