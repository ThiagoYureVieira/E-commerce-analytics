# E-commerce Analytics

Projeto de análise de dados baseado nos datasets públicos da Olist, disponibilizados no Kaggle. A iniciativa tem como objetivo demonstrar capacidade de análise exploratória, preparação de dados, modelagem analítica e entrega de bases prontas para visualização em Tableau.

## Visão geral

Este repositório organiza o fluxo completo de uma análise de e-commerce, desde a ingestão dos CSVs públicos até a criação de arquivos analíticos prontos para dashboard. O foco está em responder perguntas de negócio relacionadas a:

- performance de vendas;
- categorias e produtos mais lucrativos;
- comportamento de clientes por região;
- eficiência logística e prazo de entrega;
- satisfação do cliente por meio de avaliações;
- relação entre atraso e qualidade percebida.

## Contexto de negócio

O contexto do projeto é uma loja de e-commerce brasileira com operação em múltiplos estados. A análise busca responder como a operação evolui no tempo, quais produtos e regiões geram maior faturamento e como a logística impacta a experiência do cliente.

A base de entendimento de negócio está documentada em [docs/business_understanding.md](docs/business_understanding.md), e as respostas analíticas são construídas a partir dos dados processados na pasta [data/processed](data/processed).

## Dataset utilizado

Os dados provêm dos arquivos públicos da Olist, organizados em múltiplos CSVs de:

- pedidos;
- itens dos pedidos;
- pagamentos;
- clientes;
- vendedores;
- produtos;
- avaliações;
- cidades.

Esses arquivos são usados em diferentes camadas do pipeline:

- [data/raw](data/raw): arquivos originais, sem transformação;
- [data/staging](data/staging): arquivos preparados para carga ou validação inicial;
- [data/processed](data/processed): datasets tratados e prontos para análise;
- [data/output](data/output): bases analíticas exportadas para consumo em dashboards.

Os arquivos contidos na pasta [data/raw](data/raw) foram carregados em um banco de dados local PostgreSQL e posteriormente carregados através do script load_data.py[etl/load_data](etl/load_data.py) apenas para demonstrar um fluxo de trabalho normal do mundo real onde os dados muitas vezes estão armazenada em banco de dados e posteriormente são carregados em csv para evitar sobrecarga de consultas SQL e possíveis travamentos.

## Arquitetura do projeto

A solução foi organizada em etapas bem separadas para manter o processo claro e reproduzível.

### 1. Coleta e ingestão

Os dados são lidos a partir dos arquivos CSV da pasta [data/processed](data/processed). Esse primeiro passo concentra a carga inicial dos dataframes em Python com Pandas.

### 2. Exploração inicial

Os notebooks de EDA, localizados em [notebooks](notebooks), ajudam a entender distribuição, qualidade, valores nulos, colunas relevantes e padrões de negócio. As análises iniciais cobrem:

- pedidos;
- clientes;
- vendedores;
- produtos;
- avaliações;
- itens do pedido;
- pagamentos.

### 3. Preparação analítica

No notebook [notebooks/08_data_preparation.ipynb](notebooks/08_data_preparation.ipynb), o pipeline é organizado em blocos com responsabilidades específicas:

- carregamento dos datasets;
- conversão de campos temporais para `datetime`;
- criação de colunas derivadas para ano, mês, dia, dia da semana e hora;
- cálculo de métricas de logística, como tempo de entrega e atraso;
- agregação de pagamentos, itens e avaliações por pedido;
- joins analíticos entre pedidos, clientes, produtos e vendedores;
- exportação das bases finais em CSV.

### 4. Entrega para dashboards

A preparação final gera duas bases relevantes para visualização no Tableau:

- [data/output/tableau_order_base.csv](data/output/tableau_order_base.csv): base agregada por pedido, ideal para KPIs e visão macro;
- [data/output/tableau_item_base.csv](data/output/tableau_item_base.csv): base detalhada por item, ideal para drill-down por categoria, vendedor e produto.

