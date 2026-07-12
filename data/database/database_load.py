import pandas as pd
from database_connection import DatabaseConnectionFactory

factory = DatabaseConnectionFactory()
engine = factory.get_engine()

files_list = ["customers", "orders", "sellers", "products", "order_items", "order_payments", "order_reviews"]

for file in files_list:
    csv_data = pd.read_csv(f"data/raw/{file}.csv")
    csv_data.to_sql(
        f"{file}",
        engine,
        if_exists='append',
        index=False
    )