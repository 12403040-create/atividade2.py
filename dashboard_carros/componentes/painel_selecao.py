import pandas as pd
import streamlit as st

from dados.catalogo import CATALOGO, CORES, DESCONTO_MAXIMO
from servicos.carrinho import adicionar_item, limpar_carrinho
from utils.formatacao import moeda


def renderizar_selecao():
    st.subheader("Seleção de Veículos")

    with st.form("form_veiculo", clear_on_submit=False):
        modelo = st.selectbox("Escolha o Veículo", list(CATALOGO.keys()))
        categoria = CATALOGO[modelo]["categoria"]
        preco_unit = CATALOGO[modelo]["preco"]
        st.caption(f"Categoria: **{categoria}** | Preço de Tabela: **{moeda(preco_unit)}**")

        cor = st.selectbox("Cor", CORES)
        quantidade = st.number_input("Quantidade", min_value=1, value=1, step=1)
        desconto = st.slider("Desconto (%)", min_value=0, max_value=DESCONTO_MAXIMO, value=0)

        btn_adicionar = st.form_submit_button("Adicionar à Proposta", use_container_width=True)

        if btn_adicionar:
            adicionar_item(modelo, categoria, cor, preco_unit, quantidade, desconto)
            st.success(f"**{modelo}** adicionado à proposta!")

    st.subheader("Proposta de Venda")
    if st.session_state.carrinho:
        df_carrinho = pd.DataFrame(st.session_state.carrinho)

        st.dataframe(
            df_carrinho,
            use_container_width=True,
            hide_index=True,
            column_config={
                "Preço Unit. (R$)": st.column_config.NumberColumn("Preço Unit.", format="R$ %.2f"),
                "Desconto (%)": st.column_config.NumberColumn("Desconto", format="%d%%"),
                "Subtotal (R$)": st.column_config.NumberColumn("Subtotal", format="R$ %.2f"),
            },
        )

        if st.button("Limpar Proposta", use_container_width=True):
            limpar_carrinho()
            st.rerun()
    else:
        st.info("A proposta está vazia. Adicione veículos acima.")
