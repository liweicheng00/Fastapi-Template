import os
from pydantic import BaseSettings


class RedisSettings(BaseSettings):
    redis_host: str = os.getenv('O2_REDIS_HOST')
    redis_port: str = os.getenv('O2_REDIS_PORT')
    db_index: int 
