from pydantic_settings import BaseSettings
from dotenv import load_dotenv
from loguru import logger
load_dotenv()


class DatabaseConfig(BaseSettings):
    DB_HOST: str
    DB_PORT: int
    DB_NAME: str
    DB_USER: str
    DB_PASSWORD: str


database_config = DatabaseConfig()


logger.add(
    'logs/log_{time:YYYY-MM-DD}.log', rotation="50 MB", compression="gz", level="INFO", diagnose=False,
    backtrace=False, colorize=True
)
