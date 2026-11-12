# Dashboard de Vendas - Concessionária

Aplicação em Streamlit para registrar vendas de carros, com pagamento à vista ou financiado e painel de resultados.

## Estrutura

```
dashboard_carros/
├── app.py
├── requirements.txt
├── README.md
├── .streamlit/
│   └── config.toml
├── dados/
│   └── catalogo.py
├── servicos/
│   ├── estado.py
│   ├── carrinho.py
│   ├── financiamento.py
│   └── vendas.py
├── utils/
│   └── formatacao.py
└── componentes/
    ├── painel_selecao.py
    ├── painel_pagamento.py
    └── painel_vendas.py
```

## Como executar

```
pip install -r requirements.txt
streamlit run app.py
```

## Pastas

- `dados`: catálogo de veículos e parâmetros (cores, parcelas, juros, entrada mínima).
- `servicos`: regras de negócio e controle do `st.session_state`.
- `utils`: funções auxiliares, como formatação de moeda.
- `componentes`: blocos de interface de cada área da tela.
