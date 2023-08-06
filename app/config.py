import os
from typing import Optional, Union
from pydantic import BaseSettings, HttpUrl

from app.utils.config.postgressql import PostgreSettings


class Settings(PostgreSettings, BaseSettings):
    runtime_env: str = os.getenv('RUNTIME_ENV')
    docs_url: Optional[str] = None
    trusted_hosts: list
    origins: list = []

    frontend_domain: Optional[HttpUrl]

    slack_notification_webhook: str = ""


RUNTIME_ENV = os.getenv('RUNTIME_ENV')
if RUNTIME_ENV == 'production':
    settings = Settings()
elif RUNTIME_ENV == 'rc':
    settings = Settings()
elif RUNTIME_ENV == 'hotfix':
    settings = Settings()
elif RUNTIME_ENV == 'demo':
    settings = Settings()
elif RUNTIME_ENV == 'test':
    settings = Settings()
else:
    settings = Settings(
        trusted_hosts=["localhost:8000", "localhost"]
    )
