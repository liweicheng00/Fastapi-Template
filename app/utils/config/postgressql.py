import os
from pydantic import BaseSettings


class PostgreSettings(BaseSettings):
    POSTGRES_URL: str = os.getenv("POSTGRES_URL")
    POSTGRES_USER: str = os.getenv("POSTGRES_USER")
    POSTGRES_PASSWORD: str = os.getenv("POSTGRES_PASSWORD")
    POSTGRES_DB: str = os.getenv("POSTGRES_DB")
