from sqlalchemy import create_engine
from urllib.parse import quote_plus
from dotenv import load_dotenv
import os

load_dotenv(".env.local")

class DatabaseConfig:
    def __init__(self):
        self.db_name = os.getenv("DATABASE_NAME")
        self.db_user = os.getenv("DATABASE_USER")
        self.db_password = os.getenv("DATABASE_PASSWORD")
        self.host = os.getenv("DATABASE_HOST", "localhost")
        self.port = os.getenv("DATABASE_PORT", "5432")

    def get_connection_url(self):
        password = quote_plus(self.db_password or "")
        return f"postgresql+psycopg2://{self.db_user}:{password}@{self.host}:{self.port}/{self.db_name}"

class DatabaseConnectionFactory:
    def __init__(self):
        self._config = DatabaseConfig()
        self._engine = None

    def get_engine(self):
        if self._engine is None:
            self._engine = create_engine(self._config.get_connection_url())
        return self._engine