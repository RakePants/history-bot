import logging
from pathlib import Path

from pydantic_settings import BaseSettings

logging.basicConfig(
    format="%(asctime)s - %(levelname)s - %(message)s",
    level=logging.INFO,
)

BASE_DIR = Path(__file__).parent


class Settings(BaseSettings):
    bot_token: str
    pinecone_api_key: str
    pinecone_host: str
    pinecone_namespace: str

    class Config:
        extra = "ignore"


settings = Settings()
