import streamlit as st

from dados.catalogo import ENTRADA_MINIMA, JUROS_MENSAL, PARCELAS
from servicos.carrinho import total_carrinho, total_unidades
from servicos.financiamento import calcular_entrada_minima, calcular_parcela
from servicos.vendas import registrar_venda
from utils.formatacao import moeda


def renderizar_pagamento():
    st.subheader("Pagamento e Fechamento")

    total_venda = total_carrinho()
    st.metric(label="TOTAL DA VENDA", value=moeda(total_venda))

    st.markdown("---")

    if total_venda == 0:
        st.warning("Adicione veículos à proposta antes de prosseguir com o pagamento.")
        return

    forma = st.radio("Forma de Pagamento", ["À Vista", "Financiado"], horizontal=True)

    if forma == "À Vista":
        detalhe_pagamento = _pagamento_a_vista(total_venda)
    else:
        detalhe_pagamento = _pagamento_financiado(total_venda)

    if detalhe_pagamento:
        if st.button("Finalizar Venda e Novo Cliente", type="primary", use_container_width=True):
            registrar_venda(detalhe_pagamento)
            st.rerun()


def _pagamento_a_vista(total_venda):
    valor_recebido = st.number_input(
        "Valor Recebido do Cliente (R$)",
        min_value=0.0,
        value=0.0,
        step=1000.0,
        format="%.2f",
    )

    if valor_recebido == 0:
        st.info("Aguardando o recebimento do pagamento...")
        return None

    if valor_recebido < total_venda:
        falta = total_venda - valor_recebido
        st.error(f"**Valor Insuficiente!** Faltam **{moeda(falta)}** para concluir a venda.")
        return None

    troco = valor_recebido - total_venda
    st.success("**Pagamento Concluído!**")
    st.metric(label="TROCO A DEVOLVER", value=moeda(troco))

    with st.expander("Ver Comprovante da Venda"):
        st.write(f"**Veículos:** {total_unidades()}")
        st.write(f"**Total:** {moeda(total_venda)}")
        st.write(f"**Valor Pago:** {moeda(valor_recebido)}")
        st.write(f"**Troco:** {moeda(troco)}")

    return "À Vista"


def _pagamento_financiado(total_venda):
    entrada_minima = calcular_entrada_minima(total_venda)
    entrada = st.number_input(
        f"Entrada (mínimo {moeda(entrada_minima)})",
        min_value=0.0,
        value=0.0,
        step=1000.0,
        format="%.2f",
    )
    n_parcelas = st.selectbox("Número de Parcelas", PARCELAS, index=2)

    if entrada == 0:
        st.info("Aguardando o valor da entrada...")
        return None

    if entrada < entrada_minima:
        falta = entrada_minima - entrada
        percentual = ENTRADA_MINIMA * 100
        st.error(f"**Entrada Insuficiente!** Faltam **{moeda(falta)}** para atingir os {percentual:.0f}% exigidos.")
        return None

    if entrada >= total_venda:
        st.warning("A entrada cobre o valor total. Utilize a opção À Vista.")
        return None

    saldo = total_venda - entrada
    parcela = calcular_parcela(saldo, n_parcelas)
    total_financiado = parcela * n_parcelas

    st.success("**Financiamento Aprovado!**")
    m1, m2 = st.columns(2)
    m1.metric(label="SALDO A FINANCIAR", value=moeda(saldo))
    m2.metric(label=f"PARCELA ({n_parcelas}x)", value=moeda(parcela))

    with st.expander("Ver Comprovante da Venda"):
        st.write(f"**Veículos:** {total_unidades()}")
        st.write(f"**Total:** {moeda(total_venda)}")
        st.write(f"**Entrada:** {moeda(entrada)}")
        st.write(f"**Saldo Financiado:** {moeda(saldo)}")
        st.write(f"**Parcelas:** {n_parcelas}x de {moeda(parcela)}")
        st.write(f"**Taxa:** {JUROS_MENSAL * 100:.2f}% a.m.")
        st.write(f"**Total com Juros:** {moeda(entrada + total_financiado)}")

    return f"Financiado {n_parcelas}x"
