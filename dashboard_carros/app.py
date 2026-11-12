import streamlit as st

st.set_page_config(page_title="Concessionária", page_icon="🚗", layout="wide")

from componentes.painel_pagamento import renderizar_pagamento
from componentes.painel_selecao import renderizar_selecao
from componentes.painel_vendas import renderizar_painel_vendas
from servicos.estado import inicializar_estado

inicializar_estado()

st.title("🚗 Dashboard de Vendas - Concessionária")
st.markdown("---")

if st.session_state.mensagem_venda:
    st.success(st.session_state.mensagem_venda)
    st.session_state.mensagem_venda = None

col1, col2 = st.columns([1, 1], gap="large")

with col1:
    renderizar_selecao()

with col2:
    renderizar_pagamento()

st.markdown("---")
renderizar_painel_vendas()
