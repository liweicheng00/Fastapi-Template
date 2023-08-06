import os
from pydantic import BaseSettings


class MongoSettings(BaseSettings):
    mongodb_db: str = os.getenv('MONGODB_DB')
    mongodb_host: str = os.getenv('MONGODB_HOST')
    mongodb_user: str = os.getenv('MONGODB_USER')
    mongodb_password: str = os.getenv('MONGODB_PASSWORD')
    mongodb_ca_cert: str = os.getenv('MONGODB_CA_CERT')
