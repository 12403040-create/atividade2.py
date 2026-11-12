import streamlit as st

from servicos.vendas import obter_dataframe_vendas, zerar_vendas
from utils.formatacao import moeda


def renderizar_painel_vendas():
    st.subheader("Painel de Vendas Realizadas")

    if not st.session_state.vendas:
        st.info("Nenhuma venda finalizada ainda. Conclua uma venda para ver o painel.")
        return

    df_vendas = obter_dataframe_vendas()

    faturamento = df_vendas["Valor (R$)"].sum()
    unidades = int(df_vendas["Qtd"].sum())
    ticket_medio = faturamento / unidades

    k1, k2, k3 = st.columns(3)
    k1.metric("Veículos Vendidos", unidades)
    k2.metric("Faturamento", moeda(faturamento))
    k3.metric("Ticket Médio", moeda(ticket_medio))

    g1, g2 = st.columns(2, gap="large")
    with g1:
        st.markdown("**Faturamento por Categoria**")
        st.bar_chart(df_vendas.groupby("Categoria")["Valor (R$)"].sum())
    with g2:
        st.markdown("**Unidades por Modelo**")
        st.bar_chart(df_vendas.groupby("Veículo")["Qtd"].sum())

    with st.expander("Ver Histórico de Vendas"):
        st.dataframe(
            df_vendas,
            use_container_width=True,
            hide_index=True,
            column_config={
                "Valor (R$)": st.column_config.NumberColumn("Valor", format="R$ %.2f"),
            },
        )

    if st.button("Zerar Histórico de Vendas", use_container_width=True):
        zerar_vendas()
        st.rerun()
