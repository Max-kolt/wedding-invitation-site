from pydantic_settings import BaseSettings
from dotenv import load_dotenv
load_dotenv()


class DatabaseConfig(BaseSettings):
    DB_HOST: str
    DB_PORT: int
    DB_NAME: str
    DB_USER: str
    DB_PASSWORD: str


database_config = DatabaseConfig()
