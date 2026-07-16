# Business Insights - E-commerce Analytics

## Tabela Orders
- PK - order_id
- FK's - customer_id (Faz referência a customer_id da tabela customers)

- A tabela Orders possui algumas colunas de datas com muitos valores nulos, no entanto esses valores fazem sentido no contexto do negócio. De qualquer forma ao fazer a análise final é preciso considerar isso, tendo em vista que provavelmente o valor nulo ou não depende do status do pedido.

## Tabela Products
- PK - product_id

- A tabela Products possuia valores NAN em algumas colunas como product_description_lenght e product_name_lenght. Decidi retirá-las da tabela pois isso não é uma informação relevante para minha análise. Já a coluna product_category_name também possuía valores NAN, mas nesse caso substitui eles por "Outra" já que vou precisar dessa informação e provavelmente os produtos com essa coluna nula devem significar que eles não tem categoria definida. Também decidi manter os valores NAN nas colunas numéricas já que pretendo verificar se existe relação entre atraso de entrega e peso ou tamanho da mercadoria. Não quis preenchê-los com a média pq provavelmente teria valores falsos que poluiriam a análise.

## Tabela Reviews
- PK - review_id e order_id

- A tabela Reviews tem alguns valores duplicados na coluna review_id, no entanto esses valores não refletem necessariamente em um problema, pois a duplicação só se configura nesse contexto se a review_id e a order_id forem duplicadas simultaneamente. Sobre os valores nulos, é algo da regra de negócio já que o usuário pode criar reviews sem título e sem corpo, apenas nota.

## Tabela Customers
- PK - customer_id

- A tabela Customers não apresentou nenhum peculiaridade relevante de ser descrita.

## Tabela Sellers
- PK - seller_id

- A tabela Sellers não apresentou nenhum peculiaridade relevante de ser descrita.

## Tabela Payments
- PK - order_id e payment_sequential
- FK's - order_id (Faz referência a order_id da tabela orders)

- A tabela Payments não apresentou nenhum peculiaridade relevante de ser descrita.

## Tabela Order_Items
- PK - order_id e order_item_id
- FK's 
    - order_id (Faz referência a order_id da tabela orders)
    - product_id (Faz referência a product_id da tabela products)
    - seller_id (Faz referência a seller_id da tabela sellers)

- A tabela Order_Items não apresentou nenhum peculiaridade relevante de ser descrita.