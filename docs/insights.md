# Business Insights - E-commerce Analytics

## Tabela Orders
- PK - order_id
- FK's - customer_id (Faz referência a customer_id da tabela customers)

- A tabela Orders possui algumas colunas de datas com muitos valores nulos, no entanto esses valores fazem sentido no contexto do negócio. De qualquer forma ao fazer a análise final é preciso considerar isso, tendo em vista que provavelmente o valor nulo ou não depende do status do pedido.

## Tabela Products
- PK - product_id

- A tabelas Products possuia valores NAN em algumas colunas como product_description_lenght e product_name_lenght. Decidi retirá-las da tabela pois isso não é uma informação relevante para minha análise. Já a coluna product_category_name também possuía valores NAN, mas nesse caso substitui eles por "Outra" já que vou precisar dessa informação e provavelmente os produtos com essa coluna nula devem significar que eles não tem categoria definida. Também decidi manter os valores NAN nas colunas numéricas já que pretendo verificar se existe relação entre atraso de entrega e peso ou tamanho da mercadoria. Não quis preenchê-los com a média pq provavelmente teria valores falsos que poluiriam a análise.