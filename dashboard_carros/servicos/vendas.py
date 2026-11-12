import pandas as pd
import streamlit as st

from servicos.carrinho import limpar_carrinho


def registrar_venda(forma_pagamento):
    for item in st.session_state.carrinho:
        st.session_state.vendas.append({
            "Veículo": item["Veículo"],
            "Categoria": item["Categoria"],
            "Cor": item["Cor"],
            "Qtd": item["Qtd"],
            "Pagamento": forma_pagamento,
            "Valor (R$)": item["Subtotal (R$)"],
        })
    st.session_state.mensagem_venda = "Venda finalizada com sucesso!"
    limpar_carrinho()


def zerar_vendas():
    st.session_state.vendas = []


def obter_dataframe_vendas():
    return pd.DataFrame(st.session_state.vendas)
