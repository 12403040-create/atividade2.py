from dados.catalogo import ENTRADA_MINIMA, JUROS_MENSAL


def calcular_parcela(saldo, n_parcelas, taxa=JUROS_MENSAL):
    return saldo * taxa / (1 - (1 + taxa) ** -n_parcelas)


def calcular_entrada_minima(total):
    return total * ENTRADA_MINIMA
