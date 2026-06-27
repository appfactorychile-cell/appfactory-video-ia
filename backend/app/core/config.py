from functools import lru_cache

from pydantic import BaseModel


class Settings(BaseModel):
    app_name: str = "APP FACTORY VIDEO IA"
    version: str = "0.1.0"
    environment: str = "local"
    api_prefix: str = "/api"
    mock_mode: bool = True


@lru_cache
def get_settings() -> Settings:
    return Settings()
