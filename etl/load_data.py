import pandas as pd
from data.database.database_connection import DatabaseConnectionFactory

factory = DatabaseConnectionFactory()
engine = factory.get_engine()

tables = [
    "orders",
    "customers",
    "order_items",
    "order_payments",
    "order_reviews",
    "products",
    "sellers",
]

for table in tables:
    df = pd.read_sql(f"SELECT * FROM {table}", engine)
    df.to_csv(f"data/staging/{table}.csv", index=False)
