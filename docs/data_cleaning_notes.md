
JUSTIFICATIVA DOS NULOS ESPERADOS NO MODELO DE NEGÓCIO:

1. **order_approved_at e derivadas (approval_year, approval_month, approval_day)**
   - ~160 registros nulos
   - Motivo: Pedidos cancelados ou com erro de processamento não têm data de aprovação
   - Impacto: Filtros no Tableau devem ignorar nulos ou criar categoria "Sem aprovação"

2. **order_delivered_carrier_date e derivadas**
   - ~1783 registros nulos
   - Motivo: Pedidos cancelados ou ainda não enviados não têm data de coleta pela transportadora
   - Impacto: Esperado em pedidos com status "Canceled" ou "Processing"

3. **order_delivered_customer_date, delivery_days, delay_days e derivadas**
   - ~2965-3229 registros nulos
   - Motivo: Pedidos não entregues (cancelados, devolvidos ou em trânsito) não têm data de entrega
   - Impacto: KPIs de entrega devem filtrar estes registros ou calcular médias excluindo nulos

4. **items_quantity, total_price, total_freight**
   - ~775 registros nulos
   - Motivo: Estes registros provavelmente correspondem a pedidos sem itens (erro de dados ou cancelamento)
   - Impacto: Devem ser investigados ou excluídos de análises de receita

5. **review_score_mean, review_score_max, review_score_min, review_count**
   - ~768-961 registros nulos
   - Motivo: Nem todos os pedidos recebem avaliação de cliente
   - Impacto: Análises de satisfação devem filtrar registros com avaliação disponível

6. **payment_total, payment_methods_count, payment_types**
   - ~1 registro nulo
   - Motivo: Exceção, provavelmente dado corrompido ou cancelado antes do pagamento
   - Impacto: Investigue manualmente ou trate como caso especial

RECOMENDAÇÕES PARA DASHBOARD NO TABLEAU:
- Use filtros com "Include null values" apenas para análises exploratórias
- Para KPIs críticos, crie uma métrica calculada que exclua nulos: SUM(revenue) / COUNT(IF NOT NULL(revenue))
- Crie dimensões booleanas para status de entrega, pagamento e avaliação para facilitar drilldown
