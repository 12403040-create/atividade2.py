import streamlit as st


def adicionar_item(modelo, categoria, cor, preco_unit, quantidade, desconto):
    subtotal = preco_unit * quantidade * (1 - desconto / 100)
    st.session_state.carrinho.append({
        "Veículo": modelo,
        "Categoria": categoria,
        "Cor": cor,
        "Preço Unit. (R$)": preco_unit,
        "Qtd": quantidade,
        "Desconto (%)": desconto,
        "Subtotal (R$)": subtotal,
    })


def limpar_carrinho():
    st.session_state.carrinho = []


def total_carrinho():
    return sum(item["Subtotal (R$)"] for item in st.session_state.carrinho)


def total_unidades():
    return sum(item["Qtd"] for item in st.session_state.carrinho)
