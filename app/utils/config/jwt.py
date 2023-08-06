import os
from pydantic import BaseSettings


class JwtTokenSettings(BaseSettings):
    access_token_secret_key: str = os.getenv("ACCESS_TOKEN_SECRET_KEY")
    access_token_expire_minutes: int
    audience: str
    issuer: str
