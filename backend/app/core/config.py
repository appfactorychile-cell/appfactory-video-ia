from functools import lru_cache
import os
from pathlib import Path

from pydantic import BaseModel


def _load_local_env() -> None:
    candidates = [
        Path(__file__).resolve().parents[3] / ".env",
        Path(__file__).resolve().parents[4] / ".env",
    ]
    for path in candidates:
        if not path.exists():
            continue
        for line in path.read_text(encoding="utf-8").splitlines():
            value = line.strip()
            if not value or value.startswith("#") or "=" not in value:
                continue
            key, raw = value.split("=", 1)
            os.environ.setdefault(key.strip(), raw.strip().strip('"').strip("'"))


class Settings(BaseModel):
    app_name: str = "APP FACTORY VIDEO IA"
    version: str = "0.1.0"
    environment: str = "local"
    api_prefix: str = "/api"
    mock_mode: bool = False
    database_url: str = "postgresql+psycopg://appfactory:change_me@localhost:5432/app_factory_video_ia"
    secret_key: str = "change_me_local_only"


@lru_cache
def get_settings() -> Settings:
    _load_local_env()
    return Settings(
        app_name=os.getenv("APP_NAME", "APP FACTORY VIDEO IA"),
        environment=os.getenv("APP_ENV", "local"),
        database_url=os.getenv("DATABASE_URL", "postgresql+psycopg://appfactory:change_me@localhost:5432/app_factory_video_ia"),
        secret_key=os.getenv("SECRET_KEY", "change_me_local_only"),
    )
