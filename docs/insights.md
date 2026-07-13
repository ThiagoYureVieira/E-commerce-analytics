# Business Insights - E-commerce Analytics

## Tabela Orders
- PK - order_id
- FK's - customer_id (Faz referência a customer_id da tabela customers)

- A tabela Orders possui algumas colunas de datas com muitos valores nulos, no entanto esses valores fazem sentido no contexto do negócio. De qualquer forma ao fazer a análise final é preciso considerar isso, tendo em vista que provavelmente o valor nulo ou não depende do status do pedido.