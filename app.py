import streamlit as st
import pandas as pd

st.set_page_config(page_title="Rota Empreendimentos - INSS", layout="wide")

st.title("🏗️ Sistema de Cálculo INSS de Obra")
st.sidebar.header("Parâmetros da Obra")

# Inputs baseados na sua planilha
area_principal = st.sidebar.number_input("Área Principal (m²)", value=161.12)
vau = st.sidebar.number_input("VAU (R$)", value=2066.94)
fator_ajuste_slider = st.sidebar.slider("Fator de Ajuste (%)", 0, 100, 50) / 100

# Cálculos (Lógica Rota Empreendimentos)
area_equiv = area_principal * 0.89
custo_obra = area_equiv * vau
rmt_total = custo_obra * 0.20 * 0.40
inss_original = rmt_total * 0.368
multa_estimada = inss_original * 2.25

# Com Fator de Ajuste
rmt_ajustada = rmt_total * fator_ajuste_slider
cpp_pagar = rmt_ajustada * 0.20
economia = inss_original - cpp_pagar

# Exibição dos Resultados
c1, c2, c3 = st.columns(3)
c1.metric("INSS Original", f"R$ {inss_original:,.2f}")
c2.metric("INSS c/ Ajuste", f"R$ {cpp_pagar:,.2f}", delta=f"-R$ {economia:,.2f}")
c3.metric("Multa Evitada", f"R$ {multa_estimada:,.2f}")

st.divider()
st.subheader("📊 Comparativo de Custos")
st.bar_chart({"Sem Ajuste": inss_original, "Com Fator de Ajuste": cpp_pagar})

st.success(f"💰 Economia Real Gerada: R$ {economia:,.2f}")
st.info(f"📈 Honorários (30%): R$ {economia * 0.30:,.2f}")
