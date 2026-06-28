from sqlalchemy import create_engine

from app.core.config import get_settings

settings = get_settings()
connect_args = {}
if settings.database_url.startswith("postgresql"):
    connect_args["connect_timeout"] = 5

engine = create_engine(settings.database_url, pool_pre_ping=True, future=True, connect_args=connect_args)
