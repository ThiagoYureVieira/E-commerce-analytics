from sqlalchemy import create_engine
from urllib.parse import quote
import pandas as pd
from dotenv import load_dotenv
import os

load_dotenv(".env.local")

db_name = os.getenv("DATABASE_NAME")
db_pass = quote(os.getenv("DATABASE_PASSWORD"))
db_user = os.getenv("DATABASE_USER")
con_url = f"postgresql+psycopg2://{db_user}:{db_pass}@localhost:5432/{db_name}"

engine = create_engine(
    con_url
)

files_list = ["customers", "orders", "sellers", "products", "order_items", "order_payments", "order_reviews"]

for file in files_list:
    csv_data = pd.read_csv(f"data/raw/{file}.csv")
    csv_data.to_sql(
        f"{file}",
        engine,
        if_exists='append',
        index=False
    )