## Análise realizada

A análise foi estruturada para responder as perguntas definidas em [docs/business_understanding.md](docs/business_understanding.md).

### Perguntas de vendas

- Como evolui a receita ao longo do tempo?
- Quanto foi vendido por mês?
- Quais estados apresentam maior volume de vendas?

### Perguntas de produtos

- Quais categorias geram mais receita?

### Perguntas de clientes

- De quais regiões vêm os clientes?

### Perguntas de logística

- Qual é o tempo médio de entrega?
- Qual é a média de atraso por região?

### Perguntas de avaliação

- Quais categorias possuem piores avaliações?
- Há relação entre atraso e nota?

## KPIs principais

Os indicadores calculados e servidos à análise incluem:

- receita total;
- ticket médio;
- número de pedidos;
- número de clientes;
- tempo médio de entrega;
- taxa de atraso;
- avaliação média.

## Organização dos arquivos do projeto

- [docs/business_understanding.md](docs/business_understanding.md): visão de negócio e perguntas;
- [docs/data_understanding.md](docs/data_understanding.md): entendimento de schema e colunas;
- [docs/insights.md](docs/insights.md): observações e achados da análise;
- [notebooks](notebooks): notebooks de exploração e preparação;
- [etl](etl): módulos de limpeza e carga;
- [data/output](data/output): datasets prontos para dashboards.

## Como repetir a análise

A seguir está o processo recomendado para reproduzir a análise do zero.

### Pré-requisitos

- Python 3.10+;
- dependências listadas em [requirements.txt](requirements.txt);
- acesso local à pasta do projeto.

### Passo 1: preparar o ambiente

Instale as dependências com:

```bash
pip install -r requirements.txt
```

### Passo 2: verificar os dados de entrada

Confirme se os arquivos públicos da Olist estão disponíveis em [data/raw](data/raw) e se os dados processados já foram gerados em [data/processed](data/processed).

### Passo 3: executar a exploração inicial

Abra e execute os notebooks em ordem:

1. [notebooks/01_eda_orders.ipynb](notebooks/01_eda_orders.ipynb)
2. [notebooks/02_eda_customers.ipynb](notebooks/02_eda_customers.ipynb)
3. [notebooks/03_eda_sellers.ipynb](notebooks/03_eda_sellers.ipynb)
4. [notebooks/04_eda_products.ipynb](notebooks/04_eda_products.ipynb)
5. [notebooks/05_eda_order_reviews.ipynb](notebooks/05_eda_order_reviews.ipynb)
6. [notebooks/06_eda_order_items.ipynb](notebooks/06_eda_order_items.ipynb)
7. [notebooks/07_eda_order_payments.ipynb](notebooks/07_eda_order_payments.ipynb)
8. [notebooks/08_data_preparation.ipynb](notebooks/08_data_preparation.ipynb)

### Passo 4: validar a base preparada

Ao final da execução, verifique se os arquivos em [data/output](data/output) foram gerados corretamente. Eles devem incluir:

- `orders_customer_financial_analytics.csv`
- `orders_customer_product_seller_full.csv`
- `orders_temporal_features.csv`
- `tableau_order_base.csv`
- `tableau_item_base.csv`

### Passo 5: usar a base no Tableau

- Use a base de pedido para indicadores macro;
- use a base por item para drill-down por categoria, produto e vendedor;
- aplique filtros de data, estado, categoria e status de entrega.

## Resultado esperado

O projeto entrega uma base analítica bem organizada, com dados temporais enriquecidos, joins de negócio realizados e arquivos exportados prontos para visualização em Tableau. Isso permite responder de forma consistente as perguntas de negócio e montar painéis com foco em vendas, logística, clientes e avaliação.

## Observações finais

A arquitetura foi pensada para ser simples, clara e reutilizável. Caso alguém queira evoluir a análise, o próximo passo natural é:

- adicionar novas métricas de negócio;
- criar uma camada adicional de modelagem preditiva para churn ou previsão de demanda.

