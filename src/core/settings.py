from pydantic import BaseSettings
from functools import lru_cache
import os


class Settings(BaseSettings):
    APP_NAME: str = "QUOTERA"
    ENV: str = "DEV"

    class Config:
        env_file = os.getenv("ENV_FILE") or ".env.dev"


@lru_cache()
def get_settings():
    return Settings()
