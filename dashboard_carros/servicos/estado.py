import streamlit as st


def inicializar_estado():
    if "carrinho" not in st.session_state:
        st.session_state.carrinho = []
    if "vendas" not in st.session_state:
        st.session_state.vendas = []
    if "mensagem_venda" not in st.session_state:
        st.session_state.mensagem_venda = None
