# Data Understanding

## Visão geral das tabelas

- orders: pedidos realizados
- order_payments: informações de pagamento
- order_reviews: avaliações dos clientes nos pedidos
- order_items: itens vendidos por pedido
- customers: clientes que realizam pedidos
- cities: informação de geolocalização das cidades com latitude e longitude
- products: catálogo de produtos
- product_category_name_translation: a tradução do nome das categorias dos produtos
- sellers: lojas que realizam as vendas

## Relações

- orders se conecta com customers via customer_id
- order_items se conecta com orders via order_id
- order_items se conecta com products via product_id
- order_items se conecta com sellers via seller_id
- order_payments se conecta com order via order_id
- order_reviews se conecta com order via order_id
- customers se conecta com cities através da coluna customer_zip_code_prefix